# Découper sur l'axe invocation, pas sur le sujet

La première version tenait en une skill, `seo-local`, avec trois « modes » dans un même `SKILL.md` : auditer, répondre, enrichir le corpus. Tout était chargé à chaque appel, et la description devait déclencher sur les trois.

Les trois modes n'ont pas le même déclencheur. Répondre à une question avec des sources est un réflexe que l'agent doit avoir seul. Un audit complet et l'ajout d'une source sont des décisions humaines, qui coûtent une session ou modifient le dépôt. Une description qui couvre les trois paie du contexte à chaque tour pour des branches que seul l'humain ouvre.

Décision : une skill par mode d'invocation.

- **Model-invoked** (description avec déclencheurs, pas de `disable-model-invocation`) : `seo-local`, `sourcer`, `brevet-google`. L'agent peut les atteindre seul ; une autre skill peut les appeler.
- **User-invoked** (`disable-model-invocation: true`, `policy.allow_implicit_invocation: false`) : `audit-local`, `ajouter-source`, `ask-abondance`, `setup-abondance-skills`. Zéro coût de contexte ; l'humain est l'index.

Le test pour rester model-invoked : l'agent aurait-il raison de la lancer seul ? La réutilisation n'est pas le test.

Les buckets (`local/`, `methode/`) sont une organisation par sujet, pour le lecteur ; ils ne portent aucune règle d'invocation.
