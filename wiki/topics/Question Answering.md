---
id: con-s3h9j8
type: topic
kind: concept
description: The task of reading a text or an image together with a question and outputting the answer; the Block 5 models encode the text or image and the question separately, then a network combines them to predict an answer word.
tags: [machine-learning/cs566-deeplearning]
aliases: [QA, Visual Question Answering, VQA, Answer Span Selection, Extractive Question Answering]
created: 2026-09-28T00:00:00
updated: 2026-10-13T18:22:47
refreshed: 2026-10-13T18:22:47
status: stable
sources: ["[[Block 5 Slides]]"]
up: ["[[Recurrent Neural Networks (RNN)]]"]
---

> [!concept] Concept
> 1 source · refreshed 2026-10-13 · #machine-learning/cs566-deeplearning
> Up: [[Recurrent Neural Networks (RNN)]]

## Definition

Question answering (QA) gives a model a text and a question, and the model outputs the answer ([[Block 5 Slides]], pp. 169–170). Visual question answering (VQA) replaces the text with an image (p. 190).

## Explanation

### Text QA with two RNNs

The example comes from bAbI task 1 (Weston et al., 2015, CC BY 3.0) ([[Block 5 Slides]], pp. 169–170):

- Text: "Mary moved to the bathroom. John went to the hallway."
- Question: "Where is Mary?"
- Answer: "bathroom"

The approach is to encode the text and the question, then predict an answer word (pp. 169–170):

1. An RNN reads the text one word per step, from $x_1$ = "Mary" to $x_{12}$ = ".". Its last hidden state $h_{12}$ is the text embedding $T$ (pp. 171–180).
2. A second RNN reads the question one word per step: "Where", "is", "Mary", "?". Its last hidden state $h_4$ is the question embedding $Q$ (pp. 181–186).
3. A neural network takes $T$ and $Q$ and outputs the answer $y$, "Bathroom" (pp. 187–188).

Synthesis: each RNN is a many-to-one encoder, the first half of [[Sequence to Sequence]]. The answer is one word, so no decoder is needed.

### Answer span selection

A model can also read a passage and select the span that answers the question ([[Block 5 Slides]], p. 189, course schematic):

- Passage: "The observatory opened in 1935. Its telescope was upgraded in 1987."
- Question: "When did the observatory open?"
- Selected span: "1935".
- "The answer must match the relation asked about in the question." The year 1987 is also a date in the passage, but it answers a different relation.

### Visual question answering

- Example questions: "What color are her eyes?", "How many slices of pizza are there?", "Is this a vegetarian pizza?", "Does this person have 20/20 vision?" ([[Block 5 Slides]], p. 190).
- The slide cites "VQA: Visual Question Answering" (Agrawal et al.) and "A simple neural network module for relational reasoning" (Santoro et al.) (p. 190).
- For an image of rendered objects, the question "What is the size of the brown sphere?" has the answer "Small" (p. 191).

The model has three parts ([[Block 5 Slides]], pp. 193–198):

1. A convolutional network turns the image into an image feature $F$ (p. 193).
2. An RNN reads the question word by word. Its last hidden state is the question embedding $Q$ (pp. 194–196).
3. A neural network combines $F$ and $Q$ and outputs the answer $y$, "small" (pp. 197–198).

Synthesis: text QA and VQA use the same structure. Only the encoder of the evidence changes, from an RNN over words to a CNN over pixels. [[Vision Language Models (VLM)]] answer visual questions in free text instead of one answer word.

## Related

- [[Recurrent Neural Networks (RNN)]]
- [[Convolutional Neural Networks (CNN)]]
- [[Sequence to Sequence]]
- [[Image Captioning]]
- [[Vision Language Models (VLM)]]
- [[CLIP]]

## Sources

- [[Block 5 Slides]], pp. 169–198
