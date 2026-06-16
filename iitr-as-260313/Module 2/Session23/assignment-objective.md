# Objective Assignment: Working with APIs and JSON

## Instructions

- Questions 1 to 6 are **MCQs**. Choose **one correct option**.
- Questions 7 to 10 are **MSQs**. Choose **all correct options**.
- The questions are ordered from Easy to Moderate to Hard.

---

## Question 1

**Type:** MCQ  
**Difficulty:** Easy

A ShopKart customer asks: *"Where is my order ORD-88421 right now?"* The support bot must answer with **live courier location** that changes every few minutes. Which data source fits best?

A. RAG search over **returns_policy.txt**  
B. **API** call to the order-tracking system  
C. RAG search over **warranty_policy.txt**  
D. A static FAQ paragraph saved in a Word file on the laptop

**Correct Answer:** B

**Answer Explanation:**  
B is correct because order location is a **live fact** that changes constantly — it must come from an external system via an API, not stored policy documents.

A and C are incorrect because returns and warranty policies do not contain real-time courier positions. D is incorrect because a local static file cannot reflect minute-by-minute tracking updates.

---

## Question 2

**Type:** MCQ  
**Difficulty:** Easy

A customer asks: *"What is the warranty period for electronics?"* Which approach should the assistant use **first**?

A. **GET** request to a weather API  
B. **RAG** retrieval from indexed warranty policy chunks  
C. **POST** request to create a new warranty record  
D. Parse a JSON exchange-rate response

**Correct Answer:** B

**Answer Explanation:**  
B is correct because warranty duration is a **rule stored in policy documents** — the right pattern is document-grounded retrieval (RAG), not a live external feed.

A and D fetch unrelated live data (weather, rates). C is incorrect because the customer is asking to **read** a policy rule, not create a new warranty entry on a server.

---

## Question 3

**Type:** MCQ  
**Difficulty:** Easy

Your weather script prints `Weather API status code: 404` after a URL typo (`/forcast` instead of `/forecast`). What should you do **before** calling `response.json()`?

A. Assume the body is valid weather JSON and parse it  
B. **Stop and handle the error** — do not trust the body as weather data  
C. Immediately send the error HTML to Groq as context  
D. Change the HTTP method from GET to POST

**Correct Answer:** B

**Answer Explanation:**  
B is correct because **non-200 status codes** mean the response is not trustworthy weather data — always check status before parsing.

A is incorrect because 404 responses often return error pages, not weather JSON. C is incorrect because error pages must not be fed to an LLM as facts. D is incorrect because the failure is a wrong URL, not the HTTP method choice.

---

## Question 4

**Type:** MCQ  
**Difficulty:** Easy

A teammate runs forty Groq completions in one minute on a free-tier key and sees failures. Which HTTP status code best matches this situation?

A. **200**  
B. **404**  
C. **429**  
D. **201**

**Correct Answer:** C

**Answer Explanation:**  
C is correct because **429 Too Many Requests** signals **rate limiting** — too many calls in a short window, which matches heavy Groq usage on a free account.

A and D indicate success (OK / Created), not throttling. B means the resource path was not found, not quota exhaustion.

---

## Question 5

**Type:** MCQ  
**Difficulty:** Moderate

In your ShopKart weather lab you call Open-Meteo with `requests.get(url, params={...})` to read current temperature for Delhi. Which REST mapping is correct?

A. **POST** — creating a new weather record on the server  
B. **GET** — reading live data without changing server state  
C. **DELETE** — removing old forecast entries  
D. **PATCH** — partially updating the city's temperature field

**Correct Answer:** B

**Answer Explanation:**  
B is correct because fetching current weather is a **read-only** operation — REST convention uses **GET** with query parameters, no request body.

A, C, and D describe create, remove, or update actions — none apply when you only **fetch** existing forecast data.

---

## Question 6

**Type:** MCQ  
**Difficulty:** Moderate

You receive this raw text from a log file (not yet parsed):

```json
{"order_id": "ORD-4421", "status": "refund_processed"}
```

Which Python call turns it into a dictionary you can index with `data["status"]`?

A. `json.dumps(raw_text)`  
B. `response.json()` on a string variable  
C. **`json.loads(raw_text)`**  
D. `print(raw_text["status"])`

**Correct Answer:** C

**Answer Explanation:**  
C is correct because **`json.loads()`** parses a JSON **string** into a Python **dict** — the right tool when data arrives as text.

A does the opposite (dict → string). B is a `requests` response method, not for an ordinary string variable. D fails because you cannot index a raw string with a key name before parsing.

---

## Question 7

**Type:** MSQ  
**Difficulty:** Moderate

ShopKart's support lead asks you to label each customer line as **RAG**, **API**, or **neither alone is enough** for a production answer. Which labels are **correct**? Select **all** that apply.

A. *"Is express delivery available in metro cities?"* → **RAG** (policy wording)  
B. *"Has my refund for order ORD-4421 been processed yet?"* → **API** (live order/refund status)  
C. *"What is today's temperature in Mumbai for courier pickup?"* → **API** (live weather reading)  
D. *"Summarise the 7-day return window politely"* → **API** only — no documents needed

**Correct Answers:** A, B, C

**Answer Explanation:**  
A, B, and C are correct — metro express rules live in policy text (RAG); refund status is live transactional data (API); temperature is an external live reading (API).

D is incorrect because summarising the return window requires **policy evidence** (RAG) plus natural language generation — not an API weather/order call alone.

---

## Question 8

**Type:** MSQ  
**Difficulty:** Moderate

You map parts of a **Groq chat completion call** onto the generic API request–response pattern. Which pairings are **correct**? Select **all** that apply.

A. **Authorization header with API key** → request metadata / authentication  
B. **`messages` list in the request body** → data you send to the service  
C. **`choices[0].message.content`** → structured data you read back from the response body  
D. **HTTP 404** → Groq successfully returned the model's answer text

**Correct Answers:** A, B, C

**Answer Explanation:**  
A, B, and C correctly map Groq usage onto URL/method/headers/body (auth, payload, parsed reply field).

D is incorrect because **404** means **not found** — a client or path error, not a successful completion payload.

---

## Question 9

**Type:** MSQ  
**Difficulty:** Hard

Your `shopkart_api_json_lab.py` fetches weather JSON. Which practices prevent **confident wrong answers** when you extend this script later? Select **all** that apply.

A. Check **`response.status_code == 200`** (or `response.ok`) before calling **`response.json()`**  
B. Extract only needed fields (e.g. `temperature_c`, `weather_code`) instead of dumping the entire payload into a prompt  
C. Keep **`CITY_NAME`** label aligned with the **latitude/longitude** actually sent in the GET request  
D. Skip status checks when the API is free and public — free APIs always return 200

**Correct Answers:** A, B, C

**Answer Explanation:**  
A is correct — status-first discipline avoids parsing error pages as data. B is correct — selective field extraction reduces token waste and invented fields later. C is correct — mismatched label vs coordinates produces misleading "Mumbai" labels with Delhi weather.

D is incorrect — public APIs still return **4xx/5xx** on bad URLs, timeouts, or server errors; status must always be checked.

---

## Question 10

**Type:** MSQ  
**Difficulty:** Hard

Given this parsed weather fragment:

```json
{
  "latitude": 28.6139,
  "current": {
    "temperature_2m": 34.2,
    "weather_code": 3
  }
}
```

Which statements are **true**? Select **all** that apply.

A. Path to current temperature: **`current` → `temperature_2m`**  
B. In Python after parsing: **`data["current"]["temperature_2m"]`** returns **34.2**  
C. **`json.dumps(data, indent=2)`** converts a Python dict into a formatted JSON **string**  
D. **`json.loads()`** is required immediately after **`response.json()`** on the same `requests` response

**Correct Answers:** A, B, C

**Answer Explanation:**  
A and B are correct — nested key navigation in JSON maps to chained dict access in Python. C is correct — **`json.dumps()`** serialises a dict to a JSON text string (useful for logging).

D is incorrect because **`response.json()`** already parses the body into a dict — calling **`json.loads()`** again on that dict is unnecessary and wrong (loads expects a string).
