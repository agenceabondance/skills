---
titre: Local Search Implications of the Google API Leak (+ Local SEO Guide, même fuite)
editeur: Near Media (David Mihm) ; complément Local SEO Guide (Andrew Shotland)
url: https://www.nearmedia.co/googles-api-leak-and-local-search/
url_complement: https://www.localseoguide.com/local-seo-according-to-the-leaked-google-api-documents/
type: Analyse
preuve: Schéma fuité
date_publication: 2024-06-04 (Near Media) ; 2024-05-29 MàJ 2024-07-19 (Local SEO Guide)
date_ajout: 2026-09-17
fiabilite: Haute
sujets: [fuite-api-2024, content-warehouse, clics, navboost, autorite-de-site, chaines, categories, intention-locale, citations, entites, page-atterrissage]
---

# La fuite API Google 2024, lue pour le local (Near Media)

## En une phrase
La fuite du Content Warehouse (mars-mai 2024, 2 500 documents, 14 014 attributs) confirme côté **Search** ce que le schéma Geostore montre côté **Maps** : les clics, l'autorité du site, les chaînes et les catégories sont des objets nommés du système.

## Ce qu'on en tire pour un audit
- **Clics géolocalisés** : `clickRadius50Percent` = le rayon (en miles) autour du lieu assigné dans lequel le document reçoit 50 % de ses clics. La marque a une empreinte géographique de clics ; une fiche ou un site cliqué de loin est lu comme « de marque ». Non actionnable directement ; explique pourquoi la notoriété élargit la zone de classement.
- **Autorité de site** : `siteAuthority` existe malgré les dénégations publiques. Le site lié à la fiche compte pour ce qu'il vaut dans Search. Actionnable (SEO classique).
- **Proéminence on-site** : `onsiteProminence`, calculée en propageant du trafic simulé depuis la page d'accueil et les pages à fort trafic. **Les pages locales doivent être liées depuis l'accueil**, pas enterrées. Actionnable.
- **Catégories et intention** : `gcidIntent`, `salientTermSet` ; Google tient des listes de catégories distinctes pour le commerce local et l'hôtellerie ; traitement particulier des catégories à fort volume (« hyperReliableData » : café, brunch, hôtel, restaurant).
- **Chaînes** : `LocationType` propre, module `LocalsearchChainId`, concepts canoniques. Un réseau de 17 circuits ou 23 crèches est vu comme une **chaîne** : cohérence des fiches entre elles, nom identique, catégorie identique.
- **Citations** : `LocalEntityAnnotations::location_confidence` ; Google extrait adresse, téléphone et horaires depuis le contenu web. **NAP cohérent** sur le site (schema LocalBusiness) et les annuaires d'autorité. Actionnable.
- **Territoire** : `inUserLocality`, facteur suspecté : être dans la localité de l'utilisateur.
- Local SEO Guide ajoute : un attribut `prominence` mesurant la pertinence relative d'une catégorie (GConcept) pour un établissement, ce qui peut départager catégorie principale et secondaires.

## Citations utiles
> "The radius (in miles) around the assigned location that the document gets 50% of its clicks" (définition de `clickRadius50Percent`)

> "the extent of entity-related references in the documentation almost seem to position content as context for entities, rather than the other way around"

## Ce que la source ne prouve pas
- **Pas de dates** : des références à Google+ et au Local Business Center subsistent ; on ne sait pas quels attributs sont vivants.
- **Pas de poids** : le nombre de mentions d'un attribut ne dit rien de sa valeur. Mihm : à utiliser « directionally, not as gospel ».
- Fuite partielle : des sous-API référencées ne sont pas dans le dump.
- Shotland le dit lui-même : 99 % du contenu local de la fuite concerne la cartographie, pas le classement des fiches ; sa liste de 461 attributs a été résumée par ChatGPT, il recommande de retourner aux sources.

## À relier
[[04-resoneo-google-map-dissected]] (la fuite jumelle côté Maps, plus récente et plus précise sur le ranking), [[01-google-classement-local]], [[US8046371B2]] (la « page autoritaire » d'un établissement dans le brevet, `SIGNAL_GOOGLE_AUTHORITYPAGE_*` dans le schéma).
