---
id: ent-f4phf9
type: topic
kind: entity
description: A Transformer for images (Dosovitskiy et al.) that cuts an image into fixed-size patches and projects each patch with one shared linear map into a token, so token count grows with image area.
tags: [machine-learning]
aliases: [ViT, Vision Transformer, vision transformers, ViT patch embedding, patch tokenization]
created: 2026-09-28T00:00:00
updated: 2026-09-28T00:00:00
refreshed: 2026-09-28T00:00:00
status: stable
sources: ["[[Block 4 Slides]]", "An Image is Worth 16x16 Words (note)"]
---

> [!entity] Entity
> 2 sources · refreshed 2026-09-28 · #machine-learning

## What it is

The Vision Transformer (ViT) is a [[Transformers|Transformer]] model for images. The slides cite it as Dosovitskiy et al., ICLR 2021 ([[Block 4 Slides]], pp. 131, 233-235). The pre-reading note dates the paper 2020 (An Image is Worth 16x16 Words (note), § Summary). ViT cuts an image into fixed-size patches, embeds each patch as a token, and feeds the sequence to a standard Transformer encoder with no convolutions (An Image is Worth 16x16 Words (note), § Summary).

## Facts

### Patch embedding

- A 224x224 image with 16x16 patches becomes a 14x14 grid of 196 patch tokens. The count excludes the class token ([[Block 4 Slides]], p. 233).
- Each 16x16 RGB patch flattens to 768 numbers. One shared linear map projects it to D features, with the same weights at every spatial location ([[Block 4 Slides]], p. 234).
- A 448x448 image gives 28x28 = 784 patches. Doubling each side gives 4x the patch tokens ([[Block 4 Slides]], p. 235).

Synthesis: token count grows with pixel area, not side length. The note says patch size sets token count, and token count sets cost and latency (An Image is Worth 16x16 Words (note), § Summary). See [[Visual Token Count]].

### Aspect ratio

A center square crop throws image content away. The slides cite SigLIP 2 (Tschannen et al., 2025) for keeping the full aspect ratio instead ([[Block 4 Slides]], p. 276). With 16-px patches, a 256x256 image gives a 16x16 grid and a 128x512 image gives an 8x32 grid. Both use 256 tokens: the same token budget with a different grid shape ([[Block 4 Slides]], p. 277).

### Scale

Vision transformers match or beat convolutional layers at large pretraining scale ([[Block 4 Slides]], p. 131). The note says the inductive bias of convolution helps at small scale but is optional at large scale (An Image is Worth 16x16 Words (note), § Summary). See [[Convolutional Neural Networks (CNN)]].

### As an encoder

- [[CLIP]] offers a ViT-based image encoder ([[Block 4 Slides]], pp. 257, 260).
- The 2025 DINOv3 report releases ViT and ConvNeXt encoders ([[Block 4 Slides]], p. 230). DINOv2 is a ViT trained by self-distillation (DINOv2 (note), § Summary).
- With enough labels and compute, the slides say to compare a modern ConvNet with ViT or Swin under matched protocols and budgets ([[Block 4 Slides]], p. 232). See [[Pretrained Visual Encoders]].

## Related

- [[Transformers]]
- [[Convolutional Neural Networks (CNN)]]
- [[Visual Token Count]]
- [[Vision Language Models (VLM)]]
- [[CLIP]]
- [[Pretrained Visual Encoders]]

## Sources

- [[Block 4 Slides]], pp. 131, 230, 232-235, 257, 260, 276-277
- An Image is Worth 16x16 Words (note) (pre-reading summary, not the paper)
- DINOv2 (note)
