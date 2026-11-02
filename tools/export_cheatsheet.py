#!/usr/bin/env python3
"""Export the pages on the Topic Map canvas as one printable cheatsheet PDF.

Usage:
    python3 tools/export_cheatsheet.py [--out DIR] [--flow] [--font-size 9pt] [--margin 0.5in]

Needs pandoc, tectonic, and PyYAML. The reading order comes from the canvas:
each text node is a section header, and its edges lead to the pages under it.
"""

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

import yaml

VAULT = Path(__file__).resolve().parent.parent
CANVAS = VAULT / "cheatsheet" / "Topic Map.canvas"
VAULT_INDEX = VAULT / "cheatsheet" / "Cheatsheet Index.md"
DEFAULT_OUT = VAULT.parent / "Midterm-Cheatsheet"
TITLE = "CSCI 566 Midterm Cheatsheet"

IMAGE_EXT = {".png", ".jpg", ".jpeg", ".gif", ".pdf", ".svg", ".avif", ".webp"}
WIKILINK = re.compile(r"(!?)\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|([^\]]*))?\]\]")
CALLOUT_HEAD = re.compile(r"^>\s*\[!(\w+)\]\s*(.*)$")
CALLOUT_COLORS = {"warning": "orange", "danger": "red", "tip": "green", "note": "blue", "info": "blue"}
LATEX_ESCAPES = {
    "\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#",
    "_": r"\_", "{": r"\{", "}": r"\}", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}",
}
TEXT_SYMBOLS = {"✓": r"$\checkmark$", "✗": r"$\times$"}

HEADER_TEX = r"""
\usepackage{fancyhdr}
\usepackage{titlesec}
\usepackage{multicol}
\usepackage{tocloft}
\setlength{\cftbeforepartskip}{3pt}
\setlength{\cftbeforesecskip}{0pt}
\renewcommand{\cftpartfont}{\bfseries}
\renewcommand{\cftsecfont}{\normalfont}
\renewcommand{\cftsecpagefont}{\normalfont}
\usepackage{xcolor}
\usepackage[many]{tcolorbox}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small\nouppercase{\leftmark}}
\fancyhead[R]{\small\thepage}
\renewcommand{\headrulewidth}{0.3pt}
\setlength{\headheight}{12pt}
\setlength{\parindent}{0pt}
\setlength{\parskip}{3pt plus 1pt}
\titleformat*{\section}{\LARGE\bfseries}
\titleformat*{\subsection}{\large\bfseries}
\titleformat*{\subsubsection}{\normalsize\bfseries}
\titlespacing*{\section}{0pt}{4pt}{4pt}
\titlespacing*{\subsection}{0pt}{8pt}{2pt}
\titlespacing*{\subsubsection}{0pt}{6pt}{1pt}
\AtBeginDocument{%
  \setlength{\abovedisplayskip}{4pt}\setlength{\belowdisplayskip}{4pt}%
  \setlength{\abovedisplayshortskip}{2pt}\setlength{\belowdisplayshortskip}{2pt}}
\newtcolorbox{callout}[2]{enhanced, breakable, colback=#1!6!white, colframe=#1!60!black,
  title=#2, fonttitle=\bfseries\small, left=4pt, right=4pt, top=2pt, bottom=2pt,
  boxrule=0.5pt, arc=2pt, before skip=4pt, after skip=4pt}
\newcommand{\cheatsection}[1]{\clearpage\phantomsection\addcontentsline{toc}{part}{#1}%
  {\noindent\color{gray}\large\bfseries #1\par}\vspace{2pt}}
\newcommand{\cheatletter}[1]{\vspace{3pt}\noindent{\bfseries\color{gray}#1}\par\nobreak\vspace{1pt}}
\newcommand{\cheatentry}[3]{\noindent\hangindent=1em\hangafter=1 #1\ \dotfill\ {\footnotesize\textit{#2}}~\textbf{\pageref{#3}}\par}
"""


def die(msg):
    sys.exit(f"export_cheatsheet: {msg}")


def read_canvas():
    """Return [(section_label, [page_path, ...]), ...] in canvas reading order."""
    canvas = json.loads(CANVAS.read_text())
    nodes = {n["id"]: n for n in canvas["nodes"]}
    children = {}
    for e in canvas.get("edges", []):
        children.setdefault(e["fromNode"], []).append(e["toNode"])
    for kids in children.values():
        kids.sort(key=lambda i: (nodes[i]["y"], nodes[i]["x"]))

    def walk(node_id, seen, out):
        for kid in children.get(node_id, []):
            if kid in seen:
                continue
            seen.add(kid)
            if nodes[kid]["type"] == "file":
                out.append(VAULT / nodes[kid]["file"])
            walk(kid, seen, out)

    seen, sections = set(), []
    headers = sorted((n for n in nodes.values() if n["type"] == "text"), key=lambda n: (n["y"], n["x"]))
    for h in headers:
        label = h["text"].strip().lstrip("#").strip()
        pages = []
        walk(h["id"], seen, pages)
        if pages:
            sections.append((label, pages))
    leftover = [VAULT / n["file"] for n in sorted(nodes.values(), key=lambda n: (n["y"], n["x"]))
                if n["type"] == "file" and n["id"] not in seen]
    if leftover:
        sections.append(("Other", leftover))
    return sections


def find_attachments():
    found = {}
    for p in VAULT.rglob("*"):
        if p.suffix.lower() in IMAGE_EXT and not any(part.startswith(".") for part in p.parts):
            found.setdefault(p.name, p)
    return found


def split_frontmatter(text):
    if not text.startswith("---"):
        return {}, text
    _, fm, body = text.split("---", 2)
    return yaml.safe_load(fm) or {}, body


def drop_sections(lines, names=("Related", "Sources")):
    out, skipping = [], False
    for line in lines:
        if re.match(r"^#{1,2} ", line):
            skipping = line.lstrip("# ").strip() in names
        if not skipping:
            out.append(line)
    return out


def convert_callouts(lines):
    out, i = [], 0
    while i < len(lines):
        m = CALLOUT_HEAD.match(lines[i])
        if not m:
            out.append(lines[i])
            i += 1
            continue
        kind = m.group(1).lower()
        title = m.group(2).strip() or kind.capitalize()
        body = []
        i += 1
        while i < len(lines) and lines[i].startswith(">"):
            body.append(re.sub(r"^>\s?", "", lines[i]))
            i += 1
        color = CALLOUT_COLORS.get(kind, "gray")
        out += ["", "```{=latex}", f"\\begin{{callout}}{{{color}}}{{{escape_latex(title)}}}", "```", ""]
        out += body
        out += ["", "```{=latex}", "\\end{callout}", "```", ""]
    return out


def convert_links(text, attachments):
    def repl(m):
        embed, target, alias = m.group(1), m.group(2).strip(), m.group(3)
        if embed:
            path = attachments.get(target)
            return f"![]({path}){{width=60%}}" if path else ""
        return alias if alias else target
    return WIKILINK.sub(repl, text)


def escape_latex(s):
    return "".join(LATEX_ESCAPES.get(ch, ch) for ch in s)


def clean_page(path, attachments):
    """Return (title, aliases, cleaned markdown without the H1)."""
    meta, body = split_frontmatter(path.read_text())
    lines = drop_sections(body.strip("\n").split("\n"))
    lines = convert_callouts(lines)
    text = convert_links("\n".join(lines), attachments)
    for sym, tex in TEXT_SYMBOLS.items():
        text = text.replace(sym, tex)
    return path.stem, list(meta.get("aliases") or []), text.strip() + "\n"


def index_entries(pages):
    """[(sort_key, term, topic, label, is_title)] sorted alphabetically."""
    entries = []
    for n, (title, aliases, _) in enumerate(pages):
        entries.append((title, title, f"art:{n}", True))
        for a in aliases:
            entries.append((str(a), title, f"art:{n}", False))
    return sorted(entries, key=lambda e: sort_key(e[0]))


def sort_key(term):
    return term.lower().lstrip(" -")


def index_latex(entries):
    out = ["```{=latex}", "\\phantomsection\\addcontentsline{toc}{section}{Index}",
           "\\section*{Index}\\markboth{Index}{Index}", "\\begin{multicols}{2}\\small"]
    letter = None
    for term, topic, label, is_title in entries:
        first = sort_key(term)[:1].upper()
        first = "#" if first.isdigit() else first
        if first != letter:
            letter = first
            out.append(f"\\cheatletter{{{escape_latex(letter)}}}")
        t = escape_latex(term)
        if is_title:
            t = f"\\textbf{{{t}}}"
        out.append(f"\\cheatentry{{{t}}}{{{escape_latex(topic)}}}{{{label}}}")
    out += ["\\end{multicols}", "```", ""]
    return "\n".join(out)


def build_markdown(sections, pages, flow):
    parts = ["```{=latex}", "\\thispagestyle{empty}", "```", "", index_latex(index_entries(pages))]
    n = 0
    for label, paths in sections:
        parts.append(f"```{{=latex}}\n\\cheatsection{{{escape_latex(label)}}}\n```\n")
        for k, _ in enumerate(paths):
            title, _, text = pages[n]
            if k > 0 and not flow:
                parts.append("```{=latex}\n\\clearpage\n```\n")
            parts.append(f"# {title}\n\n\\label{{art:{n}}}\n\n{text}\n")
            n += 1
    return "\n".join(parts)


def read_pages_from_aux(aux_path, count):
    pages = {}
    for m in re.finditer(r"\\newlabel\{art:(\d+)\}\{\{[^}]*\}\{(\d+)\}", aux_path.read_text(errors="replace")):
        pages[int(m.group(1))] = int(m.group(2))
    return [pages.get(i) for i in range(count)]


def write_vault_index(entries, page_numbers, labels_to_n):
    lines = [
        "---",
        "description: Alphabetical lookup of every term on the printed cheatsheet, with the topic page that covers it. Regenerated by tools/export_cheatsheet.py.",
        "---", "",
        "> Every title and alias from the pages in [[Topic Map.canvas|Topic Map]], one row per term. Bold rows are page titles. Page numbers match the last PDF export.",
        "", "| Term | Topic | Page |", "| --- | --- | --- |",
    ]
    for term, topic, label, is_title in entries:
        page = page_numbers[labels_to_n[label]]
        t = f"**{term}**" if is_title else term
        lines.append(f"| {t} | [[{topic}]] | {page if page else ''} |")
    VAULT_INDEX.write_text("\n".join(lines) + "\n")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT, help=f"output directory (default {DEFAULT_OUT})")
    ap.add_argument("--flow", action="store_true", help="let articles share pages instead of starting each on a new page")
    ap.add_argument("--font-size", default="9pt", help="8pt, 9pt, 10pt, ... (default 9pt)")
    ap.add_argument("--margin", default="0.5in", help="page margin (default 0.5in)")
    ap.add_argument("--paper", default="letterpaper", help="letterpaper or a4paper")
    args = ap.parse_args()

    for tool in ("pandoc", "tectonic"):
        if not shutil.which(tool):
            die(f"{tool} is not installed (brew install {tool})")

    out = args.out
    md_dir = out / "markdown"
    md_dir.mkdir(parents=True, exist_ok=True)
    for old in md_dir.glob("*.md"):
        old.unlink()

    attachments = find_attachments()
    sections = read_canvas()
    pages = []
    for _, paths in sections:
        for p in paths:
            title, aliases, text = clean_page(p, attachments)
            pages.append((title, aliases, text))
            (md_dir / f"{len(pages):02d} {title}.md").write_text(f"# {title}\n\n{text}")

    combined = build_markdown(sections, pages, args.flow)
    (out / "cheatsheet.md").write_text(combined)
    (out / "header.tex").write_text(HEADER_TEX)

    tex = out / "cheatsheet.tex"
    subprocess.run([
        "pandoc", str(out / "cheatsheet.md"), "-f", "markdown+raw_tex", "-t", "latex", "-s", "-o", str(tex),
        "--toc", "--toc-depth=1", "-H", str(out / "header.tex"),
        "-V", "documentclass=extarticle", "-V", f"fontsize={args.font_size}",
        "-V", f"geometry:margin={args.margin}", "-V", f"geometry:paper={args.paper}",
        "-V", f"title={TITLE}", "-V", "toc-title=Contents", "-V", "colorlinks=false",
    ], check=True)
    # pandoc's \maketitle wastes a page, and a one-column contents list spills over one
    src = tex.read_text()
    src = src.replace("\\maketitle\n", "{\\LARGE\\bfseries " + TITLE + "\\par}\\vspace{4pt}\n")
    src = src.replace("\\tableofcontents\n", "\\begin{multicols}{2}\\tableofcontents\\end{multicols}\n")
    tex.write_text(src)

    res = subprocess.run(["tectonic", "--keep-intermediates", "--keep-logs", "--outdir", str(out), str(tex)],
                         capture_output=True, text=True)
    if res.returncode != 0:
        sys.stderr.write(res.stdout[-3000:] + res.stderr[-3000:])
        die(f"tectonic failed; see {out / 'cheatsheet.log'}")

    page_numbers = read_pages_from_aux(out / "cheatsheet.aux", len(pages))
    entries = index_entries(pages)
    write_vault_index(entries, page_numbers, {f"art:{n}": n for n in range(len(pages))})

    missing = [m.group(1) for m in re.finditer(r"Missing character: There is no (\S+)", (out / "cheatsheet.log").read_text(errors="replace"))]
    print(f"wrote {out / 'cheatsheet.pdf'}")
    print(f"{len(pages)} articles; last article starts on page {max(p for p in page_numbers if p)}")
    for (title, _, _), p in zip(pages, page_numbers):
        print(f"  p.{p:>3}  {title}")
    if missing:
        print(f"warning: glyphs missing from the font: {sorted(set(missing))}")


if __name__ == "__main__":
    main()
