---
name: seo-local
description: Corpus sourcé sur le classement local de Google (fiche d'établissement, pack local). Utiliser pour répondre à une question de classement local avec des sources, vérifier qu'une recommandation locale est étayée, ou chercher ce que Google, un brevet ou une étude dit d'un signal local.
---

# SEO local

Le corpus vit dans `references/` : une fiche par source, les brevets dans `references/brevets/`, et `00-index.md` qui route une question vers les fiches à lire. Le corpus a un périmètre : le classement d'une fiche d'établissement dans Google (pack local, Maps). Le site web et le classement organique n'y entrent que comme signaux de la fiche.

Call the Skill tool with "sourcer" : c'est la règle d'écriture, les niveaux de preuve et la forme d'une vérification.

## Répondre

1. Lire `references/00-index.md`, puis seulement les fiches que les repères de routage désignent pour la question.
2. Chaque point cite sa source `[NN]` / `[USxxxx]`, dans les formes de `sourcer`. Ce qui n'est dans aucune fiche est `(hors corpus)`.
3. Une position tenue par le corpus : le mot-clé dans le nom, interdit ([02]) et classé 3e par les experts ([05]). On recommande le nom réel, on signale les concurrents qui font autrement.

Terminé quand chaque affirmation porte une source ou `(hors corpus)`, que le bloc Sources mobilisées ferme la réponse, et qu'aucune recommandation ne contredit [02] ou [03].

## Vérifier

Un livrable, une recommandation, un article à vérifier : la forme est celle de `sourcer` (une ligne par affirmation). Le corpus est la seule référence ; une affirmation vraie mais absente du corpus est « le corpus ne dit rien », et c'est un trou à noter dans `00-index.md` si une source fiable existe.

## Auditer

Un audit complet (établissements, requêtes, grille, livrable) est un flux à part : dire à l'utilisateur de lancer `/audit-local`.
