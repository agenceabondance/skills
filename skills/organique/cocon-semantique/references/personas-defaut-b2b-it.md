# Personas par défaut B2B IT

Ces 4 groupes couvrent la chaîne de décision IT classique (infrastructure, datacenter, cloud, hébergement, cybersécurité, SaaS technique). Les proposer en Phase 0 quand le secteur s'y prête ; sinon, construire des personas spécifiques sur le même gabarit (profil, préoccupations, funnel dominant, intentions, formats, ton, mots-clés types).

Chaque page du cocon reçoit un persona principal et éventuellement un secondaire. Chaque cluster mobilise au minimum 2 personas. Chaque persona doit disposer d'au moins 8 pages dédiées dans l'architecture finale.

## Groupe 1 : DIRECTION_GENERALE

- **Fonctions** : CEO, PDG, Directeur Général, Founder & CEO, Founder & CTO
- **Profil** : décisionnaire ultime ; vision stratégique, ROI, risque, compétitivité
- **Préoccupations** : souveraineté des données et risque géopolitique, conformité (RGPD, NIS2, DORA), continuité d'activité, coûts globaux (CAPEX vs OPEX, TCO), image de marque, différenciation par l'IT
- **Funnel dominant** : TOFU (veille stratégique) et BOFU (signature finale)
- **Intentions dominantes** : Informationnelle + Transactionnelle de décision
- **Formats préférés** : livres blancs, études sectorielles, articles de fond, cas clients portés par des dirigeants
- **Ton** : stratégique, business, peu technique, factuel
- **Mots-clés types** : "souveraineté numérique enjeux", "risques cloud américain entreprise", "coût total possession [solution]", "RGPD hébergement données"
- **CTA adaptés** : demande de rendez-vous, téléchargement de livre blanc
- **Médias** : infographies ROI

## Groupe 2 : DIRECTION_IT_TECHNIQUE (persona pivot, cible primaire)

- **Fonctions** : CTO, DSI, DSI Adjoint, Directeur Informatique, Responsable IT, Responsable Réseau et Systèmes, IT Manager, Directeur Technique, Directeur Datacenter
- **Profil** : décisionnaire opérationnel principal, pivot entre stratégie business et exécution technique
- **Préoccupations** : architecture cible (hybride, on-premise, edge), sécurité et certifications, SLA et redondance, performance et latence, maîtrise des coûts IT, migration et réversibilité, gouvernance et auditabilité
- **Funnel dominant** : MOFU prioritaire, TOFU et BOFU secondaires
- **Intentions dominantes** : Commerciale (comparatifs) + Informationnelle technique
- **Formats préférés** : comparatifs détaillés, guides d'architecture, articles certifications, études de cas DSI, fiches techniques
- **Ton** : technique mais accessible, structuré, orienté décision, riche en preuves
- **Mots-clés types** : "[solution] vs [alternative]", "critères choix [prestataire]", "certification [norme]", "migration [origine] vers [cible]"
- **CTA adaptés** : demande de devis, comparatif
- **Médias** : schémas d'architecture
- **Scoring** : bonus de priorité +1 sur les pages ciblant ce persona (pivot décisionnel)

## Groupe 3 : MANAGEMENT_INFRA_RESEAUX

- **Fonctions** : Manager Infrastructures, Ingénieur Système Réseaux, Responsable Administration Réseaux, Responsable Service Infrastructure
- **Profil** : décisionnaire technique opérationnel ; évalue les solutions sur le terrain et remonte les recommandations au DSI/CTO
- **Préoccupations** : connectivité et interconnexion, densité électrique et refroidissement, sécurité physique et logique, monitoring et supervision, évolutivité, intégration aux outils existants (ITSM, supervision)
- **Funnel dominant** : MOFU et BOFU techniques
- **Intentions dominantes** : Commerciale technique + Transactionnelle (devis, visite)
- **Formats préférés** : fiches techniques chiffrées, guides pratiques, comparatifs techniques, articles connectivité, visites et plans
- **Ton** : très technique, précis, chiffré, opérationnel
- **Mots-clés types** : "PUE datacenter", "densité électrique baie", "interconnexion", "fibre noire", "transit IP"
- **CTA adaptés** : visite, fiche technique
- **Médias** : tableaux chiffrés

## Groupe 4 : PRODUCTION_OPERATIONS

- **Fonctions** : Responsable Production
- **Profil** : garant de la continuité opérationnelle
- **Préoccupations** : disponibilité 24/7, RTO/RPO, astreinte et support, procédures d'escalade, tests PRA/PCA, smart hands
- **Funnel dominant** : MOFU et BOFU
- **Intentions dominantes** : Commerciale et Transactionnelle
- **Formats préférés** : articles SLA et garanties, guides PRA/PCA, fiches services managés, études de cas opérationnelles
- **Ton** : pragmatique, orienté garanties et engagements, chiffré
- **Mots-clés types** : "SLA [service]", "PRA externalisé", "support 24/7", "Tier III", "smart hands"
- **CTA adaptés** : documentation support, consultation des engagements SLA
- **Médias** : procédures et schémas opérationnels

## Règle d'attribution automatique d'un mot-clé à un persona

- Termes stratégiques (souveraineté, ROI, conformité, risque, vision) → DIRECTION_GENERALE
- Termes d'architecture et de décision (vs, comparatif, certification, choisir, migration) → DIRECTION_IT_TECHNIQUE
- Termes techniques pointus (PUE, baie, kW, peering, fibre, U, densité) → MANAGEMENT_INFRA_RESEAUX
- Termes opérationnels (SLA, smart hands, support, astreinte, RTO, RPO) → PRODUCTION_OPERATIONS
- En cas de doute : analyser la SERP top 5 et identifier le profil dominant des contenus qui rankent. La SERP réelle prime toujours sur l'intuition métier ; documenter l'écart le cas échéant.

## Mapping funnel × personas

- **TOFU** : DIRECTION_GENERALE et DIRECTION_IT_TECHNIQUE (veille)
- **MOFU** : DIRECTION_IT_TECHNIQUE et MANAGEMENT_INFRA_RESEAUX
- **BOFU** : DIRECTION_IT_TECHNIQUE (décision), MANAGEMENT_INFRA_RESEAUX (évaluation technique), PRODUCTION_OPERATIONS (validation opérationnelle), DIRECTION_GENERALE (signature finale)
