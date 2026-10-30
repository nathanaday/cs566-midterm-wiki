---
id: doc-rjpp3w
type: topic
kind: concept
description: GraphRAG (graph retrieval-augmented generation) builds a graph of sourced relations from documents, follows its edges to select the evidence passages for a question, and gives those passages to an LLM to write a cited answer; CSCI 566 teaches it with a fictional database-outage example.
tags: [machine-learning/cs566-deeplearning]
aliases: [Graph retrieval-augmented generation, Graph-based retrieval, Simplified local graph retrieval, Graph index, Atlas-Beacon outage example, GraphRAG failure modes, Retrieval vs. generation error]
created: 2026-10-05T17:36:50
updated: 2026-10-13T18:22:42
refreshed: 2026-10-13T18:22:42
status: stable
sources: ["[[Block 6 Slides Extended]]", "[[Block 6 Slides]]"]
up: ["[[Retrieval-Augmented Generation]]", "[[LLMs and Graphs]]"]
---

> [!concept] Concept
> 2 sources · refreshed 2026-10-13 · #machine-learning/cs566-deeplearning
> Up: [[Retrieval-Augmented Generation]] · [[LLMs and Graphs]]

## Definition

GraphRAG is a form of [[Retrieval-Augmented Generation]] in which a graph built from the documents selects the evidence. Before any question, the system reads the documents and stores the systems, the relations between them, and the source ID of each relation. For each question, it locates the entity that the question names, finds the connected facts, fetches their source passages, and gives the question and the passages to an LLM ([[Block 6 Slides Extended]], p. 139). "Build the graph first. Then retrieve evidence for each question" (p. 139). The deck labels its version "simplified local graph retrieval" and cites Edge et al. (2024) (pp. 135–153).

## Explanation

### Why a graph helps

In document question answering, the facts that support an answer can be spread across several documents. One document names a service, and other documents name its apps ([[Block 6 Slides Extended]], p. 135). A plain retrieval step that finds only the first document gives an incomplete answer (p. 138); see [[Retrieval-Augmented Generation]]. The graph index is built once: "The index is reusable. Each question selects the evidence it needs" (p. 139).

### The worked example: a fictional outage

> [!note] The "Atlas" in this example is a fictional database from the slides. It is unrelated to the Atlas tool that manages this vault.

The question: "Which apps could be affected if the Atlas database goes offline?" ([[Block 6 Slides Extended]], p. 135). All the systems are fictional. Atlas and Cedar are databases, Beacon is a service, and HelpDesk, Alerts, and Search are apps. Four documents each record one fact (p. 137):

| Document | Recorded fact |
| --- | --- |
| D1 | Beacon uses data from the Atlas database. |
| D2 | The HelpDesk app uses data from Beacon. |
| D3 | The Alerts app uses data from Beacon. |
| D4 | The Search app uses data from the Cedar database. |

### An edge is a claim with a source

Each document becomes one sourced relation. D1 becomes the stored tuple (Atlas, supplies data to, Beacon, D1). The arrow points from a data supplier to its consumer ([[Block 6 Slides Extended]], p. 140). The four relations form two connected components: D1, D2, and D3 connect the fictional Atlas database to two apps, and D4 links Search to Cedar in a separate part of the graph (p. 141). The system stores both the relation and a link back to the supporting document. "The graph helps us find facts; the source text lets us check them" (p. 142).

### Two-hop traversal

1. **Hop 1.** Locate the database that the question names, then follow supplier-to-consumer edges. The first hop finds Beacon and its supporting document, D1 ([[Block 6 Slides Extended]], p. 143).
2. **Hop 2.** Continue from Beacon. The next edges reach HelpDesk (D2) and Alerts (D3). The relevant evidence is D1, D2, and D3 (p. 144).

The path tells the system which source documents to bring back. "The selected context is the text of D1, D2 and D3", not the edges themselves (p. 145).

### What the LLM receives and writes

The system puts the question and the retrieved passages into one prompt ([[Block 6 Slides Extended]], p. 146):

```
Question: Which apps could be affected if Atlas goes offline?

Evidence:
[D1] Beacon uses data from the Atlas database.
[D2] The HelpDesk app uses data from Beacon.
[D3] The Alerts app uses data from Beacon.

Use these facts to answer. Cite the document IDs.
```

The answer names each app with its path: HelpDesk through Atlas → Beacon → HelpDesk [D1, D2], and Alerts through Atlas → Beacon → Alerts [D1, D3]. Search is excluded, because D4 links Search to Cedar and these documents give no path from the fictional Atlas database. "The answer names the apps and cites the dependency chain" ([[Block 6 Slides Extended]], p. 147).

### Three stages, no trained GNN

| Stage | Job in the example |
| --- | --- |
| Graph retrieval | Find the Atlas → Beacon → app paths and their source IDs. |
| Context assembly | Fetch the matching document passages for the prompt. |
| LLM generation | Write an answer from the question and those passages. |

Source: [[Block 6 Slides Extended]], p. 148. "The graph connects the source facts. The LLM expresses the supported answer" (p. 148). "This example uses graph traversal without training a GNN" (p. 148). The summary slide shows the same flow: build a sourced graph from D1–D4, retrieve D1–D3 for the question, and give the question and passages to the LLM. "The graph selects evidence. The LLM reads that evidence and writes the answer" (p. 153).

Synthesis: here the graph is a search index. In the enhancer pipeline of [[LLMs and Graphs]], the graph is an input to a trained model.

### Failure modes: missing and wrong edges

**A missing relation removes needed evidence.** Suppose graph construction misses the D3 relation, Beacon → Alerts ([[Block 6 Slides Extended]], p. 149):

| Stage | What goes wrong |
| --- | --- |
| Graph construction | D3 exists, but its Beacon → Alerts edge is absent. |
| Retrieval | The path search returns D1 and D2 and misses D3. |
| Answer | The supported answer may omit Alerts. |

"Check whether the retrieved evidence covers all required facts" (p. 149).

**A wrong relation adds an unsupported app.** Suppose the index links the fictional Atlas database to the Search app by mistake. D4 says that Search uses Cedar and gives no Atlas relation. The fix is to remove or flag the unsupported edge before the system relies on it. "Verify a graph relation against its source document" ([[Block 6 Slides Extended]], p. 150).

Synthesis: these two cases work through the GraphRAG failures that the short deck names, "missed evidence" and "noisy graph" ([[Block 6 Slides]], pp. 121–122).

### Testing: separate retrieval errors from generation errors

For the example, the required evidence is D1, D2, and D3. The required answer names both HelpDesk and Alerts with their source IDs. Search must not appear, because it is absent from the Atlas paths. "Test evidence retrieval and answer quality separately" ([[Block 6 Slides Extended]], p. 151).

The same incomplete answer can come from different stages (p. 152):

| Retrieved context | Answer | Where to investigate |
| --- | --- | --- |
| D1, D2 only | HelpDesk only | Graph construction or retrieval |
| D1, D2, D3 | HelpDesk only | LLM answer generation |

"Inspect the retrieved passages before blaming the LLM" (p. 152).

Synthesis: this is rule 5 of [[LLMs and Graphs]], "score the system where it can fail", applied to one system. The short deck gives each stage its own metric: build uses graph quality, retrieve uses evidence recall, and answer uses task accuracy ([[Block 6 Slides]], p. 132).

### What an edge means here

In GraphRAG, an entity is a node, and an edge records a document fact for retrieval ([[Block 6 Slides Extended]], p. 154). The deck contrasts this with [[GRADE]], where nodes are actions, and [[MAMA]], where nodes are agents. "Always identify what an edge means before interpreting a graph" (p. 154). The closing slide sums up the role of GraphRAG: "Connect document facts. Retrieve sources for the LLM's answer" (p. 176).

### In the short deck

The short deck lists GraphRAG as one of four families of LLM-graph systems. Its question is "Which evidence subgraph is retrieved?", and its failure is "noisy graph or missed evidence" ([[Block 6 Slides]], pp. 121–122). Its flow is query, retrieve, evidence, answer. Because it retrieves a subgraph, the whole graph stays outside the LM context (p. 128). See [[LLMs and Graphs]].

## Related

- [[Retrieval-Augmented Generation]]: the plain version, with no graph
- [[LLMs and Graphs]]: the family map and the paper-classification example from the same deck
- [[Graph]]: nodes, edges, and connected components
- [[Graph Neural Networks]]: the trained alternative that this example does not use
- [[GRADE]] and [[MAMA]]: graphs whose edges mean different things
- [[Question Answering]]: the task
- [[Agent Memory]]: another design that keeps data outside the context and retrieves it

## Sources

- [[Block 6 Slides Extended]], pp. 135–154, 176
- [[Block 6 Slides]], pp. 121–122, 128, 132
