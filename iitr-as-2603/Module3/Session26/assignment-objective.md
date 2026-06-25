# Assignment Objective

Total Questions: 10

Difficulty Flow: Easy → Moderate → Hard

Question Types:
- 6 MCQ (Single Correct): Q1–Q6
- 4 MSQ (Multiple Correct): Q7–Q10

**Scope note (assessors):** Questions exclude `response.ok`, exponential-backoff retry loops, `try`/`except` timeout handling, and PATCH/PUT/DELETE verb details. GET, brief POST, and status-code-first parsing are in scope.

---

## Q1 (MCQ, Easy)

**HostelDesk** students keep asking: *"Where is parcel TRK-88421 right now?"* Courier status changes every few minutes and is not stored in the LLM's memory.

What is the best design choice?

A. Paste yesterday's tracking screenshot into the system prompt once  
B. **Call the courier tracking API**, parse the live JSON, and pass only the needed fields into the agent workflow  
C. Ask the LLM to remember the parcel from last week's chat  
D. Raise **temperature** so the model guesses the location faster  

**Correct Answer:** B

**Answer Explanation:**  
Live parcel location is **external, changing data**. An **API** supplies current facts; the agent maps relevant JSON fields into a prompt instead of guessing.

**Why other options are wrong:**  
- A: Stale data causes wrong answers.  
- C: LLMs do not persist real tracking state across chats.  
- D: Temperature affects wording randomness, not access to live data.

---

## Q2 (MCQ, Easy)

**DevSync** documentation says a component defines **what request may be sent** and **what response will be returned** between two software systems.

Which term does this describe?

A. JSON  
B. HTTP status code  
C. **API (Application Programming Interface)**  
D. REST URL path only  

**Correct Answer:** C

**Answer Explanation:**  
An **API** is a **contract** between components — agreed request/response shapes. **REST** and **JSON** are conventions and formats used inside that contract.

**Why other options are wrong:**  
- A: JSON is a data format, not the full contract.  
- B: Status codes summarise success/failure; they are not the contract itself.  
- D: A URL names a resource; the contract includes method, headers, params, and response body.

---

## Q3 (MCQ, Easy)

**FestRoute** needs **today's temperature** from Open-Meteo for Pune outdoor planning. The script must **read** data and **not change** anything on the weather server.

Which HTTP method should the Python script use?

A. **GET**  
B. POST  
C. DELETE  
D. PATCH  

**Correct Answer:** A

**Answer Explanation:**  
**GET** is the read-only method — fetch a resource without modifying server state. Open-Meteo forecast calls in the lab use **GET**.

**Why other options are wrong:**  
- B: **POST** submits or creates data — not needed for a read-only weather fetch.  
- C, D: Not used in this session's read-only weather workflow.

---

## Q4 (MCQ, Easy)

**Nida** receives a courier API payload as one long **JSON string** in variable `raw_text`. She wants a Python **`dict`** so she can write `raw_text_parsed["tracking_id"]`.

Which function should she use first?

A. `json.dumps(raw_text)`  
B. **`json.loads(raw_text)`**  
C. `json.load(raw_text)`  
D. `requests.get(raw_text)`  

**Correct Answer:** B

**Answer Explanation:**  
**`json.loads()`** parses a JSON **string** into a Python **dict**. **`json.load()`** reads from a **file object**, not a string variable.

**Why other options are wrong:**  
- A: **`dumps`** converts dict → string (opposite direction).  
- C: **`load`** expects an open file handle.  
- D: **`requests.get`** sends HTTP requests, not parse strings.

---

## Q5 (MCQ, Moderate)

**Meera** debugs a weather script. She accidentally calls:

`https://api.open-meteo.com/v1/forcast`  
(typo: `forcast` instead of `forecast`)

The server responds, but she should **not** treat the body as weather data.

Which outcome is most likely?

A. **4xx client error** (for example **404 Not Found**) — fix the URL typo  
B. **2xx success** — safe to parse JSON and prompt the LLM  
C. **500** — always means her Python `import` statements are wrong  
D. **401** — always means Open-Meteo requires a paid API key  

**Correct Answer:** A

**Answer Explanation:**  
A wrong path is a **client-side URL mistake** → typically **4xx** (**404**). Check **status before** `response.json()`.

**Why other options are wrong:**  
- B: Non-2xx bodies must not be parsed as weather.  
- C: **5xx** is server-side failure, not Python syntax.  
- D: Open-Meteo forecast used in class is **keyless**; **401** is for auth/key problems.

---

## Q6 (MCQ, Moderate)

After this line runs:

```python
response = requests.get(OPEN_METEO_URL, params=params, timeout=15)
```

**Arjun** wants a Python `dict` of weather data for a campus agent.

What is the correct **next** step?

A. Call `response.json()` immediately — `requests` guarantees valid forecast JSON  
B. **Check `response.status_code == 200`; if not, preview `response.text[:500]` and stop before parsing**  
C. Paste `response.text` into the Groq prompt without reading the status code  
D. Skip status checks when the URL starts with `https://`  

**Correct Answer:** B

**Answer Explanation:**  
**Status-first** handling: verify **200** (success) before **`response.json()`**. Error bodies may be HTML or error JSON — not weather facts.

**Why other options are wrong:**  
- A: Failed requests can return non-JSON error bodies.  
- C: Risks **hallucination grounded in error pages**.  
- D: HTTPS does not imply success.

---

## Q7 (MSQ, Moderate)

**CampusNet** is standardising read-only API calls in Python with **`requests`**. Which practices match the **safe GET** approach from the weather lab?

A. Pass latitude and longitude via **`params=`** so they become URL query parameters  
B. Set **`timeout=15`** (or similar) so the call does not hang indefinitely  
C. **Check the status code before calling `response.json()`**  
D. Paste the **entire** API JSON response into every LLM prompt to avoid mapping work  
E. Use **GET** when the task is read-only and should not change server state  

**Correct Answers:** A, B, C, E

**Answer Explanation:**  
Safe **GET**: **`params`**, **`timeout`**, **status check**, then parse. **GET** for read-only fetches.

**Why other options are wrong:**  
- D: Dumping full JSON wastes **tokens** and weakens clear **grounding**.

---

## Q8 (MSQ, Moderate)

**Open-Air IIT** agents fetch a large Open-Meteo JSON tree but only need **city**, **temperature**, and a **plain-language weather description** for the Groq prompt.

Why **map fields into variables** instead of pasting raw JSON?

A. **Reduces token usage** in the downstream LLM prompt  
B. **Clearer grounding** — the model sees only relevant live facts  
C. Lets developers **test extracted variables** before paying for an LLM call  
D. Removes the need to ever check HTTP status codes  
E. Converting **`weather_code`** numbers to **words** (for example "overcast") helps the model interpret conditions  

**Correct Answers:** A, B, C, E

**Answer Explanation:**  
**Field mapping** saves tokens, improves grounding, enables pre-LLM validation, and turns codes into prompt-safe language.

**Why other options are wrong:**  
- D: Status checks remain mandatory before parsing.

---

## Q9 (MSQ, Hard)

**FestRoute** builds a **weather → advice** agent: Open-Meteo for live Pune data, then Groq for outdoor setup guidance.

Which steps belong in a **correct** pipeline?

A. **`requests.get`** to Open-Meteo with `latitude` / `longitude` in **`params`**; confirm status **200**  
B. Parse JSON and **extract only needed keys** into a `variables` dict (for example `temperature_c`, `weather_description`)  
C. Build a user prompt that says **use only the live weather facts below** and forbids inventing temperature  
D. Paste the **full** Open-Meteo JSON (all elevation and hourly fields) into Groq to be safe  
E. Call **`client.chat.completions.create`** with the grounded prompt as **user** content  

**Correct Answers:** A, B, C, E

**Answer Explanation:**  
The two-call pattern: **GET → map → grounded prompt → Groq**. Extract minimal fields; do not dump the full tree.

**Why other options are wrong:**  
- D: Violates **token discipline** and makes grounding harder to audit.

---

## Q10 (MSQ, Hard)

**OpsDash** is triaging API failures for a campus agent stack. Which statements are **correct**?

A. An invalid **`GROQ_API_KEY`** on a Groq completion call often returns **401 Unauthorized**  
B. **50+ Groq calls in one minute** on the free tier can trigger **429 Rate limit** — slow down and reduce call frequency  
C. A successful Open-Meteo **GET** with parseable forecast data typically returns **200 OK**  
D. **429** always means the Python file has invalid **JSON syntax**  
E. If Open-Meteo returns **200** but your code reads `temperture_2m` (typo) instead of `temperature_2m`, the API endpoint failed with **404**  

**Correct Answers:** A, B, C

**Answer Explanation:**  
**401** = auth/key problems. **429** = rate limits (not syntax). **200** = HTTP success. A **200** with a **key typo in your mapping code** is a **Python mapping bug**, not a **404** endpoint failure.

**Why other options are wrong:**  
- D: **429** is throttling, not JSON syntax.  
- E: **404** means wrong endpoint/path; **200** means the HTTP call succeeded.
