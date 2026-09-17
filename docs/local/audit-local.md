## Ce qu'elle fait

`audit-local` mène l'audit d'une fiche d'établissement Google, ou d'un réseau de fiches, en six phases jusqu'à un livrable en huit sections. Une famille de contrôles sans donnée est ⚪ et le reste : le livrable dit ce qu'il n'a pas pu vérifier, en section 2 avant de commencer et en section 7 en terminant, au lieu de faire comme si.

Il ne rend pas de score. Chaque famille (conformité, complétude, avis, pertinence, distance, proéminence, engagement, concurrence, réseau) reçoit un **verdict** (✅ 🟠 🔴 ⚪), et les actions sont classées par risque, effort et niveau de preuve. Un 🔴 en conformité passe devant tout le reste.

## Quand la prendre

Vous la lancez en tapant `/audit-local` ; l'agent ne la prendra pas seul. Elle prend en argument les établissements, les requêtes cibles et les villes.

| Votre situation | Prendre |
|---|---|
| Un client, une ou plusieurs fiches, un livrable à rendre | `audit-local` |
| Une question ponctuelle (« les posts comptent-ils ? ») | [seo-local](../local/seo-local.md) |
| Vérifier un audit déjà écrit par quelqu'un d'autre | [seo-local](../local/seo-local.md), mode vérifier |
| Un réseau de vingt fiches à comparer | `audit-local` : la famille I et `places.py reseau` sont faits pour ça |

## Prérequis

- **Un dépôt de travail configuré** par `/setup-abondance-skills` : dossier des livrables, outils de mesure disponibles. Sans lui, la phase 2 pose les questions à chaque audit ; l'audit fonctionne quand même.
- **Une clé Google Cloud** avec Places API (New), dans `GOOGLE_PLACES_API_KEY`, pour la collecte automatique du pack et du réseau. Sans elle, la collecte se fait à la main et les contrôles P sont ⚪ ou manuels. Voir `SECURITY.md`.
- Python 3.10 ou plus pour `places.py` et `audit.py`.

## Six phases, un critère de fin chacune

Cadrer, inventorier les données, collecter, dérouler la grille, écrire, et (si demandée) la version client. Chaque phase se ferme sur une condition vérifiable, pas sur une impression : « les 43 contrôles ont un verdict », « chaque 🟠 / 🔴 porte constat, source et preuve ». La phase 2 est celle qui protège le livrable : un ⚪ annoncé là est une limite, un ⚪ découvert en phase 4 est un trou.

## Questions fréquentes

**Pourquoi pas un score sur 100 ? Les clients le demandent.**

Parce que les poids des signaux ne sont pas publics : un score les additionnerait sans les connaître. La section 6 du livrable (actions classées par risque, effort et preuve) est ce qu'un client attend d'un score, sans l'invention. Position tenue depuis la première version : `.out-of-scope/score-global.md`.

**43 contrôles, est-ce qu'un agent tient ça en une passe ?**

C'est la question posée aux relecteurs de la première version. La grille est lue famille par famille, et la phase 4 exige un verdict par contrôle avant d'écrire : c'est le critère de fin, pas la longueur, qui tient l'agent. Si une famille est ⚪ d'avance (pas d'accès aux Performances), elle ne coûte rien.

**Places me donne un ordre de résultats. Ce n'est pas la position ?**

Non. Une recherche Places par texte ne connaît ni le point de mesure ni la personnalisation ; l'ordre ressemble à un classement et c'est ce qui le rend dangereux. Les positions viennent d'un suivi par point de mesure (famille E). `.out-of-scope/positions-lues-dans-places.md`.

## Ça marche si

- Le livrable a une section 2 remplie avant que la collecte commence, et une section 7 qui liste des familles ⚪ avec leur raison.
- Chaque ligne 🟠 ou 🔴 cite un `[NN]` ou un `[USxxxx]` et un niveau de preuve.
- Aucune recommandation ne contredit les consignes Google, même quand les experts la classent haut.
- Le fichier ne contient ni chiffre sur 100 ni position promise.

## Où elle se place

Le flux le plus long du dépôt, et le seul qui produit un livrable client. Il appelle [seo-local](../local/seo-local.md) pour le corpus que la grille cite, et [sourcer](../methode/sourcer.md) à travers lui pour la règle d'écriture. [setup-abondance-skills](../methode/setup-abondance-skills.md) se lance une fois avant. Pour la carte entière, [ask-abondance](../methode/ask-abondance.md).
