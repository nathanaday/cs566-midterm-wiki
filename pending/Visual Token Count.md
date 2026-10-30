---
id: con-8w43p4
type: topic
kind: concept
description: The number of tokens a vision encoder passes to the language model for one image or frame; the main cost and latency driver for edge vision language models.
tags: [machine-learning]
aliases: [visual tokens, visual token budget]
created: 2026-09-28T00:00:00
updated: 2026-09-28T00:00:00
refreshed: 2026-09-28T00:00:00
status: stable
sources: ["Fall 2026 Reading List", "An Image is Worth 16x16 Words (note)", "BLIP-2 (note)", "LLaVA-OneVision (note)", "FastVLM (note)", "SmolVLM (note)", "Learning Goals"]
---

> [!concept] Concept
> 7 sources · refreshed 2026-09-28 · #machine-learning

## Definition

Visual token count is the number of tokens that a vision encoder gives to the language model for one image or frame. This vault uses the term for an idea that recurs across several paper notes. No single source defines it.

## Explanation

The reading list says that the real constraint on edge multimodal work is visual token count, not parameter count (Fall 2026 Reading List, item 12). The paper notes support this in different ways:

- Patch size sets token count, and token count sets cost and latency (An Image is Worth 16x16 Words (note)).
- Time-to-first-token is mostly encoder latency plus prefill over the visual tokens, so cutting token count saves more than shrinking the language model (FastVLM (note)).
- High-resolution image handling sets token count, and therefore latency (LLaVA-OneVision (note)).
- Compact models save through aggressive visual token compression, not through a smaller language model alone (SmolVLM (note)).

### Ways to reduce it

| Method | Effect described | Source |
|---|---|---|
| Patch size | Patch size sets tokens per image | An Image is Worth 16x16 Words (note) |
| Fixed learned queries (Q-Former) | Token count does not depend on image resolution | BLIP-2 (note) |
| Hybrid convolution-transformer encoder (FastViTHD) | Far fewer tokens at high resolution | FastVLM (note) |
| Pixel shuffle compression | Aggressive token compression in models from about 250M to 2B parameters | SmolVLM (note) |

The SmolVLM note adds that the encoder-to-language-model size ratio should shift as the total budget shrinks, instead of shrinking both parts evenly (SmolVLM (note)).

The owner's interest in multimodal perception on edge systems is the reason this topic matters here (Learning Goals).

### Open questions

- The notes give no latency numbers. The FastVLM note names the latency breakdown table (encoder versus prefill share of time-to-first-token at each resolution) as the one to keep (FastVLM (note)).

## Related

- [[Vision Language Models (VLM)]]
- [[Transformers]]
- [[Convolutional Neural Networks (CNN)]]

## Sources

- Fall 2026 Reading List, item 12
- An Image is Worth 16x16 Words (note)
- BLIP-2 (note)
- LLaVA-OneVision (note)
- FastVLM (note)
- SmolVLM (note)
- Learning Goals
