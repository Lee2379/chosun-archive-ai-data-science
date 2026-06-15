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

## Training Behavior

The training curves showed decreasing localization, objectness, and classification losses across the fine-tuning process. This indicated that the model was learning FPC-specific visual patterns rather than relying on generic COCO categories.

![Training metrics](../assets/training-metrics.png)

## F1-Confidence Result

The fine-tuned YOLOv5_FPC model achieved:

- F1-confidence score: **0.97**
- Confidence threshold: **0.708**
- Target categories: `FPC_4x1` and `FPC_2x2`

![F1-confidence curve](../assets/f1-confidence.png)

The same project also produced representative full-page detection examples in my master's thesis work. The example below shows the fine-tuned YOLOv5_FPC detector localizing both `FPC_4x1` and `FPC_2x2` layouts in a historical newspaper page.

![Representative YOLOv5_FPC detection result](../assets/representative-fpc-detection-result.png)

## Interpretation

For this project, the F1-confidence score is especially important because the pipeline had to balance:

- Avoiding false positives that would pollute the curated archive dataset.
- Avoiding false negatives that would leave important historical cartoon objects undiscovered.

The selected threshold provided a strong balance between precision and recall for the two FPC categories.

## Baseline Comparison

The initial YOLOv5 model could not identify FPCs because the target object was outside the general COCO training domain.

![Baseline YOLOv5 failure](../assets/baseline-yolov5-failure.jpg)

The improvement came from domain-specific data collection, labeling, and fine-tuning rather than relying on a pretrained detector as-is.

## Practical Evaluation Lesson

This project demonstrates that AI model evaluation should be tied to the downstream business or research goal. The important question was not only "is the model accurate?" but also "does the model produce detections that can become a reliable database for public research, archive use, and new service value?"
