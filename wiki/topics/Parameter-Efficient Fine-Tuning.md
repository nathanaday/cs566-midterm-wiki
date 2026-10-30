---
id: doc-kjjcpr
type: topic
kind: concept
description: Parameter-efficient fine-tuning (PEFT) adapts a pretrained model by training a small set of parameters (a top-layer subset, adapters, a prefix, or a low-rank update) while the other parameters stay frozen.
tags: [machine-learning/cs566-deeplearning]
aliases: [PEFT, Parameter Efficient Fine-Tuning, Prefix Tuning, Top-K Layer Fine-Tuning, Subset Fine-Tuning, Intrinsic Dimension, Intrinsic Dimensionality]
created: 2026-10-12T16:58:10
updated: 2026-10-13T18:22:47
refreshed: 2026-10-13T18:22:47
status: stable
sources: ["[[Block 7 Slides]]", "[[Block 3 Slides]]"]
up: ["[[Fine-Tuning]]"]
---

> [!concept] Concept
> 2 sources · refreshed 2026-10-13 · #machine-learning/cs566-deeplearning
> Up: [[Fine-Tuning]]

## Definition

Parameter-efficient fine-tuning (PEFT) adapts a pretrained model by training a small set of parameters. The other parameters stay frozen. The Block 7 deck states the goal: "perform fine-tuning of fewer parameters, but achieve performance on a downstream task that is comparable to fine-tuning of all parameters" ([[Block 7 Slides]], p. 236).

The deck shows a figure from the HyperTuning paper (Phang et al., ICML 2023) that draws the contrast (p. 266):

- Fine-tuning: "all model parameters are updated".
- PEFT: "all model parameters are frozen (blue) and only a small number of parameters, φ, are updated".

See [[Fine-Tuning]] for full fine-tuning.

## Explanation

### Four approaches

The deck lists four approaches (p. 236):

| Approach | What is trained, per the slide |
| --- | --- |
| Subset | "Pick a subset of the parameters and fine-tune only those (e.g. only the top K layers of a K+L layer deep neural network)" |
| [[Adapters]] | "add additional layers that have few parameters and tune only the parameters of those layers, keeping all others fixed" |
| Prefix tuning | "for a Transformer LM, pretend as if there exist many tokens that came before your sequence and tune the keys/values corresponding to those tokens" |
| [[LoRA]] | "learn a small delta for the each of the parameter matrices with the delta chosen to be low rank" |

A second slide names three places to put trainable parameters. It says "Keep the same pretrained model as the reference" (p. 237):

- New head: "Learn a new output mapping."
- Adapter modules: "Add small trainable transformations inside the model."
- LoRA updates: "Learn low-rank updates to selected weight matrices."

"Choose the trainable part explicitly" (p. 237).

### Baseline: fine-tune the top layers only

The deck calls this the "Simple baseline for PEFT" (p. 238):

- "keep all parameters fixed except for the top K layers"
- "gradients only need to flow through K layers instead of K+L total layers"
- "reduced memory usage b/c we don't need to store the adjoints (gradient of the loss with respect to each parameter) for the full computation graph"
- It "Can easily be applied to most deep neural networks".

The figure draws a line under the top Transformer layer: "stop gradient here s.t. error does not backprop to lower layers" (p. 238).

Why it can work: "Pretraining may already provide useful features for the new task" (p. 239).

| Part | Role (p. 239) |
| --- | --- |
| Frozen lower layers | "Still compute features in the forward pass." |
| Trainable upper layers | "Learn a new mapping from those features to the target labels." |
| Gradient boundary | "Backward can stop below all trainable layers in this arrangement." |

"Check whether this restricted update is sufficient on validation data" (p. 239). In the adapter results, this baseline needs far more trainable parameters than adapters to reach similar accuracy (pp. 246–248; see [[Adapters]]).

### Prefix tuning

The deck defines prefix tuning only in the table above (p. 236). It gives no figure or result for it.

### Frozen weights can pass gradients

"A frozen layer can sit between a trainable adapter and the loss." The loss gradient passes as a derivative through the frozen output layer F and updates the trainable adapter A. "Frozen means no weight update; gradients can still pass through" ([[Block 7 Slides]], p. 245). Block 3 makes the same point for LoRA: "Backprop follows paths from the loss to A and B, including intervening frozen layers" ([[Block 3 Slides]], p. 217). See [[Backpropagation]].

### What PEFT saves and what it does not

- Top-K fine-tuning does not store the adjoints for the full computation graph ([[Block 7 Slides]], p. 238).
- LoRA trains fewer entries, but "The 48 frozen entries of W still need to be stored" in the 8 × 6 example (p. 252).
- "Fewer trainable weights shrink the optimizer state, but activation memory can stay large" ([[Block 3 Slides]], p. 217).
- "Fine-tuning LLMs is expensive and memory-intensive." "Parameter-efficient fine-tuning (PEFT) reduces parameter updates but still requires full backpropagation" ([[Block 7 Slides]], p. 266). HyperTuning starts from this limit.

Synthesis: the deck makes two statements about the backward pass, and they apply to different layouts. When all trainable parameters sit at the top, the backward pass can stop below them (p. 239). When trainable parameters sit inside lower layers, as adapters and LoRA can, the backward pass must run through the frozen layers above them (p. 245). The deck does not reconcile "still requires full backpropagation" (p. 266) with the top-K slide.

### Why a small update space can suffice

The deck shows GPT-3 results to motivate fine-tuning (p. 256):

| Method | MNLI-m (Val. Acc./%) | RTE (Val. Acc./%) |
| --- | --- | --- |
| GPT-3 Few-Shot | 40.6 | 69.0 |
| GPT-3 Fine-Tuned | 89.5 | 85.4 |

Fine-tuning helps, but the models are large. Llama 3.1 has 405 billion parameters (p. 254). The deck labels one GPT-3 linear layer as "12k * 12k" (p. 255). Question: "Can useful adaptation fit inside a small update space?" Hypothesis: "Small update spaces can suffice on some tasks" (p. 256).

**Intrinsic dimension.** Motivation: "Maybe the number of parameters in a model is not a great measure of how many degrees of freedom are needed to successfully learn some problem" (p. 257). The definition from Li et al. (2018), arXiv:1804.08838 (p. 257):

- "Learn a neural network with D parameters in a random lower dimensional subspace, d"
- "Then repeat, gradually increasing the dimensionality, d"
- "Let the intrinsic dimension be the value of d when good solutions (above 90% threshold of full parameterization) start to appear"

"For MNIST digit recognition, original neural network has D=199,210 parameters but the intrinsic dimension is only d=750" (p. 257).

To train in a random subspace, θ^(D) = θ0^(D) + Pθ^(d). P is a randomly generated D × d projection matrix. θ0^(D) and P are random and frozen, "so the system has only d degrees of freedom". θ^(d) starts as a vector of all zeros, so at the start θ^(D) = θ0^(D) (p. 258, from Li et al.). For a two-layer MLP, θ^(D) = concat(flatten(W1), flatten(W2)) (p. 258).

Aghajanyan et al. (2020), arXiv:2012.13255, "estimate the update dimension needed for a task". d90 is the number of "directions needed to reach 90% of full fine-tuning performance" (p. 259). Their Table 1 gives the estimated d90 (p. 259):

| Model | SAID MRPC | SAID QQP | DID MRPC | DID QQP |
| --- | --- | --- | --- | --- |
| BERT-Base | 1608 | 8030 | 1861 | 9295 |
| BERT-Large | 1037 | 1200 | 2493 | 1389 |
| RoBERTa-Base | 896 | 896 | 1000 | 1389 |
| RoBERTa-Large | 207 | 774 | 322 | 774 |

BERT-Base has 110 million parameters, and BERT-Large has 340 million (p. 259). The deck names SAID and DID as two methods but does not explain them.

Note: the two slides use different reference points for "90%". The Li et al. definition uses "full parameterization" (p. 257). The d90 slide uses "full fine-tuning performance" (p. 259).

Synthesis: the estimates are hundreds or thousands of directions, for models with hundreds of millions of parameters. This supports the hypothesis on p. 256. [[LoRA]] uses the same idea with a fixed rank: "LoRA Restricts the Update Space" (p. 260).

## Related

- [[Fine-Tuning]]: updates all parameters
- [[Transfer Learning]]
- [[LoRA]]
- [[Adapters]]
- HyperTuning: generates PEFT parameters without backpropagation
- [[Backpropagation]]
- Updating LLMs
- [[Transformers]]
- Pretrained Visual Encoders: freeze an encoder and train a head

## Sources

- [[Block 7 Slides]], pp. 236–239, 245–248, 252, 254–260, 266
- [[Block 3 Slides]], p. 217
