---
description: The numerical optimization method that lowers the loss by repeated steps W ← W − η·dW against the gradient; CSCI 566 works it by finite differences and hand-derived gradients, and trains with its minibatch form, SGD.
aliases: [Stochastic gradient descent, SGD, Vanilla gradient descent, Minibatch gradient descent, Update rule, Learning rate]
sources:
  - "[[Block 1 Slides]]"
  - "[[Block 3 Slides]]"
  - "CSCI 566 Syllabus"
  - "[[Block 7 Slides]]"
  - "[[F26-midterm-review-234p]]"
subject: 3 Training
---

## Definition

Gradient descent finds a low-loss $W$ by repeated small steps against the gradient. The gradient is the vector of partial derivatives of the loss; the learning rate $\eta$ sets how far each step moves. CSCI 566 computes the gradient by finite differences first, then by [[Backpropagation]], and trains with the minibatch form, SGD.

### Gradient and Update Rule

**Update rule.**

$$W \leftarrow W - \eta \cdot dW$$

- $dW$ gives the direction; $\eta$ gives the distance.
- Recompute $dW$ after every step. Stop when $dW$ is small or at the iteration limit.
- With $\eta > 0$ and $dL/dw < 0$, the update raises $w$: $-\eta \cdot dL/dw$ is positive. 
- A negative slope means the loss falls as $w$ rises, a nonzero slope is never a minimum, and the minus sign in the rule already points downhill. 

### Learning Rate

The gradient is local and gives only the direction; the learning rate controls how far the step goes.

| Rate | Loss over epochs |
| --- | --- |
| Very high | Blows up |
| High | Falls fast, then stays high |
| Low | Falls slowly |
| Good | Reaches the lowest loss |

### Full-Batch and Minibatch (SGD)

**Loss and gradient over $N$ examples.**

$$L(W) = \frac{1}{N} \sum_{i=1}^{N} L_i(x_i, y_i, W) + \lambda R(W)$$

$$\nabla_W L(W) = \frac{1}{N} \sum_{i=1}^{N} \nabla_W L_i(x_i, y_i, W) + \lambda \nabla_W R(W)$$

$R(W)$ is the [[Regularization|regularization]] term. The full sum is expensive when $N$ is large, so SGD approximates it with a minibatch.

**SGD update, optimizer notation.**

$$x_{t+1} = x_t - \alpha \nabla f(x_t)$$

| | Vanilla gradient descent | Minibatch SGD |
| --- | --- | --- |
| Data per step | All $N$ examples | Sampled minibatch |
| Batch size | $N$ | 32, 64, 128 common; 256 in the loop |
| Gradient | Exact | Noisy estimate |
| Cost per step | High | Low |

**Vanilla gradient descent runs the same loop on all the data.**
- Known issues: local minima, [[Exploding Gradient Problem|exploding gradients]], and inexact gradients.
- Variants for stability, accuracy, or speed: SGD + Momentum, AdaGrad, RMSProp, Adam, and AdamW; see [[Gradient-Based Optimizers]].


## Related

- [[Gradient-Based Optimizers]]: SGD + Momentum, AdaGrad, RMSProp, Adam, and AdamW
- Learning Rate Schedules: change the learning rate over training
- [[Optimization]]
- [[Loss Functions]]
- [[Perceptron]]
- [[Backpropagation]]: computes $dW$ for every weight in one backward pass
- Computational Graphs
- [[Forward Propagation]]
- [[Exploding Gradient Problem]]: a gradient that is too large gives a step that is too large
- [[Gradient Clipping]]
- [[Vanishing Gradient Problem]]: a gradient near 0 in early layers gives almost no step
- Shortcut Learning: gradient descent picks the most predictive feature, even a surface cue

## Sources

- [[Block 1 Slides]]
- [[Block 3 Slides]]
- CSCI 566 Syllabus
- [[Block 7 Slides]]
- [[F26-midterm-review-234p]]
