# Research runbook

## Scope

Applicant: a US (arch)diocesan office. Areas -> focus_areas tags:

- family life -> `family`
- marriage -> `marriage`
- adult catechesis -> `adult_faith_formation`
- catechesis/formation -> `faith_formation`
- OCIA/RCIA/catechumenate -> `ocia`

## Search lanes — run ALL, several pages deep

**Owner quality bar (2026-10-27):** pages only for MAJOR funders — typical
awards ≥$50k (ideally $100k+), eligibility fitting a LARGE archdiocesan office.
No parish-only funds, no other diocese's own foundation, no micro grants.
Culled/near-miss research is recorded in `wiki/NEAR-MISSES.md`, never lost.

1. **USCCB grant programs** (site:usccb.org grants; Catholic Home Missions;
   Catholic Communication Campaign; Society for the Propagation of the Faith;
   Proclamation of the Faith).
2. **National Catholic foundations**: Our Sunday Visitor Institute; Catholic
   Extension Society; the FADICA member foundation list (check EVERY member);
   major archdiocesan Catholic Community Foundations (St. Louis,
   Galveston-Houston, Baltimore, Chicago, New Orleans); National Catholic
   Partnership on Disability.
3. **Ecumenical-but-open**: Lilly Endowment congregational initiatives (e.g.
   Nurturing Children through Worship and Prayer and successors) — verify each
   initiative's eligibility page individually; many accept Catholic dioceses.
4. **OCIA-specific**: "OCIA grant", "RCIA funding", "catechumenate grant",
   North American Forum on the Catechumenate.
5. **Family/marriage**: Knights of Columbus family/council program funding,
   "marriage and family ministry grant", Catholic marriage program funds.
6. **Aggregators** (Candid/Foundation Directory, GrantWatch, Instrumentl) are
   for DISCOVERY ONLY — never the `source_url` row.
7. **Federal (lane K)**: grants.gov, HHS/ACF CFDA 93.086 family (HEART, FORGE,
   READY4Life), AmeriCorps State & National + VISTA. A diocese is a 501(c)(3);
   quote NOFO eligibility verbatim. Watch CFDA 93.086 for the next NOFO — 2025
   cohort closed with next competition several years out.
8. **San Antonio / South Texas (lane L)**: Methodist Healthcare Ministries
   (~$250k average), Baptist Health Foundation SA ($25k–$300k), Valero Energy
   Foundation, H-E-B Tournament of Champions; SAAF funds beyond Special & Urgent
   Needs are near-missed ("religious worship or instruction" exclusion).
9. **Texas-wide private (lane M)**: Meadows Foundation (rolling; Jan/Apr/Jun/
   Sep/Nov boards), plus verify any statewide private grantmaker with an open
   cycle and matching focus.
10. **National faith-friendly secular (lane N)**: Templeton network and peers —
    mostly invitation-only or closed; keep watchlist status pages.
11. **990 mining (lane P)**: ProPublica NonProfit Explorer API — parse big
    grantors' Schedule-recipients for 'diocese/catholic' payments; mine peer
    large archdioceses' 990s for their grantors. Evidence-backed funder
    discovery; see skill reference deep-research-methods.md.

## Qualification filter (status=eligible ONLY if ALL true)

- US funding; US applicant accepted. Foreign-only: exclude.
- Eligibility names diocese/archdiocese (or parish with diocesan endorsement ->
  `grantee_entity: diocesan_or_parish`). Not exclusively non-Catholic churches,
  individuals, businesses, or schools-only.
- At least one focus area matches. Pure building funds / schools-only academic
  funds: exclude — unless a director would misread their absence, in which case
  write the page with `status: not_eligible`.
- A funding cycle, deadline, or rolling line of funding is visible; a dead page
  whose last cycle ended >12 months ago with no successor: exclude.

## Verification rules (anti-hallucination)

- `source_url` MUST be the grantor's own page; you opened it, it loads, and it
  says what you wrote. `last_checked` = the date you verified.
- Amounts/`next_deadline`: fill ONLY what the page states; otherwise leave
  blank and say so in the Verification list. Do NOT guess.
- Ambiguous eligibility -> `status: maybe` with the ambiguity quoted verbatim.
- Contact names/emails come from the grantor's own page (kept per owner
  decision 2026-10-22; they are publicly published there anyway).
- Page naming: `grants/<Grantor>-<Grant>.md` (no spaces; Title-case words
  joined by dashes).
- Floor before the corpus ships: 25 pages with status `eligible` or `maybe`.