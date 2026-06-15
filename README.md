# YOLOv5_FPC: Four-Panel Cartoon Detection in the Chosun Ilbo Archive

> First-author industrial AI project demonstrating end-to-end ownership: I turned an ambiguous big-data archive problem into a concrete AI development workflow, then delivered a working object detection pipeline, curated dataset, reusable detector script, academic publication, and public service impact.

[![JOHD Paper](https://img.shields.io/badge/JOHD-First%20Author%20Paper-bb2d2b)](https://openhumanitiesdata.metajnl.com/articles/10.5334/johd.205)
[![Journal Indexing](https://img.shields.io/badge/Indexed-ESCI%20%7C%20Scopus-2f6f9f)](https://openhumanitiesdata.metajnl.com/about)
[![Public Service](https://img.shields.io/badge/Public%20Archive-Chosun%20Ilbo%20News%20Library-9a7a18)](https://archive.chosun.com/cartoon/toon_comics.html)
[![Field](https://img.shields.io/badge/Field-Computer%20Vision%20%7C%20Data%20Science-333333)](#project-at-a-glance)

![Published paper title page](assets/paper-title.jpg)

## Project at a Glance

This repository presents a portfolio-grade case study of my first-author English journal publication and the underlying industry AI project.

**Lee, S., Kim, B., & Jun, B. G. (2024). Automatic Detection of Four-Panel Cartoon in Large-Scale Korean Digitized Newspapers using Deep Learning. Journal of Open Humanities Data, 10:36. DOI: [10.5334/johd.205](https://doi.org/10.5334/johd.205).**

The project was conducted as an industry collaboration with **Chosun Ilbo Media Institute**. I owned the work end-to-end: clarifying an initially ambiguous business/research problem, converting it into a computer vision and big-data workflow, collecting and labeling training data, fine-tuning YOLOv5, evaluating the detector, running large-scale detection, curating the metadata/database, building a reusable detector script, and communicating the result through a first-author publication.

> **日本語要約:** 朝鮮日報メディア研究所との産業連携において、曖昧なビジネス・研究課題をAI開発課題として具体化し、データ構築、モデル開発、評価、大規模推論、データベース化、再利用可能な検出ツール、論文発表までをend-to-endで推進したプロジェクトです。

| Area | Result |
| --- | --- |
| Publication | First-author English journal paper in Journal of Open Humanities Data |
| Indexing | JOHD is indexed in Web of Science Emerging Sources Citation Index (ESCI) and Scopus |
| Industry partner | Chosun Ilbo Media Institute |
| Archive scope | 47,777 digitized Chosun Ilbo newspaper JPG images from 1920-1940 |
| Detection output | 1,040 four-panel cartoon objects in 1,035 image files |
| Model result | F1-confidence score of 0.97 at confidence threshold 0.708 |
| Public impact | Research dataset and detection results connected to Chosun Ilbo's public archive service |

## Professional Positioning

This project is best understood as an **ambiguous-problem-to-deliverable AI development case study**. The starting point was not a clean benchmark dataset or a predefined Kaggle-style task. It was a broad industry and cultural archive challenge: how to discover historically valuable four-panel cartoons from a massive set of digitized newspaper pages and turn the output into reusable data.

I structured the problem into sequential technical workstreams: archive data extraction, labeled dataset construction, object detection model adaptation, quantitative evaluation, large-scale inference, detected-result curation, public tool development, and publication/service handoff.

> **日本語での位置づけ:** 曖昧な産業課題を、データ収集・AIモデル開発・評価・大規模処理・成果物公開までの実行可能なプロジェクトに分解し、最終成果まで責任を持って推進した事例です。

## Why This Project Matters

Historical newspaper archives contain valuable visual materials, but they are difficult to search when the content is stored as scanned image pages. In this project, the target object was the Korean four-panel cartoon (FPC), especially the "Meongteongguri" series in Chosun Ilbo's digitized archive.

The practical challenge was not just training a model. The real problem was building a pipeline that could transform unstructured archive images into structured, searchable cultural data.

> **日本語要約:** 単なるモデル学習ではなく、非構造な新聞画像を検索・再利用可能なデータ資産へ変換することが本プロジェクトの中心課題でした。

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

> **担当範囲:** 曖昧な課題の具体化、学習データ作成、ラベリング、YOLOv5 fine-tuning、評価、大規模検出、メタデータ/DB構築、検出スクリプト開発、論文執筆・可視化までを一貫して担当しました。

![Author contribution statement](assets/author-contribution.jpg)

## End-to-End Delivery Flow

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

> **技術課題:** 一般的なCOCO事前学習モデルでは検出できない対象に対して、歴史新聞画像に特化したデータセットとfine-tuningで対応しました。

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

> **評価観点:** 数値指標だけでなく、実際の新聞紙面上で対象物を正しく局所化できるかを確認しました。

![Representative YOLOv5_FPC detection result](assets/representative-fpc-detection-result.png)

## Data and Database Curation

The data work had two separate stages: first, building the source archive image collection; second, curating the model-detected FPC results.

At the beginning of the project, I extracted and organized the source metadata and image URLs used to collect the **47,777 JPG files** from the Chosun Ilbo News Library. This spreadsheet represents the input archive collection stage, not the final detection result.

> **データ基盤:** 47,777件の画像URLとメタデータを整理し、大規模推論に利用できる入力データ基盤を構築しました。

![Source metadata used to collect 47,777 archive JPG files](assets/metadata-database.jpg)

After model evaluation, I applied the detector to the archive at scale. The pipeline identified **1,040 FPC objects** in **1,035 files**, and the detected outputs were curated into result files with direct URLs to the discovered FPC-containing newspaper images.

> **成果データ:** 検出結果はURL付きの結果ファイルとして整理し、研究者やサービス側が再利用できる形にしました。

![Detected FPC URL result file](assets/detected-fpc-url-results.png)

## Public YOLOv5_FPC Detector Script

As part of the paper, I also developed a **YOLOv5_FPC Detector script on Google Colab** so that other users could upload local image ZIP files and detect four-panel cartoons without setting up a local GPU environment.

The script installs YOLOv5 dependencies, downloads the trained YOLOv5_FPC weights, accepts a ZIP file upload, runs detection, saves label outputs, packages the detected images, and returns a downloadable ZIP file.

> **再利用性:** Google Colab上で動作する検出スクリプトを用意し、ローカルGPU環境がないユーザーでもFPC検出を試せるようにしました。

![Google Colab detector setup and weight download](assets/colab-detector-setup.png)

![Google Colab detector upload and inference process](assets/colab-detector-upload.png)

![Google Colab detector output packaging and download](assets/colab-detector-download.png)

## Publication and Public Service Impact

This project was published as a first-author paper in the **Journal of Open Humanities Data**, an English journal indexed in **ESCI** and **Scopus**. The paper and datasets make the methodology and discovered data reusable for cultural heritage data infrastructure and large-scale document AI.

The work also contributed to the public-facing Chosun Ilbo News Library experience for "Meongteongguri" four-panel cartoons.

> **実社会での成果:** 研究成果は公開データセット、論文、そして朝鮮日報ニュースライブラリの公開サービスへと接続されました。

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
