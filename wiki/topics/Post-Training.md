---
id: con-y7b5bj
type: topic
kind: concept
description: Post-training turns a pretrained base model into an assistant by training on human demonstrations and then on preferences between answers.
tags:
  - machine-learning/cs566-deeplearning
aliases:
  - Instruction Tuning
  - Alignment Training
created: 2026-09-28T00:00:00
updated: 2026-10-13T18:22:42
refreshed: 2026-10-13T18:22:42
status: stable
sources:
  - "[[Block 1 Slides]]"
  - "Lecture 1"
up:
  - "[[Large Language Models]]"
---

> [!concept] Concept
> 2 sources · refreshed 2026-10-13 · #machine-learning/cs566-deeplearning
> Up: [[Large Language Models]]

## Definition

Post-training turns a pretrained base model into an assistant ([[Block 1 Slides]], p. 86, pipeline redrawn after Ouyang et al., NeurIPS 2022):

```
pretraining (continue text) → demonstrations (imitate desired answers) → preferences (prefer one acceptable answer) → assistant behavior
```

"Different training data rewards different behavior." "Demonstrations teach form; preferences rank answers" (p. 86).

## Explanation

### Base model vs. demonstration

For the prompt "Explain the moon landing to a 6-year-old in a few sentences.":

- A base model wrote more prompts of the same form: "Explain the theory of gravity to a 6 year old." and "Explain the big bang theory to a 6 year old." ([[Block 1 Slides]], p. 84)
- A human demonstration gives the desired answer: "A rocket carries astronauts from Earth. They land, explore, and collect moon rocks. The crew returns safely to Earth." "Same prompt. The training signal now shows the desired answer." ([[Block 1 Slides]], p. 85)

### A chat is one token sequence

System, user, and assistant turns are joined into one sequence, with special tokens around each turn, such as `<|start_header_id|>user<|end_header_id|>` and `<|eot|>` ([[Block 1 Slides]], p. 87, adapted from Sean Welleck, CMU 11-711). See [[Tokenization]].

### Place in the course

- The assistant level of the task, experience, and performance table has the task "follow user intent", the experience "demonstrations + preferences", and the measure "helpfulness / safety / preference evals" (Lecture 1, § Broad ML Tasks). See [[Machine Learning Task Types]].
- The [[Evolution of Machine Learning]] timeline marks 2022-03-04 (Ouyang et al.), when a 1.3B instruction-tuned model was preferred to 175B GPT-3 ([[Block 1 Slides]], p. 42).

Synthesis: post-training changes the data, not the next-token objective. The same objective then rewards following instructions instead of continuing text. This explains why a base model and an assistant built on it act differently on the same prompt.

## Related

- [[Autoregressive Language Modeling]]
- [[Tokenization]]
- [[Machine Learning Task Types]]
- [[Evolution of Machine Learning]]
- [[Agent Loop]]
- [[Updating LLMs]]: other ways to change a model after pretraining

## Sources

- [[Block 1 Slides]], pp. 42, 83–87
- Lecture 1, § Broad ML Tasks
