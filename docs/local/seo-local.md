## Ce qu'elle fait

`seo-local` porte le corpus du classement local : huit sources (trois pages officielles Google, l'étude Resoneo sur le schéma fuité de Maps, Whitespark, deux tests Sterling Sky, la fuite API 2024 lue par Near Media) et six brevets Google, chacun avec son niveau de preuve, et un index qui route une question vers les sources à lire. Elle répond à une question de classement local, ou vérifie un texte, en citant `[NN]` après chaque point.

Ce qui n'est dans aucune source est `(hors corpus)`, même quand c'est vrai. La skill ne complète pas le corpus avec ce que le métier sait ; elle dit où le corpus s'arrête.

## Quand la prendre

Tapez `/seo-local`, ou l'agent la prend seul quand une question porte sur le classement d'une fiche d'établissement, le pack local, un signal de Maps.

| Votre situation | Prendre |
|---|---|
| « Est-ce que les services de la fiche comptent ? » | `seo-local` |
| Vérifier un livrable, une recommandation, un article | `seo-local` : une ligne par affirmation, confirmée / contredite / le corpus ne dit rien |
| Un audit complet jusqu'au livrable | [audit-local](../local/audit-local.md) |
| Ce qu'un brevet précis dit exactement | [brevet-google](../methode/brevet-google.md) |
| Ajouter une source qui manque | [ajouter-source](../methode/ajouter-source.md) |

## Adossé, ou hors corpus

Le mot de la skill est **adossé** : chaque point cite sa source et, quand la preuve est un brevet, un consensus ou une analyse, le dit dans la phrase (« un brevet décrit », « les experts classent »). Quand deux sources se contredisent, la skill expose la contradiction et la position tenue. Le cas connu : le mot-clé dans le nom, interdit par Google et classé troisième par les experts ; la skill recommande le nom réel et signale les concurrents qui font autrement.

## Questions fréquentes

**Le corpus en texte, ça tient quand il aura 50 sources ?**

Question posée aux relecteurs de la première version. Aujourd'hui l'index tient sur un écran et route en une lecture. Le jour où il déborde, c'est l'index qu'on découpe (par famille de la grille), pas la discipline.

**Je sais qu'une pratique marche, elle n'est pas dans le corpus. La skill la refuse ?**

Non : elle l'écrit `(hors corpus)`. C'est un aveu, pas un refus, et c'est aussi un trou à combler : `/ajouter-source` fait entrer la source qui la porte, si elle existe.

## Ça marche si

- Chaque phrase de la réponse porte un `[NN]` ou un `[USxxxx]`, ou `(hors corpus)`.
- Un bloc « Sources mobilisées » ferme la réponse, une ligne par source citée.
- Une vérification revient sous forme de lignes confirmée / contredite / le corpus ne dit rien, sans paragraphe de synthèse qui arrondit.

## Où elle se place

La référence du bucket local, sous [audit-local](../local/audit-local.md) qui l'appelle pour chaque contrôle de la grille. Elle appelle [sourcer](../methode/sourcer.md) pour la règle d'écriture ; [ajouter-source](../methode/ajouter-source.md) est la seule voie pour la faire grandir. Pour la carte entière, [ask-abondance](../methode/ask-abondance.md).
