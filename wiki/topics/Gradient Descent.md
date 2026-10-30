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
---

> [!concept] Concept
> 5 sources · refreshed 2026-10-19 · #machine-learning/cs566-deeplearning
> Up: [[Optimization]]

## Definition

Gradient descent finds a low-loss $W$ by repeated small steps against the gradient ([[Block 1 Slides]], pp. 317–338).

In one dimension, the derivative is

$$\frac{df(x)}{dx} = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}$$

"The gradient is the vector of partial derivatives in a higher dimension" ([[Block 1 Slides]], pp. 318–320).

## Explanation

### Numerical gradient, worked

Change one weight by $h = 0.001$, compute the loss again, and divide the change by $h$ ([[Block 1 Slides]], pp. 321–335):

| Weight changed | $L(W)$ | $L(W + h)$ | Gradient entry |
| --- | --- | --- | --- |
| $W[0][0]$ | 1.6688 | 1.6693 | $(1.6693 - 1.6688)/0.001 = 0.5$ |
| $W[0][1]$ | 1.6688 | 1.6697 | $(1.6697 - 1.6688)/0.001 = 0.9$ |

[[Block 3 Slides]] repeats this example with the same numbers ([[Block 3 Slides]], pp. 14–15).

### Analytic gradient, worked

A tiny network has $h_1 = 1.5$, $h_2 = 1$, $v_2 = -0.5$, and $c = 0$ held fixed. Trying $v_1 = 1.2$ gives loss 0.49 and $v_1 = 0.8$ gives 1.69, so $v_1$ should go up ([[Block 3 Slides]], p. 71). Then $\hat y(v_1) = 1.5 v_1 - 0.5$ and $L(v_1) = 2.25 v_1^2 - 7.5 v_1 + 6.25$, so $dL/dv_1 = 4.5 v_1 - 7.5 = -3$ at $v_1 = 1$ ([[Block 3 Slides]], p. 72). One step with $\eta = 0.2$ gives $v_1 = 1.6$, and the loss falls from 1.00 to 0.01 ([[Block 3 Slides]], p. 73). See [[Forward Propagation]].

### Update rule

$$W \leftarrow W - \eta \cdot dW$$

- $dW$ is the gradient and $\eta$, the learning rate, controls the step size.
- "Large: overshoot or diverge. Small: slow progress."
- Compute $dW$ again after each step. Stop when $dW$ is small or at the iteration limit.
- "Today: the rule. Weeks 3-4: mechanism and backpropagation."

Source: [[Block 1 Slides]], p. 336. For all nine parameters of a network updated together with $\eta = 0.05$, see [[Backpropagation]]: the loss falls from 1 to 0.055225, and "Overshooting the target can still reduce the loss" ([[Block 3 Slides]], pp. 208–214).

The midterm review repeats this step as a table of old values, gradients, and new values. "Each parameter moves by new = old − η · gradient, with positive learning rate η = 0.05 and the nine gradients from the original forward pass." "All gradients use the original forward pass." ([[F26-midterm-review-234p]], p. 94). When the network runs again on the same example, the loss falls from 1 to 0.055225 (p. 95).

Variants "for stability, accuracy, or speed": stochastic gradient descent, Adam, and batch and mini-batch algorithms ([[Block 1 Slides]], p. 337). Issues: local minima, [[Exploding Gradient Problem|exploding gradients]], and inexact gradients ([[Block 1 Slides]], p. 338). Week 1 names these but does not define them. [[Block 7 Slides]] defines minibatch SGD (below) and Adam (see [[Gradient-Based Optimizers]]).

### Learning rate

"The gradient and the learning rate play different roles." The gradient gives the direction, and "The learning rate controls how far we move" ([[Block 7 Slides]], p. 85). A worked step (p. 85):

- Current weight 2.0, gradient −0.5, learning rate 0.1.
- New weight = 2.0 − 0.1 × (−0.5) = 2.05.
- "The gradient is local. The chosen step must still be checked."

The midterm review repeats this slide ([[F26-midterm-review-234p]], p. 105).

In the vanilla loop, `step_size` is the learning rate ([[Block 7 Slides]], p. 118). The rate can be wrong in two ways ([[Block 7 Slides]], pp. 89–90):

- **Too large:** an illustrative training-loss trace for the flower classifier goes up and down and then rises over 8 epochs. "Large jumps can make training unstable" (p. 89).
- **Too small:** "The same training budget can yield very little progress." "Slow progress motivates a controlled learning-rate check" (p. 90).

A loss-versus-epoch plot shows four rates ([[Block 7 Slides]], p. 119). With a very high rate, the loss blows up. With a high rate, it falls fast and then stays at a high level. With a low rate, it falls slowly. With a good rate, it reaches the lowest loss. The slide asks, "Which one of these learning rates is best to use?"

These slides agree with the Week 1 rule "Large: overshoot or diverge. Small: slow progress." ([[Block 1 Slides]], p. 336). Learning Rate Schedules covers how to change the rate during training.

### Reading the sign of a gradient

The midterm review asks a check question ([[F26-midterm-review-234p]], p. 106). Gradient descent uses a positive learning rate $\eta$ and the update $w \leftarrow w - \eta \cdot (dL/dw)$. For one weight, backpropagation reports $dL/dw < 0$. What does the update do to $w$?

The update increases $w$: "−η·(dL/dw) is positive, so w rises, though a finite step still needs checking" (p. 107). The slide also says why the other answers are wrong (p. 107):

- "a negative slope means the loss falls locally as w rises, not that it grows."
- "a minimum has zero slope; a nonzero slope means a small move can lower the loss."
- "η stays positive, and the minus sign in the update already points downhill."

Synthesis: the worked step in the Learning rate section is this case. The gradient −0.5 raises the weight from 2.0 to 2.05.

### Full-batch and minibatch (SGD)

Block 7 opens with the same loop under the title "Learning network parameters through optimization" ([[Block 7 Slides]], p. 10):

```python
# Vanilla Gradient Descent
while True:
  weights_grad = evaluate_gradient(loss_fun, data, weights)
  weights += - step_size * weights_grad # perform parameter update
```

Vanilla gradient descent uses "all data here to update the model weights" ([[Block 7 Slides]], p. 86). Each step moves the original $W$ in the negative gradient direction on the loss surface (p. 87).

The loss is an average over $N$ examples plus a [[Regularization|regularization]] term ([[Block 7 Slides]], p. 88):

$$L(W) = \frac{1}{N} \sum_{i=1}^{N} L_i(x_i, y_i, W) + \lambda R(W)$$

$$\nabla_W L(W) = \frac{1}{N} \sum_{i=1}^{N} \nabla_W L_i(x_i, y_i, W) + \lambda \nabla_W R(W)$$

"Full sum expensive when N is large!" Stochastic gradient descent (SGD) does this instead: "Approximate sum using a minibatch of examples", with "32 / 64 / 128 common" (p. 88):

```python
# Vanilla Minibatch Gradient Descent
while True:
  data_batch = sample_training_data(data, 256) # sample 256 examples
  weights_grad = evaluate_gradient(loss_fun, data_batch, weights)
  weights += - step_size * weights_grad # perform parameter update
```

In optimizer notation, SGD is $x_{t+1} = x_t - \alpha \nabla f(x_t)$ ([[Block 7 Slides]], p. 101). The midterm review repeats the SGD slide and this update ([[F26-midterm-review-234p]], pp. 108, 110). Minibatch gradients are noisy. Under poor conditioning, plain SGD zigzags, and where the gradient is zero, it gets stuck ([[Block 7 Slides]], pp. 92–97). [[Optimization]] explains these problems. [[Gradient-Based Optimizers]] covers the update rules built on SGD that address them.

### Optimizers

[[Block 3 Slides]] calls the move past plain SGD "Gradient Descent Grew Up" ([[Block 3 Slides]], p. 16). [[Gradient-Based Optimizers]] covers SGD + Momentum, AdaGrad, RMSProp, Adam, AdamW, Muon, and SOAP. "Optimizers consume gradients; they do not produce them" ([[Block 3 Slides]], p. 16). [[Backpropagation]] produces them.

### Why it matters

Synthesis: the numerical method needs one extra loss computation for each weight, which is too slow for large models. [[Backpropagation]] computes the same gradient with one backward pass through a computational graph. The CSCI 566 Syllabus covers gradient descent in week 3 and backpropagation in week 4.

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

- [[Block 1 Slides]], pp. 317–338
- [[Block 3 Slides]], pp. 14–16, 71–73, 208–214
- CSCI 566 Syllabus, weeks 3–4
- [[Block 7 Slides]], pp. 10, 85–90, 92–97, 101, 118–119
- [[F26-midterm-review-234p]], pp. 94–95, 105–108, 110
