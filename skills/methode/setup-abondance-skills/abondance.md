# Configuration des skills Abondance

Écrit par `/setup-abondance-skills` le <AAAA-MM-JJ>. Se modifie à la main.

## Livrables

Les audits s'écrivent dans `<dossier>/`, un sous-dossier par client, en markdown.

## Outils de mesure

| Donnée | Outil | Disponible |
|---|---|---|
| Positions Maps par point de mesure | <Monitorank / grille géographique / aucun> | ✅ / ⚪ |
| Trafic issu de la fiche | <GA4 / Matomo / aucun> ; UTM sur les fiches : <oui / non> | ✅ / ⚪ |
| Métriques Performances (export de l'interface) | Accès <propriétaire / gestionnaire / public seulement> | ✅ / ⚪ |

Une ligne ⚪ fait ⚪ la famille correspondante de la grille (E, G) tant qu'un accès n'est pas donné pour un client précis.

## Clé Places

`GOOGLE_PLACES_API_KEY` : <présente / absente> dans l'environnement au moment du setup. Jamais sa valeur ici ni ailleurs dans le dépôt. Absente : voir `SECURITY.md`.
