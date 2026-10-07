# Outils Haloscan par phase

Mapping des outils du MCP Haloscan avec leur usage dans le workflow. Chaque appel doit être tracé dans la Feuille 10 du livrable (N° appel, outil, paramètre, date, nombre de résultats, phase, usage).

## Exploration de mots-clés

| Outil | Usage | Phase |
|---|---|---|
| `get_keywords_overview` | Aperçu complet. Avec `requested_data: ["similar_serp"]` : **source unique de la mesure de similarité SERP** (voir ci-dessous). Avec `serp` : extraction des titles du top 3 pour l'inspiration Title. Avec `metrics` : volume, KGR, KVI, allintitle, CPC | 1, 3, 4, **5, 5bis**, 9 |
| `get_keywords_match` | Correspondances exactes du mot-clé. Filtres disponibles : `volume_min/max`, `kgr_min/max`, `kvi_min/max`, `allintitle_min/max`, `competition_min/max`, `cpc_min/max`, `word_count_min/max`, `include`, `exclude` | 3 |
| `get_keywords_related` | Termes contextuellement liés, base du clustering. Aussi pour élargir un cluster < 8 pages | 3, 6 |
| `get_keywords_similar` | Variantes sémantiques | 3 |
| `get_keywords_synonyms` | Alternatives linguistiques | 3 |
| `get_keywords_questions` | Questions PAA à intégrer dans les briefs et FAQ | 3, 9 |
| `get_keywords_highlights` | Opportunités tendances | 3 |
| `get_keywords_site_structure` | Organisation hiérarchique optimale, oriente le clustering | 6 |
| `get_keywords_serp_compare` | ⚠️ **NE PAS UTILISER pour l'anti-cannibalisation.** Cet outil compare **une même requête entre deux dates** (`keyword`, `period`, `first_date`, `second_date`). Il ne compare pas deux mots-clés entre eux. Réservé au suivi d'évolution d'une SERP dans le temps | hors workflow |

### ⚠️ Mesure de la similarité SERP : la méthode réelle

**Ne pas utiliser `get_keywords_serp_compare`.** Sa signature est
`{keyword, period, first_date, second_date}` : un seul mot-clé, deux dates. Il mesure l'évolution
d'une SERP dans le temps, pas la proximité entre deux requêtes.

**Méthode correcte** : appeler `get_keywords_overview` avec `requested_data: ["similar_serp"]`
sur le mot-clé principal. La réponse contient un tableau `similar_serp.results` où chaque entrée
porte `keyword`, `volume` et **`similarity`** (score normalisé de 0 à 1).

```json
"similar_serp": { "results": [
  { "keyword": "echelle telescopique 5 metres", "volume": 480, "similarity": 0.8067 },
  { "keyword": "escabeau télescopique 5 mètres", "volume": 260, "similarity": 0.6665 },
  { "keyword": "echelle pliante 5m",             "volume": 15,  "similarity": 0.6332 }
]}
```

Les seuils du workflow s'appliquent directement à ce score : **0,60** et **0,30** en Phase 5,
**0,60** et **0,40** en Phase 5bis.

**Avantage** : un seul appel par mot-clé principal renvoie tous ses voisins de SERP, au lieu d'un
appel par paire. Le coût passe de N² à N.

**Contrôle qualité recommandé** sur les paires proches du seuil (0,55 à 0,65) : comparer le
recouvrement réel des URL du top 10 des deux requêtes via `serp` dans `get_keywords_overview`.
Si un mot-clé n'apparaît pas dans le `similar_serp` du principal, la similarité est à considérer
comme faible, pas comme inconnue.

## Analyse de domaines et concurrence

| Outil | Usage | Phase |
|---|---|---|
| `get_domains_overview` | Trafic, KW positionnés, position moyenne, pays d'un domaine | 1, 2 |
| `get_domains_keywords` | Mots-clés positionnés d'un domaine (top 20 pour l'audit, top 100 par concurrent) | 1, 2 |
| `get_domains_top_pages` | Meilleures pages d'un domaine (top 10 audit, top 30 par concurrent) | 1, 2 |
| `get_domains_competitors` | Découverte des concurrents SEO du site analysé | 2 |
| `get_domains_competitors_keywords_diff` | Gap de mots-clés entre le site et un concurrent : source des quick wins | 2 |
| `get_domains_competitors_best_pages` | Meilleures pages des concurrents (complément) | 2 |
| `get_domains_competitors_keywords_best_pos` | Meilleures positions des concurrents (complément) | 2 |
| `get_page_best_keywords` | Mots-clés d'une URL précise : cartographie des variantes des 5 meilleures pages de chaque concurrent | 2 |

## Bonnes pratiques d'appel

- Validation d'accès en Phase 0 : un appel test `get_keywords_overview` sur un mot-clé générique du secteur. En cas d'échec : arrêt immédiat, aucune donnée inventée.
- Si un appel retourne plus de 500 résultats : conserver le top 300 par volume décroissant + tous les mots-clés BOFU géolocalisés quel que soit leur volume.
- Les données Haloscan arrivent souvent sans accents : restaurer l'orthographe correcte dans tous les champs éditoriaux (voir regles-onpage-fr.md), conserver la forme brute uniquement dans la colonne "Mot-clé" du tableau maître.
- Filtrer le marché cible (par défaut FR) sur toutes les analyses de concurrents multi-pays.

## ⚠️ Haloscan n'expose AUCUN indice de difficulté (KD)

Vérifié jusqu'au niveau de `get_keywords_overview`. Le bloc `seo_metrics` retourne exactement :
`results_count`, `allintitle_count`, `volume`, `keyword_visibility_index` (KVI), `keyword_count`,
`kgr`. Le bloc `ads_metrics` retourne `volume`, `cpc`, `competition`, `impressions`.
**Aucun champ `kd`, `difficulty` ou équivalent.** Aucun filtre `kd_min`/`kd_max` non plus.

**Substitution imposée** : la difficulté se qualifie par le **KGR** (Keyword Golden Ratio,
`allintitle_count / volume`), avec le seuil de référence **KGR <= 0,25** = mot-clé peu
concurrentiel. Compléter par `keyword_visibility_index`, `allintitle_count` et `competition`.

Toute colonne « KD » d'un livrable doit être renommée **KGR** ou porter explicitement `NA`.
**Ne jamais aller chercher un KD chez un autre fournisseur** pour compléter : les indices de
difficulté ne sont jamais comparables entre outils, et mélanger deux référentiels invalide toute
la qualification.

## ⚠️ Deux volumes coexistent et ne sont pas égaux

`get_keywords_overview` renvoie un volume dans `seo_metrics` **et** un volume dans `ads_metrics`,
qui peuvent différer d'un ordre de grandeur (constaté : 112 contre 1 600 sur la même requête).

Choisir **une seule source pour tout le livrable**, la déclarer dans la feuille de traçabilité, et
s'y tenir. Par défaut : le volume de `ads_metrics`, cohérent avec les volumes retournés par
`get_keywords_match` et les outils de domaine.

## Volumétrie des appels

Un cocon complet représente typiquement **300 à 450 appels Haloscan**. Pour les phases de collecte
de masse (Phase 3) et de similarité (Phases 5 et 5bis), privilégier l'**API REST Haloscan** en
direct plutôt qu'un appel MCP par mot-clé : mêmes endpoints, mêmes champs, gain de temps
considérable. Le MCP reste adapté aux phases 0, 1, 2 et 9, moins volumineuses.
Tracer l'intégralité des appels dans la feuille 9 quelle que soit la voie utilisée.
