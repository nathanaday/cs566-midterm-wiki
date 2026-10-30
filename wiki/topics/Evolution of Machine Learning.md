---
id: con-c74yp5
type: topic
kind: concept
description: The CSCI 566 account of ML progress as parallel tracks of research, data, compute, systems, and capability/interface, from the 1958 perceptron to 2026 agent systems.
tags:
  - machine-learning/cs566-deeplearning
aliases:
  - History of Machine Learning
  - Evolution of ML
  - Three pillars of ML applications
created: 2026-09-28T00:00:00
updated: 2026-10-13T18:22:47
refreshed: 2026-10-13T18:22:47
status: stable
sources:
  - "[[Block 1 Slides]]"
  - "Lecture 1"
up:
  - "[[Deep Learning]]"
---

> [!concept] Concept
> 2 sources · refreshed 2026-10-13 · #machine-learning/cs566-deeplearning
> Up: [[Deep Learning]]

## Definition

The lecture explains ML progress with parallel tracks: research, data, compute, systems, and capability/interface ([[Block 1 Slides]], pp. 28–39). The track structure is adapted from Tianqi Chen, CMU 15-884 Machine Learning Systems. The stage labels on the capability track are course synthesis, not CMU claims (p. 39).

The slide caption: "Research changes the recipe; Data and Compute change the feasible scale; Systems make it usable; Capability / Interface is what people experience" ([[Block 1 Slides]], p. 39).

## Explanation

### Three pillars, then systems

| Track | Period | Milestones |
| --- | --- | --- |
| Research | 1958–2000 | Perceptron (1958), backprop (1986), SVM (1992), ConvNet (1998), gradient boosting machine (1999) |
| Data | 2000–2010 | Wikipedia (2001), Flickr (2004), MTurk (2005), Netflix Prize (2009), Kaggle and ImageNet (2010) |
| Compute | 2006 onward | Public cloud (2006), CUDA (2007), multi-GPU servers (2016), TensorCore (2017), large clusters (2019) |
| Systems | 2010 onward | GraphLab, Spark, XGBoost, scikit-learn, Caffe, TensorFlow, MXNet, PyTorch |

Sources: [[Block 1 Slides]], pp. 28–31 and 38. The slides say "many algorithms we use today are created before 2000" (p. 28) and "data serves as fuel for machine learning models" (p. 29). The three-pillar slide starts the compute track at 2007 (p. 31); the compute slide says "2006 – Now" (p. 30).

Deep learning depended on both software and hardware. GPUs gave fast tensor operations (p. 33), and deep learning also needed mature learning systems such as PyTorch, TensorFlow, MXNet, and ONNX (p. 34). [[AlexNet]] is the case study that joins the pillars (pp. 35–37).

### Capability track, 2012–2026

The stages are deep learning → foundation model → assistant → agent system ([[Block 1 Slides]], p. 39).

| Date | Event as the slide gives it | Citation on the slide |
| --- | --- | --- |
| 2012 | AlexNet top-5 error 15.3% vs. 26.2% | Krizhevsky et al., NeurIPS 2012 |
| 2014-09-01 | "Learn where to look; no fixed vector" | Bahdanau et al., ICLR 2015 (arXiv:1409.0473) |
| 2017-06-12 | Transformer: parallel sequence training | Vaswani et al., NeurIPS 2017 (arXiv:1706.03762) |
| 2018-10-11 | BERT: pretrained once; 11 NLP tasks | Devlin et al., NAACL 2019 (arXiv:1810.04805) |
| 2020-01-23 | Model, data, compute power laws; >7 orders | Kaplan et al. (arXiv:2001.08361) |
| 2020-05-28 | GPT-3: 175B; no gradient update | Brown et al., NeurIPS 2020 (arXiv:2005.14165) |
| 2021-09-03 | FLAN 137B: 60+ tasks; wins 20/25 vs. zero-shot GPT-3 | Wei et al., ICLR 2022 (arXiv:2109.01652) |
| 2022-03-04 | 1.3B preferred to 175B GPT-3 | Ouyang et al., NeurIPS 2022 (arXiv:2203.02155) |
| 2022-10-06 | Reasoning + actions + observations interleave | Yao et al., ICLR 2023 (arXiv:2210.03629), see [[ReAct]] |
| 2022-11-30 | Conversation becomes default public interface | OpenAI, "Introducing ChatGPT" |
| 2023-06-13 | Action request becomes an API primitive | OpenAI, "Function calling and other API updates" |
| 2023-10-10 | 2,294 issues, 12 repos; best 1.96% | Jimenez et al., ICLR 2024 (arXiv:2310.06770) |
| 2024-11-25 | MCP: connect assistants, data, and tools | Anthropic, "Introducing the Model Context Protocol" |
| 2025-03-11 | Agent runtime becomes a platform layer | OpenAI, "New tools for building agents" |
| 2025-10-16 | Agent Skills: procedural know-how as a portable package | Anthropic, "Equipping agents for the real world with Agent Skills" |
| 2025-12-18 | Agent Skills becomes a cross-platform open standard | open-standard update |
| 2024/2025 | τ-bench: pass^1 < 50%; retail pass^8 < 25% | Yao et al., ICLR 2025 |
| 2026 | Least-privilege benchmark "from our lab" | instructor's lab |

Sources: [[Block 1 Slides]], pp. 40–46. The slide titles name each phase: parallelism changes which models win (2012–2017), pretraining changes the unit of reuse (2018–2020), training for instructions changes the interface (2021–2022), evaluation moves from an answer to an environment (2022–2024), agent plumbing becomes a systems layer (2024–2025), and capability outruns control (2026). The summary for the last stages is "capability -> reliability -> control" (p. 46).

### Links to the lecture notes

The timeline answers two open questions in Lecture 1, § Background Topics:

- The notes' entry "2014 - no fixed vector (?)" is the Bahdanau et al. attention paper ([[Block 1 Slides]], p. 40).
- The notes' entry "2020 - model, data, compute >7 orders (power law)" is the Kaplan et al. scaling-laws paper ([[Block 1 Slides]], p. 41). See [[Scaling Laws]].

The slides and the notes agree that most core algorithms are old. The notes say many meaningful changes come from data and compute (Lecture 1, § Background Topics; [[Block 1 Slides]], p. 28).

Synthesis: the unnamed 2026 node is likely [[FORTIS]]. The deck later cites FORTIS as a 2026 benchmark of over-privilege in agent skills, with least privilege as its concern ([[Block 1 Slides]], p. 143).

## Related

- [[AlexNet]]
- [[Deep Learning]]
- [[Scaling Laws]]
- [[Agent Loop]]
- [[Agent Skills]]
- [[ReAct]]
- [[FORTIS]]
- [[What Counts as Solved]]

## Sources

- [[Block 1 Slides]], pp. 26–46, 143
- Lecture 1, § Background Topics
