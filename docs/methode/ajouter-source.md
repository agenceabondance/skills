## Ce qu'elle fait

`ajouter-source` fait entrer une page, une étude ou un brevet dans un corpus Abondance : elle contrôle la fiabilité, rédige la source depuis son gabarit avec son niveau de preuve, et tient l'index à jour (table, routage, veille, trous connus). Une source entre avec son éditeur, sa date et son niveau, ou n'entre pas.

Le niveau est celui que la source justifie. Une page sans méthode exposée entre en Analyse, ou pas du tout : la skill demande avant de choisir pour vous.

## Quand la prendre

Vous la lancez en tapant `/ajouter-source` ; l'agent ne la prendra pas seul, parce qu'ajouter une source modifie le dépôt. Elle prend en argument une URL, un numéro de brevet ou un sujet.

| Votre situation | Prendre |
|---|---|
| Une étude vient de sortir, elle doit entrer dans le corpus | `ajouter-source` |
| Un brevet à lire sans le verser | [brevet-google](../methode/brevet-google.md) |
| Whitespark a publié son édition annuelle | `ajouter-source` : elle remplace la source 05 et met la veille à jour |
| Une question de classement, sans ajout | [seo-local](../local/seo-local.md) |

## Prérequis

Un corpus à viser : celui de `seo-local` aujourd'hui, celui du sujet concerné demain. La skill demande lequel si ce n'est pas dit.

## Une source entre, ou n'entre pas

Le gabarit impose une section « ce que la source ne prouve pas » et une section « à relier » : une source entre avec ses limites et sa place dans le corpus, pas seulement avec ses conclusions. Si elle comble un des trous connus de l'index, le trou disparaît ; si elle peut se périmer (édition annuelle, doc Google), la veille la note.

## Questions fréquentes

**Je peux ajouter un article de blog qui dit quelque chose d'intéressant ?**

Oui, en Analyse, si l'auteur est identifié. Le corpus ne lui fera dire qu'une opinion (« selon X, ... »), jamais un fait. Une étude avec échantillon et méthode entre en Empirique et pèse autrement.

## Ça marche si

- Le nouveau fichier de `references/` a un frontmatter complet et une section « ce que la source ne prouve pas » non vide.
- `00-index.md` a gagné une ligne dans sa table et, si la source répond à une question nouvelle, une ligne de routage.
- Un trou connu a disparu de l'index, ou la veille a gagné une entrée.

## Où elle se place

La seule voie d'entrée dans un corpus. Elle appelle [sourcer](../methode/sourcer.md) pour le niveau et [brevet-google](../methode/brevet-google.md) pour un brevet ; ce qu'elle écrit, [seo-local](../local/seo-local.md) le lit. Pour la carte entière, [ask-abondance](../methode/ask-abondance.md).
