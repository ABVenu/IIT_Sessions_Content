# AI API Integration

In the **previous** lessons you learned how an **LLM** turns tokens into text, and how **prompt engineering** shapes answers with roles, constraints, and structured JSON in small scripts. Those skills lived mostly in chat tabs and local Node labs. A real campus product needs a **server** in the middle—your **FastAPI** app—so students never touch the provider’s secret key and every call follows rules you control.

This lesson wires an **LLM API** into FastAPI the same way you already call **SQLAlchemy** and return **`StudentOut`**: authenticate on the server, validate input, call the external service, return a safe response. You will **not** repeat prompt technique drills here; you will **use** the prompts you already know inside **chat-shaped** HTTP requests.

## What you will learn in this lesson

- **LLM API providers** — OpenAI, Google (Gemini), Anthropic (Claude), and the shared HTTPS pattern
- **Authentication** — API keys in environment variables, never in the browser
- **Chat APIs** — **system**, **user**, and **assistant** messages in one payload
- **Streaming** — sending partial text to the client for a responsive UI
- **Rate limits** — HTTP 429, backoff, and polite failure messages
- **Hands-on** — a small **`campus_ai_api`** FastAPI service with buffered and streaming routes

Connecting idea: Prompt engineering wrote the **order slip**; API integration builds the **service counter** between your frontend and the model kitchen.

---

## Why integrate on the backend?

- **Official Definition:** **AI API integration** is connecting a hosted large language model to your application through HTTPS, with credentials and business rules enforced on your server.
- **In Simple Words:** The browser talks to **your** API; **your** API talks to OpenAI/Google/Anthropic with a secret key.
- **Real-Life Example:** At a popular **dosa** shop, customers order at the **counter**, not inside the kitchen. The wholesale account stays with the owner.

| Risk if the frontend calls the model directly | What the backend fixes |
| --- | --- |
| API key visible in DevTools | Key loaded from **`.env`** on the server only |
| Unlimited spend during a fest | You add **rate limits**, quotas, or queues |
| No audit trail | You log request metadata (not secrets) |
| Prompt rules skipped | **System** message applied on every call |

**Need:** Your **`campus_api`** already proves you can design routes, Pydantic models, and `/docs`. The LLM is **one more dependency**—like a payment gateway—not a replacement for SQL.

**Common mistake:** Copying the Gemini URL with `?key=` into React because “it feels faster.” Speed without a counter is how teams get surprise bills.

### Activity — draw the three boxes

On paper, draw three boxes: **Browser**, **FastAPI**, **LLM provider**. Label one arrow “JSON question, no key” and one arrow “HTTPS + secret key.” Mark where **system** prompt text is added.

---

## The LLM API provider ecosystem

- **Official Definition:** An **LLM API provider** hosts models and exposes them through documented HTTP endpoints you call with an **API key**.
- **In Simple Words:** You rent brainpower over the internet instead of installing a model on your laptop.
- **Real-Life Example:** Three different mobile networks—same idea (call someone far away), different plans and coverage.

| Provider | Model families you will hear | Typical use in this course |
| --- | --- | --- |
| **OpenAI** | GPT series | Chat completions, tools, widely copied JSON shape |
| **Google** | **Gemini** | Same `generateContent` pattern as your Node labs |
| **Anthropic** | **Claude** | Strong long-context assistants and coding help |

**Logic:** Providers differ in price, policy, and features, but integration steps rhyme:

1. Create a project in the provider console.
2. Generate an **API key** (treat like an ATM PIN).
3. Send HTTPS requests with JSON bodies.
4. Parse text (or stream chunks) from the response.

**Common doubt:** “Must we use all three?” — No. Pick **one** primary provider per feature; abstract later if needed.

**Do not confuse:** Provider **chat UI** (web) vs **API** (programmatic). This lesson is API-only.

Connecting idea: Once you pick a provider, every call needs **authentication** before you worry about streaming.

---

## Authentication and secure API key usage

- **Official Definition:** **API authentication** here means proving your server is allowed to call the provider, usually with a bearer token or key in headers or query (provider-specific).
- **In Simple Words:** The key is the password that bills **your** account.
- **Real-Life Example:** A hostel **mess card**—only the kitchen swipe machine should read it, not every guest.

**Secure setup checklist**

| Step | Practice |
| --- | --- |
| Store key | **`GEMINI_API_KEY`** or **`OPENAI_API_KEY`** in **`.env`**, not Git |
| Load key | **`python-dotenv`** or OS env at startup |
| Use key | Only inside server code (`httpx`, official SDK) |
| Never | Log full key, commit `.env`, paste key in prompts |
| Frontend | Calls **`/ai/chat`**, never the provider URL |

**`.env` example (local only)**

```text
GEMINI_API_KEY=your_key_from_google_ai_studio
```

**`.gitignore` must include**

```text
.env
.venv/
```

**Common mistake:** Putting the key in a FastAPI **query parameter** on a public route “for testing.” Anyone can replay that URL from browser history.

**Integrated security note:** Same discipline as database URLs—rotate keys if leaked, use separate keys for dev vs demo if the console allows.

### Activity — red-team your teammate’s design

Read this claim: “We will store the key in `localStorage` so refresh keeps working.” Write three concrete harms (billing, abuse, compliance) in bullet form.

---

## Chat APIs and role-based messages

- **Official Definition:** A **chat completion API** accepts an ordered list of **messages**, each with a **role** (`system`, `user`, `assistant`) and **content** (text).
- **In Simple Words:** You send a short conversation transcript, not one mystery paragraph.
- **Real-Life Example:** A hospital **OPD file**—fixed instructions at the top (system), patient complaint (user), doctor’s earlier note (assistant).

| Role | Who writes it | Typical content |
| --- | --- | --- |
| **system** | Your backend (hidden from user) | Tone, safety, “use only provided context” |
| **user** | End user or your route | Question, form text |
| **assistant** | Model (prior turns) | Earlier replies in a thread |

**Mapping from prompt engineering**

| Prompt block you already use | Chat role |
| --- | --- |
| Constraints + role persona | **system** |
| Task + context | **user** |
| Multi-turn helpdesk | prior **assistant** + new **user** |

**Gemini-shaped JSON (conceptual)**

```json
{
  "contents": [
    { "role": "user", "parts": [{ "text": "system-style instructions often go in first user turn for simple APIs" }] }
  ],
  "generationConfig": { "temperature": 0.3 }
}
```

**OpenAI-shaped JSON (conceptual)**

```json
{
  "model": "gpt-4o-mini",
  "messages": [
    { "role": "system", "content": "You are a campus helpdesk bot." },
    { "role": "user", "content": "When is the fee deadline?" }
  ]
}
```

**Logic:** Your FastAPI route builds the message list from trusted server data + user input. Sanitize length; strip obvious PII if policy requires.

**Common mistake:** Letting the browser send a **system** message. Users could override “never reveal keys” instructions.

Connecting idea: After the model replies, you may return the full text at once—or **stream** it.

---

## Project layout: `campus_ai_api`

You will add a **separate small service** (or a router module) so LLM experiments do not break stable **`campus_api`** CRUD.

| File | Purpose |
| --- | --- |
| `main.py` | FastAPI app, routes, CORS |
| `schemas.py` | Pydantic models for request/response |
| `llm_client.py` | One place that talks to Gemini |
| `.env` | `GEMINI_API_KEY` |
| `requirements.txt` | `fastapi`, `uvicorn`, `httpx`, `python-dotenv` |

**Install dependencies**

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install fastapi uvicorn httpx python-dotenv
```

---

## Full code: buffered chat route

Create **`schemas.py`**

```python
from pydantic import BaseModel, Field  # Import Pydantic for request/response shapes


class ChatRequest(BaseModel):  # Body the frontend sends to your server
    question: str = Field(..., min_length=1, max_length=2000)  # Limit size for safety


class ChatResponse(BaseModel):  # Body your server returns after the model answers
    answer: str  # Plain text reply for the UI
```

Create **`llm_client.py`**

```python
import os  # Read environment variables
import httpx  # Async HTTP client for calling Gemini


GEMINI_MODEL = "gemini-2.0-flash"  # Model id used in the URL path


def _api_key() -> str:  # Central place to load the secret key
    key = os.getenv("GEMINI_API_KEY", "").strip()  # Read from environment
    if not key:  # Fail fast if developer forgot .env
        raise RuntimeError("GEMINI_API_KEY is missing from environment")  # Clear error
    return key  # Return non-empty key


async def gemini_chat(system_text: str, user_text: str, temperature: float = 0.3) -> str:
    key = _api_key()  # Load key on each call (simple pattern for class)
    url = (
        f"https://generativelanguage.googleapis.com/v1beta/models/"
        f"{GEMINI_MODEL}:generateContent?key={key}"
    )  # HTTPS endpoint for non-streaming generate
    prompt = f"System instructions:\n{system_text}\n\nUser question:\n{user_text}"  # Combine roles in one text block for simplicity
    payload = {  # JSON body expected by Gemini REST API
        "contents": [{"parts": [{"text": prompt}]}],  # Single user-style content block
        "generationConfig": {"temperature": temperature},  # Lower = steadier answers
    }
    async with httpx.AsyncClient(timeout=60.0) as client:  # Open one async client for the request
        response = await client.post(url, json=payload)  # POST JSON to provider
    if response.status_code == 429:  # Provider rate limit signal
        raise httpx.HTTPStatusError(  # Let route layer map to friendly HTTP status
            "Rate limited by provider", request=response.request, response=response
        )
    response.raise_for_status()  # Raise for other 4xx/5xx errors
    data = response.json()  # Parse JSON response body
    text = data["candidates"][0]["content"]["parts"][0]["text"]  # Extract model text safely
    return text  # Return answer string to FastAPI route
```

Create **`main.py`**

```python
from dotenv import load_dotenv  # Load .env before reading env vars

load_dotenv()  # Execute load at import time for local dev

from fastapi import FastAPI, HTTPException  # Web framework and HTTP errors
from fastapi.middleware.cors import CORSMiddleware  # Allow frontend origin in dev

from schemas import ChatRequest, ChatResponse  # Pydantic models
from llm_client import gemini_chat  # Provider call helper
import httpx  # For catching provider HTTP errors


app = FastAPI(title="campus_ai_api")  # OpenAPI title for /docs

app.add_middleware(  # CORS so browser frontend can call localhost
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500", "http://localhost:5173"],  # Adjust to your static server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SYSTEM_PROMPT = (  # Fixed server-side behaviour for every chat call
    "You are a campus helpdesk assistant. "
    "Answer in plain English. "
    "If the question needs official data you do not have, say you do not know."
)


@app.get("/health")  # Simple health check for mentors
async def health():
    return {"status": "ok"}  # JSON heartbeat


@app.post("/ai/chat", response_model=ChatResponse)  # Buffered chat endpoint
async def ai_chat(body: ChatRequest):
    try:  # Try provider call
        answer = await gemini_chat(SYSTEM_PROMPT, body.question)  # Build prompt server-side
    except httpx.HTTPStatusError as exc:  # Map provider failures
        if exc.response is not None and exc.response.status_code == 429:  # Rate limit case
            raise HTTPException(status_code=503, detail="AI is busy. Try again in a minute.")  # User-friendly
        raise HTTPException(status_code=502, detail="AI provider error")  # Generic upstream failure
    except RuntimeError as exc:  # Missing API key
        raise HTTPException(status_code=500, detail=str(exc))  # Config error for developer
    return ChatResponse(answer=answer)  # Validated response model
```

**How the code works**

- **`ChatRequest`** stops empty or huge questions before you spend tokens.
- **`SYSTEM_PROMPT`** lives only in Python—users cannot override it from the browser.
- **`gemini_chat`** is the only module that knows the provider URL and key.
- **`503`** on **429** tells the UI to retry politely instead of crashing.

**Run the server**

```bash
uvicorn main:app --reload --port 8010
```

**Test in `/docs`**

- Open `http://127.0.0.1:8010/docs`
- POST **`/ai/chat`** with `{"question": "What is a 404 error in APIs?"}`

### Activity — compare to Node lab

Call the same question with your older **`fetch`** Gemini script and with **`/ai/chat`**. Note one advantage of the FastAPI layer (key location, validation, or logging).

---

## Streaming responses

- **Official Definition:** **Streaming** delivers model output in **chunks** as they are generated instead of waiting for the full completion.
- **In Simple Words:** The answer types itself on screen.
- **Real-Life Example:** Live cricket commentary arrives ball-by-ball; you do not wait for the full match transcript.

**Why streaming matters**

| Buffered | Streamed |
| --- | --- |
| User sees spinner until entire essay finishes | User sees first words quickly |
| Simpler code | Needs **SSE** or chunked HTTP reader on frontend |
| Fine for short FAQs | Better for long explanations |

**FastAPI streaming sketch (`StreamingResponse`)**

```python
from fastapi.responses import StreamingResponse  # Stream bytes to client
import asyncio  # Sleep between demo chunks


async def fake_token_stream():  # Teaching stream before wiring provider stream
    words = ["Fee", "deadline", "is", "listed", "on", "the", "notice", "board."]  # Demo tokens
    for word in words:  # Yield one chunk at a time
        yield word + " "  # SSE/text chunk
        await asyncio.sleep(0.15)  # Small delay so UI effect is visible


@app.get("/ai/chat/stream-demo")  # Practice route (replace with real provider stream later)
async def stream_demo():
    return StreamingResponse(fake_token_stream(), media_type="text/plain")  # Plain text stream
```

**Provider note:** Gemini and OpenAI both offer **stream** flags or separate endpoints. Pattern: open long-lived response, read lines, forward to client, **flush** often.

**Common mistake:** Streaming to the browser **directly from the provider**—that exposes keys again. Stream **from your server** after the server authenticated.

**Frontend habit:** Use **`fetch` + `ReadableStream`** or EventSource if you standardise on SSE—details stay in frontend labs; this lesson focuses on the **server emitting** chunks.

---

## Rate limits and graceful handling

- **Official Definition:** A **rate limit** caps how many requests or tokens you may use per minute; providers often return HTTP **429 Too Many Requests**.
- **In Simple Words:** The kitchen asks you to wait for the next token.
- **Real-Life Example:** Railway **tatkal** windows—only so many bookings per minute.

| Symptom | Likely cause | Backend response |
| --- | --- | --- |
| HTTP **429** | Too many parallel users | Return **503** + retry message |
| Timeouts | Huge prompts | Shorten context, raise timeout carefully |
| 402 / billing errors | Quota exhausted | Alert admin, disable feature flag |

**Backoff pattern (conceptual Python)**

```python
import asyncio  # Wait between retries
import random  # Jitter so clients do not retry in sync


async def call_with_backoff(fn, max_attempts=3):  # fn is async provider call
    delay = 1.0  # Start with one second
    for attempt in range(max_attempts):  # Limited retries
        try:
            return await fn()  # Success path
        except httpx.HTTPStatusError as exc:  # Catch HTTP errors
            if exc.response is None or exc.response.status_code != 429:  # Non-rate errors bubble up
                raise  # Stop retrying
            if attempt == max_attempts - 1:  # Last attempt failed
                raise  # Give up
            await asyncio.sleep(delay + random.random())  # Wait with jitter
            delay *= 2  # Exponential backoff
```

**Logic:** Never tight-loop retries on 429—that amplifies outages.

**Product choices:** Queue heavy jobs, cache frequent answers (“What are library hours?”), show “AI busy” banner during fest traffic.

---

## Wiring the frontend (pattern only)

Your static page should **`fetch`** your backend:

```javascript
const response = await fetch("http://127.0.0.1:8010/ai/chat", {  // Your FastAPI URL
  method: "POST",  // JSON body
  headers: { "Content-Type": "application/json" },  // Tell server we send JSON
  body: JSON.stringify({ question: userText }),  // Pydantic field name must match
});
const data = await response.json();  // Parse ChatResponse
console.log(data.answer);  // Show in UI
```

**How the code works**

- No **`GEMINI_API_KEY`** in this file.
- Field name **`question`** matches **`ChatRequest`**.
- Errors surface as HTTP status—you can show mentor-approved messages.

---

## Observability without leaking secrets

| Log | OK? |
| --- | --- |
| Route name, latency, token estimate | Yes |
| User question (if policy allows) | Maybe—check privacy |
| Full API key | Never |
| Provider response id | Yes—for support tickets |

**Common doubt:** “Should we save every chat in SQL?” — Only if product needs history; plan tables in capstone design later, not in this lesson’s scope.

---

## Errors you will see in class

| Error | Meaning | Fix |
| --- | --- | --- |
| `GEMINI_API_KEY is missing` | `.env` not loaded | `load_dotenv()` + restart uvicorn |
| **401/403** from provider | Bad or revoked key | Regenerate key in console |
| **404** model | Wrong model string | Match console model id |
| CORS browser error | Origin not allowed | Add your static server origin |
| Empty `candidates` | Safety block or bad payload | Log `data`, shorten prompt |

---

## What this lesson deliberately does not cover

Richer provider features—**JSON schema responses**, **image inputs**, **embedding vectors**, and **multimodal** pipelines—belong in the **next** lesson so each file stays focused. Capstone **route planning** and **auth design** come later in the module.

---

## Hands-on checklist

1. Create **`campus_ai_api`** with the three Python files and a working **`.env`**.
2. Prove **`/health`** and **`/ai/chat`** in `/docs` with two different questions.
3. Move **`temperature`** to `0.0` vs `0.8` for the same question; note tone change.
4. Temporarily remove the API key and confirm the API returns a clear **500** config error—not a provider stack trace to users.
5. Hit **`/ai/chat/stream-demo`** in the browser and watch partial text arrive.
6. Document one **429** handling rule your team will use during demo week.

---

## Key Takeaways

- **LLM APIs** are normal HTTPS dependencies—treat keys like database passwords and keep them on the server.
- **Chat APIs** formalise **system / user / assistant** roles you already practiced as prompt blocks.
- A thin **FastAPI** layer adds validation, CORS, logging, and stable JSON for your frontend.
- **Streaming** improves perceived speed; **rate limits** require backoff and honest user messaging.
- Upcoming lessons add **typed**, **visual**, and **searchable** AI outputs on top of this integration base.

## Important Commands, Libraries, Terminologies used

| Name | Meaning in this lesson |
| --- | --- |
| **LLM API** | Hosted model reachable over HTTPS with an API key |
| **OpenAI / Gemini / Claude** | Major providers with similar integration steps |
| **API key** | Secret credential stored in `.env` on the server |
| **`GEMINI_API_KEY`** | Environment variable for Google Gemini calls |
| **Chat API** | Endpoint accepting a list of role-tagged messages |
| **system / user / assistant** | Roles in a chat transcript |
| **`campus_ai_api`** | Practice FastAPI service for AI routes |
| **`ChatRequest` / `ChatResponse`** | Pydantic models for `/ai/chat` |
| **`httpx.AsyncClient`** | Async HTTP client for provider calls |
| **`generateContent`** | Gemini REST action used for buffered replies |
| **Buffered response** | Wait for full model text before returning |
| **StreamingResponse** | FastAPI helper to send chunks as they arrive |
| **HTTP 429** | Rate limit status from provider |
| **Exponential backoff** | Increasing wait between retries |
| **CORS** | Browser permission for cross-origin API calls |
| **`uvicorn`** | ASGI server running FastAPI |
| **`load_dotenv()`** | Loads `.env` into environment variables |
| **Upstream / downstream** | Provider = upstream; browser = downstream client |
