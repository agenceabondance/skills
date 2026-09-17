"""Tests des scripts, sans reseau ni cle API.

Lancer : py -m pytest -q   (python3 -m pytest sur Mac)
"""
import subprocess
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]  # skills/local/audit-local
SCRIPTS = RACINE / "scripts"
FIXTURES = RACINE / "tests" / "fixtures"


def lancer(*args, cwd=None):
    r = subprocess.run([sys.executable, *args], capture_output=True, text=True, encoding="utf-8", cwd=cwd)
    assert r.returncode == 0, r.stderr
    return r.stdout


# ---------------------------------------------------------------- audit.py
def test_audit_pack_trouve_le_client_et_les_alertes():
    out = lancer(SCRIPTS / "audit.py", "places", FIXTURES / "places-pack.csv", "--client", "motorsport academy")
    assert "| stage de pilotage | Le Mans | 1 |" in out          # meilleure fiche du client au rang 1
    assert "| stage de pilotage | Nantes | absent |" in out      # client absent d'un pack
    assert "majuscules integrales" in out                        # alerte de nom sur un concurrent
    assert "statut CLOSED_PERMANENTLY" in out                    # fiche fermee signalee
    assert "**Client absent** des 1 premiers" in out


def test_audit_pack_ne_rend_pas_de_verdict_ni_de_score():
    out = lancer(SCRIPTS / "audit.py", "places", FIXTURES / "places-pack.csv", "--client", "motorsport academy")
    assert "/100" not in out and "score" not in out.lower()


def test_audit_reseau_doublons_et_categories():
    out = lancer(SCRIPTS / "audit.py", "places", FIXTURES / "places-reseau.csv", "--client", "motorsport academy")
    assert "3 fiche(s) au nom du client, 1 autre(s)" in out
    assert "Noms en double" in out and "Motorsport Academy Lohéac" in out
    assert "Catégories principales hétérogènes" in out


def test_audit_export_interface_colonnes_reconnues_et_manquantes():
    out = lancer(SCRIPTS / "audit.py", "gbp", FIXTURES / "export-interface.csv")
    assert "2 fiche(s)" in out
    assert "Colonnes non trouvées dans l'export" in out and "statut" in out   # colonne absente signalee, pas devinee
    assert "pas de site" in out and "pas d'horaires (lundi vide)" in out


def test_audit_places_exige_client():
    r = subprocess.run([sys.executable, SCRIPTS / "audit.py", "places", FIXTURES / "places-pack.csv"],
                       capture_output=True, text=True, encoding="utf-8")
    assert r.returncode != 0 and "--client" in (r.stderr + r.stdout)


# ---------------------------------------------------------------- places.py
def test_places_dry_run_compte_les_appels(tmp_path):
    out = lancer(SCRIPTS / "places.py", "--dry-run", "--out", tmp_path, "pack", "a,b", "--villes", "x,y,z")
    assert out.count("[dry-run] POST") == 6                       # 2 requetes x 3 villes
    assert "6 appel(s) API" in out


def test_places_plafond_arrete_avant_l_appel(tmp_path):
    r = subprocess.run([sys.executable, SCRIPTS / "places.py", "--dry-run", "--max-appels", "2", "--out", tmp_path,
                        "pack", "a", "--villes", "x,y,z"], capture_output=True, text=True, encoding="utf-8")
    assert r.returncode != 0 and "Plafond de 2 appels" in (r.stderr + r.stdout)
    assert r.stdout.count("[dry-run]") == 2


def test_places_n_affiche_jamais_la_cle(tmp_path, monkeypatch):
    """Cle factice dans l'environnement, plafond a 0 : le script s'arrete avant tout appel
    et ne doit jamais ecrire la cle, ni dans la sortie ni dans les fichiers."""
    monkeypatch.setenv("GOOGLE_PLACES_API_KEY", "AIzaFAUSSE-CLE-DE-TEST")
    r = subprocess.run([sys.executable, SCRIPTS / "places.py", "--max-appels", "0", "--out", tmp_path, "fiche", "ChIJx"],
                       capture_output=True, text=True, encoding="utf-8")
    assert r.returncode != 0 and "Plafond de 0 appels" in (r.stderr + r.stdout)
    assert "AIzaFAUSSE" not in r.stdout + r.stderr
    assert not any("AIzaFAUSSE" in f.read_text(encoding="utf-8") for f in tmp_path.glob("*"))


def test_la_cle_n_est_jamais_ecrite_dans_les_sorties():
    src = (SCRIPTS / "places.py").read_text(encoding="utf-8")
    assert "print(cle" not in src and "cle)" not in src.split("def ecrire")[1]


def test_audit_neutralise_les_noms_hostiles():
    """Un nom de fiche ecrit par un tiers ne doit ni casser le tableau markdown ni injecter du HTML."""
    out = lancer(SCRIPTS / "audit.py", "places", FIXTURES / "places-pack-hostile.csv", "--client", "ma marque")
    assert "<script>" not in out and "&lt;script&gt;" in out
    assert "Plombier \| " in out                                  # le pipe est echappe, la ligne reste lisible
    assert "| stage" not in out
    ligne = next(l for l in out.splitlines() if "alert" in l)
    assert ligne.count(" | ") >= 8                                # la ligne a toujours toutes ses colonnes
