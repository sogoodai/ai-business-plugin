#!/usr/bin/env bash
# Copies the playbooks from sogoodai/ai-business-kit, their master copy, into skills/.
# Skills listed in OWNED live only in this repo. Edit every other skill in ai-business-kit, then run this.
#   scripts/sync-playbooks.sh [ref]          sync from a branch, tag or commit (default: main)
#   scripts/sync-playbooks.sh --check [ref]  exit 1 if skills/ differs from that ref
set -euo pipefail

REPO=sogoodai/ai-business-kit
SRC=plugins/marketing/skills
OWNED=(sogood)

root=$(cd "$(dirname "$0")/.." && pwd)
check=0
if [[ ${1:-} == --check ]]; then check=1; shift; fi
ref=${1:-main}

tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT
git -C "$tmp" init -q
git -C "$tmp" fetch -q --depth 1 "https://github.com/$REPO.git" "$ref"
git -C "$tmp" checkout -q FETCH_HEAD
sha=$(git -C "$tmp" rev-parse HEAD)

junk=(__pycache__ .ruff_cache .DS_Store)
excludes=() skip=()
for name in "${junk[@]}"; do excludes+=("--exclude=$name"); skip+=(-x "$name"); done
for name in "${OWNED[@]}"; do
  if [[ -e "$tmp/$SRC/$name" ]]; then
    echo "$REPO has a skill named $name, which this repo owns. Rename one of them." >&2
    exit 1
  fi
  excludes+=("--exclude=/$name/")
  skip+=(-x "$name")
done

if (( check )); then
  if ! changes=$(diff -rq "${skip[@]}" "$tmp/$SRC" "$root/skills"); then
    echo "skills/ differs from $REPO@${sha:0:7}:" >&2
    echo "$changes" >&2
    exit 1
  fi
  echo "skills/ matches $REPO@${sha:0:7}"
else
  rsync -a --delete "${excludes[@]}" "$tmp/$SRC/" "$root/skills/"
  echo "$REPO@$sha" > "$root/PLAYBOOKS_SOURCE"
  echo "Synced skills/ from $REPO@${sha:0:7}"
fi
