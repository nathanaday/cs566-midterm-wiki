---
description: The last layer of a classification network, which maps the raw class scores (logits) to a probability distribution with sigma(z)_i = e^{z_i} / sum_j e^{z_j}.
aliases: [Softmax, Softmax Function]
sources: ["[[Block 4 Slides]]", "Lecture 3 Notes - Convolutional and Pooling Layers"]
subject: 2 Neural networks
---

## Definition

The softmax layer maps the raw class scores (logits) of a network to a probability distribution over the $K$ output classes. It is the last layer of a classification network, and its output feeds the cross-entropy loss, so the course also calls it the loss layer.

- Outputs are positive and sum to one; the class with the top probability is the prediction.
- The layer is nonlinear and has one node per class.
- Softmax is a layer, not a loss. The loss is cross-entropy applied to its output.

### Formulas

**Softmax.** For class $i$ of $K$, with logit vector $z$:

$$\sigma(z)_i = \frac{e^{z_i}}{\sum_{j=1}^{K} e^{z_j}}$$

**Cross-entropy loss.** With one-hot target $y$, prediction $p = \sigma(z)$, and true class $c$:

$$L = -\sum_{i=1}^{K} y_i \log p_i = -\log p_c$$

**Combined gradient.** Softmax and cross-entropy together give a gradient with respect to the logits of

$$\frac{\partial L}{\partial z} = p - y$$



## Related

- [[Convolutional Neural Networks (CNN)]]
- [[Fully Connected Layer]]
- [[Loss Functions]]
- Autoregressive Language Modeling
- [[Linear Classification]]

## Sources

- [[Block 4 Slides]]
- Lecture 3 Notes - Convolutional and Pooling Layers
