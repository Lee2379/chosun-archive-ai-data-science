"""Public-safe YOLOv5_FPC inference demo.

This script mirrors the public Google Colab detector flow described in the
portfolio without bundling private archive dumps, proprietary collaboration
materials, or model weights. It expects the user to provide a local YOLOv5
checkout, a permitted YOLOv5_FPC weight file, and an input image directory.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run YOLOv5_FPC detection on newspaper archive images."
    )
    parser.add_argument(
        "--yolov5-dir",
        type=Path,
        required=True,
        help="Path to a local YOLOv5 checkout containing detect.py.",
    )
    parser.add_argument(
        "--weights",
        type=Path,
        required=True,
        help="Path to a permitted YOLOv5_FPC model weight file.",
    )
    parser.add_argument(
        "--source",
        type=Path,
        required=True,
        help="Input image, directory, or ZIP-extracted image folder.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("runs/fpc-detection"),
        help="Output directory for detection results.",
    )
    parser.add_argument(
        "--conf",
        type=float,
        default=0.60,
        help="Detection confidence threshold.",
    )
    parser.add_argument(
        "--imgsz",
        type=int,
        default=640,
        help="YOLOv5 inference image size.",
    )
    parser.add_argument(
        "--save-txt",
        action="store_true",
        help="Save YOLO-format label outputs.",
    )
    return parser.parse_args()


def validate_paths(args: argparse.Namespace) -> Path:
    detect_py = args.yolov5_dir / "detect.py"
    missing = [
        str(path)
        for path in [detect_py, args.weights, args.source]
        if not path.exists()
    ]
    if missing:
        raise FileNotFoundError("Missing required path(s): " + ", ".join(missing))
    return detect_py


def run_detection(args: argparse.Namespace, detect_py: Path) -> None:
    args.output.mkdir(parents=True, exist_ok=True)
    command = [
        sys.executable,
        str(detect_py),
        "--weights",
        str(args.weights),
        "--source",
        str(args.source),
        "--conf",
        str(args.conf),
        "--imgsz",
        str(args.imgsz),
        "--project",
        str(args.output),
        "--name",
        "result_images",
        "--exist-ok",
    ]
    if args.save_txt:
        command.append("--save-txt")
    subprocess.run(command, check=True)


def package_results(output_dir: Path) -> Path | None:
    result_dir = output_dir / "result_images"
    if not result_dir.exists():
        return None

    archive_base = output_dir / "FPC_model_detected_images"
    return Path(shutil.make_archive(str(archive_base), "zip", result_dir))


def main() -> None:
    args = parse_args()
    detect_py = validate_paths(args)
    run_detection(args, detect_py)
    archive = package_results(args.output)

    if archive is None:
        print(f"Detection finished. Results are under: {args.output}")
    else:
        print(f"Detection finished. Packaged results: {archive}")


if __name__ == "__main__":
    main()
