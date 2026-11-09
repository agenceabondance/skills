# Skills Abondance

[![skills.sh](https://skills.sh/b/agenceabondance/skills)](https://skills.sh/agenceabondance/skills)

Des skills pour Claude Code, Codex et tout agent qui lit le format `SKILL.md`, publiées par [Abondance](https://www.abondance.com), média SEO francophone. Elles partagent une règle : **ce qu'on écrit sur Google est adossé à une source, avec son niveau de preuve, ou marqué `(hors corpus)`.**

Un agent qui répond « les posts améliorent le classement » sans dire qui l'a mesuré, sur combien de fiches, recopie une liste de facteurs. Ces skills l'obligent à dire d'où vient chaque phrase, et à avouer quand il ne sait pas.

## Installation (30 secondes)

Deux voies, deux philosophies. Le **plugin Claude Code** installe l'ensemble comme un paquet géré, en lecture seule, mis à jour quand le dépôt publie une version : on s'abonne. **skills.sh** copie des fichiers modifiables dans votre projet : on adapte. Choisir une seule des deux ; les deux ensemble donnent chaque skill en double.

### 1. Prendre les skills

<details>
<summary><strong>Claude Code</strong></summary>

```
/plugin marketplace add agenceabondance/skills
/plugin install abondance-skills@abondance
```

Un paquet géré, en lecture seule, mis à jour quand le dépôt publie une version.

</details>

<details>
<summary><strong>Codex, et les autres agents</strong></summary>

```bash
npx skills@latest add agenceabondance/skills
```

L'installeur laisse choisir les skills. `sourcer` est appelée par toutes les autres : la prendre. `npx skills@latest update` reprend les dernières modifications.

</details>

### 2. Lancer `/setup-abondance-skills`

Une fois par dépôt de travail. Il demande où vont les livrables, quels outils de mesure vous avez (suivi de positions, mesure du site, accès aux fiches), et note si une clé Places est présente. `/audit-local` le lira au lieu de vous le redemander.

### 3. C'est prêt.

Les scripts (`places.py`, `audit.py`, `brevet.py`) demandent Python 3.10 ou plus, bibliothèque standard seule. `places.py` demande en plus une clé Google Cloud avec Places API (New), dans `GOOGLE_PLACES_API_KEY` : voir [`SECURITY.md`](SECURITY.md).

## Pourquoi ces skills

### #1 : le score sur 100 que personne ne peut justifier

> « Nous ne connaissons pas : les coefficients, les fonctions de normalisation, les seuils, les transformations, les calibrations par marché, les interactions entre signaux, les versions de modèle. »
>
> Resoneo, [Google Map disséqué](https://think.resoneo.com/google-map-dissected/fr/)

**Le problème.** Les poids des signaux de classement local ne sont pas publics. Un audit qui rend « 72/100 » additionne des poids qu'il n'a pas, et le client ne peut plus distinguer ce qui est vérifié de ce qui est deviné.

**La réponse.** [`/audit-local`](./skills/local/audit-local/SKILL.md) rend un **verdict par famille** (✅ 🟠 🔴 ⚪) et des actions classées par risque, effort et niveau de preuve. Une famille sans donnée est ⚪ et le reste : le livrable dit ce qu'il n'a pas pu vérifier, en section 2 avant de commencer et en section 7 en terminant.

### #2 : le facteur qu'on croit sourcé

> « If your business is closed, you're invisible. »
>
> Whitespark, Local Search Ranking Factors 2026 (sur le facteur horaires, rang 5)

**Le problème.** C'est vrai, et c'est du consensus d'experts, pas une mesure. Les listes de « facteurs de ranking local » mélangent ce que Google dit, ce que des experts pensent, ce qu'un test a mesuré et ce qu'un schéma fuité nomme sans en donner le poids. Quatre choses différentes, présentées pareil.

**La réponse.** [`/sourcer`](./skills/methode/sourcer/SKILL.md) sépare six niveaux et impose leur nom dans la phrase :

| Niveau | Ce qu'on écrit |
|---|---|
| **Officiel** | « Google indique que... » |
| **Empirique** | « Un test de [source] sur [n] fiches a observé... » |
| **Consensus** | « Les experts classent ce facteur au rang N » |
| **Schéma fuité** | « Le signal existe ; son poids n'est pas connu » |
| **Brevet** | « Un brevet Google décrit... » |
| **Analyse** | Cité comme une opinion |

[`/seo-local`](./skills/local/seo-local/SKILL.md) porte le corpus qui va avec : huit sources et six brevets Google, chacun avec son niveau, et un index qui route une question vers ce qu'il faut lire.

> [!TIP]
> Le mot de la discipline est **adossé**. Une affirmation adossée cite sa source ; une affirmation qui ne l'est pas porte `(hors corpus)`. Ce n'est pas un défaut : c'est l'aveu qui dit au lecteur où s'arrête ce qu'on sait. Le vocabulaire complet est dans [`CONTEXT.md`](CONTEXT.md).

### #3 : le brevet lu sur son titre

**Le problème.** Un titre de brevet dit ce que Google a demandé ; les revendications délivrées disent ce qu'il a obtenu. Le corpus contient un brevet titré sur le sentiment des avis et délivré sur les interactions : une source rédigée sur le titre aurait affirmé le contraire de ce que Google a obtenu.

**La réponse.** [`/brevet-google`](./skills/methode/brevet-google/SKILL.md) lit les revendications, date le statut, et écrit ce que le brevet ne prouve pas.

### #4 : la recommandation qui fait suspendre la fiche

> « Google se réserve le droit de suspendre l'accès aux fiches d'établissement [...] pour les personnes ou établissements qui ne respecteraient pas ces consignes. »
>
> Google, Consignes de représentation d'un établissement

**Le problème.** Le mot-clé dans le nom de la fiche est interdit par Google et classé troisième facteur par les experts. Une skill qui optimise sans lire les consignes recommande la suspension.

**La réponse.** La famille A (conformité) se déroule en premier et en entier ; un 🔴 en A prime sur toute optimisation. La position du corpus est tenue une fois, dans `seo-local` : on recommande le nom réel, on signale les concurrents qui font autrement.

### En résumé

Ces skills ne rendent pas l'agent plus malin sur le SEO local. Elles l'obligent à montrer ses sources, à nommer le niveau de chaque preuve, et à écrire ce qu'il ne sait pas. C'est ce qui manque aux listes de facteurs qui circulent, et c'est ce qu'un client est en droit d'attendre d'un audit.

## Référence

Un seul axe sépare les skills : qui peut les déclencher. Les **user-invoked** ne partent que quand vous les tapez ; elles orchestrent. Les **model-invoked** partent aussi d'elles-mêmes quand la tâche s'y prête ; elles portent la discipline réutilisable. Une user-invoked peut appeler des model-invoked, jamais l'inverse. Vous ne savez pas laquelle : `/ask-abondance`.

### Local

Le classement d'une fiche d'établissement dans Google : pack local, Maps.

**User-invoked**

- **[audit-local](./skills/local/audit-local/SKILL.md)** : auditer une fiche ou un réseau en six phases, chacune avec son critère de fin, jusqu'au livrable.

**Model-invoked**

- **[seo-local](./skills/local/seo-local/SKILL.md)** : le corpus (huit sources, six brevets, index de routage) ; répondre à une question de classement local avec des sources, vérifier qu'une recommandation est étayée.

### Méthode

Ce qui court sous tous les corpus, quel que soit le sujet.

**User-invoked**

- **[ask-abondance](./skills/methode/ask-abondance/SKILL.md)** : quelle skill pour ma situation ; un routeur sur les skills du dépôt.
- **[setup-abondance-skills](./skills/methode/setup-abondance-skills/SKILL.md)** : configurer un dépôt de travail (livrables, outils de mesure, clé Places). Une fois par dépôt.
- **[ajouter-source](./skills/methode/ajouter-source/SKILL.md)** : verser une page, une étude ou un brevet dans un corpus, avec son niveau de preuve.

**Model-invoked**

- **[sourcer](./skills/methode/sourcer/SKILL.md)** : la discipline de citation ; unique propriétaire des niveaux de preuve.
- **[brevet-google](./skills/methode/brevet-google/SKILL.md)** : lire un brevet Google sur ses revendications, chercher les brevets d'un sujet, rédiger la source.

Chaque skill a une page pour humains dans [`docs/`](docs/) : ce qu'elle fait, quand la prendre, où elle se place.

## Contribuer

Une source de plus dans un corpus, un brevet lu, un contrôle ajouté à la grille : `/ajouter-source` fait entrer une source avec son éditeur, sa date et son niveau de preuve, ou ne la fait pas entrer. Les règles du dépôt sont dans [`CLAUDE.md`](CLAUDE.md), les décisions dans [`.agents/adr/`](.agents/adr/), ce qu'on ne fera pas dans [`.out-of-scope/`](.out-of-scope/). `python scripts/check-repo.py` vérifie les conventions mécaniques ; `python -m pytest -q` les scripts.

## Licence

Code (`scripts/`, `tests/`) sous licence [MIT](LICENSE). Textes (`SKILL.md`, corpus, grille, docs) sous [CC BY 4.0](LICENSE-CONTENU.md) : réutilisables avec attribution à Abondance. Les citations reproduites dans les sources restent la propriété de leurs auteurs, cités avec leur lien.

## Remerciements

Le point de départ est l'étude [« Google Map disséqué »](https://think.resoneo.com/google-map-dissected/fr/) de Resoneo, diffusée par Olivier de Segonzac : la première lecture publique du schéma interne de Google Maps, avec ses 72 signaux nommés et, surtout, l'honnêteté de dire ce qu'elle ne sait pas (les poids). Ces skills essaient de tenir la même ligne. Merci aussi à Whitespark, Sterling Sky et Near Media, cités source par source, et à [Matt Pocock](https://github.com/mattpocock/skills), dont la discipline d'écriture de skills structure ce dépôt.
