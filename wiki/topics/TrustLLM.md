---
id: ent-by1dtk
type: topic
kind: entity
description: TrustLLM is a benchmark and toolkit that measures LLM trustworthiness across six tested dimensions on 16 models and 30 datasets (Sun et al., ICML 2024).
tags:
  - machine-learning/cs566-deeplearning
  - dataset
aliases:
  - TrustEval
  - TrustGen
created: 2026-09-28T00:00:00
updated: 2026-10-13T18:22:42
refreshed: 2026-10-13T18:22:42
status: stable
sources:
  - "[[Block 1 Slides]]"
  - "Lecture 1"
up:
  - "[[LLM Trustworthiness]]"
---

> [!entity] Entity
> 2 sources · refreshed 2026-10-13 · #dataset · #machine-learning/cs566-deeplearning
> Up: [[LLM Trustworthiness]]

## What it is

TrustLLM is a benchmark and toolkit for the trustworthiness of large language models ([[Block 1 Slides]], p. 5). It is the second case study of Part 3 of the Week 1 lecture (p. 172). The deck cites Sun et al., ICML 2024 (arXiv:2401.05561) (p. 171). Project site: [TrustLLM](https://trustllmbenchmark.github.io/TrustLLM-Website/) (p. 172).

## Facts

- More than 60 researchers from more than 40 institutions work on it (p. 173). The slides name Lichao Sun (Lehigh) and Yue Huang (Notre Dame) (p. 174).
- The motivation: phones, cars, medicine, and databases have standard tests; LLMs do not (p. 175).
- The project has four parts: principles (eight facets of trust), a survey of 600+ papers, a benchmark (16 LLMs, 30+ datasets, six dimensions), and insights (p. 180). See [[LLM Trustworthiness]].

### Benchmark

- 30 datasets, existing and new. New ones include Jailbreak Trigger (1,300 prompts), AdvInstruction, Privacy Awareness, and Opinion Pairs. Existing ones include TruthfulQA, AdvGLUE, ETHICS, and Do-Not-Answer (pp. 184–185).
- Classification and generation tasks. Evaluation uses scripts (such as keyword matching), a Longformer classifier, or GPT-4 or ChatGPT as judge. Metrics include accuracy, refuse-to-answer (RtA), attack success rate, and micro F1 (pp. 184, 186).
- 16 models: GPT-3.5-turbo, GPT-4, ERNIE-3.5-turbo, PaLM 2, ChatGLM2-6b, Vicuna 7b/13b/33b, Llama2 7b/13b/70b, WizardLM-13b, Koala-13b, Baichuan-13b, Oasst-12b, and Mistral-7b (p. 187).

### Sub-tasks by dimension

| Dimension | Sub-tasks |
| --- | --- |
| Truthfulness | misinformation, hallucination, sycophancy, adversarial factuality |
| Safety | jailbreak, toxicity, misuse, exaggerated safety |
| Fairness | stereotype, disparagement, preference |
| Robustness | natural noise, out-of-distribution detection and generalization |
| Privacy | privacy awareness, privacy leakage |
| Machine ethics | implicit ethics, explicit ethics, emotional awareness |

Sources: [[Block 1 Slides]], pp. 184, 191–196.

### Jailbreak evaluation

- Definition: "an attempt to elicit an on-topic response to a prompt P for restricted behavior by submitting a modified prompt P'" (p. 188).
- The Jailbreak Trigger dataset groups attacks as prefix injection, sensitive content removal (encoded strings), style constraints, persona and scenario, and distractors (p. 189).
- A Longformer classifier labels each answer as a refusal or not. The metric RtA is the percentage of answers that refuse (p. 190).

### Findings

- "No utility, no trustworthiness." Trust rankings often follow utility leaderboards such as MT-Bench (p. 199).
- Many models are over-aligned: "Llama2-7b obtained a 57% of refusing to answer when the given prompt is not harmful" (p. 199).
- Proprietary models generally lead, but "Llama2, an open-source LLM, surpasses proprietary LLMs in trustworthiness in many tasks" (p. 200).
- Openness of models and of trust technology helps trustworthiness (p. 200).

A ranking card of all 16 models by sub-task is on p. 197.

### TrustEval and TrustGen

- **TrustEval** is "a modular and extensible toolkit for comprehensive trust evaluation of generative foundation models". It builds datasets, generates responses from LLMs, vision-language models, and text-to-image models, and judges them to produce reports and leaderboards (pp. 202–203). Repository: [TrustEval-toolkit](https://github.com/TrustGen/TrustEval-toolkit).
- **TrustGen** extends the work to generative foundation models (Huang et al., ICLR 2026, arXiv:2502.14296; [site](https://trustgen.github.io/)). It has three thrusts: standard guidelines, dynamic evaluation, and in-depth discussion of challenges, including trade-offs between performance and trust (pp. 204–206).

## Related

- Defines the dimensions in [[LLM Trustworthiness]]
- A project of the instructor's lab, [[FORTIS]] (p. 5)
- Follows the case study in [[Deployment Failure Modes]]; its exaggerated-safety dimension matches false refusal

## Sources

- [[Block 1 Slides]], pp. 5, 171–206
- Lecture 1 (a link to the project site only)
