---
name: brevet-google
description: Lire un brevet Google sur ses revendications. Utiliser quand l'utilisateur cite un numéro de brevet, demande ce qu'un brevet Google décrit ou prouve, ou veut trouver les brevets Google sur un sujet.
---

# Brevet Google

Un brevet se lit sur ses **revendications**, pas sur son titre ni son abrégé. Le titre dit ce que le déposant a demandé ; les revendications délivrées disent ce qu'il a obtenu, et les deux divergent (le corpus local en contient un cas, [US10394830B1], titré sur le sentiment des avis et délivré sur les interactions).

Call the Skill tool with "sourcer" : un brevet est un niveau de preuve à lui seul, et il se cite « un brevet Google décrit », jamais « Google fait ».

## Lire

1. `scripts/brevet.py <numéro ou URL>` dépose le texte complet dans `scripts/cache/` (non versionné) : en-tête, abrégé, revendications numérotées avec leurs dépendances, description en paragraphes, brevets cités et citants. `--meta` pour l'en-tête seul (déposant, dates, statut).
2. Lire les revendications indépendantes en premier. Une revendication dépendante précise sa parente ; elle ne l'élargit jamais.
3. Répondre avec le mécanisme (entrées, calcul, sortie), les revendications qui le portent (rev. N), le statut (actif, expiré et pourquoi), et ce que le brevet **ne prouve pas** : un mécanisme décrit n'est pas un mécanisme déployé.

## Chercher

`scripts/brevet.py --chercher "<sujet>"` liste les brevets sur le sujet dont le déposant est Google (`--tous` pour lever le filtre). Un brevet qui entre dans un corpus se lit en entier ; la liste ne suffit pas.

## Rédiger une fiche

Pour verser le brevet dans un corpus, la fiche suit [`GABARIT-BREVET.md`](GABARIT-BREVET.md). Le titre traduit vient après le numéro ; le statut porte sa date de relevé, parce qu'il bouge (annuités, expiration).

Terminé quand la fiche porte les revendications clés citées mot pour mot, le statut daté, et la section « ce que le brevet ne prouve pas » remplie.
