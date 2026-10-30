import os, re, shutil, sys
from collections import defaultdict, deque

SRC = "/Users/nathanaday/Vaults/USC-Fall-2026"
DST = "/Users/nathanaday/projects/usc/cs566-course/Midterm-Wiki"
SEEDS = ["Block 1 Slides", "Block 2 Slides", "Block 3 Slides", "Block 4 Slides",
         "Block 5 Slides", "Block 6 Slides", "Block 6 Slides Extended", "Block 7 Slides", "F26-midterm-review-234p"]
COPY_ROOTS = ["wiki/sources", "wiki/topics", "internal/wiki/originals"]
EXCLUDE_TAGS = ("cs566-project", "cs513-acps", "autonomous-driving")
EXCLUDE_STEMS = {"Bayesian Optimization", "Sim-to-Real Transfer", "KL Divergence", "1x1 Convolution", "Differentiable vs Non-Differentiable Reinforcement Learning", "CS513-ACPS", "CS513-Project", "Autonomous Driving", "CS566-project", "Depth Anything V2", "Yue Zhao"}
LINK_RE = re.compile(r"!?\[\[([^\]\|#]+)(?:#[^\]\|]*)?(?:\|[^\]]*)?\]\]")
TAGS_RE = re.compile(r"^tags:\s*\[(.*?)\]", re.M)

# index: relative path -> full path; stem -> [relative paths]
by_rel, by_stem = {}, defaultdict(list)
for root in COPY_ROOTS:
    for dirpath, _, files in os.walk(os.path.join(SRC, root)):
        for f in files:
            if f.startswith("."): continue
            rel = os.path.relpath(os.path.join(dirpath, f), SRC)
            by_rel[rel] = os.path.join(SRC, f)
            by_stem[os.path.splitext(f)[0]].append(rel)
            by_stem[f].append(rel)  # also allow full filename (e.g. foo.pdf)

def frontmatter_tags(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        head = fh.read(6000)
    if not head.startswith("---"): return []
    fm = head.split("\n---", 1)[0].split("\n")
    tags = []
    for i, line in enumerate(fm):
        if not line.startswith("tags:"): continue
        rest = line[5:].strip()
        if rest.startswith("["):
            tags += [t.strip().strip('"') for t in rest.strip("[]").split(",") if t.strip()]
        else:
            for nxt in fm[i+1:]:
                if nxt.startswith("  - ") or nxt.startswith("- "): tags.append(nxt.split("-", 1)[1].strip().strip('"'))
                else: break
        break
    return tags

SRC_RE = re.compile(r"^sources:\s*\[(.*)\]", re.M)
EXCLUDE_ONLY_SOURCES = {"Block 8 Slides"}
def only_excluded_sources(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        head = fh.read(6000)
    if not head.startswith("---"): return False
    fm = head.split("\n---", 1)[0].split("\n")
    raw = []
    for i, line in enumerate(fm):
        if not line.startswith("sources:"): continue
        rest = line[8:].strip()
        if rest.startswith("["): raw = [x for x in rest.strip("[]").split(",") if x.strip()]
        else:
            for nxt in fm[i+1:]:
                if nxt.lstrip().startswith("- "): raw.append(nxt.split("-", 1)[1])
                else: break
        break
    srcs = {x.strip().strip('"').strip("[]").split("|")[0] for x in raw}
    return bool(srcs) and srcs <= EXCLUDE_ONLY_SOURCES

def resolve(target):
    target = target.strip()
    for cand in (target, target + ".md"):
        if cand in by_rel: return cand
    stem = os.path.basename(target)
    hits = by_stem.get(stem) or by_stem.get(os.path.splitext(stem)[0])
    if hits:
        if len(hits) > 1: ambiguous[target] = hits
        return hits[0]
    return None

ambiguous = {}
queue = deque()
for s in SEEDS:
    rel = resolve(s)
    if rel is None: sys.exit(f"seed not found: {s}")
    queue.append((rel, "<seed>"))

copied, excluded, unresolved, skipped_sources = {}, defaultdict(set), defaultdict(set), defaultdict(set)
SEED_RELS = {resolve(x) for x in SEEDS}
seen = set()
while queue:
    rel, via = queue.popleft()
    if rel in seen: continue
    seen.add(rel)
    full = os.path.join(SRC, rel)
    if rel.startswith("wiki/sources/") and rel not in SEED_RELS:
        skipped_sources[rel].add(via); continue
    stem = os.path.splitext(os.path.basename(rel))[0]
    if rel.endswith(".md") and (stem in EXCLUDE_STEMS or (rel.startswith("wiki/topics/") and only_excluded_sources(full)) or any(x in t for x in EXCLUDE_TAGS for t in frontmatter_tags(full))):
        excluded[rel].add(via); continue
    copied[rel] = via
    if not rel.endswith(".md"): continue
    with open(full, encoding="utf-8", errors="replace") as fh:
        text = fh.read()
    for m in LINK_RE.finditer(text):
        t = m.group(1)
        r = resolve(t)
        if r is None: unresolved[t].add(rel)
        else: queue.append((r, rel))

for rel in copied:
    dst = os.path.join(DST, rel)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copy2(os.path.join(SRC, rel), dst)

def bucket(rel): return rel.split("/")[0] + "/" + rel.split("/")[1] if rel.startswith("wiki") else "originals"
counts = defaultdict(int)
for rel in copied: counts[bucket(rel)] += 1
print("COPIED:", dict(counts), "total", len(copied))
print("\nEXCLUDED (tags/bridges), linked from:")
for rel in sorted(excluded): print(f"  {os.path.basename(rel)}  <- {', '.join(sorted(os.path.basename(v) for v in excluded[rel]))}")
print("\nSOURCES NOT COPIED (non-seed), linked from:")
for rel in sorted(skipped_sources): print(f"  {os.path.basename(rel)}  <- {', '.join(sorted(os.path.basename(v) for v in skipped_sources[rel]))}")
print("\nUNRESOLVED link targets (not under wiki/ or originals), linked from:")
for t in sorted(unresolved): print(f"  [[{t}]]  <- {', '.join(sorted(os.path.basename(v) for v in unresolved[t]))}")
if ambiguous:
    print("\nAMBIGUOUS basenames:")
    for t, h in ambiguous.items(): print(f"  {t}: {h}")
