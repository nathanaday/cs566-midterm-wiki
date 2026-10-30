---
id: con-t7dp4k
type: topic
kind: concept
description: An encoder-decoder model that reads an input sequence into one vector (many-to-one) and then generates an output sequence from that vector (one-to-many).
tags: [machine-learning]
aliases: [Seq2Seq, Encoder-Decoder, Sequence Transduction Model]
created: 2026-09-28T00:00:00
updated: 2026-09-28T00:00:00
refreshed: 2026-09-28T00:00:00
status: stable
sources: ["[[Block 5 Slides]]", "Topic Note - Sequence Transduction"]
---

> [!concept] Concept
> 2 sources · refreshed 2026-09-28 · #machine-learning

## Definition

A sequence-to-sequence model joins two recurrent parts ([[Block 5 Slides]], pp. 68–69, credited to Stanford CS231n):

- **Many to one**: the encoder reads the input sequence $x_1, x_2, \dots$ and encodes it in a single vector, its final hidden state $h_T$ (p. 68).
- **One to many**: the decoder starts from that vector and produces the output sequence $y_1, y_2, \dots$ (p. 69).

The slides cite Sutskever et al., "Sequence to Sequence Learning with Neural Networks", NIPS 2014 (pp. 68–69).

## Explanation

### Two sets of weights

The encoder applies one function $f_W$ with weights $W_1$ at every input step. The decoder applies $f_W$ with separate weights $W_2$ at every output step ([[Block 5 Slides]], p. 69). Each part reuses its own weights across time, as in any [[Recurrent Neural Networks (RNN)|RNN]].

### Sequence transduction

- Transduction converts one thing into another, such as translation or speech to text. A sequence transduction model converts one sequence into another. Classification instead outputs one label (Topic Note - Sequence Transduction).
- In the encoder-decoder structure, the encoder compresses the whole input into an internal representation. The decoder generates the output one piece at a time (Topic Note - Sequence Transduction).
- Before the Transformer, RNNs or CNNs did this work (Topic Note - Sequence Transduction). See [[Transformers]].

### Synthesis

- The single vector $h_T$ is the only path from input to output. The Block 5 deck names the same limit for an LSTM: "A fixed-size state must compress the entire past" ([[Block 5 Slides]], p. 122). Attention and the Transformer remove this limit.
- The two halves appear alone as other tasks. [[Question Answering]] uses many-to-one encoders. [[Image Captioning]] uses a one-to-many decoder that starts from an image vector.
- The decoder generates one token at a time and feeds each token back, as in [[Autoregressive Language Modeling]]. In training it can read the observed tokens instead; see [[Teacher Forcing]].

## Related

- [[Recurrent Neural Networks (RNN)]]
- [[Transformers]]
- [[Image Captioning]]
- [[Question Answering]]
- [[Autoregressive Language Modeling]]
- [[Teacher Forcing]]

## Sources

- [[Block 5 Slides]], pp. 68–69, 122
- Topic Note - Sequence Transduction
