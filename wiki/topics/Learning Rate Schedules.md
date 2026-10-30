---
id: doc-wjjxph
type: topic
kind: concept
description: A learning rate schedule is a planned change of the learning rate during training (step, cosine, linear, or inverse-sqrt decay, linear warmup, cyclical rates); CSCI 566 shows PyTorch's lr_scheduler classes and chooses rates by validation within a fixed budget.
tags: [machine-learning/cs566-deeplearning]
aliases: [Learning rate schedule, LR schedule, Learning rate decay, Step decay, Cosine learning rate decay, Cosine decay, Linear decay, Inverse square root decay, Linear warmup, Learning rate warmup, Warmup, Cyclical learning rates, CLR, Triangular learning rate policy, LR range test, torch.optim.lr_scheduler, PyTorch learning rate schedulers, LRScheduler, Learning rate search across scales, Log-scale learning rate search, Select the learning rate by validation performance, Compare complete training setups on validation results]
created: 2026-10-12T16:58:10
updated: 2026-10-13T18:22:47
refreshed: 2026-10-13T18:22:47
status: stable
sources: ["[[Block 7 Slides]]"]
up: ["[[Gradient-Based Optimizers]]"]
---

> [!concept] Concept
> 1 source · refreshed 2026-10-13 · #machine-learning/cs566-deeplearning
> Up: [[Gradient-Based Optimizers]]

## Definition

A learning rate schedule is "a planned change in learning rate" ([[Block 7 Slides]], p. 127). In vanilla gradient descent, the learning rate is the `step_size` in `weights += - step_size * weights_grad` (p. 118). A schedule changes that value during training, because "Early training and late refinement need not use the same learning rate" (p. 127).

## Explanation

### Why the rate matters

SGD, SGD+Momentum, Adagrad, RMSProp, and Adam all have the learning rate as a hyperparameter (p. 119). The slide plots loss against epoch for four rates. With a very high rate, the loss goes up sharply. With a low rate, the loss goes down slowly. With a high rate, the loss drops fast and then stays at a higher level. With a good rate, the loss gets lowest (p. 119). See [[Gradient Descent]] for the update rule.

The course diagram has three stages: "Warm up from a small rate", then "Train at a chosen scale", then "Decay for finer updates" (p. 127).

### Decay schedules

Notation: $\alpha_0$ is the initial learning rate, $\alpha_t$ is the learning rate at epoch $t$, and $T$ is the total number of epochs (pp. 122–125).

| Schedule | Rule | Papers cited on the slide |
| --- | --- | --- |
| Step | "Reduce learning rate at a few fixed points. E.g. for ResNets, multiply LR by 0.1 after epochs 30, 60, and 90." (p. 121) | none |
| Cosine | $\alpha_t = \frac{1}{2}\alpha_0\left(1 + \cos(t\pi/T)\right)$ (p. 122) | Loshchilov and Hutter, "SGDR: Stochastic Gradient Descent with Warm Restarts", ICLR 2017; Radford et al., "Improving Language Understanding by Generative Pre-Training", 2018; Feichtenhofer et al., "SlowFast Networks for Video Recognition", arXiv 2018; Child et al., "Generating Long Sequences with Sparse Transformers", arXiv 2019 (pp. 122–123) |
| Linear | $\alpha_t = \alpha_0(1 - t/T)$ (p. 124) | Devlin et al., "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding", 2018 (p. 124) |
| Inverse sqrt | $\alpha_t = \alpha_0/\sqrt{t}$ (p. 125) | Vaswani et al., "Attention is all you need", NIPS 2017 (p. 125) |

The slides list each paper next to its formula. They do not say what each paper does with the schedule.

What the plots show:

- **Step** (p. 121): the training loss drops at each reduction point, near epochs 30, 60, and 90. It falls from about 4 at the start to about 1 by epoch 100.
- **Cosine** (p. 122): the learning rate falls along a half cosine from 1.0 at epoch 0 to 0 at epoch 100. On p. 123, the training loss under a cosine schedule falls smoothly over 300 epochs and is near 0 by about epoch 250.
- **Linear** (p. 124): the learning rate falls in a straight line from 1.0 at epoch 0 to 0 at epoch 100.
- **Inverse sqrt** (p. 125): the learning rate falls fast at first, then slowly, to about 0.1 at epoch 100. Open point: the formula is undefined at $t = 0$, but the plot starts at 1.0 at epoch 0. The slide does not say how it treats $t = 0$.

### Linear warmup

"Warmup gradually raises the learning rate to avoid unstable early updates. Its duration is a choice" (p. 126). In the example plot, the learning rate goes up in a straight line from 0 to about 0.58 in the first few epochs. Then it decays to about 0.1 by epoch 100 (p. 126). The slide cites Goyal et al., "Accurate, Large Minibatch SGD: Training ImageNet in 1 Hour", arXiv 2017 (p. 126).

The slide also says: "Linear batch-size scaling is an ImageNet SGD example, not a universal rule" (p. 126). It does not define linear batch-size scaling.

Synthesis: after the peak, the warmup plot has the same shape and end value (about 0.1 at epoch 100) as the inverse-sqrt plot on p. 125. The slide does not name the decay it uses after warmup.

### Cyclical learning rates

In the triangular policy, the learning rate moves up and down between a minimum bound (`base_lr`) and a maximum bound (`max_lr`). "The input parameter stepsize is the number of iterations in half a cycle" ([[Block 7 Slides]], p. 128, Figure 2 of Smith, "Cyclical learning rates for training neural networks", 2017 IEEE WACV).

A second figure is an "LR range test". It shows CIFAR-10 classification accuracy as the learning rate increases over 8 epochs (p. 128). In the plot, accuracy rises from about 0.1 near a rate of 0 to a peak of about 0.5 between rates of about 0.01 and 0.015. It falls again near 0.02. The slide does not say how to set `base_lr` and `max_lr` from this test.

Synthesis: the decay schedules above lower the rate in one direction. A cyclical schedule raises and lowers it many times.

### PyTorch: torch.optim.lr_scheduler

The slide shows part of the `torch.optim` documentation table (p. 128):

| Class | Description on the slide |
| --- | --- |
| `lr_scheduler.LRScheduler` | "Adjusts the learning rate during optimization." |
| `lr_scheduler.LambdaLR` | "Sets the initial learning rate." |
| `lr_scheduler.MultiplicativeLR` | "Multiply the learning rate of each parameter group by the factor given in the specified function." |
| `lr_scheduler.StepLR` | "Decays the learning rate of each parameter group by gamma every step_size epochs." |
| `lr_scheduler.MultiStepLR` | "Decays the learning rate of each parameter group by gamma once the number of epoch reaches one of the milestones." |
| `lr_scheduler.ConstantLR` | "Multiply the learning rate of each parameter group by a small constant factor." |
| `lr_scheduler.LinearLR` | "Decays the learning rate of each parameter group by linearly changing small multiplicative factor." |
| `lr_scheduler.ExponentialLR` | "Decays the learning rate of each parameter group by gamma every epoch." |

The slide shows these eight rows only. The LambdaLR row is the slide's full description of that class.

Synthesis: `MultiStepLR` with milestones at epochs 30, 60, and 90 and gamma 0.1 matches the ResNet step example on p. 121.

### Choosing the learning rate and the schedule

- To the question "Which one of these learning rates is best to use?", the slide answers: "Compare validation performance within the same training budget" (p. 120).
- Search across scales: "A broad first pass checks orders of magnitude." The example candidate rates are 0.0001, 0.001, 0.01, and 0.1. "Find a useful region, then search more closely." "These values illustrate spacing, not a universal recommendation." "A fixed compute budget makes comparisons meaningful" (p. 187).
- The deck's general steps for hyperparameters include "Find LR that makes loss go down", "Coarse grid, train for ~1-5 epochs", and "Refine grid, train longer" (p. 186).
- An optimizer is one part of the training setup: "Compare complete runs under the same evaluation protocol." For either optimizer choice (the slide names SGD + momentum and AdamW), "Tune learning rate, decay, batch size and schedule." "Use validation results to compare the complete setup" (p. 129). See [[Gradient-Based Optimizers]].

Synthesis: these slides all ask for the same conditions: the same training budget, the same evaluation protocol, and a decision on the validation split. This applies the rule in [[Model Evaluation]] to choose hyperparameters on validation data, not on training or test data.

## Related

- [[Gradient Descent]]: the update rule whose step size a schedule changes
- [[Gradient-Based Optimizers]]: each optimizer has a learning rate to schedule
- [[Model Evaluation]]: choose hyperparameters on a validation split
- [[Model Selection]]
- [[Early Stopping]]
- [[ResNet]]: that topic records a divide-by-10 rule when validation error plateaus. This deck gives fixed epochs 30, 60, and 90 as its step example.
- [[CLIP]]: trained with cosine learning rate decay
- [[Transformers]]: the inverse-sqrt slide cites Vaswani et al.

## Sources

- [[Block 7 Slides]], pp. 118–129, 186–187
