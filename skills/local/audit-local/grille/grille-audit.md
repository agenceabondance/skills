# Grille d'audit d'une fiche Google Business Profile

Une ligne par contrôle. Chaque contrôle porte sa source (`[NN]` = source du corpus, `[USxxxx]` = brevet), son **niveau de preuve** (voir la skill `sourcer`) et dit si le propriétaire peut agir. **Pas de score global** : les poids sont inconnus ([04]), on rend un verdict par famille.

**Colonne « Comment »** : où prendre la donnée.

| Code | Source de la donnée | Accès nécessaire |
|---|---|---|
| **M** | À la main : lecture de la fiche sur Maps, ou de l'interface de gestion | Aucun (Maps) ou propriétaire (interface) |
| **P** | `scripts/places.py` (Places API, donnée publique) | Une clé Google Cloud à soi, aucun accès à la fiche du client |
| **E** | Export CSV de l'interface Fiche d'établissement (onglet Performances, ou export en masse pour un réseau) | Propriétaire ou gestionnaire |
| **G** | GA4 / Search Console du site (trafic issu de la fiche via UTM, requêtes locales) | Accès aux outils de mesure du site |
| **K** | Suivi de positions Maps (Monitorank ou grille géographique) | Compte Monitorank |

**Ordre de lecture obligatoire** : la famille A avant tout. Un point A en échec prime sur toute optimisation : on corrige la conformité, puis on optimise.

**Verdict par famille** : ✅ conforme / rien à faire · 🟠 à améliorer · 🔴 bloquant ou risque de suspension · ⚪ non vérifié (dire pourquoi : pas d'accès, pas de donnée).

---

## A. Conformité (risque de suspension)

| # | Contrôle | Comment | Sources | Preuve | Actionnable |
|---|---|---|---|---|---|
| A1 | L'établissement est **éligible** : accueil de clients sur place ou intervention chez eux ; pas de boîte postale, domiciliation ni coworking sans enseigne | M | [02] | Officiel | Oui |
| A2 | La fiche est **validée** (revendiquée et vérifiée) | M (interface) | [01] | Officiel | Oui |
| A3 | Le **nom** est le nom réel : pas de mot-clé, ville, slogan, mention légale, téléphone, URL, majuscules intégrales | M, P | [02] | Officiel | Oui |
| A4 | Entreprise de service à domicile : **adresse masquée** et zone desservie définie ; établissement avec accueil : adresse affichée | M | [02], [05] (risque 105/115) | Officiel + Consensus | Oui |
| A5 | **Zones desservies** : pas de chevauchement entre fiches d'un même réseau, pas de zone à plus de 2 h de route | M | [05] (risques 102, 82) | Consensus | Oui |
| A6 | Le **site web** de la fiche ne redirige pas vers un autre domaine ; le **téléphone** est local, pas surtaxé, pas un centre d'appels | M, P | [02], [05] (risque 115) | Officiel + Consensus | Oui |
| A7 | **Description, posts** : pas de bourrage de mots-clés ; **photos** : pas d'images générées par IA présentées comme réelles | M | [02], [05] (risques 35, 51, 45, 25) | Officiel + Consensus | Oui |
| A8 | **Doublons** : pas de seconde fiche pour le même établissement, pas de fiche par spécialité pour un professionnel | P (recherche par nom + ville), M | [02] | Officiel | Oui |
| A9 | Pratique de **collecte d'avis** conforme : aucune contrepartie, pas de tri des clients, pas d'avis internes | M (entretien client) | [03] | Officiel | Oui |

## B. Complétude de la fiche

| # | Contrôle | Comment | Sources | Preuve | Actionnable |
|---|---|---|---|---|---|
| B1 | **Catégorie principale** = ce que l'établissement est, la plus précise disponible | M, P | [01], [02], [05] (rang 1), [04] (PRIMARY) | Officiel + Consensus + Schéma | Oui |
| B2 | **Catégories secondaires** pertinentes, sans en abuser (Google : le moins possible ; experts : rang 8) | M, P | [02], [05] | Officiel + Consensus | Oui |
| B3 | **Horaires** exacts, y compris horaires spéciaux (fériés, saison) ; vérifier que l'établissement est ouvert aux heures où on le cherche | M, P | [01], [05] (rang 5) | Officiel + Consensus | Oui |
| B4 | **Services** : les services prédéfinis de la catégorie sont cochés quand ils correspondent à l'offre réelle | M (interface) | [07], [05] (rang 22) | Empirique | Oui |
| B5 | **Attributs** renseignés (accès, paiement, équipements, public) | M, P | [01] | Officiel | Oui |
| B6 | **Description** présente, factuelle, sans bourrage | M | [01], [02] | Officiel | Oui |
| B7 | **Photos** : volume, fraîcheur (dernière photo), diversité (extérieur, intérieur, équipe, prestation) ; **photo de couverture et logo** | M, P (nombre, plafonné à 10) | [01], [05] | Officiel + Consensus | Oui |
| B8 | **Produits / offres** renseignés quand l'activité s'y prête | M | [01] | Officiel | Oui |
| B9 | **Repère sur la carte** placé sur l'entrée réelle | M | [05] (rang 10), [US8898173B1] | Consensus + Brevet | Oui |
| B10 | **Site web** renseigné, pointant vers la page de l'établissement (pas seulement l'accueil pour un réseau) | M, P | [01], [04] (`HOMEPAGE_CLICKS`), [US8046371B2] | Officiel + Schéma + Brevet | Oui |
| B11 | **Questions-réponses** : questions posées par le public ont une réponse du propriétaire (hors corpus : aucune source sur l'effet) | M | (hors corpus) | - | Oui |

## C. Avis

| # | Contrôle | Comment | Sources | Preuve | Actionnable |
|---|---|---|---|---|---|
| C1 | **Volume** d'avis Google, comparé aux concurrents du pack sur les mêmes requêtes | P, M | [05] (rang 9), [04] (`SIGNAL_GOOGLE_REVIEWS`) | Consensus + Schéma | Partiel |
| C2 | **Note moyenne**, comparée aux concurrents | P, M | [05] (rang 6), [06] | Consensus + Empirique | Partiel |
| C3 | **Cadence** : avis réguliers chaque mois, pas un stock ancien qui dort ; date du dernier avis | M (dates des avis), P (5 avis les plus pertinents : borne basse) | [06] | Empirique | Partiel |
| C4 | **Part d'avis avec texte** ; mots-clés de la prestation présents naturellement dans les textes | M, P (échantillon) | [06], [US10394830B1], [04] (sentiment par thème) | Empirique + Brevet + Schéma | Partiel |
| C5 | **Réponses du propriétaire** : taux de réponse, délai, ton, y compris sur les avis négatifs | M, P (échantillon) | [01] | Officiel | Oui |
| C6 | **Qui écrit** : part de contributeurs actifs (Local Guides, profils avec historique) vs profils vides | M | [US10929409B2] | Brevet | Non |
| C7 | **Avis hors Google** (plateformes métier, annuaires) : existence et volume | M | [US8046371B2] (rev. 7) | Brevet | Partiel |
| C8 | **Signaux de fraude** chez le client ou ses concurrents : pics groupés, 5 étoiles sans texte, profils sans autre contribution | M | [03] | Officiel | Signalement |

## D. Pertinence (requête ↔ fiche)

| # | Contrôle | Comment | Sources | Preuve | Actionnable |
|---|---|---|---|---|---|
| D1 | Les **requêtes cibles** sont listées et qualifiées : intention locale forte (« + ville », « près de moi ») ou faible (générique) | G, K | [US8171048B2], [US11893034B2], [08] (`gcidIntent`) | Brevet + Schéma | Cadrage |
| D2 | La catégorie principale correspond à la **catégorie des fiches qui rankent** sur les requêtes cibles | P (catégories du pack) | [05] (rang 1), [08] | Consensus + Schéma | Oui |
| D3 | Les requêtes explicites (nom d'un service) ont leur **service** coché | M | [07] | Empirique | Oui |
| D4 | La fiche est **ouverte** aux heures de pointe des requêtes (croiser horaires et courbe horaire des impressions) | E, M | [05] (rang 5) | Consensus | Oui |

## E. Distance et territoire

| # | Contrôle | Comment | Sources | Preuve | Actionnable |
|---|---|---|---|---|---|
| E1 | Pour chaque ville visée : l'adresse est **dans la commune** ou hors commune (auquel cas ne rien promettre sur le pack de cette ville) | M (carte) | [US8898173B1], [05] (rang 4) | Brevet + Consensus | Non |
| E2 | Les positions sont lues **par point de mesure**, pas par requête seule (grille géographique ou plusieurs villes Monitorank) | K | [US11893034B2], [05] (rang 2) | Brevet + Consensus | Cadrage |
| E3 | Pour un réseau : chaque établissement couvre **sa** zone, sans concurrence interne entre fiches sur les mêmes requêtes | K, P | [04] (chaînes), [08] | Schéma | Oui |

## F. Proéminence web (le site et les citations)

| # | Contrôle | Comment | Sources | Preuve | Actionnable |
|---|---|---|---|---|---|
| F1 | La **page d'atterrissage** liée à la fiche existe, porte le NAP identique, du contenu réel sur l'établissement, et le balisage `LocalBusiness` (ou sous-type) | M, crawl | [06], [08], [US8046371B2], [US8171048B2] | Empirique + Schéma + Brevet | Oui |
| F2 | Les pages locales sont **liées depuis l'accueil** ou une page à fort trafic (pas enterrées à 4 clics) | crawl | [08] (`onsiteProminence`) | Schéma | Oui |
| F3 | **NAP cohérent** sur le site, la fiche et les annuaires d'autorité du secteur ; corriger les variantes de nom, d'adresse, de téléphone | M, P | [US8046371B2], [08] (`location_confidence`), [05] | Brevet + Schéma + Consensus | Oui |
| F4 | **Citations** : présence sur les quelques annuaires d'autorité du métier et de la zone (qualité, pas volume) | M | [05], [US8046371B2] | Consensus + Brevet | Oui |
| F5 | **Autorité du site** et **notoriété de marque** (requêtes sur le nom dans GSC, volume de recherche du nom) | G, Ahrefs | [04] (`WEB_QUERYVOL`, `AUTHORITYPAGE_PAGERANK_CONFIDENCE`), [08] (`siteAuthority`), [01] | Schéma + Officiel | Partiel (SEO classique) |
| F6 | **Wikipédia / Wikidata** : existence d'une entrée pour la marque (réseaux, marques notoires seulement) | M | [04] (`WIKIPEDIA_ARTICLES`) | Schéma | Rarement |

## G. Engagement (les métriques Performances)

Ces chiffres ne s'obtiennent qu'avec l'accès à la fiche (E) ; sans accès, la famille est ⚪ et le dire.

| # | Contrôle | Comment | Sources | Preuve | Actionnable |
|---|---|---|---|---|---|
| G1 | **Vues / impressions** de la fiche (Recherche et Maps), tendance sur 12 mois | E | [04] (`LISTING_IMPRESSIONS`, `INFOWINDOW_VIEWS`) | Schéma | Indirect |
| G2 | **Demandes d'itinéraire** et **appels** | E | [04] (`DIRECTION_REQUESTS`), [05] | Schéma + Consensus | Indirect |
| G3 | **Clics vers le site** ; recoupés avec le trafic UTM de la fiche dans GA4 | E, G | [04] (`HOMEPAGE_CLICKS`) | Schéma | Indirect |
| G4 | **Requêtes ayant déclenché la fiche** (onglet Performances) : part marque / hors marque | E | [04] | Schéma | Cadrage |
| G5 | **Cadence de publication** : posts, photos, réponses sur les 90 derniers jours (« la fiche a l'air vivante ») | M, E | [05] | Consensus | Oui |

## H. Concurrence

| # | Contrôle | Comment | Sources | Preuve | Actionnable |
|---|---|---|---|---|---|
| H1 | Pour chaque requête cible × ville : les **3 à 10 fiches du pack**, avec note, volume d'avis, catégorie principale, photos, site | P | [05], [06] | Consensus + Empirique | Comparaison |
| H2 | **Écart** du client à la médiane du pack sur note, avis, cadence, photos | P | [06] | Empirique | Comparaison |
| H3 | Concurrents en **infraction** (mot-clé dans le nom, doublons, avis suspects) : documenter pour signalement | P, M | [02], [03] | Officiel | Signalement |

## I. Multi-établissements (réseaux)

| # | Contrôle | Comment | Sources | Preuve | Actionnable |
|---|---|---|---|---|---|
| I1 | **Cohérence** des fiches du réseau : même modèle de nom (« Marque - Ville »), même catégorie principale, même structure | P (toutes les fiches), E | [04] (`CHAIN_STORES`), [08] (`LocalsearchChainId`) | Schéma | Oui |
| I2 | **Une page d'atterrissage par établissement**, liée depuis sa fiche | M, crawl | [06], [08] | Empirique + Schéma | Oui |
| I3 | **Pas de fiche orpheline** (fermée, non revendiquée, en doublon) ni d'établissement sans fiche | P (recherche par ville), E | [02] | Officiel | Oui |
| I4 | **Homogénéité de traitement** : écarts d'avis, de photos, de réponses entre établissements (les retardataires) | P, E | [05] | Consensus | Oui |

---

## Ce que la grille ne fait pas

- Elle ne donne **pas de score sur 100** et ne classe pas les familles entre elles : les poids ne sont pas connus ([04]). Le livrable donne un verdict par famille et une priorisation des actions par (risque, effort, niveau de preuve).
- Elle ne remplace pas le **suivi de positions** : elle dit quoi corriger, Monitorank dit si ça a bougé.
- Un point ⚪ reste ⚪ : ne jamais présenter comme vérifié un point qu'on n'a pas pu observer.
