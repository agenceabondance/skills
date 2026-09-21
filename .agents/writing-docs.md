# Pages docs

Chaque skill promue (buckets `local/` et `methode/`) a une page pour humains dans `docs/<bucket>/<skill>.md`. La page n'est pas la skill et n'est pas une copie du `SKILL.md`.

La plupart des skills sont user-invoked : l'agent ne les lancera jamais pour vous, donc *vous* êtes l'index qui doit se souvenir qu'elles existent et quand les prendre. C'est de la charge cognitive. Le travail d'une page docs est de l'alléger : orienter un lecteur autour d'une skill pour qu'il sache quand la prendre et où elle se place. Ensemble, les pages sont un routeur distribué ; chacune en est un nœud.

Agir quand une skill promue entre, est renommée ou change de comportement : créer ou resynchroniser sa page. Une skill qui quitte un bucket promu perd sa page.

Pas de H1 : le titre vient du nom de la skill à la publication.

## Structure

Remplir le gabarit ci-dessous, dans l'ordre. Le **cadre fixe** (`## Ce qu'elle fait`, `## Quand la prendre`, `## Où elle se place`) est sur chaque page. `## Prérequis` et les sections libres du milieu ne portent que ce dont cette skill a besoin ; supprimer le reste.

<page-template>

## Ce qu'elle fait

Un ou deux paragraphes. D'abord le travail de la skill en une phrase, puis la **contrainte qui la définit** : le fait unique qui la fait se comporter autrement que le défaut évident (`audit-local` : une famille sans donnée est ⚪ et le reste). En phrase déclarative, jamais en aparté étiqueté (« La contrainte : »). C'est la ligne la plus précieuse de la page.

## Quand la prendre

Deux temps, toujours présents :

- **Mode d'invocation.** Vous la tapez, ou l'agent la lance. User-invoked : « Vous la lancez en tapant `/<nom>` ; l'agent ne la prendra pas seul. » Model-invoked : « Tapez `/<nom>`, ou l'agent la prend seul quand la tâche s'y prête. »
- **Frontière.** L'entrée d'index : « la prendre quand... ». Là où la skill se confond avec une voisine, l'autre moitié : « pour X, prendre plutôt [voisine]. » Un choix à plusieurs branches va dans un tableau ou une liste, jamais dans un paragraphe.

## Prérequis

Seulement quand la skill a besoin de quelque chose pour fonctionner : un espace où elle écrit, une configuration préalable (`/setup-abondance-skills`), un outil. Sinon, supprimer la section.

## <milieu libre>

Une à trois sections courtes, dans le vocabulaire propre de la skill : la boucle qu'elle suit, l'artefact qu'elle produit, l'anti-pattern qu'elle tue. La seule obligation : **faire apparaître le mot-clé de la skill** (*adossé*, *verdict par famille*, *revendications*), pour que le lecteur apprenne à la fois ce qu'elle est et le mot avec lequel il y pensera.

## Questions fréquentes

Les questions que les lecteurs posent vraiment, en gras, la réponse dessous. Une question observée vaut toujours plus qu'une inventée : chercher d'abord dans les issues du dépôt (`gh issue list --search "<skill>" --state all`), dans `CHANGELOG.md` (tout renommage produit un « où est passé... »). Le compte reste honnête : une skill discutée en mérite six, une skill neuve une ou deux, ou aucune ; supprimer le titre plutôt que remplir.

## Ça marche si

Quelques puces disant ce que le lecteur voit quand la skill fait son travail, vérifiables sans ouvrir `SKILL.md` : un signal dans son propre travail (« le livrable a une section 7 qui liste des familles ⚪ »). Supprimer le titre si les signes restent vagues.

## Où elle se place

Toujours présente. Le rôle (une étape d'une chaîne, un setup à lancer une fois, une référence sous les autres, un outil à prendre n'importe quand), les une ou deux voisines qui comptent avec leur « parce que », et le renvoi vers `ask-abondance`, le routeur, pour que la page reste un nœud et n'ait jamais à redessiner le graphe.

</page-template>

## Conventions

- Expliquer le **pourquoi**, pas le processus : la page oriente, elle ne recopie pas les étapes.
- Ne jamais nommer l'auteur. Une trouvaille garde sa substance, pas son attribution. Citer un *utilisateur* reste bien (« un relecteur a demandé... »), anonymement.
- Employer les mots de `CONTEXT.md` (fiche, source, adossé, verdict, hors corpus) pour que la page et la skill parlent une langue.
- Pas de commande d'installation sur une page : le bloc canonique vit dans `.agents/install-block.md` et le README.
- La page reste légère. Elle documente des skills à faible charge ; le mobilier (titres vides, liens répétés) est ce qu'elle combat.
