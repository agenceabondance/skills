---
name: audit-local
description: "Auditer une fiche d'établissement Google ou un réseau, en six phases, jusqu'au livrable."
argument-hint: "Établissements, requêtes cibles, villes"
disable-model-invocation: true
---

# Audit local

Six phases, chacune avec son critère de fin. La grille (`grille/grille-audit.md`) et le gabarit (`grille/gabarit-livrable.md`) sont la référence ; ce fichier dit dans quel ordre, et quand une phase est finie.

Call the Skill tool with "seo-local" : le corpus que la grille cite, et la règle d'écriture.

## Phase 1 : Cadrer

Établissements, requêtes cibles, villes de mesure. Chaque requête est qualifiée : **intention locale forte** (« + ville », « près de moi ») ou **faible** (générique). Une requête faible relève du site, pas de la fiche ([US8171048B2], [US11893034B2]) : elle sort du périmètre et entre dans la section 7 du livrable.

Terminé quand la section 1 du gabarit est remplie et que chaque requête porte son intention.

## Phase 2 : Inventorier les données

**C'est la phase qui protège le livrable.** Une famille sans donnée est ⚪ et le reste. Un ⚪ annoncé ici est une limite ; un ⚪ découvert en phase 4 est un trou.

Si `docs/agents/abondance.md` existe (écrit par le setup), il pré-remplit les outils disponibles et le dossier des livrables : ne demander que ce qui change pour ce client. Pour chaque ligne de la section 2 du gabarit, ✅ ou ⚪ : fiche publique, export Performances, trafic UTM, positions par ville, pack des concurrents. Demander au client ce qui manque avant de collecter.

Terminé quand la section 2 est remplie et que chaque famille de la grille a sa source de donnée (codes M/P/E/G/K) ou son ⚪ motivé.

## Phase 3 : Collecter

Du moins cher au plus cher :

1. **À la main** (M) : Maps et l'interface de gestion.
2. **Places** (P) : `scripts/places.py pack` par requête et ville, puis `reseau` pour une marque. Photographie publique de la fiche et du pack, sans accès client. `--dry-run` avant tout lot inhabituel ; la clé et le plafond d'appels sont dans le `SECURITY.md` du dépôt.
3. **Trafic UTM** (G) : quand les fiches portent un `utm_campaign`, l'outil de mesure du site **corrige l'inventaire Places**. Une recherche par texte manque des fiches, et une fiche qui disparaît se lit d'abord dans un trafic mensuel qui tombe à zéro. C'est aussi la seule source qui dit ce qu'une fiche rapporte.
4. **Export de l'interface** (E) : quand le propriétaire donne accès.
5. `scripts/audit.py` transforme les CSV (Places ou export) en tableaux pour le livrable. Il aligne des chiffres et signale des écarts ; le verdict reste à la phase 4.

Les **positions** viennent d'un suivi par point de mesure (K, famille E). Une recherche Places par texte donne l'inventaire d'un pack, jamais un rang.

Terminé quand chaque contrôle non-⚪ de la grille a sa donnée sous la main : fichier, capture ou chiffre noté.

## Phase 4 : Dérouler la grille

Famille A en premier, en entier. **Un 🔴 en A prime sur tout** : le livrable dit « corriger, puis optimiser », et les familles B à I passent derrière.

Pour chaque contrôle : le constat observé (chiffre, capture, exemple), la source `[NN]` / `[USxxxx]` et son niveau de preuve, recopiés depuis la grille. Un contrôle qu'on n'a pas pu observer est ⚪ avec sa raison.

Réseau multi-établissements : la famille I et `places.py reseau` sont le cœur. La cohérence entre fiches (modèle de nom, catégorie, une page par établissement) et les fiches en retard pèsent plus que l'optimisation d'une fiche isolée ([04], [08]).

Terminé quand les 43 contrôles ont un verdict et que chaque 🟠 / 🔴 porte constat, source et preuve.

## Phase 5 : Écrire le livrable

Depuis `grille/gabarit-livrable.md`, en markdown, dans le dossier des livrables (celui du setup, sinon celui que le client indique). Les sections 2 (données non disponibles) et 7 (ce que l'audit ne dit pas) ont le même statut que les autres : sans elles, le livrable n'est pas fini.

Les recommandations (section 6) sont classées : ce qui protège (A), puis ce qui est prouvé et peu coûteux (Officiel, Empirique), puis le Consensus, en dernier ce qui ne tient qu'à un Schéma ou un Brevet. Une action adossée à un signal que le schéma marque déprécié (le PageRank de la page d'autorité, [04]) sort de la liste.

Terminé quand :

- [ ] Les 8 sections du gabarit sont remplies.
- [ ] Chaque 🟠 / 🔴 de la section 4 a constat, source et preuve.
- [ ] Chaque ligne de la section 6 a une source ou `(hors corpus)`, et respecte [02] et [03].
- [ ] La section 7 liste chaque famille ⚪ avec sa raison, et chaque requête à intention faible.
- [ ] Le livrable ne contient ni score ni rang promis.

## Phase 6 : Version client

Seulement si elle est demandée. Une page pour le lecteur final : sans raisonnement interne, sans jargon de la grille, avec un bloc « méthode et limites » qui reprend les sections 2 et 7. Le niveau de preuve reste visible sur chaque recommandation : c'est ce qui distingue ce livrable d'une liste de facteurs.
