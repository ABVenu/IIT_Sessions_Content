# Subjective Assignment: ShopKart — Fetch, Parse, Print

## Practical Task

**Difficulty:** Light (guided mini-lab)  
**Type:** Coding implementation

---

## Scenario

ShopKart's ops desk wants a **quick courier-weather snapshot** before dispatching express handoffs. You already have most of the weather fetch script from the lab. Finish two small pieces, run it once, and prove you can also parse a **static order JSON string** the way API responses arrive as text.

No Groq calls, no agent routing, no GitHub repo — one short `.py` file only.

---

## Setup

Create a folder and file:

```text
shopkart_api_json_lab/
└── shopkart_api_json_lab.py
```

Install if needed:

```bash
pip install requests
```

---

## Starter code

Copy this into **`shopkart_api_json_lab.py`**. The GET helper is **already complete** — do not rewrite it.

```python
import json
import sys

import requests

OPEN_METEO_URL = "https://api.open-meteo.com/v1/forecast"
DELHI_LAT = 28.6139
DELHI_LON = 77.2090
CITY_NAME = "Delhi"
REQUEST_TIMEOUT_SECONDS = 15


def fetch_current_weather(latitude: float, longitude: float) -> dict:
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,weather_code",
    }
    response = requests.get(OPEN_METEO_URL, params=params, timeout=REQUEST_TIMEOUT_SECONDS)
    print(f"Weather API status code: {response.status_code}")

    if response.status_code != 200:
        print("Weather API call failed. Body preview:")
        print(response.text[:500])
        sys.exit(1)

    return response.json()


# ── TODO 1: YOU WRITE THIS FUNCTION ──────────────────────────────────────────
def extract_weather_fields(city_name: str, weather_data: dict) -> dict:
    """Return a small dict with city, temperature_c, weather_code, latitude, longitude."""
    pass


# ── TODO 2: YOU WRITE THIS BLOCK ─────────────────────────────────────────────
ORDER_JSON_STRING = """
{
    "order_id": "ORD-88421",
    "status": "out_for_delivery",
    "customer_city": "Delhi"
}
"""


def main():
    print(f"Step 1 — GET live weather for {CITY_NAME}...")
    weather_data = fetch_current_weather(DELHI_LAT, DELHI_LON)

    print("\nStep 2 — Extract selected JSON fields...")
    fields = extract_weather_fields(CITY_NAME, weather_data)
    print(json.dumps(fields, indent=2))

    print("\nStep 3 — Parse order JSON string with json.loads()...")
    # Parse ORDER_JSON_STRING, then print order_id and status on separate lines


if __name__ == "__main__":
    main()
```

---

## Your tasks (only these three)

### 1. Complete `extract_weather_fields`

Return a dictionary with exactly these keys:

- `city` — use the `city_name` argument  
- `temperature_c` — from `weather_data["current"]["temperature_2m"]`  
- `weather_code` — from `weather_data["current"]["weather_code"]`  
- `latitude` — from `weather_data["latitude"]`  
- `longitude` — from `weather_data["longitude"]`

### 2. Parse the order string in `main()`

After Step 3's print line:

- Use **`json.loads(ORDER_JSON_STRING)`** to get a Python dict  
- Print **`order_id`** and **`status`** on two separate lines (labels optional)

### 3. Run and verify

```bash
cd shopkart_api_json_lab
python shopkart_api_json_lab.py
```

Confirm in the terminal:

- Status code **200**  
- Pretty-printed weather dict with all five keys  
- Order ID **ORD-88421** and status **out_for_delivery** printed after Step 3

---

## Submission Instruction

- Code all the points mentioned in VS Code in a single `.py` file (`shopkart_api_json_lab.py`).
- Run the code and verify it is working.
- Submit the complete code in the LMS code editor/answer box.

---

## Answer Explanation (Reference Approach)

### Step-by-step solution walkthrough

1. Keep the provided `fetch_current_weather` unchanged — it already demonstrates GET, status check, and `response.json()`.
2. Implement `extract_weather_fields` by reading nested keys from the parsed dict (same shape as the lab).
3. In `main()`, call `json.loads` on the multiline order string and print two fields — this mirrors JSON arriving as text before parsing.
4. Run once with Delhi coordinates; no second city or error-drill required for this assignment.

### Reference solution — parts you write

```python
def extract_weather_fields(city_name: str, weather_data: dict) -> dict:
    current = weather_data["current"]
    return {
        "city": city_name,
        "temperature_c": current["temperature_2m"],
        "weather_code": current["weather_code"],
        "latitude": weather_data["latitude"],
        "longitude": weather_data["longitude"],
    }


def main():
    print(f"Step 1 — GET live weather for {CITY_NAME}...")
    weather_data = fetch_current_weather(DELHI_LAT, DELHI_LON)

    print("\nStep 2 — Extract selected JSON fields...")
    fields = extract_weather_fields(CITY_NAME, weather_data)
    print(json.dumps(fields, indent=2))

    print("\nStep 3 — Parse order JSON string with json.loads()...")
    order = json.loads(ORDER_JSON_STRING)
    print("Order ID:", order["order_id"])
    print("Status:", order["status"])
```

### Sample terminal output (values will vary)

```text
Step 1 — GET live weather for Delhi...
Weather API status code: 200

Step 2 — Extract selected JSON fields...
{
  "city": "Delhi",
  "temperature_c": 34.2,
  "weather_code": 3,
  "latitude": 28.6139,
  "longitude": 77.209
}

Step 3 — Parse order JSON string with json.loads()...
Order ID: ORD-88421
Status: out_for_delivery
```

### Alternative approaches

- Pretty-printing the order dict with `json.dumps` after loads is acceptable if `order_id` and `status` are clearly shown.
- A tiny `print_order_summary(order_dict)` helper is fine — behaviour matters, not extra abstraction.

### Notes for evaluation

- Full credit: working `extract_weather_fields` with all five keys, `json.loads` on the order string, status 200 path exercised, single-file submission.
- Partial credit: fetch works but extraction keys missing, or order parsed without printing both fields.
- No dataset download required — weather API is public; order JSON is inline in the starter file.
