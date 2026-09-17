## Ce qu'elle fait

`ask-abondance` est le routeur : elle nomme chaque skill du dépôt et dit dans quelle situation la prendre. Elle ne lance rien elle-même ; la plupart des skills sont user-invoked, donc c'est vous qui les tapez, et cette page vous évite de les retenir toutes.

## Quand la prendre

Vous la lancez en tapant `/ask-abondance` ; l'agent ne la prendra pas seul. La prendre quand vous ne savez pas laquelle prendre.

## La carte

Deux couches. Celles qui **produisent** : [audit-local](../local/audit-local.md) (un livrable), [seo-local](../local/seo-local.md) (une réponse ou une vérification), [brevet-google](../methode/brevet-google.md) (une lecture de brevet), [ajouter-source](../methode/ajouter-source.md) (une source de plus). Et la **méthode dessous** : [sourcer](../methode/sourcer.md), que toutes appellent. Une précondition : [setup-abondance-skills](../methode/setup-abondance-skills.md), une fois par dépôt de travail.

## Où elle se place

Le nœud central du routeur distribué que forment ces pages. Chaque autre page renvoie ici pour ne pas avoir à redessiner le graphe.
