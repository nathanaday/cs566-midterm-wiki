---
id: con-jpz8dh
type: topic
kind: concept
description: A sequence model that stacks mostly fixed-state recurrent layers and adds an attention layer at intervals, so it keeps bounded memory but can still look up past tokens directly.
tags: [machine-learning/cs566-deeplearning]
aliases: [Hybrid Layers, Hybrid Recurrent-Attention Architecture, Periodic Attention, HYB]
created: 2026-09-28T00:00:00
updated: 2026-10-13T18:22:47
refreshed: 2026-10-13T18:22:47
status: stable
sources: ["[[Block 5 Slides]]"]
up: ["[[Recurrent Neural Networks (RNN)]]"]
---

> [!concept] Concept
> 1 source · refreshed 2026-10-13 · #machine-learning/cs566-deeplearning
> Up: [[Recurrent Neural Networks (RNN)]]

## Definition

A hybrid model combines "fixed-state layers plus periodic direct access" ([[Block 5 Slides]], p. 228). Most layers carry a recurrent state of fixed width. Some layers use attention, which reads past tokens directly.

The deck's 8-layer example, along the depth of the model (p. 229):

`STATE, STATE, STATE, ATTN, STATE, STATE, STATE, ATTN`

The state layers give "bounded recurrent memory". The attention layers give "periodic token lookup" (p. 229).

## Explanation

On the compress-or-re-read spectrum, the hybrid sits between the RNN and SSM (constant-size decode state) and attention (direct access to more tokens). The deck labels it "periodic attention access" ([[Block 5 Slides]], p. 227). See [[Recurrent State vs Growing Context]].

"Hybrids spend direct-access capacity selectively" (p. 229). The deck sums up the hybrid path as "mostly state + selective attention" (p. 230).

The deck names two hybrid models, with one line each (p. 228):

- **Qwen3-Next:** "3:1 mix".
- **Kimi Linear:** "KDA + MLA".

The deck does not expand KDA or MLA. It warns that "benchmark claims remain source-specific" (p. 228).

Synthesis, not from the deck: the 8-layer example has three state layers for each attention layer (p. 229), which matches the "3:1" label on Qwen3-Next. The deck does not say that the two describe the same layout.

## Related

- [[Recurrent State vs Growing Context]]: the spectrum and the other design path, stronger recurrence
- [[KV Cache]]: what the attention layers store
- [[Transformers]]
- [[Recurrent Neural Networks (RNN)]]
- [[Long Short-Term Memory]]

## Sources

- [[Block 5 Slides]], pp. 227–230
