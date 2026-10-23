# scripts/import_mathesar.py — reload data/grants.csv into PG `grants` on chroma-server.
# Usage: python3 scripts/import_mathesar.py   (from the repo root)
# The wiki/ pages are the source of truth; this is a delete+reload projection,
# so there is no staging table and no upsert.
import csv

rows = list(csv.DictReader(open('data/grants.csv', newline='', encoding='utf-8')))
# gen_csv.py already validated rows; do not re-validate here (DRY).

def lit(v):
    return "NULL" if not str(v or '').strip() else "'" + str(v).replace("'", "''") + "'"

GRANTORS = {}   # grantor name -> (kind, website, contact_name, contact_email)
for r in rows:
    GRANTORS.setdefault(r['grantor'],
        (r['grantor_kind'], r['grantor_website'],
         r['contact_name'], r['contact_email']))

lines = ["BEGIN;", "DELETE FROM grants;", "DELETE FROM grantor;",
         # nextval() is not transactional: failed reruns advance sequences even
         # on rollback, which would break the fixed grantor_id mapping below.
         # Reset so the mapping (1..N) and the FKs stay correct on every reload.
         "ALTER SEQUENCE grantor_id_seq RESTART WITH 1;",
         "ALTER SEQUENCE grants_id_seq RESTART WITH 1;"]
ORDERED = sorted(GRANTORS)
GID = {g: i for i, g in enumerate(ORDERED, start=1)}
for g in ORDERED:
    kind, site, cn, ce = GRANTORS[g]
    vals = ", ".join(lit(v) for v in (g, kind, site, cn, ce))
    lines.append("INSERT INTO grantor (name, kind, website, contact_name,"
                 " contact_email) VALUES (" + vals + ");")
for r in rows:
    vals = ", ".join(lit(v) for v in (
        GID[r['grantor']], r['grant'], r['focus_areas'],
        r['amount_min'], r['amount_max'],
        r['award_type'] or 'cash', r['grantee_entity'], r['eligibility'],
        r['deadline_type'] or 'annual_cycle', r['next_deadline'],
        r['application_url'], r['status'], r['submitted_on'],
        r['decision'], r['award_amount'],
        r['source_url'], r['last_checked'], r['wiki_page']))
    lines.append("INSERT INTO grants (grantor_id, name, focus_areas, amount_min,"
        " amount_max, award_type, grantee_entity, eligibility, deadline_type,"
        " next_deadline, application_url, status, submitted_on, decision,"
        " award_amount, source_url, last_checked, wiki_page) VALUES ("
        + vals + ");")
lines.append("COMMIT;")
open('/tmp/grants_import.sql', 'w').write("\n".join(lines) + "\n")
print(f"wrote /tmp/grants_import.sql; grantors={len(GRANTORS)} grants={len(rows)}")
# NOTE: the grants INSERT column order MUST match scripts/_schema.sql exactly —
# it does; change both together. Contact fields collapse into the grantor INSERT
# above.