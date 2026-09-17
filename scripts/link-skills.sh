#!/usr/bin/env bash
set -euo pipefail

# Script de developpement, pour les mainteneurs du depot. Ce n'est pas un
# installeur pris en charge : les voies d'installation sont dans README.md.
#
# Lie chaque skill des buckets promus dans les dossiers de skills locaux :
#   - ~/.claude/skills : Claude Code
#   - ~/.agents/skills : Codex et les autres harnais compatibles Agent Skills
# Chaque entree est un lien symbolique vers ce depot : un `git pull` suffit
# pour que les skills installees soient a jour. Relancer apres un ajout, un
# retrait ou un renommage.

REPO="$(cd "$(dirname "$0")/.." && pwd)"
DESTS=("$HOME/.claude/skills" "$HOME/.agents/skills")

names=()
srcs=()
while IFS= read -r -d '' skill_md; do
  src="$(dirname "$skill_md")"
  names+=("$(basename "$src")")
  srcs+=("$src")
done < <(find "$REPO/skills/local" "$REPO/skills/methode" -name SKILL.md -print0)

for DEST in "${DESTS[@]}"; do
  if [ -L "$DEST" ]; then
    resolved="$(readlink -f "$DEST")"
    case "$resolved" in
      "$REPO"|"$REPO"/*)
        echo "erreur : $DEST est un lien vers ce depot ($resolved)." >&2
        echo "Le retirer (rm \"$DEST\") et relancer ; le script le recreera comme un vrai dossier." >&2
        exit 1
        ;;
    esac
  fi
  mkdir -p "$DEST"
  for i in "${!names[@]}"; do
    target="$DEST/${names[$i]}"
    if [ -e "$target" ] && [ ! -L "$target" ]; then
      rm -rf "$target"
    fi
    ln -sfn "${srcs[$i]}" "$target"
    echo "lie ${names[$i]} -> ${srcs[$i]} ($DEST)"
  done
done
