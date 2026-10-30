---
id: con-fx77h7
type: topic
kind: concept
description: A model that predicts how the state of the world changes in response to an action, so that a system can search imagined actions for the one that best meets an objective.
tags: [machine-learning]
aliases: [world model]
created: 2026-09-28T00:00:00
updated: 2026-10-19T18:32:33
refreshed: 2026-10-19T18:32:33
status: stable
sources: ["Topic Note - World Models", "Topic Note - Reinforcement Learning in Differentiable vs Non-Differentiable Systems", "Topic Note - Sample Efficiency", "Topic Note - NVIDIA COSMOS", "World Models, Ha & Schmidhuber (note)", "DreamerV3 (note)", "V-JEPA 2 (note)", "A Path Towards Autonomous Machine Intelligence (note)", "Genie (note)", "Fall 2026 Reading List", "Learning Goals"]
---

> [!concept] Concept
> 11 sources · refreshed 2026-10-19 · #machine-learning

## Definition

A world model predicts the outcome of an action: how the state of the world changes when an agent acts. A system with a world model can search the predicted outcomes for the action that best completes a task objective (Topic Note - World Models, § About). The term comes from Ha & Schmidhuber (2018), which the reading list calls "the origin paper for the term" (Fall 2026 Reading List, item 7).

## Explanation

### Why it matters

- **Planning by search.** The topic note says that feed-forward propagation is computationally limited, and that reasoning and planning need search and optimization. A feed-forward network perceives the state, makes a prediction, and acts. A world-model system perceives the state, receives an objective, imagines an action, determines the optimal action, and then acts (Topic Note - World Models, § Feed Forward Propagation vs Search Optimization). The note calls LLM-based agents "System 1" and world-model agents "System 2" (§ Agentic Systems: Two Ways).
- **Training in imagination.** The Ha & Schmidhuber note says the controller trains entirely inside the model's imagined rollouts and then transfers to the real environment (World Models, Ha & Schmidhuber (note), § Summary). The DreamerV3 note says the actor and the critic train only on trajectories imagined in latent space, never on replayed pixels (DreamerV3 (note), § Summary).
- **Cost on small hardware.** The DreamerV3 note says imagination rollouts run on latent vectors of a few hundred dimensions, not on frames, and calls that ratio the argument for latent prediction on constrained hardware (DreamerV3 (note), § What To Read For). This matters for the owner's interest in decision making on edge systems (Learning Goals, § Interests).
- **Known dynamics need no learning.** When Newtonian physics gives the state transition in closed form, the world model is exact and deterministic, and control becomes a convex optimization problem solved as MPC. Reinforcement learning enters when part of the transition cannot be modeled in closed form (Topic Note - Reinforcement Learning in Differentiable vs Non-Differentiable Systems). See Differentiable vs Non-Differentiable Reinforcement Learning.

### Designs in the vault

The paper notes are pre-reading summaries, not the papers.

| Work | Prediction target | Where actions come from | Source |
|---|---|---|---|
| Ha & Schmidhuber (2018) | Next VAE latent (Variational Autoencoder), predicted by an MDN-RNN from the current latent and the action | A tiny linear controller picks actions from the latent and the RNN state | World Models, Ha & Schmidhuber (note) |
| DreamerV3 (2023) | Next latent state of a Recurrent State Space Model (RSSM) learned from pixels; each state has a deterministic recurrent part and a stochastic part | An actor and a critic trained in imagination; the note says one hyperparameter setting works across more than 150 tasks | DreamerV3 (note) |
| V-JEPA 2 (2025) | Masked regions in representation space; self-supervised on more than a million hours of video | A second stage conditions the predictor on actions from a small amount of robot data and uses it for planning | V-JEPA 2 (note) |
| Genie (2024) | Next frame, from video tokens plus a latent action; trained on about 200,000 hours of unlabeled gameplay video | A latent action model infers a discrete action (8 codes) between frames; at inference a person supplies it | Genie (note) |
| [[NVIDIA Cosmos]] | Video: the 1.0 family has diffusion models and next-video-token models | The Cosmos 3 Generator also outputs actions | Topic Note - NVIDIA COSMOS |
| LeCun (2022) | Representations, with the world model built as a hierarchy over multiple time scales | A position paper with a modular architecture (configurator, perception, world model, cost, actor, short-term memory); no experiments | A Path Towards Autonomous Machine Intelligence (note) |

### Pixel space versus representation space

The sources disagree about what a world model should predict. The grouping below is synthesis, not a claim from any one source.

- **Against pixels.** The LeCun note points to the paper's case against generative pixel prediction (A Path Towards Autonomous Machine Intelligence (note), § What To Read For). The V-JEPA 2 note says the claim under test is that prediction targets should be abstract, because pixels carry detail that no policy needs (V-JEPA 2 (note), § Summary).
- **Toward pixels or video.** The core Cosmos models are video predictors (Topic Note - NVIDIA COSMOS, § About). Genie predicts the next frame (Genie (note), § Summary). Ha & Schmidhuber and DreamerV3 learn their latents from frames or pixels (World Models, Ha & Schmidhuber (note), § Summary; DreamerV3 (note), § Summary).
- **Cost of a representation target.** With no decoder, there is no pixel reconstruction to inspect, so evaluation gets harder (V-JEPA 2 (note), § What To Read For).

No source in the vault shows which target works better.

### Hierarchical planning

The topic note says predictions happen at multiple levels of abstraction and over multiple time scales, and each level generates subgoals for the level below. Its example is planning an overseas trip: early on, a person plans only at a high level and defers the specific actions until they arrive. The note sketches one architecture with a world model per level: `encoder-1` maps the state $x(t)$ to a level 1 state, which feeds `world-model-1` and `encoder-2`; `encoder-2` gives a level 2 state for `world-model-2`; the predictions join into the objective as needed (Topic Note - World Models, § Hierarchical Planning).

The LeCun note says the paper proposes a world model built as a hierarchy over multiple time scales (A Path Towards Autonomous Machine Intelligence (note), § Summary). The two sources agree. Neither gives experimental evidence.

### Sample efficiency

The topic note lists Sample Efficiency as a related topic (Topic Note - World Models, § Related Topics). The sample-efficiency note defines two measures (Topic Note - Sample Efficiency):

- **Intelligence per watt**: "how many valid points do we get per watt of spend".
- **Intelligence per sample**: "how much does the model improve with just one more sample in the train data?"

The note says many models are poor in intelligence per sample: they need tens of thousands of training samples to learn even intuitive concepts. Synthesis: no source in the vault measures whether a world model improves either measure.

### Existing work named in the topic note

The topic note lists NVIDIA Cosmos and Gaussian Splatting (an NVIDIA GTC session) as existing work (Topic Note - World Models, § References). See [[NVIDIA Cosmos]] and [[3D Gaussian Splatting]].

### Open questions

- What would a latent action mean for a fixed camera that watches a scene change with no agent acting? (Genie (note), § What To Read For)
- What health check could run on a sensor node for a model that has no decoder? (V-JEPA 2 (note), § What To Read For)
- The reading list says DINO-WM builds a world model on frozen DINO features (Fall 2026 Reading List, item 3). No other source in the vault describes DINO-WM.

## Related

- [[World Action Models]]
- [[NVIDIA Cosmos]]
- [[Vision Language Action Models]]
- [[Recurrent Neural Networks (RNN)]]
- Variational Autoencoder (the latent model in Ha & Schmidhuber)
- Differentiable vs Non-Differentiable Reinforcement Learning
- [[3D Gaussian Splatting]]

## Sources

- Topic Note - World Models
- Topic Note - Reinforcement Learning in Differentiable vs Non-Differentiable Systems
- Topic Note - Sample Efficiency
- Topic Note - NVIDIA COSMOS
- World Models, Ha & Schmidhuber (note)
- DreamerV3 (note)
- V-JEPA 2 (note)
- A Path Towards Autonomous Machine Intelligence (note)
- Genie (note)
- Fall 2026 Reading List
- Learning Goals
