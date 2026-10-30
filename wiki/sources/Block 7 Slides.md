---
id: doc-dwhmj6
type: source
description: "The CSCI 566 Block 7 deck by Yue Zhao on training and transfer (400 PDF pages): preprocessing, activations, initialization, optimizers, learning rate schedules, regularization, hyperparameter choice, transfer learning, fine-tuning and PEFT, then optional research examples (an LLM election study, TOD) and AutoML with Bayesian optimization and MetaOD."
tags: [machine-learning/cs566-deeplearning/cs566-course]
aliases: []
created: 2026-10-12T15:30:15
updated: 2026-10-12T16:59:46
refreshed: 2026-10-12T16:59:46
authority: official
status: absorbed
file: "[[internal/wiki/originals/33a91ec2d18df0a3.pdf]]"
media: pdf
sha256: 33a91ec2d18df0a3d28c4b319dd790406056b1f14c4c95eb283b88c63cd72680
origin: ingest
locator: F26-block7-training-transfer-432p.pdf
measure: 400 pages
captured: 2026-10-12T15:30:15
---

> [!source] PDF · 400 pages · official
> Captured 2026-10-12 from `F26-block7-training-transfer-432p.pdf` (ingest) · absorbed by 2026-10-12 Ingest the CS566 Block 7 slides

![[internal/wiki/originals/33a91ec2d18df0a3.pdf]]

## Summary

The CSCI 566 deck "Block 7: Training a Model That Works", by the instructor Yue Zhao. The file name in the course repository says "432p", but the PDF has 400 pages. The deck has no date. It credits earlier versions of USC CSCI566, Stanford CS 229 and 231n, and CMU 10-623.

The deck follows one small image-classification project, the [[Flower Classifier Running Example]], in three parts (p. 11):

- Make learning work: data preprocessing, normalization layers, activations, weight initialization, optimizers, and learning rate schedules.
- Check generalization: training and validation curves, early stopping, regularization, data augmentation, and the choice of hyperparameters.
- Reuse a trained model: transfer learning with CNNs, fine-tuning, domain-adversarial and multitask learning, in-context learning against fine-tuning, and parameter-efficient fine-tuning (adapters, prefix tuning, LoRA, HyperTuning).

After the core workflow (p. 271), the deck gives optional research examples: an LLM election simulation and TOD, a tensor-based outlier detection system. Then it covers AutoML: hyperparameter optimization, grid and random search, Bayesian optimization, meta-learning for unsupervised outlier model selection (MetaOD, MetaOOD), and neural architecture search. The last slide gives advice for the course project (p. 400).

Notes on reading the deck:

- The printed slide numbers match the PDF pages at first, then drift (for example, PDF p. 281 shows slide 285, and p. 400 shows slide 412). The wiki cites PDF pages.
- Many slides say "Sources and assumptions in speaker notes". The PDF does not hold the speaker notes.
- Many numbers on the flower slides are marked as illustrative or toy values for teaching.

## Structure

- pp. 1–12, title, a recap of earlier blocks, the lecture plan, and the flower example: [[CS566-DeepLearning]], [[Flower Classifier Running Example]].
- pp. 13–18, cross-entropy, one training step, mini-batches and epochs, the three data splits, and feature scales: [[Loss Functions]], [[Backpropagation]], [[Model Evaluation]].
- pp. 19–41, data preprocessing, batch and layer normalization, the input convention of a pretrained model, missing data, and StandardScaler: [[Data Preprocessing]], [[Fit Preprocessing on Training Data Only]], [[Batch Normalization]], [[Layer Normalization]], [[Test Set Contamination]].
- pp. 42–55, a recap of activation functions and how to choose one: [[Activation Functions]], [[Dying ReLU]].
- pp. 56–83, weight initialization: zero, small random, Xavier, and He/Kaiming: [[Weight Initialization]], [[ResNet]].
- pp. 84–117, gradient descent, the learning rate, SGD and its problems, momentum, AdaGrad, RMSProp, Adam, and AdamW: [[Gradient Descent]], [[Optimization]], [[Gradient-Based Optimizers]].
- pp. 118–129, learning rate schedules, warmup, cyclical rates, and PyTorch schedulers: [[Learning Rate Schedules]].
- pp. 130–137, training and validation curves, checkpoint selection, early stopping, and ensembles: [[Overfitting and Underfitting]], [[Early Stopping]].
- pp. 138–170, weight penalties, dropout, data augmentation, DropConnect, stochastic depth, cutout, mixup, and evaluation rules: [[Regularization]], [[Dropout]], [[Data Augmentation]].
- pp. 171–190, controlled experiments and the procedure for choosing hyperparameters: [[Model Selection]], [[Change One Factor per Experiment]], [[Model Evaluation]].
- pp. 191–210, transfer learning with CNNs: a frozen backbone, DeCAF, the size-and-similarity guide, and pretraining as the norm: [[Transfer Learning]], [[Fine-Tuning]], [[AlexNet]], [[Convolutional Neural Networks (CNN)]], [[Image Captioning]], [[ImageNet Large Scale Visual Recognition Challenge]], [[Pretrained Visual Encoders]].
- pp. 211–226, the transfer taxonomy, layer transfer, domain shift, multitask learning, domain-adversarial training, and zero-shot learning: [[Transfer Learning]], [[Multitask Learning]], [[Domain-Adversarial Training]], [[Machine Learning Task Types]].
- pp. 227–240, fine-tuning LLMs against in-context learning, and the PEFT approaches: [[In-Context Learning]], [[Fine-Tuning]], [[Parameter-Efficient Fine-Tuning]].
- pp. 241–263, the Transformer recap, encoder-only models and BERT, adapters, LoRA, LLM sizes, and intrinsic dimension: [[Transformers]], [[Adapters]], [[LoRA]], [[Parameter-Efficient Fine-Tuning]]
- pp. 264–271, HyperTuning and the complete flower workflow: [[HyperTuning]], [[Updating LLMs]], [[Flower Classifier Running Example]].
- pp. 272–287, optional research example: the LLM election simulation: [[LLM Election Simulation]].
- pp. 288–310, optional research example: TOD and provable quantization: [[TOD]].
- pp. 311–340, AutoML, model search, hyperparameter optimization, grid and random search, search budgets, and prediction-based tuning: [[AutoML]], [[Model Selection]], Bayesian Optimization.
- pp. 341–351, the Bayesian optimization walkthrough on the flower learning rate: Bayesian Optimization.
- pp. 352–396, meta-learning, unsupervised outlier model selection, MetaOD, MetaOOD, and the table of automated OD/OOD methods: [[Unsupervised Outlier Model Selection]], [[MetaOD]].
- pp. 397–400, neural architecture search, NAS benchmarks, and training choices for the project: [[AutoML]], [[Flower Classifier Running Example]].
