---
id: ent-ywvd6c
type: topic
kind: entity
description: "NVIDIA's platform for building world models for physical AI: open world foundation models, mostly video predictors, plus tools for data curation, training, and customization."
tags: [machine-learning, tool]
aliases: [Cosmos, COSMOS]
created: 2026-09-28T00:00:00
updated: 2026-09-28T00:00:00
refreshed: 2026-09-28T00:00:00
status: stable
sources: ["Topic Note - NVIDIA COSMOS", "Guest Lecture 9-21 Notes (part 1)"]
---

> [!entity] Entity
> 2 sources · refreshed 2026-09-28 · #machine-learning · #tool

## What it is

NVIDIA Cosmos is a platform for building custom world models for physical AI. It offers open world foundation models plus tools for data curation, training, and customization. The topic note says the core models are video predictors (Topic Note - NVIDIA COSMOS, § About).

## Facts

### Cosmos 3 and the "3D Omni" model

Two sources describe a two-tower model. Their accounts agree in outline.

| | Topic Note - NVIDIA COSMOS, § Lineage | Guest Lecture 9-21 Notes (part 1), § New Entities |
|---|---|---|
| Name | Cosmos 3 (June 2026), the current generation | "Cosmos 3D Omni Model", a world foundation model |
| Architecture | Two-tower mixture-of-transformers that combines physical reasoning, world generation, and action generation in one open model | Dual tower: an autoregressive VLM and a diffusion model |
| Towers | Reasoner: text and vision in, text out. Generator: text, vision, sound, and action in; vision, sound, and action out | Not named |
| Outputs | Vision, sound, action, and text | Multi-modal: images, video, text, audio, and others |
| Order | The Generator cannot run without the Reasoner; reasoning comes before generation by design | Not stated |

Synthesis: the autoregressive VLM tower probably is the Reasoner, and the diffusion tower probably is the Generator. The lecture notes do not list actions as an output. No source confirms the name "3D Omni" or the tower mapping.

### Cosmos Reasoner

- Grounding and planning (Topic Note - NVIDIA COSMOS, § Lineage); embodied planning (Guest Lecture 9-21 Notes (part 1), § New Entities).
- A video critic: it checks synthetic data for hallucinations (Guest Lecture 9-21 Notes (part 1), § New Entities).

### Earlier generation

The 1.0 family trained on 20 million hours of video, on 10,000 H100 GPUs over three months. It has diffusion models that denoise and autoregressive models that predict the next token over video tokens (Topic Note - NVIDIA COSMOS, § About).

## Related

- [[World Models]]: Cosmos is a video predictor, so it sits on the pixel side of the pixel-versus-representation question (synthesis). The world-model topic note lists Cosmos as existing work.
- [[World Action Models]]: the Generator outputs actions, so Cosmos may count as a WAM (synthesis).
- [[Isaac Teleop]]: another NVIDIA robot-learning tool from the same lecture.

## Sources

- Topic Note - NVIDIA COSMOS
- Guest Lecture 9-21 Notes (part 1)
