---
id: con-0tp56w
type: topic
kind: concept
description: The recursive application of the chain rule along a computational graph, which gives the gradient of the loss for every parameter in one backward pass.
tags: [machine-learning/cs566-deeplearning]
aliases: [Backprop, Backward Pass]
created: 2026-09-28T00:00:00
updated: 2026-10-19T17:48:15
refreshed: 2026-10-19T17:48:15
status: stable
sources: ["[[Block 3 Slides]]", "[[Block 4 Slides]]", "[[Block 6 Slides]]", "[[Block 7 Slides]]", "[[F26-midterm-review-234p]]"]
up: ["[[Neural Networks]]"]
---

> [!concept] Concept
> 5 sources · refreshed 2026-10-19 · #machine-learning/cs566-deeplearning
> Up: [[Neural Networks]]

## Definition

"backpropagation = recursive application of the chain rule along a computational graph to compute the gradients of all inputs/ parameters/ intermediates" ([[Block 3 Slides]], p. 207). It has two passes (p. 207):

- **Forward:** "compute the result of an operation and save any intermediates needed for gradient computation in memory".
- **Backward:** "apply the chain rule to compute the gradient of the loss function with respect to the inputs".

[[Block 4 Slides]] recaps it as a network diagram with an arrow from the output $Y$ back to the input $X$, labeled with the chain rule $\dfrac{\partial Y}{\partial X} = \dfrac{\partial Y}{\partial h_1} \cdot \dfrac{\partial h_1}{\partial X}$ (p. 9). [[Block 6 Slides]] restates it for graph neural networks: after forward propagation computes $L$, back-propagation obtains the gradient $\nabla_\Theta L$ by the chain rule (p. 61).

The midterm review puts backpropagation in the training loop: "Training turns a score into a loss, a loss into gradients, and gradients into parameter updates." It gives three rules ([[F26-midterm-review-234p]], p. 78):

- "Backpropagation applies the chain rule, multiplying local derivatives along each path."
- "When a value feeds several branches, its gradient is the sum of the branch contributions."
- "The optimizer is a separate step that uses the computed gradients to update parameters." See [[Gradient-Based Optimizers]].

The slides start from the goal: "If we can compute $\partial L/\partial W_1, \partial L/\partial W_2$ then we can learn $W_1$ and $W_2$" ([[Block 3 Slides]], p. 103). Deriving $\nabla_W L$ on paper is "very tedious". A new loss, such as L2 in place of L1, means a new derivation from scratch, and the method is "not feasible for complex models" (p. 104). The "better idea" is a computational graph plus backpropagation (p. 105).

## Explanation

For a scalar loss, one backward pass gives the gradient for every parameter, at the same asymptotic order as the forward pass (p. 180). A numerical gradient needs one extra loss computation for each weight ([[Gradient Descent]]). Synthesis: this is why backpropagation makes [[Gradient Descent]] practical for large networks.

### The chain rule

The chain rule is $\dfrac{dy}{dx} = \dfrac{dy}{du} \cdot \dfrac{du}{dx}$. In words: "Differentiate outer function, Keep the inside the same", then multiply by "Differentiate inner function" ([[F26-midterm-review-234p]], p. 82, from Block 3 slide 125). Backpropagation applies this rule at every node. In $f = (x + y)z$ with $q = x + y$, the review labels the two factors of $\dfrac{\partial f}{\partial y} = \dfrac{\partial f}{\partial q} \dfrac{\partial q}{\partial y}$ as the upstream gradient and the local gradient (pp. 83-84).

### Local, upstream, and downstream gradients

For one node with inputs $x, y$, output $z$, and a scalar loss $L$ after it (pp. 128-133):

- **Local gradient:** $\partial z / \partial x$, the node's own derivative.
- **Upstream gradient:** $\partial L / \partial z$, from the node that uses $z$.
- **Downstream gradient:** $\partial L / \partial x = \dfrac{\partial L}{\partial z} \dfrac{\partial z}{\partial x}$, sent to the node that made $x$.

Each node needs only its own local gradient. The first example is $f = (x + y)z$ with $x = -2$, $y = 5$, $z = -4$ (pp. 108-133, credited to Stanford CS231n); it is worked on Computational Graphs. The midterm review repeats it and gets $\partial f/\partial q = -4$, $\partial f/\partial z = 3$, $\partial f/\partial y = -4$, and $\partial f/\partial x = -4$ ([[F26-midterm-review-234p]], pp. 83-86). A vectorized example from [[Block 4 Slides]], p. 10, is also on that page.

### Patterns in gradient flow

| Gate | Rule | Slide example |
| --- | --- | --- |
| add | gradient distributor: each input gets the upstream gradient unchanged | upstream 2; both inputs get 2 |
| mul | "swap multiplier": each input gets the upstream gradient times the other input | inputs 2 and 3, upstream 5; gradients 15 and 10 |
| copy | gradient adder: a value used twice gets the sum of both gradients | branch gradients 4 and 2; the source gets 6 |
| max | gradient router: the full gradient goes to the larger input; the other gets 0 | inputs 4 and 5, upstream 9; 9 to the 5, 0 to the 4 |

Source: [[Block 3 Slides]], pp. 154-157, credited to CS231n. The midterm review states the copy rule for any number of branches: "When a value feeds several branches, its gradient is the sum of the branch contributions" ([[F26-midterm-review-234p]], p. 78).

### Worked example: a sigmoid neuron

$$f(w, x) = \frac{1}{1 + e^{-(w_0 x_0 + w_1 x_1 + w_2)}}, \qquad w_0 = 2,\ x_0 = -1,\ w_1 = -3,\ x_1 = -2,\ w_2 = -3$$

Forward: $w_0 x_0 = -2$, $w_1 x_1 = 6$, sum $4$, plus $w_2$ gives $1$, and $\sigma(1) \approx 0.73$ (pp. 134-153).

Backward, with the sigmoid local gradient $\dfrac{d\sigma}{dx} = \dfrac{e^{-x}}{(1 + e^{-x})^2} = (1 - \sigma(x))\sigma(x)$ (p. 151). At the sigmoid: $1.00 \times (1 - 0.73)(0.73) \approx 0.2$ (p. 153).

| Gradient | $dw_0$ | $dx_0$ | $dw_1$ | $dx_1$ | $dw_2$ |
| --- | --- | --- | --- | --- | --- |
| Value | $-0.20$ | $0.40$ | $-0.40$ | $-0.60$ | $0.20$ |

Source: pp. 137-153, 167. "Computational graph representation may not be unique. Choose one where local gradients at each node can be easily expressed!" (p. 150). The slides group the last four nodes ($\times -1$, exp, $+1$, $1/x$) into one sigmoid gate.

The same example as flat code (pp. 161-167):

```python
s0 = w0 * x0
s1 = w1 * x1
s2 = s0 + s1
s3 = s2 + w2
L = sigmoid(s3)

grad_L = 1.0
grad_s3 = grad_L * (1 - L) * L
grad_w2 = grad_s3
grad_s2 = grad_s3
grad_s0 = grad_s2
grad_s1 = grad_s2
grad_w1 = grad_s1 * x1
grad_x1 = grad_s1 * w1
grad_w0 = grad_s0 * x0
grad_x0 = grad_s0 * w0
```

Synthesis: each backward line is one local gradient times one upstream gradient, in the reverse order of the forward lines.

### Vector derivatives and the Jacobian

| Input | Output | Derivative | Shape |
| --- | --- | --- | --- |
| $x \in \mathbb{R}$ | $y \in \mathbb{R}$ | regular derivative | scalar |
| $x \in \mathbb{R}^N$ | $y \in \mathbb{R}$ | gradient | $\mathbb{R}^N$ |
| $x \in \mathbb{R}^N$ | $y \in \mathbb{R}^M$ | Jacobian | $\mathbb{R}^{N \times M}$ |

Source: pp. 168-170. Two examples come from *Mathematics for Machine Learning* (Deisenroth, Faisal, and Ong). For $f(x) = Ax$, the gradient is $A$ (p. 171). For $h(t) = f(g(t))$, the chain rule multiplies a $1 \times 2$ Jacobian by a $2 \times 1$ Jacobian (p. 172).

### Backprop with vectors

When $x$, $y$, and $z$ are vectors, the loss $L$ is "still a scalar" (pp. 173-176). The local gradients are Jacobian matrices of shape $[D_x \times D_z]$ and $[D_y \times D_z]$. The downstream gradient is a matrix-vector product of the local Jacobian and the upstream gradient (pp. 177-179):

$$\frac{\partial L}{\partial x} = \frac{\partial z}{\partial x} \frac{\partial L}{\partial z}$$

### Backprop skips the full Jacobian

From p. 180:

- For $z = f(x)$, backprop maps the upstream gradient to the downstream gradient with a vector-Jacobian product (VJP).
- No full Jacobian is materialized. Each operation applies a local VJP.
- For a scalar $L$, one reverse sweep gives all parameter gradients. Baydin et al. (JMLR 2018) show this has the same asymptotic order as evaluation.
- Same order is not equal time: the backward pass reads saved activations and adds up gradients.

"Backprop scales by moving gradient vectors, not full Jacobian matrices" (p. 180).

### Backward pass through a full network

The slides show the forward pass through a network with three hidden layers (p. 181). The backward pass starts at a loss computed from the estimate $Y$ and the ground truth $Y^*$, "e.g., $L(W) = \lVert f(X; W) - Y^* \rVert_2$" (p. 184). It then computes each hidden unit's gradient from right to left (pp. 185-206). These diagrams have no numbers. They show the order of the calculation.

### Worked example: the tiny network

This is the network from [[Forward Propagation]] (pp. 67-74), trained one full step (pp. 208-214).

Setup (p. 208): $x = (1, 2)$, $W = \begin{pmatrix} 1 & 0.5 \\ -1 & 1 \end{pmatrix}$, $b = (-0.5, 0)$, $v = (1, -0.5)$, $c = 0$, target 2. Forward: $z = (1.5, 1)$, $h = (1.5, 1)$, $\hat y = 1$.

| Step | Result | Page |
| --- | --- | --- |
| Prediction error | $L = (1 - 2)^2 = 1$; $\partial L / \partial \hat y = -2$ | 209 |
| Output edges | $\partial L / \partial v = (-3, -2)$, $\partial L / \partial c = -2$; into $h$: $-2 \times 1 = -2$ and $-2 \times (-0.5) = +1$ | 210 |
| Active ReLUs | $z_1, z_2 > 0$, so ReLU$' = 1$ and $\delta = (-2, +1)$ | 211 |
| First-layer weights | $\nabla W = \delta x^T = \begin{pmatrix} -2 & -4 \\ 1 & 2 \end{pmatrix}$, $\nabla b = (-2, 1)$ | 212 |
| Update all nine parameters, $\eta = 0.05$ | $W = \begin{pmatrix} 1.10 & 0.70 \\ -1.05 & 0.90 \end{pmatrix}$, $b = (-0.40, -0.05)$, $v = (1.15, -0.40)$, $c = 0.10$ | 213 |
| Run again | $h = (2.1, 0.7)$, $\hat y = 2.235$, $L = 0.055225$ | 214 |

"The negative output weight flips one hidden gradient" (p. 210). "Overshooting the target can still reduce the loss" (p. 214).

[[F26-midterm-review-234p]] repeats this example with one slide for each step (pp. 89-95). Its numbers agree with the table. It adds these statements:

- "Negative slope: raising ŷ a little lowers the loss" (p. 89).
- "Each gradient is ∂L/∂ŷ times what the parameter multiplies" (p. 90).
- It defines $\delta_i \equiv \partial L / \partial z_i$, "the loss sensitivity to hidden unit i's sum" (p. 91). The first-layer rules are $\partial L / \partial w_{ij} = \delta_i \times x_j$ and $\partial L / \partial b_i = \delta_i$ (p. 92).
- "Column 2 = 2 × column 1 because x₂ = 2x₁" (p. 92).
- "Every gradient below comes from the original forward pass (ŷ = 1, t = 2, L = 1)" (p. 93). "All gradients use the original forward pass" (p. 94).

> [!note] Synthesis: the slides' questions
> [[Block 3 Slides]] asks three questions without answers. Answers derived from the numbers above:
> - Should gradient descent raise or lower the output (p. 209)? Raise it: $\partial L / \partial \hat y < 0$. The midterm review gives the same answer: "raising ŷ a little lowers the loss" ([[F26-midterm-review-234p]], p. 89).
> - What changes if a pre-activation is negative (p. 211)? ReLU$' = 0$, so that unit's gradient is 0.
> - Why is the second column of $\nabla W$ twice the first (p. 212)? Because $x_2 = 2 x_1$ and $\nabla W = \delta x^T$. The midterm review gives the same reason ([[F26-midterm-review-234p]], p. 92).

### Worked example: one path through one hidden unit

"A single path from weight to loss gives a gradient of 12 as a product of four factors" ([[F26-midterm-review-234p]], p. 96):

- Forward: $x = 3$, $w = 1$, $b = -1$, so $z = 2$. ReLU gives $h = 2$. The output weight $v = 2$ gives $\hat y = 4$.
- Loss: $t = 2$, $L = \tfrac{1}{2}(\hat y - t)^2 = 2$, and $e = \hat y - t = 2$.
- Gradient: $\partial L / \partial w = (4 - 2) \times 2 \times 1 \times 3 = 12$, that is, error × output weight × ReLU$'$ × input.

The slide shows how the loss scale changes the first factor: for $L = e^2$, $\partial L / \partial \hat y = 2e$; for $L = \tfrac{1}{2}e^2$, $\partial L / \partial \hat y = e$. "All derivatives use the original values, computed before any update" (p. 96).

Synthesis: the tiny network above uses $L = (\hat y - t)^2$, so its first factor is $2e = -2$. This path uses $\tfrac{1}{2}e^2$, so its first factor is $e$.

### One training step, mini-batches, and epochs

[[Block 7 Slides]] places backpropagation inside one training step (p. 14):

1. Predict, and compare the prediction with the label. "The label tells us how to score the current prediction."
2. Backpropagate the loss.
3. Update the trainable parameters.

"Forward computes the loss. Backward computes gradients." ([[Block 7 Slides]], p. 14). The update in step 3 is the optimizer's job; see [[Gradient Descent]] and [[Gradient-Based Optimizers]].

The deck then counts steps on a flower training split (p. 15; see Flower Classifier Running Example):

- The training split has 320 flower photos. A mini-batch contains 32 photos, and one update uses that group.
- 10 mini-batches cover 320 photos: one epoch.
- Shuffle the training photos, then begin another epoch.

"An epoch counts data passes. An update changes parameters." ([[Block 7 Slides]], p. 15).

The full loss $L(W) = \frac{1}{N}\sum_{i=1}^{N} L_i(x_i, y_i, W) + \lambda R(W)$ and its gradient sum over all $N$ examples. That full sum is expensive when $N$ is large, so a minibatch of examples approximates it. Sizes of 32, 64, and 128 are common ([[Block 7 Slides]], p. 88). The "Vanilla Minibatch Gradient Descent" code on the same slide samples 256 examples per batch, a size outside that list (p. 88).

Mini-batches give different gradient estimates. One batch may contain mostly easy photos, and another mostly difficult photos. A single mini-batch is "a cheap but noisy estimate of the training objective". Across many mini-batches, "repeated updates can make progress without every step lowering loss." "Judge the trend over many updates." ([[Block 7 Slides]], p. 98).

Synthesis: with $N$ training examples and a batch size $B$ that divides $N$, one epoch is $N / B$ updates, here $320 / 32 = 10$. Each update runs one forward pass and one backward pass on its batch. The slides do not say what happens to a last partial batch when $B$ does not divide $N$.

### Memory cost

From p. 215:

- The forward pass stores activations that the backward pass will later need.
- That memory is held until the gradient arrives, so it grows with depth and batch size.
- Checkpointing keeps a few boundary activations and recomputes the rest during the backward pass: "Less memory, more compute. Exact recomputation leaves the gradient unchanged."
- Korthikanti et al. (MLSys 2023) measure this at scale; Adacc (arXiv:2508.00806) tunes it per tensor.

Synthesis: [[LoRA]] and Test-Time Training still run backprop, so they pay this memory cost. Context-only updates and Agent Memory do not (Updating LLMs). In a recurrent network the stored activations also grow with sequence length; Backpropagation Through Time covers that case and its truncated form.

## Related

- Computational Graphs
- [[Forward Propagation]]
- [[Neural Networks]]
- [[Gradient Descent]]
- [[Gradient-Based Optimizers]]: the update step that consumes the gradients
- [[Loss Functions]]
- [[Activation Functions]]
- [[Vanishing Gradient Problem]]: a product of many small local gradients
- [[Exploding Gradient Problem]]
- Backpropagation Through Time: backpropagation through an RNN unrolled over time
- Updating LLMs
- Flower Classifier Running Example: the 320-photo split behind the epoch count

## Sources

- [[Block 3 Slides]], pp. 102-215. The scalar examples, gate patterns, and vector slides are credited in the slides to Stanford CS231n.
- [[Block 4 Slides]], p. 9, the chain-rule recap
- [[Block 6 Slides]], p. 61, the GNN restatement
- [[Block 7 Slides]], pp. 14-15, 88, 98, the training step, mini-batches, and epochs
- [[F26-midterm-review-234p]], pp. 78, 82-96, the midterm review's recap: training-loop rules, the chain rule, the $(x + y)z$ example, the tiny network, and the single-path example
