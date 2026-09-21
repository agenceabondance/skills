#!/usr/bin/env python3
"""Lecture de brevets sur Google Patents, sans dependance hors bibliotheque standard.

Usage :
  py brevet.py US9031929B1                 # extrait le texte complet dans cache/US9031929B1.txt
  py brevet.py https://patents.google.com/patent/US9031929B1/en
  py brevet.py US9031929B1 --meta          # affiche seulement l'en-tete (deposant, dates, statut)
  py brevet.py --chercher "site quality"   # cherche des brevets Google sur ce sujet
  py brevet.py --chercher "site quality" --tous   # sans filtrer sur le deposant Google

Sur Mac : python3 a la place de py.

Le fichier extrait contient, dans l'ordre : l'en-tete, l'abrege, les revendications
numerotees (les dependantes sont marquees), la description en paragraphes numerotes,
puis les brevets cites et citants. Il sert de matiere a la redaction de la fiche ;
il n'est pas versionne (dossier cache/ ignore par git).
"""
import html
import json
import os
import re
import sys
import urllib.parse
import urllib.request

UA = "Mozilla/5.0 (compatible; Abondance seo-local; +https://www.abondance.com)"
DEPOSANTS_GOOGLE = ("google inc", "google llc", "google technology holdings")
CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache")

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def telecharger(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8", errors="replace")


def numero_depuis(arg):
    m = re.search(r"patent/([A-Z]{2}[0-9A-Z]+)", arg)
    if m:
        return m.group(1)
    return arg.strip().upper().replace(" ", "").replace(",", "")


def texte(fragment):
    fragment = re.sub(r"<br\s*/?>", "\n", fragment)
    fragment = re.sub(r"</(p|div|li|h[1-6]|heading)>", "\n", fragment)
    fragment = re.sub(r"<[^>]+>", " ", fragment)
    fragment = html.unescape(fragment)
    fragment = re.sub(r"[ \t]+", " ", fragment)
    fragment = re.sub(r"\n\s*\n+", "\n", fragment)
    return fragment.strip()


def section(h, nom):
    m = re.search(r'<section itemprop="%s".*?</section>' % nom, h, re.S)
    return m.group(0) if m else ""


def meta(h, numero):
    d = {"numero": numero}
    m = re.search(r'<meta name="DC.title" content="([^"]*)"', h)
    d["titre"] = html.unescape(m.group(1)).strip() if m else ""
    contrib = [html.unescape(x).strip() for x in re.findall(r'<meta name="DC.contributor" content="([^"]*)"', h)]
    # Le deposant est le dernier contributeur, les inventeurs les precedent.
    d["inventeurs"] = contrib[:-1] if len(contrib) > 1 else contrib
    d["deposant"] = contrib[-1] if contrib else ""
    for cle, prop in (("priorite", "priorityDate"), ("depot", "filingDate"),
                      ("publication", "publicationDate"), ("expiration", "expiration")):
        m = re.search(r'<time itemprop="%s" datetime="([^"]*)"' % prop, h)
        d[cle] = m.group(1) if m else ""
    m = re.search(r'itemprop="ifiStatus">([^<]*)', h)
    d["statut_ifi"] = m.group(1).strip() if m else ""
    # Delivre (B1/B2) ou simple demande publiee (A1) : le suffixe du numero le dit.
    d["type_publication"] = "brevet delivre" if re.search(r"B\d$", numero) else "demande publiee"
    m = re.search(r'itemprop="applicationNumber">([^<]*)', h)
    d["numero_demande"] = m.group(1).strip() if m else ""
    m = re.search(r'<section itemprop="abstract".*?</section>', h, re.S)
    d["abrege"] = texte(m.group(0)).replace("Abstract", "", 1).strip() if m else ""
    # Chronologie : depot, publication, delivrance, expiration ajustee. Une demande (A1)
    # delivree depuis porte ici le numero du brevet delivre.
    d["chronologie"] = []
    d["delivre_sous"] = ""
    for x in re.findall(r'<dd itemprop="events".*?</dd>', h, re.S):
        dt = re.search(r'datetime="([^"]*)"', x)
        ti = re.search(r'itemprop="title">([^<]*)', x)
        if not ti:
            continue
        titre_ev = html.unescape(ti.group(1)).strip()
        d["chronologie"].append("%s %s" % (dt.group(1) if dt else "?", titre_ev))
        mg = re.match(r"Publication of (US\d+B\d)", titre_ev)
        if mg and mg.group(1) != numero:
            d["delivre_sous"] = "%s (%s)" % (mg.group(1), dt.group(1) if dt else "?")
    return d


def est_google(deposant):
    # "Google Inc.", "Google, Inc", "Google LLC" : on normalise la ponctuation avant de comparer.
    d = re.sub(r"[^a-z ]", "", deposant.lower())
    d = re.sub(r"s+", " ", d).strip()
    return d in DEPOSANTS_GOOGLE


def revendications(h):
    s = section(h, "claims")
    if not s:
        return []
    # Une revendication = <div id="CLM-00002" num="00002" class="claim">, enveloppee dans
    # <div class="claim-dependent"> quand elle depend d'une autre.
    out = []
    morceaux = re.split(r'(?=<div id="CLM-\d+")', s)
    for i, chunk in enumerate(morceaux[1:], 1):
        precedent = morceaux[i - 1][-80:]
        dep = 'class="claim-dependent"' in precedent
        t = re.sub(r"\s+", " ", texte(chunk))
        if t:
            out.append((dep, t))
    if not out:
        # Balisage different : on retombe sur le texte brut de la section.
        out = [(False, texte(s))]
    return out


def description(h):
    s = section(h, "description")
    if not s:
        return [], []
    paras = []
    # Un paragraphe = <div id="p-0002" num="0001" class="description-paragraph">, les titres
    # de sections sont des <heading>. On garde l'ordre d'apparition des deux.
    for m in re.finditer(r'<div id="p-\d+" num="(\d+)" class="description-(?:paragraph|line)">(.*?)</div>|<heading[^>]*>(.*?)</heading>', s, re.S):
        if m.group(3) is not None:
            t = re.sub(r"\s+", " ", texte(m.group(3)))
            if t:
                paras.append(("titre", t))
            continue
        t = re.sub(r"\s+", " ", texte(m.group(2)))
        if t:
            paras.append((m.group(1).lstrip("0") or "0", t))
    titres = [t for k, t in paras if k == "titre"]
    if not [p for p in paras if p[0] != "titre"]:
        paras = [("", p) for p in texte(s).split("\n") if p.strip()]
    return paras, titres


def references(h, nom):
    rows = re.findall(r'<tr itemprop="%s"[^>]*>(.*?)</tr>' % nom, h, re.S)
    out = []
    for r in rows:
        num = re.search(r'itemprop="publicationNumber">([^<]*)', r)
        tit = re.search(r'itemprop="title">([^<]*)', r)
        ass = re.search(r'itemprop="assigneeOriginal">([^<]*)', r)
        dat = re.search(r'itemprop="priorityDate">([^<]*)', r)
        if num:
            out.append((num.group(1).strip(), (tit.group(1).strip() if tit else ""),
                        (ass.group(1).strip() if ass else ""), (dat.group(1).strip() if dat else "")))
    return out


def extraire(numero, seulement_meta=False):
    url = "https://patents.google.com/patent/%s/en" % numero
    h = telecharger(url)
    d = meta(h, numero)
    if not d["titre"]:
        print("Brevet introuvable : %s" % url)
        sys.exit(2)
    google = est_google(d["deposant"])
    print("%s | %s" % (d["numero"], d["titre"]))
    print("Deposant : %s%s" % (d["deposant"], "" if google else "   <-- PAS GOOGLE : hors perimetre sauf validation explicite"))
    print("Inventeurs : %s" % ", ".join(d["inventeurs"]))
    print("Priorite %s | depot %s | publication %s | expiration %s" % (d["priorite"], d["depot"], d["publication"], d["expiration"] or "-"))
    print("Statut : %s (%s%s)" % (d["statut_ifi"] or "?", d["type_publication"],
                                   ", delivree depuis sous " + d["delivre_sous"] if d["delivre_sous"] else ""))
    if seulement_meta:
        for ev in d["chronologie"]:
            print("  " + ev)
        return
    claims = revendications(h)
    paras, titres = description(h)
    cites = references(h, "backwardReferencesOrig") or references(h, "backwardReferences")
    citants = references(h, "forwardReferencesOrig") or references(h, "forwardReferences")
    os.makedirs(CACHE, exist_ok=True)
    chemin = os.path.join(CACHE, numero + ".txt")
    with open(chemin, "w", encoding="utf-8") as f:
        f.write("# %s - %s\n" % (d["numero"], d["titre"]))
        f.write("url: %s\n" % url)
        for k in ("deposant", "priorite", "depot", "publication", "expiration", "statut_ifi", "type_publication", "numero_demande"):
            f.write("%s: %s\n" % (k, d[k]))
        f.write("inventeurs: %s\n" % ", ".join(d["inventeurs"]))
        f.write("deposant_google: %s\n\n" % ("oui" if google else "NON"))
        f.write("## Abrege\n%s\n\n" % d["abrege"])
        f.write("## Revendications (%d)\n" % len(claims))
        for i, (dep, t) in enumerate(claims, 1):
            f.write("[%d%s] %s\n\n" % (i, " dependante" if dep else " INDEPENDANTE", t))
        n_paras = sum(1 for k, _ in paras if k != "titre")
        f.write("## Description (%d paragraphes)\n" % n_paras)
        if titres:
            f.write("Titres de sections : %s\n\n" % " | ".join(titres))
        for num, t in paras:
            if num == "titre":
                f.write("### %s\n\n" % t)
            else:
                f.write("[%s] %s\n\n" % (num or "-", t))
        f.write("## Brevets cites (%d)\n" % len(cites))
        for n, t, a, dt in cites:
            f.write("- %s | %s | %s | %s\n" % (n, t, a, dt))
        f.write("\n## Brevets citants (%d)\n" % len(citants))
        for n, t, a, dt in citants:
            f.write("- %s | %s | %s | %s\n" % (n, t, a, dt))
    n_indep = sum(1 for dep, _ in claims if not dep)
    print("Extrait dans %s : %d revendications (%d independantes), %d paragraphes, %d cites, %d citants"
          % (chemin, len(claims), n_indep, n_paras, len(cites), len(citants)))


def chercher(terme, tous=False, nombre=20):
    q = "q=%s" % urllib.parse.quote_plus(terme)
    if not tous:
        q += "&assignee=" + urllib.parse.quote_plus("Google LLC") + "&assignee=" + urllib.parse.quote_plus("Google Inc")
    q += "&num=%d" % nombre
    url = "https://patents.google.com/xhr/query?url=%s&exp=" % urllib.parse.quote(q, safe="")
    data = json.loads(telecharger(url))
    res = data.get("results", {})
    print("%s resultats pour \"%s\"%s (les %d premiers)" % (
        res.get("total_num_results", "?"), terme, "" if tous else " chez Google", nombre))
    print("numero | priorite | publie | deposant | titre")
    for cluster in res.get("cluster", []):
        for r in cluster.get("result", []):
            p = r.get("patent", {})
            print("%s | %s | %s | %s | %s" % (
                p.get("publication_number", ""), p.get("priority_date", ""),
                p.get("publication_date", ""), texte(p.get("assignee", "")), texte(p.get("title", ""))))


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0)
    if args[0] == "--chercher":
        if len(args) < 2:
            print("Il manque le terme a chercher.")
            sys.exit(1)
        chercher(args[1], tous="--tous" in args)
    else:
        extraire(numero_depuis(args[0]), seulement_meta="--meta" in args)
