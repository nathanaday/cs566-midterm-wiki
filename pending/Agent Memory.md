---
id: con-ejx8d9
type: topic
kind: concept
description: Agent memory stores information outside the model and retrieves it into context when needed, so the agent's behavior changes while the weights stay fixed.
tags:
  - machine-learning/cs566-deeplearning
aliases:
  - LLM Agent Memory
created: 2026-09-28T00:00:00
updated: 2026-10-13T18:22:42
refreshed: 2026-10-13T18:22:42
status: stable
sources:
  - "[[Block 3 Slides]]"
  - "[[Block 1 Slides]]"
  - "Sep 14 Lecture Account"
up:
  - "[[Agent Loop]]"
---

> [!concept] Concept
> 3 sources · refreshed 2026-10-13 · #machine-learning/cs566-deeplearning
> Up: [[Agent Loop]]

## Definition

Agent memory stores information outside the model and puts it back into context when the agent needs it. The weights do not change. "An Agent Can Remember Without Training" ([[Block 3 Slides]], p. 221). The Sep 14 lecture listed it as one of four ways to update an LLM (Sep 14 Lecture Account, § Updating LLMs); see [[Updating LLMs]].

## Explanation

### The course example

[[Block 3 Slides]] gives an example (pp. 221–223):

1. A fixed model $\theta$ reads a tool result, "length: 200 cm", and answers "200 m?".
2. A user correction is saved as a memory record: "Tool returns cm. Divide by 100 for m." The slide asks: "A file was written. Did any weight receive a gradient?" (p. 221).
3. On the next attempt, the record is retrieved into context and the same model answers "2 m". "Context changed; θ did not" (p. 222).
4. "This memory example keeps θ fixed" (p. 223).

The slide on p. 223 compares what changes in three cases:

| Method | What changes | What stays fixed |
| --- | --- | --- |
| Memory (this example) | context tokens | θ |
| [[LoRA]] | adapter A, B | base W |
| [[Test-Time Training]] | selected weights, θ → θ' | the rest |

The agent core in the [[Agent Loop]] is memory plus the model, and the two interact in both directions ([[Block 1 Slides]], p. 90, after Dawn Song, UC Berkeley "Agentic AI", Fall 2025).

### General background

Synthesis (general background; no course source in the vault states it):

- **Write:** the agent saves facts, results, or user preferences to a store, such as files, a database, or a vector index.
- **Read:** on a later turn or session, a retrieval step finds the matching entries and adds them to the context.
- Short-term memory is the current context. Long-term memory is the external store.

### Costs and limits

Synthesis: agent memory has the low cost of [[In-Context Learning]] and adds persistence. The slide puts it with context tokens, where θ stays fixed ([[Block 3 Slides]], p. 223).

- Each read still uses part of the finite request context ([[Agent Skills]]; [[Block 1 Slides]], p. 94).
- A wrong entry stays wrong until the agent or a person edits it.

## Related

- [[Updating LLMs]]
- [[Agent Loop]]: memory is half of the agent core
- [[In-Context Learning]]
- [[LoRA]]
- [[Test-Time Training]]
- [[Agent Skills]]

## Sources

- [[Block 3 Slides]], pp. 221–223
- [[Block 1 Slides]], p. 90 (memory in the agent core) and p. 94 (context budget)
- Sep 14 Lecture Account, § Updating LLMs
