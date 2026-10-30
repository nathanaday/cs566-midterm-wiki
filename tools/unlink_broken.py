import os, re, sys
from collections import Counter

VAULT = sys.argv[1] if len(sys.argv) > 1 else "/Users/nathanaday/projects/usc/cs566-course/Midterm-Wiki"
LINK_RE = re.compile(r"!?\[\[([^\]\|#]+)(#[^\]\|]*)?(?:\|([^\]]*))?\]\]")

by_rel, stems = {}, set()
for dirpath, dirs, files in os.walk(VAULT):
    dirs[:] = [d for d in dirs if not d.startswith(".")]
    for f in files:
        if f.startswith("."): continue
        rel = os.path.relpath(os.path.join(dirpath, f), VAULT)
        by_rel[rel] = True
        stems.add(f); stems.add(os.path.splitext(f)[0])

def resolves(target):
    t = target.strip()
    if t in by_rel or t + ".md" in by_rel: return True
    b = os.path.basename(t)
    return b in stems or os.path.splitext(b)[0] in stems

broken = Counter()
files_changed = 0
def repl(m):
    target, heading, alias = m.group(1), m.group(2), m.group(3)
    target = target.rstrip("\\")  # table rows escape the alias pipe as \|
    if resolves(target): return m.group(0)
    broken[target.strip()] += 1
    if alias is not None: return alias
    text = os.path.splitext(os.path.basename(target.strip()))[0]
    return text + (" " + heading[1:].strip() if heading and heading[1:].strip() else "")

for dirpath, dirs, files in os.walk(VAULT):
    dirs[:] = [d for d in dirs if not d.startswith(".")]
    for f in files:
        if not f.endswith(".md"): continue
        p = os.path.join(dirpath, f)
        with open(p, encoding="utf-8") as fh: text = fh.read()
        new = LINK_RE.sub(repl, text)
        if new != text:
            files_changed += 1
            with open(p, "w", encoding="utf-8") as fh: fh.write(new)

print(f"files changed: {files_changed}; links unlinked: {sum(broken.values())}; distinct targets: {len(broken)}")
for t, n in broken.most_common(): print(f"  {n:3d}  {t}")
