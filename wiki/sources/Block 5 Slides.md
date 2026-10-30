---
id: src-p9ayrd
type: source
description: "The CSCI 566 Block 5 slide deck by Yue Zhao on sequence models: RNNs, backpropagation through time, vanishing and exploding gradients, LSTMs, attention, the decoder-only Transformer, RNN applications, and optional material on the KV cache and modern recurrence."
tags: [machine-learning/cs566-deeplearning]
aliases: []
created: 2026-09-28T00:00:00
updated: 2026-09-28T00:00:00
refreshed: 2026-09-28T00:00:00
authority: official
status: absorbed
file: "[[internal/wiki/originals/0a94275989111d63.pdf]]"
media: pdf
sha256: 0a94275989111d63eef3587ba269b663e05d94ac5c1641cbecff3eb623494da9
origin: ingest
locator: Block 5 Slides.pdf
measure: 231 pages
captured: 2026-09-28T00:00:00
---

> [!source] PDF · 231 pages · official
> Captured 2026-09-28 from `Block 5 Slides.pdf` (ingest) · absorbed by 2026-09-28 Ingest the CS566 Block 5 and Block 6 slides (2)

![[internal/wiki/originals/0a94275989111d63.pdf]]

## Summary

The CSCI 566 deck "Block 5: RNN, LSTM, and Transformer", by the instructor Yue Zhao. It has 231 PDF pages. It opens with logistics (quiz scheduling, proposal feedback) and a frame for the next blocks: CNNs, RNNs, and GNNs all share parameters and differ in which inputs can interact. It builds the recurrent neural network from sequence tasks, trains it with backpropagation through time, and shows why vanilla RNN gradients vanish or explode. It introduces the LSTM as memory with learned gates, then moves from attention over image regions to self-attention and a decoder-only Transformer. It ends with RNN applications (captioning, question answering, VQA) and optional material on LSTM details, the KV cache, and modern recurrence. Most slides credit Stanford CS231n. Locators are PDF page numbers.

## Structure

- pp. 1–20, logistics and motivation: parameter sharing across CNN, RNN, and GNN; sequential data; autoregression: [[CS566-DeepLearning]], [[Recurrent Neural Networks (RNN)]], Autoregressive Language Modeling.
- pp. 21–69, RNN basics: input/output configurations, the recurrence formula, the vanilla RNN, computational graphs, and sequence to sequence: [[Recurrent Neural Networks (RNN)]], Sequence to Sequence.
- pp. 70–85, character-level language models, test-time sampling, and training with the observed next input: Autoregressive Language Modeling, Teacher Forcing.
- pp. 86–105, backpropagation through time, truncation, and vanilla RNN gradient flow: Backpropagation Through Time, [[Vanishing Gradient Problem]], [[Exploding Gradient Problem]], [[Gradient Clipping]].
- pp. 106–122, the LSTM as memory with learned gates, and the limit of a compact state: Long Short-Term Memory.
- pp. 123–152, attention over image regions, self-attention, the causal mask, and the decoder-only Transformer: Attention, Causal Mask, Positional Encoding, [[Transformers]].
- pp. 153–200, RNN applications: image captioning, question answering, and VQA; what survives across architecture generations: Image Captioning, Question Answering.
- pp. 201–222, optional LSTM details: equations, gradient path, worked example, GRU and variants: Long Short-Term Memory, [[Recurrent Neural Networks (RNN)]].
- pp. 223–231, optional: the KV cache, fixed state against growing history, hybrid and stronger recurrence, and bidirectional RNNs: KV Cache, Recurrent State vs Growing Context, Hybrid Recurrent-Attention Models.
