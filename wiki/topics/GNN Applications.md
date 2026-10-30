---
id: con-82wmtg
type: topic
kind: concept
description: "The CSCI 566 Block 6 examples of graph neural networks in use: link prediction for recommenders (PinSage) and drug side effects, ETA prediction on road graphs in Google Maps, molecule classification for antibiotic discovery, and how each drug discovery task sets the output the GNN must give."
tags: [machine-learning/cs566-deeplearning]
aliases: [GNN use cases, PinSage, Polypharmacy side effect prediction, Traffic prediction with GNNs, ETA prediction, Deep learning for antibiotic discovery, Molecules as graphs, Recommender systems as graphs, Biomedical graph link prediction, Google Maps ETA prediction with GNNs, Road network as a graph, A Deep Learning Approach to Antibiotic Discovery, Stokes et al. 2020, Molecular graphs for drug discovery, Graph tasks in drug discovery, Prediction tasks in drug discovery]
created: 2026-09-28T00:00:00
updated: 2026-10-13T18:22:47
refreshed: 2026-10-13T18:22:47
status: stable
sources: ["[[Block 6 Slides]]", "[[Block 6 Slides Extended]]"]
up: ["[[Graph Neural Networks]]"]
---

> [!concept] Concept
> 2 sources · refreshed 2026-10-13 · #machine-learning/cs566-deeplearning
> Up: [[Graph Neural Networks]]

## Definition

Block 6 of CSCI 566 shows graph neural networks (GNNs) at work in products and in science. The examples fall into two groups: link prediction (recommenders, drug side effects) and prediction for a whole graph or subgraph (travel time, molecules) ([[Block 6 Slides]], pp. 21–30; [[Block 6 Slides Extended]], pp. 31–40).

In this topic, a page number without a document name refers to [[Block 6 Slides]]. The extended deck repeats these slides, and its pages are given with its name. It also adds a section on graph tasks in drug discovery ([[Block 6 Slides Extended]], pp. 41–46).

## Explanation

### Link prediction

The link-level task predicts new, missing, or unknown links from the links that exist. At test time the model ranks node pairs with no link and predicts the top K pairs (p. 21; [[Block 6 Slides Extended]], p. 31).

**Recommender systems.** Users interact with items: they watch movies, buy merchandise, or listen to music. The nodes are users and items, and the edges are user-item interactions. The goal is to recommend items that a user might like. A new "You might also like" edge is a predicted link (p. 22; [[Block 6 Slides Extended]], p. 32).

**PinSage.** PinSage is a graph-based recommender that recommends related pins to users from a query pin (p. 23). It learns node embeddings z_i so that related items lie closer, for example d(z_cake1, z_cake2) < d(z_cake1, z_sweater). The recommendation becomes a prediction of "whether two nodes in a graph are related" (p. 23). The slide cites "Graph Convolutional Neural Networks for Web-Scale Recommender Systems" (p. 23; [[Block 6 Slides Extended]], p. 33).

**Polypharmacy side effects.** The extended deck titles this slide "Biomedical Graph Link Prediction" ([[Block 6 Slides Extended]], p. 34). The nodes are drugs and proteins, and the edges are interactions: drug-protein, protein-protein, and side-effect relations between drugs. The edge types include r1, gastrointestinal bleed side effect, and r2, bradycardia side effect (p. 24). An example query: "How likely will Simvastatin and Ciprofloxacin, when taken together, break down muscle tissue?" (p. 24). The slide cites "Modeling Polypharmacy Side Effects with Graph Convolutional Networks" (p. 24; [[Block 6 Slides Extended]], p. 34).

### Prediction for a graph or a subgraph

A graph-level task makes "a prediction for an entire graph or a subgraph of the graph" (p. 25; [[Block 6 Slides Extended]], p. 35). The deck gives traffic prediction and drug discovery as examples.

**Traffic prediction.** The extended deck opens this example with a Google Maps route from the University of California, Los Angeles to the USC Viterbi School of Engineering. The route takes 17 min (14.0 miles) via I-10 E, the "Fastest route now due to traffic conditions" ([[Block 6 Slides Extended]], p. 36). A road network is a graph. The nodes are road segments, the edges are the connections between segments, and the model predicts the time of arrival (ETA) (p. 27; [[Block 6 Slides Extended]], p. 37). DeepMind's "Predicting Time of Arrival with GNNs" (2020) was "Used in Google Maps, 2020" (p. 28). In that pipeline, anonymized travel data is analyzed into supersegments, which become training data for a GNN. The Google Maps routing system supplies candidate routes from A to B, and the GNN predictions rank them by ETA. The ranked routes go to the Google Maps API and app (p. 28, citing DeepMind, Sep 2020; [[Block 6 Slides Extended]], p. 38).

**Antibiotic discovery.** "Antibiotics are small molecular graphs": atoms are nodes and chemical bonds are edges (p. 29; [[Block 6 Slides Extended]], p. 39). The slide shows beta-lactam classes, such as penicillins, cephalosporins, and carbapenems, and cites Konaklieva, *Antibiotics* 3.2 (2014): 128–142 (p. 29). A GNN graph classification model predicts promising molecules from a pool of candidates (p. 30; [[Block 6 Slides Extended]], p. 40). According to the figure (p. 30; [[Block 6 Slides Extended]], p. 40):

- The model is a directed message passing neural network.
- It trains on about 10^4 molecules, with iterative re-training.
- It makes large-scale predictions, with an upper limit of 10^8 or more molecules.
- For comparison, conventional chemical screening has an upper limit of 10^5–10^6 molecules and a 1–3% hit rate in hit validation.

The source is Stokes et al., "A deep learning approach to antibiotic discovery", *Cell* 180.4 (2020): 688–702 (p. 30; [[Block 6 Slides Extended]], p. 40).

### Graph tasks in drug discovery

The extended deck says that "The molecule examples we just saw are part of a larger scientific workflow". It names three scales ([[Block 6 Slides Extended]], p. 41):

| Scale | What the graph is and what to predict |
| --- | --- |
| One molecule | "Atoms and bonds form a graph. Predict a molecular property." |
| Interacting objects | "Drugs and proteins form a network. Predict a possible interaction." |
| Scientific workflow | "Therapeutics Data Commons (TDC) collects tasks and datasets for this workflow." |

The slide's rule: "Choose what the graph represents and what we want to predict" (p. 41).

The deck separates two kinds of task ([[Block 6 Slides Extended]], p. 42):

- Interaction prediction: "will two objects interact?"
- Molecule property prediction: "what property does this molecule have?"

"Molecular properties and interactions require different outputs" (p. 42). [[Therapeutics Data Commons]] groups its problems by the output they need, and the deck concludes: "Our GNN head must match the scientific question" (p. 45). To predict a molecule property, the GNN pools the atom vectors over the graph and predicts one property. To predict a drug-protein interaction, it combines a drug vector and a protein vector (p. 46). [[Graph Neural Networks]] covers the prediction head.

### Synthesis

Each example first chooses what the nodes and edges are, then chooses the level of the prediction: a node pair or a whole (sub)graph. The same GNN machinery then applies. The extended deck states this choice as a rule (p. 41) and ties the level of the prediction to the head of the GNN (pp. 45–46). The drug discovery thread continues with [[Therapeutics Data Commons]] ([[Block 6 Slides]], pp. 31–38; [[Block 6 Slides Extended]], pp. 41–45).

## Related

- [[Therapeutics Data Commons]]: datasets, tasks, and benchmarks for therapeutic ML, grouped by the output each problem needs
- [[LLMs and Graphs]]: later in the same deck
- [[Graph Neural Networks]]: the models behind these applications, and the prediction head that must match the task
- [[Graph Convolutional Network]]: PinSage and the polypharmacy model are graph convolutional networks
- [[Graph]]: link-level and graph-level tasks

## Sources

- [[Block 6 Slides]], pp. 21–30
- [[Block 6 Slides Extended]], pp. 31–42, 45–46
