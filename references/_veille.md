# Veille des sources SEO local

Registre des sources en ligne à surveiller. But : détecter qu'une page a changé depuis son ajout, mettre à jour la fiche et sa `date_publication`, et le dire.

## Comment faire la veille (Mode C de la skill)

Pour chaque source ci-dessous :
1. Re-fetch l'URL (WebFetch).
2. Comparer aux **signaux de version** consignés.
3. Rien n'a changé : mettre à jour `dernière vérif`, ne pas toucher la fiche.
4. La page a changé : mettre à jour la fiche (points, citations, `date_publication`), actualiser les signaux ici, **signaler le diff à l'utilisateur**. Jamais de réécriture silencieuse.
5. Page inaccessible : le signaler, ne pas supprimer la fiche sans validation.

Les brevets ne se surveillent pas (texte figé) ; seul leur **statut** (annuités, expiration) peut bouger : `py scripts/brevet.py <numéro> --meta` le relit.

## Sources à surveiller

### 01 - Google, classement local
- URL : https://support.google.com/business/answer/7091?hl=fr
- Ajout : 2026-09-17 · Dernière vérif : 2026-09-17
- Signaux : trois facteurs pertinence / distance / proéminence ; six conseils (valider, informations à jour, attributs, répondre aux avis, photos et vidéos, produits) ; phrase « aucun moyen d'obtenir une meilleure place [...] contre rémunération ».

### 02 - Google, consignes de représentation
- URL : https://support.google.com/business/answer/3038177?hl=fr
- Ajout : 2026-09-17 · Dernière vérif : 2026-09-17
- Signaux : liste des interdits dans le nom (slogans, codes, symboles, majuscules, horaires, téléphone, URL, mentions légales, localisation, services) ; « le moins de catégories possible » ; règle nom différent pour un service au même lieu ; types sans horaires (hébergement, cinémas, écoles, aéroports).

### 03 - Google, contenus utilisateurs Maps
- URL : https://support.google.com/contributionpolicy/answer/7400114?hl=fr
- Ajout : 2026-09-17 · Dernière vérif : 2026-09-17
- Signaux : « expérience réellement vécue » ; interdiction des avantages contre avis ; interdiction de décourager les avis négatifs et de solliciter sélectivement ; sanctions jusqu'à clôture du compte.

### 04 - Resoneo, Google Map disséqué
- URL : https://think.resoneo.com/google-map-dissected/fr/ (archive : https://www.resoneo.com/archive/)
- Ajout : 2026-09-17 · Dernière vérif : 2026-09-17
- Signaux : 72 signaux dont 25 dépréciés ; 10 936 déclarations Geostore ; 5 083 appels / 86 584 résultats ; 15 tags retirés de RankDetailsProto ; données d'août 2026 ; 8 sections (Le socle ... Ce que cela change). Une nouvelle version après l'annonce IA du 6 août 2026 est probable.

### 05 - Whitespark, Local Search Ranking Factors
- URL : https://whitespark.ca/local-search-ranking-factors/
- Ajout : 2026-09-17 · Dernière vérif : 2026-09-17
- Signaux : édition 2026 publiée le 6 novembre 2025 ; 47 experts, 187 facteurs ; top 3 = catégorie principale (227), proximité (225), mots-clés dans le nom (223) ; « ouvert à l'heure de la recherche » nouveau rang 5. **Édition annuelle** : une édition 2027 est attendue vers novembre 2026, elle remplace la fiche.

### 06 - Sterling Sky, near me 2025
- URL : https://www.sterlingsky.ca/what-gets-you-ranking-for-near-me-2025/
- Ajout : 2026-09-17 · Dernière vérif : 2026-09-17
- Signaux : 8 186 fiches, 200 villes, 5 requêtes, publié le 5 novembre 2025, partenariat Places Scout.

### 07 - Sterling Sky, services
- URL : https://www.sterlingsky.ca/services-in-google-business-profile-impact-ranking/
- Ajout : 2026-09-17 · Dernière vérif : 2026-09-17
- Signaux : date affichée 27 février 2026 ; effet en 24 à 72 h ; services personnalisés « currently testing ». Un résultat publié sur les services personnalisés = mise à jour de la fiche.

### 08 - Near Media, fuite API
- URL : https://www.nearmedia.co/googles-api-leak-and-local-search/
- Ajout : 2026-09-17 · Dernière vérif : 2026-09-17
- Signaux : 4 juin 2024, David Mihm ; attributs clickRadius50Percent, onsiteProminence, siteAuthority, gcidIntent, LocalsearchChainId, inUserLocality. Page d'analyse figée a priori.
