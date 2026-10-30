---
description: "The CSCI 566 Block 5 slide deck by Yue Zhao on sequence models: RNNs, backpropagation through time, vanishing and exploding gradients, LSTMs, attention, the decoder-only Transformer, RNN applications, and optional material on the KV cache and modern recurrence."
---

The original is [[attachments/Block 5 Slides.pdf|Block 5 Slides.pdf]], 231 pages, an official course document saved as `Block 5 Slides.pdf` on 2026-09-28.

## Summary

The CSCI 566 deck "Block 5: RNN, LSTM, and Transformer", by the instructor Yue Zhao. It has 231 PDF pages. It opens with logistics (quiz scheduling, proposal feedback) and a frame for the next blocks: CNNs, RNNs, and GNNs all share parameters and differ in which inputs can interact. It builds the recurrent neural network from sequence tasks, trains it with backpropagation through time, and shows why vanilla RNN gradients vanish or explode. It introduces the LSTM as memory with learned gates, then moves from attention over image regions to self-attention and a decoder-only Transformer. It ends with RNN applications (captioning, question answering, VQA) and optional material on LSTM details, the KV cache, and modern recurrence. Most slides credit Stanford CS231n. Locators are PDF page numbers.

## Structure

- pp. 1–20, logistics and motivation: parameter sharing across CNN, RNN, and GNN; sequential data; autoregression: [[_index|CSCI 566 Midterm Wiki]], [[Recurrent Neural Networks (RNN)]], Autoregressive Language Modeling.
- pp. 21–69, RNN basics: input/output configurations, the recurrence formula, the vanilla RNN, computational graphs, and sequence to sequence: [[Recurrent Neural Networks (RNN)]], Sequence to Sequence.
- pp. 70–85, character-level language models, test-time sampling, and training with the observed next input: Autoregressive Language Modeling, Teacher Forcing.
- pp. 86–105, backpropagation through time, truncation, and vanilla RNN gradient flow: Backpropagation Through Time, [[Vanishing Gradient Problem]], [[Exploding Gradient Problem]], [[Gradient Clipping]].
- pp. 106–122, the LSTM as memory with learned gates, and the limit of a compact state: Long Short-Term Memory.
- pp. 123–152, attention over image regions, self-attention, the causal mask, and the decoder-only Transformer: Attention, Causal Mask, Positional Encoding, [[Transformers]].
- pp. 153–200, RNN applications: image captioning, question answering, and VQA; what survives across architecture generations: Image Captioning, Question Answering.
- pp. 201–222, optional LSTM details: equations, gradient path, worked example, GRU and variants: Long Short-Term Memory, [[Recurrent Neural Networks (RNN)]].
- pp. 223–231, optional: the KV cache, fixed state against growing history, hybrid and stronger recurrence, and bidirectional RNNs: KV Cache, Recurrent State vs Growing Context, Hybrid Recurrent-Attention Models.
