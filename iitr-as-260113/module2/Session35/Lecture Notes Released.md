# Tool Integration in AI Agents

## What We Covered Last Time & What's Coming Today

Last time, we built a clear picture of how modern software talks to the world through **APIs** and **JSON**. We saw layered architecture (frontend, backend, database), the **request–response cycle**, **HTTP methods**, **status codes**, and how API payloads are shaped as JSON objects that behave like Python dictionaries.

Today we connect that API foundation to **agentic action**. An agent is not useful if it can only chat — it must **call tools** (Make My Trip, a weather service, your own database, and more). We will cover:

- A quick API recap so tool calls feel familiar, not new
- **Function calling** — how the model chooses a tool and the runtime executes it
- Why every external tool is ultimately an **API call** returning JSON
- How Python connects to a database through **drivers**, **ORM**, **Pydantic**, and **SQLAlchemy**
- A full **agent_tool_call** demo: validate input, query SQLite, return structured results
- How you would wire an **LLM** to pick tools in a real application

---

## Why Tools Matter for AI Agents

**Tools** (also called **functions** in code) are how an agent reaches outside its own text generation.

- **Official Definition:** In agentic systems, a tool is an external capability — API, database query, calculator, email sender — that the agent can invoke to perform an action and receive structured data back.
- **In Simple Words:** The agent is the smart coordinator; tools are the hands that actually do the work.
- **Real-Life Example:** A travel desk employee who can only give general advice is like a chat-only model. Give them phone access to Make My Trip, Expedia, and a calendar API, and they become an agent that can **book**, not just **suggest**.

Without tools, questions like “What is the weather in Delhi **right now**?” fail because the model’s training data has a **cutoff date**. With a weather API tool, the agent fetches live data and answers accurately.

![An AI agent as coordinator — registered tools (weather, travel, database, calculator) extend what it can do beyond chat alone](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/session35/session35-01-agent-coordinator-tools.png)

---

## Quick Recap: APIs as the Communication Layer

Every tool integration in this session sits on the same API ideas from the previous class.

### What an API Is

- **Official Definition:** An **API (Application Programming Interface)** is a contract between two software systems that defines how they request and exchange data.
- **In Simple Words:** A fixed menu of allowed requests and responses — you cannot order off-menu.
- **Real-Life Example:** Razorpay’s payment API tells Amazon’s payment service exactly what to send and what it will get back when initiating a charge.

### Client, Server, and Request–Response

- **Client** initiates the request (needs data or wants an operation).
- **Server** receives the request, processes it, and returns a **response**.
- **Client** and **server** are **relative** roles. Amazon’s order service is a **client** when it calls the payment service; payment service is a **client** when it calls Razorpay.

![Client–server request–response — who initiates the call, who processes it, and how data travels back as JSON](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/session35/session35-02-client-server-request-response.png)

### Microservices at Scale

Large platforms like Amazon split the backend into **microservices** — order service, product service, inventory, notifications, payment, and more. Each service talks to others through APIs. The same pattern appears when an agent calls many small tools instead of one giant program.

![Microservices at platform scale mirror an agent’s tool registry — many small capabilities connected through APIs](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/session35/session35-03-microservices-and-agent-tools.png)

### HTTP Methods (Quick Map)

| Method | Typical use |
|---|---|
| **GET** | Read / fetch data (e.g. all orders vs one order by ID) |
| **POST** | Create a new resource |
| **PUT / PATCH** | Update (full replace vs partial) |
| **DELETE** | Remove a resource |

Example from class: `GET /orders` often returns all orders; `GET /orders/123` targets one order — exact behaviour depends on how the API is implemented.

### Status Codes (Three Families)

- **2xx** — Success (e.g. **200** OK, **201** Created when a new resource is made).
- **4xx** — **Client** error (e.g. **401** Unauthorized, **404** Not Found).
- **5xx** — **Server** error (e.g. **500** Internal Server Error, **502** Bad Gateway).

When a tool returns **404**, the URL or resource may be wrong. **401** often means missing or wrong credentials.

### JSON as the Wire Format

- **Official Definition:** **JSON (JavaScript Object Notation)** is a text format of key–value pairs, arrays, and nested objects used for API bodies and responses.
- **In Simple Words:** A standard envelope every system can open — very similar to a Python `dict`.
- **Real-Life Example:** Flight search arguments (`source`, `destination`, `date`, `passengers`) travel as JSON; the agent reads JSON results back into its reasoning loop.

---

## Function Calling in AI Agents

**Function calling** means giving the model a **list of available tools** and letting it decide **which tool to call** and with **what arguments**.

- **Official Definition:** Function calling is the pattern where an LLM emits a structured tool choice and parameters; the application validates and runs the call, then feeds results back to the model.
- **In Simple Words:** The brain picks the hammer; your Python code swings it.
- **Real-Life Example:** You register Make My Trip, weather, calculator, and database search tools. A user asks for Bangalore weather — the model selects the weather tool with `city` and time arguments.

**Important:** The model does **not** call Make My Trip or your database directly. It only **decides** and outputs structured intent. The **agent runtime** (your Python application) performs the real HTTP or database work.

![Function calling — the LLM chooses the tool and arguments; your Python runtime performs the real API or database work](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/session35/session35-04-function-calling-brain-runtime.png)

### Nine-Step Tool-Call Flow (As Walked Through in Class)

1. **User asks a question** — e.g. “What is the current weather in Delhi?”
2. **Model checks** whether it already has enough knowledge to answer without a tool.
3. **If yes** — it answers directly (no tool call).
4. **If no** — it picks a tool from the list you registered (each tool has a **name** and **description**).
5. **Model generates structured arguments** for that tool (city, dates, category, price cap, etc.).
6. **Application validates arguments** — types, required fields, ranges — before any external call. LLMs and users both make mistakes.
7. **Application executes** the Python function or API request.
8. **Tool returns data** — usually as JSON or JSON-like structures.
9. **Application sends results back to the model**; the model writes a user-friendly final answer.

![Nine-step tool-call flow — from user question through tool choice, validation, execution, JSON result, and final answer](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/session35/session35-05-nine-step-tool-call-flow.png)

**Authentication:** Real tools (booking, email, payments) almost always need **auth** (API keys, OAuth). The class demo skipped auth; production integrations must include it.

**Tool metadata:** Descriptions matter more than arbitrary function names (`f1`, `f2`). A clear description — “Search products in the e-commerce database by category and max price” — helps the model route correctly.

---

## How Agents Use APIs as Tools

Whether the tool is Make My Trip, a weather API, or your **own database exposed through Python**, the agent side of the story is the same:

- Send a request with the right **method**, **headers**, and **body**.
- Read **status code** and **JSON body**.
- Pass that JSON back into the agent loop for the next reasoning step.

Internal tools (your SQLite product table) still flow through Python functions that **behave like tools** in the agent registry — the database is not “inside” the LLM; it is a separate entity the app reaches on the model’s behalf.

![Agents use external tools through API-style requests — method, headers, body in; status code and JSON out](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/session35/session35-06-agents-use-apis-as-tools.png)

---

## Connecting Applications to Databases

Agents do not talk to raw database files by hand. Your **Python application layer** sits in the middle.

- **Database drivers / connectors** — libraries that open a fast, reliable connection to MySQL, PostgreSQL, SQLite, etc.
- **ORM (Object–Relational Mapping)** — maps a Python **class** to a database **table** and attributes to **columns**, so you avoid hand-maintaining huge schemas.
- **Why not only manual SQL strings in Python?** Possible, but slow to write, easy to mistype, and painful when joins and filters grow.

**SQLAlchemy** is the library used in class — it is **not** a database; it is Python code that speaks to databases through drivers and optional ORM.

![Application layer between agent and database — drivers, ORM, and SQLAlchemy over SQLite or other engines](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/session35/session35-07-app-database-connection-stack.png)

### SQLAlchemy Core vs ORM

- **Core** — lower-level; you define tables more explicitly (seen in earlier classes).
- **ORM** — define classes like `Product`; SQLAlchemy creates tables and builds queries from Python attributes. **ORM is the style used in today’s live build.**

---

## Pydantic for Tool Input Validation

Before a tool hits the database or a paid API, validate the argument dict.

- **Official Definition:** **Pydantic** is a Python library that defines data models with types and constraints and raises **ValidationError** when input does not match.
- **In Simple Words:** A bouncer that checks shape and types at the door.
- **Real-Life Example:** A flight tool without `destination` should fail fast in Python — not after an expensive bad API call.

In this session, Pydantic validated **tool arguments** (e.g. product search filters). Modelling full HTTP request/response bodies for REST APIs is the same idea and is exercised more in API-focused work; here the focus is the **agent tool boundary**.

### ProductSearchInput Model (Concept from Demo)

- **category** — required `str`, minimum length 1 (no empty string tricks).
- **max_price** — required `int`, must be **greater than zero**.
- **in_stock** — optional `bool`, default **True** (only show in-stock items unless the caller overrides).

Unpacking: `ProductSearchInput(**input_data)` turns a plain `dict` into a validated object. Wrong types (e.g. integer `1234` for `category`) trigger validation; **try/except** around `ValidationError` returns a clean error payload instead of crashing the agent.

![Pydantic validates tool arguments before any database or paid API call — types, required fields, and constraints at the door](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/session35/session35-08-pydantic-validation-bouncer.png)

---

## Live Build: agent_tool_call Project

The instructor created a new project **`agent_tool_call`** with a virtual environment, installed **pydantic**, **sqlalchemy**, and noted **openai** for a follow-on LLM hook-up.

### Setup Commands

```bash
# Create an isolated Python environment for this project
python3 -m venv venv

# Activate it (macOS/Linux)
source venv/bin/activate

# Install libraries used in the demo
pip3 install pydantic sqlalchemy openai
```

**How the setup works:**
- `venv` keeps project dependencies separate from system Python.
- `pydantic` validates tool arguments.
- `sqlalchemy` connects to SQLite and runs ORM queries.
- `openai` is for the next step when you let the LLM choose tools (students were asked to integrate the API key themselves).

### Full Application Code (app.py)

```python
# Import Pydantic for validating tool input dictionaries
from pydantic import BaseModel, Field, ValidationError

# Import SQLAlchemy engine and SELECT helper for queries
from sqlalchemy import create_engine, select

# Import ORM base class, column mapping, and session factory pieces
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, sessionmaker

# Import Optional so in_stock can be omitted with a default
from typing import Optional


# Create the declarative base — parent for all ORM table classes
Base = declarative_base()


# ORM class that maps to the products table in SQLite
class Product(Base):
    # Explicit table name in the database
    __tablename__ = "products"

    # Primary key column with auto-increment
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    # Product display name stored as text
    name: Mapped[str] = mapped_column()

    # Category such as mobile, laptop, etc.
    category: Mapped[str] = mapped_column()

    # Price stored as integer rupees for simple filtering
    price: Mapped[int] = mapped_column()

    # Whether the item is currently in stock
    in_stock: Mapped[bool] = mapped_column()


# SQLite file created in the project folder; echo=False keeps SQL logs quiet
engine = create_engine("sqlite:///e-commerce.db", echo=False)

# Create all tables for classes that inherit from Base (here, products)
Base.metadata.create_all(engine)

# Session factory bound to our engine — each session is one conversation with the DB
SessionLocal = sessionmaker(bind=engine)


# Sample seed rows matching the six-product demo discussed in class
SAMPLE_PRODUCTS = [
    {"name": "iPhone 15", "category": "mobile", "price": 79900, "in_stock": True},
    {"name": "Samsung Galaxy S24", "category": "mobile", "price": 74999, "in_stock": True},
    {"name": "OnePlus 12R", "category": "mobile", "price": 42999, "in_stock": True},
    {"name": "Google Pixel 8", "category": "mobile", "price": 54999, "in_stock": False},
    {"name": "Redmi Note 13", "category": "mobile", "price": 18999, "in_stock": True},
    {"name": "Motorola Edge 40", "category": "mobile", "price": 29999, "in_stock": True},
]


# Pydantic model describing valid search arguments for the search_product tool
class ProductSearchInput(BaseModel):
    # Category is required and cannot be an empty string
    category: str = Field(..., min_length=1)

    # Maximum price filter; must be a positive integer
    max_price: int = Field(..., gt=0)

    # When omitted, default to showing only in-stock items
    in_stock: Optional[bool] = True


def insert_data() -> None:
    """Insert demo products if you are running the script fresh."""
    # Open a short-lived database session
    with SessionLocal() as session:
        # Build ORM Product instances from plain dictionaries
        products = [Product(**row) for row in SAMPLE_PRODUCTS]

        # Stage every row in one batch
        session.add_all(products)

        # Persist inserts to e-commerce.db
        session.commit()


def search_product(input_data: dict):
    """
    Tool function: validate dict input, query ORM, return rows or an error dict.
  """
    try:
        # Unpack the incoming dict into a validated Pydantic object
        validated_input = ProductSearchInput(**input_data)
    except ValidationError as err:
        # Return structured failure instead of raising to the agent runtime
        return {
            "success": False,
            "error": "Invalid input provided",
            "details": err.errors(),
        }

    # New session for the read query
    with SessionLocal() as session:
        # ORM SELECT with filters from validated fields — no hand-written SQL string
        query = select(Product).where(
            Product.category == validated_input.category,
            Product.price <= validated_input.max_price,
            Product.in_stock == validated_input.in_stock,
        )

        # Execute and fetch all matching Product instances
        products_from_db = session.scalars(query).all()

        # Return ORM objects; caller can read fields or shape JSON for the model
        return products_from_db


def agent_flow() -> None:
    """
    Simulated agent step: one hard-coded tool call instead of live LLM routing.
  """
    # In production this list is built from registered tools + LLM choice
    tool_calls = [
        {
            "tool_name": "search_product_tool",
            "arguments": {
                "category": "mobile",
                "max_price": 50000,
                "in_stock": True,
            },
        }
    ]

    # For each chosen tool, pull arguments and invoke the Python function
    for tool_call in tool_calls:
        arguments = tool_call["arguments"]
        tool_output = search_product(arguments)
        print(tool_output)


# Standard entry point when running: seed data, then run the simulated agent flow
if __name__ == "__main__":
    insert_data()
    agent_flow()
```

**How the code works:**
- `Product` inherits from `Base`, so `create_all` builds a **products** table from class attributes.
- `insert_data` uses `add_all` + `commit` to load six mobile SKUs (iPhone 15, S24, 12R, etc.).
- `search_product` is the **tool**: Pydantic first, then SQLAlchemy `select` + `where` on category, price cap, and stock flag.
- With `max_price=50000` and `in_stock=True`, the live run highlighted **OnePlus 12R** among in-stock mobiles under the cap.
- `agent_flow` hard-codes one tool call; a real app would fill `tool_calls` from the LLM response.
- Running `insert_data` repeatedly without clearing the table can **duplicate rows** — that is why repeated runs printed the same names many times in class.

![agent_tool_call demo — validated ProductSearchInput filters drive an ORM query against the products table in SQLite](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/session35/session35-10-agent-tool-call-demo.png)

### Reading ORM Results

Query results arrive as a **list of `Product` objects**, not pretty JSON. Printing the list may show **memory addresses**; use `product.name`, loop `for p in tool_output: print(p.name)`, or build dicts/JSON for the model. Field access follows the object reference — like opening a locker at a known address.

### Validation Demo

Passing `category: 1234` (integer instead of string) triggers Pydantic; the handler returns `success: False` with details such as “input should be a valid string” — the process stays stable for the user.

---

## End-to-End Mental Model

Trace one user question through the stack:

1. **User query** enters the agent.
2. **LLM** decides whether to answer from memory or call a tool.
3. **Tool choice + arguments** come back as structured data.
4. **Pydantic** validates arguments in Python.
5. **SQLAlchemy ORM** runs the database query (SQL generated internally).
6. **Rows** return to Python; shape them for the model if needed.
7. **LLM** turns facts into a natural-language reply.

![End-to-end agent stack — user query, LLM tool choice, Pydantic validation, SQLAlchemy query, rows back, natural-language reply](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/session35/session35-09-end-to-end-agent-stack.png)

APIs remain how external SaaS tools are reached; Python + Pydantic + SQLAlchemy is how **your** backend tool (here, product search) is implemented safely.

### Wiring OpenAI (Logic Discussed at Close)

Students were asked to integrate the client themselves using patterns from earlier classes:

- Import **OpenAI**, create a **client**, set the **API key**.
- Pass the **user query** and a **list of tools** (names + descriptions) in the prompt.
- Instruct the model: answer if possible; otherwise emit which tool to call — do not invent live facts.
- Read the model’s tool choice, call your Python function (e.g. `search_product`), return output to the model for the final answer.

**LangChain** and **LangGraph** were previewed as the focus of the **next module** — frameworks that package much of this orchestration.

---

## Key Takeaways

- Agents become useful when they **call tools**; every serious tool path ends in **API-style** request and **JSON-style** response.
- The **LLM chooses** tools and arguments; your **application validates and executes** — the model never dials Razorpay or SQLite directly.
- **Pydantic** guards tool inputs; **SQLAlchemy ORM** maps classes to tables and expresses queries without fragile raw SQL strings.
- The **agent_tool_call** demo tied validation, SQLite, and a simulated tool registry into one traceable flow.
- Next up: agent **frameworks** (LangChain / LangGraph) and fuller **LLM-driven** tool routing on top of this foundation.

---

## Important Commands, Libraries, and Terminologies

| Term / command | Meaning |
|---|---|
| **API** | Contract between systems; how agents reach external services |
| **JSON** | Text data format for API bodies and tool results |
| **Function calling** | LLM selects a tool and arguments; runtime runs the call |
| **Tool / function** | Registered capability (search, weather, DB query) |
| **Client / server** | Relative roles in request–response; initiator vs processor |
| **GET / POST / PUT / PATCH / DELETE** | HTTP verbs for read, create, update, delete |
| **2xx / 4xx / 5xx** | Success, client error, server error status families |
| **Database driver** | Connector library between app and DB engine |
| **ORM** | Maps Python classes to SQL tables |
| **SQLAlchemy** | Python DB toolkit (Core + ORM); not a database |
| **Pydantic** | Validates and structures Python data; `ValidationError` on bad input |
| **BaseModel** | Pydantic parent for input/output models |
| **declarative_base()** | SQLAlchemy ORM base for table classes |
| **create_engine()** | Opens connection to DB URL (e.g. `sqlite:///e-commerce.db`) |
| **metadata.create_all()** | Creates tables for ORM models |
| **sessionmaker / Session** | Factory and handle for DB transactions |
| **add_all / commit** | Stage many rows and save inserts |
| **select().where()** | ORM read query with filters |
| **session.scalars(query).all()** | Run query; return list of row objects |
| `python3 -m venv venv` | Create virtual environment |
| `pip3 install pydantic sqlalchemy openai` | Install demo dependencies |
| `python3 app.py` | Run seed + simulated agent flow |
