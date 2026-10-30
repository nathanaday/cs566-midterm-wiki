---
id: con-kgs1an
type: topic
kind: concept
description: A Transformer adds a position vector to each token vector, so the input keeps word order that token vectors alone do not carry.
tags: [machine-learning]
aliases: [Position vector, Positional embedding, Positional encodings]
created: 2026-09-28T00:00:00
updated: 2026-10-19T17:48:15
refreshed: 2026-10-19T17:48:15
status: stable
sources: ["[[Block 5 Slides]]", "Attention Is All You Need (note)", "[[F26-midterm-review-234p]]"]
---

> [!concept] Concept
> 3 sources · refreshed 2026-10-19 · #machine-learning

## Definition

The model adds a position vector to each token vector: word vector + position vector = input vector. For example, "dog" at position 2 plus $p_2$ gives input 2 ([[Block 5 Slides]], p. 132; [[F26-midterm-review-234p]], p. 178). The position values preserve word order across the sequence (same pages). The input of the complete model is "Tokens + position" ([[Block 5 Slides]], p. 149; [[F26-midterm-review-234p]], p. 194).

## Explanation

Token vectors alone do not specify their order. "dog bites man" and "man bites dog" use the same words but swap the actor and the target ([[Block 5 Slides]], p. 131; [[F26-midterm-review-234p]], p. 177). Position answers the question "where is this token?" ([[Block 5 Slides]], p. 139; [[F26-midterm-review-234p]], p. 185). It is separate from the [[Causal Mask]], which sets which tokens are visible, and from the [[Attention|attention weights]], which set how much each token contributes (same pages).

### Position and the mask do different jobs

The midterm review tests this split with a practice question. A text model uses both position vectors and a causal mask: which choice explains their different roles? ([[F26-midterm-review-234p]], p. 195). The correct answer is D: "Position vectors tell where each token is, and the causal mask blocks access to future tokens" (pp. 195–196). The answer slide explains the wrong choices (p. 196):

- A gives position vectors the job of blocking future tokens and gives the mask the job of recording word order. "The roles are swapped": position vectors carry order information, and the causal mask limits which tokens can be used.
- B says the mask alone tells each token where it sits. But the mask controls the allowed connections, and position vectors add explicit location information.
- C says position vectors alone stop each token from using later tokens. But position vectors describe location and do not restrict access. Only the causal mask keeps future tokens out of view.

"Position vectors supply explicit location information. A causal mask controls which tokens may be read" (p. 196).

### Other sources

The Attention note names positional encodings as one of the parts that every model on the reading list reuses (Attention Is All You Need (note)). Block 5 does not say whether the position vectors are learned or fixed functions such as sinusoids. The midterm review does not say either.

Synthesis, not a claim of the sources: attention forms a weighted sum over a set of vectors, and a sum does not depend on the order of its terms. Without position vectors, the model has no other signal of order.

## Related

- [[Transformers]]
- [[Attention]]
- [[Causal Mask]]: controls access, where position supplies location
- [[Tokenization]]
- [[Vision Transformer (ViT)]]

## Sources

- [[Block 5 Slides]], pp. 131–132, 139, 149
- Attention Is All You Need (note)
- [[F26-midterm-review-234p]], pp. 177–178, 185, 194–196: the midterm recap and a practice question on position against the mask
