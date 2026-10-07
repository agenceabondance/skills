## Ce qu'elle fait

`cocon-semantique` construit l'architecture de contenu d'un site autour d'un mot-clé pilier : audit, benchmark concurrentiel, cartographie des mots-clés, clusters par personas, classification TOFU/MOFU/BOFU, briefs avec Title et Meta description, jusqu'à un XLSX de dix feuilles exploitable par une équipe éditoriale. Chaque métrique vient d'un appel Haloscan documenté : si Haloscan ne répond pas, la skill s'arrête au lieu d'inventer, et elle qualifie la difficulté par le KGR parce que Haloscan n'expose aucun KD.

## Quand la prendre

Tapez `/cocon-semantique`, ou l'agent la prend seul quand la tâche s'y prête : cocon sémantique, étude de mots-clés, clustering, architecture de contenu, structuration de pages autour d'un pilier.

| Votre situation | Prendre |
|---|---|
| « Construis le cocon de ce site sur [pilier] » | `cocon-semantique` |
| « Quelles pages créer pour couvrir [thématique] ? » | `cocon-semantique` |
| Une question sur le classement d'une fiche dans Maps | [seo-local](../local/seo-local.md) |

## Prérequis

Le MCP Haloscan connecté (France). Un appel test valide l'accès en phase 0 ; sans lui, rien ne démarre.

## Le cadrage bloque, la SERP tranche

La phase 0 pose deux ou trois questions (site, concurrents, personas, pilier) avec des défauts proposés, puis la skill exécute sans redemander. Deux pages ne visent jamais le même mot-clé : la **similarité SERP** arbitre chaque paire suspecte, pas l'intuition. Un argument commercial sans demande de recherche (garantie, SAV) ne devient pas une page : il passe en bloc transversal des pages BOFU, là où l'utilisateur choisit.

## Ça marche si

- Le XLSX a dix feuilles, et la feuille méthodologie dit d'où vient chaque volume (une seule source, déclarée).
- Aucune colonne ne s'appelle KD ; la difficulté est un KGR, avec son seuil.
- Chaque page a un mot-clé principal unique, et les paires suspectes de cannibalisation sont arbitrées par écrit.

## Où elle se place

Une chaîne complète à elle seule, première skill du bucket organique. Elle ne cite pas de corpus : ses chiffres sont des données Haloscan datées, pas des affirmations sur Google. Pour la carte entière, [ask-abondance](../methode/ask-abondance.md).
