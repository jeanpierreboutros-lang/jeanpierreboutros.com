#!/bin/sh
# Merge this domain-scoped block while preserving the account's existing rules.
# Backups belong outside the public document root.
set -eu
target=${1:?"Usage: install-seo.sh DOCUMENT_ROOT PRIVATE_BACKUP_DIRECTORY"}
backup_dir=${2:?"A private backup directory is required"}
script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
fragment="$script_dir/seo.htaccess"
test -d "$target"
test -r "$fragment"
target=$(CDPATH= cd -- "$target" && pwd -P)
mkdir -p "$backup_dir"
backup_dir=$(CDPATH= cd -- "$backup_dir" && pwd -P)
case "$backup_dir/" in "$target/"*) echo "Backup directory must be outside the document root." >&2; exit 1;; esac
if test -L "$target/.htaccess"; then
  echo "Refusing to replace a symlinked .htaccess; inspect it first." >&2
  exit 1
fi
chmod 700 "$backup_dir"
temporary=$(mktemp "$target/.jpb-htaccess.XXXXXX")
remainder=$(mktemp "$backup_dir/.jpb-remainder.XXXXXX")
trap 'rm -f "$temporary" "$remainder"' EXIT HUP INT TERM
if test -f "$target/.htaccess"; then
  begin_count=$(awk '$0=="# BEGIN JPB MANAGED SEO"{n++} END{print n+0}' "$target/.htaccess")
  end_count=$(awk '$0=="# END JPB MANAGED SEO"{n++} END{print n+0}' "$target/.htaccess")
  if test "$begin_count" != "$end_count" || test "$begin_count" -gt 1; then
    echo "Unbalanced or repeated JPB block; inspect .htaccess before deployment." >&2
    exit 1
  fi
  if ! awk '
    $0=="# BEGIN JPB MANAGED SEO"{if(inside || closed) bad=1;inside=1}
    $0=="# END JPB MANAGED SEO"{if(!inside) bad=1;inside=0;closed=1}
    END{exit (bad || inside)}
  ' "$target/.htaccess"; then
    echo "Invalid JPB block order; inspect .htaccess before deployment." >&2
    exit 1
  fi
  awk '
    $0=="# BEGIN JPB MANAGED SEO"{inside=1;next}
    $0=="# END JPB MANAGED SEO"{inside=0;next}
    !inside{print}
  ' "$target/.htaccess" > "$remainder"
  cp -p "$target/.htaccess" "$temporary"
else
  : > "$remainder"
  chmod 644 "$temporary"
fi
cat "$fragment" "$remainder" > "$temporary"
if test -f "$target/.htaccess" && cmp -s "$target/.htaccess" "$temporary"; then
  echo "JPB redirects are already current."
  exit 0
fi
if test -f "$target/.htaccess"; then
  backup=$(mktemp "$backup_dir/htaccess-before-jpb.XXXXXX")
  cp -p "$target/.htaccess" "$backup"
  chmod 600 "$backup"
fi
mv "$temporary" "$target/.htaccess"
echo "Installed JPB redirects; existing non-JPB rules preserved."
