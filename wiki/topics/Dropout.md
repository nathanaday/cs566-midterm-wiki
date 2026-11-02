---
description: A regularizer that sets a random subset of hidden activations to zero in each training forward pass, then turns the mask off at evaluation and uses a classic or inverted scaling convention so that training and evaluation scales match.
aliases: [Dropout regularization, Classic dropout, Inverted dropout]
sources: ["[[Block 7 Slides]]", "[[F26-midterm-review-234p]]"]
subject: 3 Training
---

## Definition

Dropout zeros a random subset of hidden activations in each training forward pass and draws a new mask every step; the weights stay. Evaluation turns the mask off and applies one scaling convention so that training and evaluation activations keep the same expected size. It is one of the [[Regularization]] methods that add noise in training and use the full model at test time; dropping half the units is the common default.

### Why It Helps

- **Redundant features.** A score must survive losing any subset of its features, which prevents co-adaptation.
- **Ensemble.** Each mask is one model and all masks share parameters; an FC layer of 4096 units has $2^{4096}$ masks.

### Expectation Argument

Training output is random, $y = f_W(x, z)$ with mask $z$. Evaluation wants the average over masks:

**Mask average.**
$$y = E_z[f(x, z)] = \int p(z)\, f(x, z)\, dz$$

For one linear unit $a = w_1 x + w_2 y$ with drop probability 0.5, the four masks are equally likely:

**Two-input unit.**
$$E[a] = \tfrac{1}{4}(w_1x + w_2y) + \tfrac{1}{4}(w_1x) + \tfrac{1}{4}(w_2y) + \tfrac{1}{4}(0) = \tfrac{1}{2}(w_1x + w_2y)$$

Training output averages half the evaluation output, so one side must rescale. The rule is exact for the expected input of one linear unit; through nonlinear layers the scaled network only approximates the integral.

### Scaling Conventions

Let $q$ be the keep probability, so the drop probability is $1 - q$.

| Convention | Training | Evaluation |
| --- | --- | --- |
| Classic | Keep unchanged, or zero | Multiply by $q$ |
| Inverted (more common) | Keep divided by $q$, or zero | Unchanged |

Worked example, inverted, $q = 0.5$, activation 2: kept outputs $2 / 0.5 = 4$, dropped outputs 0, expected training output $0.5 \times 4 + 0.5 \times 0 = 2$, evaluation output 2 with the mask off. The expectation across masks is preserved; one pass gives 0 or 4.

**Inverted dropout, one hidden layer.**

```python
p = 0.5                                   # keep probability
H1 = np.maximum(0, np.dot(W1, X) + b1)
U1 = (np.random.rand(*H1.shape) < p) / p  # mask scaled by 1/p
H1 *= U1
```

Each hidden layer draws its own mask; the output layer has none. Classic dropout omits the `/ p` here and instead multiplies each hidden layer by `p` in `predict`.

> [!tip]
> At evaluation the mask is off and the output is deterministic. Inverted dropout needs no scaling, since the $1/q$ already happened in training; classic dropout multiplies by $q$. With inverted $q = 0.8$ (training scale 1.25), scaling by 0.8 at evaluation shrinks the output and scaling by 1.25 inflates it.

> [!tip] Naming of p
> Lecture prose uses `p` for the drop probability, but the code uses `p` and `q` for the keep probability; the two agree only at 0.5, so check which one a framework means.

### Use

Turn off the mask at evaluation and apply the chosen convention, as in [[Switch the Model to Evaluation Mode When Evaluating]]. Pair with [[Early Stopping]] when the validation protocol allows; the diagnosis table is in [[Regularization]].

## Related

- [[Regularization]]
- [[Batch Normalization]]
- [[Data Augmentation]]
- [[Early Stopping]]
- [[Overfitting and Underfitting]]
- [[Neural Networks]]
- [[Activation Functions]]
- [[Switch the Model to Evaluation Mode When Evaluating]]: evaluation turns the mask off

## Sources

- [[Block 7 Slides]]
- [[F26-midterm-review-234p]]
