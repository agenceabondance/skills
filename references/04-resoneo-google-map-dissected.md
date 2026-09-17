---
titre: Google Map disséqué - les 72 signaux d'Oyster Rank
editeur: Resoneo (« Seg », @5eg ; diffusé par Olivier de Segonzac)
url: https://think.resoneo.com/google-map-dissected/fr/
url_archive: https://www.resoneo.com/archive/ (10 936 déclarations Geostore, dump téléchargeable)
type: Étude
preuve: Schéma fuité
date_publication: 2026-08
date_ajout: 2026-09-17
fiabilite: Haute
sujets: [oyster-rank, geostore, signaux, engagement, avis, categories, chaines, wikipedia, pagerank, popularite, proeminence, poids-inconnus]
---

# Google Map disséqué - les 72 signaux d'Oyster Rank

## En une phrase
Le schéma interne de Google Maps (Geostore) nomme 72 signaux de classement, dont 25 dépréciés, et prouve que les signaux d'engagement, d'avis et de présence web existent, sans donner aucun poids.

## Méthode de la source
Trois niveaux de preuve empilés : la fuite de documentation Google de 2024, un binaire récent embarquant le schéma Geostore non public (protobuf compilés, décodés), et une surface de recherche instrumentée (5 083 appels, 86 584 résultats, données d'août 2026). Chaque affirmation se vérifie ligne à ligne dans l'archive publiée.

## Ce qu'on en tire pour un audit

**Les signaux qui existent, groupés par ce qu'ils mesurent.** Le classement Geostore s'appelle **Oyster Rank** (et non PlaceRank).

| Groupe | Signaux nommés | Actionnable ? |
|---|---|---|
| Engagement sur la fiche | `SIGNAL_GOOGLE_LISTING_IMPRESSIONS`, `SIGNAL_GOOGLE_INFOWINDOW_VIEWS`, `SIGNAL_GOOGLE_DIRECTION_REQUESTS`, `SIGNAL_GOOGLE_HOMEPAGE_CLICKS`, `SIGNAL_GOOGLE_RBL_CLICKS`, `SIGNAL_GOOGLE_RBL_CLICK_FRACTION` | Indirectement : une fiche complète et attractive génère ces actions. **Ce sont les métriques de l'onglet Performances de la fiche** (vues, itinéraires, clics site) : l'étude valide que ces chiffres, accessibles au propriétaire, sont des signaux |
| Avis | `SIGNAL_GOOGLE_REVIEWS` | Partiellement (sollicitation conforme) |
| Présence web | `SIGNAL_GOOGLE_AUTHORITYPAGE_PAGERANK_CONFIDENCE`, `SIGNAL_GOOGLE_WEB_QUERYVOL` (volume de recherche du nom), `SIGNAL_WIKIPEDIA_ARTICLES`, `SIGNAL_WIKIPEDIA_WIKI_SCORE` | Oui : la page « autoritaire » de l'établissement (son site) et sa notoriété de marque |
| Structure | `SIGNAL_GOOGLE_CHAIN_STORES` (+ `BusinessChainProto`, `Persona.ChainAffinity` côté utilisateur) | Oui : déclarer l'appartenance à une chaîne / un réseau |
| Lieu | `SIGNAL_PLACE_INSIGHTS_POPULARITY`, `_PROMINENCE`, `_LANDMARK`, `_APPROACHABILITY`, `_TOTAL_ROAD_SEGMENT_USAGE` | Non : comportement des visiteurs et environnement physique |
| Dépréciés (extraits) | `SIGNAL_GOOGLE_MAPS_NAVBOOST_CLICKS`, `SIGNAL_GOOGLE_MAPS_NAVBOOST_CLICKTHROUGH_RATE`, `SIGNAL_GOOGLE_AUTHORITYPAGE_PAGERANK`, `SIGNAL_GOOGLE_WEBPAGE_REFERENCE_DOMAINS` | Le PageRank brut de la page et le compte de domaines référents sont marqués dépréciés, remplacés par une « confiance » PageRank. Ne pas vendre du netlinking « pour la fiche » sur cette base |

**Ce qui change la lecture d'un audit :**

- **Catégories** : le schéma ne porte qu'une distinction **PRIMARY / NON_PRIMARY** sur les GConcepts. Le basculement de la catégorie principale est un fait ; le reste (« ajouter des catégories fait monter ») ne l'est pas ici.
- **Avis** : stockés structurés (sujets du Knowledge Graph, sentiment par thème, positions de caractères). Le **texte** de l'avis est exploité, pas seulement l'étoile. Renforce la reco « avis avec texte » de [[06-sterling-sky-near-me-2025]] et le brevet [[US10394830B1]].
- **Site web** : `website[]` dans FeatureProto et `SIGNAL_GOOGLE_HOMEPAGE_CLICKS` dans le ranking. Le lien site de la fiche est un objet de classement.
- **Le classement final n'est pas Oyster Rank** : il ajoute compréhension sémantique de la requête, contexte géographique, génération de candidats, pertinence. Oyster Rank est la composante « proéminence » de [[01-google-classement-local]], pas le tout.

## Citations utiles
> « Le système dont nous détaillons plus loin les 72 signaux, Oyster Rank, a donc un nom, et ce n'est pas PlaceRank. »

> « `RankDetailsProto` expose : signal[] signal_mixer_type. Mais 15 autres tags ont été retirés du scope. La documentation du champ parent indique précisément que cette structure contient les signaux et leurs poids. »

> « Nous ne connaissons pas : les coefficients, les fonctions de normalisation, les seuils, les transformations, les calibrations par marché, les interactions entre signaux, les versions de modèle. »

> « `SIGNAL_GOOGLE_REVIEWS` appartient explicitement au vocabulaire de ranking Geostore. »

> « Seul le basculement `PRIMARY` est un fait porté par le schéma. »

> « Une petite fraction du code, de l'ordre de 0,1 %, échappe à cet accès général. Elle est isolée pour des raisons de confidentialité, principalement autour de l'anti-spam, et porte le nom de HIP. »

## Ce que la source ne prouve pas
- **Aucun poids, aucun seuil.** Un signal nommé peut peser 40 % ou 0,4 %. Interdit d'en déduire un score.
- **Un signal déclaré n'est pas un signal actif** : 25 sur 72 sont dépréciés, et le schéma ne dit pas si les autres sont encore alimentés.
- Les signaux comportementaux sensibles et l'anti-spam sont derrière la frontière HIP : ce qui compte le plus est peut-être ce qu'on ne voit pas.
- Données d'août 2026, antérieures à l'annonce IA de Google du 6 août 2026.
- La causalité entre les pipelines de visite détectés et `POPULARITY` n'est pas démontrée.

## À relier
[[01-google-classement-local]] (la doctrine que ces signaux matérialisent), [[05-whitespark-lsrf-2026]] (la seule pondération disponible, par consensus), [[08-near-media-fuite-api-2024]] (l'autre fuite, côté Search), [[US8046371B2]] (le brevet dont les facteurs de proéminence recoupent les signaux présence web).
