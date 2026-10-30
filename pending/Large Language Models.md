---
id: doc-hdr4c4
type: topic
kind: concept
description: "The CSCI 566 topics on large language models: how they predict text, how they are post-trained and updated, prompted to reason, run as agents, grounded in retrieval, and judged for trust."
tags: [machine-learning/cs566-deeplearning]
aliases: [LLM, LLMs]
created: 2026-10-13T18:20:10
updated: 2026-10-13T18:22:42
refreshed: 2026-10-13T18:22:42
status: stable
sources: ["[[Autoregressive Language Modeling]]", "[[Post-Training]]", "[[Updating LLMs]]", "[[Chain-of-Thought Prompting]]", "[[Agent Loop]]", "[[Retrieval-Augmented Generation]]", "[[LLMs and Graphs]]", "[[LLM Trustworthiness]]", "[[LLM Election Simulation]]"]
up: ["[[CS566-DeepLearning]]", "[[Machine Learning]]"]
---

> [!concept] Concept
> 9 sources · refreshed 2026-10-13 · #machine-learning/cs566-deeplearning
> Up: [[CS566-DeepLearning]] · [[Machine Learning]]

## Definition

A large language model is a neural network trained to predict text, which CSCI 566 then teaches to adapt, to prompt for reasoning, to run as an agent, to ground in retrieved documents, and to judge for trust ([[Autoregressive Language Modeling]]). This page gathers those topics; each linked topic holds the claims and their citations.

## Explanation

### How they work

- [[Autoregressive Language Modeling]]: A language model writes the probability of a token sequence as a product of next-token probabilities, and it generates text by predicting a token, appending it, and repeating.
- [[Post-Training]]: post-training turns a pretrained base model into an assistant by training on human demonstrations and then on preferences between answers.

### Adapting them

- [[Updating LLMs]]: the ways to change an LLM's behavior after pretraining, compared by what state changes: context tokens, a LoRA adapter, test-time-trained weights, or an agent memory record.

### Reasoning and acting

- [[Chain-of-Thought Prompting]]: chain-of-thought (CoT) prompting puts worked examples with intermediate steps into a few-shot prompt, so that a large language model writes its own chain of steps before its final answer.
- [[Agent Loop]]: an agent is a model choosing tools in a loop: the agent core plans, tool adapters act on the environment, and the runtime returns each result as an observation that starts the next turn.

### Grounding in documents and graphs

- [[Retrieval-Augmented Generation]]: retrieval-augmented generation (RAG) answers a question in two steps: a retrieval step finds the relevant document passages, and an LLM reads them and writes the answer, so the answer can only be as complete as the retrieved evidence.
- [[LLMs and Graphs]]: how CSCI 566 combines large language models with graphs: the LLM as enhancer or as predictor, worked through a paper-classification example, four system families (features, foundation, GraphRAG, tool agent), and the rules it gives for testing what graph context adds.

### Trust

- [[LLM Trustworthiness]]: LLM trustworthiness is a model's level of truthfulness, safety, fairness, robustness, privacy, machine ethics, transparency, and accountability, as defined by the TrustLLM framework.

### Research examples

- [[LLM Election Simulation]]: the presenters' study in CSCI 566 Block 7, shown as an optional research example: LLMs get demographic personas and vote, the votes are summed into state-level U.S.

## Related

- [[CS566-DeepLearning]]: the broader subject
- [[Machine Learning]]: the broader subject

## Sources

- [[Autoregressive Language Modeling]]
- [[Post-Training]]
- [[Updating LLMs]]
- [[Chain-of-Thought Prompting]]
- [[Agent Loop]]
- [[Retrieval-Augmented Generation]]
- [[LLMs and Graphs]]
- [[LLM Trustworthiness]]
- [[LLM Election Simulation]]
