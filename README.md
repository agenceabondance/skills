# seo-local

Une skill pour Claude Code (et tout agent qui lit le format `SKILL.md`) qui audite des fiches Google Business Profile **avec des sources**, et un corpus de connaissances sur le classement local de Google, où chaque affirmation porte son niveau de preuve.

Publiée par [Abondance](https://www.abondance.com), média SEO francophone.

## Pourquoi

Les listes de « facteurs de ranking local » qui circulent mélangent ce que Google dit, ce que des experts pensent, ce qu'un test a mesuré et ce qu'un schéma fuité nomme sans en donner le poids. Cette skill sépare les quatre, et interdit le score sur 100 que personne ne peut justifier.

| Niveau de preuve | Ce que ça veut dire | Ce qu'on peut écrire |
|---|---|---|
| **Officiel** | Google le dit publiquement | « Google indique que... » |
| **Schéma fuité** | Le signal existe dans le code ou la doc interne ; poids inconnu | « Le signal existe ; son poids n'est pas connu » |
| **Brevet** | Google a décrit le mécanisme ; déploiement non prouvé | « Un brevet Google décrit... » |
| **Empirique** | Un test publié a mesuré un effet | « Un test de [source] sur [n] fiches a observé... » |
| **Consensus** | Des experts le pensent | « Les experts classent ce facteur au rang N » |

## Ce qu'il y a dedans

- **`SKILL.md`** : les trois modes (auditer, répondre ou vérifier, enrichir le corpus) et les règles.
- **`references/`** : 8 fiches sources (3 pages officielles Google, l'étude Resoneo « Google Map disséqué » et ses 72 signaux, Whitespark 2026, deux tests Sterling Sky, la fuite API 2024 lue par Near Media) et **6 brevets Google** sur la recherche locale, lus sur leurs revendications. Un index de routage, un registre de veille.
- **`grille/`** : la grille d'audit (9 familles, 43 contrôles, chacun avec sa source, son niveau de preuve, actionnable ou non, et où prendre la donnée) et le gabarit du livrable.
- **`scripts/`** : trois scripts Python sans dépendance. `places.py` photographie un établissement et les fiches présentes sur les mêmes requêtes via Places API (New) ; `audit.py` transforme ce CSV (ou un export de l'interface Google) en tableaux markdown ; `brevet.py` lit un brevet complet sur Google Patents.

## Installation

```bash
git clone https://github.com/agenceabondance/skill-seo-local.git ~/.claude/skills/seo-local
```

Claude Code charge la skill à la session suivante. Pour un autre agent, pointer sur `SKILL.md`.

Les scripts demandent Python 3.10 ou plus (`py` sous Windows, `python3` sur Mac et Linux). `places.py` demande en plus une clé Google Cloud avec Places API (New) activée, dans la variable d'environnement `GOOGLE_PLACES_API_KEY` : voir [`SECURITY.md`](SECURITY.md).

```bash
py scripts/places.py --dry-run pack "plombier" --villes "Nantes,Rennes"   # voir les appels sans les faire
py scripts/places.py pack "plombier" --villes "Nantes,Rennes" --n 10
py scripts/places.py reseau "Ma Marque"
py scripts/audit.py places sortie-places/places-pack-*.csv --client "ma marque"
py scripts/brevet.py --chercher "local search prominence"
py -m pytest -q
```

## Ce que la skill ne fait pas

- Elle ne donne pas de score ni de position garantie : les poids des signaux ne sont pas publics.
- Elle ne lit pas les positions dans Maps : la recherche Places par texte n'est pas le pack local. Les positions viennent d'un outil de suivi.
- Elle ne recommande rien de contraire aux consignes Google, même quand des experts classent la pratique haut (le mot-clé dans le nom de la fiche, par exemple).

## Contribuer

Une source de plus dans le corpus, un brevet lu, un contrôle ajouté à la grille : voir le mode C de `SKILL.md` et les gabarits dans `references/`. Une fiche entre avec sa source, sa date et son niveau de preuve, ou n'entre pas.

## Licence

Code (`scripts/`, `tests/`) sous licence [MIT](LICENSE). Textes (`references/`, `grille/`, `SKILL.md`) sous [CC BY 4.0](LICENSE-CONTENU.md) : réutilisables avec attribution à Abondance. Les citations reproduites dans les fiches restent la propriété de leurs auteurs, cités avec leur lien.

## Remerciements

Le point de départ de ce travail est l'étude [« Google Map disséqué »](https://think.resoneo.com/google-map-dissected/fr/) de Resoneo, diffusée par Olivier de Segonzac : la première lecture publique du schéma interne de Google Maps, avec ses 72 signaux nommés et, surtout, l'honnêteté de dire ce qu'elle ne sait pas (les poids). Cette skill essaie de tenir la même ligne. Merci aussi à Whitespark, Sterling Sky et Near Media, dont les travaux sont cités fiche par fiche.
