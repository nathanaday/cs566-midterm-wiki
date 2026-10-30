---
description: "The CSCI 566 Block 2 slide deck on classical ML by Yue Zhao, for week 2: decision trees, tree ensembles, k-nearest neighbors, clustering, and model metrics, with detours to chain-of-thought, Tree of Thoughts, and classical ML inside LLM agents."
---

> [!source] PDF · 213 pages · official
> Captured 2026-09-28 from `Block 2 Slides.pdf` (ingest) · absorbed by 2026-09-28 Ingest the CS566 Block 2 and Block 4 slides (2)

![[internal/wiki/originals/c33d56ad8e5837ca.pdf]]

## Summary

The CSCI 566 deck "Block 2: Classical ML Algorithms", by the instructor Yue Zhao. It has 213 PDF pages. It opens with course logistics and career advice, recaps the linear model from [[Block 1 Slides]], and then teaches decision trees, tree ensembles, k-nearest neighbors, clustering, and model metrics. Short detours connect each classical method to current LLM and agent systems: chain-of-thought and Tree of Thoughts after decision trees, kNN-LM and semantic caching after kNN, LLM-guided clustering after k-means, and classical classifiers in the agent control plane at the end. The deck says the week-2 lecture (Aug 31) is pre-recorded (p. 4). Most slides credit Stanford CS 229, CMU 10601, or Stanford CS 329P. Locators are PDF page numbers.

## Structure

- pp. 1–20, logistics and career advice: project teams, the pre-proposal, Piazza and Gradescope, office hours, the midterm, course goals, job search, and compute credits: [[CS566-DeepLearning]], Yue Zhao, Cloud Spending Safeguards.
- pp. 21–29, recap of the linear model, loss, and optimization: [[Linear Classification]], [[Loss Functions]], Optimization.
- pp. 30–103, decision trees: the loan example, stumps, classification error, greedy learning, stopping conditions, threshold splits, splitting criteria, and pruning: [[Decision Trees]].
- pp. 82–100, overfitting, model and data complexity, model selection, memorization, test set contamination, and ridge and lasso: [[Overfitting and Underfitting]], Model Selection, Test Set Contamination, [[Regularization]].
- pp. 104–112, ensembles: bias and variance, bagging, random forests, gradient boosting, and tabular baselines: Tree Ensembles, Gradient Boosting.
- pp. 113–134, optional detour on search inside a language model: Chain-of-Thought Prompting, Tree of Thoughts.
- pp. 135–140, model metrics and guardrail classifiers: [[Model Evaluation]], Classification Metrics.
- pp. 141–182, k-nearest neighbors, hyperparameter selection, cross-validation, and nearest neighbors in LLM systems: [[k-Nearest Neighbors]], [[Model Evaluation]].
- pp. 183–211, clustering, k-means, CuraWeb deduplication, and LLM-guided few-shot clustering: [[Clustering]], [[k-Means]].
- pp. 212–213, classical ML in the agent loop, and the move to neural networks: Agent Loop.
