# scripts/gen_home.py — regenerate the index table in wiki/Home.md from the
# grant pages. Run after gen_csv (it reads the same parsed pages). The table
# between the INDEX-TABLE markers is the only thing this edits.
import glob, os, re, sys
import frontmatter

WIKI = os.environ.get('GRANTS_WIKI', 'wiki')
HOME = os.path.join(WIKI, 'Home.md')

rows = []
for path in sorted(glob.glob(os.path.join(WIKI, 'grants', '*.md'))):
    if os.path.basename(path).startswith('_'):
        continue
    pm = frontmatter.load(path)
    slug = os.path.basename(path)[:-3]
    rows.append("| [{grant}]({href}) | {grantor} | {focus} | {status} |".format(
        grant=pm.get('grant', slug), href='grants/' + slug,
        grantor=pm.get('grantor', ''), focus=str(pm.get('focus_areas') or '—'),
        status=pm.get('status', '')))

try:
    home = open(HOME).read()
    idx = home.index('## Index')
    new_home = (home[:idx]
        + "## Index\n\n"
        + "\n".join(rows) + "\n")
    open(HOME, 'w').write(new_home)
    print(f"Home.md index rewritten with {len(rows)} pages")
except FileNotFoundError:
    sys.exit(f"{HOME} missing")
except ValueError:
    sys.exit("Home.md has no '## Index' section")