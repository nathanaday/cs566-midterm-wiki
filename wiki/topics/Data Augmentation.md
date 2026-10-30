---
description: A regularizer that applies random, label-preserving transformations (flips, crops and scales, color jitter, learned AutoAugment policies) to each training image before the network sees it, while the label stays the same.
aliases: [Augmentation, Label-preserving augmentation, Augment only with label-preserving transformations, Horizontal flip, Random crops and scales, Color jitter, PCA color augmentation, AutoAugment, Automatic data augmentation]
sources: ["[[Block 7 Slides]]", "[[F26-midterm-review-234p]]"]
---

## Definition

Data augmentation transforms each training image after it is loaded and before the network sees it. The label does not change. The slides present it as a form of regularization ("Regularization: Data Augmentation") ([[Block 7 Slides]], pp. 154-155).

## Explanation

### The pipeline

The slides draw the training pipeline in two steps ([[Block 7 Slides]], pp. 154-155):

1. Load an image and its label ("cat"). Pass the image through the CNN and compute the loss against the label.
2. With augmentation, transform the image before the CNN. The label "cat" goes to the loss unchanged.

Synthesis: each epoch sees a slightly different version of each image, so the network can fit the exact training pixels less easily. This is why augmentation counts as a regularizer against [[Overfitting and Underfitting|overfitting]].

### Keep the label valid

The slide title states the rule: "An Augmented Example Must Keep a Valid Label". The slide also says: "Choose transformations that preserve the task label." ([[Block 7 Slides]], p. 156). In the flower example, a mild crop or brightness change of a photo labeled daisy gives an altered photo that is still labeled daisy (p. 156). See Flower Classifier Running Example.

The same transformation can be correct for one task and wrong for another (p. 163):

- **Flower photo.** "A rotated view may still show the same flower species."
- **Digit recognition.** "A rotated 6 can resemble a 9. Keeping label 6 can be wrong."

The slide concludes: "Augmentation depends on the task semantics." (p. 163). The slide gives the list of transformations under the heading "Choose transformations that keep labels valid": translation, rotation, stretching, shearing, and "task-valid lens distortions" (p. 162).

[[F26-midterm-review-234p]] repeats the slides of pp. 156 and 163 (pp. 134-135). A third review slide, "Augmentation Must Keep Labels Valid", draws one transformation for both tasks: "A 180 degree rotation keeps a daisy a daisy, but a rotated 6 can resemble a 9." The rotated daisy keeps "Label: daisy (still valid)". For the digit, "Label 6 can be wrong: may resemble 9". The slide's rule: "Augment only when the target stays valid for the task" ([[F26-midterm-review-234p]], p. 136).

### Horizontal flips

A horizontal flip mirrors the image from left to right. The slide shows a cat image and its mirror image (p. 157).

### Random crops and scales

In training, sample random crops and scales. The slides give the [[ResNet]] recipe (p. 158):

1. Pick a random L in the range [256, 480].
2. Resize the training image so that its short side = L.
3. Sample a random 224 x 224 patch.

In testing, average the predictions on a fixed set of crops. The ResNet recipe (p. 159):

1. Resize the image at 5 scales: {224, 256, 384, 480, 640}.
2. For each size, use 10 crops of 224 x 224: 4 corners + center, + flips.

Synthesis: the slides do not state the total, but 5 scales x 10 crops gives 50 crops for each test image.

### Color jitter

- **Simple.** Randomize contrast and brightness (pp. 160-161).
- **More complex** (p. 161):
  1. Apply PCA to all [R, G, B] pixels in the training set.
  2. Sample a "color offset" along the principal component directions.
  3. Add the offset to all pixels of a training image.

The slide says this version was used in Krizhevsky et al. 2012 ([[AlexNet]]), ResNet, and other models (p. 161).

### Automatic data augmentation (AutoAugment)

The slide on automatic data augmentation cites Cubuk et al., "AutoAugment: Learning Augmentation Strategies from Data", CVPR 2019 (p. 164). Its figure shows five sub-policies. Each sub-policy has two operations, and each operation has a probability and a magnitude (p. 164):

| Sub-policy | First operation | Second operation |
|---|---|---|
| 1 | ShearX, 0.9, 7 | Invert, 0.2, 3 |
| 2 | ShearY, 0.7, 6 | Solarize, 0.4, 8 |
| 3 | ShearX, 0.9, 4 | AutoContrast, 0.8, 3 |
| 4 | Invert, 0.9, 3 | Equalize, 0.6, 3 |
| 5 | ShearY, 0.8, 5 | AutoContrast, 0.7, 3 |

The figure applies each sub-policy to the same digit image ("15") in three batches (p. 164). Synthesis: the outputs of one sub-policy differ from batch to batch. This is consistent with each operation being applied at random with its probability. The slide does not explain the numbers, and it does not describe how the policies are learned. Only the paper title says that the strategies are learned from data.

### Cutout

Cutout is a related regularizer. The slide lists it as "Cutout / Random Crop" in its list of regularizers, apart from "Data Augmentation" ([[Block 7 Slides]], p. 168):

- **Training.** Set random image regions to zero.
- **Testing.** Use the full image.
- It "works very well for small datasets like CIFAR". It is "less common for large datasets like ImageNet".
- Source on the slide: DeVries and Taylor, "Improved Regularization of Convolutional Neural Networks with Cutout", arXiv 2017.

Open point: the slide's name "Random Crop" for Cutout is not the same method as the "Random crops and scales" augmentation on p. 158. The deck does not explain the shared name.

### Evaluation

Randomness in training needs a fixed rule at evaluation. For augmentation, the slides say: "Use a fixed evaluation transform, or a predefined averaging protocol." They also say: "Decide the evaluation protocol before comparing models." (p. 165). The same slide gives the evaluation rules for [[Dropout]] and [[Batch Normalization]]. The ResNet multi-crop test above is one example of a predefined averaging protocol (p. 159). Synthesis: two models compare fairly only when they use the same evaluation transform. See [[Model Evaluation]] and ImageNet Large Scale Visual Recognition Challenge.

## Related

- [[Regularization]]: the weight penalties. Augmentation regularizes through the data.
- [[Overfitting and Underfitting]]
- [[Dropout]]
- [[Batch Normalization]]
- [[Data Preprocessing]]: deterministic transforms applied to all data. Augmentation applies random transforms in training only.
- Flower Classifier Running Example
- [[ResNet]]
- [[AlexNet]]
- [[Model Evaluation]]

## Sources

- [[Block 7 Slides]], pp. 154-165, 168
- [[F26-midterm-review-234p]], pp. 134-136
