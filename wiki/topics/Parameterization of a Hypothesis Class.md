---
id: con-p7hq2k
type: topic
kind: concept
description: A model is a family of functions indexed by its parameters, and the way the parameters enter the formula decides which functions the family contains and how hard they are to find; two formulas with different parameters can name the same set of functions, and a formula can name a strict subset of another.
tags: [machine-learning/cs566-deeplearning]
aliases: [Hypothesis class, Hypothesis space, Model family, Reparameterization, Over-parameterization, Reachable functions]
created: 2026-10-29T22:50:00
updated: 2026-10-29T22:50:00
refreshed: 2026-10-29T22:50:00
status: draft
sources: ["[[Block 1 Slides]]", "[[Block 2 Slides]]", "[[Block 3 Slides]]", "[[F26-midterm-review-234p]]", "[[CSCI 566 Midterm (Spring 2024)]]"]
up: ["[[Function Approximation]]"]
---

> [!concept] Concept
> 5 sources · refreshed 2026-10-29 · #machine-learning/cs566-deeplearning
> Up: [[Function Approximation]]

## Definition

A hypothesis class is the set of functions a model can represent. The slides write it as "Set, ℋ, of candidate hypothesis functions, h : 𝒳→ 𝒴" and give "all possible decision trees" as the example ([[Block 1 Slides]], p. 250). A parametric model such as $f(x; W) = Wx$ names that set through its weights: each choice of $W$ picks one function, and the class is every function some $W$ can produce ([[Block 1 Slides]], p. 231). The parameterization is the rule that turns parameter values into a function. Synthesis: two rules can produce the same class, and a rule can produce only part of a class that looks the same on paper. That is what the sample midterm tests in Q37 and Q38.

## Explanation

### What the decks define

The supervised learning setup has four pieces: inputs $x \in \mathcal{X}$, outputs $y \in \mathcal{Y}$, an unknown target $c^* : \mathcal{X} \to \mathcal{Y}$, and the hypothesis set $\mathcal{H}$. The learner "produces a hypothesis function, ŷ = h(x), that best approximates unknown target function y = c*(x) on the training data" ([[Block 1 Slides]], p. 250). The goal is approximation: "f does NOT have to be exactly f*" (p. 223). For $f$ to approximate any $f^*$, "f is better to be highly capable", and deep learning qualifies because it is "Non-linear (high capacity)" (p. 226).

Model complexity is "The capacity of a set of function to fit data points". In practice it refers to "The number of learnable parameters" and "The value range for those parameters" ([[Block 2 Slides]], p. 89). The summary slide shortens this to "the ability to fit various functions" (p. 95). Model selection means "Pick up a model family, then select proper hyper-parameters" (p. 94). On a two-class dataset, "more neurons = more capacity" ([[Block 3 Slides]], p. 95). [[Overfitting and Underfitting]] covers the complexity curve; [[VC Dimension]] covers the precise measure the slide names.

The decks define the class, the capacity, and the family. They never ask whether two formulas with different parameters name the same family, or whether a formula can leave part of a family out. The rest of this section is Synthesis, written to answer that question for the exam.

### Parameters as coordinates on a family

Synthesis: think of the parameter vector as a coordinate that points at one function in the family. For $y = wx$ with $w \in \mathbb{R}$, the family is every line through the origin, and $w$ is the slope. Two things about the family follow from the formula and from nothing else:

- **Which functions are reachable.** The class is the image of the parameter map $w \mapsto f(\cdot\,; w)$. If the map misses some functions, the class is smaller than its formula suggests.
- **How easy a function is to find.** [[Gradient Descent]] moves in parameter space, so the shape of the map decides how smooth the loss surface is in $w$, how many $w$ give the same function, and whether the gradient blows up anywhere.

The first point is about the class. The second is about optimization. They are separate, and the midterm tests them separately: it fixes the second by assuming unlimited data and asking about the best outcome.

### A parameterization can shrink the class

Synthesis: take $y = w^2 x$. Each $w$ still gives a line through the origin, so the family looks like the linear family. The slope is $w^2$, which is never negative, so the family contains only lines with slope $\ge 0$. No value of $w$ reaches $y = -x$. In the slides' terms, the formula limits "The value range for those parameters" that matter, which is one of the two things model complexity refers to ([[Block 2 Slides]], p. 89). The slope is the parameter that matters, and the formula restricts its range to $[0, \infty)$.

The test for a shrunken class is to write down the function the formula produces, read off the effective parameters (here, the slope), and ask what values they can take.

### A reparameterization keeps the class

Synthesis: take $y = \tan(w)\,x + wx = (\tan w + w)\,x$. The slope is $g(w) = \tan w + w$. On the interval $(-\pi/2, \pi/2)$, $\tan w$ runs from $-\infty$ to $+\infty$ and is continuous, and adding $w$ keeps it continuous and increasing, so $g$ takes every real value. Every line through the origin is reachable. The class is the same set as $\{y = wx\}$, with a different coordinate on it. This is a reparameterization: a change of coordinates on the same family. A reparameterization leaves the best achievable fit unchanged because the best function is in both classes.

Over-parameterization is the case where many coordinates name the same function. The slope $\tan w + w$ repeats on every branch of $\tan$, so infinitely many $w$ give the same line. The class is still the set of lines through the origin.

### Stacked linear layers: an over-parameterized linear class

The decks give one example of this kind, in the form of a warning. A network with two layers and no activation between them is "equivalent to a single affine layer": from $h = W_1 x + b_1$ and $y = W_2 h + b_2$, "we get y = W2W1x + W2b1 + b2", so "The combined weight is W2W1 and the combined bias is W2b1 + b2". The scalar case is $h = 3x + 2$, $y = 2h - 1$, giving $y = 6x + 3$ ([[F26-midterm-review-234p]], p. 42). The review's summary slide states it as "Stacking affine layers without a nonlinearity still gives one affine map" (p. 37). [[Block 3 Slides]] asks "What if we try to build a neural network without one?" and answers "We end up with a linear classifier again!" (p. 66; the question is posed on p. 65; repeated in [[F26-midterm-review-234p]], p. 44).

Synthesis: in the language of this topic, the two-layer linear network is a reparameterization of the one-layer linear class. It has more parameters ($W_1, b_1, W_2, b_2$ against $W, b$), so it is over-parameterized, and many pairs $(W_1, W_2)$ give the same product $W_2 W_1$. The class does not grow. The reachable functions are still the affine maps, and if the hidden width is smaller than the input or output width, the product $W_2 W_1$ has limited rank, so the class can even shrink. The activation is what adds functions. See [[Fundamentals of Deep Learning Nonlinear Activation]] for the bends each ReLU adds.

### Same class, different landscape

Synthesis: an equal class means an equal best-case fit, and nothing more. The slides note that for linear models "The loss function is typically convex" ([[Block 1 Slides]], p. 344). That holds for $y = wx$ under squared loss: the loss is a parabola in $w$. Under $y = (\tan w + w)\,x$ the same loss becomes a function of $w$ with poles at $w = \pm\pi/2, \pm 3\pi/2, \dots$, where the slope and its gradient $\sec^2 w + 1$ blow up, and with repeated minima on every branch. Gradient descent can reach a minimum on either, and with a finite dataset and a fixed learning rate the second is the harder run. The exam removes this difference by saying "unlimited data" and asking for the answer that "best describes the outcome", which points at the best function in the class rather than at a training run.

## Exam Questions

**Q37.** Linear regression on $(x, y)$ pairs with unlimited data. Model A is $y = w^2 x$ and model B is $y = wx$. Which statement best describes the outcome? Answer: B, there are datasets on which B performs better than A ([[CSCI 566 Midterm (Spring 2024)]], Q37).

Every function of A is a line through the origin with slope $w^2 \ge 0$, and B reaches that same line with its own $w$ set to $w^2$. B's class contains A's class, so A never beats B. B also reaches negative slopes. On a dataset generated by $y = -2x$, B fits it and A can do no better than the flat line $y = 0$. With unlimited data there is no overfitting to separate them, so the only difference is which functions each class contains.

**Q38.** Same setup, with model A now $y = \tan(w)\,x + wx$ and model B $y = wx$. Answer: D, they perform equally well on all datasets ([[CSCI 566 Midterm (Spring 2024)]], Q38).

A's slope is $\tan w + w$. This takes every real value as $w$ moves across $(-\pi/2, \pi/2)$, so A's class is every line through the origin, and so is B's. The classes are equal, so the best fit is equal on any dataset. A's parameter space is a worse place to run gradient descent, because of the poles of $\tan$, and that is why the question says unlimited data and asks about the best outcome: it is asking about the class, and the class is the same.

**Q44.** An MLP with one hidden layer, 2 inputs, 1 output, and no activation after the hidden layer or the output. With enough data and hidden neurons, which of $y = x$, $y = |x|$, $y = x^2$ can it fit? Answer: A, only $y = x$ ([[CSCI 566 Midterm (Spring 2024)]], Q44).

Two affine layers with nothing between them collapse to one affine map $y = (W_2 W_1)x + (W_2 b_1 + b_2)$ ([[F26-midterm-review-234p]], p. 42). The class is the affine functions. $y = x$ is affine. $y = |x|$ has a corner and $y = x^2$ curves, so neither is in the class, and adding hidden neurons adds coordinates without adding functions.

## Related

- [[Function Approximation]]: the goal that a hypothesis class serves; the class is the set of $f$ the learner can choose from
- [[Linear Classification]]: the class $f(x; W, b) = Wx + b$ that Q37, Q38, and Q44 all reduce to
- [[Overfitting and Underfitting]]: model complexity as the capacity of the class, and why unlimited data removes the estimation side of the comparison
- [[Fundamentals of Deep Learning Nonlinear Activation]]: the collapse of stacked affine layers and what an activation adds to the class
- [[Linear Separability]]: the datasets the linear class cannot fit, whatever its parameterization
- [[VC Dimension]]: the slides' precise measure of the capacity of a class
- [[Gradient Descent]]: the search in parameter space, whose difficulty a reparameterization changes

## Sources

- [[Block 1 Slides]], pp. 223–231, 250, 344
- [[Block 2 Slides]], pp. 89, 94–95
- [[Block 3 Slides]], pp. 65–66, 95
- [[F26-midterm-review-234p]], pp. 37, 42, 44
- [[CSCI 566 Midterm (Spring 2024)]], Q37, Q38, Q44
