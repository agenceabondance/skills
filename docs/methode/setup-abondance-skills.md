## Ce qu'elle fait

`setup-abondance-skills` écrit, une fois par dépôt de travail, la configuration que `audit-local` lit avant de poser des questions : où vont les livrables, quels outils de mesure existent (suivi de positions, mesure du site, accès aux fiches), et si une clé Places est présente dans l'environnement. Elle explore le dépôt d'abord, propose une réponse par section, et n'écrit qu'après confirmation.

Elle ne stocke jamais la valeur de la clé, seulement sa présence.

## Quand la prendre

Vous la lancez en tapant `/setup-abondance-skills` ; l'agent ne la prendra pas seul. Une fois, avant le premier audit dans un dépôt ; puis le fichier se modifie à la main.

## Ce qu'elle écrit

Un bloc `## Skills Abondance` dans `CLAUDE.md` (ou `AGENTS.md`, celui qui existe) et `docs/agents/abondance.md`, une table des outils avec ✅ ou ⚪ par ligne. Une ligne ⚪ fait ⚪ la famille correspondante de la grille d'avance, et le livrable le dira.

## Ça marche si

- Le premier `/audit-local` qui suit ne redemande ni le dossier des livrables ni les outils, seulement ce qui change pour ce client.
- `docs/agents/abondance.md` ne contient aucune clé.

## Où elle se place

Un setup à lancer une fois. [audit-local](../local/audit-local.md) est la seule skill qui la lit, en dépendance molle : sans elle, l'audit demande. Pour la carte entière, [ask-abondance](../methode/ask-abondance.md).
