#!/usr/bin/env python3
"""Photographie des fiches Google (client + concurrents) via Places API (New), sans dependance.

Les donnees Places sont publiques : aucun acces a la fiche du client n'est necessaire,
seulement une cle Google Cloud (Places API (New) activee) dans la variable
d'environnement GOOGLE_PLACES_API_KEY. La cle n'est jamais affichee ni ecrite.

Usage :
  py places.py pack "stage de pilotage" --villes "Le Mans,Nantes" [--n 10]
      -> pour chaque requete x ville, les N premieres fiches du resultat Places
         (equivalent approximatif du pack local, voir "Limites" ci-dessous)
  py places.py pack requetes.txt --villes villes.txt
      -> idem, requetes et villes lues dans des fichiers (une par ligne)
  py places.py reseau "Ma Marque" [--region FR]
      -> toutes les fiches portant ce nom (inventaire d'un reseau, doublons, orphelines)
  py places.py fiche ChIJ...   [ChIJ... ...]
      -> detail complet d'une ou plusieurs fiches (par place_id)

Options communes :
  --out DOSSIER      dossier de sortie (defaut : ./sortie-places)
  --max-appels N     plafond d'appels API pour la session (defaut : 200)
  --lang fr          langue des resultats (defaut : fr)  --region FR (defaut : FR)
  --dry-run          n'appelle pas l'API : affiche les appels qui seraient faits (sans cle)

Sorties (dans --out) :
  places-<commande>-<AAAAMMJJ-HHMM>.csv   table plate, une ligne par fiche
  places-<commande>-<AAAAMMJJ-HHMM>.json  reponses brutes (pour relecture ou reprise)

Sur Mac : python3 a la place de py.

Limites a connaitre :
  - Text Search n'est PAS le pack local : c'est le classement de la recherche Places pour
    la requete, sans la position de l'utilisateur ni la personnalisation. Il sert a
    photographier QUI est present et avec QUELS attributs (note, avis, categorie, photos),
    pas a lire une position. Les positions se lisent dans Monitorank.
  - Places rend au plus 5 avis (les "plus pertinents", pas les plus recents) et 10 photos :
    avis_recent_parmi_5 est une borne basse de la date du dernier avis, nb_photos_max10
    plafonne a 10. Le vrai stock se lit sur la fiche ou dans l'interface.
  - Chaque appel pack ou fiche demande des champs "Enterprise + Atmosphere" (note, avis,
    photos, site, telephone, horaires) : SKU le plus cher de Places, avec un quota gratuit
    mensuel limite (de l'ordre de 1 000 appels, a verifier sur la tarification Google).
    Le compteur d'appels et le plafond --max-appels sont la pour ca.
"""
import argparse
import csv
import datetime as dt
import json
import os
import sys
import urllib.error
import urllib.request

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

API_TEXT = "https://places.googleapis.com/v1/places:searchText"
API_DETAILS = "https://places.googleapis.com/v1/places/"

# Champs demandes. Le FieldMask determine le SKU facture : ces champs tombent dans
# "Enterprise + Atmosphere" (avis, note, photos). Ne pas en ajouter sans raison.
CHAMPS_FICHE = [
    "id", "displayName", "primaryType", "primaryTypeDisplayName", "types",
    "formattedAddress", "location", "businessStatus", "googleMapsUri",
    "websiteUri", "nationalPhoneNumber", "regularOpeningHours",
    "rating", "userRatingCount", "photos", "reviews", "editorialSummary",
]
CHAMPS_PACK = ["places." + c for c in CHAMPS_FICHE]


# --------------------------------------------------------------------------- cle
def cle_api():
    """Lit la cle dans l'environnement ; sur Windows, retombe sur la variable utilisateur
    du registre (setx n'est visible que par les processus lances apres coup)."""
    cle = os.environ.get("GOOGLE_PLACES_API_KEY")
    if cle:
        return cle
    if sys.platform == "win32":
        try:
            import winreg
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment") as k:
                cle, _ = winreg.QueryValueEx(k, "GOOGLE_PLACES_API_KEY")
                if cle:
                    return cle
        except OSError:
            pass
    sys.exit("Cle absente : definir GOOGLE_PLACES_API_KEY (setx sous Windows, export sur Mac), "
             "puis relancer le terminal.")


# --------------------------------------------------------------------------- appels
class Compteur:
    def __init__(self, plafond):
        self.plafond = plafond
        self.n = 0

    def tick(self):
        self.n += 1
        if self.n > self.plafond:
            sys.exit(f"Plafond de {self.plafond} appels atteint : arret. "
                     f"Relancer avec --max-appels plus haut si c'est voulu.")


DRY_RUN = False


def appel(url, cle, champs, corps=None, compteur=None):
    """Un appel Places API (New). POST pour searchText, GET pour un detail."""
    if compteur:
        compteur.tick()
    if DRY_RUN:
        print(f"  [dry-run] {'POST' if corps is not None else 'GET'} {url.split('/v1/')[-1]} "
              f"{json.dumps(corps, ensure_ascii=False) if corps is not None else ''}")
        return {"places": []}
    entetes = {
        "X-Goog-Api-Key": cle,
        "X-Goog-FieldMask": ",".join(champs),
        "Content-Type": "application/json",
    }
    donnees = json.dumps(corps).encode("utf-8") if corps is not None else None
    req = urllib.request.Request(url, data=donnees, headers=entetes,
                                 method="POST" if corps is not None else "GET")
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", errors="replace")[:600]
        sys.exit(f"Erreur HTTP {e.code} sur {url.split('/v1/')[-1]} : {detail}")


def recherche_texte(cle, texte, compteur, lang, region, n):
    corps = {"textQuery": texte, "languageCode": lang, "regionCode": region,
             "pageSize": min(max(n, 1), 20)}
    rep = appel(API_TEXT, cle, CHAMPS_PACK, corps, compteur)
    return rep.get("places", [])


def detail_fiche(cle, place_id, compteur, lang, region):
    url = f"{API_DETAILS}{place_id}?languageCode={lang}&regionCode={region}"
    return appel(url, cle, CHAMPS_FICHE, None, compteur)


# --------------------------------------------------------------------------- aplatissement
def texte_local(champ):
    """Un champ localise Places est {"text": ..., "languageCode": ...}."""
    if isinstance(champ, dict):
        return champ.get("text", "")
    return champ or ""


def aplatir(p, requete="", ville="", rang=""):
    """Une fiche Places -> une ligne plate pour le CSV. Les champs absents restent vides :
    l'absence est une information (pas de site, pas d'horaires...)."""
    avis = p.get("reviews", []) or []
    dates_avis = sorted([a.get("publishTime", "") for a in avis if a.get("publishTime")], reverse=True)
    avec_texte = sum(1 for a in avis if texte_local(a.get("text")).strip())
    reponses = sum(1 for a in avis if a.get("ownerResponse") or a.get("authorAttribution", {}).get("ownerResponse"))
    horaires = p.get("regularOpeningHours", {}) or {}
    return {
        "requete": requete,
        "ville": ville,
        "rang": rang,
        "place_id": p.get("id", ""),
        "nom": texte_local(p.get("displayName")),
        "categorie_principale": texte_local(p.get("primaryTypeDisplayName")) or p.get("primaryType", ""),
        "type_principal": p.get("primaryType", ""),
        "types": "|".join(p.get("types", []) or []),
        "note": p.get("rating", ""),
        "nb_avis": p.get("userRatingCount", ""),
        "adresse": p.get("formattedAddress", ""),
        "telephone": p.get("nationalPhoneNumber", ""),
        "site": p.get("websiteUri", ""),
        "statut": p.get("businessStatus", ""),
        "horaires": " ; ".join(horaires.get("weekdayDescriptions", []) or []),
        "nb_photos_max10": len(p.get("photos", []) or []),
        "avis_recent_parmi_5": dates_avis[0][:10] if dates_avis else "",
        "avis_avec_texte_sur_5": f"{avec_texte}/{len(avis)}" if avis else "",
        "description_editoriale": texte_local(p.get("editorialSummary")),
        "lat": (p.get("location") or {}).get("latitude", ""),
        "lng": (p.get("location") or {}).get("longitude", ""),
        "maps": p.get("googleMapsUri", ""),
    }


# --------------------------------------------------------------------------- commandes
def lire_liste(arg):
    """Un argument est soit une liste separee par des virgules, soit un chemin de fichier
    (une valeur par ligne)."""
    if arg and os.path.isfile(arg):
        with open(arg, encoding="utf-8") as f:
            return [l.strip() for l in f if l.strip() and not l.startswith("#")]
    return [x.strip() for x in (arg or "").split(",") if x.strip()]


def cmd_pack(args, cle, compteur):
    requetes = lire_liste(args.requete)
    villes = lire_liste(args.villes) or [""]
    lignes, brut = [], []
    for requete in requetes:
        for ville in villes:
            texte = f"{requete} {ville}".strip()
            places = recherche_texte(cle, texte, compteur, args.lang, args.region, args.n)
            brut.append({"requete": requete, "ville": ville, "texte": texte, "places": places})
            for i, p in enumerate(places[: args.n], start=1):
                lignes.append(aplatir(p, requete, ville, i))
            print(f"  {texte!r} : {len(places)} fiches")
    return lignes, brut


def cmd_reseau(args, cle, compteur):
    """Inventaire des fiches portant un nom de marque : Text Search sur le nom seul, puis
    sur le nom + chaque ville optionnelle, dedoublonne par place_id."""
    vus, lignes, brut = {}, [], []
    textes = [args.nom] + [f"{args.nom} {v}" for v in lire_liste(args.villes)]
    for texte in textes:
        places = recherche_texte(cle, texte, compteur, args.lang, args.region, 20)
        brut.append({"texte": texte, "places": places})
        for p in places:
            if p.get("id") in vus:
                continue
            vus[p["id"]] = True
            lignes.append(aplatir(p, requete=args.nom, ville=texte.replace(args.nom, "").strip()))
        print(f"  {texte!r} : {len(places)} fiches, {len(vus)} distinctes au total")
    return lignes, brut


def cmd_fiche(args, cle, compteur):
    lignes, brut = [], []
    for pid in args.place_ids:
        p = detail_fiche(cle, pid, compteur, args.lang, args.region)
        brut.append(p)
        lignes.append(aplatir(p))
        print(f"  {texte_local(p.get('displayName'))!r} : note {p.get('rating', '-')}, "
              f"{p.get('userRatingCount', 0)} avis")
    return lignes, brut


# --------------------------------------------------------------------------- sortie
def ecrire(lignes, brut, dossier, commande):
    os.makedirs(dossier, exist_ok=True)
    horodatage = dt.datetime.now().strftime("%Y%m%d-%H%M")
    base = os.path.join(dossier, f"places-{commande}-{horodatage}")
    with open(base + ".json", "w", encoding="utf-8") as f:
        json.dump(brut, f, ensure_ascii=False, indent=1)
    if lignes:
        with open(base + ".csv", "w", encoding="utf-8-sig", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(lignes[0].keys()), delimiter=";")
            w.writeheader()
            w.writerows(lignes)
    return base


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default="sortie-places")
    ap.add_argument("--max-appels", type=int, default=200)
    ap.add_argument("--lang", default="fr")
    ap.add_argument("--region", default="FR")
    ap.add_argument("--dry-run", action="store_true", help="n'appelle pas l'API, affiche les appels prevus")
    sub = ap.add_subparsers(dest="commande", required=True)

    s = sub.add_parser("pack", help="requete(s) x ville(s) -> les N premieres fiches")
    s.add_argument("requete", help="une requete, une liste separee par des virgules, ou un fichier")
    s.add_argument("--villes", default="", help="idem, villes")
    s.add_argument("--n", type=int, default=10)

    s = sub.add_parser("reseau", help="toutes les fiches portant un nom de marque")
    s.add_argument("nom")
    s.add_argument("--villes", default="", help="villes a ajouter au nom pour elargir la recherche")

    s = sub.add_parser("fiche", help="detail d'une ou plusieurs fiches")
    s.add_argument("place_ids", nargs="+")

    args = ap.parse_args()
    global DRY_RUN
    DRY_RUN = args.dry_run
    cle = "dry-run" if DRY_RUN else cle_api()
    compteur = Compteur(args.max_appels)
    fonctions = {"pack": cmd_pack, "reseau": cmd_reseau, "fiche": cmd_fiche}
    lignes, brut = fonctions[args.commande](args, cle, compteur)
    base = ecrire(lignes, brut, args.out, args.commande)
    print(f"\n{len(lignes)} ligne(s), {compteur.n} appel(s) API.")
    print(f"Sortie : {base}.csv et .json")


if __name__ == "__main__":
    main()
