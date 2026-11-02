---
description: The recursive application of the chain rule along a computational graph, which gives the gradient of the loss for every parameter in one backward pass.
aliases: [Backprop, Backward Pass]
sources: ["[[Block 3 Slides]]", "[[Block 4 Slides]]", "[[Block 6 Slides]]", "[[Block 7 Slides]]", "[[F26-midterm-review-234p]]"]
subject: 2 Neural networks
---

## Definition

Backpropagation applies the chain rule recursively along a computational graph to get the gradient of a scalar loss with respect to every input, parameter, and intermediate. **Only computes the gradient.** Parameter updates come from the optimization step.

The forward pass computes each operation and saves the intermediates; the backward pass multiplies local derivatives from the loss back to the inputs. One backward pass costs the same asymptotic order as the forward pass, which makes [[Gradient Descent]] practical for large networks.

### The Chain Rule at One Node

$$\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}$$

| Name | Symbol | Comes from |
| --- | --- | --- |
| Local gradient | $\partial z / \partial x$ | the node's own derivative |
| Upstream gradient | $\partial L / \partial z$ | the node that consumes $z$ |
| Downstream gradient | $\partial L / \partial x$ | sent to the node that produced $x$ |

**Downstream loss (upstream * local)**

$$\frac{\partial L}{\partial x} = \frac{\partial L}{\partial z} \cdot \frac{\partial z}{\partial x}$$

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

> [!tip]
> Every local gradient uses the values of the original forward pass. Do not plug in updated weights or recomputed activations part way through the backward pass.

### One Neuron: Gradient and Update

For a hidden unit $z = wx + b$, $h = \mathrm{ReLU}(z)$, output $\hat y = v h$, and loss $L$:

**Gradient of one weight along one path.**

$$\frac{\partial L}{\partial w} = \frac{\partial L}{\partial \hat y} \cdot v \cdot \mathrm{ReLU}'(z) \cdot x$$

Error term, times output weight, times activation derivative, times input. Define $\delta \equiv \partial L / \partial z$, the sensitivity of the loss to the unit's pre-activation. Then $\partial L / \partial w = \delta \, x$ and $\partial L / \partial b = \delta$.

**Weight update.**

$$w \leftarrow w - \eta \, \frac{\partial L}{\partial w}$$

ex: $2(\hat y - t)$ for $L = (\hat y - t)^2$, and $\hat y - t$ for $L = \tfrac{1}{2}(\hat y - t)^2$.

> [!tip]
> A negative output weight $v$ flips the sign of the gradient reaching that hidden unit. A pre-activation $z \le 0$ makes $\mathrm{ReLU}' = 0$, so that unit's weights get no gradient this step.


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
