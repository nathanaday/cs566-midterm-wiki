---
id: con-g6knfz
type: topic
kind: concept
description: ReAct is an agent pattern that repeats Thought, Action, and Observation, so that each tool result grounds the next reasoning step.
tags:
  - machine-learning/cs566-deeplearning
aliases:
  - Reasoning and Acting
  - Thought-Action-Observation
created: 2026-09-28T00:00:00
updated: 2026-10-13T18:22:42
refreshed: 2026-10-13T18:22:42
status: stable
sources:
  - "Lecture 1"
  - "[[Block 1 Slides]]"
up:
  - "[[Agent Loop]]"
---

> [!concept] Concept
> 2 sources · refreshed 2026-10-13 · #machine-learning/cs566-deeplearning
> Up: [[Agent Loop]]

## Definition

ReAct is a loop of Thought → Action → Observation, repeated. Reasoning and acting correct each other (Lecture 1, § Reasoning and Acting Fail Differently; [[Block 1 Slides]], p. 91). The slides cite Yao et al., ICLR 2023 (arXiv:2210.03629).

## Explanation

### Reasoning and acting fail in different ways

| Pattern | Sequence | Result |
| --- | --- | --- |
| Reason only | wrong fact → more reasoning → wrong answer | Errors compound with no grounding |
| Act only | search → observations → no synthesis | Actions happen, but nothing is made of them |
| ReAct | Thought → Action → Observation → repeat | Reasoning and acting correct each other |

Sources: Lecture 1, § Reasoning and Acting Fail Differently; [[Block 1 Slides]], p. 91.

### Example: an observation breaks a wrong premise

Question: "Besides the Apple Remote, what other device can control Front Row?" ([[Block 1 Slides]], p. 92, from Yao et al., Fig. 1)

- Reason only: the model assumes the Apple Remote was made for Apple TV and answers about Apple TV. "Wrong premise persists."
- ReAct: the model runs `Search[Apple Remote]`. The observation names the "Front Row media center" and "keyboard function keys". The model corrects its path: "search, observe, correct."

### Example: a trajectory recovers

The instructor injected the observations in steps 3 and 5 (Lecture 1, § A Real Trajectory Recovers; [[Block 1 Slides]], p. 93, adapted from Shunyu Yao, UC Berkeley LLM Agents MOOC, Fall 2024).

| # | Step | Content |
| --- | --- | --- |
| 1 | Thought | Need current market capitalization for Apple, Nvidia, and Microsoft. |
| 2 | Action | `search(current market capitalization: Apple, Nvidia, Microsoft)` |
| 3 | Observation | nothing found! (injected) |
| 4 | Recovery | Search each company individually; start with Apple. |
| 5 | Observation | 'price': 180.75 (injected) |
| 6 | Recovery | Price is not market cap → search shares outstanding |

Synthesis: the agent recovers twice. At step 4 it splits a query that returned nothing. At step 6 it sees that a share price is not a market capitalization. Both sources end at step 6, with no final answer.

### Where observations help, and where they do not

Synthesis: an observation after each action grounds the next thought. This limits the compounding errors of reason-only systems. Recovery also needs the model to notice a wrong kind of result, not only an empty one.

Observations do not help when the model refuses before it acts. In the stall or timeout failure, a defense-trained agent fails at step 1 of a benign task, before any external content arrives. Each retry meets the same refusal until the turn cap ([[Block 1 Slides]], pp. 125, 132–133). The study behind these slides ran its agents under the ReAct framework (p. 130). See [[Deployment Failure Modes]].

### On the timeline

The [[Evolution of Machine Learning]] timeline marks 2022-10-06 (Yao et al.): "Reasoning + actions + observations interleave" ([[Block 1 Slides]], p. 43).

## Related

- [[Agent Loop]]: the system that runs this pattern
- [[Deployment Failure Modes]]
- [[Evolution of Machine Learning]]

## Sources

- Lecture 1, § Reasoning and Acting Fail Differently and § A Real Trajectory Recovers
- [[Block 1 Slides]], pp. 43, 91–93, 125, 130, 132–133
