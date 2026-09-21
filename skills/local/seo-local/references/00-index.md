# Index du corpus SEO local

Une ligne par source. Lu en premier pour router vers les bonnes sources. La colonne **Preuve** porte le niveau de preuve de chaque source, défini dans la skill `sourcer` (Officiel, Empirique, Consensus, Schéma fuité, Brevet, Analyse) ; c'est la colonne qui manque partout ailleurs, et la raison d'être de ce corpus.

## Sources

| N° | Source | Titre | Éditeur | Type | Preuve | Publié | Ajouté | Fiabilité | Sujets |
|----|-------|-------|---------|------|--------|--------|--------|-----------|--------|
| 01 | [01-google-classement-local](01-google-classement-local.md) | Améliorer votre classement local sur Google | Google | Doc officielle | Officiel | non datée | 2026-09-17 | Haute | pertinence, distance, proeminence, fiche-complete, avis, photos, horaires |
| 02 | [02-google-regles-representation](02-google-regles-representation.md) | Consignes de représentation d'un établissement | Google | Doc officielle | Officiel | non datée | 2026-09-17 | Haute | nom, adresse, categories, telephone, site-web, horaires, eligibilite, suspension, multi-etablissements |
| 03 | [03-google-regles-contenus-utilisateurs](03-google-regles-contenus-utilisateurs.md) | Règles des contenus utilisateurs Maps (avis) | Google | Doc officielle | Officiel | non datée | 2026-09-17 | Haute | avis, sollicitation, faux-avis, incitation, suspension |
| 04 | [04-resoneo-google-map-dissected](04-resoneo-google-map-dissected.md) | Google Map disséqué, les 72 signaux d'Oyster Rank | Resoneo | Étude | Schéma fuité | 2026-08 | 2026-09-17 | Haute | oyster-rank, engagement, avis, categories, chaines, presence-web, poids-inconnus |
| 05 | [05-whitespark-lsrf-2026](05-whitespark-lsrf-2026.md) | Local Search Ranking Factors 2026 | Whitespark | Étude | Consensus | 2025-11-06 | 2026-09-17 | Haute | ponderation, top-facteurs, categorie-principale, horaires, avis, services, facteurs-negatifs |
| 06 | [06-sterling-sky-near-me-2025](06-sterling-sky-near-me-2025.md) | 8 186 fiches, 200 villes : ce qui classe sur « near me » | Sterling Sky | Étude | Empirique | 2025-11-05 | 2026-09-17 | Haute | avis, cadence-avis, avis-avec-texte, adresse-masquee, page-atterrissage |
| 07 | [07-sterling-sky-services](07-sterling-sky-services.md) | Les Services de la fiche influencent-ils le classement ? | Sterling Sky | Test | Empirique | 2026-02-27 | 2026-09-17 | Moyenne | services, services-predefinis, delai-effet |
| 08 | [08-near-media-fuite-api-2024](08-near-media-fuite-api-2024.md) | La fuite API 2024 lue pour le local | Near Media (+ Local SEO Guide) | Analyse | Schéma fuité | 2024-06 | 2026-09-17 | Haute | clics, autorite-de-site, chaines, categories, citations, entites |

## Brevets (`brevets/`)

Périmètre : brevets dont le déposant est Google, qui décrivent un mécanisme de classement **local** (fiches, lieux, distance, avis). Lus sur pièces avec la skill `brevet-google`.

| Numéro | Source | Titre | Priorité | Publié | Statut | Sujets |
|---|---|---|---|---|---|---|
| US8046371B2 | [US8046371B2](brevets/US8046371B2.md) | Scoring local search results based on location prominence | 2005 | 2011 | Expiré (terme 2025) | proeminence, page-autoritaire, citations, avis |
| US8898173B1 | [US8898173B1](brevets/US8898173B1.md) | Ranking location search results based on multiple distance measures | 2010 | 2014 | Expiré (annuités) | distance, requete-ville, polygone, centre-ville |
| US11893034B2 | [US11893034B2](brevets/US11893034B2.md) | Distance based search ranking demotion | 2013 | 2024 | Actif | distance, retrogradation, intention-locale |
| US10394830B1 | [US10394830B1](brevets/US10394830B1.md) | Sentiment detection as a ranking signal for reviewable entities ⚠️ revendications délivrées sur les interactions, pas le sentiment | 2007 | 2019 | Actif | avis, sentiment, texte-des-avis |
| US10929409B2 | [US10929409B2](brevets/US10929409B2.md) | Identifying local experts for local search | 2013 | 2021 | Expiré (annuités) | avis, experts-locaux, categorie, personnalisation |
| US8171048B2 | [US8171048B2](brevets/US8171048B2.md) | Ranking documents based on a location sensitivity factor | 2003 | 2012 | Expiré (annuités) | intention-locale, pages-locales, resultats-web |

## Repères de routage

| La question porte sur | Lire d'abord |
|---|---|
| Ce que Google dit officiellement du classement | 01 |
| Le nom, l'adresse, les catégories, l'éligibilité, un risque de suspension | 02, 05 (facteurs négatifs) |
| Les avis : ce qu'on a le droit de faire | 03 |
| Les avis : ce qui compte (volume, cadence, texte, qui les écrit) | 06, US10394830B1, US10929409B2, 04, 05 |
| Quels signaux existent vraiment chez Google | 04, 08 |
| Quel facteur pèse le plus (au dire des experts) | 05 |
| Les services de la fiche | 07, 05 |
| La distance, une requête « + ville », un établissement hors commune | US8898173B1, US11893034B2, 05 |
| Les pages locales du site, l'intention locale d'une requête | US8171048B2, 08, 05 |
| La proéminence, les citations NAP, le site lié | US8046371B2, 01, 08, 04 |
| Les chaînes / réseaux multi-établissements | 04, 08, 02 |
| Les métriques Performances de la fiche (vues, itinéraires, clics) | 04 |

## Trous connus du corpus (à combler quand une source fiable se présente)

- Aucune source française sur les requêtes « métier + ville » (les tests empiriques sont américains, sur « near me »).
- Aucun test publié sur l'effet des **posts** et des **photos** sur le classement (uniquement du consensus, source 05).
- Aucune source sur les **questions-réponses** de la fiche.
- Aucune source sur le comportement du pack local dans les **AI Overviews / Mode IA** ; la skill `geo` (sa source 11) note que le local est un des secteurs touchés.
