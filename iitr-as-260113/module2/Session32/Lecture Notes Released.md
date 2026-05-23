# Working with APIs and JSON

## Context of the Session

In the previous session, we explored how AI agents use **external tools and APIs to perform actions** — covering function calling, how Pydantic validates structured data, and how SQLAlchemy lets Python talk to databases. You saw the full backend stack that an agent uses to query, validate, and return data.

Today, we zoom out and go deeper into the foundation that makes all of that work — **APIs and JSON**. Here is what we will cover:

- What APIs are, and why every AI application depends on them
- How modern software (websites, apps, AI agents) is structured in three layers
- How data flows from the user to the backend to the database and back
- How REST APIs are designed, and what HTTP methods mean
- How to read API request and response structure
- What HTTP status codes mean and when you'll see them
- What JSON is, and how to parse and create JSON in Python

---

## Why APIs Matter — Especially for AI

Before we dive into the technical details, let us understand **why** this topic matters for someone building AI agents.

Imagine you are building an **AI travel agent** — an application that generates itineraries, checks flight prices, books hotels, and compares deals across Make My Trip, Expedia, and Air India. Your agent is smart, but it cannot do any of this by itself. It needs to **talk to external systems** — and the only way software systems talk to each other is through **APIs**.

Here is the key insight:

- **Every time your agent checks flight prices**, it makes an API call to Make My Trip or a similar service.
- **Every time your agent asks an LLM to generate text**, it makes an API call to OpenAI or Gemini.
- **Every time a user clicks a button on any website**, the browser makes an API call to the backend.

APIs are not just a web development thing. They are the **universal language that all modern software uses to communicate** — including AI applications.

---

## What Is an API?

**API** stands for **Application Programming Interface**.

- **Official Definition:** An API is a contract between two software components that defines what request can be sent and what response will be received.
- **In Simple Words:** An API is a structured way for one piece of software to ask another piece of software to do something, and get a result back.
- **Real-Life Example:** Think of an API like the **menu at a restaurant**. The menu lists exactly what you can order, the format in which you order it, and what you will receive. You cannot order something that is not on the menu. Similarly, an API defines exactly what "orders" (requests) a system accepts and what it will return.

Here are two ways to think about APIs:

- **APIs as a Bridge:** APIs are the bridge between the agent's brain and real-world software applications. When your Python code calls `client.responses.create(...)`, it is crossing that bridge into OpenAI's servers.
- **APIs as a Contract:** An API is a contract between two parties. Make My Trip's API says: "Send me source, destination, and date — I will return flight prices." If you do not follow the contract (for example, forget to send the source city), you get an error back.

![API as a contract — like a menu that defines what you can request and what you receive in return](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/session34/session34-01-api-contract-menu.png)

> **Quick Note on MCP:** You may have heard the term **MCP (Model Context Protocol)**. It acts as a relationship manager — instead of your application directly dealing with OpenAI's contract and then Gemini's contract separately, MCP sits in the middle and handles the communication for you. We will cover MCP in a dedicated session.

---

## How Modern Software Is Structured

To understand APIs, you need to understand **where they fit in a software application**. Every modern application — whether it is Amazon, Swiggy, or your AI agent — is divided into three main layers.

### The Three Layers

| Layer | What It Is | Real-Life Analogy |
|---|---|---|
| **Frontend** | The part the user sees and interacts with | The dining area of a restaurant — what you see and interact with |
| **Backend** | The "brain" that processes all requests and enforces rules | The kitchen — where all the cooking/processing happens |
| **Database** | Permanent storage for all data | The pantry/storeroom — where all ingredients (data) are stored |

**Frontend** is anything the user interacts with:
- Websites (Amazon.in, Swiggy.com)
- Mobile apps (Zomato app, Uber app)
- Voice interfaces (Alexa, Google Assistant)
- Wearables (smartwatch apps)

**Backend** is the most important layer — it is the brain. It takes the user's request, figures out what to do, fetches data from the database, and prepares the response. If the backend is slow (for example, searching for "iPhone" takes 10 minutes), no one will use the app — no matter how beautiful the website looks.

**Database** is where all data lives. Amazon has millions of products, millions of users, millions of orders. All of that data is stored in databases and retrieved on-demand.

![Three layers of modern software — frontend (what users see), backend (processing), and database (durable storage)](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/session34/session34-02-three-layers-fe-be-db.png)

---

## The Full Request Flow: FE → API → BE → API → DB

Let us trace exactly what happens when you click on **"My Orders"** on Swiggy:

1. **User clicks "My Orders"** on the Swiggy app (Frontend).
2. **Frontend sends an API request** to the backend — specifically a `GET /orders` request (you are trying to *get* or *read* your order details).
3. **Backend receives the request** and first validates: "Is this user actually logged in?"
4. **Backend queries the database** — something like `SELECT * FROM orders WHERE user_id = 123`.
5. **Database returns the matching records** to the backend.
6. **Backend formats the data as JSON** and sends it back as the API response.
7. **Frontend receives the response** and displays the list of orders on screen.

> **Where do AI Agents live in this flow?** Agents are written and run in the **backend layer**. The frontend takes a user's message, sends it to the backend via an API, and the backend decides which agent to trigger. For example: if the user types "book me a flight to Bangalore", the backend creates a flight-booking agent that then calls Make My Trip's API.

![End-to-end request flow — from user action through API, backend, database, JSON response, and back to the screen](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/session34/session34-03-request-flow-fe-api-be-db.png)

---

## REST APIs — A Convention for Designing APIs

You will constantly hear the term **REST API**. Let us understand what it means.

- **Official Definition:** REST stands for **Representational State Transfer**. It is a set of design guidelines for structuring APIs around the data (resources) they work with.
- **In Simple Words:** REST says your API endpoints (names/URLs) should be named after the *thing* they operate on — not the *action* they perform.
- **Real-Life Example:** Instead of naming APIs as `create-user`, `get-user`, `delete-user` (action-focused), REST says just call them `/users` and express the action through the HTTP method.

**REST Principle in Practice:**

| What you want to do | Non-REST (action in URL) | REST style |
|---|---|---|
| Get all courses | `/get-courses` | `GET /courses` |
| Get one course | `/get-course-by-id` | `GET /courses/123` |
| Create a new order | `/create-order` | `POST /orders` |
| Update a user's phone | `/update-phone` | `PATCH /users/123` |
| Delete an account | `/delete-user` | `DELETE /users/123` |

> **Important note:** REST is a **convention, not a strict rule**. Real-world applications often cannot follow REST 100% — that is completely fine. But understanding REST helps you read and design APIs much more easily.

![REST style — resource-based URLs paired with HTTP methods for read, create, partial update, full replace, and delete](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/session34/session34-04-rest-http-methods-crud.png)

---

## HTTP Methods — The "Action" in Every API Call

Every API call carries a **method** that tells the server what action to perform. These map directly to the four CRUD operations.

### The Five HTTP Methods

**GET — Read / Fetch a resource**
- Use it when you want to *retrieve* data without changing anything.
- Example: `GET /orders` → give me all the orders for the logged-in user.
- Example: `GET /courses/123` → give me the details of course number 123.
- No request body needed — you are just asking for data.

**POST — Create a new resource**
- Use it when you want to *add something new*.
- Example: `POST /orders` → place a new order.
- You pass all the details of the new resource in the **request body** (because there may be hundreds of fields).

**PATCH — Partial Update**
- Use it when you want to update *only a few fields* of an existing resource.
- Example: `PATCH /users/123` with body `{"phone": "9876543210"}` → update only the phone number.
- Does not replace the entire record — just updates what you send.

**PUT — Full Replacement**
- Use it when you want to *completely replace* an existing resource.
- Example: At a gym app like Cult Fit — transferring a membership from one user to another replaces the entire membership object.
- Think of it as: take out the old record completely and put in a new one.

**DELETE — Remove a resource**
- Use it when you want to *delete* something permanently.
- Example: `DELETE /users/123` → delete the account with ID 123.
- Usually no request body — just specify the ID in the URL.

### Quick CRUD Mapping

| CRUD | HTTP Method | Meaning |
|---|---|---|
| Create | POST | Add new resource |
| Read | GET | Fetch resource |
| Update (partial) | PATCH | Modify some fields |
| Update (full) | PUT | Replace entire object |
| Delete | DELETE | Remove resource |

---

## Structure of an API Request

Every API request you send has four components. Think of these like a formal letter — there is an address, a subject, some context, and the message itself.

### The Four Parts

![The four parts of an API request — URL, HTTP method, headers (auth and content type), and optional JSON body](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/session34/session34-05-api-request-four-parts.png)

**1. URL / Endpoint**
The address of the API. It includes the domain and the resource path.

```
https://www.flipkart.com/search?q=iphone
```

- `https://` — the protocol (how data travels over the internet)
- `www.flipkart.com` — the domain (which server to talk to)
- `/search` — the API endpoint (which functionality to use)
- `?q=iphone` — query parameters (the search term you are passing)

**2. Method**
The HTTP method: `GET`, `POST`, `PUT`, `PATCH`, or `DELETE`.

**3. Headers**
Metadata attached to the request — most importantly, **authentication tokens**.
- When you log in to Amazon, the server gives your browser a **token** (like a digital ID card).
- With every future request, your browser automatically attaches that token in the headers.
- The server reads the token to know *who* is making the request.
- Headers also specify the **content type**: `"Content-Type": "application/json"` tells the server the body is in JSON format.

**4. Body (Request Body)**
The actual data you are sending — used with `POST`, `PUT`, and `PATCH` requests.
- For GET and DELETE, there is usually no body.
- For POST/PATCH, the body is a JSON object with all the fields you want to create or update.

> **Live Proof:** You can see all of this in action by opening any website (like Flipkart), pressing `F12`, going to the **Network tab**, and performing a search. You will see every API request your browser makes — including the URL, method, request headers, and payload (body).

---

## Structure of an API Response

When the server responds to your request, it sends back:

**1. Status Code**
A three-digit number that immediately tells you if the request worked or not.

**2. Response Headers**
Metadata coming back from the server (for example, a new authentication token after login).

**3. Response Body**
The actual data you requested — almost always in **JSON format**.

---

## HTTP Status Codes — The Server's Feedback

Status codes are organized into groups by their first digit. You do not need to memorize every code — just remember the **pattern**.

### The Pattern

| Code Range | Meaning | Who is at fault? |
|---|---|---|
| **2xx** | Success | Nobody — everything went well |
| **4xx** | Client Error | You (the client) made a mistake |
| **5xx** | Server Error | The server has a problem |

### Most Common Status Codes

| Code | Name | When You See It |
|---|---|---|
| **200** | OK | Request was successful — data returned as expected |
| **201** | Created | A new resource was successfully created (e.g., order placed) |
| **400** | Bad Request | You sent an invalid or incomplete request (e.g., missing source city in a flight search) |
| **401** | Unauthorized | You are not logged in or your token is invalid |
| **403** | Forbidden | You are logged in, but you do not have *permission* (e.g., trying to access the admin panel) |
| **404** | Not Found | The URL or resource you requested does not exist (e.g., typing a wrong URL) |
| **500** | Internal Server Error | Something went wrong on the server side — not your fault |

![HTTP status families — 2xx success, 4xx client mistakes, 5xx server problems — with common codes you will see in practice](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/session34/session34-06-http-status-code-families.png)

**Everyday examples:**
- You search `masaischool.com/abcxyz` (a page that does not exist) → **404 Not Found**
- You try to open `masaischool.com/admin` without being an admin → **403 Forbidden**
- Amazon's backend crashes during a sale → **500 Internal Server Error**

---

## JSON — The Language APIs Speak

Now we come to the format that APIs use to send and receive data: **JSON**.

- **Official Definition:** JSON stands for **JavaScript Object Notation**. It is a lightweight, text-based format for storing and transmitting structured data between systems over a network.
- **In Simple Words:** JSON is a way to write data as structured text — using **key-value pairs** — that is easy for both humans to read and machines to process.
- **Real-Life Example:** Think of JSON like a **filled-in form**. A form has labels (keys) and the information you wrote in (values) — `Name: Ravi`, `Age: 25`, `City: Mumbai`. JSON is exactly like that, but in a format computers can send over the internet.

![JSON as structured key–value text — and how json.loads / json.dumps swap between strings and Python dictionaries](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/session34/session34-07-json-python-roundtrip.png)

### JSON Structure

A JSON object uses curly braces `{}`, with **key-value pairs** separated by commas. Keys are always strings (in quotes). Values can be strings, numbers, booleans, lists, or even nested JSON objects.

```json
{
  "order_id": 101,
  "customer": {
    "name": "Ravi Sharma",
    "email": "ravi@example.com"
  },
  "items": [
    { "name": "Laptop", "price": 65000 },
    { "name": "Mouse", "price": 799 }
  ],
  "status": "placed"
}
```

### JSON Data Types

| JSON Type | Example | Python Equivalent |
|---|---|---|
| String | `"name": "Ravi"` | `str` |
| Number (int) | `"age": 25` | `int` |
| Number (float) | `"price": 65000.50` | `float` |
| Boolean | `"is_active": true` | `bool` |
| Null | `"discount": null` | `None` |
| Array (List) | `"items": [...]` | `list` |
| Object (Dict) | `"customer": {...}` | `dict` |

> **Key Insight:** JSON objects look almost identical to Python dictionaries. The main difference: in JSON, keys must always be in double quotes, and `true`/`false` are lowercase. This makes working with JSON in Python very natural.

---

## Working with JSON in Python

Python has a built-in module called **`json`** that gives you two essential functions.

### `json.loads()` — Parse: JSON String → Python Dictionary

When you receive a JSON response from an API, it arrives as a **text string**. You cannot directly access `response["order_id"]` until you **parse** it (convert the string into a Python dictionary).

- **`json.loads()`** = **L**oad **S**tring → converts a JSON string into a Python dictionary.

### `json.dumps()` — Stringify: Python Dictionary → JSON String

When your application wants to **send** data to an API (for example, when placing an order), you need to convert your Python dictionary into a JSON string first.

- **`json.dumps()`** = **D**ump to **S**tring → converts a Python dictionary into a JSON string.

### Full Code Example: Parsing and Stringifying JSON

```python
# Import the built-in JSON module — no installation needed
import json

# ─────────────────────────────────────────────────────────────────
# PART 1: json.loads() — Parsing a JSON string into a Python dict
# ─────────────────────────────────────────────────────────────────

# Imagine this is the raw JSON response we received from an API
# It looks like our data, but it is just ONE big string right now
json_response_string = '''
{
    "order_id": 101,
    "customer": {
        "name": "Ravi Sharma",
        "email": "ravi@example.com"
    },
    "items": [
        {"name": "Laptop", "price": 65000},
        {"name": "Mouse", "price": 799}
    ],
    "status": "placed"
}
'''

# Convert the JSON string into a Python dictionary using json.loads()
# After this, 'order' is a real Python dict — we can access fields easily
order = json.loads(json_response_string)

# Now we can access individual fields using dictionary syntax
print("Order ID:", order["order_id"])                      # prints: 101
print("Customer Email:", order["customer"]["email"])       # prints: ravi@example.com
print("First Item Name:", order["items"][0]["name"])       # prints: Laptop
print("Order Status:", order["status"])                    # prints: placed

# ─────────────────────────────────────────────────────────────────
# PART 2: json.dumps() — Converting a Python dict to a JSON string
# ─────────────────────────────────────────────────────────────────

# Imagine we are creating a new order in Python and need to send it to an API
# We build the data as a Python dictionary first
new_order = {
    "order_id": 202,
    "product_id": 1000,
    "product_name": "iPhone 15",
    "price": 89999
}

# Convert the Python dictionary into a JSON string using json.dumps()
# indent=2 makes the output nicely formatted and readable
json_string = json.dumps(new_order, indent=2)

# Now json_string is ready to be sent in an API request body
print("\nJSON ready to send to API:")
print(json_string)

# If you check the type — it is a string, not a dict
print("\nType of json_string:", type(json_string))  # <class 'str'>
```

**How the code works:**

- `import json` — loads Python's built-in JSON module. No pip install needed.
- `json.loads(json_response_string)` — takes the raw text coming from an API and turns it into a Python dictionary you can work with.
- `order["customer"]["email"]` — once parsed, you navigate nested data exactly like a Python dictionary.
- `order["items"][0]["name"]` — JSON arrays become Python lists; you access elements by index.
- `json.dumps(new_order, indent=2)` — takes a Python dictionary and turns it into a formatted JSON string ready to be sent in an API request body.
- The `type(json_string)` check confirms JSON is fundamentally just a string — that is why it is easy to send over the internet.

---

## AI Models Are Also Just APIs

Here is the big reveal — **calling OpenAI or Gemini is exactly the same as any other API call**. There is nothing magical about it.

![Large language models are consumed like any other API — client, authenticated POST, JSON response with the model's answer](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/session34/session34-08-llm-as-api-call.png)

When you write this code in Python:

```python
# Install the library: pip install openai
from openai import OpenAI

# Step 1: Create a client — this sets up the "contract" with OpenAI
# The API key tells OpenAI who you are (authentication)
client = OpenAI()  # automatically reads OPENAI_API_KEY from environment

# Step 2: Make an API call — POST request to OpenAI's servers under the hood
# You are sending: model name, instructions, and your prompt (the request body)
response = client.responses.create(
    model="gpt-4o",                             # which model to use
    instructions="You are a helpful assistant", # system prompt
    input="What is the capital of India?"       # user's question (the prompt)
)

# Step 3: The response comes back as a structured JSON object
# You read the model's reply from the response — just like reading order["status"]
print(response.output_text)  # prints the model's answer
```

**How the code works:**

- `from openai import OpenAI` — imports the OpenAI library which handles the low-level HTTP request for you.
- `OpenAI()` — creates a client object. This is like signing the contract with OpenAI. It reads your API key from the environment variable `OPENAI_API_KEY`.
- `client.responses.create(...)` — this is the actual API call. Under the hood, it sends a `POST` request to OpenAI's server with your prompt in the request body.
- The response comes back as a JSON object containing the model's reply, usage stats, and other metadata.
- `response.output_text` — you access the model's reply from the structured response — exactly like accessing `order["status"]` from an order JSON.

> **Switching from OpenAI to Gemini?** The pattern is the same — create a Gemini client, get a Gemini API key, and call Gemini's version of the create function. The specific method names differ (different contract), but the overall flow of: *install library → create client → make call → read response* remains identical.

---

## Key Takeaways

- **APIs are contracts** between software systems that define what request to send and what response to expect — every modern application (including AI agents) communicates through APIs.
- **Modern software has three layers** — Frontend (user-facing), Backend (brain/processing), Database (storage) — and AI agents live in the backend layer, calling APIs to external tools and LLMs.
- **REST APIs organize endpoints around resources** (`/orders`, `/users`) and express actions through HTTP methods: `GET` (read), `POST` (create), `PATCH` (partial update), `PUT` (full replace), `DELETE` (remove).
- **HTTP status codes give immediate feedback**: 2xx = success, 4xx = your mistake, 5xx = server's problem — with 200 (OK), 201 (Created), 400 (Bad Request), 401 (Unauthorized), 403 (Forbidden), 404 (Not Found), 500 (Internal Server Error) being the most common.
- **JSON is just text shaped like a Python dictionary** — `json.loads()` converts incoming JSON strings to Python dicts so you can work with the data, while `json.dumps()` converts Python dicts to JSON strings so you can send them in API requests.

In the next session, we will revisit these API and JSON concepts in the context of **how agents actively use tools** — you will see how agents make decisions about which API to call, send the request, and use the JSON response to decide their next action.

---

## Important Commands, Libraries, and Terminologies

| Term / Command | What It Is |
|---|---|
| **API** | Application Programming Interface — a contract between two software components for request-response communication |
| **REST** | Representational State Transfer — a convention for designing APIs around resources (nouns, not actions) |
| **Endpoint** | The specific URL path of an API (e.g., `/orders`, `/users/123`) |
| **HTTP** | HyperText Transfer Protocol — the protocol the internet uses to send requests and responses |
| **GET** | HTTP method to read/fetch a resource (no body) |
| **POST** | HTTP method to create a new resource (with body) |
| **PATCH** | HTTP method to partially update a resource (only the fields you send) |
| **PUT** | HTTP method to fully replace a resource (with body) |
| **DELETE** | HTTP method to remove a resource (usually no body) |
| **Request Body** | The JSON data payload sent with POST, PATCH, or PUT requests |
| **Headers** | Metadata in the request/response — most importantly holds authentication tokens |
| **Authentication Token** | A digital "ID card" given to you after login; attached in headers to prove who you are |
| **Status Code** | A 3-digit number in the response: 2xx = success, 4xx = client error, 5xx = server error |
| **200 OK** | Request was successful |
| **201 Created** | New resource was created successfully |
| **400 Bad Request** | Client sent invalid or incomplete input |
| **401 Unauthorized** | Not logged in or invalid token |
| **403 Forbidden** | Logged in, but no permission for this action |
| **404 Not Found** | URL or resource does not exist |
| **500 Internal Server Error** | Server-side bug or crash |
| **JSON** | JavaScript Object Notation — lightweight text format for structured data exchange |
| **`json.loads()`** | Python function to parse a JSON string into a Python dictionary |
| **`json.dumps()`** | Python function to convert a Python dictionary into a JSON string |
| **CRUD** | Create, Read, Update, Delete — the four fundamental operations on any data |
| **Domain** | The base address of a server (e.g., `www.flipkart.com`) |
| **Query Parameter** | Extra parameters in the URL after `?` (e.g., `?q=iphone`) |
| **`import json`** | Python standard library — no pip install needed |
| **MCP** | Model Context Protocol — an abstraction layer that helps agents switch between LLM providers without rewriting code |
