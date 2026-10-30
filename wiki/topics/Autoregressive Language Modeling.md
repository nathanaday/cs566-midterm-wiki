---
id: con-ddazb7
type: topic
kind: concept
description: A language model writes the probability of a token sequence as a product of next-token probabilities, and it generates text by predicting a token, appending it, and repeating.
tags:
  - machine-learning/cs566-deeplearning
aliases:
  - Next-Token Prediction
  - Language Modeling
  - Autoregressive Generation
  - Autoregression
  - Character-Level Language Model
created: 2026-09-28T00:00:00
updated: 2026-10-19T18:32:33
refreshed: 2026-10-19T18:32:33
status: stable
sources:
  - "Lecture 1"
  - "[[Block 1 Slides]]"
  - "[[Block 3 Slides]]"
  - "CSCI 566 Syllabus"
  - "[[Block 5 Slides]]"
  - "[[F26-midterm-review-234p]]"
  - "Block 8 Slides"
up:
  - "[[Large Language Models]]"
---

> [!concept] Concept
> 7 sources · refreshed 2026-10-19 · #machine-learning/cs566-deeplearning
> Up: [[Large Language Models]]

## Definition

A language model gives the probability of a token sequence as a product of next-token probabilities (Lecture 1, § Deep Learning; [[Block 1 Slides]], p. 81, adapted from Sean Welleck, CMU 11-711):

$$P(x_1, \dots, x_T) = \prod_{t=1}^{T} P(x_t \mid x_{<t})$$

Here $x_t$ is the next token and $x_{<t}$ is the context.

The model generates text with a loop (Lecture 1, § Deep Learning; [[Block 1 Slides]], p. 81):

```
predict → append → repeat
```

A causal model scores the next token from the context. For "Once upon", the example scores are "a" .62, "time" .23, "light" .15. The model samples "a" and appends it, so the next context is "Once upon a" and the next target is "time" ([[Block 5 Slides]], p. 19). The slide states: "Autoregressive = factorization and target, not one model family" (p. 19).

Text becomes tokens before the model sees it. See [[Tokenization]].

Synthesis: the product is the chain rule of probability, so it holds for any distribution over sequences. The modeling choice is to learn each conditional term. An RNN and a Transformer can both learn it; the examples below use each.

## Explanation

### Each step is a classification

Each term is a classification over the vocabulary ([[Block 3 Slides]], pp. 98–101). The slides use the context "The light is ?" and a toy vocabulary of three tokens:

| Step | red | blue | green | Slide |
| --- | --- | --- | --- | --- |
| Linear head $z = Wh + b$ gives logits | ln 2 | 0 | 0 | p. 98 |
| Softmax: $\exp(z)$ = 2, 1, 1; sum 4; $p_i = \exp(z_i)/4$ | 0.500 | 0.250 | 0.250 | p. 99 |
| One gradient step on the logits, $\eta = 0.4$ | 0.574 | 0.213 | 0.213 | p. 101 |

- The observed next token, "red", is the target. The cross-entropy loss is $L = -\ln 0.5 = 0.693$ (p. 100).
- The gradient with respect to the logits is $\partial L/\partial z = p - y = (-0.5, +0.25, +0.25)$. The step $z \leftarrow z - 0.4(p - y)$ raises the probability of the observed token, lowers the others, and drops the loss from 0.693 to 0.554 (p. 101).
- The slide notes: "Direct logit step shown; training updates network parameters" (p. 101).

See [[Loss Functions]].

### A character-level RNN language model

The Block 5 deck trains an RNN to predict the next character ([[Block 5 Slides]], pp. 70–73, credited to Stanford CS231n):

- For the training text "hello", the inputs h, e, l, l have the targets e, l, l, o (p. 70).
- The input "l" has the target "l" after "hel" and "o" after "hell". "Same input l, different history: the hidden state carries context" (p. 70).
- The vocabulary is [h, e, l, o]. Each input character is a one-hot vector, for example "h" = [1, 0, 0, 0] (p. 71).
- The hidden state update is $h_t = \tanh(W_{hh} h_{t-1} + W_{xh} x_t)$ (p. 72).
- An output layer with weights $W_{hy}$ scores each vocabulary character from the hidden state (p. 73).
- The example scores are not yet all correct. For input "h", the target "e" scores 2.2 but "o" scores 4.1 (p. 73). Training pushes the target score up (see the classification step above).

### Test-time sampling

"At test-time sample characters one at a time, feed back to model" ([[Block 5 Slides]], pp. 74–77):

| Input | Softmax over [h, e, l, o] | Sample | Slide |
| --- | --- | --- | --- |
| h | .03, .84, .00, .13 | e | p. 74 |
| e | .25, .20, .50, .05 | l | p. 76 |
| l | .11, .17, .68, .03 | l | p. 77 |
| l | .11, .02, .08, .79 | o | p. 77 |

Each sample becomes the next one-hot input (pp. 75–77).

Synthesis: the softmax values on these slides do not follow from the output scores shown with them. For the first step, the scores 1.0, 2.2, -3.0, 4.1 give "o" the highest probability under a softmax, but the slide gives "e" .84. Read the table as an illustration of the loop, not as a calculation.

### Generation feeds back its choice

- In generation, the prompt "a" goes through the RNN to next-token scores. The model chooses "cat", and that output is the next input. "Generation feeds back its choice, even when that choice is wrong" ([[Block 5 Slides]], p. 81).
- In training, the next input comes from the data, not from the prediction. See [[Teacher Forcing]] ([[Block 5 Slides]], pp. 79–80).
- "Feedback into the model explains generation, not correctness." To continue "a ...", both "a dog runs" and "a cat runs" can be valid. To describe a photo of a dog, "cat" is wrong, even in a fluent sentence (p. 82).

### A character-level RNN on real text

- The deck trains an RNN on Shakespeare's sonnets ([[Block 5 Slides]], p. 83).
- Samples start as random characters. With more training they gain word-like tokens, then punctuation and names such as Natasha, Princess Mary, and Pierre, then near-grammatical sentences (p. 84).
- Samples from the Shakespeare model copy the play format, with speaker names (PANDARUS, VIOLA, KING LEAR, Second Senator) and verse lines. The meaning is incoherent (p. 85).

### Generation with a Transformer

- "Read the prefix, then choose one more token." Transformer blocks process the prefix. A prediction head turns the last-position vector into scores for the next word ([[Block 5 Slides]], p. 146; [[F26-midterm-review-234p]], p. 191).
- The prefix "The dog chased the ball ." produces "It". The extended prefix then produces "barked" ([[Block 5 Slides]], pp. 146–147; [[F26-midterm-review-234p]], pp. 191–192). "Append the new token to the sequence and repeat the process" ([[F26-midterm-review-234p]], p. 192).
- "Generate → append the new token → run the model again" ([[Block 5 Slides]], p. 149; [[F26-midterm-review-234p]], p. 194).
- During generation, the next chosen token is not yet known. During training the full example is known, so the model scores every position in one pass ([[Block 5 Slides]], p. 148; [[F26-midterm-review-234p]], p. 193). The midterm review puts it as: "In training, all target positions are known; in generation, each step sees only the generated prefix" ([[F26-midterm-review-234p]], p. 174). "Train many positions together; generate one new token at a time" ([[Block 5 Slides]], p. 151). See [[Teacher Forcing]] and [[Transformers]].

### One task, many kinds of knowledge

One next-token task can need different knowledge ([[Block 1 Slides]], p. 80, adapted from Manning et al., Stanford CS224N):

| Prompt | Next token | Knowledge |
| --- | --- | --- |
| Stanford University is located in ___, California. | Stanford | world knowledge |
| I put ___ fork down on the table. | the | syntax |
| 1, 1, 2, 3, 5, 8, 13, 21, ___ | 34 | pattern |

Synthesis: next-token prediction is not one fixed skill. It is whatever the context needs, so one objective at scale can produce many abilities.

### Pretraining is not the user's task

The user asks to "Find 3 recent papers", "Verify the facts", or "Send the email". For each, pretraining rewards only "Predict the next token". "The objective and the user task are different" ([[Block 1 Slides]], p. 83).

So a base model continues the pattern of a prompt. Given "Explain the moon landing to a 6-year-old in a few sentences.", it wrote more prompts of the same form: "Explain the theory of gravity to a 6 year old." and "Explain the big bang theory to a 6 year old." "A base model completes the pattern, not the instruction" ([[Block 1 Slides]], p. 84). [[Post-Training]] closes this gap.

### Prefill and decode

Generation has two stages ([[Block 3 Slides]], pp. 56–58):

- **Prefill** processes the prompt and stores a key and a value for each prompt token (p. 56).
- **Decode** computes each new position, then appends its key and value. It reuses the cached keys and values of earlier tokens (p. 57).
- Each new token adds stored history to attend to. "Caching avoids recomputing the past; it does not make history free" (p. 58).

See [[KV Cache]].

### Scale and emergence

- The notes say intelligent behavior seems to emerge in LLMs trained on large data, beyond memorization. They also say it is not clear how, why, or to what extent (Lecture 1, § Deep Learning).
- The 2020 timeline entry "model, data, compute >7 orders (power law)" (Lecture 1, § Background Topics) is the Kaplan et al. scaling-laws preprint of 2020-01-23 ([[Block 1 Slides]], p. 41). See [[Scaling Laws]].

### Where the course covers it

The syllabus lists attention and decoding in week 9, self-supervised learning and LLMs in week 11, and scaling laws in week 12 (CSCI 566 Syllabus). The Block 8 recap ends with: "Next block: how attention and decoding support autoregressive generation." (Block 8 Slides, p. 253)

## Related

- [[Tokenization]]
- [[Teacher Forcing]]: how training supplies the next input
- [[Recurrent Neural Networks (RNN)]]
- [[Transformers]]
- [[Image Captioning]]: generation conditioned on an image
- [[Post-Training]]
- [[KV Cache]]
- [[Loss Functions]]
- [[Scaling Laws]]
- [[Deep Learning]]
- [[Machine Learning Task Types]]: the base-model level of the task, experience, and performance table
- [[Agent Loop]]: the model inside the agent core
- [[In-Context Learning]]: a base model continues the pattern of its prompt
- Generative Models: autoregressive models are one of the five generative families on the Block 8 map. Training teaches them to "Predict the next token", and a sample comes from "Generate one token at a time" (Block 8 Slides, p. 247)

## Sources

- Lecture 1, § Deep Learning and § Background Topics
- [[Block 1 Slides]], pp. 41, 80–84
- [[Block 3 Slides]], pp. 56–58, 98–101
- [[Block 5 Slides]], pp. 19, 70–77, 79–85, 146–151
- CSCI 566 Syllabus, weeks 9, 11, 12
- [[F26-midterm-review-234p]], pp. 174, 191–194: the midterm recap of Transformer generation
- Block 8 Slides, pp. 247, 253: the map of generative families and the next-block note
