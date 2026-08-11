"""Upload session19 lecture note images to S3 and print URLs."""
import os
from datetime import date
from pathlib import Path

import boto3
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[5]
load_dotenv(ROOT / "Command Center" / ".env")

BUCKET = os.environ["AWS_BUCKET_NAME"]
PREFIX = "iitp-sdai-2606/module2/session19"
BASE_URL = os.environ["AWS_BUCKET_URL"].rstrip("/")
VERSION = date.today().strftime("%Y%m%d")

s3 = boto3.client(
    "s3",
    region_name=os.environ["AWS_REGION"],
    aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
    aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"],
)

IMAGE_NAMES = [
    "session19-01-dom-railway-display-board.png",
    "session19-02-getElementById-college-id.png",
    "session19-03-querySelector-supermarket-aisle.png",
    "session19-04-event-handling-doorbell.png",
    "session19-05-form-validation-signup-counter.png",
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
