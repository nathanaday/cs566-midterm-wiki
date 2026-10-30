---
id: doc-y3txw1
type: topic
kind: concept
description: A head is a small trainable network on top of a larger model (the backbone) that maps the backbone's outputs or features to a task's outputs; in transfer learning the backbone is often pretrained and frozen, and in a graph neural network a shared head reads each node vector or the pooled graph vector.
tags: [machine-learning/cs566-deeplearning]
aliases: [head, prediction head, classifier head, new head, shared classifier, node head, graph head]
created: 2026-10-13T18:25:38
updated: 2026-10-19T17:48:15
refreshed: 2026-10-19T17:48:15
status: draft
sources: ["[[Block 7 Slides]]", "[[Block 4 Slides]]", "CS566 Project Pre-proposal", "CS566-project", "[[F26-midterm-review-234p]]"]
up: ["[[Transfer Learning]]"]
---

> [!concept] Draft · Concept
> 5 sources · refreshed 2026-10-19 · #machine-learning/cs566-deeplearning
> Up: [[Transfer Learning]]

## Definition

A head is a small neural network attached to a larger pre-trained model. It reads the model's outputs. It is useful because the larger pre-trained model can stay frozen while the head adds to its capabilities or behavior (CS566-project, My Journal).

## Explanation

- **In transfer learning.** Stage 1 of [[Transfer Learning]] replaces the original label predictor of a pretrained model with a new head, such as "a three-class flower head". The pretrained backbone stays frozen, and only the head trains ([[Block 7 Slides]], p. 194). See [[Flower Classifier Running Example]].
- **As a baseline.** Block 7 calls a frozen backbone with a new head "A low-cost baseline for the new labels." It says to compare it with partial and full fine-tuning "using the same validation protocol" ([[Block 7 Slides]], p. 210). See [[Fine-Tuning]].
- **When to use one.** Freeze the encoder and train a head when labels or compute are scarce. Fine-tune when a task shift justifies it ([[Block 4 Slides]], p. 230). See [[Pretrained Visual Encoders]].
- **The trainable part.** The summary slide of Block 7 lists the trainable part of a model as the full model, selected layers, or a new head ([[Block 7 Slides]], p. 226).
- **Linear probe.** A linear probe is a head that is one linear classifier on fixed features. Only the head learns, so its score measures the features. See [[Pretrained Visual Encoders]].

### In a graph neural network

In a [[Graph Neural Networks|graph neural network]], the head reads the vectors that the GNN layers compute. For node A, the head converts the node vector $h_A$ into class scores: node vector $h_A$, then a shared classifier, then low-risk and high-risk scores. "A training label supplies the loss for a labeled node." "The head and GNN layers train together when both are trainable." ([[F26-midterm-review-234p]], p. 212).

The output task selects the head. Node tasks keep one output per node and use node heads, which give the labels of A, B, and the other nodes. Graph tasks pool the node vectors and use one graph head, which gives one graph label ([[F26-midterm-review-234p]], p. 217). See [[Graph Convolutional Network]] and [[Permutation Invariance and Equivariance]].

Synthesis: in this case the layers under the head are not necessarily pretrained or frozen. The same classifier is applied to every node vector, so the head keeps the node outputs in step with any node reordering.

### In the CS566 project

The project trains a small convolutional head on top of a frozen Depth Anything V2. The head predicts, per pixel, whether the depth error exceeds a threshold (CS566 Project Pre-proposal, p. 1). The journal of CS566-project gives the idea in the user's words: when Depth Anything says one pixel is 23 m away, the head adds a confidence, such as "23m, 0.9 confident" against "23m, 0.3 confident". Because a network learns by comparing its output with a label, the head needs only the observation and the ground truth to train (CS566-project, My Journal). See Per-Pixel Depth Confidence Head.

## Related

- [[Transfer Learning]]
- [[Fine-Tuning]]
- [[Pretrained Visual Encoders]]
- [[Parameter-Efficient Fine-Tuning]]
- [[Graph Neural Networks]]: node heads and the graph head after a readout
- [[Graph Convolutional Network]]: the head and the GNN layers trained together
- Per-Pixel Depth Confidence Head
- CS566-project

## Sources

- [[Block 7 Slides]]
- [[Block 4 Slides]]
- CS566 Project Pre-proposal
- CS566-project (My Journal: the user's notes)
- [[F26-midterm-review-234p]], pp. 212, 217
