# Page forms

Every topic and source is a note in the wiki folders. The file name is the title. Links are the identity of notes, so write `[[Title]]` and never an id.

## Topic

A topic is one subject. Its properties:

```yaml
type: topic
description: One sentence on what the subject is. Search finds the topic by it.
tags: [ml/self-supervised, vision]
aliases: [SSL]
sources: ["[[wiki/sources/DINOv2|DINOv2]]"]
status: draft          # draft | stable | contested | deprecated
kind: concept          # concept (an idea) | entity (a named thing) | overview (the page of a tag)
```

Sections, in order: `## Definition` or `## What it is` (two or three sentences), `## Explanation` or `## Facts`, `## Related` (links, each with a few words on how it relates), `## Sources` (each cited source, one line on what it gives), `## Notes` (the user's; never change it).

- Every claim names its source: `… trains on 142M images ([[DINOv2]], p. 3)`.
- `status`: `draft` when thin; `stable` when complete for what its sources say; `contested` when sources disagree and the topic shows both; `deprecated` when the subject is gone, with a link to what replaced it.
- A topic takes the tags of the sources it came from, and more when the subject reaches further. Prefer a tag that exists; `wiki_tags` lists them.

## Source

A source note stands for one captured original. Capture copies the file into `internal/wiki/originals/`, named by its content hash, and writes the source note `<name> (source).md` with `type: source`, `status: pending`, `file` (the frozen copy, which the note embeds), `from` (where the file was captured from), and `sha256`. For a file that a reader cannot open, such as a `.pptx` or a `.docx`, capture also writes its text beside the copy, which `text` links and the note embeds in place of the copy. Read and cite the copy, or its text: the file in `from` can change later, and the copy is what the source says. The ingest sets the rest, in a modify:

```yaml
description: One sentence on what the original is.
tags: [paper, vision]
authority: secondary   # official | primary | secondary | community | synthetic | unknown
status: absorbed       # when every claim worth keeping is in the topics
```

Body: the embed of the copy or its text, then `## Summary` (what it says, a paragraph or two), `## Structure` (one line per part, linking the topics that grew from it), `## Notes` (the user's). Cite a source by its note, `[[Dart Manipulation Tutorials (source)]]`, never by the file it came from.

Never change the copy that a source embeds, or the file it came from.
