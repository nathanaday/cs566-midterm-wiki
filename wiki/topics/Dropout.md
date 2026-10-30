---
description: A regularizer that sets a random subset of hidden activations to zero in each training forward pass, then turns the mask off at evaluation and uses a classic or inverted scaling convention so that training and evaluation scales match.
aliases: [Dropout regularization, Classic dropout, Inverted dropout, Dropout test-time scaling, Dropout scaling conventions]
sources: ["[[Block 7 Slides]]", "[[F26-midterm-review-234p]]"]
---

## Definition

"During training, some hidden activations are randomly set to zero" ([[Block 7 Slides]], p. 140; [[F26-midterm-review-234p]], p. 128). In each forward pass, dropout sets some neurons to zero at random. The probability of dropping is a hyperparameter, and 0.5 is common ([[Block 7 Slides]], p. 141, citing Srivastava et al., "Dropout: A simple way to prevent neural networks from overfitting", JMLR 2014).

Dropout is one of the methods in [[Regularization]] that add randomness during training and use the full model at test time.

## Explanation

### The mask changes at each step

In one training step, some feature activations are kept and the others are temporarily zeroed. In the next step, a new random mask keeps a different subset of activations. "The weights remain. The activation mask changes" ([[Block 7 Slides]], p. 140). [[F26-midterm-review-234p]] repeats this slide (p. 128).

### Code: a training step

The slides give a NumPy forward pass for a 3-layer network ([[Block 7 Slides]], p. 142). After each ReLU hidden layer, the code makes a binary mask and multiplies the layer by it:

```python
p = 0.5 # probability of keeping a unit active. higher = less dropout
H1 = np.maximum(0, np.dot(W1, X) + b1)
U1 = np.random.rand(*H1.shape) < p # first dropout mask
H1 *= U1 # drop!
```

The second hidden layer gets its own mask `U2` in the same way. The output layer has no mask.

> [!warning] Naming of p
> The slides use two meanings. On p. 141, the hyperparameter is the probability of *dropping*. In the code on pp. 142 and 152, `p` is the probability of *keeping* a unit. On p. 151, `q` is the keep probability and the drop probability is `1 − q`. With the common value 0.5, the two meanings give the same number. With other values they do not. Check which meaning a framework uses. The midterm review writes "Inverted dropout, p = 0.5" for a keep probability of 0.5 ([[F26-midterm-review-234p]], p. 131), and uses q = 0.8 as a keep probability (p. 132).

### Why it helps

The slides give two interpretations:

- **Redundant features.** Dropout "forces the network to have a redundant representation" and "prevents co-adaptation of features". In the example, a cat score uses features such as "has an ear", "has a tail", "is furry", "has claws", and "mischievous look". The score must still work when some of these features are dropped ([[Block 7 Slides]], p. 143).
- **An ensemble.** "Dropout is training a large ensemble of models (that share parameters)." Each binary mask is one model. An FC layer with 4096 units has $2^{4096} \sim 10^{1233}$ possible masks. The slide compares this with "only ~ $10^{82}$ atoms in the universe" ([[Block 7 Slides]], p. 144).

### Test time: average out the mask

Dropout makes the output random: $y = f_W(x, z)$, where $z$ is the random mask. At test time we want to "average out" the randomness ([[Block 7 Slides]], p. 145):

$$y = f(x) = E_z[f(x, z)] = \int p(z) f(x, z)\, dz$$

The slide says this integral "seems hard". To approximate it, the slides take one neuron $a$ with two inputs $x$ and $y$ and weights $w_1$ and $w_2$ ([[Block 7 Slides]], pp. 146–148):

- At test time, with no mask: $E[a] = w_1 x + w_2 y$.
- During training, with drop probability 0.5, each of the four masks has probability 1/4:

$$E[a] = \tfrac{1}{4}(w_1x + w_2y) + \tfrac{1}{4}(w_1x + 0y) + \tfrac{1}{4}(0x + 0y) + \tfrac{1}{4}(0x + w_2y) = \tfrac{1}{2}(w_1x + w_2y)$$

Thus the training output is, on average, half the test output. The scale must be matched.

### Scaling conventions

Let $q$ be the probability of keeping an activation. The dropping probability is $1 - q$ ([[Block 7 Slides]], p. 151).

| Convention | Training | Evaluation |
| --- | --- | --- |
| Classic dropout | Keep the activation unchanged, or set it to zero. | Multiply it by $q$. |
| Inverted dropout | Keep the activation divided by $q$, or set it to zero. | Use it unchanged. |

"Each convention matches training and evaluation scales" ([[Block 7 Slides]], p. 151). [[F26-midterm-review-234p]] repeats this slide (p. 129).

**Classic dropout.** "Classic convention: multiply by the KEEP probability" ([[Block 7 Slides]], p. 149). The example `predict` function multiplies each hidden layer by `p`, with the comment "NOTE: scale the activations", in an "ensembled forward pass" ([[Block 7 Slides]], p. 150).

**Inverted dropout.** The slides call it "more common". The mask divides by `p` in training: `U1 = (np.random.rand(*H1.shape) < p) / p`. Then "test time is unchanged": `predict` has "no scaling necessary" ([[Block 7 Slides]], p. 152).

Worked example ([[Block 7 Slides]], p. 153): a hidden activation is 2 and the keep probability is 0.5. A kept unit outputs 2 / 0.5 = 4. A dropped unit outputs 0. The expected training output is 0.5 × 4 + 0.5 × 0 = 2. At evaluation the activation stays 2, with no dropout mask. "The preserved quantity is an expectation across masks." [[F26-midterm-review-234p]] repeats this slide (p. 130).

A second review slide draws the same case as two branches: "With keep probability 0.5, a kept activation is doubled, so the average training output matches evaluation." The kept branch outputs 4 and the dropped branch outputs 0, and at evaluation the slide reads "Eval: dropout off, output 2". Its note: "Same expected scale; one pass gives 0 or 4" ([[F26-midterm-review-234p]], p. 131).

### Check: inverted dropout at evaluation

The midterm review asks a check question ([[F26-midterm-review-234p]], p. 132). A layer uses inverted dropout with keep probability q = 0.8. In training, a random mask zeros some activations and scales the kept ones by 1.25. What happens in evaluation mode? The slide grades each option (p. 133):

| Option | Verdict |
| --- | --- |
| Apply a random mask that drops 20% and scale the kept activations by 1.25, as in training. | Wrong: "evaluation should be deterministic, so no random dropout mask is applied." |
| Disable the dropout mask and pass activations through with no extra scaling. | Correct: "the 1/q scaling already happened in training, so average sizes already match." |
| Disable the dropout mask and multiply every activation by 0.8. | Wrong: "scaling by q at test time is the non-inverted convention and would shrink outputs here." |
| Disable the dropout mask and multiply every activation by 1.25. | Wrong: "1.25 offsets dropped units only in training; at evaluation it would inflate outputs." |

Synthesis: 1.25 is 1/q for q = 0.8. Each wrong option applies one convention's scaling twice, or applies the training mask at evaluation.

### Limit of the approximation

"Evaluation disables the random dropout mask. Match each activation's expected scale. A nonlinear network output need not equal its full mask-averaged prediction" ([[Block 7 Slides]], p. 150). Synthesis: the scaling rule is exact for the expected input to one linear unit, as in the two-input example. After nonlinear layers, the scaled network only approximates the integral on p. 145.

### Evaluation rule and use

At evaluation, "turn off the random mask; apply the chosen scaling convention" ([[Block 7 Slides]], p. 165). The slides advise to use dropout and early stopping "when they fit the architecture and validation protocol" ([[Block 7 Slides]], p. 170). See the evaluation rule and the diagnosis table in [[Regularization]], and [[Switch the Model to Evaluation Mode When Evaluating]].

## Related

- [[Regularization]]
- [[Batch Normalization]]
- [[Data Augmentation]]
- [[Early Stopping]]
- [[Overfitting and Underfitting]]
- [[Neural Networks]]
- [[Activation Functions]]
- [[Switch the Model to Evaluation Mode When Evaluating]]: evaluation mode turns the mask off

## Sources

- [[Block 7 Slides]], pp. 140–153, 165, 170
- [[F26-midterm-review-234p]], pp. 128–133
