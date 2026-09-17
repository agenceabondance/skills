---
name: setup-abondance-skills
description: "Configurer ce dépôt pour les skills Abondance : dossier des livrables, outils de mesure disponibles, clé Places. À lancer une fois par dépôt de travail."
disable-model-invocation: true
---

# Setup des skills Abondance

Écrire la configuration par dépôt que `audit-local` lit avant de demander quoi que ce soit :

- **Livrables** : où les audits s'écrivent.
- **Outils de mesure** : suivi de positions Maps, outil de mesure du site, accès aux fiches.
- **Clé Places** : présente dans l'environnement ou non (jamais sa valeur).

Skill pilotée par la conversation, pas un script : explorer, présenter ce qu'on a trouvé, confirmer, écrire.

## Processus

### 1. Explorer

Lire ce qui existe ; ne rien supposer :

- `CLAUDE.md` et `AGENTS.md` à la racine : lequel existe ? Y a-t-il déjà un bloc `## Skills Abondance` ?
- `docs/agents/abondance.md` : la sortie d'un setup précédent.
- Un dossier qui ressemble à des livrables clients (`clients/`, `audits/`, `livrables/`).
- `GOOGLE_PLACES_API_KEY` dans l'environnement : présente ou absente. Ne jamais l'afficher.
- Des exports d'interface Google (`*.csv` avec des colonnes Performances) ou des sorties `places-*.csv` : signes de ce qui a déjà servi.

### 2. Présenter et demander

Résumer ce qui est là et ce qui manque, puis prendre les sections dans l'ordre, une réponse à la fois. Ouvrir chaque section par la réponse recommandée, pour qu'un mot suffise à l'accepter.

**Section A : livrables.** Proposer le dossier trouvé en exploration ; sinon `audits/<client>/`. Le livrable d'un audit s'écrit là, en markdown.

**Section B : outils de mesure.** Trois questions, une par ligne de la section 2 du gabarit de livrable :

- Suivi de positions Maps : quel outil (Monitorank, grille géographique, autre), ou aucun.
- Outil de mesure du site : GA4, Matomo, autre, ou aucun ; et si les fiches portent un `utm_campaign`.
- Accès aux fiches : propriétaire, gestionnaire, ou public seulement.

Une réponse « aucun » est une réponse : elle fait ⚪ la famille correspondante d'avance, et le livrable le dira.

**Section C : clé Places.** Ne rien demander : l'exploration a dit si `GOOGLE_PLACES_API_KEY` est là. Écrire « présente » ou « absente », et si absente, renvoyer à `SECURITY.md` pour la créer.

### 3. Confirmer

Montrer le bloc `## Skills Abondance` à ajouter et le contenu de `docs/agents/abondance.md`, rédigé depuis [`abondance.md`](abondance.md). Laisser modifier avant d'écrire.

### 4. Écrire

Le fichier à modifier : `CLAUDE.md` s'il existe, sinon `AGENTS.md` s'il existe, sinon demander lequel créer. Ne jamais créer l'un quand l'autre existe. Un bloc `## Skills Abondance` déjà présent se met à jour en place.

Le bloc :

```markdown
## Skills Abondance

Livrables dans `<dossier>`. Outils de mesure et clé Places : voir `docs/agents/abondance.md`.
```

Puis `docs/agents/abondance.md` depuis le gabarit.

### 5. Terminé

Dire que `audit-local` lira ce fichier en phase 2 et ne redemandera que ce qui a changé. Le fichier se modifie à la main ; relancer cette skill n'est utile que pour repartir de zéro.
