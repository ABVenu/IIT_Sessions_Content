"""Upload Session03_M3_1 lecture note images to S3 and print URLs."""
import os
from pathlib import Path

import boto3
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[6]
load_dotenv(ROOT / "Command Center" / ".env")

BUCKET = os.environ["AWS_BUCKET_NAME"]
PREFIX = "iitp-sdai-2606/masterclasses/sdai2606/session03"
BASE_URL = os.environ["AWS_BUCKET_URL"].rstrip("/")
VERSION = "20260910"

s3 = boto3.client(
    "s3",
    region_name=os.environ["AWS_REGION"],
    aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
    aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"],
)

IMAGE_NAMES = [
    "session03-01-three-kinds-of-web.png",
    "session03-02-web1-vs-web2.png",
    "session03-03-browser-load-render.png",
    "session03-04-frontend-backend-split.png",
    "session03-05-api-json-cloud-loop.png",
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
