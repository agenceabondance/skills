# Spécification du livrable XLSX

Fichier : `cocon_semantique_[nom-projet].xlsx`, généré avec openpyxl, format .xlsx uniquement (jamais .xlsm). Si un skill `xlsx` est disponible dans l'environnement (sur claude.ai et Claude Desktop : `/mnt/skills/public/xlsx/SKILL.md`), le lire avant d'écrire le code ; en son absence (Claude Code en local), générer directement avec openpyxl.

## Structure : 10 feuilles dans cet ordre exact

| # | Nom de l'onglet | Contenu | Couleur onglet |
|---|---|---|---|
| 1 | 0_Légende | Codes couleur + glossaire | Gris |
| 2 | 1_Cadrage_Strategique | Audit site + pilier | Bleu |
| 3 | 2_Benchmark_Concurrents | 7 concurrents + carte + axes | Bleu |
| 4 | 3_Gap_Analysis_QuickWins | ≥ 50 quick wins | Vert |
| 5 | 4_Tableau_Maitre_MotsCles | ≥ 300 mots-clés, 21 colonnes | Vert |
| 6 | 5_Anti_Cannibalisation | Paires arbitrées | Orange |
| 7 | 6_Architecture_Cocon | ≥ 50 pages + parcours personas | Orange |
| 8 | 7_Briefs_Pages | 24 colonnes par page | Jaune |
| 9 | 8_Priorisation_Planning | Scores + vagues 12 mois | Jaune |
| 10 | 9_Sources_Haloscan | Traçabilité des appels | Violet |

## Feuille 1 : 0_Légende (8 sections)

Chaque section affiche des cellules colorées d'exemple avec le code hexadécimal.

**A. Intention** : Informationnelle #B4D7FF, Commerciale #FFD9B4, Transactionnelle #C6EFCE, Navigationnelle #D9D9D9
**B. Funnel** : TOFU #E2EFDA, MOFU #FFF2CC, BOFU #FCE4D6
**C. Personas** : un code couleur par persona défini en Phase 0 (défauts B2B IT : DIRECTION_GENERALE #D5A6BD, DIRECTION_IT_TECHNIQUE #9FC5E8, MANAGEMENT_INFRA_RESEAUX #A2C4C9, PRODUCTION_OPERATIONS #B6D7A8)
**D. Types d'article** : What is #9FC5E8, How to #B4A7D6, Comparative #FFE599, Top #D5A6BD, Review #EA9999, Interview #F9CB9C, Generalist #B6D7A8, Landing #E06666
**E. Score de priorité** : ≥ 10 #38761D (HAUTE), 6 à 9 #F1C232 (MOYENNE), < 6 #E06666 (BASSE)
**F. Couverture concurrentielle** : 0 à 2/7 #38761D (ESPACE BLANC), 3 à 4/7 #F1C232 (MIXTE), 5 à 7/7 #E06666 (SATURÉ)
**G. Similarité SERP** : ≥ 60% #E06666 (FUSION), 30 à 59% #F6B26B (ZONE GRISE), < 30% #93C47D (SÉPARATION)
**H. Glossaire** : KGR, KVI, allintitle, SERP, PAA, TOFU/MOFU/BOFU + acronymes du secteur analysé.
Y inscrire explicitement : « Haloscan n'expose aucun indice de difficulté (KD). La difficulté est
qualifiée par le KGR = allintitle / volume. Seuil de référence : KGR <= 0,25 = peu concurrentiel. »

## Feuille 2 : 1_Cadrage_Strategique

Colonnes : Élément | Valeur | Source Haloscan | Date analyse.
Lignes : URL site, trafic SEO mensuel, KW positionnés, position moyenne, top 20 KW actuels (1 ligne chacun), top 10 pages, mot-clé pilier + volume + KGR + tendance, persona principal/secondaire du pilier, promesse différenciante, angle éditorial pilier.

## Feuille 3 : 2_Benchmark_Concurrents

Colonnes : Concurrent | URL | Statut (Pré-identifié/Découvert) | Trafic SEO | KW positionnés | Position moyenne | Pays principal | Top intention | Persona dominant | Angle éditorial | Forces SEO | Faiblesses SEO | Top 5 pages (séparées par ;) | Mots-clés stars (top 5, séparés par ;) | Opportunité gap | Limite données (si audit manuel).

Sous le tableau : bloc carte de positionnement éditorial (4 quadrants avec concurrents placés) + bloc 3 axes différenciants recommandés avec justifications.

## Feuille 4 : 3_Gap_Analysis_QuickWins

Colonnes : Mot-clé | Volume | KGR | Tendance | Catégorie (TOFU/MOFU/BOFU) | Persona cible | Intention | Concurrents positionnés | Meilleure position concurrente | Type d'article | Cluster cible | Priorité (1-5) | Effort (1-5) | Score opportunité | Page concurrente référence.

Mise en forme : Score opportunité en gradient vert→rouge, Persona et Catégorie colorés selon la légende.

## Feuille 5 : 4_Tableau_Maitre_MotsCles (21 colonnes)

ID | Mot-clé | Volume | KGR | Tendance 12 mois | SERP features | Intention | Funnel | Persona principal | Persona secondaire | Type d'article | Cluster | **Statut KW** (Principal/Secondaire fort/Secondaire faible/Orphelin) | **KW principal de rattachement** | **Similarité SERP avec principal** | Couverture concurrentielle (0-7) | Concurrents positionnés | Questions PAA | KW sémantiquement liés | Source Haloscan | Date extraction.

Mise en forme conditionnelle :
- Intention, Funnel, Personas, Type : couleurs de la légende
- Statut KW : Principal vert foncé, Secondaire fort vert clair, Secondaire faible jaune, Orphelin rouge
- Similarité SERP : gradient vert (haut) → rouge (bas)
- Couverture : gradient section F
- Volume : gradient bleu clair → bleu foncé
- KGR : gradient vert (KGR bas = facile, <= 0,25) → rouge (KGR élevé = difficile). Attention au sens : contrairement à un KD, un KGR bas est favorable
- Filtres automatiques, volet figé ligne 1 + colonne B

## Feuille 6 : 5_Anti_Cannibalisation

Colonnes : Paire ID | KW A | KW B | Volume A | Volume B | Similarité SERP % | Persona A | Persona B | URLs communes top 5 | Décision | Justification | Action recommandée.
Mise en forme : Similarité en gradient section G, Décision colorée (Fusion rouge, Zone grise orange, Séparation vert).

## Feuille 7 : 6_Architecture_Cocon

Colonnes : Niveau (1/2/3) | ID page | Cluster | Titre H1 | URL slug | Mot-clé principal | Volume | Type | Intention | Funnel | Persona principal | Persona secondaire | Pages parentes | Pages enfants | Pages sœurs | Maillage transversal.
Ligne du pilier (Niveau 1) en gras sur fond gris foncé.
Sous le tableau : un mini-tableau "Parcours" par persona listant la séquence TOFU → MOFU → BOFU.

## Feuille 8 : 7_Briefs_Pages (24 colonnes)

1. ID page | 2. URL cible | 3. Title (≤60 c.) | 4. **Longueur Title** | 5. H1 | 6. Meta description (≤155 c.) | 7. **Longueur Meta** | 8. KW principal + volume + KGR | 9. KW secondaires forts (sim ≥ 60%) | 10. KW secondaires faibles (sim 40-59%) | 11. Questions PAA | 12. Type | 13. Intention | 14. Funnel | 15. Persona principal | 16. Persona secondaire | 17. Angle éditorial | 18. Ton | 19. Plan H2/H3 (secondaires forts en H2, faibles en H3) | 20. Maillage entrant | 21. Maillage sortant | 22. Schema.org | 23. Référence concurrentielle | 24. Sources d'inspiration Title (3 URLs top 3 + leurs titles).

Formules de validation OBLIGATOIRES (adapter les lettres de colonnes) :
- Longueur Title : `=SI(NBCAR(C2)<=60;"OK";"DÉPASSEMENT")` avec MFC : OK vert, DÉPASSEMENT rouge
- Longueur Meta : `=SI(NBCAR(F2)<=155;"OK";"DÉPASSEMENT")` avec MFC identique
- En openpyxl, écrire les formules en syntaxe anglaise : `=IF(LEN(C2)<=60,"OK","DÉPASSEMENT")`

Largeurs : URL 30, Title 50, Meta 50, KW secondaires 35, Plan H2/H3 60, Sources Title 60, autres 20. Renvoi à la ligne automatique partout, volet figé ligne 1 + colonne B.

## Feuille 9 : 8_Priorisation_Planning

Colonnes : ID page | KW principal | Volume | KGR | Persona | Funnel | Potentiel (1-5) | Difficulté (1-5) | Effort (1-5) | Stratégicité persona (0/+1) | Opportunité concurrentielle (0/+2) | Score final | Vague (1/2/3) | Mois cible | Statut production.
Tri par score décroissant. Score final en gradient section E. Vague colorée (1 vert foncé, 2 bleu, 3 gris). Statut en liste déroulante (À faire / En cours / Publié / Optimisé). Sous le tableau : compteurs de pages par vague.

## Feuille 10 : 9_Sources_Haloscan

Colonnes : N° appel | Outil | Paramètre d'entrée | Date | Nombre de résultats | Phase associée | Usage.
Listing chronologique exhaustif : traçabilité totale du livrable.

## Règles techniques transverses

- Police Calibri 11
- En-têtes : gras, fond #404040, texte blanc, hauteur 30 px
- Bordures fines noires sur toutes les cellules de données
- Filtres automatiques sur toutes les feuilles tabulaires
- Volets figés : ligne 1 partout ; colonne B en plus sur les feuilles 4, 5, 7, 8, 9
- Nombres : volume avec séparateur de milliers, KGR à 4 décimales (ratio, non borné à 1), similarité SERP en % (score 0-1 formaté), pourcentages en %
- Hyperliens cliquables sur toutes les URLs
- Cellules limitées à 32 767 caractères (tronquer au-delà)
- Métadonnées : auteur, titre du projet, sujet "Stratégie SEO 12 mois"
- Aucun tiret cadratin (U+2014) nulle part
