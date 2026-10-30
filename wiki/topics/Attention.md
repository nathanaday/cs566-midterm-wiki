---
id: con-bzzk8f
type: topic
kind: concept
description: Attention computes a weighted sum of value vectors, with weights from comparing a query against the allowed keys; in self-attention the tokens of one sequence supply the queries, keys, and values, and the mask sets which token pairs interact.
tags: [machine-learning]
aliases: [Self-attention, Attention weights, Attention mechanism, Visual attention, Soft attention, Contextual token representation, Attention as a token interaction graph, Token interaction graph, Attention masks as graph edges]
created: 2026-09-28T00:00:00
updated: 2026-10-19T17:48:15
refreshed: 2026-10-19T17:48:15
status: stable
sources: ["[[Block 5 Slides]]", "[[Block 6 Slides]]", "[[Block 6 Slides Extended]]", "[[F26-midterm-review-234p]]"]
---

> [!concept] Concept
> 4 sources · refreshed 2026-10-19 · #machine-learning

## Definition

Block 6 defines attention in general terms: given a set of value vectors and a query vector, attention computes a weighted sum of the values that depends on the query ([[Block 6 Slides]], p. 116). Each token has a value vector, which is its representation, and a query vector. The query computes the attention scores, and those scores are the weights in the sum (p. 116). The extended deck adds the key: each token has a query, a key, and a value. The model compares a query with the allowed keys to get the weights, and uses those weights to mix the matching values ([[Block 6 Slides Extended]], p. 123).

Self-attention is attention in which the context comes from the sequence itself ([[Block 5 Slides]], p. 128). It is the key component of the [[Transformers|Transformer]] ([[Block 6 Slides]], p. 115; [[Block 6 Slides Extended]], p. 122).

## Explanation

### Reading context instead of carrying a state

The midterm review opens its attention section with one contrast. Instead of carrying one state forward, attention lets each position read directly from a context ([[F26-midterm-review-234p]], p. 174). Recurrent models pass a carried state step by step; attention computes a weighted read over many positions (p. 174). The same slide says that position information, masks, and attention weights are distinct parts that a reader should not confuse (p. 174). See [[Recurrent Neural Networks (RNN)]].

### Attention over image regions

Block 5 introduces attention with image captioning and credits the mechanism to Xu et al. (2015) ([[Block 5 Slides]], p. 123). The decoder keeps one feature vector for each image region, so the model does not have to force all parts of the scene into one vector (p. 125). The current caption prefix queries the regions:

- For the prefix "A", the weighted mixture gives the most weight to the person region, and the model predicts "person" (p. 126).
- For "A person throws a", the weight moves to the disc region, and the model predicts "frisbee" (p. 127).

The regions stay the same. Only the weights change: a new prefix computes new scores from the same evidence (p. 127).

### Self-attention over text

Over text, the context is the sequence itself. Each token reads itself and earlier tokens, and the sequence supplies position and context ([[Block 5 Slides]], p. 128). "Self" means that the current position and its context share one sequence (p. 150).

A token needs context from other tokens to resolve its meaning. In "The dog chased the ball. It", "It" can refer to the dog or the ball, and all seven positions, "It" included, can supply information ([[Block 5 Slides]], p. 133; [[F26-midterm-review-234p]], p. 179).

### The two steps

1. **Compute the weights** at the query position. The deck's example weights for one head at "It" are: The 0.05, dog 0.35, chased 0.15, the 0.05, ball 0.25, "." 0.05, It 0.10. The weights add to 1 ([[Block 5 Slides]], p. 134; [[F26-midterm-review-234p]], p. 180).
2. **Mix the values.** The weights form a weighted sum of the value vectors. The result is the context vector for "It". Each weight controls how much its value vector contributes ([[Block 5 Slides]], p. 135; [[F26-midterm-review-234p]], p. 181).

The weights come from the current input, so a different token or context gives a different set of weights ([[Block 5 Slides]], p. 134; [[F26-midterm-review-234p]], p. 180). Each query position gets its own weights and its own context vector: shared parameters compute a different mixture at each position ([[Block 5 Slides]], p. 140; [[F26-midterm-review-234p]], p. 186). The deck leaves the projections that produce the queries, keys, and values to Block 9 ([[Block 5 Slides]], p. 135; [[F26-midterm-review-234p]], p. 181).

### A numeric example

The midterm review reduces step 2 to single numbers ([[F26-midterm-review-234p]], p. 182). The task is to predict the next token after "The dog barked". At "barked", toy attention mixes the prefix values 1 (The), 5 (dog), and 9 (barked) with the weights 0.2, 0.3, and 0.5:

$$\text{context} = 0.2 \cdot 1 + 0.3 \cdot 5 + 0.5 \cdot 9 = 0.2 + 1.5 + 4.5 = 6.2$$

The slide adds: "Projection parameters are learned and fixed at inference; attention weights are recomputed for each input" (p. 182).

Synthesis, not a claim of the slides: the weights add to 1, so the context is a weighted average of the values, and it stays between the smallest value (1) and the largest (9). Training learns the projections. The model computes the weights again from each input, so one trained model gives "It" different weights in different sentences.

### Contextual token vectors

Attention gives the same starting vector different outputs in different contexts. "It" starts from the same vector in "The ball rolled. It" and in "The dog ran. It". It ends with a ball context in the first sentence and a dog context in the second ([[Block 5 Slides]], p. 136). The earlier dog-and-ball sentence stays ambiguous (p. 136).

### Self-attention as a token graph

Block 6, the graph neural network deck, reads self-attention as a graph over tokens. The first version says every token attends to all other tokens through matrix calculation ([[Block 6 Slides]], p. 115). The extended version changes this: each token attends to the allowed positions, and a [[Causal Mask]] excludes future tokens ([[Block 6 Slides Extended]], p. 122).

Unmasked self-attention uses a complete token interaction graph: a query at one position reads all positions ([[Block 6 Slides]], p. 117; [[Block 6 Slides Extended]], p. 124). A causal mask removes the edges to future tokens, so the allowed interactions become directional ([[Block 6 Slides]], p. 118; [[Block 6 Slides Extended]], p. 125).

#### Comparison with a GNN

The extended deck compares self-attention with a [[Graph Neural Networks|GNN]]. It reminds the reader that in Block 5, tokens gathered context from allowed positions ([[Block 6 Slides Extended]], p. 121):

| Model | What it reads |
|---|---|
| Road GNN | the connected road segments |
| Self-attention | the token positions that the mask allows |

The two models weight their inputs differently: attention learns input-dependent mixing weights (p. 121). The slide concludes: "GNN neighborhoods and attention masks both restrict information flow" (p. 121). The slide calls itself a course schematic (p. 121).

The slides do not make this claim; it is our synthesis. The mask has the role of the graph's edges. A GNN layer reads its neighbors through [[Neighborhood Aggregation]]. In the basic [[Graph Convolutional Network]] update, each neighbor gets the same weight, $1/|N(v)|$. Attention computes each weight from the query and the keys of the current input instead.

## Related

- [[Transformers]]
- [[Causal Mask]]
- [[Positional Encoding]]
- [[KV Cache]]
- [[Autoregressive Language Modeling]]
- [[Recurrent Neural Networks (RNN)]]: a carried state instead of a weighted read
- [[Vision Language Models (VLM)]]
- [[Graph Neural Networks]]: GNN neighborhoods restrict information flow, as attention masks do
- [[Neighborhood Aggregation]]
- [[Graph Convolutional Network]]

## Sources

- [[Block 5 Slides]], pp. 123–128, 133–136, 140, 150
- [[Block 6 Slides]], pp. 115–118
- [[Block 6 Slides Extended]], pp. 121–125
- [[F26-midterm-review-234p]], pp. 174, 179–182, 186: the midterm recap of the Block 5 attention slides, with a numeric example
