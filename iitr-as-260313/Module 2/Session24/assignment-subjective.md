# Subjective Assignment: ShopKart — Wire the Tool Agent Loop

## Practical Task

**Difficulty:** Medium  
**Type:** Coding implementation

---

## Scenario

ShopKart's support desk already has **policy** and **weather tool functions** tested and registered in Groq's **`tools`** list. The missing piece is the **agent runtime** — the loop that sends customer questions to Groq, executes whatever **`tool_calls`** come back, feeds JSON results to the model, and returns one **grounded** reply.

Your job: implement **`run_tool_agent`** and prove routing works on **two customer questions** — one policy-only, one that needs **both** policy and live weather.

---

## Setup

Create a folder and file:

```text
shopkart_tool_agent/
├── shopkart_tool_agent.py
└── .env                  # GROQ_API_KEY=your-key-here
```

Install:

```bash
pip install groq requests python-dotenv
```

---

## Starter code

Copy into **`shopkart_tool_agent.py`**. **Do not rewrite** the tool functions or **`TOOLS`** registry — they are complete.

```python
import json
import sys

import requests
from dotenv import load_dotenv
from groq import Groq

GENERATION_MODEL = "llama-3.3-70b-versatile"
OPEN_METEO_URL = "https://api.open-meteo.com/v1/forecast"
REQUEST_TIMEOUT_SECONDS = 15

POLICY_SNIPPETS = {
    "returns": (
        "Unopened items may be returned within 7 calendar days of delivery. "
        "Opened or used items are not eligible unless defective."
    ),
    "shipping": (
        "Standard delivery takes 3-5 business days after dispatch. "
        "Express delivery (paid) arrives in 1-2 business days in metro cities only."
    ),
    "warranty": (
        "Electronics carry a 12-month manufacturer warranty from delivery date. "
        "Warranty does not cover physical damage or liquid exposure."
    ),
    "refunds": (
        "Refunds are credited within 5-7 business days after warehouse verification. "
        "Cash-on-delivery orders are refunded to UPI or bank account only."
    ),
}

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "search_shopkart_policy",
            "description": (
                "Search ShopKart customer policy for returns, shipping, warranty, or refunds. "
                "Use when the question is about rules, timelines, or eligibility in policy documents."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Customer policy question in plain English",
                    },
                },
                "required": ["query"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_city_weather",
            "description": (
                "Fetch current weather for a delivery city using latitude and longitude. "
                "Use when live weather may affect courier handoff or delivery timing."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "city_name": {"type": "string", "description": "City label for logs and replies"},
                    "latitude": {"type": "number", "description": "City latitude"},
                    "longitude": {"type": "number", "description": "City longitude"},
                },
                "required": ["city_name", "latitude", "longitude"],
            },
        },
    },
]


def search_shopkart_policy(query: str) -> dict:
    query_lower = query.lower()
    matched = []
    keyword_map = {
        "returns": ["return", "unopened", "opened", "eligible", "send back"],
        "shipping": ["shipping", "express", "delivery", "metro", "dispatch"],
        "warranty": ["warranty", "repair", "defect", "liquid", "water"],
        "refunds": ["refund", "cod", "upi", "money back", "credit"],
    }
    for category, keywords in keyword_map.items():
        if any(word in query_lower for word in keywords):
            matched.append({"category": category, "text": POLICY_SNIPPETS[category]})
    if not matched:
        return {"error": "No policy excerpt found", "query": query, "excerpts": []}
    return {"query": query, "excerpts": matched}


def get_city_weather(city_name: str, latitude: float, longitude: float) -> dict:
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,weather_code",
    }
    response = requests.get(OPEN_METEO_URL, params=params, timeout=REQUEST_TIMEOUT_SECONDS)
    if response.status_code != 200:
        return {
            "error": "Weather API failed",
            "status_code": response.status_code,
            "city": city_name,
        }
    data = response.json()
    current = data["current"]
    return {
        "city": city_name,
        "temperature_c": current["temperature_2m"],
        "weather_code": current["weather_code"],
        "latitude": latitude,
        "longitude": longitude,
    }


TOOL_FUNCTIONS = {
    "search_shopkart_policy": search_shopkart_policy,
    "get_city_weather": get_city_weather,
}


# ── TODO: YOU IMPLEMENT THIS FUNCTION ────────────────────────────────────────
def run_tool_agent(client: Groq, user_message: str) -> str:
    """Run model → tool loop until the model returns a final text answer."""
    pass


def main():
    load_dotenv()
    client = Groq()

    demo_queries = [
        "Can I return unopened earphones within seven days?",
        "I chose express delivery to Delhi metro tomorrow. What does policy say about express timing, and is current weather likely to affect courier handoff today?",
    ]

    for user_message in demo_queries:
        print("\n" + "=" * 72)
        print("Customer:", user_message)
        print("=" * 72)
        answer = run_tool_agent(client, user_message)
        print("\nFinal answer:")
        print(answer)


if __name__ == "__main__":
    main()
```

---

## Your tasks

### 1. Implement `run_tool_agent`

Build the full **tool execution loop**:

- Start **`messages`** with a **system prompt** that tells the assistant to use tools when policy or weather are needed, **ground answers in tool JSON only**, and **not invent** policy numbers or weather when tools fail or return **`error`**.
- Call **`client.chat.completions.create`** with **`model=GENERATION_MODEL`**, **`messages`**, **`tools=TOOLS`**, and **`tool_choice="auto"`**.
- While **`assistant_message.tool_calls`** is non-empty:
  - Append the assistant message to **`messages`**.
  - For each **`tool_call`**: parse arguments with **`json.loads`**, look up the function in **`TOOL_FUNCTIONS`** (return **`{"error": f"Unknown tool: {name}"}`** if missing), execute it, and append a **`role: tool`** message with matching **`tool_call_id`** and **`content=json.dumps(result)`**.
  - Call Groq again with the updated **`messages`** and the same **`tools`** / **`tool_choice="auto"`**.
- Return **`assistant_message.content.strip()`** when the model stops requesting tools.

### 2. Run both demo queries

```bash
cd shopkart_tool_agent
python shopkart_tool_agent.py
```

Verify in the terminal:

| Query | Expected routing | Answer should |
|---|---|---|
| Unopened earphones return | **Policy tool only** | Mention **7 days** (from policy excerpts) — no invented weather |
| Express Delhi + weather | **Policy + weather tools** | Cite **metro express 1–2 days** **and** a live **temperature** value |

Temperature will vary by run — that is expected. Policy numbers must match tool JSON, not guesses.

---

## Submission Instruction

- Code all the points mentioned in VS Code in a single `.py` file (`shopkart_tool_agent.py`).
- Run the code and verify it is working.
- Submit the complete code in the LMS code editor/answer box.

---

## Answer Explanation (Reference Approach)

### Step-by-step solution walkthrough

1. Keep **`search_shopkart_policy`**, **`get_city_weather`**, **`TOOLS`**, and **`TOOL_FUNCTIONS`** unchanged — they are the tested tool layer.
2. In **`run_tool_agent`**, build the system + user messages, then enter the **`while assistant_message.tool_calls`** loop — this is the core agent runtime from the lab.
3. Inside the loop, always **`json.loads`** tool arguments before calling Python functions, and always **`json.dumps`** results into **`role: tool`** messages with the correct **`tool_call_id`**.
4. Run both demo queries with a valid **`GROQ_API_KEY`** in **`.env`** — query 1 should route policy-only; query 2 should combine policy shipping rules with Open-Meteo temperature.

### Reference solution — `run_tool_agent`

```python
def run_tool_agent(client: Groq, user_message: str) -> str:
    messages = [
        {
            "role": "system",
            "content": (
                "You are a precise ShopKart support assistant. "
                "Use tools when policy rules or live weather are needed. "
                "Ground answers in tool JSON only — do not invent policy numbers or weather. "
                "If a tool returns error, say you cannot confirm that part."
            ),
        },
        {"role": "user", "content": user_message},
    ]

    response = client.chat.completions.create(
        model=GENERATION_MODEL,
        messages=messages,
        tools=TOOLS,
        tool_choice="auto",
    )
    assistant_message = response.choices[0].message

    while assistant_message.tool_calls:
        messages.append(assistant_message)

        for tool_call in assistant_message.tool_calls:
            function_name = tool_call.function.name
            raw_arguments = tool_call.function.arguments
            arguments = json.loads(raw_arguments)

            if function_name not in TOOL_FUNCTIONS:
                result = {"error": f"Unknown tool: {function_name}"}
            else:
                result = TOOL_FUNCTIONS[function_name](**arguments)

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": json.dumps(result),
                }
            )

        response = client.chat.completions.create(
            model=GENERATION_MODEL,
            messages=messages,
            tools=TOOLS,
            tool_choice="auto",
        )
        assistant_message = response.choices[0].message

    return assistant_message.content.strip()
```

### Sample terminal output (temperature will vary)

```text
Customer: Can I return unopened earphones within seven days?
...
Final answer:
You may return unopened items within 7 calendar days of delivery ...

Customer: I chose express delivery to Delhi metro tomorrow...
...
Final answer:
Express delivery in metro cities arrives in 1-2 business days ... Current temperature in Delhi is around 33°C ...
```

### Alternative approaches

- Logging each **`tool_call`** name and raw JSON to the terminal before execution helps debugging — optional but useful.
- A small helper **`execute_tool_call(tool_call) -> dict`** is acceptable if the same loop behaviour is preserved.

### Notes for evaluation

- Full credit: working **`while tool_calls`** loop, correct **`json.loads`** / **`json.dumps`**, **`role: tool`** messages with **`tool_call_id`**, grounded system prompt, both demo queries run successfully.
- Partial credit: tools work when called manually but loop missing, or loop runs but tool results not appended before the second Groq call.
- Requires **`GROQ_API_KEY`** in **`.env`** and network access for Open-Meteo — no external dataset download.
