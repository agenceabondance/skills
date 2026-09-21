# Local

Le classement d'une fiche d'établissement dans Google : pack local, Maps.

## User-invoked

Accessibles seulement quand vous les tapez (Claude Code : `disable-model-invocation: true` ; Codex : `policy.allow_implicit_invocation: false` dans `agents/openai.yaml`).

- **[audit-local](./audit-local/SKILL.md)** : auditer une fiche ou un réseau en six phases, chacune avec son critère de fin, jusqu'au livrable. Porte la grille (9 familles, 43 contrôles), le gabarit de livrable, `places.py` et `audit.py`.

## Model-invoked

Accessibles par vous ou par l'agent quand la tâche s'y prête.

- **[seo-local](./seo-local/SKILL.md)** : le corpus (huit sources, six brevets, index de routage). Répondre à une question de classement local avec des sources, vérifier qu'une recommandation est étayée.
