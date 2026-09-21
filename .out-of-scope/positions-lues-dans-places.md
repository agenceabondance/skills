# Lire des positions dans l'API Places

`places.py` ne rend pas de rang, et les demandes d'un mode « position dans le pack » sont hors périmètre.

## Pourquoi

Une recherche Places par texte n'est pas le pack local : elle ne prend pas en compte le point de mesure de l'utilisateur, la personnalisation ni la mise en page des résultats. L'ordre renvoyé ressemble à un classement, et c'est ce qui le rend dangereux : un livrable qui le recopie promet une position que Google n'affiche à personne.

Les positions viennent d'un suivi par point de mesure (famille E de la grille) : un outil de suivi Maps ou une grille géographique. `places.py` sert à l'inventaire d'un pack (qui est présent, avec quelle note, quelle catégorie), jamais au rang.

## Demandes reçues

- Aucune pour l'instant ; `audit.py` est testé pour ne rendre ni verdict ni score (`test_audit_pack_ne_rend_pas_de_verdict_ni_de_score`).
