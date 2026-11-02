---
description: LoRA (low-rank adaptation) keeps a pretrained weight matrix W frozen and trains a low-rank update ΔW = BA, so the layer computes (W + BA)x.
aliases: [Low-Rank Adaptation, LoRA Updates]
sources: ["[[Block 3 Slides]]", "Sep 14 Lecture Account", "[[Block 7 Slides]]"]
subject: 5 Transfer learning and fine-tuning
---

## Definition

LoRA (low-rank adaptation) is a [[Parameter-Efficient Fine-Tuning]] method. It freezes a pretrained weight matrix $W_0$ and learns a small low-rank delta $\Delta W = BA$, so the layer computes $(W_0 + BA)x$. Only $A$ and $B$ train (Hu et al., ICLR 2022).

### The Update

**Low-rank update.**

$$z = W_0 x + B A x = (W_0 + BA)x$$

- $W_0$ is $d \times k$ and frozen.
- $B$ is $d \times r$, $A$ is $r \times k$, with $r \ll \min(d, k)$.
- The change must be expressible as $BA$ at rank $r$, so it has fewer degrees of freedom than a full update.

**Scaling.** The update is scaled by $\alpha / r$:

$$z = W_0 x + \frac{\alpha}{r} B A x$$

With $\alpha$ fixed, changing $r$ keeps the update magnitude comparable.

**Initialization.** $B = 0$ and $A$ random Gaussian, so $BA = 0$ at step zero and the adapted layer starts as the pretrained layer. See [[Weight Initialization]].

### Parameter Count

**Trainable parameters.**

$$\text{Full: } d \cdot k \qquad \text{LoRA: } r(d + k)$$

The saving depends on rank and matrix shape. The $d \cdot k$ frozen entries of $W_0$ still need to be stored.

| Case | Full | LoRA | Ratio |
| --- | --- | --- | --- |
| $8 \times 6$, $r = 2$ | 48 | 28 | 58% |
| $4096 \times 4096$, $r = 8$ | 16.8M | 65,536 | 0.4% |

### Rank Choice

- Smaller $r$: fewer parameters, a more restricted set of changes.
- Larger $r$: more parameters, more possible changes. More capacity does not guarantee better accuracy.
- Validation decides; rank is a hyperparameter searched with learning rate and weight decay.

### Inference and Comparison to Adapters

**Merge.** After training, fold the update into the weights once: $W = W_0 + BA$. Inference then costs no more than the base model. One base model can hold a swappable update per task.

| | LoRA | [[Adapters]] |
| --- | --- | --- |
| Pretrained weights | Frozen | Frozen |
| What is added | $BA$ to selected weights | Small module in the forward pass |
| Inference cost after training | None (merged) | Module stays |
| Learns | An update to $W$ | A new sub-network |

> [!tip]
> The low-rank object is the update $\Delta W = BA$, not $W_0$. LoRA does not factorize the original matrix.

> [!tip]
> PEFT reduces parameter updates, not backpropagation. The backward pass still runs through frozen layers to reach $A$ and $B$; optimizer state shrinks, activation memory can stay large. See [[Backpropagation]].

## Related

- [[Parameter-Efficient Fine-Tuning]]
- [[Adapters]]
- [[Fine-Tuning]]
- HyperTuning: generates LoRA parameters from task demonstrations
- [[Weight Initialization]]
- Updating LLMs
- Post-Training
- Test-Time Training: trains a LoRA adapter per test input
- [[Backpropagation]]
- [[Gradient Descent]]

## Sources

- [[Block 3 Slides]]
- Sep 14 Lecture Account
- [[Block 7 Slides]]
