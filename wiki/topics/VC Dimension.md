---
id: con-v3d9hs
type: topic
kind: concept
description: The VC dimension of a classifier family is the largest number of points it can shatter, which is label in every possible way; a line or a disc in the plane has VC dimension 3, so four points can defeat either.
tags: [machine-learning/cs566-deeplearning]
aliases: [Vapnik-Chervonenkis Dimension, Shattering, Model Capacity Measure]
created: 2026-10-29T22:50:00
updated: 2026-10-29T22:50:00
refreshed: 2026-10-29T22:50:00
status: draft
sources: ["[[Block 2 Slides]]", "[[CSCI 566 Midterm (Spring 2024)]]"]
up: ["[[Overfitting and Underfitting]]"]
---

> [!concept] Concept
> 2 sources · refreshed 2026-10-29 · #machine-learning/cs566-deeplearning
> Up: [[Overfitting and Underfitting]]

## Definition

The VC dimension is the slides' "More precisely measure of complexity": "VC dim for classification model: the maximum number of examples the model can shatter" ([[Block 2 Slides]], p. 89). Synthesis: a hypothesis class shatters a set of $n$ points when, for each of the $2^n$ ways to assign binary labels to them, some hypothesis in the class predicts every label correctly. The VC dimension is the largest $n$ for which some set of $n$ points is shattered. One shattered set is enough; the class does not have to shatter every set of that size.

## Explanation

### Why the slides bring it up

Model complexity is "The capacity of a set of function to fit data points". In practice it "usually refers to" the number of learnable parameters and their value range, but "It's hard to compare between different types of ML models", for example "trees vs neural network" ([[Block 2 Slides]], p. 89). The VC dimension answers that problem: it counts what the classifier can fit, so it compares a tree, a linear model, and a network on one scale. The deck gives this one slide and no examples; everything below is Synthesis.

### A line in the plane

Synthesis: a linear classifier in two dimensions has VC dimension 3. Three points at the corners of a triangle can be shattered: each of the 8 labelings is either all one class, one point against two (a line separates one corner from the opposite side), or the reverse. Four points cannot be shattered. Place them at the corners of a square and label the diagonals differently, the XOR arrangement of [[Linear Separability]]: no line puts both members of one diagonal on one side and both of the other on the other side. Four points with one inside the triangle of the other three also fail, since a line that puts the three outer points on one side puts the inner point there too.

### A disc in the plane

Synthesis: a disc classifier with learnable center $(a, b)$ and radius $r$ also has VC dimension 3. Take three points that are not on one line. A tiny disc picks out any single point, a large disc covers all three, and a disc of very large radius acts like a half-plane, so it can cover any two and leave out the third. Four points cannot be shattered. Put one point inside the triangle of the other three and ask for the three outer points inside the disc and the inner point outside: a disc that holds the three corners holds the whole triangle, because a disc is convex, so the inner point is inside as well. Four corners of a square fail too: a disc that holds two opposite corners contains the segment between them, and a short calculation shows it must then hold at least one of the other two corners.

### Parameters and capacity

Synthesis: the line has three parameters $(w_1, w_2, b)$ and the disc has three $(a, b, r)$, and both have VC dimension 3, so in these cases the count matches. It does not in general. The classifier $\text{sign}(\sin(wx))$ on the real line has one parameter and infinite VC dimension, which is why the slide calls parameter count the usual measure and VC dimension the precise one. The slide's complexity curve, where generalization error falls and then rises as complexity grows ([[Block 2 Slides]], p. 90), reads the same with VC dimension on the horizontal axis.

## Exam Questions

**Q41.** A binary classifier on a 2D plane predicts $y = 0$ when $(x_1 - a)^2 + (x_2 - b)^2 < r^2$ and $y = 1$ otherwise, with $a$, $b$, $r$ learnable. What is the minimum number of distinct points that makes perfect prediction impossible? Answer: C, 4 ([[CSCI 566 Midterm (Spring 2024)]], Q41).

Reasoning: the boundary is a disc, and the question asks for the smallest set size the disc family cannot shatter, which is one more than its VC dimension. Three points not on one line can always be fit: a small disc isolates one point, a large disc holds all three, and a huge disc acts as a half-plane and holds any two. Four points can be placed so that no disc fits one labeling: with one point inside the triangle of the other three, no disc holds the three corners and excludes the inner point. So 2 and 3 are too few, 8 is more than needed, and the answer is 4.

Synthesis: the three-point claim assumes the points are in general position. Three points on one line with the outer two labeled inside and the middle one outside cannot be fit either, but the VC definition asks whether some set of that size is shattered, and the triangle is.

## Related

- [[Overfitting and Underfitting]]: model complexity, data complexity, and the complexity curve
- [[Linear Separability]]: the XOR arrangement that defeats a line
- [[Linear Classification]]: the line classifier with VC dimension 3 in the plane
- [[Decision Trees]]: the tree whose size is the deck's other measure of complexity
- [[Neural Networks]]: "more neurons = more capacity"
- [[Model Evaluation]]: generalization error, which VC dimension is meant to bound

## Sources

- [[Block 2 Slides]], pp. 89-90, 95
- [[CSCI 566 Midterm (Spring 2024)]], Q41
