---
name: export-cheatsheet
description: Export the curated cheatsheet PDF from the pages on the Topic Map canvas. Use when the user says export the cheatsheet, export cheatsheet PDF, build the cheatsheet, print the cheatsheet, or regenerate the index page numbers.
---

# Export the Cheatsheet

Run the exporter from the vault root and report the result:

```
python3 tools/export_cheatsheet.py
```

It reads `cheatsheet/Topic Map.canvas`, strips each page down to its title and content sections, writes the cleaned Markdown and `cheatsheet.pdf` to `../Midterm-Cheatsheet/`, and rewrites `cheatsheet/Cheatsheet Index.md` with the page numbers from the PDF.

Options worth offering when the user asks for a shorter or larger print:

- `--flow` lets articles share pages instead of starting each one on a new page.
- `--font-size 8pt` or `10pt` changes the body size (9pt is the default).
- `--margin 0.4in` narrows the margins (0.5in is the default).
- `--out DIR` changes the output directory.

After it runs, tell the user the PDF path, the total page count from the script's output, and any glyph warning it prints. If pandoc or tectonic is missing, the script says which one; both install with Homebrew.
