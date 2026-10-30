---
description: The failure in which a ReLU unit's pre-activation is negative on every training example, so it outputs zero, gets a zero gradient, and stops learning.
aliases: [Dead ReLU, Dead Neurons]
sources: ["[[Block 3 Slides]]", "[[Block 7 Slides]]", "[[F26-midterm-review-234p]]"]
subject: 2 Neural networks
---

## Definition

ReLU "can suffer from 'dying ReLU' problem, where neurons can become inactive on all current training examples" ([[Block 3 Slides]], p. 77). The midterm review repeats this sentence ([[F26-midterm-review-234p]], p. 50).

A ReLU unit outputs 0 and has a gradient of 0 for every negative pre-activation ([[Activation Functions]]). The problem "occurs when ReLU neurons become inactive and output zero on every current training example. This happens when the weights shift so that the neuron's pre-activation is negative on every training example, which zeroes its gradient and stalls its learning" ([[Block 3 Slides]], p. 92).

## Explanation

### Causes

"If the input is always negative (bad learning rate, inappropriate data preprocessing) – they are 'died'" ([[Block 3 Slides]], p. 261). Block 3 names these causes but does not work an example.

If many activations fall into the negative range, ReLU outputs zero and receives zero gradient. This creates "dead neurons", which "stop learning from that data until upstream changes revive them". The slides call this "a significant issue in deep models with large FFN layers, where some neurons may never activate after certain weight updates" (p. 81).

### A numeric example

The midterm review works one example, "Dead ReLU: A Numeric Path to Zero Gradient" ([[F26-midterm-review-234p]], p. 97):

| Step | Value |
| --- | --- |
| Input and parameters | $x = 1$, $w = -0.7$, $b = -0.5$ |
| Pre-activation | $z = wx + b = -1.2$ |
| Output | $a = \text{ReLU}(z) = 0$ |
| Local derivative | $da/dz = 0$ |
| Weight gradient | $dL/dw = 0$ |

"If this unit stays on the negative side for relevant training examples, the local gradient cannot move its incoming weights." "The issue is a whole negative region with zero local derivative, not the single point z = 0." "A dead ReLU outputs zero and blocks the gradient on the data that keep its pre-activation negative" (p. 97).

Synthesis: the review puts the problem in the whole negative region, not in the missing derivative at $z = 0$ that [[Activation Functions]] notes. The definition above asks for a negative pre-activation on every training example. The review's last sentence describes the same block on any part of the data that keeps the pre-activation negative.

### Fixes

- Leaky ReLU and Parametric ReLU (PReLU) "allow a small, positive gradient when the unit is not active, thereby keeping the neurons alive" ([[Block 3 Slides]], p. 92). Leaky ReLU is "less prone to 'dying'" (p. 264).
- [[Block 7 Slides]] states the same mechanism. For Leaky ReLU, $\max(0.01x, x)$: "A small negative slope preserves a local gradient path" (p. 52). For Leaky ReLU and PReLU: "Leaky fixes α; PReLU learns α. Negative inputs pass a gradient" (p. 53).
- Leaky ReLU, PReLU, and ELU "can also be used to avoid dead neurons in ReLU" ([[Block 3 Slides]], p. 232).
- GELU has a soft threshold, so neurons "have a chance of recovering instead of being stuck at zero output" (p. 82).

### Why it matters

The slides call ReLU "a good default choice for most problems" ([[Block 3 Slides]], p. 75), and dying ReLU is the limitation they list for it (p. 77). The midterm review lists the same limitation ([[F26-midterm-review-234p]], p. 50). Plain ReLU still learns in practice; [[Block 3 Slides]] gives four reasons (pp. 262-263), listed in [[Activation Functions]].

Open question: does the course measure how often units die, or only name the risk?

## Related

- [[Activation Functions]]
- [[Activation Sparsity]]: zero outputs are also the source of ReLU's sparsity
- [[Vanishing Gradient Problem]]
- [[Backpropagation]]: a zero local derivative stops the chain rule at the unit
- [[Gradient Descent]]

## Sources

- [[Block 3 Slides]], pp. 75, 77, 81-82, 92, 232, 261-264
- [[Block 7 Slides]], pp. 52-53
- [[F26-midterm-review-234p]], pp. 50, 97
