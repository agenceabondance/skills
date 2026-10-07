---
name: cocon-semantique
description: "Construction complète de cocons sémantiques SEO pilotés par les données du MCP Haloscan, avec benchmark concurrentiel, clustering par personas, classification TOFU/MOFU/BOFU, anti-cannibalisation par similarité SERP, briefs de pages avec Titles et Meta descriptions conformes, et livrable XLSX multi-feuilles avec mise en forme conditionnelle. Utiliser ce skill dès que l'utilisateur demande un cocon sémantique, une étude de mots-clés, un clustering SEO, une architecture de contenu, une stratégie de contenu SEO, un benchmark concurrentiel de mots-clés, une classification TOFU/MOFU/BOFU, ou veut structurer des pages autour d'un mot-clé pilier, même s'il ne prononce pas le mot « cocon ». Requiert le MCP Haloscan connecté."
---

# Cocon Sémantique SEO

Construire un cocon sémantique complet, sourcé à 100% par les données Haloscan, livré en fichier XLSX exploitable par une équipe éditoriale.

## Principes non négociables

1. **Zéro invention de métrique.** Chaque volume, KGR, tendance ou SERP provient d'un appel Haloscan documenté. Si Haloscan est indisponible : arrêt immédiat et signalement, jamais de données inventées.
   ⚠️ **Haloscan n'expose aucun KD.** La difficulté se qualifie par le **KGR** (seuil de référence
   0,25), complété par KVI, allintitle et competition. Ne jamais emprunter un KD à un autre outil
   pour combler le manque : mélanger deux référentiels de difficulté invalide la qualification.
2. **Phase 0 bloquante.** Aucune production avant validation du cadrage (site, secteur, concurrents, personas, mot-clé pilier). Poser 2 à 3 questions ciblées avec des défauts proposés, attendre les réponses, puis exécuter sans redemander.
3. **Un mot-clé principal unique par page.** Zéro cannibalisation, vérifiée par similarité SERP.
4. **Français irréprochable.** Accents partout, y compris sur les majuscules (É, À, Ç). Voir `references/regles-onpage-fr.md`.
5. **Jamais le tiret cadratin (U+2014)** dans aucun livrable.
6. **Livrable unique XLSX** conforme à `references/spec-xlsx.md`.

## Workflow

### Phase 0 : Cadrage (BLOQUANT)

Collecter avant toute exécution :

| Variable | Question à poser | Défaut proposé |
|---|---|---|
| URL du site | Quel site analyser ? | aucun, obligatoire |
| Secteur et enjeux | Secteur d'activité et enjeux marché ? | déduire du site, confirmer |
| Concurrents connus | Concurrents déjà identifiés ? | découverte via `get_domains_competitors` |
| Personas | Personas cibles définis ? | demander le fichier. À défaut, en dériver du catalogue et de la SERP. `references/personas-defaut-b2b-it.md` n'est utilisable **que** si le secteur est effectivement B2B IT : ne jamais l'appliquer à un autre secteur |
| Mot-clé pilier | Mot-clé pilier candidat ? | proposer 3 candidats après audit Phase 1 |
| Volume cible | Nombre de pages visé ? | 50 à 80 pages, minimum 50 |

Valider aussi : accès MCP Haloscan (appel test `get_keywords_overview` sur un mot-clé du secteur), et présence d'un éventuel document méthodologique fourni par l'utilisateur (le lire avant de poursuivre).

### Phase 1 : Audit du site

- `get_domains_overview` : trafic, mots-clés positionnés, position moyenne
- `get_domains_keywords` : top 20 mots-clés actuels. ⚠️ Retourne parfois `API_ERROR` avec un tableau vide : basculer sur `get_domains_positions`
- `get_domains_top_pages` : top 10 pages actuelles
- Valider le mot-clé pilier : volume > 500/mois (adapter le seuil aux niches B2B, minimum 300), tendance stable ou haussière, non brandé, pérenne. Si volume insuffisant : proposer 3 alternatives chiffrées et demander arbitrage.

**Test de demande sur les arguments commerciaux de la marque (obligatoire).**
Avant de prévoir la moindre page dédiée à un argument différenciant (garantie, SAV, certification,
fabrication locale, service), **vérifier qu'il constitue un champ de recherche** via
`get_keywords_match` sur l'argument.

Un argument commercial fort n'est pas nécessairement un champ de mots-clés. Cas réel rencontré :
la garantie 5 ans et le SAV France structuraient tout le discours d'une marque, mais
`garantie [produit]` ne renvoyait **aucune donnée** et le champ entretien complet pesait
130 recherches mensuelles.

- **Demande avérée** → l'argument mérite une page.
- **Demande nulle ou marginale** → l'argument devient un **bloc transversal des pages BOFU**,
  jamais une page autonome. Il ne fait pas venir, il fait choisir : il doit apparaître là où
  l'utilisateur arbitre, pas sur une page qu'il faudrait aller chercher.

Documenter le résultat de ce test dans la feuille de cadrage.

### Phase 2 : Benchmark concurrentiel

1. **Concurrents pré-identifiés** (fournis en Phase 0) : pour chacun, `get_domains_overview`, `get_domains_keywords` (top 100 filtré marché cible), `get_domains_top_pages` (top 30), `get_page_best_keywords` sur les 5 meilleures pages. Identifier persona dominant et angle éditorial.
2. **Découverte** : `get_domains_competitors` sur le site analysé, filtrer (même secteur, marché cible, exclure blogs génériques/comparateurs/affiliation), retenir 3 concurrents additionnels. Total visé : 7 concurrents.
3. **Gap analysis** : `get_domains_competitors_keywords_diff` pour chaque concurrent. Extraire minimum 50 quick wins classés TOFU/MOFU/BOFU avec persona cible.
4. **Synthèse** : matrice benchmark, carte de positionnement éditorial 2D (Technique/Stratégique × axes différenciants du secteur), 3 axes de différenciation recommandés.

### Phase 3 : Cartographie des mots-clés

Séquence obligatoire depuis le mot-clé pilier :
`get_keywords_match` → `get_keywords_related` → `get_keywords_similar` → `get_keywords_synonyms` → `get_keywords_questions` → `get_keywords_highlights`

Puis élargir : 5 mots-clés graines par persona (via leurs exemples de mots-clés). Intégrer les 50 quick wins. Filtrer doublons, hors-secteur, volume < 30/mois (sauf longue traîne BOFU stratégique). **Objectif : minimum 300 mots-clés sourcés.**

### Phase 4 : Classification multidimensionnelle

Classer chaque mot-clé sur 6 dimensions :
1. **Intention** : Informationnelle / Commerciale / Transactionnelle / Navigationnelle
2. **Funnel** : TOFU / MOFU / BOFU (règle d'arbitrage : SERP top 5 avec 3+ pages transactionnelles = BOFU, 3+ guides = TOFU, sinon MOFU)
3. **Persona principal** (attribution par termes du mot-clé, arbitrage par SERP en cas de doute)
4. **Persona secondaire** (optionnel)
5. **Type d'article** : What is / How to / Comparative / Top / Review / Interview / Generalist / Landing
6. **Couverture concurrentielle** : nombre de concurrents en top 10 (0 à 7)

### Phase 5 : Anti-cannibalisation

⚠️ **Ne pas utiliser `get_keywords_serp_compare`** : cet outil compare une même requête entre deux
dates, pas deux mots-clés entre eux. Voir `references/outils-haloscan.md`.

**Méthode** : `get_keywords_overview` avec `requested_data: ["similar_serp"]` sur chaque mot-clé
principal candidat. La réponse liste ses voisins de SERP avec un score `similarity` de 0 à 1.
Un seul appel par principal suffit, au lieu d'un appel par paire.

- **similarity ≥ 0,60** : FUSION (un seul mot-clé principal, l'autre devient secondaire)
- **0,30 à 0,59** : ZONE GRISE (différenciation éditoriale forte obligatoire)
- **< 0,30**, ou mot-clé absent du `similar_serp` du principal : SÉPARATION (deux pages distinctes)
- Exception : SERP similaire mais personas radicalement différents → deux pages aux angles opposés, justification documentée.

Contrôle sur les paires limites (0,55 à 0,65) : vérifier le recouvrement réel des URL du top 10
via `requested_data: ["serp"]` avant de trancher.

### Phase 5bis : Attribution des mots-clés secondaires

Pour chaque futur mot-clé principal de page :
- Candidats secondaires = même cluster, même intention, même persona
- Lire le score `similarity` du candidat dans le `similar_serp` du principal (déjà collecté en Phase 5) :
  - **≥ 0,60** : SECONDAIRE FORT (à placer en H2)
  - **0,40 à 0,59** : SECONDAIRE FAIBLE (à placer en H3)
  - **< 0,40** ou absent : REJET (réaffecter à une autre page ou promouvoir en principal)
- Chaque page : 1 principal + 2 à 5 secondaires validés. KW orphelin sans rattachement possible : promouvoir en principal si volume ≥ 50/mois ou BOFU stratégique, sinon exclure avec justification.

### Phase 6 : Clustering

`get_keywords_site_structure` pour orienter. Règles : 5 à 8 clusters, 8 à 12 pages chacun, équilibre TOFU/MOFU/BOFU par cluster, minimum 2 personas mobilisés par cluster, persona dominant identifié.

**Personas à faible volume de marché : ne pas forcer.** Si un persona ne mobilise que quelques
dizaines de mots-clés une fois la cartographie terminée, c'est une donnée de marché, pas un défaut
de collecte. Lui imposer 8 pages produirait du contenu sans demande.

Traiter ces personas en **océan bleu** : 2 à 4 pages sur des requêtes sans concurrence, à fort
potentiel de conversion, en documentant l'arbitrage. La règle des 8 pages par persona vaut pour
les personas porteurs de volume, pas pour tous.

### Phase 7 : Architecture

3 niveaux maximum (Pilier → Clusters → Supports). Minimum 50 pages. Maillage Hub and Spoke + liens horizontaux entre pages sœurs + liens transversaux funnel-driven reliant TOFU → MOFU → BOFU du même persona. Dessiner un parcours complet par persona.

⚠️ **Deux règles impératives, sous peine d'échec du cocon.**

**1. Maillage sœur-sœur bidirectionnel complet.** Toutes les pages d'un même niveau au sein d'un
cluster doivent être reliées entre elles. C'est le point de défaillance le plus fréquent : un
cocon dont le maillage mère-fille est parfait mais dont les pages sœurs ne sont pas reliées **ne
fonctionne pas**. Si un cocon déployé ne produit rien, vérifier ce point en premier.

**2. Sur un site e-commerce, toute page à intention transactionnelle DOIT lister des produits.**
Une page pilier ou de cluster commerciale sans liste de produits perd ses positions, parce qu'elle
ne répond pas à l'intention de recherche, quels que soient son maillage et son autorité.
**L'intention prime toujours sur le signal de puissance.** Inscrire cette contrainte dans le brief
de chaque page BOFU.

### Phase 8 : Priorisation

Score par page = (Potentiel business × 2) + Stratégicité persona (+1 si persona pivot) + Opportunité concurrentielle (+2 si couverture ≤ 2/7) - Difficulté SEO - Effort production.
3 vagues sur 12 mois : V1 (M1-M3) pilier + clusters BOFU prioritaires + quick wins, V2 (M4-M6) clusters MOFU, V3 (M7-M12) TOFU + longue traîne.

### Phase 9 : Briefs par page

22 champs par page, dont Title et Meta description soumis aux règles strictes de `references/regles-onpage-fr.md` :
- **Title** : ≤ 60 caractères espaces inclus, mot-clé principal en début, inspiré des titles des 3 URLs top 3 de la SERP (extraits via `get_keywords_overview` avec serp, documentés dans le brief), élément différenciant en fin.
- **Meta description** : ≤ 155 caractères espaces inclus, mot-clé principal présent, pain point du persona adressé, CTA explicite adapté à l'intention.
- Plan H2/H3 distribuant les secondaires forts (H2) et faibles (H3).
- Référence concurrentielle : URL de la page concurrente à battre + angle de différenciation.

### Phase 10 : Génération du livrable XLSX

Suivre intégralement `references/spec-xlsx.md` : 10 feuilles ordonnées (Légende, Cadrage, Benchmark, Quick wins, Tableau maître, Anti-cannibalisation, Architecture, Briefs, Priorisation, Sources Haloscan), mise en forme conditionnelle par codes couleur, volets figés, filtres, formules de validation automatique des longueurs Title/Meta, onglets colorés.

Générer avec openpyxl (`python3 -c "import openpyxl"` pour vérifier la dépendance, sinon `pip install openpyxl`). Écrire le script de génération dans un répertoire de travail temporaire, l'exécuter, puis vérifier le fichier produit (nombre de feuilles, formules, mises en forme) avant de le livrer.

Si un skill `xlsx` est disponible dans l'environnement (sur claude.ai et Claude Desktop : `/mnt/skills/public/xlsx/SKILL.md`), le consulter avant d'écrire le code. En son absence (Claude Code en local), générer directement avec openpyxl.

## Auto-vérification avant livraison

Vérifier systématiquement, et reprendre la phase concernée si un point échoue :
- Métriques 100% Haloscan, zéro invention, **aucun KD emprunté à un autre outil**
- Similarité SERP issue de `similar_serp`, **jamais de `get_keywords_serp_compare`**
- Test de demande effectué sur les arguments commerciaux de la marque, résultat documenté
- Sur un site e-commerce : **100% des pages BOFU portent la contrainte « doit lister des produits »**
- Maillage sœur-sœur bidirectionnel complet sur chaque niveau de chaque cluster
- Arbitrage documenté pour tout persona traité en océan bleu
- Concurrents pré-identifiés tous analysés + 3 découverts
- ≥ 50 quick wins, ≥ 300 mots-clés, ≥ 50 pages, 5 à 8 clusters, ≥ 8 pages par persona
- 100% des paires suspectes arbitrées (cannibalisation) et 100% des pages avec 2 à 5 secondaires validés ≥ 40%
- 100% des Titles ≤ 60 c. démarrant par le mot-clé principal, inspirés du top 3 documenté
- 100% des Meta ≤ 155 c. avec mot-clé + CTA
- Orthographe française complète, accents sur majuscules, slugs URL sans accent (seule exception)
- Aucun tiret cadratin (U+2014)
- 10 feuilles XLSX conformes avec mise en forme conditionnelle et formules de validation

## Gestion des erreurs

| Situation | Action |
|---|---|
| Haloscan indisponible | Arrêt immédiat, signalement, proposer reprise ultérieure |
| **KD demandé quelque part** | Haloscan n'en expose aucun : utiliser le KGR (seuil 0,25) et le signaler dans la légende, le cadrage et chaque en-tête de colonne concerné. Jamais d'emprunt à un autre outil |
| **Besoin de comparer deux mots-clés** | Ne pas utiliser `get_keywords_serp_compare` (il compare des dates). Utiliser `similar_serp` de `get_keywords_overview` |
| **`get_domains_keywords` renvoie `API_ERROR`** | Basculer sur `get_domains_positions` |
| **Deux volumes différents pour un mot-clé** | `seo_metrics` et `ads_metrics` divergent. Choisir une source unique pour tout le livrable, la déclarer en feuille 9, s'y tenir |
| **Un concurrent pré-identifié n'apparaît pas dans les concurrents détectés** | Normal : les concurrents perçus sont des concurrents de marché, les détectés des concurrents de SERP. Analyser les deux et documenter l'écart, c'est un résultat en soi |
| **Le gap analysis déclare « missing » un mot-clé où le site est positionné** | Faux positif connu (jusqu'à 6 % constatés). Croiser systématiquement avec l'export des positions réelles avant de retenir un quick win |
| **Un concurrent généraliste pollue le gap** | Relancer le diff sans lui plutôt que de filtrer a posteriori |
| **Un persona mobilise moins de 30 mots-clés** | Océan bleu : 2 à 4 pages, ne pas forcer le quota. Documenter |
| **Argument commercial sans demande de recherche** | Bloc transversal des pages BOFU, jamais une page dédiée |
| Concurrent sans données Haloscan | Audit manuel du site, signaler la limite dans le benchmark |
| Concurrent multi-pays ou anglophone | Filtrer le marché cible ; inspiration éditoriale seulement si hors langue |
| Mot-clé pilier < seuil de volume | Proposer 3 alternatives chiffrées, demander arbitrage |
| Cluster < 8 pages | Élargir via `get_keywords_related` sur la thématique pivot |
| Persona < 8 pages | Relancer la cartographie avec graines spécifiques à ce persona |
| Title incompressible sous 60 c. | Retirer la marque, puis raccourcir le différenciant, puis réduire à un mot-clé fort |
| Meta incompressible sous 155 c. | Prioriser mot-clé > bénéfice > CTA, supprimer adverbes |
| Top 3 SERP mono-domaine | Élargir l'inspiration au top 5 |
| Données Haloscan sans accents | Restaurer les accents dans les champs éditoriaux ; conserver la forme brute uniquement dans la colonne mot-clé du tableau maître |
| Cellule XLSX trop longue | Tronquer à 32 767 caractères, format .xlsx uniquement |

## Références

- `references/regles-onpage-fr.md` : règles Title, Meta description et orthographe française. À lire avant la Phase 9.
- `references/spec-xlsx.md` : spécification complète des 10 feuilles, codes couleur hexadécimaux, mise en forme conditionnelle. À lire avant la Phase 10.
- `references/personas-defaut-b2b-it.md` : 4 groupes de personas B2B IT réutilisables (Direction Générale, Direction IT, Management Infra, Production). À proposer en Phase 0 si le secteur s'y prête.
- `references/outils-haloscan.md` : mapping des 17 outils Haloscan par phase avec leurs usages.
