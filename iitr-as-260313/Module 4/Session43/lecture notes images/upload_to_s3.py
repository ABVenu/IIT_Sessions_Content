"""Upload Session43 lecture note images to S3."""
import os
from pathlib import Path

import boto3
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[5]
load_dotenv(ROOT / "Command Center" / ".env")

BUCKET = os.environ["AWS_BUCKET_NAME"]
PREFIX = "iitr-as-260313/module4/session43"
BASE_URL = os.environ["AWS_BUCKET_URL"].rstrip("/")

IMAGES = [
    "session43-01-langchain-vs-langgraph.png",
    "session43-02-building-blocks.png",
    "session43-03-reducer-merge.png",
    "session43-04-tool-cycle.png",
]

s3 = boto3.client(
    "s3",
    region_name=os.environ["AWS_REGION"],
    aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
    aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"],
)

images_dir = Path(__file__).parent
urls = {}
for name in IMAGES:
    path = images_dir / name
    if not path.exists():
        raise FileNotFoundError(f"Missing image: {path}")
    key = f"{PREFIX}/{name}"
    s3.upload_file(str(path), BUCKET, key, ExtraArgs={"ContentType": "image/png"})
    url = f"{BASE_URL}/{key}"
    urls[name] = url
    print(f"Uploaded {name} -> {url}")

print("\n--- URL map ---")
for name, url in urls.items():
    print(f"{name}: {url}")
