---
description: k-means lowers its squared-distance objective at every step and so converges, but only to a local minimum fixed by the starting centers; random restarts and k-means++ seeding are the standard remedies.
aliases: [k-Means Local Minimum, Centroid Initialization, k-means++, Random Restarts]
sources: ["[[Block 2 Slides]]", "[[F26-midterm-review-234p]]", "[[Block 7 Slides]]", "[[CSCI 566 Midterm (Spring 2024)]]"]
---

## Definition

A centroid is the center of a cluster: in [[k-Means]], the mean of the observations assigned to that cluster ([[Block 2 Slides]], p. 197). The algorithm starts from k centers chosen before any assignment ([[Block 2 Slides]], p. 195) and then repeats assignment and revision "until convergence" ([[Block 2 Slides]], p. 198). Where it stops depends on where it started: the review deck shows two finished runs on the same data with different centers and different totals ([[F26-midterm-review-234p]], p. 36).

## Explanation

### Why every step lowers the objective

k-means scores a clustering by $J$, "the total squared distance from points to their assigned centers" ([[F26-midterm-review-234p]], p. 35). The assignment step sends each point to its closest center, $z_i \leftarrow \arg\min_j \lVert \mu_j - x_i \rVert_2^2$ ([[Block 2 Slides]], p. 199), and the revision step sets each center to the mean of its points (p. 197). "With assignments fixed, the mean minimizes the sum of squared distances" ([[F26-midterm-review-234p]], p. 35).

Synthesis: neither step can raise $J$. A point changes cluster only when a closer center exists, and moving a center to the mean is the best move for fixed assignments. $J$ is a sum of squares, so zero bounds it from below, and the number of possible assignments is finite. A sequence that never rises and cannot cycle must stop. That is the convergence the slide promises, and it says nothing about which stopping point is reached.

### Why the stopping point is a local minimum

The review runs k-means twice on {1, 3, 5, 9} with k = 2. Run A ends at $\mu_1 = 2$, $\mu_2 = 7$ with $J = 10$. Run B ends at $\mu_1 = 3$, $\mu_2 = 9$ with $J = 8$. "Repeating the assignment and mean steps changes neither run", and "Comparing two converged runs does not prove global optimality" ([[F26-midterm-review-234p]], p. 36).

Synthesis: a converged run is a local minimum of $J$. No single assignment or mean step improves it, yet another start reaches a lower $J$. Run A is stuck because 5 is closer to 7 than to 2, so the split {1, 3} against {5, 9} never changes. The decks do not use the phrase "local minimum" for k-means. Block 7 uses it for gradient descent on a loss surface: at a local minimum or saddle point the gradient is zero and "gradient descent gets stuck" ([[Block 7 Slides]], p. 94). The k-means case is the same idea without gradients: the update rule has a fixed point that is not the best answer.

### What a poor start looks like

Synthesis: the decks give no picture of a bad initialization beyond the one-dimensional example. The usual failure in two dimensions: two starting centers land in the same true cluster and split it in half, while a third true cluster has no nearby center and is absorbed by a neighbor. Each step still lowers $J$, and the run converges with one center covering two true groups and two centers sharing one.

### Remedies

Synthesis: the decks state no fix, so both remedies below are background.

- Random restarts. Run k-means several times from different random centers and keep the run with the lowest $J$. The review's comparison of Run A and Run B is one restart done by hand: compute $J$ for each converged run and keep the smaller ([[F26-midterm-review-234p]], p. 36). The lowest $J$ found is still no proof of the global minimum.
- k-means++ seeding (Arthur and Vassilvitskii, 2007). Pick the first center at random from the data. Pick each later center from the data with probability proportional to its squared distance from the nearest center already chosen, so the seeds spread out. Then run ordinary k-means. The seeding gives an expected $J$ within a factor of $O(\log k)$ of the optimum, and in practice it reaches a low $J$ in fewer restarts.

Synthesis: the pass count matters at scale. One CuraWeb assignment pass costs about $3 \times 10^{14}$ distance computations ([[Block 2 Slides]], p. 202), so a seeding that saves restarts or iterations pays for itself.

## Exam Questions

**Q49.** In clustering, what does "centroid" mean? Answer A: the center point of a cluster in k-means ([[CSCI 566 Midterm (Spring 2024)]], Q49). The slides say "cluster center" and set it to the "mean of assigned observations" ([[Block 2 Slides]], p. 197); the word centroid appears on the CuraWeb slide, "6.42B points against 49K centroids" (p. 202). The other options describe a largest point, an average between-cluster distance, and a random start in hierarchical clustering, none of which the decks define.

**Q50.** If the initial centroids are chosen poorly, what may happen? Answer B: the algorithm may converge to a local minimum ([[CSCI 566 Midterm (Spring 2024)]], Q50). The algorithm runs from any start and the user fixes k, so A and C are out; it never switches method, so D is out. Run A on the review slide is this outcome: a converged run with $J = 10$ when $J = 8$ is reachable ([[F26-midterm-review-234p]], p. 36).

## Related

- [[k-Means]]: the algorithm and its objective; this topic covers only where it stops
- [[Clustering]]: the task, and the center-and-spread view of a cluster
- [[Gradient Descent]]: the other place the course meets local minima, with gradients
- [[Weight Initialization]]: the neural-network version of a start that shapes where training ends

## Sources

- [[Block 2 Slides]], pp. 195-199, 202
- [[F26-midterm-review-234p]], pp. 31-36. Pp. 31-34 repeat Block 2 slides 195-198.
- [[Block 7 Slides]], pp. 93-94, local minima for gradient descent
- [[CSCI 566 Midterm (Spring 2024)]], Q49, Q50
