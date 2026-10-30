---
id: src-2vfn29
type: source
description: "The CSCI 566 Block 3 slide deck on neural networks by Yue Zhao, for weeks 3 and 4: neurons, forward propagation, activations, backpropagation, ways to update an LLM, and gradient problems."
tags: [machine-learning/cs566-deeplearning]
aliases: []
created: 2026-09-28T00:00:00
updated: 2026-09-28T00:00:00
refreshed: 2026-09-28T00:00:00
authority: official
status: absorbed
file: "[[internal/wiki/originals/10ea1101df5966c8.pdf]]"
media: pdf
sha256: 10ea1101df5966c8e639fcd54e755bb2b30827ecdccf46a8f6f964bd90793025
origin: ingest
locator: Block 3 Slides.pdf
measure: 272 pages
captured: 2026-09-28T00:00:00
---

> [!source] PDF · 272 pages · official
> Captured 2026-09-28 from `Block 3 Slides.pdf` (ingest) · absorbed by 2026-09-28 Absorb the CS566 and self-study sources

![[internal/wiki/originals/10ea1101df5966c8.pdf]]

## Summary

The CSCI 566 deck "Block 3: Neural Networks", by the instructor Yue Zhao. It has 272 PDF pages, and the PDF was made on 2026-09-07. CSCI 566 Syllabus puts this material in week 3 (Sep 14: perceptron, gradient descent, forward propagation) and week 4 (Sep 21: backpropagation, vanishing gradients, activation functions). Many slides add one number or one arrow to the slide before; pp. 3–16 repeat [[Block 1 Slides]] pp. 207–339. Locators are PDF page numbers; the printed number equals the PDF page except on pp. 161–167, which are printed 61–67.

## Structure

- pp. 1–35, motivation: one function, recap of loss and gradient descent, neurons, from linear classifiers to networks, why deep: [[Function Approximation]], [[Gradient Descent]], [[Neural Networks]], [[Deep Learning]], [[Perceptron]].
- pp. 36–74, forward propagation, an LLM aside on the KV cache, data shapes, fully connected layers, a tiny worked network: [[Forward Propagation]], KV Cache, [[Neural Networks]].
- pp. 75–101, activation choice, "ReLU Strikes Back" and GELU, capacity, the next token as classification: [[Activation Functions]], [[Activation Sparsity]], [[Dying ReLU]], [[Loss Functions]], Autoregressive Language Modeling.
- pp. 102–180, backpropagation on computational graphs: scalar examples, gate patterns, vector derivatives, Jacobians: [[Backpropagation]], Computational Graphs.
- pp. 181–223, backpropagation through a full network, GPU memory, and four ways to update an LLM: [[Backpropagation]], Updating LLMs, In-Context Learning, [[LoRA]], Test-Time Training, Agent Memory.
- pp. 224–272, vanishing and exploding gradients, residual paths, clipping, activation functions in depth, next blocks: [[Vanishing Gradient Problem]], [[Exploding Gradient Problem]], [[Gradient Clipping]], [[Residual Connections]], [[Batch Normalization]], [[Activation Functions]].
