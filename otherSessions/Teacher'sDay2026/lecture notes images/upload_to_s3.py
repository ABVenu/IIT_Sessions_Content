"""Upload Teacher's Day 2026 lecture note images to S3 and print URLs."""
import os
from pathlib import Path

import boto3
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[4]
load_dotenv(ROOT / "Command Center" / ".env")

BUCKET = os.environ["AWS_BUCKET_NAME"]
PREFIX = "othersessions/teachers-day-2026"
BASE_URL = os.environ["AWS_BUCKET_URL"].rstrip("/")
VERSION = "20260903c"

s3 = boto3.client(
    "s3",
    region_name=os.environ["AWS_REGION"],
    aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
    aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"],
)

IMAGE_NAMES = [
    "teachersday2026-01-ai-on-your-phone.png",
    "teachersday2026-02-ai-vs-not-ai.png",
    "teachersday2026-03-clear-question.png",
    "teachersday2026-04-ai-in-three-streams.png",
    "teachersday2026-05-school-ai-tools.png",
    "teachersday2026-06-ai-in-commerce.png",
    "teachersday2026-07-ai-in-arts.png",
    "teachersday2026-08-use-ai-safely.png",
    "teachersday2026-09-mentor-school-website.png",
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
