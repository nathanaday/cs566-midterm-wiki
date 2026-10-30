---
id: con-c6qa54
type: topic
kind: concept
description: Test-time training (TTT) updates selected model weights at inference time with a next-token loss on the observed context, then predicts with the updated weights.
tags: [machine-learning/cs566-deeplearning]
aliases: [TTT]
created: 2026-09-28T00:00:00
updated: 2026-10-13T18:22:42
refreshed: 2026-10-13T18:22:42
status: stable
sources: ["[[Block 3 Slides]]", "Sep 14 Lecture Account"]
up: ["[[Updating LLMs]]"]
---

> [!concept] Concept
> 2 sources · refreshed 2026-10-13 · #machine-learning/cs566-deeplearning
> Up: [[Updating LLMs]]

## Definition

Test-time training (TTT) is one of the four ways in [[Updating LLMs]] that the Sep 14 lecture listed (Sep 14 Lecture Account, § Updating LLMs). It updates weights at inference time with a training signal from the input itself.

[[Block 3 Slides]] gives an example (pp. 218–220, citing Tandon et al. 2025, "End-to-End Test-Time Training for Long Context", arXiv:2512.23675):

- The observed context is "The code is 731", followed by a future token that the model has not seen. The model learns to "Predict '731' from the past. Target: already observed." "The past can provide next-token training examples" (p. 218).
- A next-token loss updates selected MLPs, θ → θ'. "Outer training prepares an adaptable initialization" (p. 219).
- The model predicts with θ'. "No future ground truth enters the adaptation loss" (p. 220).

## Explanation

General steps (general background, consistent with the slides):

1. Make a training signal from the input with no label, for example next-token prediction on the input text.
2. Take a few gradient steps on that signal. The steps can train all weights, only a [[LoRA]] adapter, or selected MLPs as on p. 219.
3. Make the prediction with the updated weights $\theta'$.
4. Usually, reset the weights before the next input.

History (general background, not from a course source): Sun et al. introduced the method for image classifiers under distribution shift (ICML 2020). "TTT" also names a different idea: a sequence-model layer whose hidden state is a small model that learns during the forward pass (Sun et al., 2024). The slides use the first idea, on an LLM's context.

Synthesis: TTT sits between the other ways in [[Updating LLMs]].

- As with [[In-Context Learning|context only]], the change serves one input and uses only tokens already seen.
- As with [[LoRA]], the change is in the weights and comes from [[Backpropagation]] and [[Gradient Descent]].

The cost is training compute on every inference.

## Related

- [[Updating LLMs]]
- [[LoRA]]
- [[In-Context Learning]]
- [[Backpropagation]]
- [[Gradient Descent]]

## Sources

- [[Block 3 Slides]], pp. 218–220
- Sep 14 Lecture Account, § Updating LLMs
- The general steps and the history are general background, not from a course source.
