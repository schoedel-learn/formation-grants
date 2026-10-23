# scripts/gen_csv.py — parse wiki grant pages -> data/grants.csv
# Usage: python3 scripts/gen_csv.py   (from the repo root)
# The wiki/ directory is the source of truth; this script is validation + export.
import csv, glob, os, sys
import frontmatter

FIELDS = ['grant', 'grantor', 'grantor_website', 'grantor_kind', 'contact_name',
          'contact_email', 'focus_areas', 'amount_min', 'amount_max', 'award_type',
          'grantee_entity', 'eligibility', 'deadline_type', 'next_deadline',
          'application_url', 'status', 'submitted_on', 'decision', 'award_amount',
          'source_url', 'last_checked', 'wiki_page']
# NOTE: this list feeds import_mathesar.py too; change both together with
# scripts/_schema.sql.
ALLOWED_FOCUS = {'family', 'marriage', 'adult_faith_formation',
                 'faith_formation', 'ocia'}
ALLOWED_STATUS = {'researching', 'eligible', 'maybe', 'not_eligible',
                  'applied', 'awarded', 'declined', 'excluded'}

WIKI = os.environ.get('GRANTS_WIKI', 'wiki')

def norm_focus(v):
    if isinstance(v, str):
        v = [v]
    try:
        return ' '.join(x for x in v if x in ALLOWED_FOCUS)
    except TypeError:
        return ''

pages, errors = [], []
for path in sorted(glob.glob(os.path.join(WIKI, 'grants', '*.md'))):
    if os.path.basename(path).startswith('_'):     # template
        continue
    pm = frontmatter.load(path)
    if not pm.get('grant') or not pm.get('grantor'):
        errors.append(f"{path}: missing grant/grantor"); continue
    if not str(pm.get('source_url') or '').startswith('http'):
        errors.append(f"{path}: bad source_url"); continue
    if not str(pm.get('last_checked') or '').count('-') == 2:
        errors.append(f"{path}: last_checked must be YYYY-MM-DD"); continue
    if pm.get('status') not in ALLOWED_STATUS:
        errors.append(f"{path}: bad status {pm.get('status')!r}"); continue
    row = {k: pm.get(k, '') for k in FIELDS if k not in ('focus_areas', 'wiki_page')}
    row['focus_areas'] = norm_focus(pm.get('focus_areas'))
    row['wiki_page'] = os.path.relpath(path, WIKI)
    for k in ('amount_min', 'amount_max', 'award_amount'):
        s = str(row[k] or '').replace('.', '', 1)
        row[k] = row[k] if s.isdigit() else ''
    pages.append(row)

os.makedirs('data', exist_ok=True)
with open('data/grants.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=FIELDS)
    w.writeheader()
    w.writerows(pages)
elig = sum(1 for p in pages if p['status'] in ('eligible', 'maybe'))
print(f"pages: {len(pages)}; eligible/maybe: {elig}; errors: {len(errors)}")
for e in errors:
    print("  ", e)
if errors or elig < 25:
    sys.exit(1)