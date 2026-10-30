---
id: doc-jd0qbn
type: topic
kind: concept
description: "Retrieval-augmented generation (RAG) answers a question in two steps: a retrieval step finds the relevant document passages, and an LLM reads them and writes the answer, so the answer can only be as complete as the retrieved evidence."
tags: [machine-learning/cs566-deeplearning]
aliases: [RAG, Retrieval augmented generation]
created: 2026-10-05T17:31:20
updated: 2026-10-13T18:22:42
refreshed: 2026-10-13T18:22:42
status: stable
sources: ["[[Block 6 Slides Extended]]"]
up: ["[[Large Language Models]]"]
---

> [!concept] Concept
> 1 source · refreshed 2026-10-13 · #machine-learning/cs566-deeplearning
> Up: [[Large Language Models]]

## Definition

"RAG means retrieval-augmented generation. Retrieval supplies relevant evidence" ([[Block 6 Slides Extended]], p. 136). The flow has three parts: a user question, a step that finds the relevant document passages, and an LLM that reads the passages and writes an answer. "The LLM answers using the documents that were retrieved" (p. 136).

## Explanation

### The task

CSCI 566 uses RAG for document question answering. The input is a question and documents. The output is an answer with sources ([[Block 6 Slides Extended]], p. 126).

### When the facts are spread across documents

The deck's example asks which apps could be affected if a fictional database named Atlas goes offline. This Atlas is unrelated to the Atlas tool that manages this vault. One document says that the Beacon service uses data from the Atlas database. Other documents say which apps use Beacon ([[Block 6 Slides Extended]], pp. 135–137). "We now need supporting facts spread across documents" (p. 135).

Suppose the first search returns only the document that mentions "Atlas", D1: "Beacon uses data from the Atlas database." D1 shows that Beacon depends on Atlas. It does not show which apps depend on Beacon, so the system needs more documents. "D1 identifies Beacon, but the app names are in D2 and D3" ([[Block 6 Slides Extended]], p. 138).

[[GraphRAG]] addresses this gap. It builds a graph of sourced relations before any question, then follows the graph from the named entity to collect all the needed passages (p. 139).

### Retrieval errors and generation errors

An incomplete answer can come from retrieval or from generation. If the retrieved context lacks a needed passage, look at retrieval. If the context holds every needed passage and the answer still omits a fact, look at the LLM's generation. "Inspect the retrieved passages before blaming the LLM" ([[Block 6 Slides Extended]], p. 152).

Synthesis: the deck shows this test on its graph version, but the test needs nothing from the graph. It applies to any RAG system, because every RAG system has a retrieval stage and a generation stage that can fail on their own.

### Elsewhere in the wiki

Synthesis: RAG changes what the model knows through its input alone, so it is a form of [[In-Context Learning]] in which a retrieval step chooses the context. [[k-Nearest Neighbors]] covers RAG as a nearest-neighbor lookup from the Block 2 deck, which compares RAG with kNN-LM and with long context.

## Related

- [[GraphRAG]]: RAG with a graph of sourced relations as the index
- [[k-Nearest Neighbors]]: retrieval as nearest-neighbor search
- [[In-Context Learning]]: retrieved text enters the input and the weights stay fixed
- [[Agent Memory]]: stored records retrieved into context
- [[Question Answering]]: the task
- [[LLMs and Graphs]]: the deck section that introduces RAG

## Sources

- [[Block 6 Slides Extended]], pp. 126, 135–139, 152
