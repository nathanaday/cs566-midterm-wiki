---
id: doc-7thktk
type: topic
kind: entity
description: MAMA is the CSCI 566 example of a multi-agent communication graph, with agents as nodes and permitted messages as edges, used to show that the pattern of connections changes how much private data an attacker agent recovers (cited from Liu et al., Topology Matters, Findings of ACL 2026).
tags: [machine-learning/cs566-deeplearning]
aliases: [Topology Matters, Communication topology, Agent communication topology, Multi-agent communication graph, Communication graph, Communication graph versus run graph, Message-leakage path, "Chain, star, and complete topologies"]
created: 2026-10-05T17:31:20
updated: 2026-10-13T18:22:42
refreshed: 2026-10-13T18:22:42
status: stable
sources: ["[[Block 6 Slides Extended]]"]
up: ["[[LLMs and Graphs]]"]
---

> [!entity] Entity
> 1 source · refreshed 2026-10-13 · #machine-learning/cs566-deeplearning
> Up: [[LLMs and Graphs]]

## What it is

MAMA is the Block 6 example of a graph whose nodes are agents. "An agent is a node. An edge permits messages within a team" ([[Block 6 Slides Extended]], p. 154). The deck contrasts it with [[GRADE]]: "GRADE describes one run. MAMA studies communication among several agents" (p. 168). The MAMA slides cite Liu et al., Topology Matters (Findings of ACL 2026) (pp. 169–175). The slides do not expand the name MAMA.

## Facts

### The graph

| Part | Meaning in MAMA |
| --- | --- |
| Node | One agent in a team (p. 168): the target T, the attacker A, and other LLM agents (p. 169). |
| Edge | Allowed communication (p. 168). "Messages can travel only along the allowed connections" (p. 169). In the figures, "Lines allow messages in both directions" (p. 170). |
| Question | "Can A recover private data held by T?" (p. 169) |

### Communication topology

"Topology means the pattern of allowed connections between agents" (p. 169). The same four agents can form different graphs (p. 170):

- **Chain**: T, 2, 3, and A in a line.
- **Star**: T connects to 2, 3, and A.
- **Complete**: every pair of agents connects.

"Connections change who can read whose messages" (p. 170).

An extra edge can make a path shorter. "Chain: distance T to A = 3" and "Complete: distance = 1". "A shorter path offers a different route for information exposure" (p. 173).

Synthesis: in the star figure on p. 170, T also connects directly to A, so the distance is 1 there too. The slides do not state this.

### The leakage setup

"An agent team works on a public task. One agent also holds private data" (p. 169). In the illustration, T stores a private code, DEMO-731. All agents work on a public travel plan, and the test is whether A recovers the code. "The public task does not require that code." "Code and task are synthetic teaching examples." "Recovering the private code counts as leakage in this illustration" (p. 171).

The slides then show how relays move the code. Along a chain, agent 2 and agent 3 repeat the code in their messages until A reads it. "Each arrow is one permitted message. A relay can copy information it received." "An allowed path creates an opportunity for leakage" (p. 172).

Synthesis: an agent between T and A does not block the data. If each relay copies what it receives, a longer path only delays the leak.

### The cited result

The slide reports the Table 2 mean leakage rate for Llama-3.1-70B, with 6 agents and up to 10 rounds (p. 174):

| Topology | Mean leakage | Standard deviation |
| --- | --- | --- |
| Chain | 12.95% | 1.64 percentage points |
| Complete | 25.32% | 2.54 percentage points |

"In this setting, complete connectivity leaked more than a chain" (p. 174).

Synthesis: the complete graph leaked about twice as much as the chain, 12.37 percentage points more. The slide shows one model, one team size, and two topologies. It does not show a result for the star. The illustrations use four agents, but the result uses six.

### Communication graph versus run graph

"A communication graph specifies possible paths. A run graph records what happened" (p. 175). The two graphs answer different questions (p. 175):

| Graph | Question |
| --- | --- |
| MAMA | "Who can exchange messages, and what private data leaks?" |
| [[GRADE]] | "Which earlier outputs did the recorded actions use?" |

The design implication: "Communication paths and data dependencies need separate checks." The rule: "Define the edge meaning, then test the claim that depends on it" (p. 175). The deck's summary: "GRADE records data use. MAMA tests communication paths" (p. 176). It gives the same warning earlier: "Always identify what an edge means before interpreting a graph" (p. 154).

Synthesis: an edge in a communication graph shows that a message could pass. It does not show that a message did pass. To show which message carried the private data, you need a record of the run, such as the run graph that GRADE builds.

## Related

- [[GRADE]]: a graph of the actions in one run. The deck contrasts it with MAMA.
- [[LLMs and Graphs]]: GraphRAG, the third graph in the comparison on p. 154.
- [[Graph]]: nodes, edges, and the choice of representation.
- [[Agent Loop]]: what each agent in the team runs.
- [[Deployment Failure Modes]]: the MAST failures of multi-agent systems had no attacker. MAMA puts an attacker inside the team.
- [[LLM Trustworthiness]]: privacy is one of its dimensions.

## Sources

- [[Block 6 Slides Extended]], pp. 154, 168–176
