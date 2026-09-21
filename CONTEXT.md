# Skills Abondance

Des skills pour agents, organisées en buckets par sujet, qui partagent une discipline de citation (`sourcer`) et une configuration par dépôt écrite par `/setup-abondance-skills`.

## Vocabulaire

**Fiche** :
La fiche d'établissement Google (ex-Google My Business) : ce que le public voit dans Maps et le pack local, ce que le propriétaire gère dans son interface. Toujours ce sens-là.
_Éviter_ : fiche GBP, listing, profil.

**Source** :
Une entrée du corpus : un fichier de `references/`, numéroté `[NN]`, rédigé depuis le gabarit de `ajouter-source`, portant son niveau de preuve. Un brevet est une source numérotée `[USxxxx]`, dans `references/brevets/`.
_Éviter_ : fiche source, fiche du corpus (« fiche » est réservé à l'établissement).

**Corpus** :
L'ensemble des sources d'un sujet, avec son `00-index.md` qui route une question vers les sources à lire. Un corpus par bucket ; `seo-local` porte celui du local.

**Niveau de preuve** :
Ce que la source autorise à écrire : Officiel, Empirique, Consensus, Schéma fuité, Brevet, Analyse. Défini une seule fois, dans `sourcer`.
_Éviter_ : fiabilité (c'est une autre colonne de l'index : la confiance dans l'éditeur, pas la nature de la preuve), poids.

**Adossé** :
Se dit d'une affirmation qui cite sa source `[NN]` ou `[USxxxx]` avec son niveau de preuve. Une affirmation qui ne l'est pas porte `(hors corpus)`. C'est le mot de la discipline.

**Hors corpus** :
La marque d'une affirmation qu'aucune source ne porte. Pas un défaut : un aveu, qui dit au lecteur où s'arrête ce qu'on sait.

**Contrôle** :
Une ligne de la grille d'audit : ce qu'on vérifie, où prendre la donnée, quelle source le fonde, si le propriétaire peut agir. 43 contrôles en 9 familles.

**Famille** :
Un groupe de contrôles (A. Conformité, B. Complétude, ... I. Multi-établissements). L'unité du verdict.

**Verdict** :
Ce que l'audit rend par famille : ✅ conforme, 🟠 à améliorer, 🔴 bloquant, ⚪ non vérifié. Jamais un chiffre.
_Éviter_ : score, note.

**Livrable** :
Le document d'audit, en huit sections depuis le gabarit de `audit-local`. Les sections 2 (données non disponibles) et 7 (ce que l'audit ne dit pas) en font partie au même titre que les autres.

**Pack local** :
Les trois fiches (ou plus) que Google affiche avec une carte sur une requête à intention locale. Ce que l'audit compare, ce qu'un suivi de positions mesure. Une recherche Places par texte n'est pas le pack local.

**Requête à intention locale** :
Forte (« plombier Nantes », « près de moi ») ou faible (« plombier ») ; seule la première relève de la fiche. Qualifiée en phase 1 de l'audit.

**Réseau** :
Plusieurs fiches d'une même marque. Famille I de la grille ; `places.py reseau` les inventorie.

## Relations

- Un **corpus** contient des **sources** ; son `00-index.md` les route.
- Chaque **source** porte un **niveau de preuve**.
- Un **contrôle** est **adossé** à une ou plusieurs **sources**, ou marqué **hors corpus**.
- Une **famille** groupe des **contrôles** et reçoit un **verdict**.
- Un **livrable** rend un **verdict** par **famille** pour une **fiche** ou un **réseau**.

## Ambiguïtés levées

- « Fiche » désignait à la fois la fiche d'établissement Google et une entrée du corpus (« fiche 05 », « une fiche par source »). Résolu : **fiche** est l'établissement, **source** est l'entrée du corpus. Les skills, les README et l'index suivent la règle ; le texte interne des sources (`references/*.md`, section « À relier ») porte encore l'ancien usage et se corrige au fil des relectures.
- « Score » et « verdict » se sont côtoyés dans les premiers brouillons. Résolu : **verdict**, par famille ; le score est hors périmètre (`.out-of-scope/score-global.md`).
