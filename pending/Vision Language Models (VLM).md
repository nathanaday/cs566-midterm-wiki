---
id: con-2kwmq8
type: topic
kind: concept
description: Models that connect a vision encoder to a language model so the language model can read visual tokens and answer in free text, traced here from ViT and CLIP through BLIP-2, LLaVA, edge models, and agentic vision.
tags: [machine-learning]
aliases: [VLM, multimodal LLM, visual instruction tuning, LLaVA-style vision-language model]
created: 2026-09-28T00:00:00
updated: 2026-09-28T00:00:00
refreshed: 2026-09-28T00:00:00
status: stable
sources: ["An Image is Worth 16x16 Words (note)", "CLIP (note)", "BLIP-2 (note)", "Visual Instruction Tuning (note)", "LLaVA-OneVision (note)", "FastVLM (note)", "SmolVLM (note)", "WinCLIP (note)", "Fall 2026 Reading List", "Learning Goals", "[[Block 4 Slides]]"]
---

> [!concept] Concept
> 11 sources · refreshed 2026-09-28 · #machine-learning

## Definition

A VLM connects a vision encoder to a language model so that the language model can read visual tokens. No source in the vault defines the term. This page is a synthesis of eight paper notes and the CSCI 566 Block 4 slides.

## Explanation

The owner wants to analyze sensor data, including images and video, and to do multimodal perception on edge systems (Learning Goals). The CLIP note says any class that you can describe in words becomes a zero-shot class (CLIP (note)).

### Lineage in the vault

1. **ViT:** an image becomes a sequence of patch tokens (An Image is Worth 16x16 Words (note)). See [[Vision Transformer (ViT)]].
2. **CLIP:** a [[Contrastive Learning|contrastive]] image-text embedding space trained on 400M image-text pairs; classification is a nearest-text lookup (CLIP (note)). See [[CLIP]].
3. **BLIP-2:** a Q-Former with a fixed set of learned queries connects a frozen image encoder to a frozen language model (BLIP-2 (note)).
4. **LLaVA:** one linear layer projects CLIP features into the language model's token embedding space. The language model is the trunk and the vision encoder is an adapter (Visual Instruction Tuning (note)).
5. **LLaVA-OneVision:** one model and one training recipe for single images, multiple images, and video; the common baseline that edge VLM papers compare against (LLaVA-OneVision (note)).
6. **FastVLM and SmolVLM:** edge models that cut [[Visual Token Count|visual token count]] (FastVLM (note), SmolVLM (note)).
7. **WinCLIP:** CLIP applied to industrial anomaly detection (WinCLIP (note)).

### Matching versus generation

A matching model such as CLIP can only select and rank the text candidates that you supply, for example "a cat", "a dog", "a bicycle". Generation needs a language interface ([[Block 4 Slides]], pp. 274-275). In the visual instruction tuning design, a vision encoder and a learned projector feed an LLM. The LLM then answers a question such as "What color are its eyes?" with "Its eyes are green." ([[Block 4 Slides]], p. 275). The slides cite Liu et al. (NeurIPS 2023), Visual Instruction Tuning ([[Block 4 Slides]], pp. 274-275).

### Design question: how visual tokens reach the language model

The reading list states the question: how do you get visual tokens into a language model without retraining either side? (Fall 2026 Reading List, item 5)

- **Fixed queries (BLIP-2).** Token count does not depend on image resolution. Training runs in two stages and updates only the Q-Former (BLIP-2 (note)).
- **Projection (LLaVA).** A simpler and cheaper recipe. Most open VLMs that you can deploy today still follow it. The LLaVA note says the data recipe carries more of the result than the architecture does (Visual Instruction Tuning (note)).

The BLIP-2 note asks why the field mostly chose the simpler design (BLIP-2 (note)). No source in the vault answers this.

### Agentic vision: act, then observe

The slides credit this example to Google, Agentic Vision (Jan 2026) ([[Block 4 Slides]], pp. 280-283). A visual agent inspects image regions step by step before it answers. See [[Agent Loop]].

1. **Observe.** To answer "What is the printed serial number?" on a photo of a meter, the agent must first find the label and decide which region to inspect next ([[Block 4 Slides]], p. 280).
2. **Act.** It crops the serial-number region from the original-resolution image ([[Block 4 Slides]], p. 281).
3. **Observe again.** It reads the crop and answers 916076 ([[Block 4 Slides]], p. 282).

The slide titles give the rule: choose the region before you read its digits, and observe the crop before you answer ([[Block 4 Slides]], pp. 281-282).

**Why the crop helps.** The encoder input size is fixed, so a crop gives more input pixels to a small detail, but the model sees less context. In the slides' example the source is 1792 x 1792 pixels and a printed digit is 16 px tall. Resizing the whole image to 224 x 224 divides by 8, so the digit becomes 2 px. Resizing a 448 x 448 crop to 224 x 224 divides by 2, so the digit becomes 8 px. The crop must come from the original-resolution image ([[Block 4 Slides]], p. 284). The slides call this teaching geometry, not an OCR result or a specific model pipeline ([[Block 4 Slides]], pp. 284-285).

**When the crop fails.** A crop gives useful evidence only when it covers the region the question asks about. A crop of the meter's partly hidden LCD display is the wrong region, because the LCD reading is not the printed serial number ([[Block 4 Slides]], p. 283). More pixels cannot fix occlusion or a wrong choice of region ([[Block 4 Slides]], p. 285).

## Related

- [[CLIP]]
- [[Vision Transformer (ViT)]]
- [[Visual Token Count]]
- [[Visual Anomaly Detection]]
- [[Vision Language Action Models]]
- [[Transformers]]
- [[Contrastive Learning]]
- [[Agent Loop]]
- [[ReAct]]

## Sources

- An Image is Worth 16x16 Words (note)
- CLIP (note)
- BLIP-2 (note)
- Visual Instruction Tuning (note)
- LLaVA-OneVision (note)
- FastVLM (note)
- SmolVLM (note)
- WinCLIP (note)
- Fall 2026 Reading List, item 5
- Learning Goals
- [[Block 4 Slides]], pp. 274-285
