---
description: Transfer learning starts a model from representations learned on other (source) data instead of training from scratch; CSCI 566 sorts its methods by whether the source and target data have labels, and chooses how much of a pretrained network to train from the amount of target data and its similarity to the source.
aliases: [transfer learning with CNNs, frozen backbone, frozen backbone with a new head, frozen features, pretrained feature extractor, feature extraction, Stage 1 transfer, layer transfer, transfer strategy by dataset size and similarity, feature generality across CNN layers]
sources: ["[[Block 7 Slides]]", "[[F26-midterm-review-234p]]", "Block 8 Slides"]
---

## Definition

Training from scratch learns all representations from the target dataset. Transfer learning starts with representations learned from other data ([[Block 7 Slides]], p. 192). The deck calls this other data the source data and describes it as "not directly related to the task" ([[Block 7 Slides]], p. 211). "The source and target data determine how useful transfer is." ([[Block 7 Slides]], p. 192) [[F26-midterm-review-234p]] repeats the slide of p. 192 (p. 141). Its lead line gives the motive: "Our flower dataset is small. A pretrained model already encodes visual patterns." ([[F26-midterm-review-234p]], p. 141)

## Explanation

### Methods by labeled and unlabeled data

The deck sorts transfer methods by whether the source data and the target data have labels ([[Block 7 Slides]], pp. 211, 214, 219, 224). The table credits Hung-yi Lee (NTU) ([[Block 7 Slides]], p. 224).

| Target data | Source data labeled | Source data unlabeled |
|---|---|---|
| Labeled | [[Fine-Tuning]], Multitask Learning | (empty in the slides) |
| Unlabeled | Domain-Adversarial Training, zero-shot learning | (empty in the slides) |

- The slide gives a warning: "different terminology in different literature" ([[Block 7 Slides]], p. 211).
- The first version of the table names the labeled cell "Model Fine-tuning" ([[Block 7 Slides]], p. 211). Later versions say "Fine-tuning" ([[Block 7 Slides]], pp. 214, 219, 224).
- Open point: the unlabeled-source column is empty in every version of the table in this deck ([[Block 7 Slides]], pp. 211, 214, 219, 224). The slides do not say which methods go there.
- Block 8 shows label-free pretraining. An Autoencoder first trains to rebuild its input, and "Reconstruction pretraining needs no class labels" (Block 8 Slides, p. 98). Then a classifier goes on top of the encoder, and the encoder is fine-tuned with labels (Block 8 Slides, pp. 89-97). See Autoencoder Pretraining. Synthesis: this method starts from unlabeled data, so it may fit the empty column. Block 8 does not place it in the table.

### Stage 1: a frozen backbone with a new head

The running example is a small flower dataset ([[Block 7 Slides]], p. 192). See Flower Classifier Running Example. The first step is to "Replace the original label predictor with a three-class flower head." ([[Block 7 Slides]], p. 194)

- "Stage 1: backbone = the pretrained feature extractor. Keep it fixed." The early features and the later features are frozen. Only the classifier trains ([[Block 7 Slides]], p. 194).
- "Frozen features still participate in the forward pass." ([[Block 7 Slides]], p. 194)
- [[F26-midterm-review-234p]] repeats this slide (p. 142).
- The deck calls this setup "A low-cost baseline for the new labels." ([[Block 7 Slides]], p. 210)
- If the fixed features are insufficient, Stage 2 unfreezes selected layers ([[Block 7 Slides]], p. 201). See [[Fine-Tuning]].

### The CNN recipe

The deck gives a three-step recipe for a VGG-style CNN. The slides cite Donahue et al. (DeCAF, ICML 2014) and Razavian et al. (CVPR Workshops 2014) ([[Block 7 Slides]], pp. 197-200).

1. Train on ImageNet. The network ends in FC-4096, FC-4096, and FC-1000 ([[Block 7 Slides]], p. 197).
2. Small dataset with C classes: reinitialize the last layer as FC-C and train it. Freeze all layers below it ([[Block 7 Slides]], p. 198).
3. Bigger dataset: train FC-C and the two FC-4096 layers. Freeze the convolutional layers. "With bigger dataset, train more layers." ([[Block 7 Slides]], p. 200)

[[F26-midterm-review-234p]] repeats the slide of p. 200, which shows all three steps (p. 143). Step 3 also gives a learning-rate rule. See [[Fine-Tuning]].

### Generic and specific features

In the same VGG-style stack, the slide labels the early convolutional layers "More generic" and the top FC layers "More specific" ([[Block 7 Slides]], p. 202).

Synthesis: this explains the recipe. Generic lower-layer features are useful for many tasks, so they stay frozen. The specific top layers fit the source labels, so they are replaced or retrained first.

### How much of the model to train

The midterm review sums up the choice: "In transfer learning, you choose which pretrained layers stay frozen and which remain trainable." It lists this with initialization, normalization, and regularization as "Choices [that] shape how training behaves" ([[F26-midterm-review-234p]], p. 112).

The deck gives a guide by the amount of target data and its similarity to the source dataset ([[Block 7 Slides]], pp. 203-204):

| | Very similar dataset | Very different dataset |
|---|---|---|
| Very little data | Use a linear classifier on the top layer | "You're in trouble... Try linear classifier from different stages" |
| Quite a lot of data | Fine-tune a few layers | Fine-tune a larger number of layers |

"Data size, domain similarity and compute budget affect the choice." ([[Block 7 Slides]], p. 210) The same slide lists three options ([[Block 7 Slides]], p. 210):

| Option | Slide description |
|---|---|
| Frozen backbone + new head | "A low-cost baseline for the new labels." |
| Partial fine-tuning | "Adapt some features while keeping others fixed." |
| Full fine-tuning | "More flexibility, with greater training cost." |

**Rule.** "Compare these options using the same validation protocol." ([[Block 7 Slides]], p. 210)

The summary slide puts transfer inside the normal training loop. "The same classifier can start from random or pretrained weights." The starting point is a new model or loaded pretrained weights. The trainable part is the full model, selected layers, or a new head. Evaluation selects by validation performance and tests the final choice. "Initialization, optimization and transfer fit one training loop." ([[Block 7 Slides]], p. 226; repeated in [[F26-midterm-review-234p]], p. 145) See Model Selection and [[Model Evaluation]].

### Layer transfer

Layer transfer copies some parameters from a network trained on the source data into the target network ([[Block 7 Slides]], p. 213). The slide gives two options ([[Block 7 Slides]], p. 213):

1. Train only the remaining layers on the target data. This prevents overfitting.
2. Fine-tune the whole network, if there is sufficient data.

### When transfer fails

"A model trained on everyday photos may miss specialized visual features." ([[Block 7 Slides]], p. 215)

- Similar source and target: some shapes, textures, and object parts may transfer usefully ([[Block 7 Slides]], p. 215).
- Different source and target: microscopy or unusual sensors may need different representations ([[Block 7 Slides]], p. 215).

**Rule.** "Check target-domain performance before trusting reuse." ([[Block 7 Slides]], p. 215)

### Transfer is the norm

- "Transfer learning with CNNs is pervasive... (it's the norm, not an exception)" ([[Block 7 Slides]], p. 205).
- Object detection (Fast R-CNN) and image captioning (CNN + RNN) both use a CNN pretrained on ImageNet. The captioning model also uses word vectors pretrained with word2vec ([[Block 7 Slides]], pp. 206-207).
- "Architecture matters": the slide's MSCOCO object detection scores are 5 for DPM (pre-DL), 15 for Fast R-CNN (AlexNet), 19 for Fast R-CNN (VGG-16), 29 for Faster R-CNN (VGG-16), 36 for Faster R-CNN (ResNet-50), 39 for Faster R-CNN (ResNet-101), and 46 for Mask R-CNN FPN (ResNet-101). The chart comes from Girshick's ICCV 2017 tutorial ([[Block 7 Slides]], p. 208). The slide does not name the metric.
- A counterpoint: He et al. (ICCV 2019) find that training from scratch can work as well as training from a pretrained ImageNet model for object detection, but it takes 2-3x as long to train. They also find that collecting more data is better than fine-tuning on a related task ([[Block 7 Slides]], p. 209).

## Related

- [[Fine-Tuning]]
- Pretrained Visual Encoders
- [[Parameter-Efficient Fine-Tuning]]
- Domain-Adversarial Training
- Multitask Learning
- Autoencoder Pretraining (pretraining with no class labels)
- [[Convolutional Neural Networks (CNN)]]
- [[Overfitting and Underfitting]]
- Model Selection
- [[Model Evaluation]]
- Flower Classifier Running Example
- Sim-to-Real Transfer (another case of a model that fails when the domain changes)

## Sources

- [[Block 7 Slides]], pp. 192, 194, 197-198, 200-211, 213-215, 219, 224, 226
- [[F26-midterm-review-234p]], pp. 112, 141-145
- Block 8 Slides, pp. 89-98
