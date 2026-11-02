---
name: ingest
description: "Absorb the sources of an ingest session into cited topics through one change plan that a person approves: chunk, extract, match, draft, propose. To ingest files from a conversation, call wiki_ingest, which starts an ingest session."
---
# Ingest

**In a conversation**, with no ingest session, do not ingest the files yourself. Call `wiki_ingest` with the files or the folder that the user names, as vault paths or absolute paths: it captures them as sources and starts an ingest session, which runs this skill. Tell the user the session's name, and that they approve its change in Obsidian when it is proposed. Then end.

**In an ingest session**, the session's `sources` property links the source notes to absorb. You cannot write under `wiki/topics/` or `wiki/sources/` yourself: the session is read-only, and every change to the wiki goes through `wiki_change` as one plan. Work map-reduce, so a long document or many documents cost the same care as one.

Two agents of the session do the reading and the drafting, each in a fresh context: `extractor` reads one chunk, and `drafter` drafts the writes of one slice. Run each with `yami_agent`; calls in one turn run at the same time. An agent knows only its brief and your task, so give it everything in the task. `page-forms.md`, in this skill's folder `internal/wiki/skills/ingest/`, gives the properties and the sections of a topic and a source: read it before you assemble the plan.

1. **Chunks.** Call `wiki_chunks` for each source. It names the file to read and its chunks: line ranges, page ranges, or the whole file. Call `wiki_tags` once for the tag list.
2. **Extract.** For each chunk, call `yami_agent` with the agent `extractor`, in waves of at most eight, also when you could read the chunk yourself: each worker reads with a fresh context, so the last chunk gets the care of the first. Only when the sources hold one chunk in all, extract it yourself from the extractor's brief, `internal/wiki/agents/extractor/AGENT.md`. The task gives the source note's path, the file and the range from `wiki_chunks`, the source's tags, and the tag list. Each returns an Item Map. A `partial` chunk goes again, narrower.
3. **Match.** Call `wiki_match` with every subject's name at once, aliases included, so a subject named in three chunks is one subject.
4. **Slice.** Put every subject that hits or nears one topic into the same slice, so two drafters never write one topic. At most eight subjects per slice.
5. **Draft.** For each slice, call `yami_agent` with the agent `drafter`. The task gives the slice (each subject with its items and its match), the source notes, their tags, and the tag list. Each returns writes. With one or two slices, draft them yourself from the drafter's brief, `internal/wiki/agents/drafter/AGENT.md`.
6. **Assemble.** One plan for `wiki_change`: every drafted write, plus a modify of each source with its `description`, `tags`, `authority`, `## Summary`, `## Structure` (one line per part, linking the topics that grew from it), and `status: absorbed`. Give the plan a short `title` ("Ingest the DINOv2 paper"), `notes` (what it does, the coverage, each skipped subject with its reason), and `session` (this session document's path). Past 25 new topics, keep the ones with the most claims and list the rest in the notes.
7. **Propose.** Call `wiki_change`. It validates the plan, writes it as a change document that waits for a person's approval, and links the change from this session. Nothing in the wiki changes until a person approves it in Obsidian. When the tool refuses, fix the writes it names and call it again. When it returns warnings, links to no note, fix those writes and propose the plan again; the person approves the last proposal and rejects the rest.
8. **End.** Your work ends when the plan is proposed and covers every source. Do not wait for the approval, and do not lint the wiki for the plan's effect: the wiki holds it only after the approval. When a change of this session was rejected, the session's feedback holds the reason: read it, and propose a new plan that answers it.

One plan holds at most 100 writes, about ten sources, or forty chunks. More is several plans, one after another.
