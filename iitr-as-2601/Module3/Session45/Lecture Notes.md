# Prompt Versioning & API Rate Limits

## Introduction

In the previous session, you learned how **tokens**, **context windows**, **temperature**, and **truncation** shape what users see from an LLM product. Those internals explain *why* a prompt costs money, slows down, or forgets earlier turns.

This session shifts from *what goes inside one request* to *how you manage prompts over time* and *how you call APIs safely during development*. You will learn to **version** prompts and configs like code, **compare** two versions on the same test questions, and **respect rate limits** with **retries**, **backoff**, and **visible logs**.

**What you will learn:**

- **Store** prompts and tool configs in **versioned files** or a simple **registry pattern**
- **Compare** two prompt versions against the same **eval questions** (qualitative review)
- **Explain** **HTTP rate limits** and implement **exponential backoff** on API errors
- **Log** retry events so failures are visible while you build and debug

---

## Why Prompts Need Versioning

A prompt is not a one-time sticky note — it is **living product logic**. When you change wording, temperature, or tool rules, behaviour changes even if the model name stays the same.

- **Official Definition:** **Prompt versioning** is the practice of tracking, naming, and storing each revision of a prompt (and related config) so you can reproduce, compare, and roll back behaviour.
- **In Simple Words:** Treat prompts like **recipe versions** in your family's notebook — *"Paneer butter masala v1 (mild)"* vs *"v2 (extra spice)"* — so you know which version guests liked.
- **Real-Life Example:** A **Zomato restaurant** updates its menu card. If they erase the old card, nobody remembers what changed when complaints rise. Saving **v1** and **v2** side by side lets the team compare.

| Without versioning | With versioning |
|---|---|
| "It worked yesterday" — no proof | Same eval questions run on **v1** and **v2** |
| Teammate edits a shared Google Doc silently | **`prompts/support_v2.txt`** checked into your project folder |
| Bug reports cannot be reproduced | You reload **exact** prompt file + config from that date |

- **Common mistake:** Editing the system prompt **inline in a notebook cell** without saving the old text — you lose the baseline forever.
- **Design habit:** Every meaningful prompt change gets a **new version label** (`v1`, `v2`, or a date stamp) — even for small wording tweaks that affect tone or grounding rules.

---

## Storing Prompts in Versioned Files

The simplest production-ready pattern for beginners is **one file per version** inside a clear folder structure. No database required.

- **Official Definition:** A **versioned file layout** stores each prompt revision as a separate file (often with a version suffix or subfolder) alongside a small **config** file for model settings.
- **In Simple Words:** Like keeping **`Diwali_2024.jpg`** and **`Diwali_2025.jpg`** in the same album — both visible, neither overwrites the other.
- **Real-Life Example:** An **IRCTC** ticket PDF is saved with **PNR + date** in the filename so you can open the exact booking later — prompts deserve the same discipline.

### Recommended Folder Layout

```
project/
├── prompts/
│   ├── support_agent/
│   │   ├── v1_system.txt
│   │   ├── v2_system.txt
│   │   └── eval_questions.txt
│   └── summarizer/
│       └── v1_system.txt
├── config/
│   ├── support_agent_v1.yaml
│   └── support_agent_v2.yaml
└── logs/
    └── api_retries.log
```

- **`prompts/`** holds the **text** the model reads — system instructions, grounding rules, few-shot examples.
- **`config/`** holds **numbers and switches** — model name, `temperature`, `max_tokens`, tool names — separate from prose so designers and developers can edit safely.
- **`logs/`** captures **retry and failure events** during development (covered later in this document).

- **Why separate config from prompt text:** Wording changes often; model name or temperature changes less often. Mixing both in one giant string makes diffs hard to read.
- **Common doubt:** *"Is a `.txt` file enough?"* — Yes for learning and small teams. A **registry** (next section) wraps files when you have many prompts.

### Loading a Versioned Prompt in Python

```python
# load_prompt.py — read a specific prompt version from disk

from pathlib import Path  # Built-in library for clean file paths

# Root folder where all prompt files live
PROMPTS_DIR = Path("prompts/support_agent")  # Folder for one agent's prompts

def load_prompt(version: str) -> str:
    """Load system prompt text for a given version label like 'v1' or 'v2'."""
    file_path = PROMPTS_DIR / f"{version}_system.txt"  # Build path: prompts/support_agent/v1_system.txt
    if not file_path.exists():  # Stop early if someone typo'd the version name
        raise FileNotFoundError(f"No prompt file found: {file_path}")
    return file_path.read_text(encoding="utf-8").strip()  # Read full file as one string


def load_config(version: str) -> dict:
    """Load YAML-style settings for this prompt version (simple dict for demo)."""
    # In real projects use PyYAML; here we use a plain dict keyed by version
    CONFIGS = {
        "v1": {"model": "llama-3.3-70b-versatile", "temperature": 0.0, "max_tokens": 512},
        "v2": {"model": "llama-3.3-70b-versatile", "temperature": 0.0, "max_tokens": 512},
    }
    if version not in CONFIGS:
        raise KeyError(f"Unknown config version: {version}")
    return CONFIGS[version]


# Example usage — load v1 prompt and its matching config
active_version = "v1"  # Change to "v2" to switch behaviour deliberately
system_prompt = load_prompt(active_version)  # String sent as system message to the API
settings = load_config(active_version)  # Dict with model name and temperature
print(f"Loaded {active_version}: {len(system_prompt)} characters, temp={settings['temperature']}")
```

**How the code works:**

- **`Path`** builds cross-platform paths — works on Windows lab machines and Mac laptops alike.
- **`load_prompt`** maps a **version label** to exactly one file — switching versions is one string change, not a hunt through notebook cells.
- **`load_config`** keeps **model settings** out of the prose prompt — same pattern teams use before moving to YAML files.
- **`FileNotFoundError`** and **`KeyError`** fail fast during development instead of sending a blank system prompt to the API.

### Sample Prompt Files (v1 vs v2)

**`prompts/support_agent/v1_system.txt`**

```
You are ShopEasy Support Bot. Answer ONLY from the provided context.
If the answer is not in the context, say: "I don't have that information."
Keep replies under 3 sentences. Use polite Indian English.
```

**`prompts/support_agent/v2_system.txt`**

```
You are ShopEasy Support Bot. Answer ONLY from the provided context.
If the answer is not in the context, say: "I don't have that information."
Keep replies under 3 sentences. Use polite Indian English.
Always end with: "Need anything else? Reply with your order ID."
```

- **v2** adds one **closing line** — small diff, potentially big UX change. Version files make that diff visible in `git diff`.

---

## The Simple Registry Pattern for Prompts and Tool Configs

When one project holds **many agents** (support, summarizer, email drafter), a flat folder still works — but a **registry** gives you one lookup table: *name → version → file path + config*.

- **Official Definition:** A **registry pattern** is a central map (Python dict, JSON file, or module) that registers named resources — here, **prompt versions** and **tool configs** — so application code asks for `"support_agent/v2"` instead of hard-coding paths.
- **In Simple Words:** Like a **school timetable** — instead of every student guessing which room is Period 3, one chart says *"Period 3 = Room 204, Maths"*.
- **Real-Life Example:** A **Big Bazaar** store directory at the entrance — *"Electronics → Floor 2, West wing"* — one lookup, no wandering.

| Piece | Stored in registry | Example key |
|---|---|---|
| System prompt file path | `prompt_path` | `prompts/support_agent/v2_system.txt` |
| Model settings | `config` | `temperature=0`, `max_tokens=512` |
| Tool definitions | `tools` | List of JSON schemas for function calling |
| Active default version | `default_version` | `"v2"` |

- **Tool configs in the registry:** Register not just Python functions but **which tools this agent may call** and **max steps** — same place as the prompt version so one `"support_agent/v2"` entry is complete.
- **Common mistake:** Registry points to **`v2` prompt** but code still loads **`v1` config** — always register **prompt + config + tools** as one bundle.

### Full Registry Example

```python
# prompt_registry.py — central map for prompts, configs, and tool settings

from pathlib import Path  # File path helper

REGISTRY = {
    "support_agent": {
        "v1": {
            "prompt_path": Path("prompts/support_agent/v1_system.txt"),
            "config": {
                "model": "llama-3.3-70b-versatile",
                "temperature": 0.0,
                "max_tokens": 512,
            },
            "tools": ["lookup_order"],  # Tool names this agent may call
            "max_tool_steps": 3,
        },
        "v2": {
            "prompt_path": Path("prompts/support_agent/v2_system.txt"),
            "config": {
                "model": "llama-3.3-70b-versatile",
                "temperature": 0.0,
                "max_tokens": 512,
            },
            "tools": ["lookup_order"],
            "max_tool_steps": 3,
        },
    },
    "summarizer": {
        "v1": {
            "prompt_path": Path("prompts/summarizer/v1_system.txt"),
            "config": {
                "model": "llama-3.3-70b-versatile",
                "temperature": 0.2,
                "max_tokens": 256,
            },
            "tools": [],  # No tools — plain text summarization
            "max_tool_steps": 0,
        },
    },
}


def get_agent_bundle(agent_name: str, version: str) -> dict:
    """Return prompt text, config, and tool list for one agent version."""
    if agent_name not in REGISTRY:
        raise KeyError(f"Unknown agent: {agent_name}")
    versions = REGISTRY[agent_name]
    if version not in versions:
        raise KeyError(f"Unknown version {version} for agent {agent_name}")
    entry = versions[version]  # Single registry row
    prompt_text = entry["prompt_path"].read_text(encoding="utf-8").strip()  # Load prompt from disk
    return {
        "system_prompt": prompt_text,
        "config": entry["config"],
        "tools": entry["tools"],
        "max_tool_steps": entry["max_tool_steps"],
        "version_label": f"{agent_name}/{version}",
    }


# Example — load support agent v2 in one call
bundle = get_agent_bundle("support_agent", "v2")
print(bundle["version_label"], "tools:", bundle["tools"])
```

**How the code works:**

- **`REGISTRY`** is the **single source of truth** — add a new agent by adding a nested dict, not by scattering paths across notebooks.
- Each version entry bundles **`prompt_path`**, **`config`**, **`tools`**, and **`max_tool_steps`** — prevents half-updated deployments.
- **`get_agent_bundle`** reads the file at call time — edit `v2_system.txt`, rerun, and behaviour updates without touching executor code.
- **`KeyError`** guards typos in agent or version names before any API call burns tokens.

---

## Comparing Two Prompt Versions (Qualitative Eval)

Before you ship **v2**, run the **same questions** through **v1** and **v2** and compare answers side by side. This is **qualitative eval** — human judgment on tone, grounding, and completeness, not a single accuracy score.

- **Official Definition:** **Qualitative evaluation** compares model outputs on a fixed **eval set** using structured human review criteria (faithfulness, brevity, tone) rather than automated metrics alone.
- **In Simple Words:** Like tasting **two batches of chai** with the same recipe tweak — same cups, same sip order, note which one is sweeter.
- **Real-Life Example:** **Board exam answer sheets** — two students answer the **same five questions**; the teacher compares clarity and correctness question by question.

| Eval question type | What to watch for |
|---|---|
| **Grounded fact** | Does it stay inside provided context? |
| **Missing info** | Does it admit *"I don't know"* instead of guessing? |
| **Tone / length** | Under 3 sentences? Polite closing in v2 only? |
| **Tool trigger** | Does it call `lookup_order` when an order ID appears? |

- **Eval set size:** Start with **5–10 questions** — enough to spot regressions, small enough to review in one sitting.
- **Same context for both versions:** Pass identical **RAG chunks** or **tool mocks** — otherwise you are comparing apples and oranges.
- **Common mistake:** Changing **temperature** and **prompt text** at the same time — you cannot tell which change fixed the bug. Change **one knob per version**.

### Eval Questions File

**`prompts/support_agent/eval_questions.txt`** (one question per line)

```
What is the return window for electronics?
My order ORD-9912 shows delivered but I received nothing.
Can I exchange a shirt bought during the Diwali sale?
What is ShopEasy's CEO's personal phone number?
Summarize the warranty policy for laptops in one sentence.
```

- The last question tests **grounding** — if CEO phone is not in context, both versions should refuse politely.

### Side-by-Side Comparison Script

```python
# compare_prompt_versions.py — run v1 and v2 on the same eval questions

import os  # Read API key from environment
import time  # Pause between eval API calls to avoid rate limits
from groq import Groq  # Groq Python SDK for LLM calls
from prompt_registry import get_agent_bundle  # Registry from previous section

# Fixed context chunk — same for every eval question so comparison is fair
FAKE_CONTEXT = """
ShopEasy policies (2025):
- Electronics returns: 7 days from delivery if unopened.
- Clothing exchanges: 15 days with tags attached.
- Diwali sale items follow the same return rules as regular items unless marked 'final sale'.
- Warranty: laptops have 1-year manufacturer warranty; contact brand service for claims.
- ShopEasy support email: help@shopeasy.in (no phone support for order lookup).
"""

EVAL_FILE = "prompts/support_agent/eval_questions.txt"  # Path to eval questions


def build_user_message(question: str) -> str:
    """Wrap question with context — identical wrapper for v1 and v2."""
    return f"Context:\n{FAKE_CONTEXT}\n\nQuestion: {question}"


def call_groq(client, system_prompt: str, config: dict, user_message: str) -> str:
    """Single Groq chat completion — temperature from config."""
    response = client.chat.completions.create(
        model=config["model"],  # Model name from registry config
        messages=[
            {"role": "system", "content": system_prompt},  # Versioned system prompt
            {"role": "user", "content": user_message},  # Question + shared context
        ],
        temperature=config["temperature"],  # Keep 0 for stable comparison
        max_tokens=config["max_tokens"],
    )
    return response.choices[0].message.content.strip()  # Assistant reply text


def load_eval_questions(path: str) -> list:
    """Read non-empty lines from eval file."""
    with open(path, encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]  # Skip blank lines


def compare_versions(questions: list) -> None:
    """Print v1 vs v2 answers for each question."""
    client = Groq(api_key=os.environ["GROQ_API_KEY"])  # API key from env var, never hard-coded
    v1 = get_agent_bundle("support_agent", "v1")  # Load v1 bundle from registry
    v2 = get_agent_bundle("support_agent", "v2")  # Load v2 bundle from registry

    for idx, question in enumerate(questions, start=1):
        user_msg = build_user_message(question)  # Same context + question for both
        ans_v1 = call_groq(client, v1["system_prompt"], v1["config"], user_msg)
        ans_v2 = call_groq(client, v2["system_prompt"], v2["config"], user_msg)
        print("=" * 60)
        print(f"Q{idx}: {question}")
        print(f"--- v1 ---\n{ans_v1}")
        print(f"--- v2 ---\n{ans_v2}")
        print()  # Blank line between questions
        time.sleep(1)  # Polite pause — reduces 429 when running many eval calls on one org key


if __name__ == "__main__":
    questions = load_eval_questions(EVAL_FILE)  # Load fixed eval set
    compare_versions(questions)  # Run full comparison
```

**How the code works:**

- **`FAKE_CONTEXT`** is shared — any difference in answers comes from **prompt version**, not from different retrieval results.
- **`build_user_message`** uses one template — eval fairness rule enforced in code.
- **`compare_versions`** loads both bundles from the **registry** — no duplicate path strings in the loop.
- Printing **`--- v1 ---`** and **`--- v2 ---`** blocks makes paste-into-spreadsheet or screenshot review easy during lab time.

### Qualitative Review Checklist

After running the script, score each pair manually:

| Criterion | v1 (Y/N) | v2 (Y/N) | Notes |
|---|---|---|---|
| Stays inside context | | | |
| Refuses unknown facts cleanly | | | |
| Meets length rule (≤3 sentences) | | | |
| v2 closing line present (v2 only) | | | |

- **Ship rule of thumb:** **v2** must be **equal or better on every must-have row** — if v2 wins on tone but loses on grounding, keep v1 as default until fixed.
- **Save outputs:** Copy console output to **`logs/eval_v1_vs_v2_2025-06-14.txt`** — becomes evidence in stand-up or code review.

> **Activity 1 — Run a Two-Version Eval**
>
> 1. Create **`v1_system.txt`** and **`v2_system.txt`** with one deliberate difference (like the closing line above).
> 2. Write **five eval questions** in **`eval_questions.txt`**, including one **unanswerable** question from context.
> 3. Run the comparison script (or call the API twice per question manually if SDK setup is pending).
> 4. Fill the **qualitative checklist** for each question. Decide: **keep v1**, **promote v2**, or **draft v3**.
> 5. Write one sentence: *"v2 is better/worse because ___ on question Q3."*

---

## HTTP Rate Limits — What Happens When APIs Say "Slow Down"

Cloud LLM APIs protect shared infrastructure with **rate limits** — caps on how many requests or tokens you can use per minute, hour, or day.

- **Official Definition:** An **HTTP rate limit** is a server-enforced quota on request frequency or token volume; exceeding it returns status **`429 Too Many Requests`** (or provider-specific error codes in the response body).
- **In Simple Words:** Like **RTO office token counters** — only **N people per hour** get served; arrive too fast and you wait for the next batch.
- **Real-Life Example:** **UPI apps** during sale hour — *"Bank server busy, try again"* appears when the backend throttle trips, not because your phone is broken.

| Limit type | Typical meaning | What triggers it in agent dev |
|---|---|---|
| **Requests per minute (RPM)** | Too many API calls in 60 seconds | ReAct loop with 8+ steps in one minute |
| **Tokens per minute (TPM)** | Too many input+output tokens/minute | Fat RAG prompt + long history in a tight loop |
| **Daily quota** | Org-wide cap resets every 24h | Running class demos all day on one free-tier key |

- **HTTP 429:** Standard signal — *"Slow down or wait."* Not the same as **401** (bad key) or **500** (server crash).
- **Response headers:** Many providers send **`Retry-After`** (seconds to wait) — polite clients read it before sleeping.
- **Agent multiplier:** One user message can become **5–15 API calls** in a tool loop — rate limits bite faster than in single-turn chat.

- **Common mistake:** Hammering the API in a **`for` loop** with **no delay** — you burn the quota and teach bad habits before production.
- **Designer note:** Show users a **friendly wait message** when retries happen — not a raw *"429"* string.

---

## Exponential Backoff and Retries

When a call fails with a **retryable** error (429, transient 503), wait before trying again — and increase the wait after each failure. That pattern is **exponential backoff**.

- **Official Definition:** **Exponential backoff** retries a failed operation after delays that grow exponentially (e.g. 1s, 2s, 4s, 8s), often with **jitter** (small random extra delay) to avoid synchronized retries from many clients.
- **In Simple Words:** Like knocking on a friend's door — wait longer between knocks if they do not answer, instead of banging every second.
- **Real-Life Example:** **IRCTC Tatkal** — if the site errors, you wait and retry later; wise users do not refresh 50 times per second.

| Attempt | Base delay (seconds) | With jitter (example) |
|---|---|---|
| 1 | 1 | 1.0 – 1.3 |
| 2 | 2 | 2.0 – 2.5 |
| 3 | 4 | 4.0 – 4.8 |
| 4 | 8 | 8.0 – 9.0 |
| Stop | Max attempts reached | Surface error to developer / user |

- **Retry only retryable errors:** **429**, **503**, timeouts — not **401** (fix your key) or **400** (fix your JSON).
- **Cap max attempts:** **`max_retries=4`** is enough for dev — infinite retry hides broken code.
- **Jitter:** Add **`random.uniform(0, 0.3) * delay`** so ten notebook users do not retry in perfect sync.

### Full Backoff Wrapper

```python
# groq_with_backoff.py — call Groq with exponential backoff on rate limits

import os  # Environment variables for API key
import time  # sleep between retries
import random  # jitter so retries spread out
import logging  # log each retry for visibility (next section)
from groq import Groq  # Groq SDK
from groq import RateLimitError  # Specific exception for 429-style failures

# Configure logging to file + console — details in "Logging Retry Events" section
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("logs/api_retries.log", encoding="utf-8"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger("groq_backoff")


def groq_chat_with_backoff(messages, model, temperature=0.0, max_tokens=512, max_retries=4):
    """
    Call Groq chat completions with exponential backoff on rate limit errors.
    Returns assistant text string; raises last error if all retries fail.
    """
    client = Groq(api_key=os.environ["GROQ_API_KEY"])  # Fresh client each call (simple demo pattern)
    last_error = None  # Remember final exception for re-raise

    for attempt in range(max_retries + 1):  # attempt 0 = first try, then up to max_retries waits
        try:
            response = client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
            )
            return response.choices[0].message.content.strip()  # Success — exit function

        except RateLimitError as err:
            last_error = err  # Save for possible re-raise after loop
            if attempt == max_retries:  # No retries left
                logger.error("Rate limit: all %s retries exhausted", max_retries)
                break
            base_delay = 2 ** attempt  # 1, 2, 4, 8 seconds for attempts 0,1,2,3
            jitter = random.uniform(0, 0.3) * base_delay  # Random extra fraction of base
            wait_seconds = base_delay + jitter
            logger.warning(
                "Rate limit hit (attempt %s/%s). Sleeping %.2fs before retry.",
                attempt + 1,
                max_retries,
                wait_seconds,
            )
            time.sleep(wait_seconds)  # Pause before next attempt

        except Exception as err:
            # Non-rate-limit errors should not backoff blindly — re-raise immediately
            logger.exception("Non-retryable API error: %s", err)
            raise

    raise last_error  # Propagate last RateLimitError if every attempt failed


# Example usage with a versioned system prompt loaded from registry
if __name__ == "__main__":
    from prompt_registry import get_agent_bundle

    bundle = get_agent_bundle("support_agent", "v1")  # Load prompt + config
    messages = [
        {"role": "system", "content": bundle["system_prompt"]},
        {"role": "user", "content": "What is the electronics return window?"},
    ]
    answer = groq_chat_with_backoff(
        messages=messages,
        model=bundle["config"]["model"],
        temperature=bundle["config"]["temperature"],
        max_tokens=bundle["config"]["max_tokens"],
    )
    print(answer)
```

**How the code works:**

- **`RateLimitError`** is caught specifically — other exceptions fail fast without useless waits.
- **`2 ** attempt`** doubles wait time each retry — classic exponential curve.
- **`jitter`** spreads retry times when many students share a classroom API org.
- **`logger.warning`** on each retry makes invisible waits **visible** in terminal and log file.
- **`max_retries`** bounds total pain — after exhaustion, caller can show a friendly user message.

> **Activity 2 — Observe Backoff Without Burning Quota**
>
> 1. Run the **mock backoff demo** below — it simulates **`RateLimitError`** twice, then succeeds (no real API quota used).
> 2. Open **`logs/api_retries.log`** and confirm **attempt numbers** and **wait_s** values grow (1s range, then 2s range).
> 3. Answer in one line: *"Without backoff, my loop would have sent ___ extra failing requests."*

### Mock Backoff Demo (No Real API Calls)

```python
# mock_backoff_demo.py — practice exponential backoff without hitting Groq

import time
import random
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("logs/api_retries.log", encoding="utf-8"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger("mock_backoff")


class FakeRateLimitError(Exception):
    """Stand-in for Groq RateLimitError during local practice."""
    pass


def fake_api_call(attempt_counter: dict) -> str:
    """Pretend API: fail twice, succeed on third try."""
    attempt_counter["n"] += 1
    if attempt_counter["n"] <= 2:
        raise FakeRateLimitError("simulated 429")
    return "Mock success — return policy is 7 days for electronics."


def run_mock_backoff(max_retries=4):
    attempt_counter = {"n": 0}
    last_error = None
    for attempt in range(max_retries + 1):
        try:
            return fake_api_call(attempt_counter)
        except FakeRateLimitError as err:
            last_error = err
            if attempt == max_retries:
                logger.error("Mock rate limit: all retries exhausted")
                break
            base_delay = 2 ** attempt
            jitter = random.uniform(0, 0.3) * base_delay
            wait_seconds = base_delay + jitter
            logger.warning(
                "Mock rate limit (attempt %s/%s). Sleeping %.2fs.",
                attempt + 1,
                max_retries,
                wait_seconds,
            )
            time.sleep(wait_seconds)
    raise last_error


if __name__ == "__main__":
    print(run_mock_backoff())
```

**How the code works:**

- **`FakeRateLimitError`** lets you practice the same **`try/except`** flow without an API key.
- **`attempt_counter`** tracks how many times the fake API was called — you should see **3 calls** total (2 failures + 1 success).
- Backoff math matches the real **`groq_chat_with_backoff`** function — skills transfer directly when you swap in Groq.

---

## Logging Retry Events During Development

Retries that happen silently feel like **random slowness**. During development, **log every retry** with timestamp, attempt number, wait time, and error type.

- **Official Definition:** **Retry logging** records structured events each time an API client waits and retries after a failure, so developers can audit throttling during builds and demos.
- **In Simple Words:** Like a **shop ledger** — every time the shutter was down and you reopened, write the time and reason.
- **Real-Life Example:** **Swiggy** order tracking shows *"Restaurant is busy"* — you see delay cause; dev logs do the same for your API layer.

| Log field | Why include it |
|---|---|
| **Timestamp** | Correlate with demo time or cron job |
| **Attempt `k` of `N`** | Spot loops that always hit max retries |
| **Sleep seconds** | Verify backoff math |
| **Error type / status** | Distinguish 429 vs 503 vs timeout |
| **Prompt version label** | Know which agent config was active |

- **Log destination:** **`logs/api_retries.log`** file for persistence; **console** for live notebook feedback.
- **Do not log secrets:** Never write full **API keys** or **PII** — log order IDs only if policy allows.
- **Common mistake:** **`print("retrying...")`** without timestamps — useless when reviewing yesterday's class run.

### Structured Retry Logger Helper

```python
# retry_logger.py — small helper to standardize retry log lines

import logging  # Standard library logging
from datetime import datetime, timezone  # UTC timestamps for consistent logs

logger = logging.getLogger("api_retries")


def log_retry_event(
    service: str,
    attempt: int,
    max_retries: int,
    wait_seconds: float,
    error_name: str,
    prompt_version: str = "unknown",
) -> None:
    """Write one structured retry line — call before time.sleep in backoff."""
    message = (
        f"service={service} | version={prompt_version} | "
        f"attempt={attempt}/{max_retries} | wait_s={wait_seconds:.2f} | error={error_name}"
    )
    logger.warning(message)  # WARNING level — visible but not confused with crash ERROR


def log_retry_success(service: str, prompt_version: str, total_attempts: int) -> None:
    """Log when a call succeeds after one or more retries."""
    logger.info(
        "service=%s | version=%s | recovered_after_attempts=%s",
        service,
        prompt_version,
        total_attempts,
    )


def log_retry_exhausted(service: str, prompt_version: str, error_name: str) -> None:
    """Log when all retries failed — developer must investigate."""
    logger.error(
        "service=%s | version=%s | retries_exhausted | last_error=%s",
        service,
        prompt_version,
        error_name,
    )


# Example log lines you should see in logs/api_retries.log after a throttled demo:
# 2025-06-14 10:15:02,441 | WARNING | service=groq | version=support_agent/v2 | attempt=1/4 | wait_s=1.12 | error=RateLimitError
# 2025-06-14 10:15:03,601 | INFO    | service=groq | version=support_agent/v2 | recovered_after_attempts=2
```

**How the code works:**

- **`log_retry_event`** builds one **parseable line** — grep-friendly in large log files.
- **`prompt_version`** ties throttling to **registry label** — essential when v2 suddenly adds longer outputs and hits TPM faster.
- **`log_retry_success`** confirms recovery — without it, you only see problems, not happy endings.
- **`log_retry_exhausted`** at **ERROR** level flags configs that need slower loops or higher quotas.

### Reading Logs During Debug

```python
# tail_retries.py — print last 10 retry lines from today's development

from pathlib import Path

LOG_PATH = Path("logs/api_retries.log")

if LOG_PATH.exists():
    lines = LOG_PATH.read_text(encoding="utf-8").strip().splitlines()
    for line in lines[-10:]:  # Last 10 events only
        print(line)
else:
    print("No retry log yet — run groq_with_backoff.py first.")
```

**How the code works:**

- Quick **tail** script for lab — no extra tools required on Windows or Mac.
- Empty log means either **no throttling yet** (good) or **logging not wired** (check handlers).

> **Activity 3 — Build a Retry Audit Trail**
>
> 1. Wire **`log_retry_event`** into your backoff function (replace inline `logger.warning` if you prefer the helper).
> 2. Run **three eval questions** in a row through **`groq_chat_with_backoff`**, loading **`support_agent/v2`** from the registry.
> 3. Open **`logs/api_retries.log`** and highlight any line with **`retries_exhausted`** — if none, note total **`attempt=`** counts.
> 4. Write a **three-bullet mini-report**: (a) how many retries happened, (b) longest wait, (c) one change you would make if this were a live demo (e.g. pause between eval questions).

---

## Putting It Together — A Resilient Prompt Pipeline

A mature **development** flow connects all pieces:

```
[Registry: agent + version]
        ↓
[Load prompt file + config + tools]
        ↓
[Eval script OR production caller]
        ↓
[groq_chat_with_backoff + retry logs]
        ↓
[Qualitative review → promote version]
```

| Stage | Artifact | Purpose |
|---|---|---|
| **Design** | `v2_system.txt` diff from v1 | Visible wording change |
| **Register** | `REGISTRY["support_agent"]["v2"]` | One bundle for code |
| **Evaluate** | `eval_questions.txt` + checklist | Human gate before default switch |
| **Operate** | Backoff + `api_retries.log` | Survive 429 during demos |
| **Promote** | Set `default_version = "v2"` in registry | Team agrees v2 wins eval |

- **Change discipline:** Version bump → eval → log review → promote — skip eval only for typo fixes that cannot affect behaviour.
- **Rate limit hygiene:** Space eval loops with **`time.sleep(1)`** between questions in shared org keys — backoff is for failures, politeness is for prevention.
- **Link to token budgeting:** Shorter prompts (from your earlier internals work) reduce **TPM** pressure — versioning and token trimming work together.

### End-to-End Demo Script (Condensed)

```python
# dev_pipeline_demo.py — registry load, eval one question, backoff, logging

import os
import time
from prompt_registry import get_agent_bundle
from groq_with_backoff import groq_chat_with_backoff

CONTEXT = "Electronics returns: 7 days if unopened."
QUESTION = "How long can I return a laptop?"


def run_one_eval(agent: str, version: str) -> str:
    """Load bundle, call API with backoff, return answer."""
    bundle = get_agent_bundle(agent, version)
    version_label = bundle["version_label"]
    user_content = f"Context:\n{CONTEXT}\n\nQuestion: {QUESTION}"
    messages = [
        {"role": "system", "content": bundle["system_prompt"]},
        {"role": "user", "content": user_content},
    ]
    answer = groq_chat_with_backoff(
        messages=messages,
        model=bundle["config"]["model"],
        temperature=bundle["config"]["temperature"],
        max_tokens=bundle["config"]["max_tokens"],
    )
    return answer


if __name__ == "__main__":
    for ver in ("v1", "v2"):
        print(f"--- {ver} ---")
        print(run_one_eval("support_agent", ver))
        time.sleep(1)  # Polite gap between calls on shared dev keys
```

**How the code works:**

- **`get_agent_bundle`** ensures eval uses the same paths as production code — no notebook-only shortcuts.
- **`groq_chat_with_backoff`** centralizes retry policy — change backoff once, all callers benefit.
- **`time.sleep(1)`** between v1 and v2 calls reduces avoidable 429 during classroom demos.
- **`time.sleep(1)`** between v1 and v2 calls reduces avoidable 429 during classroom demos.
- **`get_agent_bundle`** keeps eval and demo paths identical — no notebook-only shortcuts.

---

## Key Takeaways

- **Prompt versioning** saves every revision in **named files** or a **registry bundle** — prompt text, config, and tools stay together so rollbacks are possible.
- **Qualitative eval** runs the **same questions** with the **same context** on two versions — use a checklist before promoting **v2** to default.
- **HTTP 429 rate limits** are normal when agents loop fast or many developers share one org key — they mean *wait*, not *rewrite your prompt*.
- **Exponential backoff with jitter** and a **max retry cap** turn transient failures into recoverable delays instead of crash loops.
- **Retry logs** with timestamps and **version labels** make invisible waits visible — essential for debugging demos and shared dev environments.

These habits prepare you for **structured evaluation**, **orchestration**, and **deployment** topics where prompts, configs, and API policies must stay traceable as systems grow.

---

## Important Commands, Libraries, and Terminologies

| Term / Command | Type | Meaning |
|---|---|---|
| **Prompt versioning** | Practice | Tracking named revisions of prompts and configs |
| **Versioned file layout** | Pattern | One file per version (`v1_system.txt`, `v2_system.txt`) |
| **Registry pattern** | Pattern | Central map: agent name + version → paths and settings |
| **`get_agent_bundle()`** | Code pattern | Load prompt, config, tools for one registry entry |
| **Qualitative eval** | Process | Same questions, human-reviewed comparison of outputs |
| **Eval set** | Artifact | Fixed list of test questions (`eval_questions.txt`) |
| **HTTP 429** | Status code | Too Many Requests — rate limit exceeded |
| **RPM / TPM** | Limits | Requests or tokens allowed per minute |
| **Retry-After** | HTTP header | Server hint for seconds to wait before retry |
| **Exponential backoff** | Pattern | Delays grow as 1s, 2s, 4s, 8s between retries |
| **Jitter** | Pattern | Random extra delay to desynchronize retries |
| **`RateLimitError`** | Exception | Groq SDK signal for throttling — catch for backoff |
| **`max_retries`** | Config | Cap on retry attempts before surfacing failure |
| **`logging.FileHandler`** | Code | Persist log lines to `logs/api_retries.log` |
| **`log_retry_event`** | Code pattern | Structured WARNING line before each sleep |
| **`time.sleep()`** | Code | Pause between retries or eval questions |
| **`pathlib.Path`** | Library | Safe file paths for prompt loading |
| **`GROQ_API_KEY`** | Env var | API key read from environment, not source code |
| **Promote version** | Workflow | Set winning version as registry default after eval |
| **Retry audit trail** | Log habit | Timestamp + attempt + version for every retry |
