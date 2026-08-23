# Ops: Caching & Concurrency

## Introduction

In the **previous** session you deployed a **FastAPI RAG** parcel hatch: retrieve desk notes, ask **Groq**, return JSON, then put the same app on **Render** so people outside your laptop could call `/ask`.

A public hatch creates a new problem. Classmates repeat the same question, one shared **API key** gets many hits at once, and every Groq call spends **tokens**. This session is **ops**: keep the live desk fast, fair, and cheaper without rebuilding the RAG brain.

**Running story:** the campus parcel desk is now on the road. You add four habits: **cache** repeated answers, **rate-limit** each student, notice when a **queue** would help, and read a simple **cost log**.

**What you will learn:**

- Cache **identical** and **near-identical** model replies when it is safe for demos
- Apply **per-user** or **per-session** rate limits so one shared key is not exhausted
- Explain when a **job queue** helps — without building a full queue product
- Read a **cost log** from **token** counters tied to sessions

---

## Why Operations Matter After Deploy

Deploy answers “can others reach the hatch?” Ops answers “can the hatch survive a busy hour?”

- **Official Definition:** **Ops** (operations) is the set of habits that keep a running service healthy: speed, fairness, reliability, and cost — after the feature already works.
- **In Simple Words:** Opening the parcel counter is deploy. Managing the rush, the photocopy machine, and the electricity bill is ops.
- **Real-Life Example:** A canteen can cook one plate well. Lunch rush needs a token system, a line, and a note of how much gas was used.

**Why agents need ops early**

- LLM calls are slower and costlier than reading a local file
- Classroom keys are often **shared** — one noisy client can block everyone
- Identical FAQs (“Flipkart Room 214?”) do not need a fresh Groq call each time
- Without a log, you cannot see who spent tokens

**Common doubt:** “Is ops only for big companies?”  
No. The moment a URL is shareable, duplicate work and burst traffic start. Small guards on a demo hatch already teach the same ideas used in production.

### Activity — Name the Failure

The Render URL works. Twenty classmates paste the same curl. Groq returns **429** and the bill jumps. Which layer failed first: RAG quality, or ops (duplicate calls + no per-user cap)? **Answer:** **ops** — the RAG can still be honest.

---

## The Four Levers of a Busy Desk

Think of four windows at the same counter. Each lever solves a different pain.

| Lever | Pain it reduces | Desk picture |
|---|---|---|
| **Response cache** | Paying Groq again for the same FAQ | Photocopy yesterday’s slip |
| **Rate limit** | One student flooding the shared key | Five tokens per person per minute |
| **Concurrency limit** | Too many Groq calls at the same instant | Only two clerks on the phone |
| **Cost log** | “Who spent the tokens?” | Session-wise receipt |

![Four windows at a campus parcel desk — cache photocopy, student rate-limit tokens, a short waiting line, and a session cost receipt — showing ops levers after a live hatch](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module4/session50/session50-01-ops-four-levers.png)

- **Official Definition:** **Concurrency** means how many tasks your app tries to do **at the same time**. A **concurrency limit** caps that number so the shared brain (Groq) is not overloaded.
- **In Simple Words:** Two phone lines to Groq, not fifty overlapping shouts.
- **Real-Life Example:** A hostel office with two landlines. Extra visitors wait or come back — they do not all grab the handset.

Cache cuts repeats; rate limits cut greedy clients; a concurrency cap protects the phone lines; the log tells you whether the mix is working.

---

## Response Caching

Every Groq call has a delay and a token cost. If the question is the same FAQ, reuse the last good answer.

- **Official Definition:** **Response caching** stores a previous model output against a **cache key** (usually a normalised question) and returns that stored output on later matching requests instead of calling the model again.
- **In Simple Words:** Photocopy the Gate 2 slip instead of phoning the clerk brain every time someone asks the same thing.
- **Real-Life Example:** The mess menu for Tuesday is printed once. Ten students asking “what is lunch?” get the same printout — not ten fresh phone calls to the cook.

| Term | Meaning | Parcel example |
|---|---|---|
| **Cache hit** | Answer found in store | Second “Flipkart 214” returns instantly |
| **Cache miss** | No stored answer — call Groq | First time that question appears |
| **TTL** | Time-to-live: how long a copy stays valid | Drop the slip after 10 minutes if gates can change |

![Campus clerk photocopying a Gate 2 answer slip on a cache hit versus placing a paid Groq phone call on a cache miss for the same Flipkart Room 214 FAQ](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module4/session50/session50-02-cache-hit-vs-miss.png)

**Logic:** Cache **output**, not the student’s identity. The key is the **question shape**, not “who asked.”

**When caching is safe for demos**

- Public FAQs: gate numbers, office hours, “what is RAG?”
- Answers that do not depend on *who* is asking
- Knowledge that is stable for the demo window

**When caching is not safe**

- Personal data (“my OTP”, “my room’s private note”)
- Fast-changing facts if TTL is too long
- Different rooms or tracking IDs that only *look* similar in English

**Common error:** Caching on the raw string `"Where is Flipkart 214?"` but missing `"where is flipkart 214??"`. That is two misses for one FAQ. **Normalise** first.

### Identical vs near-identical keys

- **Identical:** exact same characters after you trim spaces
- **Near-identical:** same meaning after a simple clean-up — lowercase, strip punctuation, squeeze extra spaces

Normalise before hashing the key:

```text
"Where is Flipkart 214??"  →  "where is flipkart 214"
"WHERE IS  FLIPKART 214"   →  "where is flipkart 214"
```

Do **not** treat `"Room 214"` and `"Room 108"` as near-identical. Different facts, different keys.

### Activity — Cache or Call?

Decide: (1) two students ask “Flipkart Room 214”, (2) one asks “Amazon Room 108”, (3) a student asks “what is my password reset code”. **Answers:** (1) second can be a **hit**, (2) **miss** (different FAQ), (3) **do not cache** — personal. An in-memory dict is enough for class; Redis can wait.

---

## Rate-Limiting Users

Cache stops *repeat questions*. It does not stop one person asking *new* questions in a burst. That burst still burns the shared Groq key.

- **Official Definition:** A **rate limit** caps how many requests a **user** or **session** may send in a time window (for example 5 requests per 60 seconds). Extra requests are rejected, usually with HTTP **429**.
- **In Simple Words:** Five tokens per student per minute at the counter. The sixth person waits — even if they have a new question.
- **Real-Life Example:** UPI apps often lock a PIN after too many tries. The bank is protecting a shared system, not being rude.

![Student at the parcel hatch holding five request tokens for one minute, with a sixth request turned away as HTTP 429 to protect the shared Groq API key](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module4/session50/session50-03-rate-limit-tokens.png)

**Why per-session, not only global**

- A **global** cap (100/minute for the whole app) lets one noisy client eat the budget
- A **per-session** cap (5/minute per `session_id`) keeps the shared key fair
- The hatch should read `session_id` from the JSON body (demo) or a header (later)

**Logic:** Rate limits protect **people sharing a key**, not only Groq’s own cloud limits. Groq may still return 429. Your app should 429 *earlier* for greedy clients so classmates can still work.

| Limit type | Protects | Weakness if used alone |
|---|---|---|
| Provider (Groq) 429 | Groq’s cluster | Hits everyone after the key is already hot |
| App per-session 429 | Fairness on *your* hatch | Must identify the session honestly |
| Concurrency cap | Overlapping in-flight calls | Does not stop a slow drip of many calls |

**Common doubt:** “Can I just hide the key?”  
Hiding the key is required. Rate limits are still required on a public URL, because the *server* holds the key and will spend it for whoever can call `/ask`.

### Activity — Sixth Request

Policy: 5 asks / 60 seconds / session. A session already sent 5 asks in 20 seconds. What should request 6 return? **Answer:** **429** (or a clear “slow down” JSON) — not a sixth Groq call.

---

## Queue Awareness

Rate limits say “too many from you.” A **queue** says “too many for the kitchen right now — wait your turn.” You do not need Redis or Celery to understand the idea.

- **Official Definition:** A **job queue** stores work items in order (often **FIFO** — first in, first out) so workers process them when capacity is free, instead of starting every job at the same instant.
- **In Simple Words:** A token line at the canteen. You keep your place. The cook handles one plate (or a few) at a time.
- **Real-Life Example:** IRCTC does not give every passenger a private booking clerk at 10:00. Requests wait; a few are processed; others retry.

![Busy parcel counter with a numbered waiting line (FIFO) versus a crowd shouting at once, showing when a job queue helps without building full queue infrastructure](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module4/session50/session50-04-queue-fifo-line.png)

**When a queue helps**

- Each job is **slow** (LLM call, PDF parse, many retrievals)
- Arrivals come in **bursts** (class all clicks together)
- You need **retry** after a provider blip without losing the ticket
- You want **fairness**: first waiting student is served first

**When you do not need a full queue yet**

- A Zoom demo with a handful of calls
- Work that finishes in milliseconds (reading a local cache)
- You can honestly **reject** extras with 429 and ask the client to retry

**Classroom stand-in:** a **concurrency limit** (for example max 2 Groq calls in flight). Extra callers get “desk busy — retry.” That is queue *awareness*: you felt the line without installing queue infrastructure.

**Common error:** Building Kafka “because ops.” For this hatch, cache + per-session limit + a small in-flight cap already prevent most demo disasters.

### Activity — Line or Reject?

Ten `/ask` calls arrive in one second. Groq latency is ~2 seconds. Prefer: (a) start all ten Groq calls, (b) allow two in flight and tell the rest to retry, (c) install a cloud queue product before class ends? **Answer:** **(b)** for this course hatch.

---

## Cost Awareness and Token Logs

Cache and limits are guesses until you **measure**. Tokens are the unit Groq bills; sessions are how you group the bill.

- **Official Definition:** A **token** is a chunk of text the model reads or writes. A **cost log** records, per request, how many tokens were used (and whether the cache saved a call), tied to a **session**.
- **In Simple Words:** Each Groq call is a metered phone call. The receipt says who called, whether you used a photocopy, and how long the call was.
- **Real-Life Example:** A prepaid SIM statement: your number, time, pulse count. You do not need the tower’s full billing engine to read your own log.

![Session-wise parcel desk receipt listing cache hits at zero tokens versus Groq misses with prompt and completion token counts, teaching a simple cost log](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module4/session50/session50-05-session-cost-log.png)

**What to record on every `/ask`**

- `session_id` — who to group
- `cache` — `hit` or `miss`
- `prompt_tokens` / `completion_tokens` / `total_tokens`
- A classroom **INR estimate** (a constant you can change — not a live Groq price sheet)

**How to read a log (this is the skill)**

```text
session  cache   prompt  completion  total
sA       miss    180     45          225
sA       hit     0       0           0
sB       miss    175     40          215
sB       miss    190     50          240
```

- Session **sA** spent **225** tokens; the second ask was free because of cache
- Session **sB** spent **455** tokens — two misses, no reuse
- If sB’s two questions were near-identical, the cache key is too strict or TTL already expired

**Logic:** Cache hits should show **zero model tokens**. If a “hit” still shows 200 tokens, you called Groq by mistake.

**Common doubt:** “Is the INR number exact?”  
Treat it as a **classroom meter**. Real invoices use the provider’s current price. The *habit* is: log tokens per session, compare hits vs misses, then tighten cache or limits.

### Activity — Who Spent More?

From the table above, who spent more tokens, sA or sB? How many tokens did cache save for sA? **Answers:** **sB** spent more (**455** vs **225**). Cache saved **225** tokens on sA’s second ask (a repeat that would have been another miss).

---

## Parcel Desk Ops Hatch (Full Mini App)

Put the four levers on the same FastAPI hatch you already understand. This demo uses an **in-memory** cache, a per-session window, a small in-flight cap, and a cost log. Restarting the process clears memory — that is acceptable for class.

```text
parcel_ops_api/
  app.py
  requirements.txt
```

### `requirements.txt`

```text
fastapi
uvicorn
httpx
```

### Full code — `app.py`

```python
# Read environment variables for the Groq key and classroom settings
import os
# Regular expressions to strip punctuation when building a cache key
import re
# Wall clock for rate-limit windows and cache TTL
import time
# Thread lock so in-flight and log updates stay consistent
import threading
# FastAPI hatch and HTTP errors (429 when limited or busy)
from fastapi import FastAPI, HTTPException
# Freeze JSON request and response shapes
from pydantic import BaseModel, Field
# Type hints for lists and dictionaries
from typing import List, Dict, Any
# HTTPS client for Groq when the key is present
import httpx

# Create the FastAPI application
app = FastAPI(title="Parcel Desk Ops API", version="0.1.0")
# Lock shared memory used by cache, limits, and the log
LOCK = threading.Lock()
# In-memory cache: key -> (expires_at, answer, sources)
CACHE: Dict[str, Any] = {}
# session_id -> list of request timestamps inside the window
WINDOW: Dict[str, List[float]] = {}
# How many Groq calls are running right now
IN_FLIGHT = 0
# Append-only cost rows for GET /cost-log
COST_LOG: List[Dict[str, Any]] = []
# Cache lifetime in seconds (demo TTL)
TTL_SEC = 600
# Max asks per session per window
RATE_MAX = 5
# Window length in seconds
RATE_WINDOW = 60
# Max overlapping Groq calls
MAX_IN_FLIGHT = 2
# Classroom rupee estimate per 1000 tokens (change freely)
INR_PER_1K = 0.05


class AskRequest(BaseModel):  # JSON the student sends
    query: str = Field(..., min_length=1)  # Student question
    session_id: str = Field(..., min_length=1)  # Who to rate-limit and bill


class AskResponse(BaseModel):  # JSON the hatch returns
    ok: bool  # True when an answer is returned
    answer: str  # Reply text (cached or fresh)
    sources: List[str]  # Tiny demo sources
    cache: str  # "hit" or "miss"
    tokens: int  # total_tokens for this call


def normalise(text: str) -> str:
    """Build a near-identical cache key: lower, no punctuation, squeezed spaces."""
    lowered = text.lower()  # Ignore capital letters
    cleaned = re.sub(r"[^a-z0-9\s]", " ", lowered)  # Drop punctuation
    return re.sub(r"\s+", " ", cleaned).strip()  # One space between words


def rate_ok(session_id: str) -> bool:
    """Return True if this session is still under RATE_MAX in RATE_WINDOW seconds."""
    now = time.time()  # Current time
    stamps = [t for t in WINDOW.get(session_id, []) if now - t < RATE_WINDOW]  # Drop old stamps
    if len(stamps) >= RATE_MAX:  # Already used the full quota
        WINDOW[session_id] = stamps  # Keep remaining stamps for the next check
        return False  # Sixth ask in the window
    stamps.append(now)  # Record this ask
    WINDOW[session_id] = stamps  # Save the updated window
    return True  # Under the cap — allow this ask


def estimate_inr(total_tokens: int) -> float:
    """Classroom meter: tokens / 1000 times INR_PER_1K."""
    return round((total_tokens / 1000.0) * INR_PER_1K, 4)  # Not a live Groq invoice


def fake_usage(query: str, answer: str) -> Dict[str, int]:
    """When no Groq key, invent a small token count so the log still teaches."""
    prompt = max(8, len(query.split()) * 4)  # Rough prompt size
    completion = max(8, len(answer.split()) * 2)  # Rough reply size
    return {"prompt_tokens": prompt, "completion_tokens": completion, "total_tokens": prompt + completion}  # Fake usage


def call_brain(query: str) -> Dict[str, Any]:
    """Call Groq if GROQ_API_KEY exists; otherwise return an honest demo answer."""
    sources = ["Desk notes: Flipkart Room 214 → Gate 2. Amazon Room 108 → Gate 1."]  # Demo notes
    api_key = os.getenv("GROQ_API_KEY", "")  # Empty string means demo clerk
    if not api_key:  # Classroom path without spending the cloud key
        answer = "Demo clerk: Flipkart 214 is Gate 2; Amazon 108 is Gate 1. No invented gates."
        usage = fake_usage(query, answer)  # Invent a small token count for the log
        return {"answer": answer, "sources": sources, "usage": usage}  # Same shape as Groq path
    url = "https://api.groq.com/openai/v1/chat/completions"  # Groq chat endpoint
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}  # Auth
    payload = {  # Body Groq expects
        "model": os.getenv("GROQ_MODEL", "llama-3.1-8b-instant"),  # Fast classroom model
        "messages": [  # System rules plus the student question
            {"role": "system", "content": "Campus parcel clerk. Use only: Flipkart 214 Gate 2; Amazon 108 Gate 1. Never invent gates."},
            {"role": "user", "content": query},  # Raw question text
        ],
        "temperature": 0.1,  # Keep answers steady for desk facts
    }
    with httpx.Client(timeout=60.0) as client:  # One HTTP session
        response = client.post(url, headers=headers, json=payload)  # Call Groq
        response.raise_for_status()  # Raise on HTTP errors
        data = response.json()  # Parse JSON
    answer = data["choices"][0]["message"]["content"].strip()  # Assistant text
    usage = data.get("usage", fake_usage(query, answer))  # Provider token counts
    return {"answer": answer, "sources": sources, "usage": usage}  # Uniform return


@app.get("/health")  # Liveness path
def health() -> Dict[str, str]:
    """Liveness for local runs."""
    return {"status": "ok", "service": "parcel-ops-api"}  # Simple ok payload


@app.get("/cost-log")  # Receipt path for the interpretation activity
def cost_log() -> Dict[str, Any]:
    """Return the in-memory session cost log for interpretation practice."""
    return {"rows": COST_LOG}  # All rows since process start


@app.post("/ask", response_model=AskResponse)  # Main hatch
def ask(body: AskRequest) -> AskResponse:
    """Cache, rate-limit, cap concurrency, call brain on miss, append cost row."""
    global IN_FLIGHT  # We change the in-flight counter on misses
    if not body.query.strip():  # Empty question is invalid
        raise HTTPException(status_code=400, detail="query must not be empty")
    with LOCK:  # Rate-limit check is shared state
        if not rate_ok(body.session_id):  # Sixth ask in this session's minute
            raise HTTPException(status_code=429, detail="rate limit: max 5 asks per minute for this session")
    key = normalise(body.query)  # Near-identical questions share one key
    now = time.time()  # Used for TTL and later cache write
    with LOCK:  # Cache lookup is shared state
        hit = CACHE.get(key)  # None if this FAQ is new
        if hit and hit[0] > now:  # Entry exists and has not expired
            answer, sources = hit[1], hit[2]  # Reuse stored slip
            row = {"session_id": body.session_id, "cache": "hit", "prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0, "inr_estimate": 0.0, "query": key}
            COST_LOG.append(row)  # Hits must show zero tokens
            return AskResponse(ok=True, answer=answer, sources=sources, cache="hit", tokens=0)
    with LOCK:  # Concurrency cap is shared state
        if IN_FLIGHT >= MAX_IN_FLIGHT:  # Both phone lines busy
            raise HTTPException(status_code=429, detail="desk busy: concurrency limit — retry shortly")
        IN_FLIGHT += 1  # Take one phone line
    try:  # Always release the line, even on Groq errors
        result = call_brain(body.query)  # Miss path: pay tokens
    except Exception as exc:  # Missing key or provider HTTP error
        raise HTTPException(status_code=502, detail=str(exc.__class__.__name__))
    finally:
        with LOCK:
            IN_FLIGHT -= 1  # Hang up the phone line
    usage = result["usage"]  # Token object from Groq or demo
    total = int(usage.get("total_tokens", 0))  # Billable units for this miss
    with LOCK:  # Store cache and append the receipt together
        CACHE[key] = (now + TTL_SEC, result["answer"], result["sources"])  # Photocopy for TTL
        COST_LOG.append({"session_id": body.session_id, "cache": "miss", "prompt_tokens": int(usage.get("prompt_tokens", 0)), "completion_tokens": int(usage.get("completion_tokens", 0)), "total_tokens": total, "inr_estimate": estimate_inr(total), "query": key})
    return AskResponse(ok=True, answer=result["answer"], sources=result["sources"], cache="miss", tokens=total)
```

### How the code works

- `normalise` turns near-identical questions into one cache key; different room numbers stay different keys
- `rate_ok` keeps a sliding minute window per `session_id` and blocks the sixth ask with **429**
- Cache **hit** returns the stored answer, logs **zero** tokens, and never increments `IN_FLIGHT`
- Cache **miss** takes an in-flight slot (max 2), calls Groq or the demo clerk, stores TTL 10 minutes, then logs tokens
- `GET /cost-log` is the receipt you interpret — hits should be `0` tokens

**Local run**

```bash
cd parcel_ops_api
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export GROQ_API_KEY="your-groq-key"   # optional; demo clerk works without it
uvicorn app:app --reload --host 127.0.0.1 --port 8000
```

**Proof sequence** (same session, near-identical FAQ)

```bash
curl -s -X POST http://127.0.0.1:8000/ask -H 'Content-Type: application/json' \
  -d '{"query":"Where is Flipkart 214??","session_id":"sA"}'
curl -s -X POST http://127.0.0.1:8000/ask -H 'Content-Type: application/json' \
  -d '{"query":"where is flipkart 214","session_id":"sA"}'
curl -s http://127.0.0.1:8000/cost-log
```

### Activity — Prove the Hit

Run the two curls, then `/cost-log`. Confirm the second JSON shows `"cache": "hit"` and `"tokens": 0`, and sA’s hit row is zero tokens. If both are misses, both queries are not sharing `normalise`.

---

## Reading the Desk as One System

The four levers are one story, not four products.

```text
Request + session_id
  → rate limit?  (no → 429)
  → cache key    (hit → return, log 0 tokens)
  → in-flight?   (full → 429 retry)
  → Groq / demo clerk
  → store cache + append cost row
```

| Symptom | First lever to check |
|---|---|
| Same FAQ, slow every time | Cache key / TTL |
| One classmate blocks others | Per-session rate limit |
| Many overlapping timeouts | `MAX_IN_FLIGHT` (queue awareness) |
| “We spent a lot” with no names | Cost log by `session_id` |

**Common error:** Adding cache but forgetting to log hits as zero. Then the receipt lies and you cannot prove savings.

### Activity — One-Minute Pitch

Say aloud: “This live hatch caches safe FAQs, caps each session, allows only two Groq calls at once, and writes a token log. That is ops: less duplicate work, a fair shared key, and a receipt we can read.” Keep it under 60 seconds.

---

## Key Takeaways

- **Caching** reuses safe, public FAQ answers so identical and near-identical questions do not pay Groq twice.
- **Per-session rate limits** protect a shared API key; a public hatch will spend the server key for anyone who can call it.
- A full **job queue** is optional; a small **concurrency limit** plus honest 429 retries already teach “wait in line.”
- A **cost log** of tokens per session — with cache hits at zero — is how you prove savings, not how you guess them.

Once the hatch is cheap and fair, you can point more classmates at the same URL without burning the classroom key on repeated FAQs.

---

## Important Commands, Libraries, Terminologies Used

| Name | Type | Reminder |
|---|---|---|
| Ops | Term | Habits that keep a live hatch fast, fair, and measurable |
| Response cache | Pattern | Store answer by normalised question key |
| Cache hit / miss | Term | Reuse vs call the model |
| Near-identical key | Idea | Lowercase, strip punctuation, squeeze spaces |
| TTL | Term | How long a cached answer stays valid |
| Rate limit | Pattern | Max asks per session per time window |
| HTTP 429 | Status | Too many requests — slow down or retry |
| `session_id` | Field | Identity for limits and the cost log |
| Concurrency limit | Pattern | Max overlapping Groq calls (`IN_FLIGHT`) |
| Job queue / FIFO | Concept | Wait in order when the kitchen is busy |
| Token | Unit | Chunk of text Groq reads or writes |
| Cost log | Record | Per-session tokens, cache flag, classroom INR |
| FastAPI / Uvicorn | Tools | Hatch and local server |
| `GROQ_API_KEY` | Secret | Server-side only; optional in this demo |
