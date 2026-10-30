---
description: "The CSCI 566 practice of training a neural network: gradient problems, normalization and initialization, data preparation, optimizers, regularization, and transfer from trained models."
sources: ["[[Vanishing Gradient Problem]]", "[[Exploding Gradient Problem]]", "[[Weight Initialization]]", "[[Batch Normalization]]", "[[Layer Normalization]]", "[[Data Preprocessing]]", "[[Data Augmentation]]", "[[Gradient-Based Optimizers]]", "[[Dropout]]", "[[Early Stopping]]", "[[Transfer Learning]]", "Change One Factor per Experiment"]
---

## Definition

Training a neural network chooses its weights by gradient-based optimization of a loss over the training data ([[Gradient Descent]], [[Loss Functions]]). CSCI 566 teaches it as a set of problems that stop training from working or from generalizing, each with the methods that answer it. This page gathers them; each linked topic holds the claims and their citations.

## Explanation

### Gradient problems

- [[Vanishing Gradient Problem]]: in backpropagation, the gradient for early layers shrinks toward zero when many small local derivatives multiply, so those layers learn slowly or not at all.
- [[Exploding Gradient Problem]]: when the gradient becomes too large, a gradient descent step overshoots to a high-loss configuration or fills the network with Inf or NaN values.
- [[Weight Initialization]]: weight initialization sets the starting scale of a network's weights, such as small random numbers, Xavier (std = 1/sqrt(Din)), or He/Kaiming (std = sqrt(2/Din)), so that activations and gradients keep a usable scale across layers.
- [[Batch Normalization]]: A layer that normalizes each channel of a batch to zero mean and unit variance and then applies a learned scale and shift.
- [[Layer Normalization]]: A normalization layer that normalizes the features within one example or token, not one feature across a mini-batch as batch normalization does.

### Data

- [[Data Preprocessing]]: data preprocessing transforms input data before training.
- [[Data Augmentation]]: A regularizer that applies random, label-preserving transformations (flips, crops and scales, color jitter, learned AutoAugment policies) to each training image before the network sees it, while the label stays the same.

### Optimizers

- [[Gradient-Based Optimizers]]: the update rules that turn gradients into parameter steps (SGD, SGD + Momentum, AdaGrad, RMSProp, Adam, and AdamW), compared by what each remembers and how it scales each step.

### Generalization

- [[Dropout]]: A regularizer that sets a random subset of hidden activations to zero in each training forward pass, then turns the mask off at evaluation and uses a classic or inverted scaling convention so that training and evaluation scales match.
- [[Early Stopping]]: early stopping keeps the checkpoint with the best value of a chosen validation metric instead of the last training checkpoint.

### Reuse of trained models

- [[Transfer Learning]]: transfer learning starts a model from representations learned on other (source) data instead of training from scratch.

### Practice

- Change One Factor per Experiment: in CSCI 566 training and tuning experiments, keep the data split, metric, and compute budget the same, change one factor per run so the cause of a result is clear, and record the setting and outcome of every run.

## Related

- [[Neural Networks]]: the broader subject
- Machine Learning: the broader subject

## Sources

- [[Vanishing Gradient Problem]]
- [[Exploding Gradient Problem]]
- [[Weight Initialization]]
- [[Batch Normalization]]
- [[Layer Normalization]]
- [[Data Preprocessing]]
- [[Data Augmentation]]
- [[Gradient-Based Optimizers]]
- [[Dropout]]
- [[Early Stopping]]
- [[Transfer Learning]]
- Change One Factor per Experiment
