"""Upload session44 lecture note images to S3 and refresh links in Lecture Notes.md."""
import os
import re
from datetime import date
from pathlib import Path

import boto3
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[5]
SESSION_DIR = Path(__file__).resolve().parents[1]
load_dotenv(ROOT / "Command Center" / ".env")

BUCKET = os.environ["AWS_BUCKET_NAME"]
PREFIX = "iitr-as-2601/module3/session44"
BASE_URL = os.environ["AWS_BUCKET_URL"].rstrip("/")
VERSION = date.today().strftime("%Y%m%d")

s3 = boto3.client(
    "s3",
    region_name=os.environ["AWS_REGION"],
    aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
    aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"],
)

images_dir = Path(__file__).parent
notes_path = SESSION_DIR / "Lecture Notes.md"
urls = {}
for path in sorted(images_dir.glob("session44-*.png")):
    key = f"{PREFIX}/{path.name}"
    s3.upload_file(str(path), BUCKET, key, ExtraArgs={"ContentType": "image/png"})
    url = f"{BASE_URL}/{key}?v={VERSION}"
    urls[path.name] = url
    print(f"Uploaded {path.name} -> {url}")

if notes_path.exists():
    text = notes_path.read_text(encoding="utf-8")
    for fname, url in urls.items():
        pattern = rf"!\[[^\]]*\]\([^)]*{re.escape(fname)}[^)]*\)"
        if re.search(pattern, text):
            alt_match = re.search(rf"!\[([^\]]*)\]\([^)]*{re.escape(fname)}", text)
            alt = alt_match.group(1) if alt_match else fname
            text = re.sub(pattern, f"![{alt}]({url})", text, count=1)
    notes_path.write_text(text, encoding="utf-8")
    print(f"\nUpdated image links in {notes_path.name}")

print("\n--- URL map ---")
for name, url in urls.items():
    print(f"{name}: {url}")
