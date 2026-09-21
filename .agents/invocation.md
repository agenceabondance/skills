# Model-invoked et user-invoked

Chaque `SKILL.md` du dépôt est une skill. Un seul axe les sépare, **l'invocation** : qui peut l'atteindre.

- **User-invoked** : atteignable **seulement par l'humain qui tape son nom**. `disable-model-invocation: true` dans le frontmatter (Claude Code) et `policy.allow_implicit_invocation: false` dans `agents/openai.yaml` (Codex). La `description` s'adresse à un **humain** : une ligne, lue dans la liste des commandes. Sans déclencheurs (« Utiliser quand... »).
- **Model-invoked** : atteignable **par le modèle ou l'humain**. Le défaut : ni `disable-model-invocation`, ni bloc `policy`. La `description` s'adresse au **modèle** : elle porte les déclencheurs, un par branche (« Utiliser pour auditer..., répondre..., vérifier... »). Le test pour rester model-invoked : *l'agent aurait-il raison de la lancer seul ?* (La réutilisation est la raison d'extraire une skill, pas le test.)

Une skill est user-invoked dans les deux harnais ou dans aucun : `agents/openai.yaml` et le frontmatter disent la même chose. `scripts/check-repo.py` le vérifie.

Chaque skill porte un `agents/openai.yaml` à côté de son `SKILL.md` : `interface.display_name` et `interface.short_description` pour le sélecteur Codex, et le bloc `policy` pour les user-invoked.

## Dépendances

Une skill qui en appelle une autre le dit par une instruction explicite : `Call the Skill tool with "sourcer"`. Pas un lien `../autre-skill/FICHIER.md`, pas un `/sourcer` laissé dans la prose. Nommer l'outil est ce qui déclenche l'appel ; laisser tomber le `/` garde la phrase neutre entre harnais. La référence partagée vit dans la skill qui la possède ; les autres l'atteignent en appelant cette skill.

Ceci ne vaut que pour une skill **model-invoked**. Une skill user-invoked ne peut être atteinte ainsi par personne, aucune autre skill comprise. Quand une étape a pour précondition une skill user-invoked (`setup-abondance-skills`), on le dit à l'humain : « dire à l'utilisateur de lancer `/setup-abondance-skills` », jamais un appel de l'outil.

Le Skill tool prend une skill par appel. Une étape qui en veut deux, ce sont deux appels, et on le dit (`Call the Skill tool twice, for "sourcer" and "brevet-google"`).

Le routeur (`ask-abondance`) et les README de bucket nomment les skills pour qu'un humain choisisse ; ils ne lancent rien, donc ils gardent les noms en `/skill`, comme des étiquettes.

## Dépendance dure, dépendance molle

Certaines skills lisent la configuration écrite par `/setup-abondance-skills` (`docs/agents/abondance.md`).

- **Dépendance dure** : sans la configuration, la sortie est fausse, pas seulement floue. Aucune skill du dépôt n'est dans ce cas aujourd'hui.
- **Dépendance molle** (`audit-local`) : la configuration évite de redemander où vont les livrables et quels outils existent ; sans elle, la phase 2 les demande. La skill y fait référence en une phrase, sans pointeur impératif vers le setup.

Un pointeur de setup dans une skill qui n'en a qu'un besoin mou est du contexte payé pour rien.
