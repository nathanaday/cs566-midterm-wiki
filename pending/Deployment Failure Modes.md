---
id: con-kytbnj
type: topic
kind: concept
description: "Three failures that deployed LLM agents show on benign input with no attacker: false refusal (training), stall or timeout (execution), and excess privilege (skill layer), from the Week 1 FORTIS case study."
tags:
  - machine-learning/cs566-deeplearning
aliases:
  - False Refusal
  - Autonomy Tax
  - Excess Privilege
  - Agent Over-Privilege
created: 2026-09-28T00:00:00
updated: 2026-10-13T18:22:42
refreshed: 2026-10-13T18:22:42
status: stable
sources:
  - "[[Block 1 Slides]]"
  - "Lecture 1"
  - "CSCI 566 Syllabus"
up:
  - "[[LLM Trustworthiness]]"
---

> [!concept] Concept
> 3 sources · refreshed 2026-10-13 · #machine-learning/cs566-deeplearning
> Up: [[LLM Trustworthiness]]

## Definition

The lecture separates two questions (Lecture 1, § Part 3 of 4; [[Block 1 Slides]], p. 101):

- Can the model do the task?
- Does the deployed system keep behaving?

It names three failure modes. All three occur after deployment, on benign input, with no attacker ([[Block 1 Slides]], pp. 101, 108):

| # | Layer | Failure | Boundary | Amplifier | Number |
| --- | --- | --- | --- | --- | --- |
| F1 | Training | False refusal | prompt → model | shortcut training | 6% → 90% false refusal |
| F2 | Execution | Stall or timeout | model → agent loop | repeated retries | 13% → 99% timeout |
| F3 | Skill layer | Excess privilege | request → skill or tool | limits stated only in text | 6.4%–14.3% least-privilege success |

## Explanation

The case study comes from the instructor's lab ([[FORTIS]]). It follows one benign request, "Find the quarterly report in the documents folder", through all three failures. The slide says: "A local shortcut becomes a deployment-level failure. No attacker is required" ([[Block 1 Slides]], p. 103).

"Defended" means a model with extra prompt-injection or agent-safety fine-tuning on top of normal alignment (StruQ, SecAlign, Meta SecAlign), or a model behind a hosted guard (ProtectAIv2, LakeraGuard, PromptGuard2, FMOPS, Deepset). F1 and F2 test these defenses. F3 tests frontier models with no added defense ([[Block 1 Slides]], pp. 109–110).

### F1: false refusal

Defense fine-tuning learns surface cues (position, trigger token, topic) instead of intent. See [[Shortcut Learning]]. Three stress tests show it ([[Block 1 Slides]], pp. 113–123):

- A benign task moved to the second position: refusal goes from 6% to 90% (Llama-3 + StruQ, MMLU) (p. 115).
- One trigger token such as "sudo" added: refusal rises by up to 49.4 points (p. 116). Removing the token lowers refusal again (p. 123).
- Benign reasoning outside the training topics: accuracy drops by up to 40% (pp. 117–118).

Production example: in Feb 2024 a safety-tuned Gemini over-refused benign prompts, and Google paused image generation ([[Block 1 Slides]], p. 112).

### F2: stall or timeout

The root is the same as F1. The agent loop amplifies it. The model refuses at step 1, the agent retries the same state, and the run reaches its 10-turn cap with no final answer ([[Block 1 Slides]], pp. 125, 129). The slides call the gap between F1 and F2 "the autonomy tax" (p. 138; Li and Zhao, arXiv:2603.19423, p. 125).

- On 97 benign AgentDojo tasks, the best baseline (Base-Llama-3) timed out on 13% of tasks. The worst defended model (Mistral + SecAlign) timed out on 99% (pp. 130–132).
- Defended models failed at step 1 on 47–77% of benign tasks, against 3% for the base model. This happens before any tool result returns (p. 133).
- For StruQ and SecAlign, the attack detection rate fell 45–56 points, the benign false-positive rate rose 25–71 points, and bypass by obfuscated attacks rose from 14% to 81–86%. The slide says: "These two defenses lose both safety and utility" (p. 135).

Production example: in Mar 2025 the Cursor coding agent refused mid-task after about 750–800 lines ([[Block 1 Slides]], p. 126).

### F3: excess privilege

"Least privilege is the narrowest sufficient authority, not the shortest plan" ([[Block 1 Slides]], p. 139). The slides use a ladder: L0 observe, L1 read, L2 modify, L3 execute, L4 bulk or admin.

The [[FORTIS]] benchmark scores two choices: which skill, and which tools inside the skill (pp. 144–145). Results (pp. 147–150):

- End-to-end least-privilege success is 6.4%–14.3% across frontier models. The best is Claude Opus 4.7.
- When models miss, they take more authority, not less. For 7 of 10 models, 92–100% of misses are over-reach.
- Wording alone changes the failure rate: 19–51% with clear wording, 75–98% with "convenience" wording.
- The failure rate stays at 45–67% when the model gets the full `SKILL.md` with its limits. "Stated limits behave like advisory text" (p. 150).

The task still succeeds, so casual use does not reveal the problem (p. 142). Production example: in Jul 2025, Replit's AI agent wiped a live production database during a code freeze (p. 140).

### Controls proposed, not fixes

| Failure | Control | Time | Result on the slide |
| --- | --- | --- | --- |
| F1 | Cat-DPO: per-category preference optimization | training | best on every metric tested for Alpaca-7B; "Direction, not a fix for the Autonomy Tax" |
| F2, F3 | AEGIS: firewall before tool execution | runtime | 48/48 curated attacks blocked; 1.2% false positives; 8.3 ms median latency |
| F3 | Agent Audit: static analysis of agent code | before deployment | 40 of 42 known vulnerabilities found |

Sources: [[Block 1 Slides]], pp. 153, 160–165. The slides say: "Evidence narrows uncertainty; it does not certify deployment safety" (p. 167), and "none of these fixes the failures we just saw" (p. 168).

### Why it matters

A model that passes capability tests can still fail as a deployed system. The slides cite the Berkeley MAST study of 1,642 multi-agent traces: all 14 cataloged failure modes were non-adversarial. They also cite a Gartner forecast that over 40% of agentic-AI projects will be canceled by end of 2027, for reasons that do not include attacks ([[Block 1 Slides]], p. 106). The thesis: "agents fail not only because of attackers; training and system-design choices create their own failure modes" (p. 107).

The slides settle three questions:

- Shortcut learning does explain false refusal. Three stress tests and a causal check show it (pp. 113–123).
- Stall or timeout is not a loop that fails to converge. The loop repeats one refusal until the turn cap, because each retry sends the same state (pp. 125, 129, 132).
- Excess privilege is not only a loose allow check on a tool call ([[Agent Loop]]). The slides place it earlier, where the agent chooses the skill and tools (pp. 139, 143).

Synthesis: F1 matches the "exaggerated safety" dimension in [[TrustLLM]], which found that Llama2-7b refused 57% of harmless prompts ([[Block 1 Slides]], p. 199). The deck presents TrustLLM as the next step: from studying three failures to measuring many trust dimensions across models (p. 171).

## Related

- [[Shortcut Learning]]
- [[FORTIS]]
- [[Agent Skills]]
- [[Agent Loop]]
- [[ReAct]]
- [[TrustLLM]]
- [[LLM Trustworthiness]]
- [[What Counts as Solved]]

## Sources

- [[Block 1 Slides]], pp. 101–171, 199
- Lecture 1, § Part 3 of 4 and § Shortcut Learning
- CSCI 566 Syllabus, week 1 row: "agent security and trustworthy AI"
