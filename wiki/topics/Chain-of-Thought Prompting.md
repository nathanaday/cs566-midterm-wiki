---
id: con-39gvmh
type: topic
kind: concept
description: Chain-of-thought (CoT) prompting puts worked examples with intermediate steps into a few-shot prompt, so that a large language model writes its own chain of steps before its final answer.
tags: [machine-learning/cs566-deeplearning]
aliases: [CoT, Chain of Thought, CoT prompting, Self-consistency, CoT-SC, Input-output prompting, IO prompting]
created: 2026-09-28T00:00:00
updated: 2026-10-13T18:22:42
refreshed: 2026-10-13T18:22:42
status: stable
sources: ["[[Block 2 Slides]]"]
up: ["[[Large Language Models]]"]
---

> [!concept] Concept
> 1 source · refreshed 2026-10-13 · #machine-learning/cs566-deeplearning
> Up: [[Large Language Models]]

## Definition

Chain-of-thought (CoT) prompting adds chain-of-thought demonstrations to a few-shot prompt. With these demonstrations, a large enough LM generates its own chain of intermediate steps before the answer ([[Block 2 Slides]], p. 115). The slides cite Wei et al., "Chain-of-thought prompting elicits reasoning in large language models", NeurIPS, on each CoT slide (pp. 115–120).

## Explanation

### Where the course puts it

The deck puts CoT in a detour titled "Tree Search Inside a Language Model", inside the classical ML block. The link to decision trees is an analogy about search (what happens when a search can revisit), not a property of trees. The detour is not required for the midterm ([[Block 2 Slides]], pp. 113–114).

### Example

The cafeteria apples question ([[Block 2 Slides]], p. 116):

- Standard prompting: the model answers 27. This is wrong.
- CoT prompting: the model reasons 23 − 20 = 3, then 3 + 6 = 9, and answers 9. This is correct.

### Benefits

The slides list four benefits ([[Block 2 Slides]], p. 117):

- It splits a multi-step problem into steps, so a problem with more steps gets more computation.
- It makes the model's response interpretable.
- It can apply to any multi-step task.
- It needs only CoT examples in the prompt.

### Robustness and scale

- CoT is robust to different annotators, to annotators with no ML background, to the type, order, and number of exemplars, and to different LMs (LaMDA, GPT-3, PaLM). Prompt engineering still improved performance significantly in many cases ([[Block 2 Slides]], p. 118).
- The gain over standard prompting holds across the number of few-shot exemplars on GSM8K, MultiArith, Sports Understanding, Coin Flip, and Last Letter Concatenation (p. 119).
- CoT is an emergent ability of model scale. It gives larger gains on more complex problems. With GPT-3 175B and PaLM 540B, it compares favorably to the prior state of the art (p. 120). Figure 4 of Wei et al. shows CoT solve rates on GSM8K, SVAMP, and MAWPS that rise with model scale for LaMDA, GPT, and PaLM (p. 120).

### Baselines and variants

The Tree of Thoughts slides compare CoT with a simpler baseline and a sampling variant ([[Block 2 Slides]], p. 126):

| Method | What the LM does |
| --- | --- |
| Input-output (IO) prompting | Goes directly from input to output, with no intermediate steps |
| CoT | Writes one chain of intermediate steps, then the output |
| CoT with self-consistency (CoT-SC) | Runs several CoT chains and picks the output by majority vote |

Results on two search-heavy tasks:

| Method | Game of 24 success | Mini Crosswords (letter / word / game) |
| --- | --- | --- |
| IO | 7.3% | 38.7% / 14% / 0% |
| CoT | 4.0% | 40.6% / 15.6% / 1% |
| CoT-SC (k=100) | 9.0% | — |

Sources: [[Block 2 Slides]], pp. 122, 129, 131.

Synthesis: on these tasks CoT gains little over IO, and on Game of 24 it scores lower. [[Tree of Thoughts]] explains why.

### Limits

CoT is one example of LMs solving problems by generating "reasoning" processes. The LM still makes token-level decisions one by one, left to right. It has no global exploration and no local lookahead or backtracking ([[Block 2 Slides]], p. 121). On Game of 24, 60% of CoT samples fail after the first step (p. 122). See [[Tree of Thoughts]] for the full argument and for the 2026 test-time reasoning categories.

## Related

- [[Tree of Thoughts]]: adds tree search over thoughts
- [[ReAct]]: interleaves reasoning steps with tool actions and observations
- [[Autoregressive Language Modeling]]: the left-to-right generation that CoT runs on
- [[In-Context Learning]]: CoT works through examples in the prompt, with no weight change

## Sources

- [[Block 2 Slides]], pp. 113–122, 126, 129, 131
