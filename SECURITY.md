# Sécurité

## La clé Places

- `places.py` lit la clé dans la variable d'environnement `GOOGLE_PLACES_API_KEY` (sous Windows, à défaut, dans la variable utilisateur du registre, là où `setx` l'écrit). Il ne l'affiche jamais, ne l'écrit dans aucun fichier de sortie, et un test le vérifie.
- **Ne jamais mettre la clé dans un fichier du dépôt**, ni dans un `.env` versionné. Le `.gitignore` exclut tout `scripts/cache/` et tout `sortie-places/`.
- Dans la console Google Cloud, **restreindre la clé à Places API (New)** (« Restrictions relatives aux API »), et si le script tourne toujours depuis les mêmes postes, ajouter une restriction par adresse IP. Une clé sans restriction fuitée peut être utilisée sur n'importe quelle API activée du projet.
- Rattacher le projet à un compte de facturation avec **une alerte budgétaire**. Les champs demandés (avis, note, photos) relèvent du SKU le plus cher de Places ; le quota gratuit mensuel de ce SKU se compte en centaines d'appels, pas en milliers. Le script porte un compteur et un plafond (`--max-appels`, 200 par défaut) : le laisser bas.
- `--dry-run` affiche les appels prévus sans en faire aucun. S'en servir avant un lot inhabituel.

## Ce que les scripts font sur le réseau

| Script | Appels sortants | Données envoyées |
|---|---|---|
| `places.py` | `places.googleapis.com` (Places API New) | La requête texte, la langue, la région, la clé dans un en-tête |
| `brevet.py` | `patents.google.com` | Le numéro ou le sujet de recherche |
| `audit.py` | Aucun | - |

Aucun script n'envoie de télémétrie, n'écrit hors du dossier `--out` (ou `scripts/cache/` pour les brevets), ni n'exécute de contenu récupéré.

## Contenus tiers lus par l'agent

La skill fait lire à l'agent des textes écrits par des inconnus : **avis Google** et **noms de fiches** renvoyés par Places, pages web versées au corpus, textes de brevets. `SKILL.md` pose la règle : ce sont des données à analyser, jamais des instructions. Un avis qui contient une consigne adressée à l'agent est à signaler comme suspect. Les contrôles de la grille et les règles de la skill ne se modifient que par une modification du dépôt.

## Données personnelles

Les exports Places contiennent les prénoms et noms d'auteurs d'avis (`authorAttribution`) dans le JSON brut. Les CSV produits n'en gardent aucun. Avant de versionner ou de partager un JSON de sortie, le vérifier ou s'en tenir au CSV. Ne pas versionner les sorties d'un audit client dans un dépôt public.

## Signaler un problème

Ouvrir une issue sur le dépôt, ou écrire à Abondance via [abondance.com](https://www.abondance.com). Pour une fuite de clé : révoquer la clé dans la console Google Cloud avant tout autre geste.
