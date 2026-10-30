---
id: con-zx8yjj
type: topic
kind: concept
description: Tree of Thoughts (ToT) has a language model generate and evaluate intermediate thoughts as nodes of a tree and runs a search algorithm over that tree, adding lookahead and backtracking to left-to-right generation.
tags: [machine-learning/cs566-deeplearning]
aliases: [ToT, Test-time reasoning strategies, The Tree Moved Inside, System 1 and System 2, Dual-process theory]
created: 2026-09-28T00:00:00
updated: 2026-10-13T18:22:42
refreshed: 2026-10-13T18:22:42
status: stable
sources: ["[[Block 2 Slides]]"]
up: ["[[Chain-of-Thought Prompting]]"]
---

> [!concept] Concept
> 1 source · refreshed 2026-10-13 · #machine-learning/cs566-deeplearning
> Up: [[Chain-of-Thought Prompting]]

## Definition

Tree of Thoughts (ToT) adds a "System 2" control structure, tree search, to autoregressive LM generation ([[Block 2 Slides]], pp. 124–125). The LM generates intermediate "thoughts", evaluates them, and a search algorithm moves through the tree of thoughts. The slides follow Yao, S., Yu, D., Zhao, J., Shafran, I., Griffiths, T., Cao, Y., and Narasimhan, K. (2023), "Tree of thoughts: Deliberate problem solving with large language models", NeurIPS (pp. 121–133).

The slides are part of the optional detour "Tree Search Inside a Language Model" (pp. 113–114). See [[Chain-of-Thought Prompting]].

## Explanation

### The problem: limits of autoregressive generation

LMs were invented to generate text. People now use them to solve problems by generating "reasoning" processes such as chain-of-thought ([[Block 2 Slides]], p. 121). Generation has two limits (p. 121):

- Token-level decisions give no global exploration.
- One-by-one, left-to-right generation gives no local lookahead and no backtracking.

Game of 24 shows both limits. It is hard even for GPT-4 with CoT. With no lookahead, the model cannot tell whether a first token such as "5" is good. With no backtracking, a wrong first few tokens end the game. 60% of CoT samples fail after the first step (p. 122).

### System 1 and System 2

The slides frame the gap with Daniel Kahneman's *Thinking, Fast and Slow* ([[Block 2 Slides]], p. 123):

| | System 1 | System 2 |
| --- | --- | --- |
| Speed | Fast | Slow |
| Awareness | Subconscious, automatic | Conscious, effortful |
| Use | Everyday decisions | Complex decisions |
| Errors | Error prone | Reliable |

Autoregressive generation is analogous to System 1 (p. 123). A System 2 control structure, such as tree search, can augment it. The slide shows Newell, Shaw, and Simon's "Report on a General Problem-Solving Program" (P-1584, 30 December 1958, revised 9 February 1959) as the classical source of this idea (p. 125).

### How ToT differs from IO, CoT, and CoT-SC

IO prompting goes straight from input to output. CoT writes one chain. CoT-SC writes several chains and takes a majority vote. ToT branches at each thought, evaluates the branches, and continues from the promising ones ([[Block 2 Slides]], p. 126).

### The recipe: four questions

To apply ToT to a task, answer four questions ([[Block 2 Slides]], p. 127):

1. What is a thought?
2. How do you generate thoughts?
3. How do you evaluate thoughts?
4. How do you search?

### Three tasks

| Task | Input | Output | Thought | Generate | Evaluate | Search | ToT steps |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Game of 24 | 4 numbers | An equation that reaches 24 | An intermediate equation | "propose" prompt | "value" prompt (sure / likely / impossible) | BFS, depth 4, breadth ≤ 5 | 3 |
| Creative Writing | 4 random sentences | A 4-paragraph passage | A writing plan | "sample" | "vote" | BFS, depth 2, breadth 5 | 1 |
| Mini Crosswords (5x5) | 10 clues | 5x5 letters | A clue word | "propose" | "value" | DFS, depth 5–10, with backtracking and subtree pruning | 5–10 |

Sources: [[Block 2 Slides]], pp. 128, 130–132.

Game of 24 uses four numbers and + − × ÷ to reach 24. At each step the model combines two of the remaining numbers. Example: input 4 4 6 8, answer (6 − 4) × (4 + 8) = 24 (p. 122). The slides give BFS depth 4 on p. 128 and 3 steps with 3 intermediate equations on p. 132. They do not explain the difference.

Creative Writing asks for a coherent passage of 4 short paragraphs, each ending in a given sentence (p. 130).

### Results

Game of 24 success rate ([[Block 2 Slides]], p. 129):

| Method | Success |
| --- | --- |
| IO | 7.3% |
| CoT | 4.0% |
| CoT-SC (k=100) | 9.0% |
| ToT (b=1) | 45% |
| ToT (b=5) | 74% |

Mini Crosswords success rate, letter / word / game ([[Block 2 Slides]], p. 131):

| Method | Letter | Word | Game |
| --- | --- | --- | --- |
| IO | 38.7% | 14% | 0% |
| CoT | 40.6% | 15.6% | 1% |
| ToT | 78% | 60% | 20% |
| ToT + best state | 82.4% | 67.5% | 35% |
| ToT − pruning | 65.4% | 41.5% | 5% |
| ToT − backtracking | 54.6% | 20% | 5% |

The ablations show that backtracking and subtree pruning matter (p. 131).

Creative Writing: in a human coherency comparison, CoT beat ToT in 21 cases, the two were similar in 38, and ToT beat CoT in 41. ToT also scored higher than IO and CoT on GPT-4 coherency scores (p. 130).

### Benefits and summary

The slides state three benefits ([[Block 2 Slides]], p. 132):

- Modularity: generation, evaluation, and search strategies can change independently.
- Flexibility: it solves diverse problems under different resource constraints.
- A significant performance gain with no retraining of the LM.

The LM and tree search complement each other, as System 1 and System 2 do. LM reasoning gives flexible heuristics for search. Search adds deliberation and exploration to LM reasoning (p. 133). Future directions: harder problems that challenge state-of-the-art LMs such as GPT-4, better LMs for self-evaluation, and classical insights applied to frontier LM research (p. 133).

### Test-time reasoning in 2026

The slide "The Tree Moved Inside" sorts 2026 inference-time reasoning into three categories ([[Block 2 Slides]], p. 134):

| Category | What happens |
| --- | --- |
| One path | A trained reasoning model continues, checks, revises, and sometimes backtracks before it answers |
| Many leaves | Generate several complete answers, then vote on them or verify them |
| Partial tree | Branch, score, and prune before completion |

ToT belongs to the partial-tree category, and this category is still active (p. 134). GPT-5.6, Claude Opus 4.6, Gemini 3 Deep Think, and DeepSeek V4 all ship an adjustable reasoning control (p. 134). Value-guided search with a 14B generator, a 1.5B checker, and 64 generations scored 61.0% across four math contests. The full 671B DeepSeek-R1 scored 60.8% in one pass. The slide notes that this comparison is not compute matched (p. 134).

Synthesis: the categories map onto the methods above. One path is a CoT that the model learned to run, with backtracking inside the chain. Many leaves is the CoT-SC pattern. Partial tree is ToT. All three spend more compute at inference and leave the weights unchanged. [[Test-Time Training]] instead updates weights at inference.

## Related

- [[Chain-of-Thought Prompting]]: the one-chain baseline, with IO prompting and CoT-SC
- [[Autoregressive Language Modeling]]: the System 1 generation that ToT wraps
- [[World Models]]: another account of planning by search and of System 1 versus System 2
- [[Test-Time Training]]: a different way to use inference-time compute
- [[ReAct]]: reasoning steps grounded by tool observations

## Sources

- [[Block 2 Slides]], pp. 113–114, 121–134
