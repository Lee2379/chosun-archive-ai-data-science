# AI Model Evaluation

## AI Model Evaluation Goal

The model needed to be accurate enough to support large-scale discovery of four-panel cartoons from noisy historical newspaper images. Because the downstream task involved data curation, balanced precision and recall were important.

## Metrics Used

The evaluation considered standard object detection metrics:

- Precision: correctness of positive detections.
- Recall: ability to find target objects.
- mAP@0.5: mean average precision at IoU threshold 0.5.
- mAP@0.5:0.95: average mAP over multiple IoU thresholds.
- F1-score: harmonic mean of precision and recall.
- Training and validation losses: box, objectness, and classification losses.

## Mathematical Foundation

The detector was evaluated as an object detection model, where the learning objective combines bounding-box localization, object confidence, no-object confidence, and class prediction terms. At a conceptual level, the classical YOLO loss decomposes the objective as:

$$
\begin{aligned}
\mathcal{L} =
&\lambda_{\text{coord}} \sum_{i=0}^{S^2} \sum_{j=0}^{B} \mathbb{1}_{ij}^{\text{obj}}
\left[(x_i-\hat{x}_i)^2 + (y_i-\hat{y}_i)^2\right] \\
&+ \lambda_{\text{coord}} \sum_{i=0}^{S^2} \sum_{j=0}^{B} \mathbb{1}_{ij}^{\text{obj}}
\left[(\sqrt{w_i}-\sqrt{\hat{w}_i})^2 + (\sqrt{h_i}-\sqrt{\hat{h}_i})^2\right] \\
&+ \sum_{i=0}^{S^2} \sum_{j=0}^{B} \mathbb{1}_{ij}^{\text{obj}}(C_i-\hat{C}_i)^2 \\
&+ \lambda_{\text{noobj}} \sum_{i=0}^{S^2} \sum_{j=0}^{B} \mathbb{1}_{ij}^{\text{noobj}}(C_i-\hat{C}_i)^2 \\
&+ \sum_{i=0}^{S^2} \mathbb{1}_{i}^{\text{obj}} \sum_{c \in \text{classes}} (p_i(c)-\hat{p}_i(c))^2
\end{aligned}
$$

YOLOv5 uses updated implementation details for bounding-box, objectness, and classification losses, but this decomposition explains the mathematical foundation behind the detection task: the model had to localize FPC regions accurately on dense newspaper pages, avoid false detections in text-heavy areas, and distinguish FPC layout categories such as `FPC_4x1` and `FPC_2x2`.

### Notation

| Symbol | Meaning |
| --- | --- |
| $S^2$ | Number of grid cells |
| $B$ | Number of bounding boxes per grid cell |
| $\mathbb{1}_{ij}^{\text{obj}}$ | 1 if the $j$-th bounding box in cell $i$ is responsible for an object; otherwise 0 |
| $\mathbb{1}_{ij}^{\text{noobj}}$ | 1 if the $j$-th bounding box in cell $i$ is not responsible for an object; otherwise 0 |
| $x_i, y_i$ | Ground-truth bounding-box center coordinates |
| $\hat{x}_i, \hat{y}_i$ | Predicted bounding-box center coordinates |
| $w_i, h_i$ | Ground-truth bounding-box width and height |
| $\hat{w}_i, \hat{h}_i$ | Predicted bounding-box width and height |
| $C_i$ | Ground-truth confidence score |
| $\hat{C}_i$ | Predicted confidence score |
| $p_i(c)$ | Ground-truth conditional probability for class $c$ |
| $\hat{p}_i(c)$ | Predicted conditional probability for class $c$ |
| $\lambda_{\text{coord}}$ | Coordinate loss weight, commonly set to 5 |
| $\lambda_{\text{noobj}}$ | No-object confidence loss weight, commonly set to 0.5 |

The core evaluation metrics used to interpret detection quality were:

$$
\text{Precision} = \frac{\text{True Positive}}{\text{True Positive} + \text{False Positive}}
$$

$$
\text{Recall} = \frac{\text{True Positive}}{\text{True Positive} + \text{False Negative}}
$$

$$
\text{F1-score} = \frac{2 \cdot \text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}
$$

## Training Behavior

The training curves showed decreasing localization, objectness, and classification losses across the fine-tuning process. This indicated that the model was learning FPC-specific visual patterns rather than relying on generic COCO categories.

![Training metrics](../assets/training-metrics.png)

## F1-Confidence Result

The fine-tuned YOLOv5_FPC model achieved:

- F1-confidence score: **0.97**
- Confidence threshold: **0.708**
- Target categories: `FPC_4x1` and `FPC_2x2`

![F1-confidence curve](../assets/f1-confidence.png)

The same project also produced representative full-page detection examples. The example below shows the fine-tuned YOLOv5_FPC detector localizing both `FPC_4x1` and `FPC_2x2` layouts in a historical newspaper page.

![Representative YOLOv5_FPC detection result](../assets/representative-fpc-detection-result.png)

The detector was also tested on damaged and partially missing historical newspaper pages, demonstrating practical robustness for real archive material.

![YOLOv5_FPC detection on a damaged historical newspaper page](../assets/damaged-newspaper-fpc-detection-result.png)

## Interpretation

For this project, the F1-confidence score is especially important because the pipeline had to balance:

- Avoiding false positives that would pollute the curated archive dataset.
- Avoiding false negatives that would leave important historical cartoon objects undiscovered.

The selected threshold provided a strong balance between precision and recall for the two FPC categories.

## Baseline Comparison

The initial YOLOv5 model could not identify FPCs because the target object was outside the general COCO training domain.

![Baseline YOLOv5 failure](../assets/baseline-yolov5-failure.jpg)

The improvement came from self-collected FPC training data, labeling, and YOLOv5 fine-tuning rather than relying on a pretrained detector as-is.

## Practical Evaluation Lesson

This project demonstrates that AI model evaluation should be tied to the downstream business or research goal. The important question was not only "is the model accurate?" but also "does the model produce detections that can become a reliable database for public research, archive use, and new service value?"
