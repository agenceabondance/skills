# Règles on-page SEO et orthographe française

À appliquer sur 100% des champs éditoriaux du livrable (Titles, Meta descriptions, H1, H2, H3, angles éditoriaux, plans, justifications, descriptions concurrents).

## 1. Title

### Contraintes strictes
- Longueur maximum : **60 caractères espaces inclus** (compter rigoureusement)
- Mot-clé principal placé **en début** de title
- Élément différenciant en fin (bénéfice, certification, géolocalisation, marque)
- Séparateurs autorisés : ":" ou "|" (jamais le tiret cadratin U+2014)
- Accents conservés impérativement (Google les affiche, les utilisateurs les recherchent)

### Méthodologie de génération (5 étapes)
1. Appeler `get_keywords_overview` avec `requested_data` incluant `serp` sur le mot-clé principal
2. Extraire les titles des 3 URLs en positions 1, 2 et 3
3. Identifier les éléments communs (structure, bénéfices, modificateurs)
4. Identifier les éléments différenciants de chaque concurrent
5. Rédiger un title original qui s'inspire de la structure sans copier, et documenter les 3 sources dans le brief

### Format type
`[Mot-clé principal] : [bénéfice/angle différenciant] | [Marque]`

### Exemples
Valides :
- "Datacenter France souverain : hébergement HDS | Orbite" (54 c.)
- "Colocation datacenter Toulouse : baies haute densité" (52 c.)

À corriger :
- "Le meilleur datacenter en France pour héberger vos serveurs en toute sécurité" (78 c., trop long)
- "Solution souveraine de datacenter en France" (mot-clé pas en début)

### Compression si dépassement
Dans l'ordre : (a) retirer la marque, (b) raccourcir l'élément différenciant, (c) abréviation reconnue (HDS plutôt que la forme longue), (d) réduire à un seul mot-clé fort.

## 2. Meta description

### Contraintes strictes
- Longueur maximum : **155 caractères espaces inclus**
- Mot-clé principal présent une fois minimum (deux maximum)
- Pain point du persona ciblé adressé explicitement
- CTA explicite en fin, adapté à l'intention :
  - Informationnelle TOFU : "Découvrez", "Comprenez", "Explorez"
  - Commerciale MOFU : "Comparez", "Évaluez", "Découvrez nos solutions"
  - Transactionnelle BOFU : "Demandez un devis", "Contactez-nous", "Réservez une visite"
  - BOFU garanties : "Consultez nos engagements"
- Style actif, verbes forts, aucune formule creuse

### Exemples
Valides :
- "Datacenter France certifié HDS : hébergement souverain, conformité RGPD, SLA Tier III. Découvrez nos solutions de colocation à Toulouse." (136 c.)

À corriger :
- "Notre datacenter est le meilleur de France et propose des services de qualité pour tous les besoins des entreprises modernes." (formulation creuse)

### Compression si dépassement
Prioriser dans l'ordre : (a) mot-clé principal, (b) bénéfice différenciant, (c) CTA. Supprimer adverbes et formules de transition.

## 3. Orthographe française (applicable partout)

- **Accents obligatoires** sur toutes les voyelles concernées : é, è, ê, ë, à, â, ä, î, ï, ô, ö, û, ü, ù
- **Majuscules accentuées obligatoires** : É, È, Ê, À, Â, Î, Ô, Û, Ç (ex : "ÉTAT", "À LA UNE", "ÉVALUATION")
- **Cédilles** : ç et Ç quand requis ("Français", "reçu", "Ça")
- **Ligatures** recommandées dans le corps de texte : œ, æ ("œuvre", "cœur")
- **Apostrophes** : typographique ' (U+2019) dans le rédactionnel ; droite ' acceptée dans les champs techniques (slugs, formules Excel, variables)
- **Guillemets** : français « ... » dans les contenus longs ; droits acceptés en Title/Meta pour compatibilité moteurs
- **Espaces insécables** avant ; : ! ? dans le rédactionnel long ; espace simple toléré en Title/Meta par contrainte technique
- **Anglicismes** : proscrits quand un équivalent français courant existe ; autorisés pour les termes métier que les utilisateurs recherchent réellement (datacenter, cloud, edge computing, peering, smart hands)

### Mots à fort risque d'oubli d'accent
à/a, où/ou, déjà, été, hébergement, données, sécurité, certifié, opérateur, intégration, référencement, méthodologie, stratégie, créé, dédié.

### Exceptions et cas particuliers
- **Slugs URL : SANS accent** ("/securite-datacenter" et non "/sécurité-datacenter"). C'est la SEULE exception.
- **Colonne "Mot-clé" du tableau maître** : conserver la forme brute de recherche (souvent sans accent) car elle reflète la requête utilisateur réelle. En revanche, Title, Meta, H1, H2, H3 sont TOUJOURS accentués correctement.
- **Données Haloscan sans accents** : restaurer les accents lors de la transposition dans tout champ éditorial.

### Passe finale obligatoire
Avant livraison, relire l'intégralité des champs textuels pour traquer les oublis d'accent et les majuscules non accentuées.
