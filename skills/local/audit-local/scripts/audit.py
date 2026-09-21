#!/usr/bin/env python3
"""Pre-remplit la partie "donnees" d'un audit de fiches Google a partir d'un CSV, sans dependance.

Deux entrees possibles :
  - le CSV produit par places.py (pack ou reseau) : client + concurrents, donnee publique ;
  - un export de l'interface Fiche d'etablissement (Profil > Telecharger les informations
    sur les etablissements, ou l'export en masse d'un groupe) : les fiches du client seules,
    avec les champs que Places ne donne pas (categories secondaires, description, code magasin).

Usage :
  py audit.py places sortie-places/places-pack-XXXX.csv --client "ma marque" [--out audit-donnees.md]
      -> par requete x ville : le pack, la position du client, son ecart a la mediane
         (note, avis, photos), et les alertes de conformite lisibles depuis l'exterieur
  py audit.py places sortie-places/places-reseau-XXXX.csv --client "ma marque"
      -> inventaire d'un reseau : fiches fermees, sans site, sans horaires, doublons de nom,
         categories heterogenes
  py audit.py gbp export-fiches.csv [--out audit-donnees.md]
      -> memes controles de completude sur un export de l'interface (colonnes reconnues en
         francais et en anglais ; les colonnes absentes sont signalees, pas devinees)

--client est une expression reguliere (insensible a la casse) testee sur le nom de la fiche.

Le fichier produit est du markdown a coller dans la section 4 et 5 du livrable
(grille/gabarit-livrable.md, skill audit-local). Il ne rend AUCUN verdict : il aligne les chiffres et
signale ce qui merite un oeil. Le verdict par famille reste un travail de lecture.

Sur Mac : python3 a la place de py.
"""
import argparse
import csv
import re
import statistics
import sys
from collections import Counter, defaultdict

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


# --------------------------------------------------------------------------- lecture
def lire_csv(chemin):
    with open(chemin, encoding="utf-8-sig", newline="") as f:
        echantillon = f.read(4096)
        f.seek(0)
        try:
            dialecte = csv.Sniffer().sniff(echantillon, delimiters=";,\t")
        except csv.Error:
            dialecte = csv.excel
        lignes = list(csv.DictReader(f, dialect=dialecte))
    # Les valeurs viennent de tiers (noms de fiches, adresses ecrits par n'importe qui) et sont
    # recopiees dans du markdown : on neutralise ce qui casserait un tableau ou injecterait du HTML.
    return [{k: neutraliser(v) for k, v in l.items()} for l in lignes]


def neutraliser(v):
    if v is None:
        return ""
    v = str(v).replace("|", r"\|").replace("<", "&lt;").replace(">", "&gt;")
    return " ".join(v.split())


def nombre(v):
    try:
        return float(str(v).replace(",", "."))
    except (TypeError, ValueError):
        return None


# Correspondance des colonnes d'un export de l'interface Fiche d'etablissement vers nos noms.
# Les intitules varient selon la langue de l'interface et la version : on reconnait par
# motif, et on signale ce qu'on n'a pas trouve plutot que de deviner.
COLONNES_GBP = {
    "nom": [r"^(business name|nom de l.établissement|nom)$"],
    "code": [r"store code|code (du )?magasin"],
    "adresse": [r"address line 1|adresse( ligne 1)?$"],
    "ville": [r"^(locality|ville|city)$"],
    "categorie_principale": [r"primary category|catégorie principale"],
    "categories_secondaires": [r"additional categor|catégories supplémentaires"],
    "site": [r"^website|site web"],
    "telephone": [r"primary phone|téléphone principal"],
    "description": [r"^(from the business|description)"],
    "horaires_lundi": [r"monday hours|horaires.*lundi"],
    "statut": [r"^(status|statut|business status)"],
}


def normaliser_gbp(lignes):
    """Rebaptise les colonnes reconnues ; rend aussi la liste des champs non trouves."""
    if not lignes:
        return [], list(COLONNES_GBP)
    entetes = list(lignes[0].keys())
    correspondance, manquants = {}, []
    for cible, motifs in COLONNES_GBP.items():
        trouvee = next((e for e in entetes if any(re.search(m, e.strip(), re.I) for m in motifs)), None)
        if trouvee:
            correspondance[cible] = trouvee
        else:
            manquants.append(cible)
    sortie = []
    for l in lignes:
        sortie.append({cible: l.get(col, "") for cible, col in correspondance.items()})
    return sortie, manquants


# --------------------------------------------------------------------------- controles
MOTS_GENERIQUES = ("stage", "formation", "école", "ecole", "garage", "restaurant", "hôtel", "hotel",
                   "plombier", "avocat", "dentiste", "crèche", "creche", "agence", "magasin",
                   "pas cher", "meilleur", "n°1", "numero 1", "numéro 1")


def alertes_nom(nom, ville=""):
    """Lecture exterieure de la regle sur le nom [02] : mots generiques, ville, majuscules,
    mention legale, caracteres promotionnels. Ce sont des signaux a verifier, pas des verdicts."""
    a = []
    bas = nom.lower()
    if ville and ville.lower() in bas:
        a.append("ville dans le nom (usage courant pour un réseau, à confronter à [02])")
    if any(m in bas for m in MOTS_GENERIQUES):
        a.append("mot generique / service dans le nom")
    if re.search(r"\b(sarl|sas|eurl|sasu|ltd|llc|inc)\b", bas):
        a.append("mention legale dans le nom")
    if len(nom) > 8 and nom.upper() == nom and any(c.isalpha() for c in nom):
        a.append("majuscules integrales")
    if re.search(r"[|®™]|\d{2} \d{2} \d{2}|https?:|www\.", nom):
        a.append("symbole, telephone ou URL dans le nom")
    if " - " in nom or " | " in nom:
        a.append("suffixe apres tiret (a verifier : ville ou slogan ?)")
    return a


def alertes_fiche(l):
    """Completude lisible depuis Places : site, horaires, statut, photos, avis."""
    a = []
    if l.get("statut") and l["statut"] != "OPERATIONAL":
        a.append(f"statut {l['statut']}")
    if not l.get("site"):
        a.append("pas de site")
    if not l.get("horaires"):
        a.append("pas d'horaires")
    if not l.get("telephone"):
        a.append("pas de telephone")
    n_photos = nombre(l.get("nb_photos_max10"))
    if n_photos is not None and n_photos < 3:
        a.append(f"{int(n_photos)} photo(s) vues")
    if l.get("avis_avec_texte_sur_5") and l["avis_avec_texte_sur_5"].startswith(("0/", "1/")):
        a.append(f"avis avec texte {l['avis_avec_texte_sur_5']}")
    return a


def mediane(valeurs):
    v = [x for x in valeurs if x is not None]
    return statistics.median(v) if v else None


def fmt(x, dec=1):
    return "-" if x is None else (f"{x:.{dec}f}" if isinstance(x, float) and dec else f"{int(x)}")


# --------------------------------------------------------------------------- rapports
def rapport_pack(lignes, motif_client):
    est_client = lambda l: bool(re.search(motif_client, l.get("nom", ""), re.I))
    groupes = defaultdict(list)
    for l in lignes:
        groupes[(l.get("requete", ""), l.get("ville", ""))].append(l)
    out = ["## Le pack face aux concurrents (donnees Places, hors position reelle)", "",
           "Source : Text Search Places, sans position d'utilisateur. Lire la presence et les attributs, pas le rang.", ""]
    synthese = []
    for (requete, ville), fiches in groupes.items():
        fiches.sort(key=lambda l: nombre(l.get("rang")) or 99)
        out.append(f"### « {requete} » × {ville or 'sans ville'}")
        out.append("")
        out.append("| Rang | Fiche | Catégorie | Note | Avis | Photos | Avis récent (parmi 5) | Site | Alertes |")
        out.append("|---|---|---|---|---|---|---|---|---|")
        notes, avis, photos = [], [], []
        client, n_reseau = None, 0
        for l in fiches:
            marque = "**" if est_client(l) else ""
            al = alertes_nom(l.get("nom", ""), ville) + alertes_fiche(l)
            out.append(f"| {l.get('rang','')} | {marque}{l.get('nom','')}{marque} | {l.get('categorie_principale','')} | "
                       f"{l.get('note','')} | {l.get('nb_avis','')} | {l.get('nb_photos_max10','')} | {l.get('avis_recent_parmi_5','')} | "
                       f"{'oui' if l.get('site') else 'non'} | {', '.join(al)} |")
            if est_client(l):
                n_reseau += 1
                if client is None:
                    client = l
            else:
                notes.append(nombre(l.get("note")))
                avis.append(nombre(l.get("nb_avis")))
                photos.append(nombre(l.get("nb_photos_max10")))
        out.append("")
        med = (mediane(notes), mediane(avis), mediane(photos))
        if client:
            plusieurs = f" ({n_reseau} fiches du réseau dans le résultat)" if n_reseau > 1 else ""
            out.append(f"Meilleure fiche du client au rang {client.get('rang')}{plusieurs} : note {client.get('note','-')} (médiane concurrents {fmt(med[0])}), "
                       f"{client.get('nb_avis','-')} avis (médiane {fmt(med[1], 0)}), "
                       f"{client.get('nb_photos_max10','-')} photos vues (médiane {fmt(med[2], 0)}).")
            synthese.append((requete, ville, client.get("rang"), client.get("note"), med[0], client.get("nb_avis"), med[1], n_reseau))
        else:
            out.append(f"**Client absent** des {len(fiches)} premiers résultats. Médiane concurrents : note {fmt(med[0])}, {fmt(med[1], 0)} avis.")
            synthese.append((requete, ville, "absent", "", med[0], "", med[1], 0))
        out.append("")
    out.insert(4, "")
    out.insert(4, "| Requête | Ville | Rang client | Fiches réseau | Note client | Note médiane | Avis client | Avis médiane |")
    out.insert(5, "|---|---|---|---|---|---|---|---|")
    for i, s in enumerate(synthese):
        out.insert(6 + i, f"| {s[0]} | {s[1]} | {s[2]} | {s[7]} | {s[3]} | {fmt(s[4])} | {s[5]} | {fmt(s[6], 0)} |")
    return "\n".join(out)


def rapport_reseau(lignes, motif_client):
    fiches = [l for l in lignes if re.search(motif_client, l.get("nom", ""), re.I)]
    autres = len(lignes) - len(fiches)
    out = [f"## Inventaire du réseau (donnees Places) : {len(fiches)} fiche(s) au nom du client, {autres} autre(s) écartée(s)", ""]
    out.append("| Fiche | Adresse | Catégorie | Note | Avis | Statut | Site | Horaires | Alertes |")
    out.append("|---|---|---|---|---|---|---|---|---|")
    noms = Counter()
    for l in fiches:
        al = alertes_nom(l.get("nom", "")) + alertes_fiche(l)
        noms[l.get("nom", "")] += 1
        out.append(f"| {l.get('nom','')} | {l.get('adresse','')} | {l.get('categorie_principale','')} | {l.get('note','')} | "
                   f"{l.get('nb_avis','')} | {l.get('statut','')} | {'oui' if l.get('site') else 'non'} | "
                   f"{'oui' if l.get('horaires') else 'non'} | {', '.join(al)} |")
    out.append("")
    doublons = [n for n, c in noms.items() if c > 1]
    if doublons:
        out.append(f"**Noms en double** (à vérifier : doublon de fiche ou deux lieux ?) : {', '.join(doublons)}")
    cats = Counter(l.get("categorie_principale", "") for l in fiches)
    if len(cats) > 1:
        out.append(f"**Catégories principales hétérogènes** : " + ", ".join(f"{c} ({n})" for c, n in cats.most_common()))
    sans_site = sum(1 for l in fiches if not l.get("site"))
    sans_horaires = sum(1 for l in fiches if not l.get("horaires"))
    out.append(f"Sans site : {sans_site} · sans horaires : {sans_horaires} · "
               f"note médiane {fmt(mediane([nombre(l.get('note')) for l in fiches]))} · "
               f"avis médian {fmt(mediane([nombre(l.get('nb_avis')) for l in fiches]), 0)}")
    return "\n".join(out)


def rapport_gbp(lignes):
    fiches, manquants = normaliser_gbp(lignes)
    out = [f"## Export de l'interface : {len(fiches)} fiche(s)", ""]
    if manquants:
        out.append("Colonnes non trouvées dans l'export (contrôles correspondants à faire à la main) : " + ", ".join(manquants))
        out.append("")
    out.append("| Fiche | Ville | Catégorie principale | Catégories secondaires | Site | Téléphone | Description | Alertes |")
    out.append("|---|---|---|---|---|---|---|---|")
    cats = Counter()
    for l in fiches:
        al = alertes_nom(l.get("nom", ""), l.get("ville", ""))
        if "site" in l and not l.get("site"):
            al.append("pas de site")
        if "telephone" in l and not l.get("telephone"):
            al.append("pas de telephone")
        if "description" in l and not l.get("description"):
            al.append("pas de description")
        if "horaires_lundi" in l and not l.get("horaires_lundi"):
            al.append("pas d'horaires (lundi vide)")
        if "statut" in l and l.get("statut") and l["statut"].lower() not in ("open", "ouvert", "operational", ""):
            al.append(f"statut {l['statut']}")
        cats[l.get("categorie_principale", "")] += 1
        out.append(f"| {l.get('nom','')} | {l.get('ville','')} | {l.get('categorie_principale','')} | "
                   f"{l.get('categories_secondaires','')} | {'oui' if l.get('site') else 'non'} | "
                   f"{'oui' if l.get('telephone') else 'non'} | {'oui' if l.get('description') else 'non'} | {', '.join(al)} |")
    out.append("")
    if len(cats) > 1:
        out.append("**Catégories principales hétérogènes** : " + ", ".join(f"{c or '(vide)'} ({n})" for c, n in cats.most_common()))
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source", choices=["places", "gbp"], help="places = CSV de places.py ; gbp = export de l'interface")
    ap.add_argument("csv")
    ap.add_argument("--client", default="", help="regex sur le nom de la fiche (obligatoire pour places)")
    ap.add_argument("--out", default="", help="fichier markdown de sortie (defaut : affichage)")
    args = ap.parse_args()

    lignes = lire_csv(args.csv)
    if not lignes:
        sys.exit("CSV vide.")
    if args.source == "places":
        if not args.client:
            sys.exit("--client est obligatoire avec un CSV places.")
        if any(l.get("rang") for l in lignes):
            texte = rapport_pack(lignes, args.client)
        else:
            texte = rapport_reseau(lignes, args.client)
    else:
        texte = rapport_gbp(lignes)

    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(texte + "\n")
        print(f"Écrit : {args.out}")
    else:
        print(texte)


if __name__ == "__main__":
    main()
