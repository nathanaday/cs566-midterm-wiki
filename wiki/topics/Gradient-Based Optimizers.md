---
id: doc-bn9htg
type: topic
kind: concept
description: The update rules that turn gradients into parameter steps (SGD, SGD + Momentum, AdaGrad, RMSProp, Adam, and AdamW), compared by what each remembers and how it scales each step.
tags: [machine-learning/cs566-deeplearning]
aliases: [Optimizer, SGD + Momentum, SGD with momentum, Momentum, AdaGrad, Adagrad, RMSProp, Leaky AdaGrad, Adam, Adam optimizer, AdamW, Decoupled weight decay, Adaptive optimizers, Adaptive learning rates, Per-parameter learning rates]
created: 2026-10-12T16:58:10
updated: 2026-10-19T17:48:15
refreshed: 2026-10-19T17:48:15
status: stable
sources: ["[[Block 7 Slides]]", "[[Block 3 Slides]]", "[[Block 2 Slides]]", "[[F26-midterm-review-234p]]"]
up: ["Neural Network Training", "Optimization"]
---

> [!concept] Concept
> 4 sources · refreshed 2026-10-19 · #machine-learning/cs566-deeplearning
> Up: Neural Network Training · Optimization

## Definition

An optimizer is the rule that turns a gradient into a parameter update. "Optimizers consume gradients; they do not produce them" ([[Block 3 Slides]], p. 16). [[Backpropagation]] produces the gradients. The midterm review says the same: "The optimizer is a separate step that uses the computed gradients to update parameters" ([[F26-midterm-review-234p]], p. 78). The base rule is SGD, $x_{t+1} = x_t - \alpha \nabla f(x_t)$ ([[Block 7 Slides]], p. 101). The other optimizers in the course change two things: what the rule remembers from past steps, and how it scales each step ([[Block 7 Slides]], p. 116).

## Explanation

### Comparison

[[Block 7 Slides]] compares five optimizers (p. 116):

| Method | What it remembers | How it updates |
| --- | --- | --- |
| SGD | Current gradient | Update using this gradient. |
| SGD + Momentum | Recent signed gradients | Smooth the update direction. |
| AdaGrad | All past squared gradients | Scale each parameter's step. Steps can become tiny. |
| RMSProp | Recent squared gradients | Scale each parameter's step. Older gradients fade. |
| Adam | Recent signed gradients and squared gradients | Smooth the direction and scale each parameter's step. |

"All five still need a learning rate." The slide cites Duchi et al. (2011), Tieleman & Hinton (2012), and Kingma & Ba (2015) ([[Block 7 Slides]], p. 116). A later slide repeats the point: "SGD, SGD+Momentum, Adagrad, RMSProp, Adam all have learning rate as a hyperparameter" (p. 119). Learning Rate Schedules covers how the learning rate changes during training.

### SGD

SGD is "the simple two line update code" ([[Block 7 Slides]], p. 101):

```python
while True:
  dx = compute_gradient(x)
  x -= learning_rate * dx
```

SGD remembers only the current gradient (p. 116). [[Gradient Descent]] covers the full-data and minibatch forms. On real loss surfaces, plain SGD meets poor conditioning, local minima and saddle points, and noisy minibatch gradients ([[Block 7 Slides]], pp. 92–97). Optimization explains these problems. Momentum and per-parameter step scaling respond to them (pp. 99, 108).

### SGD + Momentum

"Updates can zigzag even when the long-term direction is consistent." Momentum combines the current gradient with recent directions to form the parameter update. "Momentum smooths the update direction over time" ([[Block 7 Slides]], p. 100).

The update keeps a velocity $v$ ([[Block 7 Slides]], pp. 102–103):

$$v_{t+1} = \rho v_t + \nabla f(x_t)$$

$$x_{t+1} = x_t - \alpha v_{t+1}$$

```python
vx = 0
while True:
  dx = compute_gradient(x)
  vx = rho * vx + dx
  x -= learning_rate * vx
```

- "Build up 'velocity' as a running mean of gradients" (p. 102).
- "Rho gives 'friction'; typically rho=0.9 or 0.99" (p. 102).
- The aim: "Reduce the oscillations in the rapid change directions" (p. 103).
- The actual step combines the gradient at the current point with the velocity (p. 105).

The midterm review repeats the slides of pp. 100 and 102 ([[F26-midterm-review-234p]], pp. 109–110). It then shows that the stored history changes the step (p. 111). The convention is $m_{new} = 0.5\, m_{old} + g$, then $w_{new} = w - 0.1\, m_{new}$. The current gradient is $g = 2$ in both cases:

| Stored history | $m_{new}$ | Step $\Delta w$ |
| --- | --- | --- |
| $m_{old} = 0$ | 2 | −0.2 |
| $m_{old} = 4$ | 4 | −0.4 |

"With g = 2 and m_old = 4, m_new = 4 and the step is -0.4, so history matters" ([[F26-midterm-review-234p]], p. 111). Synthesis: this is the update of p. 102 with $\rho = 0.5$ and $\alpha = 0.1$.

An alternative form is $v_{t+1} = \rho v_t - \alpha \nabla f(x_t)$ and $x_{t+1} = x_t + v_{t+1}$. "You may see SGD+Momentum formulated different ways, but they are equivalent - give same sequence of x" ([[Block 7 Slides]], p. 104).

A figure compares SGD with SGD+Momentum for local minima, saddle points, poor conditioning, and gradient noise ([[Block 7 Slides]], p. 99). Under poor conditioning, the SGD path zigzags and the momentum path is smooth. In the local-minimum and saddle-point panels, an arrow points onward from the ball. The slide has no text for these panels, so the claim that velocity carries the update past them is drawn, not stated.

Synthesis: the slide calls the velocity a "running mean", but the formula has no $(1 - \rho)$ factor, so $v$ is a decaying sum of past gradients. Adam's first moment has the factor $(1 - \beta_1)$ ([[Block 7 Slides]], p. 113). When both start at zero, the two forms differ by the constant factor $(1 - \rho)$, and the learning rate can absorb it.

The slides cite Sutskever et al., "On the importance of initialization and momentum in deep learning", ICML 2013 ([[Block 7 Slides]], pp. 102–105), and two works by Nesterov, from 1983 and 2004 (p. 105).

### Adaptive learning rates

"Different weights can experience very different gradient magnitudes." An adaptive optimizer keeps two estimates and uses them to scale each coordinate ([[Block 7 Slides]], p. 112):

| Part | Job |
| --- | --- |
| Momentum estimate | Track a smoothed gradient direction. |
| Magnitude estimate | Track recent squared-gradient magnitude. |
| Adaptive update | Rescale each coordinate using these estimates. |

[[Block 3 Slides]] gives the same reason: "One raw step size is too small for some parameters and unstable for others" ([[Block 3 Slides]], p. 16).

### AdaGrad

```python
grad_squared = 0
while True:
  dx = compute_gradient(x)
  grad_squared += dx * dx
  x -= learning_rate * dx / (np.sqrt(grad_squared) + 1e-7)
```

AdaGrad "Added element-wise scaling of the gradient based on the historical sum of squares in each dimension". The slide calls this "Per-parameter learning rates" or "adaptive learning rates" ([[Block 7 Slides]], p. 106).

- On an elongated loss surface, "Progress along 'steep' directions is damped; progress along 'flat' directions is accelerated" (p. 108).
- The sum keeps all past squared gradients (p. 116). Over a long time, "Steps may become tiny" (p. 110).

The slide cites Duchi et al., "Adaptive subgradient methods for online learning and stochastic optimization", JMLR 2011 ([[Block 7 Slides]], p. 106).

### RMSProp

The slides call RMSProp "Leaky AdaGrad" ([[Block 7 Slides]], p. 111). It changes only the accumulator line of AdaGrad:

```python
grad_squared = 0
while True:
  dx = compute_gradient(x)
  grad_squared = decay_rate * grad_squared + (1 - decay_rate) * dx * dx
  x -= learning_rate * dx / (np.sqrt(grad_squared) + 1e-7)
```

RMSProp remembers recent squared gradients, and older gradients fade (p. 116). The slide cites Tieleman and Hinton, 2012 (p. 111). The slides give no typical value for `decay_rate`.

### Adam

Adam keeps a first moment and a second moment of the gradient. The slides first show "Adam (almost)" ([[Block 7 Slides]], p. 113):

```python
first_moment = 0
second_moment = 0
while True:
  dx = compute_gradient(x)
  first_moment = beta1 * first_moment  + (1 - beta1) * dx
  second_moment = beta2 * second_moment + (1 - beta2) * dx * dx
  x -= learning_rate * first_moment / (np.sqrt(second_moment) + 1e-7))
```

The first-moment line is the momentum part. The second-moment line and the scaled update are the AdaGrad / RMSProp part: "Sort of like RMSProp with momentum". The slide then asks, "Q: What happens at first timestep?" ([[Block 7 Slides]], p. 114). The code on pp. 113–115 has an unmatched closing parenthesis on the update line; the code here keeps it as the slide shows it.

The full form adds bias correction ([[Block 7 Slides]], p. 115):

```python
first_moment = 0
second_moment = 0
for t in range(1, num_iterations):
  dx = compute_gradient(x)
  first_moment = beta1 * first_moment  + (1 - beta1) * dx
  second_moment = beta2 * second_moment + (1 - beta2) * dx * dx
  first_unbias = first_moment / (1 - beta1 ** t)
  second_unbias = second_moment / (1 - beta2 ** t)
  x -= learning_rate * first_unbias / (np.sqrt(second_unbias) + 1e-7))
```

"Bias correction for the fact that first and second moment estimates start at zero" (p. 115). "Adam still needs a learning rate and a training schedule" (p. 112). The slides cite Kingma and Ba, "Adam: A method for stochastic optimization", ICLR 2015 (pp. 113–115). They give no typical values for `beta1` and `beta2`.

Synthesis: in the first steps both moments are near zero, so they underestimate the true moments. Division by $(1 - \beta^t)$ scales them up. This factor is small at small $t$ and goes to 1 as $t$ grows.

### AdamW

"AdamW Separates Weight Decay From Adaptation." "The gradient-based update and parameter shrinkage have different jobs." The update runs in three stages: the loss gradient, then an Adam-style adaptive step, then a separate weight decay. "L2 penalties and weight decay differ under adaptive updates." The slide cites Loshchilov & Hutter, Decoupled Weight Decay (ICLR 2019) ([[Block 7 Slides]], p. 117). The slides show no update equation for AdamW.

[[Block 3 Slides]] also describes AdamW: it rescales each coordinate by running gradient statistics and decays weights separately ([[Block 3 Slides]], p. 16). [[Block 2 Slides]] notes that an L2 penalty matches weight decay under plain SGD, but not under the decoupled form in AdamW ([[Block 2 Slides]], p. 100). See [[Regularization]].

### Beyond AdamW

[[Block 3 Slides]] names Muon and SOAP, which precondition whole weight matrices. The slide cites an unnamed NVIDIA study that "reports gains over AdamW at the scales they tested" ([[Block 3 Slides]], p. 16).

### Choosing an optimizer

"An Optimizer Is One Part of the Training Setup." "Compare complete runs under the same evaluation protocol." ([[Block 7 Slides]], p. 129):

| Choice | Slide's note |
| --- | --- |
| SGD + momentum | "A useful baseline for many vision models." |
| AdamW | "A useful baseline for many Transformer models." |
| For either choice | "Tune learning rate, decay, batch size and schedule." |

"Use validation results to compare the complete setup" (p. 129). The slide cites Loshchilov & Hutter, Decoupled Weight Decay (ICLR 2019).

## Related

- [[Gradient Descent]]: the base update rule, full-batch and minibatch SGD, and the role of the learning rate
- Optimization: poor conditioning, saddle points, and noisy minibatch gradients, the problems that momentum and adaptive steps address
- Learning Rate Schedules: every optimizer here still needs a learning rate and a schedule
- [[Backpropagation]]: produces the gradients that optimizers consume
- [[Regularization]]: L2 penalty versus decoupled weight decay
- [[Gradient Clipping]]: limits the gradient before the optimizer step
- CS566 Confidence Head Training Run 1: the project plan trains with AdamW

## Sources

- [[Block 7 Slides]], pp. 92–97, 99–117, 119, 129
- [[Block 3 Slides]], p. 16
- [[Block 2 Slides]], p. 100
- [[F26-midterm-review-234p]], pp. 78, 109–111
