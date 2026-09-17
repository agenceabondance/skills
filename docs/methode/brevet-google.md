## Ce qu'elle fait

`brevet-google` lit un brevet Google sur Google Patents et en rend le mécanisme, les revendications qui le portent, le statut daté, et ce que le brevet ne prouve pas. Elle lit les **revendications**, pas le titre ni l'abrégé : le titre dit ce que le déposant a demandé, les revendications délivrées disent ce qu'il a obtenu, et les deux divergent.

Elle cherche aussi les brevets Google sur un sujet, et rédige la source pour un corpus depuis son gabarit.

## Quand la prendre

Tapez `/brevet-google`, ou l'agent la prend seul quand vous citez un numéro de brevet, demandez ce qu'un brevet Google décrit, ou cherchez les brevets d'un sujet.

| Votre situation | Prendre |
|---|---|
| « Que dit le brevet US11893034B2 ? » | `brevet-google` |
| « Google a-t-il un brevet sur les avis ? » | `brevet-google`, mode chercher |
| Verser le brevet lu dans le corpus local | [ajouter-source](../methode/ajouter-source.md), qui l'appelle |
| Une question sur le classement local qui se trouve citer un brevet | [seo-local](../local/seo-local.md) |

## Prérequis

Python 3.10 ou plus pour `brevet.py`, qui télécharge le texte depuis `patents.google.com` dans un cache local non versionné. Aucune clé.

## Les revendications, pas le titre

Le corpus local contient le cas qui justifie la skill : un brevet titré sur le sentiment des avis, dont les revendications délivrées portent sur les interactions. Une source rédigée sur le titre aurait affirmé le contraire de ce que Google a obtenu. La skill lit les revendications indépendantes d'abord, puis ce que les dépendantes précisent, et écrit le statut avec sa date de relevé parce qu'il bouge (annuités, expiration).

## Ça marche si

- La réponse cite des numéros de revendications (rev. 1, rev. 9), pas seulement le résumé.
- Le statut porte une date de relevé.
- Une section « ce que le brevet ne prouve pas » est là, et dit au moins qu'un mécanisme décrit n'est pas un mécanisme déployé.

## Où elle se place

Un outil à prendre n'importe quand, indépendant du sujet : le SEO local l'utilise aujourd'hui, l'organique demain. [ajouter-source](../methode/ajouter-source.md) l'appelle pour verser un brevet dans un corpus ; [sourcer](../methode/sourcer.md) lui donne la forme de la citation. Pour la carte entière, [ask-abondance](../methode/ask-abondance.md).
