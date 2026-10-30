---
id: doc-0apr9a
type: topic
kind: entity
description: "The CSCI 566 Block 7 teaching example: a small three-class flower photo dataset (daisy, rose, tulip) that the lecture follows through training, generalization checks, model reuse, and hyperparameter search; the Block 8 deck reuses flower images, sorted by color, to teach generation."
tags: [machine-learning/cs566-deeplearning/cs566-course]
aliases: [Flower classification running example, Flower classifier, Course flower dataset, Flower dataset, Three-class flower task, "The Flower Classifier: A Complete Workflow", Training a Model That Works]
created: 2026-10-12T16:58:10
updated: 2026-10-19T18:32:33
refreshed: 2026-10-19T18:32:33
status: stable
sources: ["[[Block 7 Slides]]", "[[F26-midterm-review-234p]]", "Block 8 Slides"]
---

> [!entity] Entity
> 3 sources · refreshed 2026-10-19 · #machine-learning/cs566-deeplearning/cs566-course

## What it is

The flower classifier is the running example of the CSCI 566 Block 7 lecture "Training a Model That Works" ([[Block 7 Slides]], p. 11). A small dataset holds labeled photos of three flower species. A neural network maps a photo to daisy, rose, or tulip. "Success means classifying new photos correctly" (p. 12). The lecture uses the example to tie each training method to a problem that the class can see: "Each method answers a problem we can observe" (p. 11).

The slides mark the example "Course teaching example" or "Course schematic", with "Sources and assumptions in speaker notes" (pp. 11–12, 15). The numbers on its slides are illustrative, not measured results. The loss values are "illustrative predictions" (p. 13), the loss trace is "plausible" (p. 89), and the trial scores are "Toy GP and scores for teaching" (pp. 336–337). The slides do not name a public dataset.

## Facts

### The lecture plan

The lecture follows the project in three parts ([[Block 7 Slides]], p. 11):

| Part | Content |
| --- | --- |
| Make learning work | Data, activations, initialization and optimization |
| Check generalization | Training and validation curves, regularization |
| Reuse a trained model | Frozen features, fine-tuning and LoRA |

### The data and the training loop

- **Classes.** Daisy, rose, and tulip ([[Block 7 Slides]], p. 12).
- **Loss.** For one photo with the true label rose, the prediction daisy 0.60, rose 0.30, tulip 0.10 gives loss 1.20. The improved prediction 0.20, 0.70, 0.10 gives loss 0.36. Cross-entropy = −ln P(rose). "Higher probability for the correct label gives lower loss." (p. 13). See [[Loss Functions]].
- **Training split.** "Suppose the training split has 320 flower photos." A mini-batch holds 32 photos, and one update uses that group. "10 mini-batches cover 320 photos: one epoch." Shuffle the photos, then begin another epoch (p. 15).
- **Splits.** "Split the flower photos before fitting preprocessing or models." The training split fits model weights and preprocessing statistics. The validation split chooses settings and a checkpoint. The test split evaluates the final selected model. "Keep near-duplicate photos in the same split." (p. 17). See [[Data Preprocessing]] and [[Fit Preprocessing on Training Data Only]].

### Where the example returns

- **Batch normalization.** "The flower classifier may receive one new photo at a time." During evaluation, BatchNorm usually uses stored running statistics, so switch the model to evaluation mode ([[Block 7 Slides]], p. 34). See [[Batch Normalization]].
- **Learning rate.** A plausible training-loss trace for the flower classifier oscillates, then climbs over 8 epochs: "Large jumps can make training unstable." (p. 89). See [[Gradient-Based Optimizers]] and [[Learning Rate Schedules]].
- **Ensembles.** Three trained classifiers disagree on one flower photo. Average their class probabilities and choose the highest score. "Measure any accuracy gain together with serving cost." (p. 136).
- **Augmentation.** A mild crop or brightness change of a photo labeled daisy gives an altered photo that is still labeled daisy: "Choose transformations that preserve the task label." (p. 156). A rotated view may still show the same flower species, but a rotated 6 can resemble a 9 (p. 163). See [[Data Augmentation]].
- **Transfer.** "Our flower dataset is small. A pretrained model already encodes visual patterns." (p. 192). The first stage replaces the original label predictor with "a three-class flower head". The pretrained backbone stays frozen, and only the classifier trains (p. 194). [[F26-midterm-review-234p]] repeats both slides (pp. 141-142). See [[Transfer Learning]], [[Fine-Tuning]], and [[Pretrained Visual Encoders]].
- **Language models.** The lecture switches "from flower photos to the sentiment of flower-shop reviews". "The flowers arrived fresh." is Positive, and a wilted-flower complaint could be Negative. A pretrained Transformer supplies the text representations ([[Block 7 Slides]], p. 228).
- **Hyperparameter search.** For "the same flower task", one could try different learning rates, regularizers, and model choices: "AutoML organizes this repeated search." (p. 313). Validation performance chooses the learning rate and weight decay, and "The test score remains outside the search loop." (p. 326). In Bayesian Optimization, "One evaluation trains a flower classifier and measures validation accuracy." (p. 336). See [[AutoML]] and [[Test Set Contamination]].

### Three completed trials

The architecture, data split, and training budget stay fixed. Only the learning rate changes ([[Block 7 Slides]], p. 337):

| Trial | Learning rate | Validation accuracy |
| --- | --- | --- |
| A | 0.001 | 0.79 |
| B | 0.01 | 0.84 |
| C | 0.1 | 0.81 |

"Other settings are unmeasured." "Best measured so far: B, validation accuracy 0.84." The slide cites Snoek et al., NeurIPS 2012, and marks the scores as toy values for teaching (p. 337).

### The complete workflow

The slide "The Flower Classifier: A Complete Workflow" returns "to the original goal of classifying new photos" ([[Block 7 Slides]], p. 271):

1. **Establish a baseline.** Fix the split, metric, preprocessing and starting model.
2. **Diagnose and change.** Use learning curves to select a controlled intervention.
3. **Select and evaluate.** Choose by validation, then evaluate the final model.

"Explain which problem each training choice addresses." (p. 271).

The next slide says: "The training and adaptation workflow is complete." It lists optional research examples: LLM behavior ([[LLM Election Simulation]]), TOD systems ([[TOD]]), and AutoML, where "A later lecture extends our manual experiment loop." "These sections can be taught separately from the core workflow." (p. 272). But the deck itself holds AutoML slides that use the flower example (pp. 313, 326, 336–337). The slides do not say if the class covers them in Block 7 or in a later lecture.

### Advice for the course project

The last slide, "Training Choices to Carry Into Your Project", gives this advice ([[Block 7 Slides]], p. 400):

- "Use a sequence of experiments that you can explain and reproduce."
- Data and evaluation: "A sound split and metric make results interpretable."
- Training and adaptation: "Choose updates that fit the task and available budget."
- Next topics: "Use the current course schedule for upcoming lectures."
- "Keep the evidence for why each change helped."

Synthesis: the slide applies the flower workflow to the course project. Assignment 1 also asks students to train and evaluate an image classifier ([[CS566-DeepLearning]], § Assessments).

### Block 8: from classifying flowers to creating flowers

The Block 8 deck on Generative Models uses flowers as its teaching images. Its first content slide is "From Classifying Flowers to Creating Flowers" (Block 8 Slides, p. 3). The deck sorts the flowers by color: red, yellow, and white (pp. 3–4). These are not the daisy, rose, and tulip classes of Block 7. The slides mark the images "Flower images: generated teaching illustrations." (p. 3). Synthesis: the deck continues the flower theme, but it does not name or reuse the Block 7 dataset.

- **Classify or generate.** A classifier scores a known rose: red 0.8, yellow 0.15, white 0.05. A generator turns a random code (0.3, −0.8) into "A new sample, rather than a class label" (Block 8 Slides, p. 3).
- **A distribution.** A toy dataset of 10 flowers has 6 red, 3 yellow, and 1 white flower, so the probabilities are 0.6, 0.3, and 0.1 (p. 4).
- **A hidden variable.** A hidden style A or B explains the color of a flower. "Seeing red raises P(A) from 0.5 to 0.75" (p. 5).
- **One generator, many samples.** The same G maps $z_1 = (0.3, -0.8)$ to a red rose and $z_2 = (-0.2, 0.6)$ to a yellow flower (p. 7).
- **GAN training.** "D learns to tell real flowers from generated ones, then G learns to make generated flowers that D judges as real." (p. 22). See Generative Adversarial Network.
- **A condition.** The class $y$ = yellow stays fixed, and two random inputs give two different yellow flowers (p. 53). See Conditional GAN.
- **Mode collapse.** The real data is 40% red rose, 35% yellow flower, and 25% white flower. A collapsed generator makes "100% red roses; 0% other types" (p. 61). See Mode Collapse.
- **VAE encoder.** The same encoder gives a rose $\mu = 2, \sigma = 0.5$ and a yellow flower $\mu = -1, \sigma = 0.5$ (p. 123). See Variational Autoencoder.

## Related

- [[CS566-DeepLearning]]: the course. Yue Zhao: the instructor.
- [[Transfer Learning]], [[Fine-Tuning]], [[LoRA]], [[Pretrained Visual Encoders]]
- [[Data Preprocessing]], [[Fit Preprocessing on Training Data Only]], [[Data Augmentation]], [[Batch Normalization]], [[Gradient-Based Optimizers]], [[Learning Rate Schedules]], [[Loss Functions]]
- [[AutoML]], Bayesian Optimization, [[Model Selection]], [[Test Set Contamination]]
- Generative Models, Generative Adversarial Network, Conditional GAN, Mode Collapse, Variational Autoencoder: the Block 8 topics that use flower images
- [[Road Delay GNN Example]]: the running example of the Block 6 deck (synthesis: the same teaching device)

## Sources

- [[Block 7 Slides]], pp. 11–13, 15, 17, 34, 89, 136, 156, 163, 192, 194, 228, 271–272, 313, 326, 336–337, 400
- [[F26-midterm-review-234p]], pp. 141-142
- Block 8 Slides, pp. 3–5, 7, 22, 53, 61, 123
