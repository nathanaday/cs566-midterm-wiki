---
description: Adapters are small bottleneck feed-forward layers with a residual connection, inserted into a frozen pretrained network so that only their parameters are fine-tuned.
aliases: [Adapter, Adapter Layer, Adapter Module, Adapter Modules]
sources: ["[[Block 7 Slides]]"]
---

> [!concept] Concept
> 1 source · refreshed 2026-10-13 · #machine-learning/cs566-deeplearning
> Up: [[Parameter-Efficient Fine-Tuning]]

## Definition

Adapters are a [[Parameter-Efficient Fine-Tuning]] approach: "add additional layers that have few parameters and tune only the parameters of those layers, keeping all others fixed" ([[Block 7 Slides]], p. 236). Another slide describes adapter modules as "Add small trainable transformations inside the model" (p. 237).

## Explanation

### Structure

"An adapter layer is simply a feed-forward neural network with one hidden layer, and a residual connection" (p. 243). "For input dimension, d, the adapter layer also has output dimension d, but bottlenecks to a lower dimension r in the middle" (p. 243). The figure, from arXiv:1902.00751, shows this order:

1. Feedforward down-project, W_down ∈ ℝ^(r×d)
2. Nonlinearity
3. Feedforward up-project, W_up ∈ ℝ^(d×r)
4. Add the input through the residual connection. See [[Residual Connections]].

### Adapters in a Transformer

- "In practice, r is chosen s.t. r << d and the adapter layers contain only 0.5% – 8% of the total parameters" (p. 244).
- "When added to a deep neural network (e.g. Transformer) all the other parameters of the pretrained model are kept fixed, and only the adapter layer parameters are fine-tuned" (p. 244).
- The figure puts one adapter after attention and one after the feed-forward network. Each adapter comes before an "add & layer norm" step (p. 244, figure inspired by He et al. (2022), arXiv:2110.04366). See [[Transformers]] and [[Layer Normalization]].
- "Interesting: it works even though the grey modules are kept fixed!" (p. 244)

Training still uses backpropagation through the frozen layers above an adapter: "Frozen means no weight update; gradients can still pass through" (p. 245). See [[Parameter-Efficient Fine-Tuning]] and [[Backpropagation]].

### Results

The slides compare adapters with the baseline "fine-tune only the top K layers" (pp. 246–248, figures from arXiv:1902.00751). The slides state:

- "Adapters achieve nearly the performance (i.e. 0% delta) of full fine-tuning but with substantially fewer parameters"
- "Sometimes adapters even outperform full fine-tuning"

Approximate readings from the charts (x-axis: "Num trainable parameters / task"):

| Chart | Adapters | Fine-tune top layers |
| --- | --- | --- |
| GLUE, BERT-Large, accuracy delta (p. 246) | near 0% from about 2 × 10^5 to about 5 × 10^7 | about −10% at 10^6; near 0% only around 10^8 |
| MNLI-m, BERT-Base, validation accuracy (p. 247) | about 82–84% from about 10^5 to about 2 × 10^7 | about 78% at 10^7, rising to about 84.5% near 10^8 |
| CoLA, BERT-Base, validation accuracy (p. 248) | about 82–83% from about 10^5 to about 2 × 10^7 | about 77% at 10^7, rising to about 82% near 10^8 |

The MNLI-m and CoLA charts also show one point labeled "Layer Norm." below 10^5 parameters, at about 80% and 78%. The deck does not explain this point.

Inconsistencies in the slides, not resolved here:

- On pp. 247–248 the bullets say "Pretrained Model: BERT-Large", but the chart titles say BERT-Base.
- The charts compare adapters with top-layer fine-tuning, not with a curve labeled full fine-tuning. On MNLI-m the top-layer curve ends slightly above the adapter curve. The charts do not show the claim that adapters "sometimes" beat full fine-tuning directly.

### Adapters versus LoRA

"Adapters and LoRA Modify Different Computations." "Both can keep the pretrained weights frozen during adaptation" (p. 263).

- Adapter: "Insert a small trainable module. Its computation remains in the adapted forward pass."
- [[LoRA]]: "Add B × A to selected weights. For a compatible fixed adapter, merge it into W for inference."

On this slide, "adapter" in the LoRA column means the trained LoRA update, not an adapter module.

Synthesis: an adapter module adds computation at inference, because its layers stay in the forward pass. A merged LoRA update does not. Ignoring biases, one adapter has about 2rd weights: r × d for the down-projection and d × r for the up-projection.

## Related

- [[Parameter-Efficient Fine-Tuning]]
- [[LoRA]]
- [[Fine-Tuning]]
- [[Transformers]]
- [[Residual Connections]]
- [[Backpropagation]]

## Sources

- [[Block 7 Slides]], pp. 236–237, 243–248, 263
