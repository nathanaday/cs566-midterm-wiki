---
id: doc-jvcwqn
type: topic
kind: concept
description: Data preprocessing transforms input data before training; CSCI 566 Block 7 covers zero-centering, normalization, PCA whitening, missing values, and the input convention of a pretrained model, with statistics fitted on the training split only.
tags: [machine-learning/cs566-deeplearning]
aliases: [Input preprocessing, Zero-centering, Zero-center data, Mean subtraction, Input normalization, Normalize data, Standardization, Feature scaling, PCA whitening, Whitening, Handling missing data, Missing data, Imputation, StandardScaler, sklearn.preprocessing.StandardScaler, Image preprocessing follows the model]
created: 2026-10-12T16:58:10
updated: 2026-10-13T18:22:47
refreshed: 2026-10-13T18:22:47
status: stable
sources: ["[[Block 7 Slides]]"]
up: ["Neural Network Training"]
---

> [!concept] Concept
> 1 source · refreshed 2026-10-13 · #machine-learning/cs566-deeplearning
> Up: Neural Network Training

## Definition

Data preprocessing is the set of transformations applied to input data before training. The Block 7 deck lists three steps: zero-center data, normalize data, and PCA whitening ([[Block 7 Slides]], pp. 19-20). The deck also covers missing values and the input convention of a pretrained model under the same subject (pp. 38-39).

## Explanation

### Why preprocess

The slides ask "Why do we need preprocessing?" (p. 20). They answer it step by step on pp. 21, 22, and 36 (see below).

A running example shows why scale matters. Two numeric inputs go to the same small classifier. Feature A ranges from 0 to 1. Feature B ranges from 0 to 1,000 ([[Block 7 Slides]], p. 18). The slide rule: "Put comparable numeric features on sensible scales." The reason: "Scaling changes how parameter updates affect predictions" (p. 18).

### Zero-centering

Subtract the per-feature mean, so that each feature is centered at zero. The NumPy form on the slide is `X -= np.mean(X, axis = 0)` ([[Block 7 Slides]], p. 22).

Why, from the slide: "Centering can reduce imbalance in layer inputs." "ReLU keeps positive inputs. Input scale and offsets can affect which units activate" (p. 21). See [[Activation Functions]].

### Normalization

After centering, divide each feature by its standard deviation. The NumPy form is `X /= np.std(X, axis = 0)` ([[Block 7 Slides]], p. 22). Why, from the slide: "Different feature magnitudes can create uneven gradient scales" (p. 22).

The result has zero mean and unit variance in each dimension: x̂(k) = (x(k) − E[x(k)]) / √Var[x(k)] (pp. 25, 29).

A limit: "Centering and scaling do not force an arbitrary distribution to become Gaussian." "The resulting values need not follow a bell-shaped distribution" (p. 27).

### PCA whitening

Why, from the slide: PCA whitening removes correlation between input features ([[Block 7 Slides]], p. 36). "Whitening transforms the data into a space where the features are uncorrelated, and all have the same variance" (p. 37).

The steps on p. 37:

1. Center: X − μ.
2. Rotate by the PCA matrix U, formed by the eigenvectors: Uᵀ(X − μ).
3. Scale by the inverse square root of the eigenvalue matrix, Λ^(-1/2). This "normalizes the variance across all dimensions."
4. A last rotation, labeled with a matrix Q. The slide does not define Q.

The slide adds: "Not common to use PCA whitening" (p. 37).

### Input preprocessing and normalization inside the network

"Input preprocessing happens once. Hidden activations change during training" ([[Block 7 Slides]], p. 24). Inside the network, a layer normalizes the hidden activations and then learns a scale and shift. "Normalization also changes the optimization behavior" (p. 24, citing Ioffe & Szegedy (2015) and Santurkar et al. (2018)). The deck uses the same formula for both cases (pp. 25, 29). See [[Batch Normalization]] and [[Layer Normalization]].

### Fitted statistics belong to the pipeline

The training split fits both the model weights and the preprocessing statistics ([[Block 7 Slides]], p. 17). "The fitted preprocessing rule is part of the model pipeline" (p. 23). The rule for this is [[Fit Preprocessing on Training Data Only]].

### StandardScaler in scikit-learn

A slide titled "Important Interview Questions" shows the scikit-learn `preprocessing` module. Its `StandardScaler` utility class is "a quick and easy way" to standardize an array-like dataset ([[Block 7 Slides]], p. 41). The example:

- `scaler = preprocessing.StandardScaler().fit(X_train)` fits the scaler on the training data.
- `scaler.mean_` is about `[1., 0., 0.33]`, and `scaler.scale_` is about `[0.81, 0.81, 1.24]`.
- `X_scaled = scaler.transform(X_train)` applies it. The slide highlights the `fit` and `transform` calls.
- "Scaled data has zero mean and unit variance" (p. 41).

### Missing data

Another interview slide asks: "How would you handle missing data in a dataset?" It gives three ways ([[Block 7 Slides]], p. 39):

1. **Imputation.** Replace missing values with a statistic like the mean, median, or mode, or use a model to predict the missing values.
2. **Removal.** "Check how deletion changes data coverage."
3. **Indicator variable.** For some algorithms, add a new variable that marks where data is missing, along with imputation.

The same slide says: "Fit any imputation rule on training data" (p. 39).

### Inputs for a pretrained model

"For a pretrained classifier, use its expected input convention" ([[Block 7 Slides]], p. 38):

| Item | What to do |
|---|---|
| Image size | Resize and crop using the model specification. |
| Channel values | Use the expected numeric range and channel order. |
| Normalization | Apply the specified per-channel mean and scale. |

The reason: "A consistent input pipeline is part of successful transfer" (p. 38). See [[Transfer Learning]].

Synthesis: here the mean and scale come from the model specification, not from your own training split.

### Open points on the slides

- p. 37: the last rotation uses a matrix Q that the slide does not define.
- p. 39: "Fit any imputation rule on training data" sits under the Removal item, not under Imputation.
- p. 41: the example transforms only `X_train`. It does not show the transform of test data. The slide ends at "Scaled data has zero mean and unit variance:" with no example after the colon.

## Related

- [[Fit Preprocessing on Training Data Only]]: the rule for fitted statistics
- [[Batch Normalization]]: normalization of hidden activations
- [[Layer Normalization]]
- [[Activation Functions]]: ReLU and input offsets
- [[Transfer Learning]]: inputs for a pretrained model
- Flower Classifier Running Example
- [[Model Evaluation]]: the train, validation, and test splits

## Sources

- [[Block 7 Slides]], pp. 17-25, 27, 29, 36-41
