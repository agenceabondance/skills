# Français partout ; Python 3.10 et bibliothèque standard seule

Deux décisions de la première version, consignées ensemble parce qu'elles ont la même raison : le public.

**Français.** Le public visé est francophone (Abondance est un média SEO francophone). Les skills, le corpus, la grille, les README et ce dépôt sont en français. Les citations gardent leur langue d'origine. Un résumé anglais du README pourra venir ; il ne remplacera pas le français. Les noms de skills restent des mots français courts (`sourcer`, `audit-local`) sauf les conventions du format (`SKILL.md`, `disable-model-invocation`).

**Bibliothèque standard.** `places.py`, `audit.py`, `brevet.py` tournent avec Python 3.10 ou plus, sans rien installer. Le public est un consultant SEO sur Windows ou Mac, pas un développeur ; « installer » doit tenir en une commande. Le prix : le parsing HTML de `brevet.py` se fait par expressions régulières, et les sorties CSV portent un BOM pour Excel. C'est un prix accepté.

Conséquence pour l'outillage du dépôt : les vérifications de conventions (`scripts/check-repo.py`) suivent la même règle, et le dépôt ne porte pas de `package.json`. Le versionnage se fait à la main dans `CHANGELOG.md` et `.claude-plugin/plugin.json`, et `check-repo.py` vérifie qu'ils s'accordent.
