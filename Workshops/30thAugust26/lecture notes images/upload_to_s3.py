"""Upload 30 August workshop lecture note images to S3 and print URLs."""
import os
from pathlib import Path

import boto3
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[4]
load_dotenv(ROOT / "Command Center" / ".env")

BUCKET = os.environ["AWS_BUCKET_NAME"]
PREFIX = "workshops/30th-august-26"
BASE_URL = os.environ["AWS_BUCKET_URL"].rstrip("/")
VERSION = "20260903"

s3 = boto3.client(
    "s3",
    region_name=os.environ["AWS_REGION"],
    aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
    aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"],
)

IMAGE_NAMES = [
    "workshop-30aug26-01-subarray-vs-skipped.png",
    "workshop-30aug26-02-fixed-window-slide.png",
    "workshop-30aug26-03-variable-window-shrink.png",
]

images_dir = Path(__file__).parent
for name in IMAGE_NAMES:
    path = images_dir / name
    if not path.exists():
        raise FileNotFoundError(f"Missing image: {path}")
    key = f"{PREFIX}/{path.name}"
    s3.upload_file(str(path), BUCKET, key, ExtraArgs={"ContentType": "image/png"})
    url = f"{BASE_URL}/{key}?v={VERSION}"
    print(f"Uploaded {path.name} -> {url}")
