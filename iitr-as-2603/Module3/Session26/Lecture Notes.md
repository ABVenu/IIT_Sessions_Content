# Working with APIs and JSON

## Context of This Session

In the **previous** session you went inside the **LLM** — how **tokens** drive **billing** and **latency**, how the **context window** forces trade-offs between **system prompts**, **few-shot examples**, and **chat history**, and how **temperature** and **truncation** shape what users actually see in long chats.

That knowledge helps you **design better prompts**. The next gap for **agentic systems** is **real-world data**: order status, weather, and exchange rates change every minute. They arrive through **APIs**, almost always packaged as **JSON**.

**In this session, you will:**

- Explain how **client applications** talk to **REST APIs** using **HTTP methods** and **status codes**
- **Read and write JSON** structures that represent **requests** and **responses** in Python
- Execute a **GET request** with the **`requests`** library and handle common **response errors** safely
- **Map JSON fields** from an API response into **variables** used in a **downstream LLM prompt**

---

## Why Agents Need APIs — Not Just Better Prompts

A well-written **system prompt** cannot tell you today's **courier location** or this hour's **USD–INR rate**. An **agent** connects to other systems through **APIs**.

- **Official Definition:** An **API (Application Programming Interface)** is a **contract** between two software components — it defines what **request** may be sent and what **response** will be returned.
- **In Simple Words:** A **fixed menu** for asking another system for work and getting a structured answer back.
- **Real-Life Example:** The **IRCTC app** asks the railway server through an API for live seat counts — it does not store every train on your phone.

| User question | Prompting alone? | Needs API? |
|---|---|---|
| *"Summarise our hostel checkout policy politely"* | Yes — if policy text is in the prompt | Optional |
| *"Where is parcel TRK-88421 right now?"* | No — status changes live | **Yes** |
| *"What is the temperature in Delhi for outdoor event planning?"* | No — weather is external | **Yes** |

- **Common mistake:** Letting the **LLM guess** live numbers when an API could supply them — **confident hallucinations** with real-looking digits.
- **Token discipline:** Dumping a **10 KB JSON blob** into a prompt wastes **context**. **Extract only what you need** before prompting.

### Practice — Prompt or API?

For each scenario, write **Prompt only**, **API**, or **Both** and one reason:

1. *"What is the library fine per late day?"* (rule is in the handbook PDF)
2. *"Has my reimbursement request REIM-221 been approved yet?"*
3. *"Will heavy rain in Mumbai affect today's outdoor tech fest setup?"*

**Expected direction:** (1) Prompt/RAG; (2) API; (3) API for weather + prompt for polite wording.

---

## The Request–Response Pattern

Before REST naming rules, lock in the rhythm every API call shares — including the **LLM APIs** you already use.

| Request part | Plain meaning | Example |
|---|---|---|
| **URL / endpoint** | Service address | `https://api.open-meteo.com/v1/forecast` |
| **HTTP method** | Action — read vs create | **GET** to read; **POST** to create |
| **Headers** | Auth, content type | `Authorization: Bearer <API_KEY>` |
| **Params / body** | Data you send | `?latitude=28.61&longitude=77.20` |

| Response part | What to do |
|---|---|
| **Status code** | **Check before trusting the body** |
| **Body** | Parse JSON only after success |

![Four parts of an API request — URL, method, headers, and params or body](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module3/session26/session26-01-api-request-four-parts.png)

**Common doubt:** *"Libraries hide HTTP — do I still need this?"* **Yes.** When a key is wrong or a URL is typoed, **status before body** is how you debug fast.

---

## REST Conventions and HTTP Methods

Most web APIs follow **REST** — URLs name **resources** (nouns) and **methods** express the **action**. Think of an API like a **restaurant waiter** — you order from the **menu** (the contract); the waiter brings **food** or says *"that item is unavailable today"*.

- **REST**
  - **Official Definition:** **Representational State Transfer** — APIs structured around **nouns** (`/orders`), not action verbs in the URL.
  - **In Simple Words:** Name the **thing**, then say **what to do** with **GET**, **POST**, **PATCH**, **PUT**, or **DELETE**.
  - **Real-Life Example:** A library shelf labelled **"Orders"** — you **read**, **add**, **edit**, or **remove** using different procedures.

| CRUD | Method | Use | Body? |
|---|---|---|---|
| **Create** | **POST** | Add a record | Yes |
| **Read** | **GET** | Fetch without changing server | No |
| **Update** | **PATCH** / **PUT** | Partial / full replace | Yes |
| **Delete** | **DELETE** | Remove a record | Rarely |

| What you want | REST style |
|---|---|
| List orders | **GET** `/orders` |
| One order | **GET** `/orders/88421` |
| Place order | **POST** `/orders` |

Today's lab uses **GET** only — **read** live weather without changing server state.

![REST — resource URLs paired with HTTP methods for read, create, update, and delete](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module3/session26/session26-02-rest-http-methods.png)

---

## HTTP Status Codes — Check Before You Trust the Body

- **Status code**
  - **Official Definition:** A three-digit **HTTP** signal summarising success or failure.
  - **In Simple Words:** The server's **first answer** — *"OK"*, *"not found"*, or *"slow down"*.
  - **Real-Life Example:** A courier saying *"delivered"* vs *"wrong pin code"* — you react before opening the box.

| Range | Meaning | Who fixes? |
|---|---|---|
| **2xx** | Success | Proceed |
| **4xx** | Client error | Your URL, params, or API key |
| **5xx** | Server error | External service — retry later |

| Code | Meaning | Agent connection |
|---|---|---|
| **200** | OK | Weather **GET** succeeded |
| **400** | Bad request | Malformed latitude |
| **401** | Unauthorized | Invalid API key |
| **404** | Not found | Typo in API path |
| **429** | Rate limit | Too many LLM or API calls — **slow down** |
| **500** | Server error | Remote service down |

- **Professional habit:** Check **`response.status_code == 200`** (or **`response.ok`**) **before** **`response.json()`**. Never feed **error HTML** into an LLM as weather data.
- **429 note:** Same class of problem as **rate limits** on LLM providers from the **previous** session — not a Python syntax bug.

![HTTP status families — 2xx success, 4xx client mistakes, 5xx server problems](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module3/session26/session26-03-http-status-codes.png)

### Practice — Status Code Match

1. URL typo `/forcast` → **404** or **400**
2. 50 LLM calls in one minute on free tier → **429**
3. Weather JSON returned successfully → **200**

---

## JSON — The Data Format APIs Speak

**JSON** is **structured text** — **key–value pairs**, **lists**, and **nested objects**.

- **Official Definition:** A lightweight, text-based format for transmitting structured data between systems.
- **In Simple Words:** A **filled form** — every field has a **label** and **value**.
- **Real-Life Example:** A courier label: **`"city": "Mumbai"`**, **`"pin": "400001"`**.

| JSON | Python |
|---|---|
| `{ "name": "Ravi" }` | `dict` |
| `[1, 2, 3]` | `list` |
| `true` / `false` | `True` / `False` |
| `null` | `None` |

**Common doubt:** Sometimes **`response.json()`** already parsed the body. If you have a raw **string**, use **`json.loads()`** first.

![JSON round-trip — json.loads and json.dumps between strings and Python dicts](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module3/session26/session26-04-json-python-roundtrip.png)

### Sample Weather Response

```json
{
  "latitude": 28.6139,
  "current": {
    "temperature_2m": 34.2,
    "weather_code": 3
  }
}
```

In Python after parsing: **`data["current"]["temperature_2m"]`** → **34.2**.

### Practice — Find the Fields

From the sample JSON above, write the key path to:

1. Latitude
2. Current temperature in Celsius
3. Weather code

**Your notes:** Nested objects use **chains of keys** — each step goes one level deeper.

---

## Reading and Writing JSON in Python

Python's **`json`** module needs **no pip install**.

- **`json.loads()`** — parse JSON **string** → Python **dict**
- **`json.dumps()`** — Python **dict** → JSON **string** for logs or POST bodies

```python
# json_basics.py — parse and stringify JSON in Python

import json  # Built-in module — no pip install

json_response_string = '''
{
    "tracking_id": "TRK-88421",
    "status": "out_for_delivery",
    "customer_city": "Delhi",
    "eta_hours": 4
}
'''  # Raw JSON arrives as one text string from an API

parcel = json.loads(json_response_string)  # String → Python dict

print("Tracking ID:", parcel["tracking_id"])  # Bracket access by key name
print("Status:", parcel["status"])
print("City:", parcel["customer_city"])

status_update = {  # Build data in Python first
    "tracking_id": "TRK-88421",
    "event": "courier_picked_up",
    "city": "Delhi"
}

json_to_send = json.dumps(status_update, indent=2)  # Dict → pretty JSON string

print("\nJSON ready for POST body:")
print(json_to_send)
print("Type after dumps:", type(json_to_send))  # Always str on the wire
```

**How the code works:**

- **`json.loads()`** turns wire-format text into a **`dict`** you index with `["key"]`.
- **`json.dumps(..., indent=2)`** formats JSON for logs or request bodies.
- **`response.json()`** in **`requests`** does the same parse as **`json.loads(response.text)`**.

### Practice — Build Request JSON

Write a Python **dict** for a POST body: `event_name` = `"Tech Fest Day 1"`, `city` = `"Delhi"`, `check_type` = `"weather"`. Then write the call that turns it into pretty-printed JSON.

**Expected direction:** `json.dumps(your_dict, indent=2)`.

---

## GET Requests with the `requests` Library

Install once: **`pip install requests`**

- **`requests`**
  - **Official Definition:** A Python library sending **HTTP requests** and returning objects with **status codes**, **headers**, and **body text**.
  - **In Simple Words:** Your program's **postal service** for requests and replies.
  - **Real-Life Example:** **WhatsApp** carrying your message — you type once; the network handles delivery.

### Safe GET Rules

| Step | Rule |
|---|---|
| 1 | Use **`requests.get(url, params=..., timeout=15)`** — GET is read-only |
| 2 | Print or log **`response.status_code`** |
| 3 | If **not 200**, preview **`response.text[:500]`** and **stop** — do not parse |
| 4 | On success, call **`response.json()`** for a Python dict |

| Failure | Status | Safe behaviour |
|---|---|---|
| Wrong URL | **404** | Fix typo; do not prompt the LLM |
| Bad API key | **401** | Check `.env` — never print the full key |
| Rate limit | **429** | Sleep and retry with backoff |
| Server down | **500** | Retry later; show user a fallback |
| Network hang | *(timeout)* | `timeout=` raises exception — catch and retry |

- **429 retry pattern:** Loop up to 3 times; on **429**, wait **`2 ** attempt`** seconds (2, 4, 8) before retrying. Caller still verifies **200** after retries.

The full lab below implements every rule in one script.

---

## Mapping JSON Fields into LLM Prompt Variables

Fetching data is half the job. **Agents** turn **API facts** into **prompt instructions** — without dumping the entire JSON tree.

- **Official Definition:** **Field mapping** selects specific keys and assigns them to **named variables** for a **prompt template**.
- **In Simple Words:** Copy only the **three lines that matter** from a long form before writing the summary.
- **Real-Life Example:** A **news anchor** says *"34°C and cloudy in Delhi"* — not the full satellite report.

| Raw API path | Variable | Prompt use |
|---|---|---|
| `current.temperature_2m` | `temperature_c` | *"Temperature is {temperature_c}°C"* |
| `current.weather_code` | `weather_description` | Map code to plain words |
| `latitude` / `longitude` | `latitude`, `longitude` | Traceability in logs |

**Why map instead of paste raw JSON?** Saves **tokens**, clearer **grounding**, easier **testing** before paying for an LLM call.

| `weather_code` | Plain description |
|---|---|
| 0 | Clear sky |
| 1–3 | Mainly clear to overcast |
| 45, 48 | Fog |
| 51–67 | Drizzle or rain |

- **Common mistake:** Putting the **numeric code alone** in the prompt — map to **words** first.

![Map API JSON fields into a downstream LLM prompt — extract only what you need before generation](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module3/session26/session26-05-field-mapping-to-llm-prompt.png)

---

## Full Lab — Fetch, Map, and Build the LLM Prompt

Create **`campus_weather_agent_lab/campus_weather_agent_lab.py`**. Chains: **GET → status check → parse → map → prompt**.

```python
# campus_weather_agent_lab.py — GET weather, map JSON, build downstream LLM prompt

import json  # Pretty-print variables and final prompt
import sys  # Exit on non-200 status

import requests  # pip install requests

OPEN_METEO_URL = "https://api.open-meteo.com/v1/forecast"  # Free weather API — no key
CITY_NAME = "Delhi"  # Event city label
CITY_LAT = 28.6139  # Latitude — must match CITY_NAME
CITY_LON = 77.2090  # Longitude — must match CITY_NAME
TIMEOUT = 15  # Seconds before network call fails

WEATHER_CODE_WORDS = {  # Numeric codes → prompt-safe words
    0: "clear sky", 1: "mainly clear", 2: "partly cloudy", 3: "overcast",
    45: "foggy", 51: "light drizzle", 61: "rain", 80: "rain showers",
}


def fetch_current_weather(latitude: float, longitude: float) -> dict:
    """GET live weather JSON — read-only."""
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,weather_code",  # Only fields we need
    }
    response = requests.get(OPEN_METEO_URL, params=params, timeout=TIMEOUT)

    print(f"Status code: {response.status_code}")

    if response.status_code != 200:  # Never parse error bodies as weather
        print("API failed. Body preview:", response.text[:500])
        sys.exit(1)

    return response.json()  # Dict ready for key navigation


def map_weather_to_variables(city_name: str, weather_data: dict) -> dict:
    """Extract and rename JSON fields for agent use."""
    current = weather_data["current"]
    code = current["weather_code"]
    description = WEATHER_CODE_WORDS.get(code, f"weather code {code}")
    return {
        "city": city_name,
        "temperature_c": current["temperature_2m"],
        "weather_code": code,
        "weather_description": description,
        "latitude": weather_data["latitude"],
        "longitude": weather_data["longitude"],
    }


def build_event_prompt(variables: dict, event_name: str) -> str:
    """Map variables into a downstream LLM user prompt."""
    return f"""
You are a campus events assistant. Use ONLY the live weather facts below.
Do not invent temperature or conditions. Reply in under 80 words.

Event: {event_name}
City: {variables["city"]}
Live temperature: {variables["temperature_c"]} degrees Celsius
Conditions: {variables["weather_description"]}

Task: Advise whether outdoor setup should continue or move partially indoors.
""".strip()


def main():
    event_name = "Tech Fest — Outdoor Demo Stage"

    print(f"Step 1 — GET weather for {CITY_NAME}...")
    weather_data = fetch_current_weather(CITY_LAT, CITY_LON)

    print("\nStep 2 — Map JSON to variables...")
    variables = map_weather_to_variables(CITY_NAME, weather_data)
    print(json.dumps(variables, indent=2))

    print("\nStep 3 — Build LLM prompt...")
    llm_prompt = build_event_prompt(variables, event_name)
    print(llm_prompt)

    print("\nStep 4 — Type check:", type(variables["temperature_c"]))
    print("Done — prompt contains live API facts, not guesses.")


if __name__ == "__main__":
    main()
```

Run: **`cd campus_weather_agent_lab`** then **`python campus_weather_agent_lab.py`**

**How the code works:**

- **`fetch_current_weather`** — **GET** with **`params`**, status check, then **`response.json()`**.
- **`map_weather_to_variables`** — renames **`temperature_2m`** → **`temperature_c`**, code → **`weather_description`**.
- **`build_event_prompt`** — **f-string** with *"do not invent"* rule; paste output into a playground to test.
- **No LLM API call here** — focus is **reliable data → clean prompt input**.

### Verification Checklist

| Check | Expected |
|---|---|
| Status | `Status code: 200` |
| Variables | **`city`**, **`temperature_c`**, **`weather_description`** in JSON output |
| Prompt | Live temperature inside printed prompt |
| Types | `temperature_c` is **float**, not string |
| Failure drill | Break URL once — script **exits** on non-200 |

### Practice — Change City and Break URL

1. Set **`CITY_NAME`** / coords to **Mumbai** (**19.0760**, **72.8777**) — confirm temperature changes.
2. Temporarily typo **`forecast`** → **`forcast`** — confirm script stops instead of faking weather.
3. **Label and coordinates must match** — saying Mumbai with Delhi coords is a silent data bug.

### Practice — Prompt Quality Check

Read the printed **`llm_prompt`** and confirm:

1. It states **scope** (campus events assistant).
2. It forbids **inventing** weather facts.
3. Every number is traceable to the **`variables`** dict.

**Agent loop preview:** Detect need → **API call** → **map fields** → **build prompt** → LLM reply (future work). Step 5 inherits **internals** lessons — keep prompts **short**, reserve **token budget** for the reply, use **low temperature** for factual wording. If the model says **40°C** but **`variables["temperature_c"]`** was **28°C**, that is a **generation** failure — log variables alongside output.

---

## Key Takeaways

- **APIs** supply **live external facts** — prompts alone cannot replace order status, weather, or rates that change every minute.
- Every call follows **request → status → body**; check **2xx** before parsing **JSON** or building prompts.
- **REST** pairs **resource URLs** with **HTTP methods**; today's lab uses **GET** to read weather.
- **`json.loads()`**, **`json.dumps()`**, and **`response.json()`** move data between text and dicts — **map only needed fields** to save tokens.
- **`requests.get()`** with **timeouts** and **status checks** is the safe baseline; mapped variables feed **downstream prompts** in the full agent loop ahead.

---

## Quick Reference — Commands, Libraries, and Terminologies

| Term / Command | Meaning |
|---|---|
| **API** | Contract for requests and responses between systems |
| **REST** | Nouns in URLs; actions in HTTP methods |
| **GET** | Read data without changing server state |
| **POST** | Create or submit data |
| **Status code** | **200** OK, **401** auth, **404** not found, **429** rate limit |
| **`response.ok`** | `True` when status is 2xx |
| **JSON** | Structured text — keys, values, lists, nested objects |
| **`json.loads()`** | JSON string → Python dict |
| **`json.dumps()`** | Python dict → JSON string |
| **`requests.get()`** | HTTP GET; `.status_code`, `.text`, `.json()` |
| **`params=`** | Query string on URL (`?latitude=...`) |
| **`timeout=`** | Max wait seconds before network failure |
| **Field mapping** | Extract and rename JSON keys for prompts |
| **`pip install requests`** | Install HTTP client library |
