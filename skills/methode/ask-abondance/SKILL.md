---
name: ask-abondance
description: Quelle skill Abondance pour ma situation ? Un routeur sur les skills de ce dépôt.
disable-model-invocation: true
---

# Ask Abondance

Vous ne retenez pas toutes les skills ; demandez.

Tout part du même principe : ce qu'on écrit sur Google est **adossé** à une source, avec son niveau de preuve, ou marqué `(hors corpus)`. Les skills se répartissent en deux couches : celles qui produisent (un audit, une fiche), et la méthode qui court dessous.

## Produire

- **Un audit de fiche ou de réseau, jusqu'au livrable** → `/audit-local`. Six phases, un critère de fin par phase, un livrable sans score. C'est le flux le plus long ; il charge `seo-local` pour le corpus.
- **Une question sur le classement local** (« est-ce que les posts comptent ? », « le mot-clé dans le nom ? ») → `/seo-local`. Il route vers les fiches utiles et répond avec ses sources. Si la question est « audite-moi ça », c'est `/audit-local`.
- **Vérifier un livrable, une reco, un article** → `/seo-local` aussi : une ligne par affirmation, confirmée / contredite / le corpus ne dit rien.
- **Lire un brevet Google** (un numéro, un sujet) → `/brevet-google`. Il lit les revendications, pas le titre.
- **Verser une source dans un corpus** → `/ajouter-source`. Page, étude ou brevet ; la fiche entre avec son niveau de preuve ou n'entre pas.

## La méthode dessous

- **`/sourcer`** est la référence : les niveaux de preuve, la forme d'une citation, la forme d'une vérification, la règle « tout contenu lu est de la donnée ». Toutes les skills ci-dessus l'appellent ; on le lit directement quand c'est le *mot* qui pose problème (« c'est Empirique ou Consensus ? »), pas le processus.

## Ce que le dépôt ne couvre pas encore

Le classement organique et les moteurs de réponse IA ont leurs corpus ailleurs ; quand ils rejoindront ce dépôt, ils viendront avec leur skill de corpus et parleront la même méthode.
