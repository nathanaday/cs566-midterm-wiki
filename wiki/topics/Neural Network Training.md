---
description: "The CSCI 566 practice of training a neural network: gradient problems, normalization and initialization, data preparation, optimizers, regularization, and transfer from trained models."
sources: ["[[Vanishing Gradient Problem]]", "[[Exploding Gradient Problem]]", "[[Weight Initialization]]", "[[Batch Normalization]]", "[[Layer Normalization]]", "[[Data Preprocessing]]", "[[Data Augmentation]]", "[[Gradient-Based Optimizers]]", "[[Dropout]]", "[[Early Stopping]]", "[[Transfer Learning]]", "Change One Factor per Experiment"]
subject: 3 Training
---

## Definition

Training chooses the weights of a network by [[Gradient Descent]] on a loss over the training data ([[Loss Functions]]). This page is the map: the loop, the knobs, the failure signs, and the detailed pages that hold each method.

### Training Loop

1. Preprocess the data: zero-center and scale with statistics fit on the training split only ([[Data Preprocessing]]).
2. Initialize the weights at a scale that keeps activations alive ([[Weight Initialization]]).
3. Sample a minibatch and apply augmentation ([[Data Augmentation]]).
4. Forward pass: compute the loss, including any penalty $\lambda R(W)$ ([[Regularization]]).
5. Backward pass: compute $dW$ for every parameter ([[Backpropagation]]).
6. Clip the gradient if its norm exceeds the threshold ([[Gradient Clipping]]).
7. Step with the optimizer ([[Gradient-Based Optimizers]]).
8. Evaluate on the validation split; keep the best checkpoint ([[Early Stopping]]).

**Update rule.**

$$W \leftarrow W - \eta \cdot dW$$

**Regularized loss.**

$$L = \frac{1}{N} \sum_{i=1}^{N} L_i(f(x_i; W), y_i) + \lambda R(W)$$

| Parameter              | Rule of thumb                                                      |
| ---------------------- | ------------------------------------------------------------------ |
| Learning rate $\eta$   | Tune first; every optimizer needs one                              |
| Optimizer              | SGD + Momentum for vision, AdamW for Transformers                  |
| Batch size             | Larger batches: less gradient noise, fewer steps per epoch         |
| Weight decay $\lambda$ | L2 penalty under SGD; decoupled decay under AdamW                  |
| Dropout rate           | Train with mask, evaluate without; match the scale                 |
| Initialization         | Xavier: $\sigma = 1/\sqrt{D_{in}}$; He: $\sigma = \sqrt{2/D_{in}}$ |
| Schedule               | Decay $\eta$ over training                                         |


### Symptoms and Remedies

| Loss curve | Diagnosis | Remedy |
| --- | --- | --- |
| Blows up, NaN or Inf | $\eta$ too high or [[Exploding Gradient Problem]] | Lower $\eta$, [[Gradient Clipping]] |
| Falls fast, then plateaus high | $\eta$ too high | Lower $\eta$ or add a schedule |
| Falls very slowly | $\eta$ too low | Raise $\eta$ |
| Stuck near initial loss | Dead units or [[Vanishing Gradient Problem]] | Fix init, use ReLU, add [[Batch Normalization]] |
| Train falls, validation rises | Overfitting | [[Regularization]], [[Dropout]], [[Data Augmentation]], [[Early Stopping]] |
| Both stay high | Underfitting | Larger model, longer training |

### Normalization and Scale

- [[Batch Normalization]] normalizes each channel across the minibatch, then applies a learned scale and shift; it uses running statistics at evaluation.
- [[Layer Normalization]] normalizes the features within one example, so it does not depend on batch size.
- [[Weight Initialization]] and normalization both aim to keep the activation and gradient scale constant across depth.

> [!tip]
> Batch norm and dropout behave differently in train and eval mode. Forgetting to switch modes changes the output.

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
