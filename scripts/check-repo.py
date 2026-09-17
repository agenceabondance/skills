#!/usr/bin/env python3
"""Verifie les conventions mecaniques du depot. Bibliotheque standard seule.

Lancer : python3 scripts/check-repo.py   (py sous Windows)

Ce que le script verifie, et que CLAUDE.md n'a donc plus besoin de dire :
  - chaque SKILL.md a un frontmatter avec name (= nom du dossier) et description ;
  - chaque skill a un agents/openai.yaml, et les deux disent la meme chose sur
    l'invocation (disable-model-invocation <-> policy.allow_implicit_invocation: false) ;
  - chaque skill d'un bucket promu est dans .claude-plugin/plugin.json, dans le
    README.md racine et dans le README.md de son bucket ;
  - aucun tiret cadratin dans la prose (SKILL.md, README, docs, ADR, CHANGELOG) ;
  - la version de plugin.json est celle de la derniere version publiee du CHANGELOG ;
  - chaque skill promue a sa page docs/<bucket>/<skill>.md.
Sort avec le code 1 et la liste des ecarts s'il y en a.
"""
import json
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
SKILLS = RACINE / "skills"
PROMUS = ("local", "methode")
erreurs = []


def erreur(msg):
    erreurs.append(msg)


def frontmatter(texte):
    m = re.match(r"^---\n(.*?)\n---\n", texte, re.S)
    if not m:
        return None
    champs = {}
    for ligne in m.group(1).splitlines():
        if ":" in ligne and not ligne.startswith(" "):
            cle, _, val = ligne.partition(":")
            champs[cle.strip()] = val.strip().strip('"')
    return champs


def skills_du_depot():
    for skill_md in sorted(SKILLS.glob("*/*/SKILL.md")):
        yield skill_md.parent.parent.name, skill_md.parent.name, skill_md


def verifier_skill(bucket, nom, skill_md):
    fm = frontmatter(skill_md.read_text(encoding="utf-8"))
    rel = skill_md.relative_to(RACINE)
    if fm is None:
        erreur(f"{rel} : pas de frontmatter")
        return None
    if fm.get("name") != nom:
        erreur(f"{rel} : name '{fm.get('name')}' != dossier '{nom}'")
    if not fm.get("description"):
        erreur(f"{rel} : description absente")
    user_invoked = fm.get("disable-model-invocation") == "true"

    yaml = skill_md.parent / "agents" / "openai.yaml"
    if not yaml.exists():
        erreur(f"{rel} : agents/openai.yaml absent")
    else:
        y = yaml.read_text(encoding="utf-8")
        codex_user = "allow_implicit_invocation: false" in y
        if codex_user != user_invoked:
            erreur(f"{rel} : invocation incoherente entre le frontmatter et agents/openai.yaml")
        if "display_name" not in y or "short_description" not in y:
            erreur(f"{yaml.relative_to(RACINE)} : display_name ou short_description absent")
    return user_invoked


def verifier_presence(bucket, nom):
    chemin = f"./skills/{bucket}/{nom}"
    plugin = json.loads((RACINE / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    if chemin not in plugin.get("skills", []):
        erreur(f"plugin.json : {chemin} absent du tableau skills")
    lien_racine = f"./skills/{bucket}/{nom}/SKILL.md"
    if lien_racine not in (RACINE / "README.md").read_text(encoding="utf-8"):
        erreur(f"README.md : aucun lien vers {lien_racine}")
    readme_bucket = SKILLS / bucket / "README.md"
    if not readme_bucket.exists() or f"./{nom}/SKILL.md" not in readme_bucket.read_text(encoding="utf-8"):
        erreur(f"skills/{bucket}/README.md : aucun lien vers ./{nom}/SKILL.md")
    page = RACINE / "docs" / bucket / f"{nom}.md"
    if not page.exists():
        erreur(f"docs/{bucket}/{nom}.md : page docs absente")


def verifier_plugin_contre_skills(connus):
    plugin = json.loads((RACINE / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    for chemin in plugin.get("skills", []):
        if chemin not in connus:
            erreur(f"plugin.json : {chemin} ne correspond a aucune skill promue")


def verifier_tirets_cadratins():
    cibles = [RACINE / "README.md", RACINE / "CLAUDE.md", RACINE / "CONTEXT.md", RACINE / "CHANGELOG.md"]
    for dossier in ("skills", "docs", ".agents", ".out-of-scope"):
        cibles += (RACINE / dossier).rglob("*.md")
    for f in cibles:
        if not f.exists():
            continue
        # Les sources du corpus citent des textes tiers : on ne les corrige pas.
        if "references" in f.parts:
            continue
        for i, ligne in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            if "—" in ligne:
                erreur(f"{f.relative_to(RACINE)}:{i} : tiret cadratin")


def verifier_version():
    plugin = json.loads((RACINE / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    changelog = (RACINE / "CHANGELOG.md").read_text(encoding="utf-8")
    m = re.search(r"^## (\d+\.\d+\.\d+)", changelog, re.M)
    if not m:
        erreur("CHANGELOG.md : aucune version publiee (## X.Y.Z)")
        return
    if plugin.get("version") != m.group(1):
        erreur(f"plugin.json version {plugin.get('version')} != derniere version du CHANGELOG {m.group(1)}")


def main():
    connus = []
    for bucket, nom, skill_md in skills_du_depot():
        verifier_skill(bucket, nom, skill_md)
        if bucket in PROMUS:
            connus.append(f"./skills/{bucket}/{nom}")
            verifier_presence(bucket, nom)
    verifier_plugin_contre_skills(connus)
    verifier_tirets_cadratins()
    verifier_version()
    if erreurs:
        print("\n".join(erreurs))
        print(f"\n{len(erreurs)} ecart(s).")
        sys.exit(1)
    print(f"OK : {len(connus)} skill(s) promue(s), conventions respectees.")


if __name__ == "__main__":
    main()
