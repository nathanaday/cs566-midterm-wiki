---
id: doc-bbkhmz
type: topic
kind: concept
description: Fine-tuning trains a model on source data and then uses training examples and a loss on the target data to update selected pretrained parameters; partial fine-tuning adapts some layers, full fine-tuning can change every weight, and about 1/10 of the original learning rate is a good starting point.
tags: [machine-learning/cs566-deeplearning]
aliases: [finetuning, fine-tune, model fine-tuning, partial fine-tuning, full fine-tuning, FT, Stage 2 transfer, Lower learning rate for fine-tuning]
created: 2026-10-12T16:58:10
updated: 2026-10-19T17:48:15
refreshed: 2026-10-19T17:48:15
status: stable
sources: ["[[Block 7 Slides]]", "[[F26-midterm-review-234p]]"]
up: ["[[Transfer Learning]]"]
---

> [!concept] Concept
> 2 sources · refreshed 2026-10-19 · #machine-learning/cs566-deeplearning
> Up: [[Transfer Learning]]

## Definition

Fine-tuning updates the parameters of a pretrained model for a target task. The deck defines it as follows: "Use training examples and loss to update selected parameters before later inference." ([[Block 7 Slides]], p. 229) The idea is to train a model on the source data, then fine-tune the model on the target data ([[Block 7 Slides]], p. 212). "Fine-tuning changes selected pretrained parameters." ([[Block 7 Slides]], p. 201; repeated in [[F26-midterm-review-234p]], p. 144)

In the [[Transfer Learning]] overview, fine-tuning is in the cell where both the source data and the target data have labels ([[Block 7 Slides]], pp. 211, 214).

## Explanation

### The task

- Source data (x^s, y^s): a large amount. Target data (x^t, y^t): very little ([[Block 7 Slides]], p. 212). A note on the slide says: "Few-shot: a few examples. One-shot: one per class/task."
- Example: supervised speaker adaptation. The source data is audio and transcriptions from many speakers. The target data is audio and transcriptions from one specific user ([[Block 7 Slides]], p. 212).
- Challenge: the target data is limited, "so be careful about overfitting" ([[Block 7 Slides]], p. 212). See [[Overfitting and Underfitting]].

### Stage 2: adapt some of the backbone

Stage 1 of [[Transfer Learning]] keeps the pretrained backbone fixed and trains a new head ([[Block 7 Slides]], p. 194). "If the fixed features are insufficient, unfreeze selected layers." In Stage 2 the early features stay frozen, and the later features and the classifier train ([[Block 7 Slides]], p. 201). [[F26-midterm-review-234p]] repeats both slides (pp. 142, 144).

### Partial and full fine-tuning

| Option | Slide description |
|---|---|
| Partial fine-tuning | "Adapt some features while keeping others fixed." |
| Full fine-tuning | "More flexibility, with greater training cost." |

Source: [[Block 7 Slides]], p. 210. The slide says to compare these two options and the frozen-backbone baseline "using the same validation protocol" ([[Block 7 Slides]], p. 210).

- "Full fine-tuning can change every entry of W." ([[Block 7 Slides]], p. 250) Each selected weight can change independently ([[Block 7 Slides]], p. 260). In [[LoRA]], the change must be expressible as B × A with the chosen rank. "More capacity does not guarantee better accuracy." ([[Block 7 Slides]], p. 260)
- "Full fine-tuning stores more than the pretrained weights." Training also holds gradients and optimizer state (values used to update trainable parameters) and activations (intermediate values needed for backpropagation). "Fewer trainable parameters can reduce training-state cost." ([[Block 7 Slides]], p. 235) This cost is the reason for Parameter-Efficient Fine-Tuning.
- The deck shows GPT-3 validation accuracy. Fine-tuned: 89.5% on MNLI-m and 85.4% on RTE. Few-shot: 40.6% and 69.0% ([[Block 7 Slides]], p. 256). The same slide asks "Can useful adaptation fit inside a small update space?" and gives the hypothesis "Small update spaces can suffice on some tasks." ([[Block 7 Slides]], p. 256)

### Learning rate

"Lower learning rate when finetuning; 1/10 of original LR is good starting point." ([[Block 7 Slides]], p. 200) The slide puts this note in the bigger-dataset case of the CNN recipe. In that case the top FC layers train and the convolutional layers stay frozen ([[Block 7 Slides]], p. 200). [[F26-midterm-review-234p]] repeats this slide (p. 143).

Synthesis: a smaller step size keeps the pretrained weights near their starting values, so the update does not erase what the source data taught. The slide gives 1/10 as a starting point, not as a fixed rule. See Learning Rate Schedules.

### How many layers to fine-tune

- "With bigger dataset, train more layers." ([[Block 7 Slides]], p. 200; [[F26-midterm-review-234p]], p. 143)
- With quite a lot of data, fine-tune a few layers if the dataset is very similar to the source. Fine-tune a larger number of layers if it is very different ([[Block 7 Slides]], p. 204).
- In layer transfer, fine-tune the whole network only if there is sufficient data ([[Block 7 Slides]], p. 213).

### Fine-tuning a language model

The deck moves the running example from flower photos to the sentiment of flower-shop reviews. The input "The flowers arrived fresh." has the label Positive. A pretrained Transformer supplies the text representations ([[Block 7 Slides]], p. 228). Fine-tuning uses the same supervised loop as for the flower photos: review + label, then loss and backpropagation, then an update of selected model parameters. "The learned adaptation is stored in the updated parameters." ([[Block 7 Slides]], p. 230)

In-Context Learning is the alternative. It puts examples in the input prompt, and the usual inference call keeps the model parameters fixed ([[Block 7 Slides]], p. 229). The slide's advice: "Ask where the adaptation is stored." ([[Block 7 Slides]], p. 229) See Updating LLMs.

### Terminology

The deck uses "fine-tune" for different amounts of training. The bigger-dataset case trains only the FC layers ([[Block 7 Slides]], p. 200). The size-and-similarity guide says "Finetune a few layers" ([[Block 7 Slides]], p. 203). The options slide separates partial and full fine-tuning ([[Block 7 Slides]], p. 210). The overview slide warns of "different terminology in different literature" ([[Block 7 Slides]], p. 211). This topic uses "fine-tuning" for any update of pretrained parameters, and says partial or full where the difference matters.

## Related

- [[Transfer Learning]]
- Parameter-Efficient Fine-Tuning
- [[LoRA]]
- In-Context Learning
- Updating LLMs
- Pretrained Visual Encoders
- Multitask Learning
- Domain-Adversarial Training
- [[Overfitting and Underfitting]]
- Learning Rate Schedules
- [[Convolutional Neural Networks (CNN)]]

## Sources

- [[Block 7 Slides]], pp. 194, 200-201, 203-204, 210-214, 228-230, 235, 250, 256, 260
- [[F26-midterm-review-234p]], pp. 142-144
