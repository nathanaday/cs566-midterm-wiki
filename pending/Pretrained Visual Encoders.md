---
id: con-cty4pv
type: topic
kind: concept
description: "Reusing an image encoder trained on large data instead of training from scratch: freeze it and train a head, or fine-tune it, measure it with a linear probe, and choose it by its full checkpoint contract."
tags: [machine-learning/cs566-deeplearning]
aliases: [linear probe, linear-probe evaluation, pretrained visual encoder workflow, transfer from a pretrained encoder, frozen vs fine-tuned, model card, checkpoint contract, constraint-first decision map]
created: 2026-09-28T00:00:00
updated: 2026-10-13T18:22:47
refreshed: 2026-10-13T18:22:47
status: stable
sources: ["[[Block 4 Slides]]", "DINOv2 (note)", "[[Block 7 Slides]]"]
up: ["[[Transfer Learning]]"]
---

> [!concept] Concept
> 3 sources · refreshed 2026-10-13 · #machine-learning/cs566-deeplearning
> Up: [[Transfer Learning]]

## Definition

A pretrained visual encoder is an image model trained on large data and reused as a component for a new task. The slides say a common workflow starts from a pretrained visual encoder, not random initialization ([[Block 4 Slides]], p. 230). A linear probe measures how good its frozen features are ([[Block 4 Slides]], p. 262). The general method is [[Transfer Learning]].

## Explanation

### Freeze or fine-tune

- Freeze the encoder and train a head when labels or compute are scarce. Fine-tune when a task shift justifies it ([[Block 4 Slides]], p. 230).
- If pretrained encoders fit the task and license, compare the frozen and fine-tuned paths ([[Block 4 Slides]], p. 232).
- Block 7 makes the same point. It calls a frozen backbone with a new head "A low-cost baseline for the new labels." It says to compare that baseline with partial and full fine-tuning "using the same validation protocol" ([[Block 7 Slides]], p. 210). See [[Transfer Learning]] and [[Fine-Tuning]].
- Reuse can fail when the domain changes. "A model trained on everyday photos may miss specialized visual features." Microscopy or unusual sensors may need different representations. "Check target-domain performance before trusting reuse." ([[Block 7 Slides]], p. 215)
- Evidence: DINOv2 tests frozen features on global and dense tasks, and the 2025 DINOv3 report releases ViT and ConvNeXt encoders ([[Block 4 Slides]], p. 230). The DINOv2 note says its features transfer to classification, segmentation, and depth estimation with only a linear probe on a frozen backbone (DINOv2 (note), § Summary).
- The course covers self-supervised objectives in week 11. This lecture treats the encoder as a component ([[Block 4 Slides]], p. 230).

### Linear probe

A linear probe is a logistic regression classifier on the image features of a frozen encoder, trained with L-BFGS ([[Block 4 Slides]], p. 262). It has only one hyperparameter and allows "fair" comparisons with other vision models ([[Block 4 Slides]], p. 262). It is a frozen-feature baseline, and the slide notes that fine-tuning can perform worse ([[Block 4 Slides]], p. 262). The CLIP evaluation ran linear probes on 27 image datasets x 65 vision models, including satellite images, car models, medical images, city classification, rendered texts, aircraft, birds, and memes ([[Block 4 Slides]], p. 262). [[CLIP]] lists the results.

Block 7 gives the same tool as a transfer choice. With very little data from a very similar dataset, "Use Linear Classifier on top layer". With very little data from a very different dataset, "Try linear classifier from different stages" ([[Block 7 Slides]], pp. 203-204).

Synthesis: a linear probe is a [[Linear Classification|linear classifier]] on fixed features. Only the head learns, so the score measures the features and not the fine-tuning recipe.

### Choosing an encoder

The slides treat the choice as more than a model name. "The checkpoint, data, license, and adaptation plan are part of the choice." ([[Block 4 Slides]], p. 230)

- **Model cards.** Start from maintained weight APIs and model cards, not a static screenshot. Architecture, checkpoint, preprocessing, input size, license, data disclosure, and evaluation protocol belong together. "A model name without its checkpoint contract is incomplete." ([[Block 4 Slides]], p. 231)
- **Tools.** TorchVision bundles weights, transforms, and metadata. timm and Hugging Face expose model cards and encoders. TorchServe is archived and is not a 2026 model-selection map ([[Block 4 Slides]], p. 231).

The slides give a constraint-first decision map ([[Block 4 Slides]], p. 232):

| Situation | Experiment |
|---|---|
| Scratch: enough labels and compute | Compare a modern ConvNet with ViT or Swin under matched protocols and budgets |
| Transfer: pretrained encoders fit the task and license | Compare frozen and fine-tuned paths |
| Edge | Measure latency and memory on the actual device; keep parameters and FLOPs as diagnostics |

"There is no universal default; the constraint set selects the experiment." ([[Block 4 Slides]], p. 232)

### Reporting rules

The slides state these as rules for any reported vision result:

- **Report the setup.** State data, checkpoint, resolution, precision, hardware, runtime, and metric ([[Block 4 Slides]], p. 232).
- **Counts are budgets.** "Counts are budgets, not accuracy or latency guarantees." Fewer MACs may not run faster, because kernels, memory bandwidth, and hardware decide speed. At matched parameters, factorization often costs some accuracy ([[Block 4 Slides]], p. 226).
- **ImageNet numbers.** "Cite the year, the split, and the training data alongside the dataset name." Reported ImageNet numbers now differ in pretraining data, resolution, and augmentation ([[Block 4 Slides]], p. 228).

## Related

- [[Transfer Learning]]
- [[Fine-Tuning]]
- [[Vision Transformer (ViT)]]
- [[CLIP]]
- [[Linear Classification]]
- [[Convolutional Neural Networks (CNN)]]
- [[Visual Anomaly Detection]]
- [[Model Evaluation]]

## Sources

- [[Block 4 Slides]], pp. 226, 228, 230-232, 262
- DINOv2 (note) (pre-reading summary, not the paper)
- [[Block 7 Slides]], pp. 203-204, 210, 215
