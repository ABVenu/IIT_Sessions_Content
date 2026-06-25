# Assignment Subjective

Total Questions: 1  
Difficulty: Medium  
Type: Applied Python implementation (Open-Meteo GET + JSON mapping + Groq grounded reply)

---

## Q1 (Applied, Medium)

**FestRoute** organises outdoor demo stages across IIT campuses. The events team wants a small Python script that:

1. Fetches **live weather** for **Pune** from Open-Meteo (no API key).  
2. Maps only the needed JSON fields into variables.  
3. Builds a **grounded user prompt** that forbids inventing weather facts.  
4. Sends that prompt to **Groq** and prints short setup advice.

You are the builder. Implement the **two-call agent pattern**: data API first, LLM second.

---

### Fixed constants (use exactly)

| Constant | Value |
|---|---|
| City label | `"Pune"` |
| Latitude | `18.5204` |
| Longitude | `73.8567` |
| Open-Meteo URL | `https://api.open-meteo.com/v1/forecast` |
| Event name | `"FestRoute — Robotics Demo Lawn"` |
| Groq model | `llama-3.3-70b-versatile` |
| Request timeout (seconds) | `15` |

**Weather code → words** (use this dict; unknown codes → `"weather code {code}"`):

| Code | Description |
|---|---|
| 0 | clear sky |
| 1 | mainly clear |
| 2 | partly cloudy |
| 3 | overcast |
| 61 | rain |

---

### What your script must do

Create a single file named **`festroute_weather_agent.py`** that:

1. Reads **`GROQ_API_KEY`** from the environment (no hard-coded keys).  
2. Defines **`fetch_current_weather(latitude, longitude)`** — `requests.get` with `params` requesting `current=temperature_2m,weather_code`, plus `timeout=15`. Print `Status code: <code>`. If status is **not 200**, print `API failed. Body preview:` plus the first **500** characters of `response.text`, then **exit** (do not parse JSON).  
3. Defines **`map_weather_to_variables(city_name, weather_data)`** — return a dict with keys: `city`, `temperature_c` (from `current.temperature_2m`), `weather_code`, `weather_description` (mapped via the table above), `latitude`, `longitude`.  
4. Defines **`build_event_prompt(variables, event_name)`** — multi-line user prompt that includes:
   - Role: campus events assistant  
   - Rule: **use ONLY the live weather facts below; do not invent temperature or conditions**  
   - Event name, city, live temperature (°C), conditions (words)  
   - Task: advise whether outdoor setup should continue or move partially indoors; reply in under **80 words**  
5. Defines **`call_groq_for_advice(llm_prompt)`** — `Groq` client, `chat.completions.create` with **user** message only (`temperature=0.2`, `max_tokens=150`). Return assistant text.  
6. In **`main()`**, print labelled steps:
   - `Step 1 — GET weather for Pune...`
   - `Step 2 — Map JSON to variables...` (pretty-print variables with `json.dumps(..., indent=2)`)
   - `Step 3 — Build LLM prompt...` (print full prompt)
   - `Step 4 — Type check:` and the type of `temperature_c` (must be **float**)
   - `Step 5 — Groq API call...` then print `LLM advice:` followed by the reply  

**Illustrative output shape (values will differ with live weather):**

```text
Step 1 — GET weather for Pune...
Status code: 200

Step 2 — Map JSON to variables...
{
  "city": "Pune",
  "temperature_c": 31.4,
  "weather_code": 3,
  "weather_description": "overcast",
  "latitude": 18.52,
  "longitude": 73.86
}

Step 3 — Build LLM prompt...
You are a campus events assistant. Use ONLY the live weather facts below.
...

Step 4 — Type check: <class 'float'>

Step 5 — Groq API call...
LLM advice:
Continue outdoor setup with shade and hydration; overcast skies suggest low rain risk but monitor temperature.
```

---

### Submission instructions

- Code all requirements in a **single file** `festroute_weather_agent.py` in VS Code or Colab.  
- Install **`requests`** and **`groq`** if needed; set **`GROQ_API_KEY`** in your environment or Colab Secrets.  
- Run the script and confirm status **200**, mapped variables, printed prompt, and LLM advice.  
- Submit the **complete `.py` file** in the LMS code editor / answer box.

---

### Answer Explanation (for assessors)

**Ideal solution walkthrough**

```python
# festroute_weather_agent.py — Open-Meteo GET, map JSON, grounded Groq advice

import json  # Pretty-print variables
import os  # Environment API key
import sys  # Exit on failed HTTP status

import requests  # pip install requests
from groq import Groq  # pip install groq

OPEN_METEO_URL = "https://api.open-meteo.com/v1/forecast"  # Free weather API
CITY_NAME = "Pune"  # Fixed city label
CITY_LAT = 18.5204  # Pune latitude
CITY_LON = 73.8567  # Pune longitude
TIMEOUT = 15  # Network timeout seconds
GROQ_MODEL = "llama-3.3-70b-versatile"  # Specified Groq model
EVENT_NAME = "FestRoute — Robotics Demo Lawn"  # Fixed event title

WEATHER_CODE_WORDS = {  # Code → plain language for prompts
    0: "clear sky",
    1: "mainly clear",
    2: "partly cloudy",
    3: "overcast",
    61: "rain",
}


def fetch_current_weather(latitude: float, longitude: float) -> dict:
    """GET live weather; stop before parse if HTTP status is not 200."""
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,weather_code",  # Only fields needed downstream
    }
    response = requests.get(OPEN_METEO_URL, params=params, timeout=TIMEOUT)  # Read-only GET
    print(f"Status code: {response.status_code}")  # Required status log
    if response.status_code != 200:  # Status-first rule
        print("API failed. Body preview:", response.text[:500])  # Debug snippet
        sys.exit(1)  # Do not parse error bodies as weather
    return response.json()  # Parsed dict for key navigation


def map_weather_to_variables(city_name: str, weather_data: dict) -> dict:
    """Extract and rename JSON fields for the LLM prompt."""
    current = weather_data["current"]  # Nested object in Open-Meteo response
    code = current["weather_code"]  # Numeric weather code
    description = WEATHER_CODE_WORDS.get(code, f"weather code {code}")  # Map to words
    return {
        "city": city_name,
        "temperature_c": current["temperature_2m"],  # Rename for prompt clarity
        "weather_code": code,
        "weather_description": description,
        "latitude": weather_data["latitude"],
        "longitude": weather_data["longitude"],
    }


def build_event_prompt(variables: dict, event_name: str) -> str:
    """Grounded user prompt — facts only from variables dict."""
    return f"""
You are a campus events assistant. Use ONLY the live weather facts below.
Do not invent temperature or conditions. Reply in under 80 words.

Event: {event_name}
City: {variables["city"]}
Live temperature: {variables["temperature_c"]} degrees Celsius
Conditions: {variables["weather_description"]}

Task: Advise whether outdoor setup should continue or move partially indoors.
""".strip()


def call_groq_for_advice(llm_prompt: str) -> str:
    """Second API call — natural-language advice from Groq."""
    client = Groq(api_key=os.environ["GROQ_API_KEY"])  # Key from environment
    completion = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[{"role": "user", "content": llm_prompt}],  # User-only prompt
        temperature=0.2,  # Low temperature for factual advice
        max_tokens=150,  # Cap output length
    )
    return completion.choices[0].message.content  # Assistant reply text


def main():
    print(f"Step 1 — GET weather for {CITY_NAME}...")
    weather_data = fetch_current_weather(CITY_LAT, CITY_LON)  # Data API call

    print("\nStep 2 — Map JSON to variables...")
    variables = map_weather_to_variables(CITY_NAME, weather_data)
    print(json.dumps(variables, indent=2))  # Pretty-print mapped dict

    print("\nStep 3 — Build LLM prompt...")
    llm_prompt = build_event_prompt(variables, EVENT_NAME)
    print(llm_prompt)  # Show grounded prompt before LLM call

    print("\nStep 4 — Type check:", type(variables["temperature_c"]))  # Should be float

    print("\nStep 5 — Groq API call...")
    advice = call_groq_for_advice(llm_prompt)  # LLM API call
    print("LLM advice:")
    print(advice)


if __name__ == "__main__":
    main()
```

**Grading notes**

| Criterion | What to check |
|---|---|
| HTTP GET | Open-Meteo URL, `params` with lat/lon and `current=`, `timeout=15` |
| Status-first | Prints status; on non-200 prints body preview and exits without `response.json()` |
| Mapping | `temperature_c`, `weather_description` from code table, required keys present |
| Prompt | "Use ONLY live weather facts", no invention rule, event + city + temp + conditions |
| Groq | Env key, model `llama-3.3-70b-versatile`, user message, `temperature=0.2`, `max_tokens=150` |
| Output steps | All five step labels printed in order |
| Types | `temperature_c` is float, not string |

**Alternative valid approaches**

- Helper functions inlined in `main()` if logic matches.  
- Slightly different LLM wording if grounded in the same variables.  
- `os.environ.get` with explicit error message if key missing.

**Common mistakes**

- Hard-coded API key.  
- Parsing JSON without checking status **200**.  
- Pasting full Open-Meteo JSON into Groq instead of mapped variables.  
- Putting numeric `weather_code` alone in the prompt without mapping to words.  
- Wrong Pune coordinates or city label mismatch.

**Excluded from grading requirements:** `response.ok`, exponential backoff on **429**, `try`/`except` timeout wrappers, PATCH/PUT/DELETE usage.
