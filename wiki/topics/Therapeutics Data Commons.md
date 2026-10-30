---
id: ent-rwg1yw
type: topic
kind: entity
description: Therapeutics Data Commons (TDC) is an open set of machine learning tasks, datasets, and benchmarks for drug discovery and development, organized by object, task, and stage, with its problems grouped by the output each one needs.
tags: [machine-learning/cs566-deeplearning, dataset]
aliases: [TDC, tdcommons.ai, TDC three-tier design]
created: 2026-09-28T00:00:00
updated: 2026-10-13T18:22:47
refreshed: 2026-10-13T18:22:47
status: stable
sources: ["[[Block 6 Slides]]", "[[Block 6 Slides Extended]]"]
up: ["[[GNN Applications]]"]
---

> [!entity] Entity
> 2 sources · refreshed 2026-10-13 · #dataset · #machine-learning/cs566-deeplearning
> Up: [[GNN Applications]]

## What it is

Therapeutics Data Commons (TDC) calls itself an "Artificial intelligence foundation for therapeutic science" ([[Block 6 Slides]], p. 31). The extended deck says that TDC "provides learning tasks, datasets and benchmarks for therapeutic science" ([[Block 6 Slides Extended]], p. 44). It "collects tasks and datasets" for the drug discovery workflow ([[Block 6 Slides Extended]], p. 41). Biomedical scientists identify useful tasks and datasets, and AI/ML scientists design methods. TDC connects the two groups to "facilitate algorithmic and scientific advance in therapeutics" ([[Block 6 Slides]], p. 35; [[Block 6 Slides Extended]], p. 44). The extended deck adds the lesson: "A model needs a defined task, usable inputs and evaluation data" ([[Block 6 Slides Extended]], p. 44).

- Website: https://tdcommons.ai
- Paper: https://www.nature.com/articles/s41589-022-01131-2
- GitHub: https://github.com/mims-harvard/TDC

([[Block 6 Slides]], p. 35)

In this topic, a page number without a document name refers to [[Block 6 Slides]]. The extended deck labels its TDC slides "Original TDC teaching graphics; Huang et al. (2021)" ([[Block 6 Slides Extended]], pp. 41–46).

## Facts

- **Core team:** Kexin Huang (Stanford), Tianfan Fu (Georgia Tech), Wenhao Gao (MIT), Yuanqi Du (Cornell), Ada Fang (Harvard), George Dasoulas (Harvard), Yue Zhao (CMU), and Nitin Pasumarthy (LinkedIn) (p. 31).
- **Coverage:** TDC covers therapeutic products (small molecule, macromolecule, gene therapy, cell and above), ML problems (single-instance prediction, multi-instance prediction, generation), and development pipelines (target discovery, hit and lead discovery, clinical trial, manufacturing) (p. 36).

### Objects, tasks, and stages

The extended deck reads the outer labels of the TDC overview figure as three questions ([[Block 6 Slides Extended]], p. 43):

- **Object:** "A molecule, protein or biological system."
- **Task:** "Predict one object, predict a pair, or generate an object."
- **Stage:** "Discovery, trials or manufacturing."

The slide's lesson: "Different biomedical problems require different representations" (p. 43). Synthesis: these three questions match the three coverage axes above, which are products, ML problems, and pipelines.

### Three-tier design

TDC sorts its content as problems, then learning tasks, then datasets (p. 37). The extended deck shows the same figure and says that it "groups problems by the required output" ([[Block 6 Slides Extended]], p. 45).

| Problem | Learning tasks | Example datasets | Required output ([[Block 6 Slides Extended]], p. 45) |
| --- | --- | --- | --- |
| Single-instance prediction | ADME, QM, Epitope, Yields, HTS, Tox, Develop, Paratope, CRISPROutcome | SARS-CoV2, Leenay, Caco2, CYP2C19, Half Life, IEDB, HIA | One molecule: "Predict its toxicity or another property." |
| Multi-instance prediction | DTI, MTI, GDA, DDI, AntibodyAff, PPI, DrugSyn, PeptideMHC, DrugRes, Catalyst | GDSC, BindingDB, HuRI, SAbDab, IEDB, TWOSIDES, KIBA | A drug–protein pair: "Predict whether the pair interacts." |
| Generation | MolGen, Reaction, RetroSyn | JNK3, DRD2, USPTO, ChEMBL, GSK3Beta, MOSES, QED, ZINC | A generated molecule: "Propose an object with desired properties." |

Source: [[Block 6 Slides]], p. 37; [[Block 6 Slides Extended]], p. 45.

The extended deck concludes: "Our GNN head must match the scientific question" (p. 45). [[GNN Applications]] and [[Graph Neural Networks]] show how the head changes with the task.

### The problem it addresses

- Drug discovery takes 12–16 years and costs $1 billion to $2 billion. It narrows 10,000 compounds to 250, then 5, then 1 approved drug (p. 32).
- The five steps are target identification, hit identification and lead optimization, clinical research, FDA review, and manufacturing and post-marketing (p. 32).
- Other challenges are various and emerging diseases and many molecular modalities: small molecules, proteins, anti-nano-bodies, vaccines, gene editing, and CAR-T (p. 32).
- For AI, the challenges are to formulate the steps as ML-solvable tasks, to find and process scattered datasets of many types, and to measure progress against real-world and clinical deployment (p. 33).
- The slides map example ML tasks to each step. Examples: PPI prediction for target identification, molecule property prediction for hit and lead, drug repurposing for clinical research, document automation for FDA review, and polypharmacy prediction for manufacturing (p. 33).
- The extended deck shows the first two steps of the original TDC diagram. For target identification, the tasks are gene-disease/drug interaction prediction and PPI prediction. For hit identification and lead optimization, the tasks are molecular optimization, protein structure prediction, and molecule property prediction ([[Block 6 Slides Extended]], p. 42).
- The slides then ask: "How to Advance Data-driven Therapeutics Design?" (p. 34).

### DrugAgent

The deck ends the TDC section with DrugAgent, an LLM agent framework for AI drug discovery tasks (p. 38):

1. A user gives a task in natural language. The example: predict Absorption, an ADMET property, on the PAMPA dataset.
2. A Planner proposes ideas, such as a GCN, a random forest, or a pretrained model like ChemBERTa.
3. An Instructor turns each idea into code. It adds domain knowledge, such as molecular fingerprints and molecular graph construction, through doc search over TDC, RDKit, and Hugging Face.
4. The Instructor reports results back. The Planner updates the plan and idea space for the next round.
5. At the maximum number of rounds, the Planner reports the best idea. In the example, a random forest predicted absorption best.

Synthesis: DrugAgent is an [[Agent Loop]] that uses TDC documentation as one of its tools.

## Related

- [[GNN Applications]]: antibiotic discovery, polypharmacy side effects, and the graph tasks in drug discovery, from the same deck
- [[Graph Neural Networks]]: the prediction head that must match the TDC problem type
- Yue Zhao: CSCI 566 instructor and TDC core team member
- [[Agent Loop]]

## Sources

- [[Block 6 Slides]], pp. 31–38
- [[Block 6 Slides Extended]], pp. 41–46
