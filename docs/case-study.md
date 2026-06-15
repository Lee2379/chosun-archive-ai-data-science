# Case Study: From Historical Archive Images to Public Cultural Data

## Executive Summary

This project was conducted during my master's program at KAIST as an R&D industry collaboration with Chosun Ilbo Media Institute. It converted a large unstructured historical newspaper archive into a searchable four-panel cartoon data asset using a custom YOLOv5 object detector.

The key professional value is end-to-end business, data science, and AI execution, not only model training. I took an ambiguous archive-content problem and moved it through the full delivery chain:

1. Define a real archive-search problem.
2. Build task-specific training data.
3. Fine-tune and evaluate a computer vision model.
4. Run large-scale detection over 47,777 images.
5. Curate the output into metadata and database-ready records.
6. Build a public Google Colab detector script for wider reuse.
7. Publish the work as a first-author English journal paper.
8. Connect the result to new public archive service value.

## Business Problem

The Chosun Ilbo News Library contains digitized historical newspaper pages from 1920 to 1940. These pages include culturally and commercially meaningful archive content, but the content is embedded inside full-page scans with dense text, advertisements, and historical document noise.

Demand for cartoon content has been increasing across East Asia, creating a potential new business and service opportunity for archive owners. Chosun Ilbo wanted to discover four-panel cartoons from its large historical database, but the starting point was unclear: the cartoons were not stored as clean structured records, and their visual format made detection difficult in noisy, unstructured newspaper scans.

Manual discovery is slow, expensive, and difficult to scale. From a business perspective, the problem was how to turn hidden content in a legacy media archive into searchable, reusable data that could support public service value, new service creation, and downstream research use. The project therefore reframed the archive-search task as a business, data science, and AI problem: detect the four-panel cartoon regions directly from scanned newspaper images and curate the results into URL-based records.

## Solution

The solution was an end-to-end object detection and data curation pipeline:

- Collect candidate FPC training images.
- Label cartoon regions with bounding boxes.
- Convert labels into YOLO-compatible format.
- Fine-tune YOLOv5 on the target object class.
- Evaluate detection quality using standard object detection metrics.
- Apply the trained model to the full archive image set.
- Curate detected results into structured metadata and URLs.
- Provide a Google Colab detector script that lets users upload image ZIP files and download detected FPC results.
- Publish the data and methodology for reuse.

## Delivery Outcome

The final pipeline processed 47,777 JPG images and identified 1,040 FPC objects across 1,035 image files. The results were published in Journal of Open Humanities Data and made available through public data references and archive-service materials.

The project also included a YOLOv5_FPC Detector script on Google Colab. This lowered the barrier for other users by handling dependency installation, model weight download, ZIP upload, detection execution, and output packaging in a browser-based environment.

## Why It Is Relevant for Data Science and AI Developer Roles

This project demonstrates the ability to connect modeling work to a real data product:

- Translate a stakeholder problem into a machine learning workflow.
- Work with messy, historically noisy, real-world images.
- Build a model where generic pretrained detection fails.
- Evaluate the model with transparent metrics.
- Operationalize inference over a large archive.
- Structure ML outputs into reusable data assets.
- Communicate the work through a peer-reviewed publication.

## Portfolio Positioning

For hiring review, this project should be read as a research-to-production case study:

- Research credibility: first-author English journal publication.
- Industry credibility: KAIST master's R&D industry collaboration with Chosun Ilbo Media Institute.
- Data credibility: large-scale archive processing and metadata curation.
- Engineering credibility: model fine-tuning, batch inference, and evaluation.
- Impact credibility: public dataset and public archive-service connection.
