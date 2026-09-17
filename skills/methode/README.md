# Méthode

Ce qui court sous tous les corpus, quel que soit le sujet.

## User-invoked

Accessibles seulement quand vous les tapez (Claude Code : `disable-model-invocation: true` ; Codex : `policy.allow_implicit_invocation: false` dans `agents/openai.yaml`).

- **[ask-abondance](./ask-abondance/SKILL.md)** : quelle skill pour ma situation. Un routeur sur les skills du dépôt.
- **[setup-abondance-skills](./setup-abondance-skills/SKILL.md)** : configurer un dépôt de travail (dossier des livrables, outils de mesure, clé Places). Une fois par dépôt.
- **[ajouter-source](./ajouter-source/SKILL.md)** : verser une page, une étude ou un brevet dans un corpus, avec son niveau de preuve. Porte le gabarit de source.

## Model-invoked

Accessibles par vous ou par l'agent quand la tâche s'y prête.

- **[sourcer](./sourcer/SKILL.md)** : la discipline de citation : niveaux de preuve, `[NN]` / `[USxxxx]`, `(hors corpus)`, forme d'une vérification. Unique propriétaire de la table des niveaux ; toutes les autres skills l'appellent.
- **[brevet-google](./brevet-google/SKILL.md)** : lire un brevet Google sur ses revendications, chercher les brevets d'un sujet, rédiger la source. Porte `brevet.py` et le gabarit de source brevet.
