---
id: con-5pwxd7
type: topic
kind: concept
description: In-context learning changes a model's behavior only through its input, such as instructions, examples, tool results, or retrieved notes, while the weights stay fixed; the course compares it with fine-tuning.
tags:
  - machine-learning/cs566-deeplearning
aliases:
  - Context Only
  - Context-Only Update
  - ICL
  - Few-Shot Prompting
  - Fine-Tuning vs. In-Context Learning
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
  - "[[Updating LLMs]]"
---

> [!concept] Concept
> 4 sources · refreshed 2026-10-13 · #machine-learning/cs566-deeplearning
> Up: [[Updating LLMs]]

## Definition

In-context learning changes only the input to the model. The weights stay the same. The Sep 14 lecture listed it as "context only", one of four ways to update an LLM (Sep 14 Lecture Account, § Updating LLMs); see [[Updating LLMs]].

Block 7 puts it next to [[Fine-Tuning]] ("Examples in the Prompt or Updates to the Weights?", [[Block 7 Slides]], p. 229):

- In-context learning: "Put examples in the input prompt. The usual inference call keeps model parameters fixed."
- Fine-tuning: "Use training examples and loss to update selected parameters before later inference."
- "Both can change behavior, through different mechanisms." "Ask where the adaptation is stored."

From [[Block 3 Slides]], "Agent Context Can Change Without Backprop" (p. 216):

- "Model calls in one run normally reuse the same fixed weights."
- "Instructions, tool results, and retrieved notes enter the next call as input." The slide says the ACE paper (ICLR 2026) draws this same line.
- "Behavior can change from step to step while the parameters stay the same."
- "A separate fine-tuning job can still update weights. That is a different loop."

## Explanation

The 2020 node of the course timeline shows the idea at scale: GPT-3, 175B parameters, "tasks specified in text", "no gradient update" ([[Block 1 Slides]], p. 41, citing Brown et al., NeurIPS 2020).

Block 7 gives a small example with flower reviews ([[Block 7 Slides]], p. 231). The prompt holds "Fresh flowers." → Positive and "Arrived wilted." → Negative, then asks for "The bouquet was lovely." → ?. The slide says: "The prompt supplies task examples for this prediction." It also names the cost: "Examples use context space. Dense attention compares many token pairs."

Synthesis (general background; no course source in the vault states it):

- The prompt can hold instructions, a few worked examples (few-shot prompting), or documents that a retrieval step adds.
- The model uses this content for one request. The next request does not have it unless the application sends it again.

### Fine-tuning versus in-context learning

Block 7 asks: "Why would we ever bother with fine-tuning if it's so inefficient?" Its answer: "even for very large LMs, fine-tuning often beats in-context learning" ([[Block 7 Slides]], p. 232).

GPT-3 on two natural language inference benchmarks, validation accuracy in percent (p. 232, figure from arxiv.org/abs/2106.09685):

| Method | MNLI-m | RTE |
|---|---|---|
| GPT-3 Few-Shot | 40.6 | 69.0 |
| GPT-3 Fine-Tuned | 89.5 | 85.4 |

MNLI-m is the matched validation set of MultiNLI. RTE is Recognizing Textual Entailment. The slide gives the reason for the gap (p. 232):

- Few-shot: "GPT-3's context length is only 2048 tokens. So the MNLI-m setting above only uses 6 few-shot examples in total."
- Fine-tuned: "MNLI-m has 393,000 training examples and GPT-3 is fine-tuned for 2 epochs."

Synthesis: the few-shot model sees 6 examples, and the fine-tuned model trains on 393,000 examples twice. The gap is a case of the context budget limit below, not only a difference in method.

A 2023 study made a fair comparison (p. 233, figure from aclanthology.org/2023.findings-acl.779.pdf). Its finding: "In a fair comparison of fine-tuning (FT) and in-context learning (ICL), we find that FT outperforms ICL for most model sizes on RTE and MNLI." The setup in the table caption:

- Model sizes from 125M to 30B, for both approaches.
- 16 examples and 10 random seeds for both approaches.
- ICL uses the `gpt-3` pattern. FT uses pattern-based fine-tuning (PBFT), with checkpoints selected by in-domain performance.
- The table shows the difference in average out-of-domain performance between ICL and FT.
- A Welch's t-test colors each cell: blue where FT is significantly better, red where ICL is significantly better, no color where there is no significant difference.

Most colored cells are blue. A few cells are red: ICL with the 13B and 30B models against FT with the smallest models (p. 233). Open point: the extractor read the red cells as an RTE-only result, but the slide image shows red cells in the MNLI table too. Check the paper before stating which cells are significant.

The deck then qualifies the result: "At least this was the general wisdom in 2023. We might have a different story to tell since 2024" (p. 234). Open point: the slide does not say what changed in 2024.

The same GPT-3 table returns on p. 256, "A Restricted Space for Fine-Tuning". There it leads to a question about [[Parameter-Efficient Fine-Tuning]]: "Can useful adaptation fit inside a small update space?" Hypothesis: "Small update spaces can suffice on some tasks."

### Limits

Synthesis: this is the cheapest way to change behavior, and the easiest to undo. It has two limits:

- Context is a finite budget. Each added example or document uses part of it ([[Agent Skills]]; [[Block 1 Slides]], p. 94). GPT-3's 2048-token context held only 6 MNLI-m examples ([[Block 7 Slides]], p. 232).
- The change does not last. [[Agent Memory]] stores information between tasks and puts it back into context.

The observed context can also supply a training signal that does change weights: "The past can provide next-token training examples" ([[Block 3 Slides]], p. 218). That is [[Test-Time Training]], not a context-only update.

Synthesis: an [[Agent Skills|agent skill]] is a context-only update. It gives the agent a procedure without retraining the model ([[Block 1 Slides]], pp. 95, 142).

## Related

- [[Fine-Tuning]]: stores the adaptation in updated parameters instead of the prompt
- [[Parameter-Efficient Fine-Tuning]]
- [[Updating LLMs]]
- [[Agent Memory]]
- [[Agent Skills]]
- [[Test-Time Training]]
- [[LoRA]]
- [[Autoregressive Language Modeling]]: a base model continues the pattern of its prompt
- [[Tokenization]]: token counts set the context budget

## Sources

- [[Block 3 Slides]], pp. 216, 218
- [[Block 1 Slides]], pp. 41, 94, 95, 142
- Sep 14 Lecture Account, § Updating LLMs
- [[Block 7 Slides]], pp. 229, 231, 232, 233, 234, 256
