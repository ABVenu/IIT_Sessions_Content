"""Upload session40 lecture note images and sample files to S3."""
import os
from pathlib import Path

import boto3
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[5]
load_dotenv(ROOT / "Command Center" / ".env")

BUCKET = os.environ["AWS_BUCKET_NAME"]
PREFIX = "iitr-as-2603/module4/session40"
BASE_URL = os.environ["AWS_BUCKET_URL"].rstrip("/")

s3 = boto3.client(
    "s3",
    region_name=os.environ["AWS_REGION"],
    aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
    aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"],
)

images_dir = Path(__file__).parent
samples_dir = images_dir.parent / "samples"
urls = {}

content_types = {
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".mp3": "audio/mpeg",
    ".txt": "text/plain; charset=utf-8",
}

files = list(sorted(images_dir.glob("session40-*.png")))
files += list(sorted(samples_dir.glob("sample_*")))

for path in files:
    key = f"{PREFIX}/{path.name}"
    extra = {"ContentType": content_types.get(path.suffix.lower(), "application/octet-stream")}
    s3.upload_file(str(path), BUCKET, key, ExtraArgs=extra)
    url = f"{BASE_URL}/{key}"
    urls[path.name] = url
    print(f"Uploaded {path.name} -> {url}")

print("\n--- URL map ---")
for name, url in urls.items():
    print(f"{name}: {url}")
