---
id: con-htqd9d
type: topic
kind: concept
description: A method that reconstructs a static scene from posed photos as an explicit cloud of oriented 3D Gaussians, so the scene can be rendered from new viewpoints in real time.
tags: [machine-learning]
aliases: [3DGS, Gaussian Splatting]
created: 2026-09-28T00:00:00
updated: 2026-10-19T14:42:31
refreshed: 2026-10-19T14:42:31
status: draft
sources: ["Topic Note - 3D Gaussian Splatting (3DGS)", "Topic Note - World Models"]
---

> [!concept] Draft · Concept
> 2 sources · refreshed 2026-10-19 · #machine-learning

## Definition

3D Gaussian Splatting (3DGS) reconstructs a static scene from a set of posed photos, so the scene can be rendered from new viewpoints in real time. It replaces the neural network of NeRF with an explicit point cloud, in which every point is a small 3D blob (Topic Note - 3D Gaussian Splatting (3DGS)).

## Explanation

Each Gaussian has (Topic Note - 3D Gaussian Splatting (3DGS)):

- a 3D position;
- an anisotropic covariance, stored as a scale vector and a rotation quaternion, so the blob can be stretched and oriented;
- an opacity;
- a color stored as spherical harmonic coefficients, so the color can change with view direction.

The note does not describe how the Gaussians are fit to the photos or how they are rendered.

The world-model topic note lists Gaussian Splatting, through an NVIDIA GTC session, as existing work related to world models (Topic Note - World Models, § References). It does not say how the two connect.

## Related

- [[World Models]]

## Sources

- Topic Note - 3D Gaussian Splatting (3DGS)
- Topic Note - World Models
