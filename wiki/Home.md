# Family / Marriage / Faith Formation / OCIA Grants

Tracking grant opportunities a US (arch)diocesan office can apply for in the
areas of **family life, marriage, adult faith formation, faith formation /
catechesis, and OCIA/RCIA**.

Each page under [`grants/`](grants/) is one opportunity: YAML front matter is
the machine contract (parsed into the tracking table and database), and the
body is a boss-facing summary. Status values live in the front matter
(`researching`, `eligible`, `maybe`, `not_eligible`, `applied`, `awarded`,
`declined`, `excluded`).

## How to add a grant

1. Copy [`grants/_template.md`](grants/_template.md) to
   `grants/<Grantor>-<Grant>.md` (no spaces, Title-case words joined by dashes).
2. Fill every front matter field you can support with the grantor's OWN page
   (`source_url` must be the grantor's site — never an aggregator). Leave
   unknown amounts/deadlines blank and note why in the Verification list.
3. Write 1–3 boss-facing paragraphs: what it funds, why we qualify, what to do
   next. Add a `## Verification` list with dates checked.
4. Commit, push, then run `sh scripts/publish.sh` from the repo root to
   refresh `data/grants.csv`, the database, and the public table page.

## Index

(Populated below as research lands — status per the front matter `status`.)

| Page | Grantor | Focus areas | Status |
|---|---|---|---|
| — | — | — | — |