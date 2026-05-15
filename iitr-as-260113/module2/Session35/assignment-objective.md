# Objective Assignment — Tool Integration in AI Agents

**Total Questions:** 10 | **6 MCQs + 4 MSQs**
**Order:** Easy → Moderate → Hard

---

## MCQ — Easy (Single Correct)

### Q1. (Easy | MCQ)

Neha is building a campus helpdesk chatbot. A student asks, "What is the temperature in Chennai right now?" The model's training data ends months ago, so it cannot know today's weather. What capability should Neha add so the assistant can answer with live data?

**Options:**

- A) Increase the model's context window so it remembers more training examples
- B) Register a weather API tool that the agent runtime can call and return JSON results to the model
- C) Ask the student to paste the weather website HTML into the chat
- D) Switch to a larger model so it guesses today's temperature from older patterns

**Correct Answer:** B) Register a weather API tool that the agent runtime can call and return JSON results to the model

**Answer Explanation:**
Live facts such as current weather require an **external tool** (here, a weather API). The model chooses the tool and arguments; the **application runtime** performs the HTTP call and passes structured results back for a natural-language reply.

- A) Incorrect — a larger context window does not add real-time data beyond the training cutoff.
- C) Incorrect — manual HTML pasting is not an agentic tool integration pattern.
- D) Incorrect — guessing from stale patterns is unreliable and not how production agents fetch live data.

---

### Q2. (Easy | MCQ)

In a function-calling setup, a user asks, "Show in-stock mobiles under ₹50,000." The model outputs a structured choice to call `search_product` with arguments. Who actually runs the Python function against SQLite?

**Options:**

- A) The LLM executes the database query inside the model weights
- B) The agent runtime (your Python application) validates arguments and executes the tool
- C) SQLite pushes rows directly into the model's hidden state
- D) The browser frontend opens the `.db` file without backend code

**Correct Answer:** B) The agent runtime (your Python application) validates arguments and executes the tool

**Answer Explanation:**
In **function calling**, the model only emits **which tool** to call and **with what arguments**. The **agent runtime** validates input and performs the real work (HTTP, database, etc.).

- A) Incorrect — the model does not execute application code or query databases directly.
- C) Incorrect — databases are reached through application-layer drivers and ORM code.
- D) Incorrect — tool execution belongs in the backend application, not the end-user browser opening raw files.

---

### Q3. (Easy | MCQ)

A flight-search tool sends `{"source": "Delhi", "destination": "Mumbai", "date": "2026-06-10"}` to a booking API. The response body uses the same key–value and nested-object style as a Python `dict`. Which format is this?

**Options:**

- A) CSV
- B) XML only
- C) JSON
- D) Plain binary protobuf with no text representation

**Correct Answer:** C) JSON

**Answer Explanation:**
**JSON** is the common text wire format for API requests and responses — key–value pairs, arrays, and nested objects that map cleanly to Python dictionaries.

- A) Incorrect — CSV is tabular and does not natively express nested objects the way shown.
- B) Incorrect — XML uses tags, not the brace-and-key style described.
- D) Incorrect — the scenario describes human-readable structured text, not opaque binary-only payloads.

---

### Q4. (Easy | MCQ)

An e-commerce platform splits order, inventory, payment, and notification logic into separate services that talk over HTTP. When an AI agent calls many small capabilities (weather, product search, calendar) instead of one monolithic program, which architectural idea does that mirror?

**Options:**

- A) Microservices — many focused services (or tools) composed through APIs
- B) Single-tier desktop app with no network boundary
- C) Replacing all APIs with manual SQL strings inside the LLM
- D) Storing every tool response only in browser localStorage with no server

**Correct Answer:** A) Microservices — many focused services (or tools) composed through APIs

**Answer Explanation:**
Large platforms use **microservices** — small services communicating via APIs. Agents register multiple **tools** the same way: coordinated capabilities instead of one giant program.

- B) Incorrect — agents integrate over network/API boundaries, not a single offline desktop tier.
- C) Incorrect — tools are invoked by application code; the LLM does not replace drivers or ORM with raw SQL inside the model.
- D) Incorrect — tool results flow through the application/agent loop, not only client-side storage.

---

## MCQ — Moderate (Single Correct)

### Q5. (Moderate | MCQ)

Ravi's `search_product` tool receives `{"category": 1234, "max_price": 50000}` where `category` must be a non-empty string. He unpacks with `ProductSearchInput(**input_data)` inside `try/except ValidationError`. What should happen before any database query runs?

**Options:**

- A) SQLAlchemy coerces `1234` to the string `"1234"` and runs the query
- B) Pydantic rejects the input; the handler returns a structured error payload such as `success: False` with validation details
- C) SQLite raises `OperationalError` because integers cannot appear in WHERE clauses
- D) The LLM automatically rewrites the argument dict to valid types

**Correct Answer:** B) Pydantic rejects the input; the handler returns a structured error payload such as `success: False` with validation details

**Answer Explanation:**
**Pydantic** validates tool arguments at the application boundary. Wrong types (integer for a required string field) raise **ValidationError**, which you catch and return as structured failure — **before** expensive or incorrect external calls.

- A) Incorrect — Pydantic does not silently coerce an integer into a valid non-empty string category in this validation setup.
- C) Incorrect — the failure is input validation, not an SQLite operational error on the query itself.
- D) Incorrect — argument correction is the application's validation layer, not automatic model-side rewriting at execution time.

---

### Q6. (Moderate | MCQ)

A teammate says, "We already installed SQLAlchemy, so we do not need SQLite or PostgreSQL anymore." What is the accurate correction?

**Options:**

- A) SQLAlchemy is a database server that replaces MySQL
- B) SQLAlchemy is a Python toolkit (Core/ORM) that talks to a database through drivers; it is not the database engine itself
- C) SQLAlchemy only works with JSON files, not relational engines
- D) SQLAlchemy is the same thing as Pydantic for HTTP response bodies only

**Correct Answer:** B) SQLAlchemy is a Python toolkit (Core/ORM) that talks to a database through drivers; it is not the database engine itself

**Answer Explanation:**
**SQLAlchemy** provides **Core** and **ORM** layers to connect and query engines such as SQLite, PostgreSQL, or MySQL via **drivers**. It does not replace the database product.

- A) Incorrect — SQLAlchemy is not a standalone database server.
- C) Incorrect — SQLAlchemy targets relational engines through connection URLs and drivers.
- D) Incorrect — Pydantic validates structured data; SQLAlchemy handles persistence and querying.

---

## MSQ — Moderate (Multiple Correct)

### Q7. (Moderate | MSQ)

An agent registry lists `search_product`, `get_weather`, and `send_email`. A user asks for Bangalore weather. **Which statements correctly describe the function-calling pattern?** *(Select all that apply)*

- A) The model may answer directly if it already has sufficient knowledge and no live data is required
- B) If a tool is needed, the model selects a tool name and generates structured arguments such as city and time window
- C) The model opens outbound HTTPS connections to Make My Trip or the weather provider without application code
- D) The application validates arguments, executes the chosen Python function or API request, and returns results (often JSON-like) to the model
- E) Clear tool descriptions help routing more than opaque names like `f1` and `f2`

**Correct Answers:** A, B, D, E

**Answer Explanation:**
- **A — Correct:** Step 2–3 of the tool flow: answer from existing knowledge when no external data is required.
- **B — Correct:** When external data is needed, the model emits structured tool choice and parameters.
- **C — Incorrect:** The **runtime** performs real HTTP/database work; the model does not dial external systems directly.
- **D — Correct:** Validate → execute → feed results back for the final user-facing answer.
- **E — Correct:** Metadata and descriptions guide correct tool selection.

---

### Q8. (Moderate | MSQ)

While wiring tools, **which HTTP method and status-code pairings are appropriate for the described situation?** *(Select all that apply)*

- A) **GET** — fetch current order status for order ID 123 without changing server data
- B) **POST** — create a new support ticket after the user submits a form body
- C) **404** — the requested product ID does not exist at the URL the client called
- D) **201** — the client sent malformed JSON missing a required field
- E) **401** — the API key or auth token is missing or invalid for a protected booking endpoint

**Correct Answers:** A, B, C, E

**Answer Explanation:**
- **A — Correct:** **GET** reads resources without mutating state.
- **B — Correct:** **POST** commonly creates a new resource (ticket).
- **C — Correct:** **404** means the resource or route was not found.
- **D — Incorrect:** missing/invalid client payload is typically **400 Bad Request**; **201 Created** signals successful resource creation.
- **E — Correct:** **401** indicates authentication failure (missing or bad credentials).

---

## MSQ — Hard (Multiple Correct)

### Q9. (Hard | MSQ)

In the `agent_tool_call` style demo, `search_product` filters mobiles by `category`, `max_price`, and `in_stock` after Pydantic validation. **Which statements about that stack are correct?** *(Select all that apply)*

- A) `ProductSearchInput` can default `in_stock` to `True` when the caller omits that field
- B) `select(Product).where(...)` expresses an ORM read query without hand-written SQL strings in application code
- C) `session.scalars(query).all()` returns a list of `Product` ORM instances, not automatically pretty-printed JSON for the LLM
- D) Calling `insert_data()` on every run without clearing the table can duplicate seed rows in SQLite
- E) Passing `max_price: 0` should pass validation because zero is a valid integer
- F) `create_engine("sqlite:///e-commerce.db")` opens a connection to a file-backed SQLite database in the project context

**Correct Answers:** A, B, C, D, F

**Answer Explanation:**
- **A — Correct:** Optional `in_stock` defaults to **True** when omitted.
- **B — Correct:** ORM `select` + `where` builds the query from mapped attributes.
- **C — Correct:** Results are **ORM objects**; you shape dicts/JSON for the model if needed.
- **D — Correct:** Re-seeding without deduplication can insert duplicates — noted in the live build.
- **E — Incorrect:** `max_price` must be **greater than zero** (`gt=0`); zero fails validation.
- **F — Correct:** The SQLite URL targets a local `e-commerce.db` file via the engine.

---

### Q10. (Hard | MSQ)

A product assistant traces one user question end to end. **Which steps belong in the correct order and responsibility split?** *(Select all that apply)*

- A) The user query enters the agent; the LLM decides whether to answer from memory or request a tool
- B) Structured tool arguments are validated in Python (for example with Pydantic) before external execution
- C) SQLAlchemy ORM runs the database read; rows return to Python for optional reshaping before the model's final reply
- D) The LLM writes directly to SQLite tables to avoid latency from Python
- E) External SaaS tools are still reached through API-style requests whose bodies and responses are commonly JSON
- F) Production integrations for booking, email, or payments should include authentication such as API keys or OAuth

**Correct Answers:** A, B, C, E, F

**Answer Explanation:**
- **A — Correct:** User in → routing decision (direct answer vs tool).
- **B — Correct:** Application-side validation guards the tool boundary.
- **C — Correct:** ORM executes the read; Python holds results until the model summarizes.
- **D — Incorrect:** Persistence is executed by **application code**, not the LLM writing to the DB.
- **E — Correct:** Third-party tools follow the same API + JSON pattern as internal ones at the boundary.
- **F — Correct:** Real tools require **auth**; demos may skip it, production must not.
