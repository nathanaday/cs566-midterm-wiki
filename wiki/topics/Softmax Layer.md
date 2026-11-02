---
description: The last layer of a classification network, which maps the raw class scores (logits) to a probability distribution with sigma(z)_i = e^{z_i} / sum_j e^{z_j}.
aliases: [Softmax, Softmax Function]
sources: ["[[Block 4 Slides]]", "Lecture 3 Notes - Convolutional and Pooling Layers"]
subject: 2 Neural networks
---

## Definition

The softmax layer maps the raw class scores (logits) of a network to a probability distribution over the $K$ output classes. It is the last layer of a classification network, and its output feeds the cross-entropy loss, so the course also calls it the loss layer.

### Formulas

**Softmax.** For class $i$ of $K$, with logit vector $z$:

$$\sigma(z)_i = \frac{e^{z_i}}{\sum_{j=1}^{K} e^{z_j}}$$

**Cross-entropy loss.** With one-hot target $y$, prediction $p = \sigma(z)$, and true class $c$:

$$L = -\sum_{i=1}^{K} y_i \log p_i = -\log p_c$$

**Combined gradient.** Softmax and cross-entropy together give a gradient with respect to the logits of

$$\frac{\partial L}{\partial z} = p - y$$

**Numerical stability.** Subtract the largest logit before exponentiating. The shift cancels in the ratio, so the probabilities do not change:

$$\sigma(z)_i = \frac{e^{z_i - \max_j z_j}}{\sum_{j=1}^{K} e^{z_j - \max_j z_j}}$$

### Facts to Recall

- Outputs are positive and sum to one; the class with the top probability is the prediction.
- The layer is nonlinear and has one node per class.
- It is one of the four CNN layer types, with the convolutional, pooling, and [[Fully Connected Layer|FC]] layers.
- In [[AlexNet]] the softmax follows the last FC layer.
- Quick check from [[Loss Functions]]: logits $(\ln 2, 0, 0)$ give probabilities $(0.5, 0.25, 0.25)$.

> [!warning] Exam trap
> Softmax is a layer, not a loss. The loss is cross-entropy applied to its output; the course names the pair the loss layer.

> [!tip]
> Without the max shift, a large logit overflows $e^{z_i}$.

## Related

- [[Convolutional Neural Networks (CNN)]]
- [[Fully Connected Layer]]
- [[Loss Functions]]
- Autoregressive Language Modeling
- [[Linear Classification]]

## Sources

- [[Block 4 Slides]]
- Lecture 3 Notes - Convolutional and Pooling Layers
