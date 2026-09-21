# Pas de score global : un verdict par famille

Décidé dès la première version, avant publication, lors de la relecture du dépôt.

Les poids des signaux ne sont pas publics ([04]). Un audit qui rend « 72/100 » additionne des poids qu'il n'a pas, et le lecteur ne peut plus distinguer ce qui est vérifié de ce qui est deviné.

Décision : `audit-local` rend un verdict par famille (✅ 🟠 🔴 ⚪) et des actions classées par risque, effort et niveau de preuve. Une famille sans donnée est ⚪ et le reste ; le livrable la nomme en section 2 et en section 7. `audit.py` est testé pour ne produire ni verdict ni score.

Les demandes de score sont hors périmètre : `.out-of-scope/score-global.md`.
