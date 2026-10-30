---
id: con-wkzzcf
type: topic
kind: concept
description: A causal mask hides future tokens from attention, so each position reads only itself and earlier positions and cannot see the token it must predict.
tags: [machine-learning]
aliases: [Causal attention, Masked self-attention, Causal masking]
created: 2026-09-28T00:00:00
updated: 2026-10-19T17:48:15
refreshed: 2026-10-19T17:48:15
status: stable
sources: ["[[Block 5 Slides]]", "[[Block 6 Slides]]", "[[Block 6 Slides Extended]]", "[[F26-midterm-review-234p]]"]
---

> [!concept] Concept
> 4 sources · refreshed 2026-10-19 · #machine-learning

## Definition

A causal mask lets each token attend to itself and earlier tokens only ([[Block 5 Slides]], p. 138; [[F26-midterm-review-234p]], p. 184). "A causal mask controls which tokens may be read" ([[F26-midterm-review-234p]], p. 196). In the graph view of [[Attention|self-attention]], the mask removes the edges to future tokens and makes the allowed interactions directional ([[Block 6 Slides]], p. 118; [[Block 6 Slides Extended]], pp. 122, 125).

## Explanation

### Why the model needs it

A text generator must hide the word it tries to predict. When the model predicts "chased" after "The dog", a view of "chased" would give away the answer ([[Block 5 Slides]], p. 137; [[F26-midterm-review-234p]], p. 183). So a position cannot see the future tokens it tries to predict (same pages).

In training, the mask lets the model score every next-token target in one pass with the future tokens hidden ([[Block 5 Slides]], p. 148; [[F26-midterm-review-234p]], p. 193). See [[Teacher Forcing]].

### What each position sees

Later positions read a longer prefix. At "dog" the model reads the first 2 positions, and at "ball" it reads the first 5 ([[Block 5 Slides]], p. 138; [[F26-midterm-review-234p]], p. 184). In Block 6's graph example, the query at position 3 reads positions 1, 2, and 3, and position 4, the future, is masked ([[Block 6 Slides]], p. 118; [[Block 6 Slides Extended]], p. 125).

The deck's example weight matrix for "The dog ran" ([[Block 5 Slides]], p. 140; [[F26-midterm-review-234p]], p. 186):

| Query | The | dog | ran |
|---|---|---|---|
| The | 1.0 | hidden | hidden |
| dog | 0.3 | 0.7 | hidden |
| ran | 0.1 | 0.6 | 0.3 |

### Mask, position, and weights are separate choices

Block 5 separates three questions ([[Block 5 Slides]], p. 139; [[F26-midterm-review-234p]], p. 185):

- [[Positional Encoding|Position]] answers "where is this token?" (dog at position 2).
- The causal mask answers "which tokens are visible?" (at dog: The and dog).
- The [[Attention|attention weights]] answer "how much does each token contribute?" (at It: dog gets 0.35).

Order, access, and contribution are three separate choices (same pages).

The midterm review tests the split between position and the mask with a practice question (pp. 195–196). Position vectors describe location but do not restrict access. Only the causal mask keeps future tokens out of view ([[F26-midterm-review-234p]], p. 196). An answer that gives position vectors the job of blocking future tokens and gives the mask the job of recording order is wrong: "The roles are swapped" (p. 196).

### Link to the KV cache (synthesis)

This is our inference, not a claim of the slides. The mask stops a past token from reading later tokens, so its keys and values do not change when new tokens arrive. That is why a [[KV Cache]] can store and reuse them.

## Related

- [[Attention]]
- [[Transformers]]
- [[Autoregressive Language Modeling]]
- [[Teacher Forcing]]: the mask lets training score all positions at once
- [[KV Cache]]
- [[Positional Encoding]]

## Sources

- [[Block 5 Slides]], pp. 137–140, 148
- [[Block 6 Slides]], p. 118
- [[Block 6 Slides Extended]], pp. 122, 125
- [[F26-midterm-review-234p]], pp. 183–186, 193, 195–196: the midterm recap and a practice question on the mask against position
