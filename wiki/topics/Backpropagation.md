---
description: The recursive application of the chain rule along a computational graph, which gives the gradient of the loss for every parameter in one backward pass.
aliases: [Backprop, Backward Pass]
sources: ["[[Block 3 Slides]]", "[[Block 4 Slides]]", "[[Block 6 Slides]]", "[[Block 7 Slides]]", "[[F26-midterm-review-234p]]"]
subject: 2 Neural networks
---

## Definition

Backpropagation applies the chain rule recursively along a computational graph to get the gradient of a scalar loss with respect to every input, parameter, and intermediate. The forward pass computes each operation and saves the intermediates; the backward pass multiplies local derivatives from the loss back to the inputs. One backward pass costs the same asymptotic order as the forward pass, which makes [[Gradient Descent]] practical for large networks.

### The Chain Rule at One Node

**Chain rule.**

$$\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}$$

Differentiate the outer function with the inside unchanged, then multiply by the inner derivative.

For one node with inputs $x, y$, output $z$, and loss $L$ after it:

| Name | Symbol | Comes from |
| --- | --- | --- |
| Local gradient | $\partial z / \partial x$ | the node's own derivative |
| Upstream gradient | $\partial L / \partial z$ | the node that consumes $z$ |
| Downstream gradient | $\partial L / \partial x$ | sent to the node that produced $x$ |

**Downstream equals upstream times local.**

$$\frac{\partial L}{\partial x} = \frac{\partial L}{\partial z} \cdot \frac{\partial z}{\partial x}$$

Each node needs only its own local gradient. The graph is not unique; pick one whose local gradients are easy to write, such as one sigmoid gate in place of $\times(-1)$, $\exp$, $+1$, and $1/x$.

**Sum over paths.** When a value feeds several branches, its gradient is the sum of the branch contributions:

$$\frac{\partial L}{\partial x} = \sum_{k} \frac{\partial L}{\partial z_k} \cdot \frac{\partial z_k}{\partial x}$$

### Gate Table

With upstream gradient $g = \partial L / \partial z$:

| Gate | Forward | Gradient to inputs | Nickname |
| --- | --- | --- | --- |
| add | $z = x + y$ | $g$ to each input | distributor |
| multiply | $z = xy$ | $g \cdot y$ to $x$, $g \cdot x$ to $y$ | swap multiplier |
| max | $z = \max(x, y)$ | $g$ to the larger input, $0$ to the other | router |
| sigmoid | $z = \sigma(x)$ | $g \cdot \sigma(x)(1 - \sigma(x))$ | |
| ReLU | $z = \max(0, x)$ | $g$ if $x > 0$, else $0$ | |

> [!warning] Exam trap
> Every local gradient uses the values of the original forward pass. Do not plug in updated weights or recomputed activations part way through the backward pass.

### One Neuron: Gradient and Update

For a hidden unit $z = wx + b$, $h = \mathrm{ReLU}(z)$, output $\hat y = v h$, and loss $L$:

**Gradient of one weight along one path.**

$$\frac{\partial L}{\partial w} = \frac{\partial L}{\partial \hat y} \cdot v \cdot \mathrm{ReLU}'(z) \cdot x$$

Error term, times output weight, times activation derivative, times input. Define $\delta \equiv \partial L / \partial z$, the sensitivity of the loss to the unit's pre-activation. Then $\partial L / \partial w = \delta \, x$ and $\partial L / \partial b = \delta$.

**Weight update.**

$$w \leftarrow w - \eta \, \frac{\partial L}{\partial w}$$

The update belongs to the optimizer, a separate step after the gradients exist; see [[Gradient-Based Optimizers]]. The loss scale sets the first factor: $2(\hat y - t)$ for $L = (\hat y - t)^2$, and $\hat y - t$ for $L = \tfrac{1}{2}(\hat y - t)^2$.

> [!tip]
> A negative output weight $v$ flips the sign of the gradient reaching that hidden unit. A pre-activation $z \le 0$ makes $\mathrm{ReLU}' = 0$, so that unit's weights get no gradient this step.

### Matrix Form for a Linear Layer

For a layer $z = Wx + b$ with $\delta = \partial L / \partial z$ a column vector:

**Linear layer gradients.**

$$\frac{\partial L}{\partial W} = \delta \, x^{T}, \qquad \frac{\partial L}{\partial b} = \delta, \qquad \frac{\partial L}{\partial x} = W^{T} \delta$$

Each entry is $\partial L / \partial w_{ij} = \delta_i \, x_j$, so column $j$ of $\nabla W$ is column 1 scaled by $x_j / x_1$.

For vector inputs and outputs the local gradient is a Jacobian ($\mathbb{R}^{N \times M}$ for $x \in \mathbb{R}^N$, $y \in \mathbb{R}^M$), but backprop never materializes it. Each operation applies a vector-Jacobian product to the upstream gradient, so gradients move as vectors, not matrices.

### Worked Example: Tiny Network, One Step

Setup: $x = (1, 2)$, $W = \begin{pmatrix} 1 & 0.5 \\ -1 & 1 \end{pmatrix}$, $b = (-0.5, 0)$, $v = (1, -0.5)$, $c = 0$, $t = 2$, $L = (\hat y - t)^2$, $\eta = 0.05$ (the [[Forward Propagation]] network).

1. Forward: $z = (1.5, 1)$, $h = (1.5, 1)$, $\hat y = 1$, $L = 1$.
2. $\partial L / \partial \hat y = 2(1 - 2) = -2$. The slope is negative, so raising $\hat y$ lowers the loss.
3. Output layer: $\partial L / \partial v = -2 \, h = (-3, -2)$, $\partial L / \partial c = -2$.
4. Into $h$: $-2 \, v = (-2, +1)$; both $z_i > 0$, so $\delta = (-2, +1)$.
5. First layer: $\nabla W = \delta x^T = \begin{pmatrix} -2 & -4 \\ 1 & 2 \end{pmatrix}$, $\nabla b = (-2, 1)$.
6. Update: $W = \begin{pmatrix} 1.10 & 0.70 \\ -1.05 & 0.90 \end{pmatrix}$, $b = (-0.40, -0.05)$, $v = (1.15, -0.40)$, $c = 0.10$.
7. Rerun: $\hat y = 2.235$, $L \approx 0.055$. Overshooting the target still reduced the loss.

### Training Loop and Memory

One training step: predict, backpropagate the loss, update the parameters.

- A mini-batch of $B$ examples gives a cheap but noisy gradient estimate; common sizes are 32, 64, and 128.
- One epoch is $N / B$ updates. An epoch counts data passes; an update changes parameters.
- Judge the loss trend over many updates, not one step.
- Stored activations make memory grow with depth and batch size. Checkpointing recomputes most of them during the backward pass: less memory, more compute, same gradient.

> [!warning] Exam trap
> Backprop computes gradients only. It does not change any parameter; the optimizer does that in a separate step.

## Related

- Computational Graphs
- [[Forward Propagation]]
- [[Neural Networks]]
- [[Gradient Descent]]
- [[Gradient-Based Optimizers]]
- [[Loss Functions]]
- [[Activation Functions]]
- [[Vanishing Gradient Problem]]
- [[Exploding Gradient Problem]]
- Backpropagation Through Time
- Updating LLMs
- Flower Classifier Running Example

## Sources

- [[Block 3 Slides]]
- [[Block 4 Slides]]
- [[Block 6 Slides]]
- [[Block 7 Slides]]
- [[F26-midterm-review-234p]]
