---
id: pol-xba7m0
type: topic
kind: policy
description: For CSCI 566 compute, use free notebooks first and stop or delete every paid cloud VM and disk after use, because a budget alert does not cap spending.
tags: [machine-learning/cs566-deeplearning]
aliases: [Compute and Cloud Credits]
created: 2026-09-28T00:00:00
updated: 2026-09-28T00:00:00
refreshed: 2026-09-28T00:00:00
status: stable
sources: ["[[Block 2 Slides]]"]
strength: should
---

> [!policy] Should · holds for repositories tagged #machine-learning/cs566-deeplearning
> 1 source · refreshed 2026-09-28

## Rule

- Start with the free notebooks: Kaggle or Colab ([[Block 2 Slides]], p. 20).
- Until the instructor announces course credit or CARC access, stop or delete every paid VM and disk when you finish ([[Block 2 Slides]], p. 20).
- Do not rely on a budget alert to limit cost ([[Block 2 Slides]], p. 20).

## Why

- "A budget alert is not a brake." Google says an alerts-only budget does not cap usage or spending; it only emails you while charges grow ([[Block 2 Slides]], p. 20).
- The Google Cloud $300 trial does not buy GPU time. A trial account cannot attach a GPU. You must upgrade to a paid account first, and then any use past the credit bills your card ([[Block 2 Slides]], p. 20).

## Applies when

Any GPU or cloud work for the CSCI 566 assignment or project, including work in cs566-course.

Free and student options ([[Block 2 Slides]], p. 20):

| Option | What it gives |
| --- | --- |
| Kaggle notebooks | A P100 or two T4s, about 30 GPU hours a week |
| Google Colab | A free GPU; the card and limits are not published |
| Azure for Students | $100 over 12 months, no credit card |
| GitHub Student Pack | A few GPU hours a month |

## Exceptions

The slides state none. Synthesis: the rule to stop paid resources applies "until then", so review it when the instructor announces course credit or CARC access ([[Block 2 Slides]], p. 20).

## Sources

- [[Block 2 Slides]], p. 20
