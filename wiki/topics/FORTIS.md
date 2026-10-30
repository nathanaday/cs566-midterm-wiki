---
id: ent-hykpxp
type: topic
kind: entity
description: FORTIS is the USC lab of CSCI 566 instructor Yue Zhao, and also the name of its 2026 benchmark for over-privilege in agent skills.
tags:
  - machine-learning/cs566-deeplearning
  - organization
aliases:
  - Fortis Lab
  - FORTIS benchmark
created: 2026-09-28T00:00:00
updated: 2026-10-13T18:22:42
refreshed: 2026-10-13T18:22:42
status: stable
sources:
  - "[[Block 1 Slides]]"
up:
  - "[[LLM Trustworthiness]]"
---

> [!entity] Entity
> 1 source · refreshed 2026-10-13 · #machine-learning/cs566-deeplearning · #organization
> Up: [[LLM Trustworthiness]]

## What it is

The name refers to two related things in [[Block 1 Slides]].

- **Fortis Lab**: the USC research lab led by the instructor, Yue Zhao, Assistant Professor of Computer Science. Its research audits and controls AI risk across deployment: anomaly and out-of-distribution detection in data, trust and robustness of foundation models, and runtime audit and control of agents (p. 4).
- **FORTIS benchmark**: "FORTIS: Benchmarking Over-Privilege in Agent Skills", Li et al., 2026 (arXiv:2605.09163) (pp. 142–143). It tests whether an agent picks the least authority a benign task needs.

## Facts

### The lab

- Projects include PyOD, PyGOD, TrustLLM, Aegis, agent-audit, and anywhere-agents. The slide reports 42M+ downloads and 22K+ GitHub stars (p. 5).
- The lab's name labels the slides of the deployment case study ([[Block 1 Slides]], pp. 101–170).

### The benchmark

- Two stages: pick the minimal skill, then pick the minimal tools inside it. At each stage, failure rate = over-privilege rate + no-action rate (p. 144).
- Scale: 3 domains (email, e-commerce, filesystem), 60 skills, 174 tools, 2,143 queries, 5 privilege levels. The model does not see the levels (p. 145).
- Example: asked to check unread email and list folders with an observe-only skill, GPT-5.4 used two mailbox-wide tools. The result looked the same, but the access was wider (p. 146).

End-to-end least-privilege success (p. 148):

| Model | Task 1 (skill) | End to end |
| --- | --- | --- |
| Claude Opus 4.7 | 54.8% | 14.3% |
| Qwen 3.6-Max | 51.3% | 13.3% |
| Claude Sonnet 4.6 | 49.5% | 11.1% |
| Gemini 3.1-Pro | 47.7% | 10.8% |
| Kimi K2.6 | 44.0% | 10.3% |
| GPT-5.4-mini | 43.5% | 8.6% |
| Gemini 3 Flash | 46.2% | 7.8% |
| GPT-5.4 | 42.2% | 6.4% |

The slide says the range covers "all 10 frontier models" but shows 8.

Other results (pp. 149–151):

- For 7 of 10 models, 92–100% of misses take too much authority.
- Clear wording gives a 19–51% failure rate. "Convenience" wording gives 75–98%. "Boundary" wording gives 71–96%.
- With the full `SKILL.md` in context, the failure rate stays at 45–67%.
- Scale does not fix it. "Permission boundaries cannot be delegated to the model's own reading of its instructions" (p. 151).

### Other lab work in the deck

| Work | Role | Citation on the slide |
| --- | --- | --- |
| Surface heuristics in defense fine-tuning | F1 false refusal | Li et al., ACL 2026, arXiv:2601.07185 |
| The Autonomy Tax | F2 stall or timeout | Li and Zhao, arXiv:2603.19423 |
| Cat-DPO | control at training time | Yang et al., arXiv:2604.17299 |
| Agent Audit | control before deployment; 57 rules, 95.24% recall on 42 vulnerabilities | Zhang et al., arXiv:2603.22853 |
| AEGIS | control at runtime; 14 frameworks, 48/48 attacks blocked | Yuan et al., arXiv:2603.12621 |

Sources: [[Block 1 Slides]], pp. 113, 125, 128, 153, 161–165. The slides state that none of the controls fixes the failures (p. 168).

## Related

- Source of the case study in [[Deployment Failure Modes]]
- Measures the skill layer described in [[Agent Skills]]
- Evidence for [[Shortcut Learning]] in defended models
- The lab also maintains [[TrustLLM]] (p. 5)
- Synthesis: likely the unnamed 2026 "least-privilege benchmark from our lab" in [[Evolution of Machine Learning]] ([[Block 1 Slides]], p. 46)

## Sources

- [[Block 1 Slides]], pp. 4–5, 46, 101–171
