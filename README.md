# Skills Abondance

Des skills pour Claude Code, Codex et tout agent qui lit le format `SKILL.md`, publiées par [Abondance](https://www.abondance.com), média SEO francophone.

Elles partagent une règle : **ce qu'on écrit sur Google est adossé à une source, avec son niveau de preuve, ou marqué `(hors corpus)`**. Un agent qui répond « les posts améliorent le classement » sans dire qui l'a mesuré, sur combien de fiches, est un agent qui recopie une liste de facteurs. Ces skills l'obligent à dire d'où vient chaque phrase.

## Installation

Deux voies, deux philosophies. Le **plugin Claude Code** installe l'ensemble comme un paquet géré, mis à jour quand le dépôt publie. **skills.sh** copie des fichiers modifiables dans votre projet, pour les adapter. Choisir une seule des deux : les deux ensemble donnent chaque skill en double.

<details>
<summary><strong>Claude Code</strong></summary>

```
/plugin marketplace add agenceabondance/skill-seo-local
/plugin install abondance-skills@abondance
```

</details>

<details>
<summary><strong>Codex, et les autres agents</strong></summary>

```bash
npx skills@latest add agenceabondance/skill-seo-local
```

L'installeur laisse choisir les skills à prendre. `sourcer` est appelée par toutes les autres : la prendre.

</details>

Les scripts (`places.py`, `audit.py`, `brevet.py`) demandent Python 3.10 ou plus, bibliothèque standard seule. `places.py` demande en plus une clé Google Cloud avec Places API (New), dans la variable d'environnement `GOOGLE_PLACES_API_KEY` : voir [`SECURITY.md`](SECURITY.md).

## Pourquoi ces skills

### #1 : le score sur 100 que personne ne peut justifier

**Le problème.** Les poids des signaux de classement local ne sont pas publics. Un audit qui rend « 72/100 » additionne des poids qu'il n'a pas.

**La réponse.** [`/audit-local`](./skills/local/audit-local/SKILL.md) rend un verdict par famille (✅ 🟠 🔴 ⚪) et des actions classées par risque, effort et niveau de preuve. Une famille sans donnée est ⚪ et le reste : le livrable dit ce qu'il n'a pas pu vérifier.

### #2 : le facteur qu'on croit sourcé

**Le problème.** Les listes de « facteurs de ranking local » mélangent ce que Google dit, ce que des experts pensent, ce qu'un test a mesuré et ce qu'un schéma fuité nomme sans en donner le poids.

**La réponse.** [`/sourcer`](./skills/methode/sourcer/SKILL.md) sépare les six niveaux et impose leur nom dans la phrase :

| Niveau | Ce qu'on écrit |
|---|---|
| **Officiel** | « Google indique que... » |
| **Empirique** | « Un test de [source] sur [n] fiches a observé... » |
| **Consensus** | « Les experts classent ce facteur au rang N » |
| **Schéma fuité** | « Le signal existe ; son poids n'est pas connu » |
| **Brevet** | « Un brevet Google décrit... » |
| **Analyse** | Cité comme une opinion |

[`/seo-local`](./skills/local/seo-local/SKILL.md) porte le corpus qui va avec : 8 fiches sources et 6 brevets Google, chacun avec son niveau.

### #3 : le brevet lu sur son titre

**Le problème.** Un titre de brevet dit ce que Google a demandé ; les revendications délivrées disent ce qu'il a obtenu. Le corpus contient un brevet titré sur le sentiment des avis et délivré sur les interactions.

**La réponse.** [`/brevet-google`](./skills/methode/brevet-google/SKILL.md) lit les revendications, date le statut, et écrit ce que le brevet ne prouve pas.

## Référence

Un seul axe sépare les skills : qui peut les déclencher. Les **user-invoked** ne partent que quand vous les tapez ; elles orchestrent. Les **model-invoked** partent aussi d'elles-mêmes quand la tâche s'y prête ; elles portent la discipline réutilisable.

### Local

- **User-invoked** : [audit-local](./skills/local/audit-local/SKILL.md), l'audit en six phases jusqu'au livrable.
- **Model-invoked** : [seo-local](./skills/local/seo-local/SKILL.md), le corpus, pour répondre et vérifier.

### Méthode

- **User-invoked** : [ask-abondance](./skills/methode/ask-abondance/SKILL.md), le routeur ; [ajouter-source](./skills/methode/ajouter-source/SKILL.md), verser une source dans un corpus.
- **Model-invoked** : [sourcer](./skills/methode/sourcer/SKILL.md), la discipline de citation ; [brevet-google](./skills/methode/brevet-google/SKILL.md), lire un brevet sur ses revendications.

Vous ne savez pas laquelle : `/ask-abondance`.

## Contribuer

Une source de plus dans un corpus, un brevet lu, un contrôle ajouté à la grille : `/ajouter-source` fait entrer une fiche avec sa source, sa date et son niveau de preuve, ou ne la fait pas entrer. `CLAUDE.md` porte les règles du dépôt.

## Licence

Code (`scripts/`, `tests/`) sous licence [MIT](LICENSE). Textes (`SKILL.md`, corpus, grille) sous [CC BY 4.0](LICENSE-CONTENU.md) : réutilisables avec attribution à Abondance. Les citations reproduites dans les fiches restent la propriété de leurs auteurs, cités avec leur lien.

## Remerciements

Le point de départ est l'étude [« Google Map disséqué »](https://think.resoneo.com/google-map-dissected/fr/) de Resoneo, diffusée par Olivier de Segonzac : la première lecture publique du schéma interne de Google Maps, avec ses 72 signaux nommés et, surtout, l'honnêteté de dire ce qu'elle ne sait pas (les poids). Ces skills essaient de tenir la même ligne. Merci aussi à Whitespark, Sterling Sky et Near Media, cités fiche par fiche, et à [Matt Pocock](https://github.com/mattpocock/skills), dont la discipline d'écriture de skills structure ce dépôt.
