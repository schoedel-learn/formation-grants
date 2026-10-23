#!/bin/sh
# scripts/publish.sh — wiki -> csv -> PG -> html -> grants.educatebarry.co, verified.
# The wiki/ pages are the source of truth; everything downstream is regenerated.
# Usage: sh scripts/publish.sh        (from the repo root; dash-safe)
set -eu
cd "$HOME/Documents/Development/formation-grants"
PYTHON=python3; [ -x .venv/bin/python3 ] && PYTHON=.venv/bin/python3   # repo venv has python-frontmatter
# CSV is a committed artifact: a dirty local regen gets committed before pulling,
# otherwise `git pull --rebase` refuses to run on a dirty tree.
git add data/grants.csv 2>/dev/null || true
git diff --cached --quiet -- data/grants.csv || git commit -m "data refresh (publish pre-step)"
git pull --rebase
"$PYTHON" scripts/gen_csv.py
"$PYTHON" scripts/import_mathesar.py
scp -q /tmp/grants_import.sql chroma-server:/tmp/
ssh chroma-server "docker cp /tmp/grants_import.sql postgresql-db-db-1:/tmp/ && \
  docker exec postgresql-db-db-1 psql -U grants_app -d grants -f /tmp/grants_import.sql \
  && rm /tmp/grants_import.sql"
rm -f /tmp/grants_import.sql
python3 scripts/gen_site.py
TOKEN=$(read-secret-value GRANTS_PUBLICATION_TOKEN)   # key: Secrets.md ## Grants DB
ssh lx-primary 'rm -rf /tmp/grants-stage && mkdir -p /tmp/grants-stage'
scp -q site/index.html lx-primary:/tmp/grants-stage/
ssh lx-primary "sudo mkdir -p '/var/lib/docker/volumes/matrix_caddy_data/_data/sites/grants.educatebarry.co/$TOKEN' && \
  sudo rsync -a --delete /tmp/grants-stage/ '/var/lib/docker/volumes/matrix_caddy_data/_data/sites/grants.educatebarry.co/$TOKEN/'"
code=$(curl -s -o /dev/null -w '%{http_code}' "https://grants.educatebarry.co/$TOKEN/")
[ "$code" = 200 ] || { echo "publish verification FAILED: $code"; exit 1; }
echo "published OK ($(date))"
# Volume path /var/lib/docker/volumes/... is CORRECT; the container mounts it at
# /data (root * /data/sites/...). Any other host path is a trap.