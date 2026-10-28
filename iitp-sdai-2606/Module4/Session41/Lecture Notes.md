# Advanced AI Integration

In the **previous** lesson you connected an **LLM API** to **FastAPI**: keys on the server, **chat** messages with roles, optional **streaming**, and **rate limit** handling on **`/ai/chat`**. That stack returns **plain text**—enough for a helpdesk line. Product features often need **forms instead of essays**, **photos instead of only typing**, and **search by meaning** instead of exact keywords.

This lesson extends **`campus_ai_api`** with **structured outputs**, **vision**, **embeddings**, and a **multimodal** flow that chains those steps. You will **not** re-teach basic provider auth or Claude Code workflows here; you will **build on** secure server calls you already wrote.

## What you will learn in this lesson

- **Structured outputs** — schema-shaped JSON you can validate with Pydantic
- **Vision APIs** — sending an image plus instructions for understanding tasks
- **Embeddings** — numeric fingerprints for **semantic search**
- **Multimodal integration** — one backend route that combines upload, vision, structure, and vectors
- **Hands-on** — routes for **FAQ extract**, **receipt check**, and **similar-question search**

Connecting idea: Integration gave you a **phone line** to the model; advanced features decide **what shape** answers take and **what you can find later**.

---

## When plain text is not enough

- **Official Definition:** **Structured output** is model-generated content constrained to a machine-readable schema (fields, types) rather than free prose.
- **In Simple Words:** The model fills a **fixed form**, not a diary entry.
- **Real-Life Example:** GST invoice fields must match accounting software columns—a paragraph of praise does not import.

| User need | Plain text pain | Advanced tool |
| --- | --- | --- |
| Admin dashboard form | Manual copy-paste from essay | **Structured JSON** |
| “Find similar question” | Keyword misspellings fail | **Embeddings** |
| Upload fee receipt photo | User must type amounts | **Vision** |

**Need:** Your **`StudentOut`** pattern already validates shapes at the API boundary. LLM output should meet the same bar before it touches SQL.

**Common mistake:** Trusting JSON because it *looks* like JSON—always **`json.loads`** + Pydantic.

### Activity — spot the extra key

Given UI fields `title`, `tags` only, decide whether model output `{"title":"X","tags":["a"],"discount":10}` is a frontend bug, backend bug, or **schema** bug. Write one sentence.

---

![Define a JSON schema or Pydantic model so the LLM output is validated before your API returns it](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module4/session41/session41-01-structured-json-schema.png?v=20261028)


## Structured outputs and response schemas

- **Official Definition:** A **response schema** (JSON Schema or provider-native schema object) declares allowed properties and types for model output.
- **In Simple Words:** You show the model the empty form before it writes answers.
- **Real-Life Example:** Board exam OMR sheet—bubbles in fixed places only.

**Two layers of safety**

| Layer | Tool | Job |
| --- | --- | --- |
| Prompt | “Return JSON with keys … only” | Steers the model |
| Code | **Pydantic** `model_validate` | Rejects bad replies |

**Pydantic model for FAQ extraction**

```python
from pydantic import BaseModel, Field  # Validation library you already use
from typing import List  # List type for tags


class FaqExtract(BaseModel):  # Shape we want from the model
    title: str = Field(..., min_length=3, max_length=120)  # Short heading
    tags: List[str] = Field(default_factory=list, max_length=5)  # Up to five tags
    confidence: float = Field(..., ge=0.0, le=1.0)  # Model self-score 0-1
```

**Prompt fragment (server-side string)**

```text
Return ONLY JSON matching keys: title (string), tags (array of strings), confidence (number 0-1).
No markdown fences. No extra keys.
Topic: Convert this student question into a catalog FAQ entry.
Question: <<<
{user_question}
>>>
```

**Validation helper**

```python
import json  # Parse text to Python dict
from pydantic import ValidationError  # Catch schema mismatch


def parse_faq_extract(raw_text: str) -> FaqExtract:  # One entry point for trust
    cleaned = raw_text.strip()  # Remove accidental spaces
    if cleaned.startswith("```"):  # Strip common fence mistake
        cleaned = cleaned.strip("`")  # Crude strip for teaching
        cleaned = cleaned.replace("json", "", 1).strip()  # Remove language tag if present
    data = json.loads(cleaned)  # Parse JSON string
    return FaqExtract.model_validate(data)  # Pydantic enforces types
```

**How the code works**

- **`json.loads`** fails fast on non-JSON.
- **`model_validate`** rejects extra fields if you configure `model_config` with `extra="forbid"` in Pydantic v2.
- Prompt + parser together beat prompt alone.

**Provider feature note:** Gemini and OpenAI expose **JSON mode** or **response_schema** flags—use them when available, but **still validate** in Python.

**Common doubt:** “Is this different from prompt engineering JSON?” — Same goal; provider schema support reduces fence and chit-chat around the JSON.

Connecting idea: Once JSON is reliable, you can store **`title` + `tags`** in tables planned for capstone work later.

---

![Send an image to a vision-capable model and map the reply into structured fields your route can trust](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module4/session41/session41-02-vision-to-structure.png?v=20261028)


## Vision APIs for image understanding

- **Official Definition:** A **vision-capable model** accepts **image bytes or URLs** plus text instructions and returns text or structured data about the image.
- **In Simple Words:** The model **looks** at a picture and answers questions you ask about it.
- **Real-Life Example:** A shopkeeper glances at a **UPI screenshot** to confirm amount before handing goods.

**Backend flow (always server-first)**

| Step | Why |
| --- | --- |
| Browser uploads to **your** FastAPI route | You scan size/type, rate-limit |
| Server forwards to provider | Key stays secret |
| Server returns sanitised JSON/text | You control what UI sees |

**Use cases that fit student projects**

- Read visible text on a notice photo (not legal OCR guarantee)
- Classify upload as “looks like fee receipt” vs “random meme”
- Extract **candidate** fields for human confirmation

**Limitations to state honestly**

- Models **hallucinate** amounts and dates on blurry photos.
- Personal IDs in images are **PII**—avoid uploading real Aadhaar in class demos.
- Vision is **assistive**, not a bank auditor.

### Activity — human-in-the-loop

For a fee receipt upload feature, list two fields you would let the model suggest and one field you would require a human to confirm before saving.

---

## Full code: vision + structured route sketch

Add to **`schemas.py`**

```python
from pydantic import BaseModel  # Base model import


class ReceiptCheck(BaseModel):  # Structured vision result
    looks_like_receipt: bool  # Coarse classification
    visible_amount_inr: str | None  # String because OCR is uncertain
    warning: str  # Human-readable caution line
```

Add **`vision_client.py`**

```python
import base64  # Encode bytes for JSON APIs
import os  # Environment variables
import httpx  # HTTP client
from pathlib import Path  # Read local demo image


GEMINI_MODEL = "gemini-2.0-flash"  # Multimodal-capable model id


async def gemini_vision_structured(image_path: Path, instruction: str) -> str:
    key = os.getenv("GEMINI_API_KEY", "").strip()  # Load secret key
    if not key:  # Guard missing configuration
        raise RuntimeError("GEMINI_API_KEY is missing from environment")  # Clear message
    image_bytes = image_path.read_bytes()  # Read file from disk
    b64 = base64.b64encode(image_bytes).decode("ascii")  # Base64 for JSON payload
    url = (
        f"https://generativelanguage.googleapis.com/v1beta/models/"
        f"{GEMINI_MODEL}:generateContent?key={key}"
    )  # Same family of endpoint as text chat
    payload = {  # Multimodal contents array
        "contents": [
            {
                "parts": [
                    {"text": instruction},  # Text instruction first
                    {
                        "inline_data": {
                            "mime_type": "image/jpeg",  # Match your file type
                            "data": b64,  # Encoded image bytes
                        }
                    },
                ]
            }
        ],
        "generationConfig": {"temperature": 0.1},  # Low randomness for extraction tasks
    }
    async with httpx.AsyncClient(timeout=90.0) as client:  # Vision can be slower
        response = await client.post(url, json=payload)  # POST to provider
    response.raise_for_status()  # Raise on HTTP errors
    data = response.json()  # Parse JSON
    return data["candidates"][0]["content"]["parts"][0]["text"]  # Return model text
```

Add route in **`main.py`**

```python
from fastapi import UploadFile, File  # File upload types
from pathlib import Path  # Temp path handling
import tempfile  # Save upload safely
from schemas import ReceiptCheck  # Output model
from vision_client import gemini_vision_structured  # Vision helper
from receipt_parser import parse_receipt  # Validation helper shown below


@app.post("/ai/receipt-check", response_model=ReceiptCheck)  # Vision + structure endpoint
async def receipt_check(file: UploadFile = File(...)):  # Single uploaded image
    suffix = Path(file.filename or "upload.jpg").suffix or ".jpg"  # Keep extension
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:  # Temp file on disk
        tmp.write(await file.read())  # Save upload bytes
        tmp_path = Path(tmp.name)  # Path for vision client
    instruction = (  # Structured prompt
        "Return ONLY JSON with keys: looks_like_receipt (boolean), "
        "visible_amount_inr (string or null), warning (string). "
        "If unsure, set visible_amount_inr null and explain in warning."
    )
    raw = await gemini_vision_structured(tmp_path, instruction)  # Call provider
    tmp_path.unlink(missing_ok=True)  # Delete temp file
    return parse_receipt(raw)  # Pydantic validation
```

**How the code works**

- Upload hits **your** disk briefly—clean up with **`unlink`**.
- Instruction demands JSON keys matching **`ReceiptCheck`**.
- **`warning`** field forces the API to admit uncertainty—good UX for demos.

---

![Embed menu or document text into vectors, then retrieve nearest matches for semantic search](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module4/session41/session41-03-embeddings-search.png?v=20261028)


## Embeddings and semantic search

- **Official Definition:** An **embedding** is a dense vector representation of text such that semantically similar texts lie close together in vector space.
- **In Simple Words:** Each sentence becomes a **list of numbers**; similar meaning → similar numbers.
- **Real-Life Example:** Library books shelved by **topic**, not only by exact title spelling.

**Why not only SQL `LIKE`?**

| Query | Keyword search | Embedding search |
| --- | --- | --- |
| “hostel curfew time” | Misses “when must I return to dorm” | Often matches |
| Exact SKU | Great | Overkill |

**Core operations**

1. **Embed** each FAQ question once; store vector in DB or file (capstone may add pgvector later).
2. **Embed** the user query at search time.
3. **Cosine similarity** (or dot product) picks nearest neighbours.

**Cosine similarity in pure Python (teaching)**

```python
import math  # Square root for normalization


def cosine_similarity(a: list[float], b: list[float]) -> float:  # Compare two vectors
    if len(a) != len(b):  # Vectors must match length
        raise ValueError("Vector length mismatch")  # Guard bad data
    dot = sum(x * y for x, y in zip(a, b))  # Dot product
    norm_a = math.sqrt(sum(x * x for x in a))  # Length of a
    norm_b = math.sqrt(sum(x * x for x in b))  # Length of b
    if norm_a == 0 or norm_b == 0:  # Avoid divide by zero
        return 0.0  # No similarity
    return dot / (norm_a * norm_b)  # Value between -1 and 1 typically near 0-1 for text
```

**Embedding API call (Gemini embedding endpoint pattern)**

```python
async def embed_text(text: str) -> list[float]:  # Return one vector
    key = os.getenv("GEMINI_API_KEY", "").strip()  # Key from env
    url = f"https://generativelanguage.googleapis.com/v1beta/models/text-embedding-004:embedContent?key={key}"  # Embedding model
    payload = {"content": {"parts": [{"text": text}]}}  # Minimal body
    async with httpx.AsyncClient(timeout=60.0) as client:  # HTTP client
        response = await client.post(url, json=payload)  # POST request
    response.raise_for_status()  # Fail on HTTP errors
    data = response.json()  # Parse response
    return data["embedding"]["values"]  # Provider-specific path to vector
```

**Common mistake:** Storing embeddings without the **original text**—you cannot show humans what matched.

**`receipt_parser.py` companion**

```python
import json  # Parse model text
from schemas import ReceiptCheck  # Pydantic target shape


def parse_receipt(raw_text: str) -> ReceiptCheck:  # Validate vision JSON
    cleaned = raw_text.strip()  # Trim whitespace
    data = json.loads(cleaned)  # Parse JSON string
    return ReceiptCheck.model_validate(data)  # Enforce types and required keys
```

**Search route sketch**

```python
from typing import List  # Type hint for ranked hits


class SearchHit(BaseModel):  # One FAQ match for UI
    question: str  # Stored FAQ text
    score: float  # Similarity score for ordering


@app.get("/ai/faq/search", response_model=List[SearchHit])  # Semantic search demo
async def faq_search(q: str):  # Query string from browser
    query_vec = await embed_text(q)  # Embed user question
    texts = ["When is hostel curfew?", "Canteen menu today"]  # Tiny static corpus
    corpus: list[tuple[str, list[float]]] = []  # Pairs of text + vector
    for text in texts:  # Pre-embed each FAQ line (do once in real apps)
        corpus.append((text, await embed_text(text)))  # Store vector with text
    hits: list[SearchHit] = []  # Collect matches
    for text, vec in corpus:  # Compare to each stored FAQ
        score = cosine_similarity(query_vec, vec)  # Similarity metric
        hits.append(SearchHit(question=text, score=score))  # Append row
    hits.sort(key=lambda h: h.score, reverse=True)  # Highest first
    return hits[:3]  # Top three only
```

**How the code works**

- **`faq_search`** never embeds the corpus on every request in real apps—you precompute offline.
- Returning **`score`** helps mentors see whether matches make sense.
- Swap the static list for SQL when capstone tables exist.

### Activity — similarity intuition

Given three questions A/B/C, rank which pair “feels” most similar before you compute vectors: (A) exam timetable, (B) when is midterm, (C) canteen menu.

---

![Chain vision understanding, text reasoning, and structured JSON—each step with a clear responsibility](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module4/session41/session41-04-multimodal-chain.png?v=20261028)


## Multimodal integration: chaining responsibilities

- **Official Definition:** **Multimodal integration** combines multiple input modalities (text, image, audio) and processing steps in one application flow.
- **In Simple Words:** One feature uses **more than one type** of AI output in sequence.
- **Real-Life Example:** Airport security: **X-ray** (image) → **stamp form** (structured) → **file case** (searchable record).

**Example pipeline: “Smart FAQ ingest”**

| Step | Modality | Output |
| --- | --- | --- |
| 1 | User types question | Raw text |
| 2 | LLM extract | **`FaqExtract` JSON** |
| 3 | Embedding API | Vector stored with FAQ row |
| 4 | Search endpoint | Returns top matches for new questions |

```python
@app.post("/ai/faq/ingest")  # Teaching route combining structure + embed
async def faq_ingest(body: ChatRequest):  # Reuse question field
    raw = await gemini_chat(FAQ_SYSTEM, body.question)  # Text model call from previous lesson
    faq = parse_faq_extract(raw)  # Structured validation
    vector = await embed_text(faq.title + " " + " ".join(faq.tags))  # Embed concise text
    # Persist faq + vector in your database in capstone; here return demo payload
    return {"faq": faq.model_dump(), "vector_dim": len(vector)}  # Show success without DB setup
```

**How the code works**

- Each step has a **single responsibility**—easier to debug than one giant prompt.
- Failure in step 2 never reaches embedding spend.
- Database persistence waits until your capstone schema is ready—this lesson proves the **AI chain**.

**Security integrated:** Scan uploads, cap text length, rate-limit ingest routes like **`/ai/chat`**.

---

## Comparing techniques (quick table)

| Technique | Best for | Still validate? |
| --- | --- | --- |
| Structured JSON | Forms, admin tools | Yes—Pydantic |
| Vision | Photos, scans | Yes—human confirm money fields |
| Embeddings | FAQ, doc search | Yes—show source text |
| Multimodal chain | Ingest + search features | Yes—per step |

---

## Errors and debugging

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| JSON parse error | Model added prose | Tighten prompt; use JSON mode |
| `extra fields not permitted` | Model invented keys | `extra="forbid"` + retry prompt |
| Vision timeout | Large image | Resize server-side |
| All similarity scores low | Wrong embedding model mix | Embed with same model id |
| Empty embedding | Wrong response path | Log provider JSON once |

---

## Provider JSON mode (conceptual comparison)

| Provider | Feature name (check docs) | You still validate in Python? |
| --- | --- | --- |
| Google Gemini | `responseMimeType: application/json` | Yes |
| OpenAI | `response_format` / JSON schema | Yes |
| Anthropic | Tool or structured output blocks | Yes |

**Logic:** Provider constraints **reduce** prose around JSON; they do not replace **`StudentOut`-style** discipline.

**Prompt upgrade when JSON mode is on**

```text
You must output JSON only. Keys: title, tags, confidence.
If you cannot comply, return {"title":"error","tags":[],"confidence":0}.
```

**Common doubt:** “Can we skip prompts if schema exists?” — No—schema does not carry **business rules** like “tags must be lowercase.”

---

## Cost and latency awareness

| Step | Cost driver | Mitigation |
| --- | --- | --- |
| Vision | Image pixels + tokens | Resize images server-side |
| Embeddings | One call per chunk | Batch FAQ builds nightly |
| Structured text | Output tokens | Keep instructions short |
| Retries | Repeated full calls | Fix prompt before retry loop |

**Integrated product note:** Show users a **progress** message on slow vision routes—same UX lesson as streaming chat.

---

## Testing structured and vision routes

| Test | Method |
| --- | --- |
| Happy path FAQ extract | `/docs` with short question |
| Invalid JSON | Temporarily break prompt; expect **422/500** with clear log |
| Huge upload | Send >5 MB image; expect **413** if you add size guard |
| Embedding stability | Same text twice → vectors nearly identical |

**Size guard snippet**

```python
MAX_BYTES = 2_000_000  # Two megabyte teaching limit


@app.post("/ai/receipt-check", response_model=ReceiptCheck)
async def receipt_check(file: UploadFile = File(...)):
    data = await file.read()  # Read bytes once
    if len(data) > MAX_BYTES:  # Reject oversized uploads
        raise HTTPException(status_code=413, detail="Image too large")  # Clear client error
    # ... continue to temp file logic
```

---

## What this lesson deliberately does not cover

**Claude Code** installation, terminal pairing workflows, and **capstone HLD/API security planning** are separate lessons so you do not mix tool setup with schema design. Basic **`/ai/chat`** auth patterns were covered already—reuse them on every new route.

---

## Hands-on checklist

1. Implement **`FaqExtract`** parsing with a deliberately bad model reply; confirm Pydantic catches it.
2. Run **vision** on a clear screenshot and on a blurry meme; compare **`warning`** text.
3. Embed two paraphrases of the same question; print **cosine similarity** > 0.8 (typical, not guaranteed).
4. Wire **`/ai/faq/ingest`** demo response without database—note what you would store in SQL later.
5. Add rate-limit handling from the previous integration lesson to one new route.

---

## Key Takeaways

- **Structured outputs** let LLM replies land in **Pydantic** models your frontend can trust.
- **Vision** belongs behind **your** upload route, with explicit uncertainty for financial fields.
- **Embeddings** power **semantic search** when keywords fail.
- **Multimodal** features are **pipelines**—chain small steps instead of one vague mega-prompt.
- Capstone work will **persist** these artefacts; today you proved the AI side before drawing final tables.

## Important Commands, Libraries, Terminologies used

| Name | Meaning in this lesson |
| --- | --- |
| **Structured output** | Model answer constrained to named fields and types |
| **Response schema** | Blueprint of allowed JSON properties |
| **`FaqExtract`** | Example Pydantic model for FAQ ingest |
| **`model_validate`** | Pydantic check after `json.loads` |
| **Vision API** | Image + text in one provider request |
| **`inline_data`** | Gemini JSON field for base64 image bytes |
| **Embedding** | Numeric vector representing text meaning |
| **`text-embedding-004`** | Example Gemini embedding model id |
| **Cosine similarity** | Metric comparing two embedding vectors |
| **Semantic search** | Find text by meaning, not exact words |
| **Multimodal** | Combining text, image, and vectors in one flow |
| **`UploadFile`** | FastAPI type for browser file uploads |
| **Human-in-the-loop** | User confirms critical fields before save |
| **JSON mode** | Provider flag encouraging valid JSON |
| **`/ai/receipt-check`** | Example vision + structure route |
| **`/ai/faq/ingest`** | Example chain: extract + embed |
