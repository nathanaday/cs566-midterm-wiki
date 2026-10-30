"""Reduce every page's frontmatter to the reader-facing keys."""
import os, re, sys, json
VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KEEP = {"topics": ["description", "aliases", "sources"], "sources": ["description", "aliases"]}
SAVED = {}  # per file, the dropped keys we still need later (sources metadata)

def parse(fm):
    out, cur = {}, None
    for line in fm.split("\n"):
        m = re.match(r"^([A-Za-z_]+):(.*)$", line)
        if m:
            cur = m.group(1); out[cur] = m.group(2).strip()
        elif cur and re.match(r"^\s+- ", line):
            out[cur] = out[cur] + "\n" + line
    return out

for kind, keep in KEEP.items():
    d = os.path.join(VAULT, "wiki", kind)
    for f in sorted(os.listdir(d)):
        if not f.endswith(".md"): continue
        p = os.path.join(d, f); t = open(p, encoding="utf-8").read()
        if not t.startswith("---\n"): continue
        fm, body = t[4:].split("\n---\n", 1)
        props = parse(fm)
        SAVED[f] = {k: v for k, v in props.items() if k not in keep}
        lines = []
        for k in keep:
            if k in props and props[k] not in ("", "[]"):
                v = props[k]
                lines.append(f"{k}:{v}" if v.startswith("\n") else f"{k}: {v}")
        new = "---\n" + "\n".join(lines) + "\n---\n" + body
        open(p, "w", encoding="utf-8").write(new)
json.dump(SAVED, open(os.path.join(VAULT, "tools", "dropped_frontmatter.json"), "w"), indent=1)
print("rewrote", sum(1 for _ in SAVED), "pages; dropped keys saved to tools/dropped_frontmatter.json")
