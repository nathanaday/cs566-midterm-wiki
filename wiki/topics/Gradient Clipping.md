---
description: Gradient clipping rescales the gradient to a threshold norm before the optimizer step, so one large gradient cannot cause a huge update.
aliases: [Norm Clipping, Global gradient norm clipping]
sources: ["[[Block 3 Slides]]", "[[Block 5 Slides]]", "[[F26-midterm-review-234p]]"]
---

## Definition

Gradient clipping scales the gradient down before the SGD update when its norm is greater than a threshold ([[Block 3 Slides]], p. 235, citing Pascanu et al. 2013, "On the difficulty of training recurrent neural networks"):

```
g ← ∂E/∂θ
if ‖g‖ ≥ threshold:
    g ← (threshold / ‖g‖) · g
```

"Take a step in the same direction, but a smaller step" (p. 235). The midterm review repeats this slide and the next one ([[F26-midterm-review-234p]], pp. 102–103).

[[Block 5 Slides]] states the same rule as "Scale gradient if its norm is too big" (p. 104):

```
n = ‖g‖₂
if n > τ:  g ← (τ / n) g
```

Synthesis: the two decks differ only at $n = \tau$ ($\ge$ against $>$). At that point the scale factor is 1, so the result is the same.

## Explanation

Clipping is the slides' fix for the [[Exploding Gradient Problem]]. On the loss surface of a simple RNN (the hidden state is a scalar), a steep "cliff" gives a large gradient. Without clipping, gradient descent takes "two very big steps", climbs the cliff, and shoots off to the right. With clipping, the steps are smaller and the effect is "less drastic" ([[Block 3 Slides]], p. 236, citing Goodfellow, Bengio, and Courville, *Deep Learning*, 2016, §10.11.1).

### Global and coordinate clipping

"Clipping rescales the whole gradient vector so its norm is at most the threshold" ([[F26-midterm-review-234p]], p. 104):

$$g' = \min\left(1, \frac{c}{\lVert g \rVert_2}\right) g$$

Example: $g = (3, 4)$, $\lVert g \rVert_2 = 5$, and $c = 2$. The scale is $2/5$, so $g' = (1.2, 1.6)$ (p. 104).

- "Global clipping applies one scale, so the gradient direction is kept."
- The gradient is "Unchanged if norm <= threshold".
- "coordinate clipping caps each entry". In the example it gives $(2, 2)$ (p. 104).

Synthesis: the $\min$ form is the pseudocode above written as one line. Coordinate clipping changes the direction: $(2, 2)$ points at 45°, and $(3, 4)$ does not. The norm of $(2, 2)$ is $2\sqrt{2} \approx 2.83$, which is above $c = 2$.

### In recurrent networks

In a vanilla RNN, gradients can explode when the largest singular value of $W_{hh}$ is greater than 1, because the backward pass multiplies by $W_{hh}^{T-1}$ ([[Block 5 Slides]], p. 103). The slides point from this case to gradient clipping (p. 104). Clipping does not help the opposite case: for vanishing gradients the slides change the RNN architecture instead (p. 105). See [[Recurrent Neural Networks (RNN)]] and Backpropagation Through Time.

### Clipping is training triage

From [[Block 3 Slides]], p. 237:

- **Signal:** log the gradient norm beside the loss. A norm spike often comes before a loss jump.
- **Clip:** rescale the gradient before the optimizer step. The direction stays; the step length does not.
- **Escalate:** depending on the system, skip a batch, restore a checkpoint, or check the data and the learning rate.
- **Practice:** OLMo (ACL 2024) publishes its clipping setting. ZClip (arXiv:2504.02507) treats spikes as routine.

"Clipping limits the damage of one step. Finding the cause is a separate job" (p. 237).

## Related

- [[Exploding Gradient Problem]]
- [[Vanishing Gradient Problem]]
- [[Gradient Descent]]
- [[Gradient-Based Optimizers]]: the step that follows the clip
- [[Recurrent Neural Networks (RNN)]]
- Backpropagation Through Time

## Sources

- [[Block 3 Slides]], pp. 234–237
- [[Block 5 Slides]], pp. 103–105
- [[F26-midterm-review-234p]], pp. 102–104
