# YOLOv5_FPC: Four-Panel Cartoon Detection in the Chosun Ilbo Archive

> First-author industrial AI project with end-to-end ownership, from problem definition and dataset construction to YOLOv5 fine-tuning, large-scale detection, database curation, publication, and real-world service impact.

[![JOHD Paper](https://img.shields.io/badge/JOHD-First%20Author%20Paper-bb2d2b)](https://openhumanitiesdata.metajnl.com/articles/10.5334/johd.205)
[![Journal Indexing](https://img.shields.io/badge/Indexed-ESCI%20%7C%20Scopus-2f6f9f)](https://openhumanitiesdata.metajnl.com/about)
[![Public Service](https://img.shields.io/badge/Public%20Archive-Chosun%20Ilbo%20News%20Library-9a7a18)](https://archive.chosun.com/cartoon/toon_comics.html)
[![Field](https://img.shields.io/badge/Field-Computer%20Vision%20%7C%20Data%20Science-333333)](#project-at-a-glance)

![Published paper title page](assets/paper-title.jpg)

## Project at a Glance

This repository presents a portfolio-grade case study of my first-author English journal publication:

**Lee, S., Kim, B., & Jun, B. G. (2024). Automatic Detection of Four-Panel Cartoon in Large-Scale Korean Digitized Newspapers using Deep Learning. Journal of Open Humanities Data, 10:36. DOI: [10.5334/johd.205](https://doi.org/10.5334/johd.205).**

The project was conducted as an industry collaboration with **Chosun Ilbo Media Institute**. I owned the work end-to-end: defining the problem, collecting and labeling training data, fine-tuning YOLOv5, evaluating the detector, running large-scale detection, curating the metadata/database, and communicating the result through a first-author publication.

| Area | Result |
| --- | --- |
| Publication | First-author English journal paper in Journal of Open Humanities Data |
| Indexing | JOHD is indexed in Web of Science Emerging Sources Citation Index (ESCI) and Scopus |
| Industry partner | Chosun Ilbo Media Institute |
| Archive scope | 47,777 digitized Chosun Ilbo newspaper JPG images from 1920-1940 |
| Detection output | 1,040 four-panel cartoon objects in 1,035 image files |
| Model result | F1-confidence score of 0.97 at confidence threshold 0.708 |
| Public impact | Research dataset and detection results connected to Chosun Ilbo's public archive service |

## Why This Project Matters

Historical newspaper archives contain valuable visual materials, but they are difficult to search when the content is stored as scanned image pages. In this project, the target object was the Korean four-panel cartoon (FPC), especially the "Meongteongguri" series in Chosun Ilbo's digitized archive.

The practical challenge was not just training a model. The real problem was building a pipeline that could transform unstructured archive images into structured, searchable cultural data.

![47,777 archive images collected from Chosun Ilbo News Library](assets/archive-scale-47777-images.jpg)

## My End-to-End Ownership

I led the technical and analytical work across the full lifecycle:

- Defined the detection problem with the research and industry context.
- Collected and reviewed training data for four-panel cartoon detection.
- Built bounding-box labels and prepared YOLO-format datasets.
- Collected and analyzed large-scale Chosun Ilbo archive image metadata.
- Fine-tuned YOLOv5 for FPC-specific object detection.
- Evaluated model behavior using precision, recall, mAP, loss curves, and F1-confidence.
- Ran batch detection over 47,777 historical newspaper images.
- Curated detected results into a metadata/database format.
- Contributed writing, methodology, software, formal analysis, visualization, and review/editing as first author.
- Helped turn research output into reusable public data and visible archive-service impact.

![Author contribution statement](assets/author-contribution.jpg)

## System Workflow

<img src="assets/system-workflow.svg" alt="End-to-end YOLOv5_FPC workflow from archive image collection to detector, curated data, publication, and public service impact" width="100%">

## Technical Challenge

The initial YOLOv5 model was trained on general-purpose COCO categories. It did not understand the target object and produced irrelevant detections on historical newspaper pages.

![Initial YOLOv5 failure on historical newspaper page](assets/baseline-yolov5-failure.jpg)

To solve this, I fine-tuned YOLOv5 on FPC-specific data. The model needed to handle:

- Degraded historical scans.
- Dense Korean/Japanese text layouts.
- Small cartoon objects embedded inside full newspaper pages.
- Different FPC layouts such as 4x1 and 2x2.
- Large-scale detection where manual review alone would be costly.

## Model Development and Evaluation

The model was fine-tuned with an FPC-specific dataset split into training, validation, and testing sets. The paper reports a split of **113 training images**, **24 validation images**, and **24 testing images**.

The training curves showed improved localization, objectness, and classification behavior over 200 epochs.

![Training and validation metrics](assets/training-metrics.png)

The fine-tuned detector achieved a strong F1-confidence result:

- **F1-score:** 0.97
- **Confidence threshold:** 0.708
- **Classes:** 4x1 and 2x2 four-panel cartoon categories

![F1-confidence curve](assets/f1-confidence.png)

The following representative detection result, produced within the same project and included in my master's thesis work, shows the fine-tuned YOLOv5_FPC model detecting both 4x1 and 2x2 FPC layouts on a full historical newspaper page.

![Representative YOLOv5_FPC detection result](assets/representative-fpc-detection-result.png)

## Data and Database Curation

The data work had two separate stages: first, building the source archive image collection; second, curating the model-detected FPC results.

At the beginning of the project, I extracted and organized the source metadata and image URLs used to collect the **47,777 JPG files** from the Chosun Ilbo News Library. This spreadsheet represents the input archive collection stage, not the final detection result.

![Source metadata used to collect 47,777 archive JPG files](assets/metadata-database.jpg)

After model evaluation, I applied the detector to the archive at scale. The pipeline identified **1,040 FPC objects** in **1,035 files**, and the detected outputs were curated into result files with direct URLs to the discovered FPC-containing newspaper images.

![Detected FPC URL result file](assets/detected-fpc-url-results.png)

## Public YOLOv5_FPC Detector Script

As part of the paper, I also developed a **YOLOv5_FPC Detector script on Google Colab** so that other users could upload local image ZIP files and detect four-panel cartoons without setting up a local GPU environment.

The script installs YOLOv5 dependencies, downloads the trained YOLOv5_FPC weights, accepts a ZIP file upload, runs detection, saves label outputs, packages the detected images, and returns a downloadable ZIP file.

![Google Colab detector setup and weight download](assets/colab-detector-setup.png)

![Google Colab detector upload and inference process](assets/colab-detector-upload.png)

![Google Colab detector output packaging and download](assets/colab-detector-download.png)

## Publication and Public Service Impact

This project was published as a first-author paper in the **Journal of Open Humanities Data**, an English journal indexed in **ESCI** and **Scopus**. The paper and datasets make the methodology and discovered data reusable for cultural heritage data infrastructure and large-scale document AI.

The work also contributed to the public-facing Chosun Ilbo News Library experience for "Meongteongguri" four-panel cartoons.

![Chosun Ilbo public archive overview](assets/chosun-service-overview.jpg)

![Chosun Ilbo public archive list](assets/chosun-service-list.jpg)

![Chosun Ilbo public archive detail page](assets/chosun-service-detail.jpg)

## Public Data and Copyright Note

This repository is a public portfolio case study built from already published research outputs, public service screenshots, and publicly accessible references. It does **not** redistribute a private source archive dump, proprietary internal materials, or unpublished collaboration files.

The research was conducted with Chosun Ilbo Media Institute, and the relevant publication, dataset references, and public archive service are already available online. The repository focuses on explaining my role, methodology, evaluation, and impact for professional portfolio review.

## Links

- Paper: [Journal of Open Humanities Data article](https://openhumanitiesdata.metajnl.com/articles/10.5334/johd.205)
- Journal indexing: [JOHD About page](https://openhumanitiesdata.metajnl.com/about)
- Public service: [Chosun Ilbo News Library - Meongteongguri four-panel cartoons](https://archive.chosun.com/cartoon/toon_comics.html)
- Metadata dataset DOI: [10.7910/DVN/DFVZWE](https://doi.org/10.7910/DVN/DFVZWE)
- Extracted FPC dataset DOI: [10.7910/DVN/KTF1HP](https://doi.org/10.7910/DVN/KTF1HP)
- YOLOv5_FPC Detector Colab script: [Google Colab](https://colab.research.google.com/drive/1qnCKaUGUTF5vSRdPc7DI6y7b05P8yuQ?usp=sharing)

## Detailed Documentation

- [Case study](docs/case-study.md)
- [Methodology](docs/methodology.md)
- [Model evaluation](docs/model-evaluation.md)
- [Publication and impact](docs/publication-and-impact.md)

## Japanese Summary

For Japanese hiring reviewers, see [README.ja.md](README.ja.md).
