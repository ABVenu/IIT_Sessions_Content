# Deployment: FastAPI RAG on Render

## Introduction

In the **previous** session you built a **Streamlit** front counter for the campus parcel desk — students typed enquiries and saw answers plus short sources and steps on your laptop.

A laptop demo is private. Faculty outside your Wi-Fi, a hostel bot, or a teammate’s script cannot reach `localhost`. Today you build a small **RAG** API with **FastAPI** and **Groq**, choose where knowledge lives (**local file** or **Supabase**), and deploy the mini app on **Render**.

**Running story:** the same **campus parcel desk**. The hatch answers from parcel notes (retrieve → ask Groq → reply). First you run it locally. Then you put the same hatch on Render so others can call it.

**What you will learn:**

- Why **deployment** is needed and how a **local** app differs from a **deployed** app
- Build a simple **RAG** flow with a **Groq** request behind **FastAPI**
- Store knowledge **locally** or in **Supabase**
- Deploy the mini app on **Render** with environment variables (no containers)

---

## Why Deployment Is Needed

Streamlit on your machine proves the idea. Deployment makes the idea **reachable**.

- **Official Definition:** **Deployment** means running your app on a host that other people (or other programs) can reach through a stable URL, not only on your personal laptop.
- **In Simple Words:** Moving the parcel counter from your hostel room to a shop that stays open on the campus road.
- **Real-Life Example:** Practising a canteen billing app alone vs giving the whole floor a link that works when your laptop is closed.

**Why agents need deployment**

- Stakeholders will not install Python to try your desk
- Bots and other apps need a public (or shared) HTTPS URL
- Keys and config can live on the host, not in screenshots of your terminal
- A pilot link is how you collect real feedback
- Your laptop cannot be the production server — sleep, travel, and Wi-Fi changes break demos

**What deployment is *not*:** It is not a substitute for honest RAG. If local answers invent gates, Render will invent the same gates — only louder, because more people can see them.

**Common doubt:** “Is local enough for the course project?”  
Local is perfect for building and debugging. A short Render pilot proves the product can live outside your laptop.

### Activity — Who Is Blocked?

Your FastAPI app works on `http://127.0.0.1:8000`. Who cannot use it yet: (a) you on the same laptop, (b) a faculty member in another city, (c) your own browser on the same machine? **Answer:** **(b)**.

Local success answers “does the brain work?” Deployed success answers “can others reach the brain?”
---

## Local App vs Deployed App

Same code story — different “front door,” process owner, and secret storage.

| Topic | Locally running app | Deployed app (e.g. Render) |
|---|---|---|
| Who starts it | You type `uvicorn` in a terminal | Render starts/restarts the process |
| URL | `http://127.0.0.1:8000` (private to your machine) | `https://your-app.onrender.com` (shareable) |
| When it stops | Laptop sleep, closed lid, stopped terminal | Host manages uptime (free tiers may sleep when idle) |
| Secrets | Shell `export` or local `.env` (never commit) | Render **Environment** panel |
| Knowledge files | Files next to your script | Bundled in the repo **or** read from Supabase |
| Who can call `/ask` | Mostly you | Anyone with the URL (lock it down later if needed) |
| Debugging | Easy logs in your terminal | Logs in the Render dashboard |

![Hostel-room localhost parcel desk only reachable by you versus the same counter on campus road with a public HTTPS link for faculty, bots, and remote callers](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module4/session49/session49-01-local-vs-deployed-reach.png)

- **Official Definition:** **Localhost** means “this same computer” — browsers use addresses like `127.0.0.1` that other machines on the internet cannot open as your app.
- **In Simple Words:** A doorbell that only rings inside your room.
- **Real-Life Example:** Your home Wi-Fi printer works for you; a stranger across town cannot print to it.

**Logic to remember:** Deployment does not magically improve your RAG. It changes **reachability**, **process lifetime**, and **where secrets/data live**.

### Activity — Match the Symptom

Match: (1) “Works for me, 404 for faculty,” (2) “App died when I closed the laptop,” (3) “Key is in Render dashboard.” To: (A) local-only URL, (B) local process lifetime, (C) deployed secret injection. **Answers:** 1→A, 2→B, 3→C.

---

## What Is a Simple RAG App?

Before FastAPI and Render, name the brain pattern you will deploy.

- **Official Definition:** **RAG** (Retrieval-Augmented Generation) means first **retrieve** relevant notes from your knowledge store, then **generate** an answer with an LLM using those notes as context.
- **In Simple Words:** Open the right parcel register pages, then ask a smart clerk to answer only from those pages.
- **Real-Life Example:** Before advising a student, the warden checks the notice file — then speaks — instead of guessing from memory.

**Today’s mini pipeline**

1. Student question arrives at `POST /ask`
2. Retrieve top matching lines from knowledge (local file **or** Supabase)
3. Send question + retrieved lines to **Groq**
4. Return JSON: `answer`, `sources`, `ok`

![Campus parcel clerk opening the register to retrieve matching notes, sending them to a Groq cloud brain, and handing back an answer slip with sources — simple RAG as a desk workflow](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module4/session49/session49-02-rag-retrieve-groq-answer.png)

- **Official Definition:** **Groq** is an LLM inference provider you call with an API key to get fast model completions over HTTPS.
- **In Simple Words:** A cloud clerk brain you rent by API key — your app sends text, Groq sends the reply.
- **Real-Life Example:** Like calling a helpline: you speak the context; they answer; you do not host the call centre yourself.

**Common error:** Sending the question to Groq with **no retrieved context**. That is plain chat, not RAG — and it may invent gate numbers.

---

## Knowledge Store: Local File vs Supabase

Your RAG needs a place to keep parcel notes.

| Choice | What it is | Best for this pilot |
|---|---|---|
| **Local file** | A `.txt` / `.md` in the project folder | Fastest classroom path; file ships with the Render deploy |
| **Supabase** | Hosted Postgres + simple API/table | When many people update knowledge without redeploying code |

![Split comparison — parcels.txt notebook in a desk drawer for local knowledge versus a shared cloud register many hostel volunteers can update for Supabase-style storage](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module4/session49/session49-03-local-file-vs-supabase-register.png)

- **Official Definition:** **Supabase** is a backend-as-a-service platform that gives you a hosted database (and related APIs) so apps can read/write data without managing a server yourself.
- **In Simple Words:** A shared online register in the cloud instead of a notebook only on your USB drive.
- **Real-Life Example:** A Google Sheet the whole hostel office edits vs a paper register locked in one drawer.

**Pilot advice:** Start with a **local** `knowledge/parcels.txt` so deploy stays simple. Switch the retriever to **Supabase** when the desk data must change without a new Render deploy.

**Supabase table sketch (optional path)**

- Create a table named `parcel_notes`
- Add a text column `content`
- Insert the same lines you would put in `parcels.txt`
- Put project URL + key into env vars on your laptop and later on Render

### Activity — Pick the Store

Data changes every hour by three office volunteers. Prefer: (a) only a file inside git, (b) Supabase table + env keys on Render? **Answer:** **(b)**.

Either way, the FastAPI hatch and Groq step stay the same — only `get_all_docs()` changes where lines come from.
---

## FastAPI Hatch + Groq RAG (Full Mini App)

Create this beginner project layout:

```text
parcel_rag_api/
  knowledge/parcels.txt
  app.py
  requirements.txt
```

![FastAPI service hatch at the campus parcel counter — POST /ask receives a JSON question slip, the clerk retrieves notes and calls Groq, and returns a JSON answer envelope](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module4/session49/session49-04-fastapi-service-hatch.png)

### Sample knowledge file — `knowledge/parcels.txt`

```text
Flipkart parcel for Room 214 is at Gate 2.
Amazon parcel for Room 108 is at Gate 1.
BlueDart for Room 312 is at the warden office.
Unknown tracking IDs must not invent a gate.
```

### `requirements.txt`

```text
fastapi
uvicorn
httpx
python-dotenv
```

### Full code — `app.py`

```python
# Import os to read environment variables for keys and data mode
import os
# Import Path to locate the local knowledge file safely
from pathlib import Path
# Import FastAPI tools for the HTTP hatch and HTTP errors
from fastapi import FastAPI, HTTPException
# Import BaseModel to freeze request/response JSON shapes
from pydantic import BaseModel, Field
# Import typing helpers for lists and optional fields
from typing import List, Optional, Dict, Any
# Import httpx to call the Groq HTTPS API
import httpx
# Load local .env values when present (local runs only)
try:
    from dotenv import load_dotenv  # Optional helper for local secrets
    load_dotenv()  # Copy .env into process environment if file exists
except ImportError:
    pass  # On Render, variables come from the dashboard instead

# Create the FastAPI application object
app = FastAPI(title="Parcel Desk RAG API", version="0.1.0")


class AskRequest(BaseModel):
    query: str = Field(..., min_length=1)  # Student question text


class AskResponse(BaseModel):
    ok: bool  # True when generation path completed with context attempt
    answer: str  # Final reply for the student
    sources: List[str]  # Retrieved knowledge lines used as context
    error: Optional[str] = None  # Machine-friendly error code when needed


def load_local_docs() -> List[str]:
    """Read parcel notes from a local text file shipped with the app."""
    # Build path to knowledge/parcels.txt next to this file's folder
    path = Path(__file__).parent / "knowledge" / "parcels.txt"
    # If file missing, return empty list so callers can fail honestly
    if not path.exists():
        return []
    # Read file as UTF-8 text
    text = path.read_text(encoding="utf-8")
    # Split into non-empty lines as simple "chunks"
    return [line.strip() for line in text.splitlines() if line.strip()]


def load_supabase_docs() -> List[str]:
    """Read parcel notes from a Supabase table via REST (optional path)."""
    # Read Supabase project URL from environment
    url = os.getenv("SUPABASE_URL", "").rstrip("/")
    # Read Supabase anon or service key from environment
    key = os.getenv("SUPABASE_KEY", "")
    # Table name defaults to parcel_notes for this pilot
    table = os.getenv("SUPABASE_TABLE", "parcel_notes")
    # Without URL/key, treat as not configured
    if not url or not key:
        return []
    # Call Supabase REST: select the content column
    endpoint = f"{url}/rest/v1/{table}?select=content"
    headers = {
        "apikey": key,  # Supabase API key header
        "Authorization": f"Bearer {key}",  # Auth header
    }
    # Perform GET with a short timeout
    with httpx.Client(timeout=20.0) as client:
        response = client.get(endpoint, headers=headers)
        response.raise_for_status()  # Raise if HTTP status is an error
        rows = response.json()  # Parse JSON list of rows
    # Collect content strings from each row
    return [str(row.get("content", "")).strip() for row in rows if row.get("content")]


def get_all_docs() -> List[str]:
    """Choose local file or Supabase based on DATA_SOURCE env var."""
    # Read mode: "local" (default) or "supabase"
    mode = os.getenv("DATA_SOURCE", "local").lower()
    # Supabase path when explicitly selected
    if mode == "supabase":
        return load_supabase_docs()
    # Default classroom path: local file
    return load_local_docs()


def retrieve(query: str, docs: List[str], k: int = 3) -> List[str]:
    """Very simple RAG retrieve: rank lines by shared words with the query."""
    # Lowercase query for naive matching
    q_words = set(query.lower().split())
    scored = []  # Hold (score, line) pairs
    for line in docs:
        # Count how many query words appear in the line
        score = len(q_words.intersection(line.lower().split()))
        if score > 0:
            scored.append((score, line))
    # Sort highest score first
    scored.sort(key=lambda item: item[0], reverse=True)
    # Return top-k lines only
    return [line for score, line in scored[:k]]


def ask_groq(query: str, sources: List[str]) -> str:
    """Call Groq chat completions with retrieved context."""
    # Read Groq API key — required for generation
    api_key = os.getenv("GROQ_API_KEY", "")
    if not api_key:
        raise RuntimeError("GROQ_API_KEY is not set")
    # Model name can be overridden by env for pilots
    model = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")
    # Join retrieved lines into one context block
    context = "\n".join(f"- {s}" for s in sources) if sources else "(no desk notes found)"
    # System instruction: answer only from context; stay honest
    system = (
        "You are the campus parcel desk assistant. "
        "Answer ONLY using the provided desk notes. "
        "If notes are missing, say you could not find the parcel. Never invent a gate."
    )
    # User message includes context + question
    user = f"Desk notes:\n{context}\n\nQuestion: {query}"
    # Groq OpenAI-compatible chat endpoint
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",  # Groq secret
        "Content-Type": "application/json",  # JSON body
    }
    payload = {
        "model": model,  # Which Groq model to use
        "messages": [
            {"role": "system", "content": system},  # Behaviour rules
            {"role": "user", "content": user},  # Context + question
        ],
        "temperature": 0.2,  # Keep answers steady for desk facts
    }
    # POST to Groq and parse the assistant text
    with httpx.Client(timeout=60.0) as client:
        response = client.post(url, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
    return data["choices"][0]["message"]["content"].strip()


@app.get("/health")
def health() -> Dict[str, str]:
    """Liveness check for local runs and Render."""
    return {"status": "ok", "service": "parcel-rag-api"}


@app.post("/ask", response_model=AskResponse)
def ask(body: AskRequest) -> AskResponse:
    """RAG hatch: retrieve desk notes, call Groq, return contract JSON."""
    if not body.query.strip():
        raise HTTPException(status_code=400, detail="query must not be empty")
    docs = get_all_docs()  # Load from local file or Supabase
    sources = retrieve(body.query, docs)  # Top matching lines
    try:
        answer = ask_groq(body.query, sources)  # Generate with Groq
        return AskResponse(ok=True, answer=answer, sources=sources, error=None)
    except Exception as exc:
        # Honest failure for missing key or provider errors
        return AskResponse(
            ok=False,
            answer="The parcel desk could not generate an answer right now.",
            sources=sources,
            error=str(exc.__class__.__name__),
        )
```

### How the code works

- `DATA_SOURCE=local` reads `knowledge/parcels.txt`; `DATA_SOURCE=supabase` reads a table via Supabase REST
- `retrieve` picks top matching lines (beginner RAG without a vector DB)
- `ask_groq` sends system rules + notes + question to Groq and returns the text
- `POST /ask` always returns the same fields: `ok`, `answer`, `sources`, `error`
- Secrets stay in env vars — never hard-coded

**Local run**

```bash
cd parcel_rag_api
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export GROQ_API_KEY="your-groq-key"
export DATA_SOURCE=local
uvicorn app:app --reload --host 127.0.0.1 --port 8000
```

Open `http://127.0.0.1:8000/docs` and try `POST /ask`.

### Activity — First Local Proof

Call `/ask` with “Flipkart Room 214”. Confirm: (1) `sources` is not empty, (2) answer mentions Gate 2, (3) a nonsense tracking id does not invent a new gate.

**Quick curl check (local)**

```bash
curl -X POST "http://127.0.0.1:8000/ask" \
  -H "Content-Type: application/json" \
  -d '{"query":"Where is the Flipkart parcel for Room 214?"}'
```

When this works locally, you are ready to document the contract and then deploy the same files to Render.
---

## Request / Response Contract

Integrators (and your future Streamlit client) should rely on fixed fields.

**Request**

```json
{ "query": "Where is the Flipkart parcel for Room 214?" }
```

**Response**

```json
{
  "ok": true,
  "answer": "Gate 2 — Flipkart for Room 214.",
  "sources": ["Flipkart parcel for Room 214 is at Gate 2."],
  "error": null
}
```

**Rules:** same keys every time; empty `sources` is allowed; never invent parcels; keep `GROQ_API_KEY` on the server only.

---

## Deploy the Mini App on Render

Now move the same hatch from localhost to a shareable URL.

- **Official Definition:** **Render** is a cloud hosting platform (a simple PaaS) that can run your web service from a Git repo, inject environment variables, and give you an HTTPS URL.
- **In Simple Words:** A rented shop manager that keeps your FastAPI process online and hands you a public link.
- **Real-Life Example:** Instead of asking visitors to enter your hostel room, you open a counter on the main road.

![Same parcel RAG hatch deployed on Render cloud — GitHub repo feeds the service, environment keys stay in a locked panel, and a faculty member in another city calls the public HTTPS desk](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module4/session49/session49-05-render-cloud-deploy.png)

### Deploy checklist (Web Service)

1. Push `parcel_rag_api/` to GitHub (**no** `.env`, **no** API keys in code)
2. On Render: **New → Web Service** → connect the repo
3. **Runtime:** Python
4. **Build command:** `pip install -r requirements.txt`
5. **Start command:** `uvicorn app:app --host 0.0.0.0 --port $PORT`
6. Add env vars in Render:
   - `GROQ_API_KEY` = your Groq key
   - `DATA_SOURCE` = `local` (or `supabase`)
   - If Supabase: `SUPABASE_URL`, `SUPABASE_KEY`, `SUPABASE_TABLE`
7. Deploy → wait for status **Live**
8. Test `https://YOUR-SERVICE.onrender.com/health` then `/docs` → `POST /ask`

**Why `--host 0.0.0.0` and `$PORT`?**  
Render’s proxy must reach your process on all interfaces, and the platform sets the port. Locally you often use `127.0.0.1` and `8000` instead.

**Local file data on Render:** `knowledge/parcels.txt` must be **committed** to the repo so the service can read it after deploy.  
**Supabase data on Render:** table rows live in Supabase; code only needs URL/key env vars — update notes without redeploying the file.

**Common errors**

- Start command missing `$PORT` → service fails health checks
- Key left only in your laptop `.env` → Render returns generation errors
- Free tier **sleeps** when idle → first request after rest can be slow (cold start)
- Forgetting to commit `knowledge/parcels.txt` while `DATA_SOURCE=local` → empty retrieval on Render

**After deploy — prove the difference**

| Check | Local | Render |
|---|---|---|
| Health | `http://127.0.0.1:8000/health` | `https://YOUR-SERVICE.onrender.com/health` |
| Ask | localhost `/docs` or curl | same path on the https URL |
| Secret | your shell / `.env` | Render Environment panel |

### Activity — Local vs Render Card

Fill one line each: Local URL = ____ . Render URL = ____ . Where is `GROQ_API_KEY` on Render? ____ . **Sample:** `127.0.0.1:8000` / `https://….onrender.com` / Environment panel.
---

## End-to-End Pilot Path

```text
Question → FastAPI /ask → retrieve (local file or Supabase)
        → Groq completion → JSON answer + sources
```

| Step | Local | Render |
|---|---|---|
| Run | `uvicorn` on your laptop | Host runs start command |
| Prove | `/docs` on localhost | `/health` then `/docs` on https URL |
| Data | `parcels.txt` on disk | Same file in repo **or** Supabase |
| Share | Hard (private URL) | Easy (send the link) |

### Activity — One-Minute Pitch

Say aloud: “This is a small RAG parcel API. It retrieves desk notes, asks Groq, and returns JSON. Locally I debug on localhost. On Render the same app gets a public URL and secrets from the dashboard — that is why we deploy.” Keep it under 60 seconds.

---

## Key Takeaways

- **Deployment** is needed so people and programs outside your laptop can reach the agent hatch.
- **Local vs deployed** mainly differs in URL, who keeps the process alive, and where secrets/data live — not in the RAG idea itself.
- A simple **FastAPI + retrieve + Groq** pipeline is enough for a pilot RAG API.
- Knowledge can start as a **local file** (shipped with the repo) or move to **Supabase** when many editors must update data without redeploying.
- On **Render**, use `0.0.0.0`, `$PORT`, and the Environment panel — never commit API keys.

Once this mini hatch is live, you can point Streamlit, bots, or classmates at the same `/ask` contract with more confidence.

---

## Important Commands, Libraries, Terminologies Used

| Name | Type | Reminder |
|---|---|---|
| Deployment | Term | App reachable beyond your laptop |
| Localhost / `127.0.0.1` | Concept | Private-to-your-machine URL |
| RAG | Pattern | Retrieve notes, then generate with an LLM |
| Groq | Provider | HTTPS LLM API using `GROQ_API_KEY` |
| FastAPI | Library | Thin HTTP API hatch |
| Uvicorn | Server | Runs FastAPI locally and on Render |
| Supabase | Data option | Hosted table for shared knowledge |
| Local `parcels.txt` | Data option | Simple file shipped with the repo |
| Render | PaaS host | Git-based web service + env panel |
| `DATA_SOURCE` | Env var | `local` or `supabase` |
| `GROQ_API_KEY` | Env var | Server-side secret only |
| Start command | Render | `uvicorn app:app --host 0.0.0.0 --port $PORT` |
| `/health` + `/ask` | Endpoints | Liveness + RAG question hatch |
| Cold start | Hosting | Free tier may sleep; first call slower |
