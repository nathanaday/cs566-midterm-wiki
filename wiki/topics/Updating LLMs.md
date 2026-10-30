---
id: con-51evgg
type: topic
kind: concept
description: "The ways to change an LLM's behavior after pretraining, compared by what state changes: context tokens, a LoRA adapter, test-time-trained weights, or an agent memory record."
tags:
  - machine-learning/cs566-deeplearning
aliases:
  - LLM Adaptation
  - Ways to Update an LLM
created: 2026-09-28T00:00:00
updated: 2026-10-13T18:22:42
refreshed: 2026-10-13T18:22:42
status: stable
sources:
  - "[[Block 3 Slides]]"
  - "[[Block 1 Slides]]"
  - "Sep 14 Lecture Account"
  - "[[Block 7 Slides]]"
up:
  - "[[Large Language Models]]"
---

> [!concept] Concept
> 4 sources · refreshed 2026-10-13 · #machine-learning/cs566-deeplearning
> Up: [[Large Language Models]]

## Definition

Updating an LLM means changing its behavior after pretraining, for example to add knowledge, a skill, or a user preference. The Sep 14 lecture listed four ways: LoRA, context only, agent memory, and test-time training (Sep 14 Lecture Account, § Updating LLMs). [[Block 3 Slides]] compares them and asks one question of each: "What changes?" (pp. 216–223).

| Way | What changes, per the slide (p. 223) | Backprop runs? |
| --- | --- | --- |
| [[In-Context Learning\|Context only]] | "context tokens; θ stays fixed" | No (p. 216) |
| [[LoRA]] | "adapter A, B; base W stays fixed" | Yes, through the frozen layers (p. 217) |
| [[Test-Time Training\|TTT]] | "selected weights; θ → θ'" | Yes, on the observed context (pp. 218–220) |
| [[Agent Memory]] | a stored record read back into context; θ fixed | No (pp. 221–222) |

The slide's table has three rows. It puts the memory example with context tokens, as a case where θ stays fixed: "This memory example keeps θ fixed" (p. 223).

The user placed the lecture's comparison on a slide numbered 229 (Sep 14 Lecture Account, § Updating LLMs). In this deck it is on pp. 216–223; the lecture version may have had different numbering.

## Explanation

The slides draw the line between training and agent runs. In training, a loss sends gradients backward and the optimizer step persists. In an agent run, model calls reuse the same fixed weights, and instructions, tool results, and retrieved notes enter the next call as input. "Behavior can change from step to step while the parameters stay the same" ([[Block 3 Slides]], p. 216).

LoRA is one [[Parameter-Efficient Fine-Tuning]] method. Others train [[Adapters]], a prefix, or only the top layers ([[Block 7 Slides]], p. 236). Block 7 agrees with the LoRA row above: PEFT "reduces parameter updates but still requires full backpropagation" (p. 266). [[HyperTuning]] instead uses a hypermodel to generate task-specific parameters "in a single forward pass" (p. 266).

A wider comparison (general background, not from a course source):

| Way | Weights change? | Change lasts after the task? | Main cost |
| --- | --- | --- | --- |
| Context only | No | No | context tokens on each request |
| LoRA | Yes, as an adapter | Yes | one training run on a dataset |
| TTT | Yes, for that input | Usually no | gradient steps at inference time |
| Agent memory | No | Yes | storage and retrieval |

Synthesis: two of the ways change the input ([[In-Context Learning|context only]] and [[Agent Memory|agent memory]]). The other two change the weights ([[LoRA]] and [[Test-Time Training|TTT]]).

- A change to the input is cheap and easy to undo. It uses part of the finite context budget on each request ([[Agent Skills]]; [[Block 1 Slides]], p. 94).
- A change to the weights needs [[Backpropagation]] and gradient steps. It uses no context, but it pays the memory cost of the backward pass: stored activations grow with depth and batch size ([[Block 3 Slides]], p. 215).

[[Post-Training]] also changes the weights, with demonstrations and preferences ([[Block 1 Slides]], pp. 85–86).

## Related

- [[In-Context Learning]]
- [[LoRA]]
- [[Parameter-Efficient Fine-Tuning]]
- [[Adapters]]
- [[HyperTuning]]
- [[Test-Time Training]]
- [[Agent Memory]]
- [[Backpropagation]]
- [[Post-Training]]
- [[Agent Skills]]: context is a finite budget

## Sources

- [[Block 3 Slides]], pp. 215–223
- [[Block 1 Slides]], p. 94 (context budget) and pp. 85–86 (post-training)
- Sep 14 Lecture Account, § Updating LLMs
- [[Block 7 Slides]], pp. 236, 266
- The wider comparison table is general background, not from a course source.
