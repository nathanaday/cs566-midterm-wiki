---
id: con-98pys1
type: topic
kind: concept
description: Tokenization splits text into tokens, the units a language model reads and predicts, which are not always words or characters.
tags:
  - machine-learning/cs566-deeplearning
aliases:
  - Tokens
  - Tokenizer
created: 2026-09-28T00:00:00
updated: 2026-10-13T18:22:42
refreshed: 2026-10-13T18:22:42
status: stable
sources:
  - "[[Block 1 Slides]]"
  - "Lecture 1"
up:
  - "[[Autoregressive Language Modeling]]"
---

> [!concept] Concept
> 2 sources · refreshed 2026-10-13 · #machine-learning/cs566-deeplearning
> Up: [[Autoregressive Language Modeling]]

## Definition

A token is the unit a language model reads and predicts. It is not always a word or a character. "Tokens Are the Pieces the Model Sees" ([[Block 1 Slides]], p. 82).

## Explanation

The slides show the `cl100k_base` tokenizer (tiktoken 0.13.0), where `·` marks one leading space ([[Block 1 Slides]], p. 82):

| Text | Tokens |
| --- | --- |
| The model predicts the next token. | 7: `The`, `·model`, `·predicts`, `·the`, `·next`, `·token`, `.` |
| `20260824123456` | 5: `202`, `608`, `241`, `234`, `56` |
| `语言模型` | 4: `语`, `言`, `模`, `型` |

The live demo is Tiktokenizer by Duong Quoc (dqbd), MIT license ([[Block 1 Slides]], p. 82). The notes link to it: https://tiktokenizer.vercel.app (Lecture 1, § Deep Learning).

A chat is also one token sequence. Special tokens mark each role, for example `<|start_header_id|>assistant<|end_header_id|>` ... `<|eot|>` ([[Block 1 Slides]], p. 87, adapted from Sean Welleck, CMU 11-711). See [[Post-Training]].

Synthesis: the examples show that a number or a non-English word can split in ways a reader does not expect. Token count, not word count, sets how much fits in a request. [[Agent Skills]] treat context as a budget for this reason.

## Related

- [[Autoregressive Language Modeling]]
- [[Post-Training]]
- [[Agent Skills]]
- [[In-Context Learning]]

## Sources

- [[Block 1 Slides]], pp. 82, 87
- Lecture 1, § Deep Learning (tokenizer link)
