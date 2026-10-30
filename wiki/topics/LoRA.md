---
id: con-m9qcqh
type: topic
kind: concept
description: LoRA (low-rank adaptation) keeps a pretrained weight matrix W frozen and trains a low-rank update ΔW = BA, so the layer computes (W + BA)x.
tags: [machine-learning/cs566-deeplearning]
aliases: [Low-Rank Adaptation, LoRA Updates]
created: 2026-09-28T00:00:00
updated: 2026-10-13T18:22:42
refreshed: 2026-10-13T18:22:42
status: stable
sources: ["[[Block 3 Slides]]", "Sep 14 Lecture Account", "[[Block 7 Slides]]"]
up: ["Updating LLMs", "Parameter-Efficient Fine-Tuning"]
---

> [!concept] Concept
> 3 sources · refreshed 2026-10-13 · #machine-learning/cs566-deeplearning
> Up: Updating LLMs · Parameter-Efficient Fine-Tuning

## Definition

LoRA (low-rank adaptation) is a Parameter-Efficient Fine-Tuning method: "learn a small delta for the each of the parameter matrices with the delta chosen to be low rank" ([[Block 7 Slides]], p. 236). It is one of the four ways in Updating LLMs that the Sep 14 lecture listed (Sep 14 Lecture Account, § Updating LLMs).

Block 3: "Freeze a learned weight matrix W. None of its entries receive an update." "Replace Wx with (W + BA)x, where B and A are small. Only A and B are trained" ([[Block 3 Slides]], p. 217, citing LoRA, ICLR 2022).

Block 7: "For a selected linear layer, keep the pretrained matrix W fixed." "LoRA uses W + ΔW, with ΔW = B × A." "Train A and B. Keep the original W frozen." "The low-rank object is the update ΔW" ([[Block 7 Slides]], p. 250, citing Hu et al., LoRA, ICLR 2022).

$$z = W_0x + BAx = (W_0 + BA)x$$

- $W_0$ is $d \times k$. It does not change.
- $B$ is $d \times r$ and $A$ is $r \times k$, with $r \ll \min(d, k)$.
- Training updates only $A$ and $B$.

(p. 261, figure inspired by He et al. (2022).)

## Explanation

### The frozen and trainable paths

"For a column input x, the layer computes W x + B(A x)." The input goes to the frozen W and, separately, through trainable A and then trainable B. The two outputs add. "Both paths use the same input x" ([[Block 7 Slides]], p. 253).

### A small example

- "W maps 6 input features to 8 output features. Choose rank 2." W is 8 × 6, B is 8 × 2, and A is 2 × 6. "The original W remains intact while B × A changes its output" (p. 251).
- "Full matrix: 8 × 6 = 48 trainable entries." "LoRA: (8 × 2) + (2 × 6) = 28 trainable entries." "The 48 frozen entries of W still need to be stored." "The saving depends on rank and matrix dimensions" (p. 252).

At LLM scale, the deck labels one GPT-3 linear layer as "12k * 12k" (p. 255).

### Rank restricts the update space

- Full fine-tuning: "Each selected weight can change independently." LoRA: "The change must be expressible as B × A with the chosen rank." "More capacity does not guarantee better accuracy" (p. 260).
- "A rank-2 update has fewer degrees of freedom than a full matrix update." A smaller rank gives "Fewer trainable parameters. A more restricted set of changes." A larger rank gives "More trainable parameters. More possible changes to the layer." "Validation decides whether extra capacity helps" (p. 262).
- The deck lists "LoRA rank" with learning rate and weight decay as settings that hyperparameter tuning searches (p. 264). See HyperTuning for the separate method of that name.

Intrinsic-dimension results suggest why a small update space can suffice. See Parameter-Efficient Fine-Tuning (pp. 256–259).

### Initialization

A slide on zero initialization says that the right initial value depends on the parameter's role: "Zero biases can be valid. LoRA also uses a zero factor with a nonzero random factor." "Initialization must account for the parameter's role" (p. 59, citing Hu et al., ICLR 2022). The slide does not say which factor is zero. See [[Weight Initialization]].

Synthesis: if one factor is zero, BA = 0 at the start, so the adapted layer starts as the pretrained layer.

### LoRA versus adapters

"Both can keep the pretrained weights frozen during adaptation" (p. 263).

- [[Adapters]]: "Insert a small trainable module. Its computation remains in the adapted forward pass."
- LoRA: "Add B × A to selected weights. For a compatible fixed adapter, merge it into W for inference."
- "LoRA learns an update rather than factorizing the original W" (p. 263).

Here "adapter" means the trained LoRA update, not an adapter module.

### Training cost

- "Backprop follows paths from the loss to A and B, including intervening frozen layers" ([[Block 3 Slides]], p. 217). See [[Backpropagation]].
- "Fewer trainable weights shrink the optimizer state, but activation memory can stay large" (p. 217).
- "LoRA (ICLR 2022) narrows what you update. The backward pass runs either way" (p. 217).
- Block 7 says the same of PEFT in general: it "reduces parameter updates but still requires full backpropagation" ([[Block 7 Slides]], p. 266).

### Background and synthesis

General background, not from a course source:

- Example: for $d = k = 4096$ and $r = 8$, $W$ has 16,777,216 entries. $A$ and $B$ together have $8 \cdot (4096 + 4096) =$ 65,536 entries, about 0.4% of $W$.
- Hu et al. introduced LoRA in 2021 (arXiv:2106.09685). The slides cite the ICLR 2022 version.

Synthesis:

- The update lasts, as in Post-Training, but training changes far fewer parameters.
- One base model can keep a separate LoRA update for each task and swap them.
- After a merge into W (p. 263), inference does no extra computation for the update.

## Related

- Parameter-Efficient Fine-Tuning
- [[Adapters]]
- [[Fine-Tuning]]
- HyperTuning: generates LoRA parameters from task demonstrations
- [[Weight Initialization]]
- Updating LLMs
- Post-Training
- Test-Time Training: can train a LoRA adapter on each test input
- [[Backpropagation]]
- [[Gradient Descent]]

## Sources

- [[Block 3 Slides]], p. 217
- Sep 14 Lecture Account, § Updating LLMs
- [[Block 7 Slides]], pp. 59, 236–237, 250–253, 255, 260–264, 266
- The size example, the history, and the synthesis are general background, not from a course source.
