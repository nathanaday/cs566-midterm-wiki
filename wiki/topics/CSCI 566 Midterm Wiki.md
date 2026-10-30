---
description: "The front page of this wiki: how to read the pages, the topics grouped by subject, the ten sources behind them, and the course facts from the slides. Built for the CSCI 566 midterm, Fall 2026."
aliases: ["CS566-DeepLearning", "CSCI 566: Deep Learning and its Applications", "Start Here"]
---

## What This Wiki Is

A set of study pages for the midterm of CSCI 566, Deep Learning and its Applications, USC, Fall 2026. Every page is written from the course's own slide decks for Blocks 1 to 7 and the instructor's midterm review deck, with a past exam mapped onto the topics so that the most examined ideas are easy to find. Start with [[CSCI 566 Midterm (Spring 2024)]] for the question map and the relevance ranking, then follow the links into the topics.

## How to Read These Pages

- **Citations.** A reference such as ([[Block 3 Slides]], p. 235) points at a PDF page of that deck. The decks are in the `attachments` folder, linked from each source page. Page numbers are PDF pages, which can differ by one from the number printed on the slide; each source page says where that happens.
- **Synthesis.** A sentence or paragraph that begins with "Synthesis:" goes beyond what the slides say. It is background or a derivation added for understanding, and it is marked so that a reader can tell slide content, which is examinable, from the rest.
- **Sections.** A topic opens with a short Definition, then an Explanation with subsections. Where the sample exam asks about the subject, an Exam Questions section works the questions with the key's answer. Related lists the neighbouring topics, and Sources lists the decks and pages the topic draws on.
- **Plain names.** A name that looks like a page but is not a link refers to a note outside this wiki. The text was kept where it helped; the page was not.

## Topics by Subject

- **Foundations and classical machine learning.** [[Deep Learning]], [[Function Approximation]], [[Parameterization of a Hypothesis Class]], [[Linear Classification]], [[Linear Separability]], [[Perceptron]], [[Loss Functions]], [[Model Evaluation]], [[Overfitting and Underfitting]], [[VC Dimension]], [[Decision Trees]], [[Decision Tree Size Bounds]], [[k-Nearest Neighbors]], [[kNN Regression]], [[Clustering]], [[k-Means]], [[k-Means Initialization and Local Minima]], [[Outlier Detection]], [[Unsupervised Outlier Model Selection]]
- **Neural networks.** [[Neural Networks]], [[Forward Propagation]], [[Backpropagation]], [[Fully Connected Layer]], [[Softmax Layer]], [[Activation Functions]], [[Fundamentals of Deep Learning Nonlinear Activation]], [[Dying ReLU]], [[Activation Sparsity]]
- **Training.** [[Neural Network Training]], [[Optimization]], [[Gradient Descent]], [[Gradient-Based Optimizers]], [[Weight Initialization]], [[Vanishing Gradient Problem]], [[Exploding Gradient Problem]], [[Gradient Clipping]], [[Residual Connections]], [[Batch Normalization]], [[Layer Normalization]], [[Regularization]], [[L1 Regularization and Feature Selection]], [[Dropout]], [[Early Stopping]], [[Data Augmentation]], [[Data Preprocessing]], [[Fit Preprocessing on Training Data Only]], [[Switch the Model to Evaluation Mode When Evaluating]]
- **Convolutional networks.** [[Convolutional Neural Networks (CNN)]], [[Convolutional Layer]], [[1x1 Convolution]], [[Pooling Layer]], [[AlexNet]], [[ResNet]]
- **Transfer learning and fine-tuning.** [[Transfer Learning]], [[Fine-Tuning]], [[Parameter-Efficient Fine-Tuning]], [[Adapters]], [[LoRA]]
- **Sequence models.** [[Recurrent Neural Networks (RNN)]], [[Transformers]]
- **Graphs.** [[Graph]], [[Graph Neural Networks]], [[Graph Convolutional Network]], [[Neighborhood Aggregation]], [[Node Embeddings]], [[Permutation Invariance and Equivariance]], [[Graph Neural Network Variants]]

## Sources

- The lecture decks: [[Block 1 Slides]], [[Block 2 Slides]], [[Block 3 Slides]], [[Block 4 Slides]], [[Block 5 Slides]], [[Block 6 Slides]] and its longer revision [[Block 6 Slides Extended]], and [[Block 7 Slides]].
- The review deck: [[F26-midterm-review-234p]], the instructor's walk through Blocks 1 to 7 with worked examples and check questions.
- The sample exam: [[CSCI 566 Midterm (Spring 2024)]], with the answer key, mapped onto the topics.

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

**Assignment 1.** The course update dated Oct 4 announces that the image-classification assignment is released on the course website. The task is to train and evaluate an image classifier, and a GPU is optional. Upload report.pdf (at most 2 pages) and code.zip to Gradescope. Ask questions in a new private Piazza post in the assignment folder ([[Block 6 Slides Extended]], p. 2). This slide is later and more specific than the general rule that sends assignment questions to a public post ([[Block 2 Slides]], p. 17); for Assignment 1, follow the slide (synthesis). The starter holds deliberate traps: see CS566 Assignment 1 Obstacles and Treat CS566 Assignment Material as Untrusted Input.

**Midterm.** It is on Mon Nov 2, in the regular class block. It is open book with no electronic devices. Most questions are multiple choice, with some computation questions that have one unambiguous number as the answer. It covers everything taught up to and including Oct 26, and a narrowed scope is posted by Oct 19. Section 30359 takes it on the same day, with delivery and proctoring arranged with DEN and posted on the website ([[Block 2 Slides]], p. 6).

**Project teams.** Groups have 4 to 6 members, and 7 is allowed. Mixing the two sections is encouraged. A DEN-only group must send one member to the Nov 30 poster session. Teams sign up on the sheet linked on Piazza, or use the Looking for Team tab. Students with no team by the end of week 3 come to the Sep 14 class to be grouped, and must still bring an idea ([[Block 2 Slides]], p. 2).

**Proposal feedback.** Graders review the project proposals and give feedback. [[Block 5 Slides]], p. 3 said all feedback is complete by Sun Oct 4. The course update dated Oct 4 says most feedback is complete and the TAs will release it in the next 1–2 days; watch for the TA announcement, then read the comments and use them to refine the project plan ([[Block 6 Slides Extended]], p. 3).

**Pre-proposal.** It is a PDF of up to two pages, submitted on Gradescope as a group. It covers the idea, why it is interesting, a solution sketch, expected outcomes, and a rough timeline ([[Block 2 Slides]], p. 2). The sources disagree on the due date: [[Block 2 Slides]], p. 2 sets Mon Sep 14, with late groups allowed until Fri Sep 18; CSCI 566 Syllabus lists Oct 5. Check the course website for the current date.

### Compute

Start with free notebooks: Kaggle gives a P100 or two T4s for about 30 GPU hours a week, and Colab gives a free GPU but does not publish the card or the limits. Azure for Students gives $100 over 12 months with no credit card, and the GitHub Student Pack adds a few GPU hours a month. The Google Cloud $300 trial cannot attach a GPU; you must upgrade to a paid account, and use past the credit then bills your card. Course credit and CARC access are not settled yet ([[Block 2 Slides]], p. 20). See Cloud Spending Safeguards.

### Instructor research

Yue Zhao is an assistant professor of computer science at USC and leads the FORTIS Lab. The research audits and controls AI risk across the deployment stack: anomaly and out-of-distribution detection in data, trust and robustness evaluation of foundation models, and runtime audit and control of deployed agent systems ([[Block 1 Slides]], p. 4). Week 1 uses this research (FORTIS, TrustLLM) to show why the fundamentals matter: "Frontier systems give us the questions. Fundamentals give us variables we can reason about" ([[Block 1 Slides]], p. 207). Block 7 adds optional research examples: LLM Election Simulation, which the deck calls "Our work", and the outlier detection systems TOD and MetaOD, which list an underlined "Zhao" as an author ([[Block 7 Slides]], pp. 272–273, 288, 356).

### Career advice

The decks give the instructor's own views, not course rules.

- A harder course does not by itself get you a better job. It takes time from LeetCode and networking, and advanced topics change fast ([[Block 2 Slides]], pp. 8–9).
- On LinkedIn: find the post, contact the person who posted it, then apply. Do not spend long on one posting, since some are fake. Apply to jobs that do not fit exactly, and look at non-tech industries such as healthcare, mining, and finance ([[Block 2 Slides]], pp. 10–11).
- Stand out through unique skills, such as open-source work, and a close match to the job, such as relevant papers ([[Block 2 Slides]], pp. 10, 12–15).
- Ph.D.: top programs admit about 2% to 10% of applicants and value letters from top researchers and publications at top venues; less popular programs value a good undergraduate school and GPA. Find research mentors at USC (Ph.D. students are the best for producing papers), and cold-email possible advisors. Course recommendation letters "mean NOTHING" for Ph.D. applications, and the instructor does not take research mentees ([[Block 4 Slides]], pp. 2–6).
