---
id: con-vwrfpn
type: topic
kind: concept
description: An agent skill is a folder with a SKILL.md file that a person writes to give an agent a procedure without retraining the model, loaded into context in stages.
tags:
  - machine-learning/cs566-deeplearning
aliases:
  - Agent Skill
  - SKILL.md
  - Skills
created: 2026-09-28T00:00:00
updated: 2026-10-13T18:22:42
refreshed: 2026-10-13T18:22:42
status: stable
sources:
  - "[[Block 1 Slides]]"
up:
  - "[[Agent Loop]]"
---

> [!concept] Concept
> 1 source · refreshed 2026-10-13 · #machine-learning/cs566-deeplearning
> Up: [[Agent Loop]]

## Definition

An agent skill is a folder with a `SKILL.md` file. A person writes it for an agent ([[Block 1 Slides]], p. 95). A skill bundles instructions, scripts, and tools so an agent gains a capability "without retraining the model". It is loaded on demand, and agent harnesses such as Claude Code, Codex, and Gemini CLI use the same `SKILL.md` format (p. 142).

## Explanation

### Three things called "skill"

| Thing | What it is | Written by | Where you meet it |
| --- | --- | --- | --- |
| Agent Skill | a folder with `SKILL.md` | a person, for the agent | this lecture, and your own tooling |
| Skill library | code the agent stores and reuses | the model, for itself | embodied-agent papers (Voyager, 2023) |
| Alexa Skill | a published third-party app unit | a developer, for a platform | consumer AI since 2015 |

Source: [[Block 1 Slides]], p. 95. "Usage one has won in agent tooling. It has not won in the research literature."

### The folder

The slides follow the Agent Skills specification (agentskills.io) ([[Block 1 Slides]], p. 96):

- `SKILL.md` (required), plus optional `scripts/`, `references/`, and `assets/`
- `SKILL.md` fields: `name` and `description` (required); `license`, `compatibility`, `metadata` (optional); `allowed-tools` (optional, experimental)

The course example `lab-paper-digest` has the description "Find recent lab papers; summarize and email a digest." It lists four steps: `search_papers`, `read_paper`, format summaries, and `send_email`. A rubric in `references/` is "read only when needed". "The skill describes the procedure; tools perform the operations" (p. 97).

### Context is a budget

A request has finite context. It holds the trajectory (user, thought, action, observation), which grows each turn, and the tool schemas. On the eager path, every schema enters each request. The alternative is deferred tool discovery and loading a matching skill on demand ([[Block 1 Slides]], p. 94).

Skills load in three stages (p. 98):

| Stage | Loads | Size |
| --- | --- | --- |
| 1. Discovery | `name` + `description` | about 100 tokens |
| 2. Activation | `SKILL.md` | under 5,000 tokens recommended |
| 3. Execution | `scripts`, `references`, `assets` | as needed |

The slide says to load more only when the task calls for it (p. 98).

### Tool, MCP server, and skill

| Thing | Unit | Runtime verb | Example |
| --- | --- | --- | --- |
| Tool | typed operation | invoke | `send_email` |
| MCP server | provider of tools, resources, prompts | connect, discover, call | `mail-mcp` exposes `send_email` |
| Skill | folder of instructions and resources | discover, load, follow | `lab-paper-digest` |

"A skill selects a tool; an MCP server may expose that tool" ([[Block 1 Slides]], p. 99).

### Pre-approved tools

`allowed-tools: send_email` in `SKILL.md` can let the tool run in the invoked turn with no prompt for each use, given client support and a trusted workspace ([[Block 1 Slides]], p. 100):

- In the open specification, the field is optional and experimental.
- Claude Code grants the tool for one turn. It also adds `disallowed-tools`, which is not in the open specification.
- Runtime trust and policy bind the file to actual execution authority.

"Pre-approval is not a deny list." The slide asks: "Who wrote the file, and what authority did the runtime bind to it?"

### A privilege boundary

The skill layer sits between user intent and tool execution, so it is a privilege boundary ([[Block 1 Slides]], pp. 142–143). The [[FORTIS]] benchmark measures agents at this layer. Agents can pick a broader skill than the request needs, or pick the right skill and reach for stronger tools (p. 143). Given the full `SKILL.md` with its limits written out, the fail rate stays at 45–67%: "Stated limits behave like advisory text" (p. 151). See [[Deployment Failure Modes]].

Synthesis: `allowed-tools` moves the allow check in the [[Agent Loop]] from each call to the whole turn. That makes the author of the file and the runtime policy more important.

### On the timeline

The [[Evolution of Machine Learning]] timeline marks the MCP release on 2024-11-25 and the Agent Skills release on 2025-10-16, "Procedural know-how as a portable package" ([[Block 1 Slides]], pp. 44–45).

## Related

- [[Agent Loop]]
- [[Deployment Failure Modes]]: excess privilege at the skill layer
- [[FORTIS]]
- [[Tokenization]]: token counts set the context budget
- [[In-Context Learning]]: a skill changes behavior through context, not weights
- [[Agent Memory]]
- [[Evolution of Machine Learning]]

## Sources

- [[Block 1 Slides]], pp. 44–45, 94–100, 142–143, 151
