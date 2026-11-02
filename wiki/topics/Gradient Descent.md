---
description: The numerical optimization method that lowers the loss by repeated steps W ← W − η·dW against the gradient; CSCI 566 works it by finite differences and hand-derived gradients, and trains with its minibatch form, SGD.
aliases:
  - Numerical solution
  - Stochastic gradient descent
  - SGD
  - Update rule
  - Learning rate
  - Vanilla gradient descent
  - Minibatch gradient descent
  - Step size
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

**Derivative in one dimension.**

$$\frac{df(x)}{dx} = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}$$

**Numerical gradient.** Change one weight by $h = 0.001$, recompute the loss, and divide the change by $h$: for $W[0][0]$, $(1.6693 - 1.6688)/0.001 = 0.5$. Each weight needs one extra loss evaluation, so this is too slow for large models; [[Backpropagation]] gives the same gradient in one backward pass.

**Update rule.**

$$W \leftarrow W - \eta \cdot dW$$

- $dW$ gives the direction; $\eta$ gives the distance.
- Recompute $dW$ after every step. Stop when $dW$ is small or at the iteration limit.
- All parameters update together from the gradients of the same original forward pass. With nine parameters and $\eta = 0.05$ the loss falls from 1 to 0.055225; see [[Backpropagation]].

**Worked step.** Weight $2.0$, gradient $-0.5$, $\eta = 0.1$: new weight $= 2.0 - 0.1 \times (-0.5) = 2.05$.

**Analytic gradient.** With $h_1 = 1.5$, $h_2 = 1$, $v_2 = -0.5$, $c = 0$ fixed, $\hat y = 1.5 v_1 - 0.5$ and $L(v_1) = 2.25 v_1^2 - 7.5 v_1 + 6.25$, so $dL/dv_1 = 4.5 v_1 - 7.5 = -3$ at $v_1 = 1$. One step with $\eta = 0.2$ gives $v_1 = 1.6$ and drops the loss from 1.00 to 0.01. See [[Forward Propagation]].

> [!warning] Exam trap
> With $\eta > 0$ and $dL/dw < 0$, the update raises $w$: $-\eta \cdot dL/dw$ is positive. A negative slope means the loss falls as $w$ rises, a nonzero slope is never a minimum, and the minus sign in the rule already points downhill. Overshooting the target can still lower the loss, but a finite step must be checked.

### Learning Rate

The gradient is local and gives only the direction; the learning rate controls how far the step goes.

| Rate | Loss over epochs |
| --- | --- |
| Very high | Blows up |
| High | Falls fast, then stays high |
| Low | Falls slowly |
| Good | Reaches the lowest loss |

- Too large: overshoot or diverge; the training loss goes up and down, then rises.
- Too small: the same training budget yields little progress.
- In the vanilla loop, `step_size` is the learning rate.
- Learning Rate Schedules changes the rate during training; the plain rule holds it fixed.

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

```python
while True:
  data_batch = sample_training_data(data, 256)
  weights_grad = evaluate_gradient(loss_fun, data_batch, weights)
  weights += - step_size * weights_grad
```

Vanilla gradient descent runs the same loop on all the data.

- Noisy minibatch gradients, zigzags under poor conditioning, and stalls where the gradient is zero are the problems of plain SGD; see [[Optimization]].
- Known issues: local minima, [[Exploding Gradient Problem|exploding gradients]], and inexact gradients.
- Variants for stability, accuracy, or speed: SGD + Momentum, AdaGrad, RMSProp, Adam, and AdamW; see [[Gradient-Based Optimizers]].

> [!tip]
> Optimizers consume gradients; they do not produce them. [[Backpropagation]] produces them.

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
