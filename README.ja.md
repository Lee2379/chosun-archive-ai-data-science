# YOLOv5_FPC: 朝鮮日報アーカイブにおける四コマ漫画検出プロジェクト

> 新聞アーカイブに埋もれていた四コマ漫画を検出・構造化し、研究データセットおよび実サービスにつなげた産業連携AIプロジェクト。

[English README](README.md)

## プロジェクト概要

本リポジトリは、私が第一著者として英文学術誌 **Journal of Open Humanities Data** に発表した研究を、データサイエンティスト / AI Developer 向けのポートフォリオとして整理したものです。

対象は、1920年から1940年までの朝鮮日報デジタル新聞アーカイブです。大量の新聞画像の中から、四コマ漫画を物体検出モデルで自動抽出し、検索・閲覧可能なデータベースとして活用できる形に構造化しました。

## 主要成果

| 項目 | 内容 |
| --- | --- |
| 論文 | Journal of Open Humanities Data, 第一著者, 2024 |
| ジャーナル | Web of Science ESCI / Scopus indexed English journal |
| 産業連携 | Chosun Ilbo Media Institute |
| 対象データ | 1920-1940年の新聞画像 47,777 JPG files |
| 検出結果 | 1,035ファイル内に1,040個の四コマ漫画オブジェクト |
| モデル評価 | F1-confidence 0.97 at threshold 0.708 |
| 実社会での成果 | 公開研究データセットおよび朝鮮日報ニュースライブラリの実サービスに接続 |

![Public archive service](assets/chosun-service-overview.jpg)

## 担当範囲

このプロジェクトでは、単なるモデル学習だけではなく、問題定義から公開成果物まで end-to-end で担当しました。

- 研究・産業課題の問題定義
- 学習データの収集
- 画像ラベリングとYOLO形式データセット構築
- 大規模新聞アーカイブのデータ収集・分析
- YOLOv5のfine-tuning
- precision / recall / mAP / F1によるモデル評価
- 47,777画像へのbatch detection
- 検出結果のメタデータ化およびデータベース構築
- Google Colab上で動作するYOLOv5_FPC Detector Scriptの開発
- 第一著者としての論文執筆、可視化、方法論整理
- 公開データセットおよび実サービスにつながる成果整理

## 技術スタック

- Python
- YOLOv5
- Object Detection
- Bounding-box Annotation
- Data Curation
- Metadata Design
- Large-scale Batch Inference
- Model Evaluation
- Google Colab Detector Script
- Cultural Heritage Data Infrastructure

## AI Developer / Data Scientist として示せる力

このプロジェクトは、企業で必要とされる以下の能力を示しています。

- ビジネス・研究課題を機械学習タスクに落とし込む力
- 小規模な教師データから実用的な検出モデルを構築する力
- モデル評価を数値と可視化の両面で説明する力
- 大規模データに対してbatch inferenceを実行する力
- 検出結果をサービスやデータベースで使える形に構造化する力
- 産業パートナーと協業し、論文・公開データ・実サービスまで成果を届ける力

## 公開データと著作権に関する注記

本リポジトリは、すでに公開された論文、公開データセット、公開サービス画面、および研究成果に基づくポートフォリオです。非公開の内部資料、未公開データ、または権利上問題のある原本アーカイブを再配布するものではありません。

本研究は Chosun Ilbo Media Institute との産業連携として実施され、関連する論文・データセット・公開サービスはオンラインで確認できます。

## 論文・サービスリンク

- 論文: [Journal of Open Humanities Data](https://openhumanitiesdata.metajnl.com/articles/10.5334/johd.205)
- ジャーナル情報: [JOHD About](https://openhumanitiesdata.metajnl.com/about)
- 実サービス: [朝鮮日報ニュースライブラリ - 멍텅구리 네컷만화](https://archive.chosun.com/cartoon/toon_comics.html)
- Metadata dataset DOI: [10.7910/DVN/DFVZWE](https://doi.org/10.7910/DVN/DFVZWE)
- Extracted FPC dataset DOI: [10.7910/DVN/KTF1HP](https://doi.org/10.7910/DVN/KTF1HP)
