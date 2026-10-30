---
id: con-9bz8t5
type: topic
kind: concept
description: During training, a sequence model reads the observed data token as its next input instead of its own prediction, so every position's input is known in advance.
tags: [machine-learning/cs566-deeplearning]
aliases: [Training Supplies the Next Input, Parallel Next-Token Training]
created: 2026-09-28T00:00:00
updated: 2026-10-19T17:48:15
refreshed: 2026-10-19T17:48:15
status: stable
sources: ["[[Block 5 Slides]]", "[[F26-midterm-review-234p]]"]
up: ["[[Recurrent Neural Networks (RNN)]]"]
---

> [!concept] Concept
> 2 sources · refreshed 2026-10-19 · #machine-learning/cs566-deeplearning
> Up: [[Recurrent Neural Networks (RNN)]]

## Definition

During training, a sequence model reads the observed data token as its next input. It does not read its own prediction. The loss scores the prediction against the same observed token ([[Block 5 Slides]], pp. 79–80).

The slides do not use the name "teacher forcing". This page uses that common name for what the slides show under "Training Supplies the Next Input" (p. 79) and "Training Scores All Positions in Parallel" ([[Block 5 Slides]], p. 148; [[F26-midterm-review-234p]], p. 193). The midterm review does not use the name either.

## Explanation

### In an RNN

The training example is "a dog runs" ([[Block 5 Slides]], pp. 79–80, course schematic):

- The RNN reads "a" and produces next-token scores. The target is "dog". The next input comes from the data: "dog" (p. 79).
- "Training: score against dog, then read the observed dog" (p. 79).
- Suppose the top prediction is "cat". "Loss uses the target dog; the next input is still dog" (p. 80).

Generation works the other way. The model chooses "cat" and reads "cat" as its next input. "Generation feeds back its choice, even when that choice is wrong" (p. 81). At test time a character-level model also feeds each sample back (pp. 74–77). See [[Autoregressive Language Modeling]].

### In a Transformer

- "During training, the full example is already known." For "The dog chased the ball . It", each position has a next-token target, from "dog" (target 1) to "barked" (target 7) ([[Block 5 Slides]], p. 148; [[F26-midterm-review-234p]], p. 193).
- The model scores every next-token target with future tokens hidden. "Training evaluates all sequence positions in a single pass" (same pages). The [[Causal Mask]] hides the future tokens.
- During generation, the next chosen token is not yet known (same pages).
- The midterm review sums up the contrast: "In training, all target positions are known; in generation, each step sees only the generated prefix" ([[F26-midterm-review-234p]], p. 174).
- An RNN updates its state in sequence, so each step waits for the previous state. A Transformer processes the positions in parallel with batched matrix operations on a GPU. "Train many positions together; generate one new token at a time" ([[Block 5 Slides]], p. 151).

### Synthesis

- Because training reads the data, not the model's outputs, every input of a training example is known before the pass starts. This is the condition that lets a Transformer score all positions at once. An RNN has the same inputs but still has to compute its hidden states one after another ([[Block 5 Slides]], p. 151).
- Training and generation read different inputs. In training the model always reads correct history. In generation it reads its own choices, which can be wrong ([[Block 5 Slides]], p. 81). The slides do not name or measure the effect of this difference.

## Related

- [[Autoregressive Language Modeling]]
- [[Recurrent Neural Networks (RNN)]]
- [[Transformers]]
- [[Causal Mask]]: hides the future tokens when training scores all positions
- [[Sequence to Sequence]]
- [[Loss Functions]]

## Sources

- [[Block 5 Slides]], pp. 74–81, 148, 151
- [[F26-midterm-review-234p]], pp. 174, 193: the midterm recap of parallel next-token training
