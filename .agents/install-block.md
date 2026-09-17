# Le bloc d'installation canonique

Un seul récit d'installation, un seul libellé. `README.md` et les pages `docs/` disent **ceci** et rien d'autre. On le change ici, puis on propage.

Le dépôt est sa propre marketplace Claude Code (`.claude-plugin/marketplace.json`). Le plugin n'est pas encore soumis à la marketplace officielle ; le jour où il l'est, `claude plugins install abondance-skills` remplace les deux lignes ci-dessous, et ce fichier change en premier.

## Claude Code : le plugin

<canonical-block name="claude-code">

```
/plugin marketplace add agenceabondance/skill-seo-local
/plugin install abondance-skills@abondance
```

Un paquet géré, en lecture seule, mis à jour quand le dépôt publie une version.

</canonical-block>

## Codex, et les autres agents : skills.sh

<canonical-block name="skills-sh">

```bash
npx skills@latest add agenceabondance/skill-seo-local
```

L'installeur laisse choisir les skills. `sourcer` est appelée par toutes les autres : la prendre. `npx skills@latest update` reprend les dernières modifications.

</canonical-block>

## Les deux voies s'excluent

Le plugin est un paquet géré qu'on suit ; skills.sh écrit des fichiers qu'on possède et qu'on modifie. Les deux ensemble donnent chaque skill en double : toujours dire « choisir une seule des deux ».
