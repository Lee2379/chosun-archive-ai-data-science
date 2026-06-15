# Public-Safe Detector Template

This folder contains a lightweight Python template that mirrors the public YOLOv5_FPC detector workflow without redistributing private archive dumps, proprietary internal materials, or model weights.

Example:

```bash
python src/yolov5_fpc_inference_demo.py \
  --yolov5-dir /path/to/yolov5 \
  --weights /path/to/yolov5_fpc.pt \
  --source /path/to/archive-images \
  --output runs/fpc-detection \
  --conf 0.60 \
  --save-txt
```

The original research also provided a Google Colab detector script for browser-based use.
