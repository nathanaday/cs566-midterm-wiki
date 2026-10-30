---
id: con-bx24yb
type: topic
kind: concept
description: A model that takes sensor tokens and text tokens as input and gives action tokens as output, as defined in the Sep 21 CS566 guest lecture notes.
tags: [machine-learning]
aliases: [WAM, world action model]
created: 2026-09-28T00:00:00
updated: 2026-09-28T00:00:00
refreshed: 2026-09-28T00:00:00
status: draft
sources: ["Guest Lecture 9-21 Notes (part 1)", "RT-2 (note)", "Genie (note)", "Topic Note - NVIDIA COSMOS", "Learning Goals"]
---

> [!concept] Draft · Concept
> 5 sources · refreshed 2026-09-28 · #machine-learning

## Definition

A world action model (WAM) takes sensor tokens and text tokens as input and gives action tokens as output (Guest Lecture 9-21 Notes (part 1), § New Entities).

## Explanation

The lecture notes give only the inputs and the outputs. The points below are synthesis, not claims from one source.

- **Overlap with VLAs.** A camera is a sensor, so a [[Vision Language Action Models|VLA]] fits this definition. The RT-2 note lists World Action Models among its topics, next to Vision Language Action Models (RT-2 (note)).
- **Wider input.** "Sensor tokens" is wider than vision. The definition admits other sensors, such as depth, audio, or force. This fits the owner's interest in multi-modal perception and decision making on the edge (Learning Goals, § Interests).
- **Genie does not fit.** The Genie note files Genie under World Action Models (Genie (note)). But Genie takes no text, and its dynamics model predicts the next frame, not an action (§ Summary). By this definition it is a [[World Models|world model]].
- **Cosmos may fit.** The Cosmos 3 Generator takes text, vision, sound, and action, and outputs vision, sound, and action (Topic Note - NVIDIA COSMOS, § Lineage). So [[NVIDIA Cosmos]] may count as a WAM.

### Open questions

- Does a WAM also predict the next state of the world, as a [[World Models|world model]] does? The lecture notes give only the inputs and outputs.
- Is "WAM" a separate class from VLA, or a wider name for the same class? No source in the vault says.

## Related

- [[Vision Language Action Models]]
- [[World Models]]
- [[NVIDIA Cosmos]]

## Sources

- Guest Lecture 9-21 Notes (part 1)
- RT-2 (note)
- Genie (note)
- Topic Note - NVIDIA COSMOS
- Learning Goals
