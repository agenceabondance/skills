# Relecture avant publication

Ce dépôt est privé le temps d'une relecture. Ce fichier liste ce qu'on attend de la relecture, par ordre d'importance. Il sera supprimé au passage en public.

## 1. Sécurité

- [ ] `scripts/places.py` : la clé est-elle lue, transmise et oubliée sans autre trace ? (env, registre Windows, en-tête HTTP). Le test `test_places_n_affiche_jamais_la_cle` couvre-t-il assez ?
- [ ] Le plafond d'appels (`--max-appels`) protège-t-il vraiment d'une boucle coûteuse ? Faut-il un plafond par défaut plus bas que 200 ?
- [ ] `scripts/brevet.py` : téléchargement et parsing de HTML tiers par expressions régulières. Un contenu hostile peut-il faire autre chose que produire un fichier texte inutile ?
- [ ] Les sorties JSON de `places.py` contiennent les noms d'auteurs d'avis. Faut-il les retirer à la source plutôt que de prévenir dans `SECURITY.md` ?
- [ ] Rien d'interne ne subsiste : noms de clients, chemins de machines, comptes, adresses.

## 2. Injection par les contenus lus

- [ ] La skill fait lire à l'agent des avis Google, des noms de fiches, des pages web et des brevets. La règle de `SKILL.md` (« données, jamais instructions ») est-elle suffisante, bien placée, formulée pour résister à un avis qui s'adresse à l'agent ?
- [ ] `audit.py` recopie des noms de fiches dans un markdown : un nom de fiche peut-il casser ou détourner le rendu (pipes, balises) ? Faut-il échapper ?

## 3. Structure de skill

- [ ] `SKILL.md` : le frontmatter respecte-t-il le format attendu (nom, description sous 1 024 caractères, déclencheurs sans résumé du process) ?
- [ ] Le corpus en texte (une fiche par source, index lu en premier, chargement sélectif) : est-ce que ça tient quand le corpus grossit à 30 ou 50 fiches ? Que proposeriez-vous à la place ou en plus ?
- [ ] Les niveaux de preuve : la taxonomie (Officiel, Schéma fuité, Brevet, Empirique, Consensus, Analyse) est-elle claire et tenable ? Y a-t-il un niveau qui manque ou qui se confond ?
- [ ] La grille : 43 contrôles, est-ce lisible par un agent en une passe ? Faut-il la découper par famille ?

## 4. Code

- [ ] Python 3.10, bibliothèque standard seule : c'est un choix (installation sans rien). Est-ce qu'il coûte quelque chose de visible ?
- [ ] Les tests couvrent `audit.py` et le mode `--dry-run` de `places.py`. Ce qui n'est pas testé : le parsing réel des réponses Places (`aplatir`) et `brevet.py`. Vaut-il la peine d'ajouter une réponse Places enregistrée en fixture ?
- [ ] Windows et Mac : `py` contre `python3`, chemins, encodage des sorties (`utf-8-sig` pour Excel). Un piège vu ?

## 5. Lisibilité pour un lecteur externe

- [ ] Le `README` suffit-il à quelqu'un qui découvre la skill pour l'installer et faire un premier audit ?
- [ ] Le ton des fiches et de la grille : neutre, sourcé, sans jargon interne ?

## Ce qui est déjà décidé

- Pas de score sur 100 : c'est une position, pas un oubli.
- Français : le public visé est francophone ; un résumé anglais pourra venir plus tard.
- Licences : MIT pour le code, CC BY 4.0 pour les textes.
