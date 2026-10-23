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

## Grants received (2025–2027)

A records scan of grants Archdiocese of San Antonio entities are already
receiving — IRS 990 grantee schedules plus funder/archdiocesan public reporting —
is consolidated at [`Grants-Received-2025-2027.md`](Grants-Received-2025-2027.md)
(details: [`received/Lane-G-990-Grantee-Records.md`](received/Lane-G-990-Grantee-Records.md)
and [`received/Lane-H-Public-Reporting-Records.md`](received/Lane-H-Public-Reporting-Records.md)).
Next re-check: FY2025 990s, projected November 2026–February 2027.

## Index

| [Diocesan Grant Application (plus BCIM and CNAMB school/religious-education grants)](grants/Black-And-Indian-Mission-Office-Diocesan-Grants) | Black and Indian Mission Office | ['faith_formation', 'adult_faith_formation'] | eligible |
| [Grant Program (Religion thematic area)](grants/Carrie-Estelle-Doheny-Foundation-Religion-Grants) | Carrie Estelle Doheny Foundation | ['faith_formation'] | maybe |
| [Endowment and Donor Advised Fund Distributions](grants/Catholic-Community-Foundation-Baltimore-Grant-Funds) | The Catholic Community Foundation | — | researching |
| [Tabor Fund Grant Program](grants/Catholic-Community-Foundation-Cleveland-Tabor-Fund) | The Catholic Community Foundation | ['faith_formation'] | maybe |
| [Education, Lay Leadership and Community Grant Cycle](grants/Catholic-Community-Foundation-Milwaukee-Grants) | The Catholic Community Foundation | ['faith_formation', 'family'] | maybe |
| [Formation and Action Grants Program (with Small Group and Parish Ministry grants)](grants/Catholic-Community-Foundation-Minnesota-Formation-And-Action-Grants) | Catholic Community Foundation of Minnesota | ['adult_faith_formation', 'faith_formation'] | maybe |
| [Women's Giving Circle Grants (2027 cycle)](grants/Catholic-Community-Foundation-New-Orleans-Wgc-Grants) | Catholic Community Foundation | ['family', 'faith_formation'] | maybe |
| [Parish Endowments Matching Program (1:1 match, up to $5,000)](grants/Catholic-Community-Foundation-San-Antonio-Endowment-Services) | Catholic Community Foundation (Archdiocese of San Antonio) | — | not_eligible |
| [National Scholarships and Contests; National Projects & Charities](grants/Catholic-Daughters-Of-The-Americas-Scholarships-And-Charities) | Catholic Daughters of the Americas | — | not_eligible |
| [Catholic School Tuition Assistance (K-12 Scholarships)](grants/Catholic-Education-Foundation-Joliet-Scholarships) | Catholic Education Foundation of the Diocese of Joliet | — | not_eligible |
| [Diocesan Funding Requests (six funding categories)](grants/Catholic-Extension-Society-Extension-Dioceses-Funding) | Catholic Extension Society | ['family', 'faith_formation', 'adult_faith_formation'] | maybe |
| [Women's Philanthropic Giving Circle (WPGC) Grants](grants/Catholic-Foundation-Central-Florida-Wpgc-Grants) | Catholic Foundation of Central Florida | ['faith_formation'] | maybe |
| [Philanthropy Fund Grant Cycle (Spring & Fall)](grants/Catholic-Foundation-Dallas-Philanthropy-Fund-Grants) | The Catholic Foundation (Dallas, TX) | — | not_eligible |
| [2026-2027 Grant Programs (incl. Evangelization and Worship; Women in Philanthropy)](grants/Catholic-Foundation-Greater-Philadelphia-Grant-Programs) | Catholic Foundation of Greater Philadelphia | ['faith_formation'] | maybe |
| [Advancing the Mission Evangelization & Lifelong Catechesis Grants](grants/Catholic-Foundation-Green-Bay-Advancing-The-Mission-Grants) | Catholic Foundation for the Diocese of Green Bay | ['family', 'marriage', 'ocia', 'adult_faith_formation'] | maybe |
| [Impact Grants (incl. Empowering Catholic Education & Formation)](grants/Catholic-Foundation-Michigan-Impact-Grants) | Catholic Foundation of Michigan | ['adult_faith_formation', 'faith_formation'] | maybe |
| [Catholic Community Grants (Fall Cycle)](grants/Catholic-Foundation-North-Georgia-Catholic-Community-Grants) | Catholic Foundation of North Georgia | — | not_eligible |
| [2026 Grant Program](grants/Catholic-Foundation-Northeast-Kansas-Grant-Program) | Catholic Foundation of Northeast Kansas | — | researching |
| [Endowment Fund Disbursements (no competitive grant program)](grants/Catholic-Foundation-Sacramento-Endowment-Disbursements) | The Catholic Foundation (Diocese of Sacramento) | — | not_eligible |
| [Mother Teresa Women's Giving Circle Grants](grants/Catholic-Foundation-South-Louisiana-Mother-Teresa-Wgc-Grants) | Catholic Foundation of South Louisiana | ['family'] | maybe |
| [Catholic Marriage Ministry Matching Grants](grants/Catholic-Marriage-Initiatives-Fund-Catholic-Marriage-Matching-Grants) | Catholic Marriage Initiatives Fund | ['family', 'marriage'] | researching |
| [Local Court Partnership Funding](grants/Catholic-Order-Of-Foresters-Partnership-Funding) | Catholic Order of Foresters | ['faith_formation'] | maybe |
| [Foundation Grant Programs (Chastity & Abstinence Education, Education Technology, Event Sponsorship, Matching Grants)](grants/Catholic-United-Financial-Foundation-Grant-Programs) | Catholic United Financial, a Trusted Fraternal Life brand | ['faith_formation'] | eligible |
| [Grants 4 Good](grants/Catholic-United-Financial-Grants-4-Good) | Catholic United Financial, a Trusted Fraternal Life brand | ['family', 'faith_formation'] | maybe |
| [Community Marriage Initiative Grants](grants/Community-Marriage-Initiatives-Fund-Community-Marriage-Initiatives-Grants) | Community Marriage Initiatives Fund | ['family', 'marriage'] | maybe |
| [Annunciation Grant Cycle](grants/Incarnate-Word-Foundation-Annunciation-Grant-Cycle) | Incarnate Word Foundation | ['family'] | maybe |
| [Sectarian (Catholic) Grants Program](grants/Kenedy-Memorial-Foundation-Catholic-Grants) | The John G. & Marie Stella Kenedy Memorial Foundation | ['faith_formation'] | applied |
| [Faith in Action Family Programs](grants/Knights-Of-Columbus-Faith-In-Action-Family-Programs) | Knights of Columbus | ['family'] | not_eligible |
| [Annual Grant Program (Letter of Request)](grants/Koch-Foundation-Catholic-Grants) | The Koch Foundation | ['faith_formation'] | applied |
| [National Initiative to Strengthen Christian Campus Ministries at Colleges and Universities (Campus Ministry Initiative)](grants/Lilly-Campus-Ministry-Initiative) | Lilly Endowment Inc. | ['adult_faith_formation', 'faith_formation'] | eligible |
| [National Initiative to Strengthen Chaplaincies at Colleges and Universities (Chaplaincy Initiative)](grants/Lilly-Chaplaincy-Initiative) | Lilly Endowment Inc. | ['faith_formation'] | not_eligible |
| [Christian Parenting and Caregiving Initiative](grants/Lilly-Christian-Parenting-and-Caregiving) | Lilly Endowment Inc. | ['family'] | not_eligible |
| [Exploring Christian Practices Initiative](grants/Lilly-Exploring-Christian-Practices) | Lilly Endowment Inc. | ['adult_faith_formation', 'faith_formation'] | not_eligible |
| [Nurturing Children Through Worship and Prayer Initiative (incl. Initiative II)](grants/Lilly-Nurturing-Children-Through-Worship-and-Prayer) | Lilly Endowment Inc. | ['family', 'faith_formation'] | maybe |
| [Serving Neighbors Through Congregational Collaborations Initiative](grants/Lilly-Serving-Neighbors-Through-Congregational-Collaborations) | Lilly Endowment Inc. | ['family', 'faith_formation'] | eligible |
| [Capital Grants for Historic Houses of Worship](grants/National-Fund-For-Sacred-Places-Capital-Grants) | National Fund for Sacred Places | — | not_eligible |
| [Making Parishes Everyone's Home (Parish Mentorship Initiative)](grants/Ncpd-Making-Parishes-Everyones-Home) | National Catholic Partnership on Disability | ['faith_formation'] | researching |
| [CorWorks Parish Accelerator (seed funding)](grants/Osv-Institute-Corworks) | OSV Institute for Catholic Innovation | — | not_eligible |
| [Domestic Grant Program (Spring and Fall cycles)](grants/Raskob-Foundation-Domestic-Grant-Program) | Raskob Foundation for Catholic Activities | ['family', 'faith_formation', 'adult_faith_formation'] | eligible |
| [Beyond Sunday Scholarships (tuition assistance and school grants)](grants/Roman-Catholic-Foundation-St-Louis-Beyond-Sunday) | Roman Catholic Foundation of Eastern Missouri | — | not_eligible |
| [Grant Program (Sessions 2027A and 2027B)](grants/Scanlan-Foundation-Grant-Sessions) | Scanlan Foundation | ['marriage', 'family', 'faith_formation'] | applied |
| [Vocations Grant Program](grants/Serra-International-Foundation-Vocations-Grant) | The Serra International Foundation | ['faith_formation'] | maybe |
| [Society for the Propagation of the Faith (mission grants/subsidies)](grants/Society-For-The-Propagation-Of-The-Faith) | Society for the Propagation of the Faith (The Pontifical Mission Societies USA) | — | not_eligible |
| [Pilgrims of Hope Matching Grant](grants/Trusted-Fraternal-Life-Pilgrims-Of-Hope-Matching-Grant) | Trusted Fraternal Life | ['faith_formation', 'family'] | maybe |
| [Catholic Campaign for Human Development (CCHD) Community & Economic Development Grants](grants/USCCB-Catholic-Campaign-For-Human-Development) | USCCB Catholic Campaign for Human Development | — | not_eligible |
| [Catholic Communication Campaign (CCC) Grants](grants/USCCB-Catholic-Communication-Campaign) | USCCB Committee on Communications (Catholic Communication Campaign) | ['faith_formation'] | maybe |
| [Catholic Home Missions Appeal Grants](grants/USCCB-Catholic-Home-Missions) | USCCB Subcommittee on Catholic Home Missions | ['faith_formation'] | maybe |
| [Legacy of Faith Faith Formation Grants](grants/Up-Catholic-Foundation-Legacy-Of-Faith-Grants) | U.P. Catholic Foundation (Diocese of Marquette) | ['faith_formation', 'family'] | maybe |
