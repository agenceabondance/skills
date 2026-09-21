---
name: ajouter-source
description: "Ajouter une source (page, étude, brevet) à un corpus Abondance, avec son niveau de preuve."
argument-hint: "URL, numéro de brevet, ou sujet à chercher"
disable-model-invocation: true
---

# Ajouter une source

Une source entre avec son éditeur, sa date et son niveau de preuve, ou n'entre pas. Le corpus visé est celui de la skill nommée par l'utilisateur (`seo-local` : `references/` de cette skill) ; son `00-index.md` est le registre à tenir à jour.

Call the Skill tool with "sourcer" : les niveaux de preuve, et le niveau qu'une source justifie.

## Page ou étude

1. Récupérer la page. Contrôler la fiabilité : éditeur identifié, méthode exposée (échantillon, période, mesure). Une page sans méthode entre en **Analyse**, ou n'entre pas : demander à l'utilisateur.
2. Rédiger la source depuis [`GABARIT-SOURCE.md`](GABARIT-SOURCE.md), numérotée à la suite du corpus.
3. Une ligne dans la table Sources de `00-index.md`, et dans les repères de routage si la source répond à une question qui n'y figurait pas. Si la page peut évoluer (édition annuelle, doc Google), une entrée dans le `_veille.md` du corpus.
4. Si la source comble un des trous connus de l'index, retirer le trou.

## Brevet

Call the Skill tool with "brevet-google" : il lit le brevet sur ses revendications et rédige la source. Ici, seulement la ligne dans la table Brevets de `00-index.md`, avec le statut daté.

## Terminé quand

- [ ] La source porte éditeur, date de publication, date d'ajout, niveau de preuve, lien.
- [ ] `00-index.md` la référence (table et routage), et `_veille.md` si elle se périme.
- [ ] Le niveau de preuve est celui que la source justifie, pas le plus flatteur.
