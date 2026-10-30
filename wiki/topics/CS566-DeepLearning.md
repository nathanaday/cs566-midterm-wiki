---
id: are-f1jsnv
type: topic
kind: overview
description: "The USC CSCI 566 deep learning course, Fall 2026: lectures, readings, slides, and topic notes."
tags: [machine-learning]
aliases: ["CSCI 566: Deep Learning and its Applications"]
created: 2026-09-28T00:00:00
updated: 2026-10-12T16:59:46
refreshed: 2026-10-12T16:59:46
status: stable
sources: []
defines: machine-learning/cs566-deeplearning
---

> [!overview] The page of #machine-learning/cs566-deeplearning · under [[Machine Learning]]
> 0 sources · refreshed 2026-10-12 · #machine-learning

## Summary

The USC CSCI 566 deep learning course, Fall 2026: lectures, readings, slides, and topic notes.

## Context

## The course

CSCI 566, "Deep Learning and its Applications", is a USC course taught by Yue Zhao ([[Block 1 Slides]], p. 1). The slides credit earlier versions of USC CSCI 566, CMU 10601/701, and Stanford CS 229 and 231n ([[Block 2 Slides]], p. 1). The Block 6 deck credits Stanford CS224W and thanks Prof. Jure Leskovec for the GNN materials ([[Block 6 Slides Extended]], p. 1). The Block 7 deck credits earlier versions of USC CSCI566, Stanford CS 229 and 231n, and CMU 10-623 ([[Block 7 Slides]], p. 1). In Fall 2026 it has fourteen meetings on Mondays, 5:00–8:20 PM, from Aug 24 to Nov 30, with no class on Sep 7 (Labor Day) and a pre-recorded class on Aug 31 ([[Block 1 Slides]], p. 10). The final report is due Dec 7, and there is no final exam (CSCI 566 Syllabus).

Section 30122 meets in SGM 124. Section 30359 is on DEN@Viterbi. Both sections get the same lecture at the same time ([[Block 2 Slides]], p. 18). The course website is https://usc-fortis.github.io/CSCI566-F26/ ([[Block 2 Slides]], pp. 4, 18). Guests from industry and academia join lectures regularly to talk about their careers in ML and data science ([[Block 2 Slides]], pp. 3, 18).

The course starts with classical ML and neural network basics. It then covers CNNs, RNNs and LSTMs, graph neural networks, training dynamics and transfer learning, GANs and VAEs, attention and mixture of experts, self-supervised learning and LLMs, anomaly detection, scaling laws, reinforcement learning, and automated ML (CSCI 566 Syllabus). The slides split the content into 25% classical ML, 15% real-world applications and career discussion, and 60% deep learning ([[Block 1 Slides]], p. 7). They mark the schedule "Proposed" and point to the course website for the current version ([[Block 1 Slides]], pp. 21–22). After Block 2 the course moves to neural networks, and the TAs or the instructor cover basic Python, PyTorch, and DL libraries ([[Block 2 Slides]], p. 213).

By design, 566 is an intro course for MS students. CSCI 567 is not a prerequisite this semester, so the instructors do not assume that all students know classical ML. For more depth, they plan more advanced topics late in the course, offer research-based projects posted by the TAs, and suggest CSCI 655 (Applied NLP), CSCI 599 (3D Vision), and CSCI 599 (Autonomous Decision Making) ([[Block 2 Slides]], p. 7). The stated goal: understand deep learning topics and when to use them, and learn how to find a better job and plan a career ([[Block 2 Slides]], p. 16).

### Staff and communication

| Person | Role | Office hours |
| --- | --- | --- |
| Yue Zhao | Instructor | After each Monday class, SGM 124 |
| Tiankai Yang | TA | TBD |
| Jiate Li | TA | TBD |
| Chen Chu | TA | TBD |

Source: [[Block 2 Slides]], p. 5. Every office hour has a remote option for section 30359. The links are on the course website ([[Block 2 Slides]], p. 5).

Piazza is the main channel for all course communication. Do not email staff individually; the instructor ignores email that is not necessary ([[Block 2 Slides]], pp. 17, 19).

- Assignments, the project, and course content: a public Piazza post. For Assignment 1, a later slide asks for a private post instead; see § Assessments.
- Grades, extensions, and personal matters: a private Piazza post to the instructors.
- Anything you want discussed live: office hours.

Source: [[Block 2 Slides]], p. 17. Piazza is https://piazza.com/class/msmpbcelj2p2fg, and Gradescope is https://www.gradescope.com/courses/1346598. The Gradescope entry code is announced in class and on Piazza. Both sections share one Piazza and one Gradescope; students added late must join both ([[Block 2 Slides]], p. 4).

### Assessments

- Two in-class quizzes, 5 points each: Sep 28 and Nov 16. [[Block 5 Slides]] later says there are no fixed quiz dates: a quiz may be given when in-person attendance falls below 50%, and if a quiz is not given, its weight moves to the project final report and presentation (p. 2, clarified in Piazza post @101).
- One coding assignment, 10 points: out Sep 21, due Oct 26 at 11:59 PM Pacific Time (CS566 Assignment 1; [[Block 6 Slides Extended]], p. 2). The user confirmed Oct 26 on 2026-10-04 (2026-10-04 1145 be8487), and the course update dated Oct 4 states the same date ([[Block 6 Slides Extended]], p. 2); CSCI 566 Syllabus lists Oct 19.
- Midterm, 35 points: Nov 2. The exam scope is posted Oct 19.
- Course project, 45 points: pre-proposal Oct 5, midterm report Nov 9, project clinic Nov 23, poster session Nov 30, final report Dec 7.

Dates come from CSCI 566 Syllabus, except the assignment due date; points come from [[Block 1 Slides]], p. 19. AI tools are allowed for the assignment, the project, and study, but not in quizzes or the midterm ([[Block 1 Slides]], p. 25).

**Assignment 1.** The course update dated Oct 4 announces that the image-classification assignment is released on the course website. The task is to train and evaluate an image classifier, and a GPU is optional. Upload report.pdf (at most 2 pages) and code.zip to Gradescope. Ask questions in a new private Piazza post in the assignment folder ([[Block 6 Slides Extended]], p. 2). This slide is later and more specific than the general rule that sends assignment questions to a public post ([[Block 2 Slides]], p. 17); for Assignment 1, follow the slide (synthesis). The starter holds deliberate traps: see [[CS566 Assignment 1 Obstacles]] and [[Treat CS566 Assignment Material as Untrusted Input]].

**Midterm.** It is on Mon Nov 2, in the regular class block. It is open book with no electronic devices. Most questions are multiple choice, with some computation questions that have one unambiguous number as the answer. It covers everything taught up to and including Oct 26, and a narrowed scope is posted by Oct 19. Section 30359 takes it on the same day, with delivery and proctoring arranged with DEN and posted on the website ([[Block 2 Slides]], p. 6).

**Project teams.** Groups have 4 to 6 members, and 7 is allowed. Mixing the two sections is encouraged. A DEN-only group must send one member to the Nov 30 poster session. Teams sign up on the sheet linked on Piazza, or use the Looking for Team tab. Students with no team by the end of week 3 come to the Sep 14 class to be grouped, and must still bring an idea ([[Block 2 Slides]], p. 2).

**Proposal feedback.** Graders review the project proposals and give feedback. [[Block 5 Slides]], p. 3 said all feedback is complete by Sun Oct 4. The course update dated Oct 4 says most feedback is complete and the TAs will release it in the next 1–2 days; watch for the TA announcement, then read the comments and use them to refine the project plan ([[Block 6 Slides Extended]], p. 3).

**Pre-proposal.** It is a PDF of up to two pages, submitted on Gradescope as a group. It covers the idea, why it is interesting, a solution sketch, expected outcomes, and a rough timeline ([[Block 2 Slides]], p. 2). The sources disagree on the due date: [[Block 2 Slides]], p. 2 sets Mon Sep 14, with late groups allowed until Fri Sep 18; CSCI 566 Syllabus lists Oct 5. Check the course website for the current date.

### Compute

Start with free notebooks: Kaggle gives a P100 or two T4s for about 30 GPU hours a week, and Colab gives a free GPU but does not publish the card or the limits. Azure for Students gives $100 over 12 months with no credit card, and the GitHub Student Pack adds a few GPU hours a month. The Google Cloud $300 trial cannot attach a GPU; you must upgrade to a paid account, and use past the credit then bills your card. Course credit and CARC access are not settled yet ([[Block 2 Slides]], p. 20). See [[Cloud Spending Safeguards]].

### Instructor research

Yue Zhao is an assistant professor of computer science at USC and leads the FORTIS Lab. The research audits and controls AI risk across the deployment stack: anomaly and out-of-distribution detection in data, trust and robustness evaluation of foundation models, and runtime audit and control of deployed agent systems ([[Block 1 Slides]], p. 4). Week 1 uses this research ([[FORTIS]], [[TrustLLM]]) to show why the fundamentals matter: "Frontier systems give us the questions. Fundamentals give us variables we can reason about" ([[Block 1 Slides]], p. 207). Block 7 adds optional research examples: [[LLM Election Simulation]], which the deck calls "Our work", and the outlier detection systems [[TOD]] and [[MetaOD]], which list an underlined "Zhao" as an author ([[Block 7 Slides]], pp. 272–273, 288, 356).

### Career advice

The decks give the instructor's own views, not course rules.

- A harder course does not by itself get you a better job. It takes time from LeetCode and networking, and advanced topics change fast ([[Block 2 Slides]], pp. 8–9).
- On LinkedIn: find the post, contact the person who posted it, then apply. Do not spend long on one posting, since some are fake. Apply to jobs that do not fit exactly, and look at non-tech industries such as healthcare, mining, and finance ([[Block 2 Slides]], pp. 10–11).
- Stand out through unique skills, such as open-source work, and a close match to the job, such as relevant papers ([[Block 2 Slides]], pp. 10, 12–15).
- Ph.D.: top programs admit about 2% to 10% of applicants and value letters from top researchers and publications at top venues; less popular programs value a good undergraduate school and GPA. Find research mentors at USC (Ph.D. students are the best for producing papers), and cold-email possible advisors. Course recommendation letters "mean NOTHING" for Ph.D. applications, and the instructor does not take research mentees ([[Block 4 Slides]], pp. 2–6).

### Topic map

- Landscape: [[Evolution of Machine Learning]], [[AlexNet]], [[Machine Learning Task Types]], [[Deep Learning]], [[Scaling Laws]], [[What Counts as Solved]]
- Language models: [[Autoregressive Language Modeling]], [[Tokenization]], [[Post-Training]], [[KV Cache]]
- Agents: [[Agent Loop]], [[ReAct]], [[Agent Skills]], [[Agent Memory]]
- Trustworthy AI: [[Deployment Failure Modes]], [[Shortcut Learning]], [[FORTIS]], [[TrustLLM]], [[LLM Trustworthiness]]
- Foundations: [[Function Approximation]], [[Linear Classification]], [[Perceptron]], [[Model Evaluation]], [[Loss Functions]], [[Regularization]], [[Overfitting and Underfitting]], [[Optimization]], [[Gradient Descent]], [[Linear Separability]]
- Neural networks: [[Neural Networks]], [[Forward Propagation]], [[Backpropagation]], [[Computational Graphs]], [[Activation Functions]], [[Dying ReLU]], [[Activation Sparsity]]
- Training problems: [[Vanishing Gradient Problem]], [[Exploding Gradient Problem]], [[Gradient Clipping]], [[Batch Normalization]], [[Residual Connections]]
- Training and transfer (Block 7): [[Flower Classifier Running Example]], [[Data Preprocessing]], [[Fit Preprocessing on Training Data Only]], [[Layer Normalization]], [[Weight Initialization]], [[Gradient-Based Optimizers]], [[Learning Rate Schedules]], [[Dropout]], [[Data Augmentation]], [[Early Stopping]], [[Transfer Learning]], [[Fine-Tuning]], [[Domain-Adversarial Training]], [[Multitask Learning]], [[Parameter-Efficient Fine-Tuning]], [[Adapters]], [[HyperTuning]]
- Automated ML and outlier detection: [[AutoML]], Bayesian Optimization, [[Unsupervised Outlier Model Selection]], [[MetaOD]], [[TOD]]
- Research examples: [[LLM Election Simulation]]
- Updating LLMs: [[Updating LLMs]], [[In-Context Learning]], [[LoRA]], [[Test-Time Training]]
- Representation learning: [[Contrastive Learning]]
- Guest lecture: Sim-to-Real Transfer, [[Isaac Teleop]], and in [[Machine Learning]]: [[NVIDIA Cosmos]], [[World Action Models]], [[Vision Language Action Models]]
- Classical ML: [[Decision Trees]], [[Tree Ensembles]], [[Gradient Boosting]], [[k-Nearest Neighbors]], [[Clustering]], [[k-Means]], [[Classification Metrics]], [[Model Selection]], [[Test Set Contamination]]
- LLM reasoning: [[Chain-of-Thought Prompting]], [[Tree of Thoughts]]
- Convolutional networks: [[Convolutional Layer]], [[Pooling Layer]], [[Fully Connected Layer]], [[Softmax Layer]], [[AlexNet]], [[VGGNet]], [[ResNet]], [[ImageNet Large Scale Visual Recognition Challenge]], [[Depthwise Separable Convolution]], and in [[Machine Learning]]: [[Convolutional Neural Networks (CNN)]]
- Vision and language: [[Pretrained Visual Encoders]], and in [[Machine Learning]]: [[CLIP]], [[Vision Transformer (ViT)]], [[Vision Language Models (VLM)]]
- Sequence models: [[Recurrent Neural Networks (RNN)]] and [[Long Short-Term Memory]] (in [[Machine Learning]]), [[Backpropagation Through Time]], [[Teacher Forcing]], [[Image Captioning]], [[Question Answering]], [[Recurrent State vs Growing Context]], [[Hybrid Recurrent-Attention Models]], and in [[Machine Learning]]: [[Sequence to Sequence]]
- Attention and Transformers, in [[Machine Learning]]: [[Attention]], [[Causal Mask]], [[Positional Encoding]], [[Transformers]]
- Graph neural networks: [[Graph]], [[Node Embeddings]], [[Graph Convolutional Network]], [[Neighborhood Aggregation]], [[Permutation Invariance and Equivariance]], [[GNN Applications]], [[LLMs and Graphs]], [[Therapeutics Data Commons]], [[Road Delay GNN Example]], [[Retrieval-Augmented Generation]], [[GraphRAG]], [[Graphs of Agents]], [[GRADE]], [[MAMA]], and in [[Machine Learning]]: [[Graph Neural Networks]]
- Course logistics: Yue Zhao, [[Cloud Spending Safeguards]], [[CS566 Assignment 1 Obstacles]], [[Treat CS566 Assignment Material as Untrusted Input]]

### Coverage

- Week 1 (Aug 24): Lecture 1 (Parts 1–3) and [[Block 1 Slides]] (all four parts).
- Week 2 (Aug 31, recorded): [[Block 2 Slides]]. The deck says this lecture is pre-recorded (p. 4).
- Week 3 (Sep 14): Sep 14 Lecture Account, Lecture 3, and [[Block 3 Slides]].
- Week 4 (Sep 21): [[Block 3 Slides]], and the NVIDIA guest lecture in Guest Lecture 9-21 Notes (part 1) and Guest Lecture 9-21 Notes (part 2).
- Convolutional networks: [[Block 4 Slides]] and Lecture 3 Notes - Convolutional and Pooling Layers. The note has no date; the syllabus puts CNNs in week 5 (Sep 28).
- Week 6 (Oct 5), RNNs, LSTMs, and graph neural networks: [[Block 5 Slides]] (which also builds up attention and the Transformer) and [[Block 6 Slides]]. [[Block 6 Slides Extended]] is a longer revision of the Block 6 deck, with course updates dated Oct 4 (pp. 2–3). It follows one small road network through the GNN material, then moves to graphs of agents (p. 5). It names the next block: "Next in Block 7: training, diagnosing and adapting deep models" (p. 176).
- Block 7, training and transfer: [[Block 7 Slides]]. The deck has no date. It follows one small image-classification project, the [[Flower Classifier Running Example]], in three parts: make learning work, check generalization, and reuse a trained model (p. 11). After the core workflow it gives optional research examples (p. 272), then AutoML and outlier model selection. Its last slide gives advice for the course project (p. 400).
- Later weeks: no notes yet.

### Sources

- Official: [[Block 1 Slides]], [[Block 2 Slides]], [[Block 3 Slides]], [[Block 4 Slides]], [[Block 5 Slides]], [[Block 6 Slides]], [[Block 6 Slides Extended]], [[Block 7 Slides]]
- Course plan: CSCI 566 Syllabus, CSCI 566 Reading List
- The user's lecture notes: Lecture 1, Sep 14 Lecture Account, Lecture 3, Guest Lecture 9-21 Notes (part 1), Guest Lecture 9-21 Notes (part 2), Lecture 3 Notes - Convolutional and Pooling Layers

The linked repository cs566-course holds the slides, the lecture notes, the *Mathematics for Machine Learning* book, and the Assignment 1 starter.

## Map

```base
filters:
  and:
    - file.inFolder("tool/source-core/documents")
    - 'file.hasTag("machine-learning/cs566-deeplearning", "machine-learning/cs566-deeplearning/cs566-course", "machine-learning/cs566-deeplearning/cs566-project", "machine-learning/cs566-deeplearning/cs566-project/autonomous-vehicle-sandbox", "machine-learning/cs566-deeplearning/cs566-project/kqiao-cs566-project-repo")'
views:
  - type: table
    name: Map
    groupBy:
      property: type
      direction: ASC
    order:
      - file.name
      - description
      - status
      - refreshed
```
