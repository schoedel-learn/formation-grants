# formation-grants

Grant research and tracking for Catholic formation ministries — **family life,
marriage, adult faith formation, faith formation/catechesis, and OCIA/RCIA** —
for a US (arch)diocesan office.

## The contract

1. **`wiki/` is the source of truth.** One page per grant opportunity
   (`wiki/grants/<Grantor>-<Grant>.md`), each with a YAML front matter block
   (the machine contract) and a boss-facing prose body. `wiki/Home.md` is the
   index; `wiki/Runbook.md` is the research/verification contract.
2. **Edit data ONLY in wiki front matter.** Then run `sh scripts/publish.sh`,
   which regenerates everything else. Never hand-edit `data/grants.csv` or the
   database.
3. **The Mathesar database `grants` is a derived projection, read-only.** Every
   row carries its `wiki_page` filename for traceability.
4. **Boss views:**
   - Code Wiki page for this repo — requested 2026-10-22 via
     codewiki-feedback@google.com (public preview, no self-serve ingestion);
     recorded here once live. The token table below does not depend on it.
   - Token table `https://grants.educatebarry.co/<token>/` — generated, dated,
     and current. Token and DB credentials live in the owner's Secrets store,
     never in this repo (the repo is public).
5. **Requirements:** Python 3 with
   `python3 -m pip install --user python-frontmatter`.

## Refresh pipeline

`scripts/publish.sh`: `git pull` → `gen_csv.py` (wiki front matter →
`data/grants.csv`) → `import_mathesar.py` (CSV → PostgreSQL `grants`, delete +
reload) → `gen_site.py` (CSV → `site/index.html`) → rsync to the web host →
curl-verified.

## Verification rules

Every grant row must carry `source_url` = the grantor's OWN page (never an
aggregator), a `last_checked` date, and fill amounts/deadlines only when the
source page states them. Ambiguous eligibility becomes `status: maybe` with the
ambiguity quoted. See `wiki/Runbook.md`.