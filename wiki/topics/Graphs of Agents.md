---
id: doc-6y47t9
type: topic
kind: concept
description: In CSCI 566 Block 6, graphs whose nodes are agents or agent actions (GRADE, MAMA), used to study execution dependencies and communication paths, with the rule to identify what a node and an edge mean before interpreting any graph.
tags: [machine-learning/cs566-deeplearning]
aliases: [Graph of agents, Agent graphs, Edge semantics in graphs, What an edge means, Node and edge meaning]
created: 2026-10-05T17:31:20
updated: 2026-10-13T18:22:42
refreshed: 2026-10-13T18:22:42
status: stable
sources: ["[[Block 6 Slides Extended]]"]
up: ["[[LLMs and Graphs]]"]
---

> [!concept] Concept
> 1 source · refreshed 2026-10-13 · #machine-learning/cs566-deeplearning
> Up: [[LLMs and Graphs]]

## Definition

In CSCI 566 Block 6, graphs of agents are graphs whose nodes are agents or the actions of an agent. They are used to "study communication paths and execution dependencies" ([[Block 6 Slides Extended]], p. 5).

The block has three parts (p. 5):

- **Graph representation**: choose the objects, connections, and input features.
- **Graph neural network**: learn predictions by combining neighboring information.
- **Graphs of agents**: study communication paths and execution dependencies.

"We will follow one small road network, then graphs of agents" (p. 5).

## Explanation

### From entities to actions and agents

The GraphRAG example in the deck uses document entities as nodes. "The next examples use actions and agents as nodes, rather than document entities" (p. 154). The slide compares three cases (p. 154):

| Case | A node is | An edge records |
| --- | --- | --- |
| [[GraphRAG]] | an entity | a document fact, for retrieval |
| [[GRADE]] | an action | order or data use in a run |
| [[MAMA]] | an agent | permission to send messages within a team |

The rule: "Always identify what an edge means before interpreting a graph" (p. 154). The deck repeats it before the MAMA case: "First identify what a node and an edge mean in the new example" (p. 168).

### The two agent cases

"GRADE describes one run. MAMA studies communication among several agents" (p. 168).

- **[[GRADE]]**: a node is one action in a run. An edge is order or data dependency (p. 168).
- **[[MAMA]]**: a node is one agent in a team. An edge is allowed communication (p. 168). The MAMA slides cite Liu et al., "Topology Matters" (Findings of ACL 2026) (pp. 169–175).

The two cases ask different questions (p. 175):

- MAMA: "Who can exchange messages, and what private data leaks?"
- GRADE: "Which earlier outputs did the recorded actions use?"

"A communication graph specifies possible paths. A run graph records what happened" (p. 175). The design implication: "Communication paths and data dependencies need separate checks" (p. 175). The slide's rule: "Define the edge meaning, then test the claim that depends on it" (p. 175).

### What a graph contributes in each use

"The meaning of the nodes and edges determines what the graph can help us do" (p. 176):

| Use | What the graph does |
| --- | --- |
| GNN prediction | Read connected objects. Train shared weights to predict labels. |
| GraphRAG retrieval | Connect document facts. Retrieve sources for the LLM's answer. |
| Agent analysis | GRADE records data use. MAMA tests communication paths. |

Synthesis: this is the representation choice in [[Graph]] applied to agent systems. The way you assign edges sets the questions the graph can answer.

Synthesis: one node set can hold more than one graph. GRADE puts an execution layer and a dependency layer on the same five action nodes (pp. 161–162). A reader must know which edge set a figure shows before reading a path in it.

Synthesis: in the two agent cases, nobody trains a [[Graph Neural Networks|GNN]] on the graph. The graph is a record or a constraint that people inspect and test. The GraphRAG example also "retrieves facts without training a GNN" (p. 153).

## Related

- [[GRADE]]: the run graph of one agent
- [[MAMA]]: the communication graph of an agent team
- [[GraphRAG]]: entity graphs for retrieval
- [[LLMs and Graphs]]: the system families that combine LLMs with graphs
- [[Graph]]: nodes, edges, and the choice of representation
- [[Graph Neural Networks]]: the prediction use of graphs
- [[Agent Loop]]: the runs and the agents that these graphs describe

## Sources

- [[Block 6 Slides Extended]], pp. 5, 153–154, 161–162, 168, 175–176
