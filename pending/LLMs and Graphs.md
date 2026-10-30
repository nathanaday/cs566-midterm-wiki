---
id: con-m8ydp4
type: topic
kind: concept
description: "How CSCI 566 combines large language models with graphs: the LLM as enhancer or as predictor, worked through a paper-classification example, four system families (features, foundation, GraphRAG, tool agent), and the rules it gives for testing what graph context adds."
tags: [machine-learning/cs566-deeplearning]
aliases: [LLMs for Graphs, LLM for graphs, Graphs and language models, LLMs on graphs, LLMs-as-Enhancers, LLM-as-Predictor, LLM as graph-task predictor, Enhancer pipeline, Paper topic classification, Matched comparison of graph context, LLM-graph system families, Graph foundation model, Graph tool agent, TAPE, KEA, Cascading structure, Iterative structure, Text-level enhancement]
created: 2026-09-28T00:00:00
updated: 2026-10-13T18:22:42
refreshed: 2026-10-13T18:22:42
status: stable
sources: ["[[Block 6 Slides]]", "[[Block 6 Slides Extended]]"]
up: ["[[Large Language Models]]", "[[GNN Applications]]"]
---

> [!concept] Concept
> 2 sources · refreshed 2026-10-13 · #machine-learning/cs566-deeplearning
> Up: [[Large Language Models]] · [[GNN Applications]]

## Definition

The end of Block 6 of CSCI 566 covers systems that combine large language models (LLMs) with graphs. It starts with two 2023 baselines: the LLM either enhances the inputs of a GNN or predicts the label directly. It then gives a 2026 map of four system families and rules for testing any claim that an LLM works on graphs ([[Block 6 Slides]], pp. 119–132).

The extended revision of the deck teaches the same enhancer and predictor split with two worked tasks. The first task classifies a paper from its abstract and its citation links. The second answers a question from several documents with [[GraphRAG]] ([[Block 6 Slides Extended]], pp. 126–153). Its LLM section does not repeat the four-family map or the GPT-3.5 case study below. Those parts come from the short deck only.

## Explanation

### The 2023 baselines

**Pipeline 1, enhance then predict.** Node text goes to an encoder or generator, which gives node features, and a GNN predicts the label. "Language model changes the inputs; the GNN makes the prediction." The slide's summary: "semantics become graph features" ([[Block 6 Slides]], p. 119).

**Pipeline 2, predict directly.** Node text, and an optional summary of the neighbors, goes to an API model. The prompt is the text plus the optional neighborhood summary, and the model outputs a class label. The slide asks, "What structure entered the prompt?" and concludes: "direct labels do not prove graph reasoning" (p. 120).

### Worked example: classify one paper two ways

The extended deck names two tasks. Paper classification takes abstracts and citation links and outputs a topic label. Document question answering takes a question and documents and outputs an answer with sources. Agent examples follow, which use graphs to describe actions and communication paths. "First classify papers. Then retrieve evidence to answer a question" ([[Block 6 Slides Extended]], p. 126). The slides mark the example as a "teaching example based on Chen et al. (2023/2024)" (pp. 126–134).

**The toy task.** Classify paper P as AI or Biology. P says "We train a neural network to recognize images." P cites paper Q, which says "Our convolutional network detects objects." The model predicts P's topic from its abstract and the available citation context. "Use both the paper's text and its citation neighbors" ([[Block 6 Slides Extended]], p. 127).

**Route 1, the enhancer pipeline.** A text encoder turns each abstract into one vector per paper. The citation links define the neighbors. A GNN with a topic head reads both and outputs the label. "The GNN prediction head produces the topic label" ([[Block 6 Slides Extended]], p. 128). For paper P, the encoder gives a vector, shown as [0.2, 0.8]. The GNN then gathers the vectors of P's graph neighbors, and the head uses the updated vector to output a label (p. 129). In one simple setup, the text encoder stays fixed. The GNN and the head learn from labeled training papers with the prediction loss. A new paper is encoded, its neighbors are gathered, and the trained graph predictor runs. "The training labels teach the GNN how to use those features" (p. 130).

**Route 2, the LLM as predictor.** The prompt gives a classification question and the paper's text: "Choose AI or Biology. Paper P: “We train a neural network to recognize images.” Topic:". The illustrative answer is AI. "Here, the LLM produces the final topic label" ([[Block 6 Slides Extended]], p. 131). Graph context enters the prompt as sentences: a citation edge becomes "Paper P cites Q. Q's abstract: ...". "The LLM can only read the graph information we include" (p. 132).

**What differs.** Route 1 is abstracts, then text vectors, then GNN and head, then label. Route 2 is abstract plus cited-paper summary, then LLM, then label. The routes differ in which component reads the graph context and which component produces the final label. "We can compare the routes on the same held-out papers" ([[Block 6 Slides Extended]], p. 133).

**Matched comparison.** To find which part of a pipeline produced a result, change one input and keep the test fixed ([[Block 6 Slides Extended]], p. 134):

| Step | Question |
| --- | --- |
| Text-only baseline | How well does the paper's own abstract predict its topic? |
| Add graph context | Does cited-paper information improve the same test? |
| Check leakage | Were test labels included by accident in any features or prompt? |

"Use matched comparisons to test the value of graph context" (p. 134).

Synthesis: the matched comparison puts rule 2 and the leakage check of rule 4 below on one slide.

### LLMs as enhancers

The LLM enhances or encodes the node text, and a GNN makes the final prediction. The enhancement happens at the feature level or at the text level ([[Block 6 Slides]], p. 123). Figure 2 on p. 125 shows three structures:

| Structure | Level | How it works | Slide note |
| --- | --- | --- | --- |
| Cascading | feature | An embedding-visible LLM, such as Sentence-BERT or e5, encodes the text attributes into the initial node features of the GNN. | "Often very effective and efficient." |
| Iterative | feature | The GNN and a pretrained language model (PLM) train together and exchange pseudo-labels. | "Can be powerful if enough labeled data." |
| Text-level | text | An embedding-invisible LLM generates augmented text attributes. The model encodes the augmented and original attributes and ensembles them. | |

Sources: [[Block 6 Slides]], pp. 124–125.

The short deck names two text-level methods ([[Block 6 Slides]], p. 124):

- **TAPE**: the LLM writes pseudo labels and explanations, PLMs re-encode them, and a GNN uses the result. The slide cites it as reference [22].
- **KEA**: the LLM adds knowledge entities to the node text, which is then encoded and ensembled.

Synthesis: Route 1 of the worked example, with a fixed text encoder, is the cascading structure.

### LLM as the graph-task predictor

The input is node text plus the graph context that is available. The LLM predicts the task output, a class or a relation ([[Block 6 Slides]], p. 127). The slide contrasts the two roles: "Enhancer: LLM-derived features feed a separate graph predictor. Predictor: the LLM supplies the final task prediction" (p. 127). The schematic comes from Chen et al. (2023), "Exploring the Potential of LLMs in Learning on Graphs" (p. 127).

### The four system families (2026 map)

| Family | Question it answers | Failure |
| --- | --- | --- |
| Features | How does text enter a GNN? | leakage or weak edges |
| Foundation | What transfers to unseen graphs? | transfer breaks across tasks |
| GraphRAG | Which evidence subgraph is retrieved? | noisy graph or missed evidence |
| Tool agent | Which graph operation runs next? | wrong tool or wrong sequence |

Sources: [[Block 6 Slides]], pp. 121–122.

**Graph foundation models.** These models pretrain across different graphs. Transfer rules, namely node equivariance, label equivariance, and feature invariance, carry the model to an unseen graph or task. "Transfer requires the right symmetries, not just more parameters" ([[Block 6 Slides]], p. 126).

**GraphRAG and tool agents.** The GraphRAG flow is query, retrieve, evidence, answer; its role is to retrieve evidence. The tool agent flow is goal, select, execute, state; its role is to orchestrate operations. In the slide's title: "GraphRAG Retrieves; Graph Agents Orchestrate" ([[Block 6 Slides]], p. 128). The extended deck works through one GraphRAG system step by step; see [[GraphRAG]].

Synthesis: the tool agent flow is the [[Agent Loop]] with graph operations as the tools.

### Case study: GPT-3.5 on Cora and Pubmed

The short deck asks, "What did the source result actually test?" ([[Block 6 Slides]], p. 129). The setup was GPT-3.5 (0613), with node text in and a predicted label out. The headline score used node text only, and a separate table added a 2-hop summary. The study used no tools and did not test random labels (p. 129). "The headline score is text classification evidence" (p. 129).

| Dataset | Text only | + 2-hop summary |
| --- | --- | --- |
| Cora | 67.00 | 71.75 |
| Pubmed | 90.75 | 88.00 |

Accuracy on a 0–100 scale ([[Block 6 Slides]], p. 130). "Neighborhood summaries change results in mixed directions" (p. 130).

Synthesis: the graph context added 4.75 points on Cora and cost 2.75 points on Pubmed. The headline number alone cannot show whether the model used the graph.

### Rules for evaluating LLM-for-graphs claims

The short deck states five rules ([[Block 6 Slides]]):

1. **Name the family before you compare results.** "Name the family before comparing results" (p. 121). Each family fails in a different way, and "a final answer score cannot locate the failed stage" (p. 122).
2. **Compare text-only and graph-context inputs under the same split** (p. 127). The extended deck repeats this rule as a matched comparison on the same held-out papers ([[Block 6 Slides Extended]], pp. 132–134).
3. **Keep the large graph outside the LM context** (p. 128). GraphRAG retrieves a subgraph, and a tool agent runs operations on the graph, so the whole graph never goes into the prompt.
4. **Report the setup before reporting the score** (p. 131). The checklist: model (name and version), data (split and leakage check), graph (size and serialization), tools (APIs and algorithms), and transfer (same graph or unseen graph) (p. 131). The extended deck asks the same leakage question: were test labels included by accident in any features or prompt ([[Block 6 Slides Extended]], p. 134)?
5. **Score the system where it can fail.** "Evaluate each stage that the chosen system actually uses" (p. 132). Each stage has its own metric: build uses graph quality, retrieve uses evidence recall, act uses tool success, and answer uses task accuracy (p. 132). [[GraphRAG]] shows this rule on a worked example: it separates retrieval errors from generation errors.

Synthesis: rule 2 and the leakage check in rule 4 apply the general rules in [[Model Evaluation]] and [[Test Set Contamination]] to graph inputs.

## Related

- [[Graph Neural Networks]]
- [[GNN Applications]]: earlier in the same deck
- [[GraphRAG]]: the document question-answering task of the extended deck
- [[Retrieval-Augmented Generation]]: the plain retrieval that GraphRAG extends
- [[GRADE]] and [[MAMA]]: the agent examples that follow, where graphs describe actions and communication paths
- [[Agent Loop]]: the pattern that a graph tool agent follows
- [[Model Evaluation]]
- [[Test Set Contamination]]: the leakage check in the setup report and in the matched comparison
- [[In-Context Learning]]: the predictor pipeline puts graph context into the prompt
- [[Agent Memory]]: another design that keeps large data outside the context and retrieves it
- [[Tree of Thoughts]]: an LLM searches a tree of its own thoughts, not a data graph

## Sources

- [[Block 6 Slides]], pp. 119–132
- [[Block 6 Slides Extended]], pp. 126–134
