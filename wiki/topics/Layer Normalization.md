---
id: doc-25zs6s
type: topic
kind: concept
description: A normalization layer that normalizes the features within one example or token, not one feature across a mini-batch as batch normalization does; it is the common choice in Transformers.
tags: [machine-learning/cs566-deeplearning]
aliases: [LayerNorm, Layer Norm, LN]
created: 2026-10-12T16:58:10
updated: 2026-10-13T18:22:47
refreshed: 2026-10-13T18:22:47
status: stable
sources: ["[[Block 7 Slides]]", "[[Block 5 Slides]]"]
up: ["[[Neural Network Training]]"]
---

> [!concept] Concept
> 2 sources · refreshed 2026-10-13 · #machine-learning/cs566-deeplearning
> Up: [[Neural Network Training]]

## Definition

Layer normalization (LayerNorm) normalizes activations, as [[Batch Normalization]] does, but it uses a different group of values. LayerNorm compares "features within one example or token". BatchNorm compares "one feature across examples in a mini-batch" ([[Block 7 Slides]], p. 35).

## Explanation

### Which values supply the statistics

"Both normalize activations, using different groups of values" ([[Block 7 Slides]], p. 35):

| | BatchNorm | LayerNorm |
| --- | --- | --- |
| Values compared | One feature across examples in a mini-batch | Features within one example or token |
| Common in | CNNs | Transformers |

The slide's rule: "Identify which values supply the normalization statistics" (p. 35).

The deck draws BatchNorm on an $N \times D$ batch $X$: it computes the mean and variance "independently for each dimension", one column of $X$ (p. 28). Synthesis: LayerNorm takes its statistics from one row of $X$, over the $D$ features of one example.

### In Transformers

LayerNorm is "common in Transformers" ([[Block 7 Slides]], p. 35). In the course's text-generating Transformer, each block runs causal multi-head attention, then "+ input → LayerNorm", then the MLP at each position, then "+ input → LayerNorm". "Shortcuts + normalization help train the stack" ([[Block 5 Slides]], p. 149). See [[Transformers]] and [[Residual Connections]].

### What the slides do not say

The slides give no formula and no citation for LayerNorm. The points below are synthesis, not slide content:

- The statistics come from one example. So the output does not depend on the other examples in the batch, and the layer needs no running statistics.
- So LayerNorm computes the same function in training and evaluation mode. This avoids the two BatchNorm pitfalls in [[Batch Normalization]]: small batches, and the train/eval mode switch.
- Like BatchNorm, the usual LayerNorm also learns a scale and shift for each feature.

Open question: does the course give the LayerNorm formula, or discuss where the normalization goes relative to the residual add?

## Related

- [[Batch Normalization]]: the same idea over a different group of values
- [[Transformers]]: LayerNorm after each residual add
- [[Residual Connections]]
- [[Data Preprocessing]]: input normalization, done once before training

## Sources

- [[Block 7 Slides]], pp. 28, 35
- [[Block 5 Slides]], p. 149
