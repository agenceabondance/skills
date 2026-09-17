# Journal des versions

## Non publié

- Le dépôt devient un dépôt de skills : `skills/local/` (`seo-local`, `audit-local`) et `skills/methode/` (`sourcer`, `ajouter-source`, `brevet-google`, `ask-abondance`). Chaque skill est user-invoked ou model-invoked ; `sourcer` devient l'unique propriétaire des niveaux de preuve ; plugin Claude Code dans `.claude-plugin/`.
- `seo-local` ne fait plus que le corpus (répondre, vérifier) ; l'audit en six phases avec critères de fin est `audit-local` ; la lecture de brevets est `brevet-google`.

## 0.1.0 - 2026-09-17

Premiere version, privee, soumise a relecture avant publication.

- Corpus : 8 fiches sources (Google x3, Resoneo, Whitespark 2026, Sterling Sky x2, Near Media) et 6 brevets Google, chacun avec son niveau de preuve ; index de routage ; registre de veille.
- Grille d'audit : 9 familles, 43 controles sources, codes de collecte ; gabarit de livrable.
- Scripts : `places.py` (Places API New, compteur et plafond d'appels, `--dry-run`), `audit.py` (CSV Places ou export de l'interface vers tableaux markdown), `brevet.py` (lecture de brevets sur Google Patents).
- Tests pytest sans reseau ni cle ; action GitHub.
