# `sourcer` est l'unique propriétaire des niveaux de preuve

La table des niveaux de preuve existait en trois exemplaires : le README, `references/00-index.md`, et implicitement le `SKILL.md`. Trois copies, trois occasions de diverger, et une notion dont la prominence dans le contexte ne correspondait pas à son rang.

Décision : la table vit dans `skills/methode/sourcer/SKILL.md` et nulle part ailleurs. Les autres fichiers la nomment (« défini dans la skill `sourcer` ») ; les skills l'atteignent par `Call the Skill tool with "sourcer"`.

Deux exceptions assumées :

- Le `README.md` racine garde une version courte (niveau, phrase type) pour le lecteur humain qui découvre le dépôt. C'est un cache pour un lecteur qui ne chargera pas la skill.
- Le gabarit de source (`ajouter-source/GABARIT-SOURCE.md`) énumère les valeurs possibles dans son frontmatter, parce qu'un gabarit se remplit sans lire une autre skill.

Ce qui en découle : un nouveau sujet (organique, moteurs de réponse IA) n'apporte pas ses propres niveaux ; il appelle `sourcer`. Si un sujet a besoin d'un niveau de plus, il se propose dans `sourcer`, pour tous.
