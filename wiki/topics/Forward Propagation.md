---
id: con-4cc83q
type: topic
kind: concept
description: Computing a neural network's output from its input one layer at a time, and saving the intermediate values that backpropagation needs.
tags: [machine-learning/cs566-deeplearning]
aliases: [Forward Pass]
created: 2026-09-28T00:00:00
updated: 2026-10-19T17:48:15
refreshed: 2026-10-19T17:48:15
status: stable
sources: ["[[Block 3 Slides]]", "Lecture 3", "[[F26-midterm-review-234p]]"]
up: ["[[Neural Networks]]"]
---

> [!concept] Concept
> 3 sources · refreshed 2026-10-19 · #machine-learning/cs566-deeplearning
> Up: [[Neural Networks]]

## Definition

Forward propagation computes a network's output from its input, one layer at a time, from left to right. Each layer's outputs feed the units of the next layer. The slides build one network (input X, three hidden layers, output Y) one unit at a time ([[Block 3 Slides]], pp. 36-55). The user's lecture notes put it this way: "The forward pass is quite simple: all calculations from each layer are passed to the next layer" (Lecture 3, § Forward Propagation).

Each hidden unit applies a non-linear function to a weighted sum of the previous layer's outputs. The slides show a "logistic neuron" with weights $w_0$ to $w_3$ and a sigmoid. The notes on the slide say the sigmoid "can be other non-linear choices" and "each neuron is associated w/ the weight matrix W" ([[Block 3 Slides]], p. 42).

The summary slide on [[Backpropagation]] adds that the forward pass must "compute the result of an operation and save any intermediates needed for gradient computation in memory" (p. 207).

## Explanation

The network runs forward propagation at inference time. The slides label it "Inference (forward pass)" (p. 35). During training it runs first; then [[Backpropagation]] computes the gradients and [[Gradient Descent]] updates the weights. See [[Neural Networks]] for the layer formulas and weight shapes.

### What to track in each layer

The CSCI 566 midterm review states what makes each forward layer concrete: "Track tensor shapes through each layer, and separate trainable parameters from computed activations" ([[F26-midterm-review-234p]], p. 37). The trainable parameters are the weights and the biases. "Inputs and activations are recomputed per example, and ReLU has no trainable parameters" (p. 41). [[Neural Networks]] gives the shape rule and a parameter count.

The review also names a change of convention: "Some source slides use row vectors xW; new formulas here use column vectors Wx, and parameter counts are the same" (p. 37).

Without a nonlinearity, the layers of a forward pass simplify to one layer: "Stacking affine layers without a nonlinearity still gives one affine map" (p. 37). See [[Fundamentals of Deep Learning Nonlinear Activation]].

### Worked example: one tiny 2-2-1 network

The slides work one small network: 2 inputs, 2 ReLU hidden units, 1 linear output ([[Block 3 Slides]], p. 67).

- Sample: $x = (1, 2)$, label $y = 2$.
- Hidden unit 1: $w = (1, 0.5)$, $b = -0.5$. Hidden unit 2: $w = (-1, 1)$, $b = 0$. Rule: $h = \max(0, z)$.
- Output: $v = (1, -0.5)$, $c = 0$.

The midterm review uses the same network two times. First it puts every value on one diagram. "All values live on the object that uses them": the inputs in the input nodes, the weights on their edges, the biases beside the hidden nodes, and the target beside the output. "Read each multiplication from an edge and each sum at the receiving node." "One fixed diagram will carry the full forward, loss, gradient, and update sequence" ([[F26-midterm-review-234p]], p. 45). Later it names the network "A 2-2-1 Network for a Regression Toy" and writes the model as equations, with target $t = 2$ (p. 87):

$$z_i = \sum_j w_{ij} x_j + b_i, \qquad h_i = \max(0, z_i), \qquad \hat y = v_1 h_1 + v_2 h_2 + c, \qquad L = (\hat y - t)^2$$

$W$ maps input to hidden, and $v$ maps hidden to output (p. 87).

| Step | Calculation | Block 3 page | Review page |
| --- | --- | --- | --- |
| Hidden values | $z_1 = 1(1) + 0.5(2) - 0.5 = 1.5$, $h_1 = 1.5$; $z_2 = -1(1) + 1(2) + 0 = 1$, $h_2 = 1$ | 68 | 46, 88 |
| Output | $\hat y = 1(1.5) + (-0.5)(1) + 0 = 1.0$ | 69 | 47, 88 |
| Loss | $L = (\hat y - y)^2 = (1 - 2)^2 = 1$ | 70 | 48, 88 |
| Direction check | $v_1 = 1.2$ gives $L = 0.49$; $v_1 = 0.8$ gives $L = 1.69$, so $v_1$ should go up | 71 | — |
| Gradient | $\hat y(v_1) = 1.5 v_1 - 0.5$, $L(v_1) = 2.25 v_1^2 - 7.5 v_1 + 6.25$, $dL/dv_1 = 4.5 v_1 - 7.5 = -3$ at $v_1 = 1$ | 72 | — |
| Step, $\eta = 0.2$ | $v_1 \leftarrow 1 - 0.2(-3) = 1.6$; $\hat y = 1.9$; $L = 0.01$ | 73 | — |

Block 3 pages are in [[Block 3 Slides]]. Review pages are in [[F26-midterm-review-234p]].

The review's notes on these steps: "Each highlighted edge contributes one product to the receiving hidden unit" (p. 46). "The output value is a weighted sum of the two hidden activations", and "The output layer is linear in this example" (p. 47). "The loss measures the output error before any parameter is updated" (p. 48).

"One weight changed, and the loss fell from 1.00 to 0.01" ([[Block 3 Slides]], p. 73).

Page 74 of [[Block 3 Slides]] is an exercise: reset $v_1 = 1$, write $L$ as a function of $v_2$, differentiate at $v_2 = -0.5$, take one step with $\eta = 0.2$, and check if the new loss is below 1. The deck gives no answer.

> [!note] Synthesis: exercise answer
> Not from the slides. $\hat y(v_2) = 1.5 + v_2$, so $L = (v_2 - 0.5)^2$ and $dL/dv_2 = -2$ at $v_2 = -0.5$. Then $v_2 \leftarrow -0.1$, $\hat y = 1.4$, and $L = 0.36$, which is below 1.

[[Block 3 Slides]] trains the same network again with backpropagation on all nine parameters (pp. 208-214). See [[Backpropagation]]. The midterm review does the same ([[F26-midterm-review-234p]], pp. 89-95). All nine gradients come from the original forward pass (p. 93). Each parameter moves by new = old − η · gradient, with $\eta = 0.05$ (p. 94). Then the forward pass runs again with the new parameters: "Every activation is freshly recomputed and compared with its old value" (p. 95).

| Value | Initial parameters (p. 88) | After one step (p. 95) |
| --- | --- | --- |
| $h_1$ | 1.5 | $\text{ReLU}(1.10 + 1.40 - 0.40) = 2.10$ |
| $h_2$ | 1 | $\text{ReLU}(-1.05 + 1.80 - 0.05) = 0.70$ |
| $\hat y$ | 1 | $1.15 \times 2.10 - 0.40 \times 0.70 + 0.10 = 2.235$ |
| $L$ | 1 | $(2.235 - 2)^2 = 0.055225$ |

The pages in this table are in [[F26-midterm-review-234p]].

## Related

- [[Neural Networks]]
- [[Backpropagation]]
- [[Gradient Descent]]
- [[Activation Functions]]: $\max(0, \cdot)$ is ReLU
- Computational Graphs
- [[Fundamentals of Deep Learning Nonlinear Activation]]: stacked affine layers collapse without a nonlinearity

## Sources

- [[Block 3 Slides]], pp. 35-55, 67-74, 207
- Lecture 3, § Forward Propagation
- [[F26-midterm-review-234p]], pp. 37, 41, 45-48, 87-95
