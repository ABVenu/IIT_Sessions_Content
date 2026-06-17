"""Upload 23rdMay advanced AI lecture note images to S3."""
import os
from datetime import date
from pathlib import Path

import boto3
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[5]
SESSION_DIR = Path(__file__).resolve().parents[1]
load_dotenv(ROOT / "Command Center" / ".env")

BUCKET = os.environ["AWS_BUCKET_NAME"]
PREFIX = "other-sessions/rahul-singh-23may/advanced-ai"
BASE_URL = os.environ["AWS_BUCKET_URL"].rstrip("/")
VERSION = date.today().strftime("%Y%m%d")

s3 = boto3.client(
    "s3",
    region_name=os.environ["AWS_REGION"],
    aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
    aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"],
)

images_dir = Path(__file__).parent
notes_path = SESSION_DIR / "Lecture Notes Released.md"

urls = {}
for path in sorted(images_dir.glob("adv-ai-*.png")):
    key = f"{PREFIX}/{path.name}"
    s3.upload_file(str(path), BUCKET, key, ExtraArgs={"ContentType": "image/png"})
    url = f"{BASE_URL}/{key}?v={VERSION}"
    urls[path.name] = url
    print(f"Uploaded {path.name} -> {url}")

print("\n--- URL map ---")
for name, url in urls.items():
    print(f"{name}: {url}")
