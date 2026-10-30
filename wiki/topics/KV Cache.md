---
id: con-m41r0r
type: topic
kind: concept
description: A Transformer stores the keys and values of past tokens during generation, so each decode step computes only the new token's key and value.
tags: [machine-learning/cs566-deeplearning]
aliases: [Key-Value Cache, KV Caching, Per-layer KV cache]
created: 2026-09-28T00:00:00
updated: 2026-10-13T18:22:42
refreshed: 2026-10-13T18:22:42
status: stable
sources: ["[[Block 3 Slides]]", "[[Block 5 Slides]]"]
up: ["[[Autoregressive Language Modeling]]"]
---

> [!concept] Concept
> 2 sources · refreshed 2026-10-13 · #machine-learning/cs566-deeplearning
> Up: [[Autoregressive Language Modeling]]

## Definition

A Transformer generates text in two stages ([[Block 3 Slides]], pp. 56–58, citing the Hugging Face Transformers caching documentation):

- **Prefill:** the model processes the whole prompt and computes a key (K) and a value (V) for each prompt token (p. 56).
- **Decode:** the model computes the new position, then appends its K and V. It reuses the cached K and V of all earlier positions (p. 57).

Example: after the prefill of "The light is", the cache holds $K_1..K_3$ and $V_1..V_3$. Generating "red" adds $K_4, V_4$. Generating "today" adds $K_5, V_5$ (pp. 56–58).

## Explanation

The cache lets [[Autoregressive Language Modeling|autoregressive generation]] skip work on past tokens. It does not remove the cost of a long history: "Caching avoids recomputing the past; it does not make history free" (p. 58). Each new token adds one more K, V pair, so there is "more stored history to attend to" at each later step (p. 58).

### Per-layer cache

[[Block 5 Slides]] shows a simplified per-layer cache and cites the Hugging Face Transformers page "How caching works" (p. 224). Each layer stores two vectors for each processed token (p. 224):

- **K, the key**, which helps score relevance.
- **V, the value**, the information to mix.

At a new token, the model reuses the past K and V, then computes and appends the K and V for the new position (p. 224). The cache adds one slot per token as history grows: 2 slots at t=2, 5 at t=5, and 8 at t=8 (p. 226). The deck marks the KV cache as an optional extension, to revisit after learning how [[Attention|attention]] reads context (p. 223).

Synthesis, not a claim of the slides: the [[Causal Mask]] stops a past token from reading later tokens, so its K and V stay the same when new tokens arrive. That is why the cache can reuse them.

## Related

- [[Autoregressive Language Modeling]]
- [[Transformers]]
- [[Attention]]
- [[Causal Mask]]
- [[Visual Token Count]]: another case where token count sets inference cost

## Sources

- [[Block 3 Slides]], pp. 56–58
- [[Block 5 Slides]], pp. 223–226
