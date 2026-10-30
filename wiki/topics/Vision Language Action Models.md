---
id: con-xv6641
type: topic
kind: concept
description: A vision-language model that also outputs actions, usually by writing each action as tokens in the language model's output vocabulary.
tags: [machine-learning]
aliases: [VLA, vision-language-action model]
created: 2026-09-28T00:00:00
updated: 2026-09-28T00:00:00
refreshed: 2026-09-28T00:00:00
status: stable
sources: ["RT-2 (note)", "OpenVLA (note)", "Guest Lecture 9-21 Notes (part 1)", "Guest Lecture 9-21 Notes (part 2)", "Genie (note)", "Fall 2026 Reading List", "Learning Goals"]
---

> [!concept] Concept
> 7 sources · refreshed 2026-09-28 · #machine-learning

## Definition

A vision-language-action model (VLA) is a vision-language model that also outputs actions. The RT-2 note says RT-2 writes actions out as text strings, and that the paper states plainly that an action is another output vocabulary (RT-2 (note), § Summary). The OpenVLA note says OpenVLA puts each continuous action dimension into 256 bins, and the bins overwrite rarely used tokens in the language model's vocabulary, so acting is plain next-token prediction (OpenVLA (note), § Summary).

## Explanation

### Why it matters

- **Transfer.** The RT-2 note says knowledge from web pre-training carries over into robot manipulation, so the robot handles objects and instructions that it never saw in the robot data (RT-2 (note), § Summary).
- **Actions beyond robotics.** The OpenVLA note asks what else a model could output as tokens: an alarm level, a maintenance action, a control setpoint (OpenVLA (note), § What To Read For). This fits the owner's interest in machine decision making on the edge (Learning Goals, § Interests).
- The reading list recommends OpenVLA for the interface question, how a continuous action becomes tokens, and says to skip the manipulation benchmarks (Fall 2026 Reading List, item 11).

### Training data

- Lighting conditions have a significant effect on policy training. Some work goes into modeling lighting accurately in simulation (Guest Lecture 9-21 Notes (part 1), § New Entities).
- A model can learn a policy that works in simulation but fails in the real world. The lecture notes say it is difficult to model all physics of contact, collision, motion, and joints (Guest Lecture 9-21 Notes (part 2), § Training a Policy). See Sim-to-Real Transfer.
- [[Isaac Teleop]] collects real-world data: an operator controls the robot remotely (Guest Lecture 9-21 Notes (part 1), § New Entities).
- The OpenVLA note says OpenVLA fine-tunes on 970k real robot episodes from Open X-Embodiment (OpenVLA (note), § Summary).

### Models in the vault

| Model | Design | Source |
|---|---|---|
| RT-2 (2023) | Co-fine-tunes a large VLM on web image-text data and robot trajectories at the same time; actions as text strings | RT-2 (note) |
| OpenVLA (2024) | 7B; a Llama 2 backbone reads fused DINOv2 and SigLIP features; 970k episodes from Open X-Embodiment; 256 bins per action dimension | OpenVLA (note) |

### VLAs and world action models

- The Sep 21 guest lecture defines a world action model as sensor tokens and text tokens in, action tokens out (Guest Lecture 9-21 Notes (part 1), § New Entities). See [[World Action Models]].
- The RT-2 note lists both Vision Language Action Models and World Action Models as its topics (RT-2 (note)).
- Synthesis: a camera is a sensor, so every VLA fits the lecture definition. A world action model may also take other sensors. Genie uses no language and outputs frames, so it fits neither definition, although its note files it under world action models (Genie (note)).

Open: no source says whether world action model is a separate class from VLA or a wider name for it.

## Related

- [[World Action Models]]
- [[World Models]]
- [[Vision Language Models (VLM)]]
- [[Isaac Teleop]]
- Sim-to-Real Transfer

## Sources

- RT-2 (note)
- OpenVLA (note)
- Guest Lecture 9-21 Notes (part 1)
- Guest Lecture 9-21 Notes (part 2)
- Genie (note)
- Fall 2026 Reading List
- Learning Goals
