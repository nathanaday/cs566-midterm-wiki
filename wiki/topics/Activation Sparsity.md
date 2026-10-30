---
description: The share of units in a layer that output exactly zero for an input, high in ReLU models, which sparsity-aware kernels can use to cut LLM inference compute.
aliases: [Sparse Activation, ReLU Strikes Back]
sources: ["[[Block 3 Slides]]"]
---

## Definition

Activation sparsity is the share of units in a layer that output exactly 0 for an input. ReLU outputs 0 for any negative input, "leading to a portion of neurons in the network not activating" ([[Block 3 Slides]], p. 262). A chart on p. 83 shows activation sparsity by layer: OPT 6.7B (ReLU) stays near 90-100%, while Llama 7B (SiLU) and Falcon 7B (GELU) stay near 0%. The caption says "ReLU-based OPTs show significantly higher sparsity" (p. 83).

## Explanation

### Why it matters

LLMs have "huge inference costs (compute + memory)". GELU and SiLU "improve convergence but increase computation", and "ReLU was largely replaced, despite its benefits in activation sparsity" (p. 83).

The slides list the gains from higher sparsity (p. 86):

- Fewer computations, but skipping that work "needs sparsity-aware kernels".
- Less data movement, with savings that "depend on the sparsity pattern".
- It works in existing transformer architectures with minimal changes.
- "Fewer FLOPs per token → faster with matching kernels."

### The "ReLU Strikes Back" paper

The slides present Mirzadeh et al., "ReLU Strikes Back: Exploiting Activation Sparsity in Large Language Models", ICLR 2024 (Apple) (p. 79). The vault has the slides' summary only, not the paper.

- **Challenge:** "Can we bring back ReLU to improve LLM efficiency without losing performance?" (p. 83).
- **Proposals:** reintroduce ReLU in LLMs; "relufication", which converts pretrained LLMs such as Llama and Falcon to ReLU; use ReLU sparsity to speed up speculative decoding; and "shifted ReLU", which improves sparsity further with simple changes (p. 84).
- **Findings:** replacing GELU or SiLU with ReLU "costs little accuracy in their results", and ReLU-based models "require up to 3× fewer inference FLOPs in the models they test" (p. 85). After relufication, activation sparsity of Falcon 7B and Llama 7B "improves significantly" (p. 86).

For why transformers adopted GELU, see [[Activation Functions]].

## Related

- [[Activation Functions]]
- [[Dying ReLU]]
- [[Transformers]]

## Sources

- [[Block 3 Slides]], pp. 79-86, 262
