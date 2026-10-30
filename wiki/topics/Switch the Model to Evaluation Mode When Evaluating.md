---
id: doc-63476b
type: topic
kind: policy
description: Before evaluation, validation, or inference, put the model in evaluation mode, so BatchNorm uses stored running statistics and dropout turns off its random mask.
tags: [machine-learning/cs566-deeplearning]
aliases: [Eval mode, Evaluation mode, Call model.eval() before inference, Mode is part of the function]
created: 2026-10-19T17:47:21
updated: 2026-10-19T17:48:15
refreshed: 2026-10-19T17:48:15
status: stable
sources: ["[[F26-midterm-review-234p]]", "[[Block 7 Slides]]", "[[Block 4 Slides]]"]
strength: must
up: ["[[Model Evaluation]]"]
---

> [!policy] Must · holds for repositories tagged #machine-learning/cs566-deeplearning
> 3 sources · refreshed 2026-10-19
> Up: [[Model Evaluation]]

## Rule

Put the model in evaluation mode before you evaluate, validate, test, or run inference with it. The slide: "Switch the model to evaluation mode when evaluating" ([[F26-midterm-review-234p]], p. 122; [[Block 7 Slides]], p. 34). Block 4 gives the PyTorch form: "Mode is part of the function. Call model.eval() before inference." ([[Block 4 Slides]], p. 176).

In evaluation mode:

- [[Batch Normalization]] uses the stored running mean and variance, and keeps the same learned scale γ and shift β ([[F26-midterm-review-234p]], pp. 122-123).
- [[Dropout]] turns off its random mask. With inverted dropout, activations pass through with no extra scaling ([[F26-midterm-review-234p]], p. 133).

## Why

- **One input at a time.** "The flower classifier may receive one new photo at a time" ([[F26-midterm-review-234p]], p. 122). See Flower Classifier Running Example.
- **In training mode, the batch changes the output.** "Stored running statistics give one photo the same normalized activation, whatever else is in the batch" ([[F26-midterm-review-234p]], p. 124). In training mode, the same photo x = 7 normalizes to 1 in the batch [7, 3] and to −1 in the batch [7, 11]. In evaluation mode, with stored mean 3 and variance 4, it normalizes to 2 with either companion (p. 124).
- **One layer gives different numbers.** With `bn = nn.BatchNorm1d(1)` and `x = [[1.],[3.]]`, train mode gives `[-1.0, 1.0]` and eval mode gives `[0.7628, 2.6697]` ([[Block 4 Slides]], p. 176). For a batch of 1, PyTorch `BatchNorm1d` raises an error on a `[1, C]` input in training mode (p. 177).
- **Evaluation must be deterministic.** "evaluation should be deterministic, so no random dropout mask is applied" ([[F26-midterm-review-234p]], p. 133).
- **Fair comparison.** "Each method has its own evaluation rule." "Decide the evaluation protocol before comparing models" ([[Block 7 Slides]], p. 165). For loss curves: "Evaluate both curves using comparable loss definitions and modes" ([[Block 7 Slides]], p. 132).

Synthesis: a model left in training mode reports a score that depends on the batch and on random masks. The score then measures the evaluation setup, not only the model. See [[Model Evaluation]].

## Applies when

CS566 course and project work that evaluates, validates, tests, or serves a network with layers whose behavior depends on the mode, such as [[Batch Normalization]] and [[Dropout]].

Synthesis, not a slide claim: this includes the validation pass inside a training loop. Put the model back in training mode before the next training step.

## Exceptions

The slides state no exceptions. The review says BatchNorm "usually" uses stored running statistics during evaluation ([[F26-midterm-review-234p]], p. 122), and Block 7 calls it "the usual running-statistics mode" ([[Block 7 Slides]], p. 165). The slides do not name the other protocols.

Synthesis: two cases are outside this rule.

- A model with no mode-dependent layers computes the same function in both modes. [[Layer Normalization]] is one such layer. The switch has no effect there, and it does no harm.
- [[Data Augmentation]] has its own evaluation rule: "Use a fixed evaluation transform, or a predefined averaging protocol" ([[Block 7 Slides]], p. 165). The data pipeline sets this rule, not the model mode.

## Sources

- [[F26-midterm-review-234p]], pp. 122-124, 133: the rule, the batch-companion example, and the dropout check question
- [[Block 7 Slides]], pp. 34, 132, 165: the rule and the evaluation rule of each method
- [[Block 4 Slides]], pp. 176-177: the PyTorch form of the rule and the train/eval example
