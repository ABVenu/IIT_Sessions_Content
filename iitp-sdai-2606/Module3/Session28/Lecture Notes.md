# Data Validation with Pydantic – Basics

Have you submitted a college admission form, an exam application, or a railway concession slip?  
Name, roll number, date of birth — if a box is blank, or someone writes “twelve” where a number is required, the desk sends the paper back. The inner office never even opens the file.

![College admission desk rejects a blank or wrong-type form; a complete form is accepted](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module3/session28/session28-01-admission-form-desk.png?v=20260915)

Your API is that desk. Until now the incoming letter could be a loose bundle: a missing title, a number where text was expected, a spelling like `titel`.  
Each route inventing its own red-pen `if` checks is like every clerk using a different rule — easy to forget at one counter.

This session gives the desk a **printed form**. FastAPI uses **Pydantic** so the letter is checked **before** your function runs, and the receipt you send back follows the same kind of form.

You have already built a FastAPI app with **CRUD** routes, typed **path** and **query** parameters, and tests in **Swagger** at `/docs`.  
Those URL slots can reject a bad id. The **body** of POST and PUT was still a loose bundle — that is the gap today.

Activate your project **venv** and start Uvicorn the same way as before:

```bash
python3 -m uvicorn main:app --reload --host 127.0.0.1 --port 8000   # Serve the FastAPI app on localhost port 8000
```

You will still test in **`/docs`**. The new work is the **shape** of the body, not a new tester. The sample app below is a notices board used only to practise schemas.

## What you will learn in this session

- What **Pydantic** is and why FastAPI uses it to **validate** JSON
- How to define a **schema** with a **BaseModel** class and **type hints**
- How to apply that schema as a **request body** on POST and PUT
- How **response models** keep API output consistent
- How to **read** a basic **422** validation error (`loc`, `msg`, `type`)

Path and query checks from the previous session still run first on those slots. Today’s new guard is the **JSON body**.

## Why a plain dict is not a contract

You already send JSON such as `{"title": "...", "message": "..."}`.  
A Python **dict** will accept almost any keys. That is convenient on day one and unsafe as soon as two clients must agree.

| What the client sends | What `payload.get("title")` does |
|-----------------------|----------------------------------|
| `"title"` missing | Returns `None`; you wrote a **400** by hand |
| `"title": 99` (a number) | Stores a number where you expected text |
| `"titel"` (spelling) | Treated as missing; silent mismatch |
| Extra key `"author"` | Ignored or stored with no rule |

- Need: The kitchen and the counter must share one **printed form**. Otherwise every waiter invents a different slip.
- Logic: A **schema** lists field **names** and **types**. Invalid JSON is rejected with **422** and your create/update function **does not run**.
- Common doubt: “I already check `title is None`.” That check is late, easy to forget on PUT, and does not catch **wrong types**.
- Common error: Treating Swagger’s example JSON as optional decoration. After today, that example is generated from **your class**.

Connecting idea: Path `int` already rejected `/notices/abc` with **422**. Pydantic does the same job for **keys inside the body**.

## What Pydantic is and how FastAPI uses it

- **Pydantic**  
  - *Official Definition:* A Python library that validates data against models declared with type hints, converting JSON-like input into typed objects.  
  - *In Simple Words:* A form-checker. You draw the boxes; it stamps the paper only if every box matches.  
  - *Real-Life Example:* A college admission form: name is text, roll number is a whole number, hostel stay is yes/no. A drawing in the roll-number box is rejected at the desk.
- **Schema**  
  - *Official Definition:* A declared structure — field names, types, and which fields are required — that incoming or outgoing data must match.  
  - *In Simple Words:* The blank form, not one filled copy.  
  - *Real-Life Example:* The printed mess rebate form vs one student’s filled sheet.
- **Validation**  
  - *Official Definition:* Checking that data matches the schema (required fields present, types usable) and reporting errors if not.  
  - *In Simple Words:* The clerk reading the form before it reaches the office.  
  - *Real-Life Example:* Railway ticket window: missing ID proof, no ticket printed.

FastAPI does not replace Pydantic. FastAPI **uses** Pydantic for bodies, and also for much of what you already saw: converting a path segment to `int`, filling query defaults, and drawing **Schemas** in `/docs`.

- You import `BaseModel` from `pydantic`. You do **not** need a separate `pip install` if FastAPI is already installed; installing FastAPI already brings Pydantic with it.
- Common error: `ModuleNotFoundError: pydantic` means the **venv** is not active, or you are not in the project that has FastAPI installed.
- Common doubt: “Is this only for FastAPI?” Pydantic works in any Python program. This course uses it **on API requests and responses**.

## Schema definition — BaseModel and type hints

A Pydantic model is an ordinary Python **class** that inherits from **BaseModel**.  
Each line under the class is a **field**: a name plus a type hint.

![NoticeCreate BaseModel schema with title and message as str, plus a valid JSON example](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module3/session28/session28-02-basemodel-schema.png?v=20260915)

- **BaseModel**  
  - *Official Definition:* The Pydantic parent class you subclass to declare a data model.  
  - *In Simple Words:* The stamp that turns a class into a checking form.  
  - *Real-Life Example:* The official letterhead. Without it, a Word file is just text, not a college form.
- **Field**  
  - *Official Definition:* One named slot on the model (`title: str`) with a type used for validation.  
  - *In Simple Words:* One box on the form.  
  - *Real-Life Example:* The “Name” line on an ID card application.
- **Type hint**  
  - *Official Definition:* The annotation after the colon (`str`, `int`, `bool`, `float`) that tells Pydantic what to accept.  
  - *In Simple Words:* The label printed next to the box: text, whole number, yes/no, decimal.  
  - *Real-Life Example:* “Age (years)” vs “Name (text)” on a medical slip.

Basic types you will use today:

| Type hint | JSON you send | Rejected examples |
|-----------|---------------|-------------------|
| `str` | `"Mess closed"` | Key missing; a JSON **number** such as `1` |
| `int` | `12` (no quotes) | `"two"` (letters); key missing |
| `bool` | `true` or `false` (JSON, lowercase) | `"maybe"`, or a JSON **object** `{}` |
| `float` | `8.5` | Letters such as `"eight"`; key missing |

- A field **without a default** is **required**. Omit it → **422**, `type` often `missing`.
- A field **with a default** (`overnight: bool = False`) is **optional**. Omit it → FastAPI fills the default.
- Need: Two models can share the same fields for different jobs. **NoticeCreate** is what the client may send. **NoticeOut** adds `id` that **you** assign.
- Logic: The class is the schema. One **instance** (`payload`) is one filled form. Read boxes with **dots**: `payload.title`, not `payload["title"]`.
- Common error: Using `payload["title"]` on a model. That is dict syntax. Models use **attributes**.
- Common error: Putting `id` on **NoticeCreate**. Clients must not pick the pin number. The server adds `id` when storing.
- Common doubt: “Is `class NoticeCreate` a route?” No. It is only a shape. Routes still use `@app.post`.

### Student activity: draw the form first

1. On paper, list three boxes for a hostel late-pass: `student_name`, `room_no`, `overnight`.
2. Mark each as **text**, **whole number**, or **true/false**.
3. Circle which boxes the student must fill (all three, if you give them no defaults).

You will turn this sketch into `HostelPass` in the full program below.

Connecting idea: Once the class exists, FastAPI can use it in two directions — **in** (request body) and **out** (response model).

## Request validation — the body is a model

Replace `payload: dict = Body(...)` with `payload: NoticeCreate`.  
FastAPI sees a **BaseModel** type that is **not** in the path, so it treats the parameter as a **JSON request body**.

- **Request body validation**  
  - *Official Definition:* Parsing the HTTP body as JSON and validating it against a Pydantic model before the path operation function runs.  
  - *In Simple Words:* The letter is opened and checked at the gate, not at your desk.  
  - *Real-Life Example:* Security at a campus event: incomplete gate pass, you never enter the hall.

![JSON body hits a Pydantic gate: valid data runs create_notice; missing title returns 422 and the function does not run](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module3/session28/session28-03-request-validation-gate.png?v=20260915)

- Need: Your `create_notice` function should only see a **valid** title and message. Empty-board id logic should not run for a broken letter.
- Logic: If validation fails, FastAPI returns **422 Unprocessable Entity** automatically. You do not `return JSONResponse(400, ...)` for missing `title` anymore.
- Common error: Leaving `Body(...)` **and** a BaseModel on the same payload. Use the model only.
- Common error: Sending a browser form or plain text. The model expects **JSON** (`Content-Type: application/json`). Swagger already does this.
- Common doubt: “Will `print(payload)` run on a bad body?” No. The function is skipped. That is how you know the gate worked.

**Required vs extra keys on input**

| JSON body | Result |
|-----------|--------|
| `{"title": "Wifi", "message": "Lab 2 down"}` | Function runs |
| `{"message": "Lab 2 down"}` | **422** — `title` missing |
| `{"title": "Wifi", "message": "Lab 2 down", "author": "Asha"}` | Function runs; extra key **ignored** by default |
| `{"title": 1, "message": "x"}` | **422** — `title` is not usable as `str` in the usual JSON case of a **number** |

- Extra keys are not stored unless you copy them yourself. Do not rely on `author` arriving in `payload`.
- An **empty string** `""` is still a `str`. Pydantic’s **basic** type check is not a “non-empty text” check. Length rules are an upcoming skill.
- JSON **boolean** is `true` / `false`. Python `True` belongs in `.py` files, not in the Swagger JSON editor.
- Common doubt: `"overnight": "yes"` may **pass** (Pydantic can treat some English words as true/false). Do not use `"yes"` to practise **422**. Use `"maybe"` or omit the key.

Swagger: open **POST /notices** after the new code. The request editor shows **title** and **message** because of **NoticeCreate**, not because you typed an example by hand.

### Student activity: predict before you click

1. POST body `{}` — **201** or **422**? Does `create_notice` run?
2. POST body `{"title": "Wifi"}` only — which field’s `loc` will mention `message`?
3. PUT `/notices/1` with a valid body but empty board — **422** (schema) or **404** (row missing)?

Connecting idea: **422** from a body schema is the same **status family** you saw for a bad path `int`. The **`loc`** list tells you **where** (body vs path vs query).

## Reading basic validation error responses

A failed body looks like this shape (field names inside `detail` may vary slightly by Pydantic version; the **reading method** stays the same):

```json
{
  "detail": [
    {
      "type": "missing",
      "loc": ["body", "title"],
      "msg": "Field required",
      "input": {"message": "Lab 2 down"}
    }
  ]
}
```

- **`detail`**  
  - *Official Definition:* FastAPI’s list of validation error objects for a **422** response.  
  - *In Simple Words:* The red-pen notes on the form, one note per problem.  
  - *Real-Life Example:* A teacher’s checklist: “Q2 blank, Q5 not a number.”
- **`loc`** (location)  
  - *Official Definition:* A list that names where the value sat: `"body"` then the field, or `"path"` then the parameter name.  
  - *In Simple Words:* Which box failed.  
  - *Real-Life Example:* “Page 2, Date of birth.”
- **`msg`**  
  - *Official Definition:* A short human-readable reason for that one error object.  
  - *In Simple Words:* What to fix in that box.  
  - *Real-Life Example:* “Date of birth is required” on a form, not a Python traceback.
- **`type`**  
  - *Official Definition:* A machine code for the kind of failure (`missing`, `int_parsing`, `bool_parsing`, `string_type`).  
  - *In Simple Words:* The category of the red pen, useful when two messages look alike.  
  - *Real-Life Example:* The same rubber stamp “missing” on every blank box, whatever the subject.

How to read one error:

1. Confirm HTTP status is **422**.
2. Open `detail[0]` (and later items if the list is longer).
3. Read **`loc`**: `body` + `title` means the JSON object’s `title` key.
4. Read **`msg`** and fix the JSON, not the Python `for` loop.

Compare with a **path** failure you already know:

| Request | Typical `loc` | Function runs? |
|---------|---------------|----------------|
| `GET /notices/abc` | `path`, `notice_id` | No |
| `POST /notices` with `{}` | `body`, `title` (and `message`) | No |
| `GET /notices/99` on empty board | (your 404 body, **not** this list) | Yes — then you return **404** |

- Need: Students often “debug” `create_notice` when the function never started. Always read **`loc` first**.
- Logic: Several missing fields → several objects inside `detail`. Fix all of them.
- Common error: Mixing **404** `{"detail": "Notice not found"}` (a **string**) with **422** `detail` (a **list**). Same key name, different shapes.
- Common doubt: “Is 422 a bug in Uvicorn?” No. It is a **successful rejection** of a bad letter.

### Student activity: decode one receipt

1. In `/docs`, POST `/notices` with `{"title": "Wifi"}` only.
2. Write the status code.
3. Copy `loc` and `msg` for each item in `detail`.
4. Add `message` and Execute again. Confirm **201** and an `id`.

## Response models — consistent API output

Validation is not only for **incoming** JSON.  
A **response model** tells FastAPI what the **outgoing** JSON must look like.

- **Response model**  
  - *Official Definition:* A Pydantic model passed as `response_model=...` on a decorator; FastAPI validates (and filters) the return value into that shape.  
  - *In Simple Words:* The printed receipt format. Extra scribbles on the kitchen copy are not shown to the student.  
  - *Real-Life Example:* A fee receipt shows roll number and amount, not the cashier’s private notes.

![NoticeCreate is the incoming schema; NoticeOut is the outgoing schema with id; extra keys such as author are dropped](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module3/session28/session28-04-request-vs-response-model.png?v=20260915)

- Need: GET-one, POST, and PUT should all return the **same keys** for one notice: `id`, `title`, `message`. Clients should not guess.
- Logic: You may `return` a **dict**. FastAPI builds **NoticeOut** from it. Keys that are **not** on **NoticeOut** are **dropped**.
- Common error: Returning a 404 **dict** from a function that has `response_model=NoticeOut` **without** `JSONResponse`. FastAPI then tries to fit `detail` into `id`/`title`/`message` and you get a **server error**. Keep not-found as **`JSONResponse`**.
- Common error: Putting `response_model=NoticeCreate` on POST. That schema has **no `id`**. Use **NoticeOut** for output.
- Common doubt: “Does `response_model` change my `notices` list?” No. It only changes what is **sent on the wire**.

```python
@app.post("/notices", response_model=NoticeOut, status_code=201)  # Shape + Created stamp
```

- `status_code=201` on the decorator replaces `JSONResponse(status_code=201, ...)` when the body is already a valid **NoticeOut**.
- GET list can stay a **dict** (`{"notices": ..., "limit": ...}`) **without** a response model today. You are practising **one-notice** output first.
- DELETE can return a small dict with `"message"` and `"notice"`; it does not need **NoticeOut**.

Connecting idea: Request model = what the client **may send**. Response model = what every client **will see**. Two classes, one resource.

### Student activity: extra key on the way out

1. After you run the full code, POST a valid notice and read the JSON keys.
2. Confirm you see `id`, `title`, `message` only.
3. Confirm you do **not** see an `author` key even if you added one on the way in.

## Build the schemas into a FastAPI app

Use this complete program as `main.py` (a sample notices board).  
Every line is commented. Path params, a small optional `limit` query, and `/docs` stay. POST/PUT bodies are **models**.

```python
from fastapi import FastAPI  # Application class Uvicorn will serve
from fastapi.responses import JSONResponse  # 404 bodies that must skip NoticeOut
from pydantic import BaseModel  # Parent class for every schema
from dotenv import load_dotenv  # Load APP_NAME from .env
import os  # os.getenv for the welcome route

load_dotenv()  # Read environment variables first

app = FastAPI(  # Application object; metadata appears in /docs
    title="Campus API",  # Title at the top of Swagger UI
    description="Notices board with Pydantic request and response schemas",  # Subtitle in /docs
    version="0.3.0",  # Version label in the generated OpenAPI file
)  # End of FastAPI() arguments

notices = []  # In-memory list; empty after restart


class NoticeCreate(BaseModel):  # JSON the client sends on POST and PUT
    title: str  # Required text; omit this key → 422
    message: str  # Required text; omit this key → 422


class NoticeOut(BaseModel):  # JSON the client receives for one notice
    id: int  # Server-assigned pin number
    title: str  # Copy of the stored title
    message: str  # Copy of the stored message


class HostelPass(BaseModel):  # Second schema: str, int, and bool together
    student_name: str  # Required text
    room_no: int  # Required whole number
    overnight: bool  # Required JSON true or false


@app.get("/")  # GET / welcome
def home():  # Welcome handler
    app_name = os.getenv("APP_NAME", "campus-api")  # Name from .env
    return {"message": "Hello from the backend", "app": app_name}  # JSON 200


@app.get("/health")  # GET /health
def health():  # Liveness
    return {"status": "ok"}  # JSON 200


@app.get("/notices")  # GET list; dict wrapper, no response_model today
def list_notices(limit: int = 10):  # Optional query; default ten
    return {"notices": notices[:limit], "limit": limit}  # Slice and echo limit


@app.get("/notices/{notice_id}", response_model=NoticeOut)  # GET one; output shape NoticeOut
def get_notice(notice_id: int):  # Path param still typed as int
    for item in notices:  # Search by id
        if item["id"] == notice_id:  # Integer compare
            return item  # dict filtered/checked as NoticeOut
    return JSONResponse(status_code=404, content={"detail": "Notice not found"})  # Valid int, missing row


@app.post("/notices", response_model=NoticeOut, status_code=201)  # Create; 201 + NoticeOut
def create_notice(payload: NoticeCreate):  # Body validated before this line runs
    ids = []  # Collect existing ids
    for item in notices:  # Walk the board
        ids.append(item["id"])  # Integer ids only
    new_id = 1  # First pin when empty
    if len(ids) > 0:  # Board already has rows
        new_id = max(ids) + 1  # Next integer
    notice = {  # Store as a plain dict in memory
        "id": new_id,  # Server-owned field
        "title": payload.title,  # Dot access to the model
        "message": payload.message,  # Dot access to the model
    }  # End of new row
    notices.append(notice)  # Save in the list
    return notice  # response_model builds the public JSON


@app.put("/notices/{notice_id}", response_model=NoticeOut)  # Replace title and message
def update_notice(notice_id: int, payload: NoticeCreate):  # Path id + body schema
    for item in notices:  # Search
        if item["id"] == notice_id:  # Match
            item["title"] = payload.title  # Replace title
            item["message"] = payload.message  # Replace message
            return item  # 200 NoticeOut
    return JSONResponse(status_code=404, content={"detail": "Notice not found"})  # Missing row


@app.delete("/notices/{notice_id}")  # DELETE — path only, no body schema
def delete_notice(notice_id: int):  # Typed path
    index = -1  # Not found yet
    i = 0  # Index while walking
    for item in notices:  # Search
        if item["id"] == notice_id:  # Match
            index = i  # Remember position
            break  # Stop the loop
        i = i + 1  # Next index
    if index == -1:  # Missing
        return JSONResponse(status_code=404, content={"detail": "Notice not found"})  # 404
    removed = notices.pop(index)  # Remove the row
    return {"message": "deleted", "notice": removed}  # 200 confirmation dict


@app.post("/hostel-pass", response_model=HostelPass)  # Practice int and bool in one body
def issue_pass(payload: HostelPass):  # Gate runs before this function
    return payload  # Echo the same fields as JSON
```

**How the code works:**

- `NoticeCreate` is the **request** schema. FastAPI fills `payload` only after JSON matches `title: str` and `message: str`.
- `payload.title` is attribute access. The old `payload.get("title")` and empty-string **400** block are gone for these two fields.
- `NoticeOut` is the **response** schema on GET-one, POST, and PUT. Returning the stored **dict** is enough; FastAPI shapes the wire JSON.
- `JSONResponse` for **404** skips `response_model`, so the error stays `{"detail": "..."}` as a string.
- `status_code=201` on POST is the Created stamp without wrapping the success body yourself.
- `HostelPass` is a second, smaller form so you can practise **`int`** and **`bool`** without mixing them into notices. It has **no defaults**, so all three keys are required.
- `list_notices(limit: int = 10)` is still a **query** parameter: the name is not in the path. Body schemas did not replace query skills.
- `GET /notices/{notice_id}` still **422**s on `abc` (path) and **404**s on a missing integer id (your code).
- DELETE has **no** BaseModel parameter, so Swagger will not show a notice body for delete.

### Student activity: two schemas, one resource

1. In `main.py`, count how many fields **NoticeCreate** has, then **NoticeOut**.
2. Write one sentence: which class is missing `id`, and why the client must not send it.
3. Find the one route that uses **HostelPass**.

## Hands-on — request, response, and errors in Swagger

Keep Uvicorn running. Open `http://127.0.0.1:8000/docs`.  
Confirm the title **Campus API** and version **0.3.0**. Scroll to **Schemas** at the bottom and find **NoticeCreate**, **NoticeOut**, and **HostelPass**.

**Valid create**

1. Expand **POST /notices** → **Try it out**.
2. Keep JSON with both `"title"` and `"message"` (double quotes).
3. **Execute**. Expect **201** and an integer `id`.
4. Expand **GET /notices/{notice_id}**, type that id, Execute. Expect **200** and the same three keys.

**Missing field — read `loc`**

1. POST again with `{"title": "Wifi"}` only.
2. Expect **422**. Note `loc` includes `"body"` and `"message"`.
3. Confirm the board did not gain a broken row: GET `/notices` still shows only the valid notice.

**Wrong type on the hostel pass**

1. Expand **POST /hostel-pass**.
2. Send `{"student_name": "Asha", "room_no": "two", "overnight": true}`.
3. Expect **422**. Read `loc` for `room_no`.
4. Send `{"student_name": "Asha", "room_no": 12, "overnight": "maybe"}`. Expect **422** on `overnight`.
5. Send `{"student_name": "Asha", "room_no": 12, "overnight": true}`. Expect **200** and the same three fields back.

**Extra key on the way in**

1. POST `/notices` with `"author": "Asha"` added beside title and message.
2. Expect **201**. The response should **not** list `author`.
3. GET the notice by id. Still no `author`.

**Empty string is still a string**

1. POST `{"title": "", "message": ""}`.
2. Expect **201** (basic types only). Write this down so you do not confuse it with “required key missing.”
3. Required means **the key is present and the type matches**, not “the text looks useful.”

**PUT and 404 vs 422**

1. PUT `/notices/{notice_id}` with a valid body and id `1` (if that row exists). Expect **200** and updated text.
2. PUT with id `99`. Expect **404** and your string `detail`.
3. PUT with id `abc`. Expect **422** with `loc` on **path**, not body.
4. PUT with a valid integer id and body `{}`. Expect **422** with `loc` on **body**.

**List query still works**

1. POST a second notice.
2. GET `/notices` with `limit` `1`. Expect one object inside `notices`.
3. This is still a **query** param. It is not a Pydantic body.

### Student activity: Swagger receipt card

1. Force one **422** on POST `/notices` and write `type`, `loc`, `msg`.
2. Force one **404** on GET-one and write whether `detail` was a list or a string.
3. Force one **422** on POST `/hostel-pass` and name the field.
4. Complete one **201** POST and write the keys on **NoticeOut**.

## If something breaks — check this list

| What you see | Likely cause | What to do |
|--------------|--------------|------------|
| `/docs` will not load | Uvicorn down, or `/doc` | Start server; use `/docs` |
| POST body editor is a free dict, no title/message | Old `main.py` still using `Body(...)` | Save the new file; `--reload`; refresh `/docs` |
| `payload["title"]` **TypeError** | Dict syntax on a model | Use `payload.title` |
| POST `{}` → function logic runs | Parameter is still `dict` | Type it as `NoticeCreate` |
| 404 dict becomes a **500** | Returned `{"detail": ...}` under `response_model=NoticeOut` | Use `JSONResponse` for not-found |
| Extra `"author"` in GET response | You stored extra keys and have **no** `response_model` | Put `response_model=NoticeOut` on GET-one |
| `overnight: True` in Swagger JSON | Invalid JSON (Python spelling) | Use `true` / `false` |
| `"overnight": "yes"` still **200** | Some words are coerced to bool | Expected; use `"maybe"` to see **422** |
| Empty title accepted | `str` allows `""` | Expected today; not the same as a missing key |
| `ModuleNotFoundError: pydantic` | Wrong interpreter / venv off | Activate venv; FastAPI install includes Pydantic |
| PUT 422 when you meant 404 | Body `{}` failed schema first | Send title and message; then a missing id can 404 |
| Schemas missing in `/docs` | Class not used on any route | Wire `NoticeCreate` / `NoticeOut` on decorators |

Connecting idea: Path and query **422**s name slots in the URL. Body **422**s name keys in JSON. Response models name keys on the way **out**.

## Key Takeaways

- **Pydantic** turns a **BaseModel** class plus **type hints** into a **schema**. FastAPI uses that schema to **validate** JSON **before** your function runs.
- **NoticeCreate** is the request body for POST and PUT (`payload.title`). Missing keys and wrong types yield **422** with a `detail` **list** you read via **`loc`**, **`msg`**, and **`type`**.
- **NoticeOut** as `response_model` keeps one-notice JSON consistent (`id`, `title`, `message`) and drops extra keys. **404** must stay a **JSONResponse** so it is not forced into that shape.
- Basic types (`str`, `int`, `bool`) check **presence and type**, not “non-empty meaning.” Prefer JSON `true`/`false` for bools; some words like `"yes"` may still pass. Extra input keys are ignored by default.
- Request and response **models** remain the JSON contract. Further FastAPI features you add later still sit **around** these schemas; they do not replace `BaseModel`.

## Important Commands, Libraries, Terminologies used

| Name | Meaning in this session |
|------|-------------------------|
| Pydantic | Library that validates data against typed models |
| `BaseModel` | Parent class for a schema |
| Schema | Declared field names and types |
| Field | One slot such as `title: str` |
| Type hint | `str`, `int`, `bool`, `float` on a field |
| `NoticeCreate` | Request body for POST/PUT notices |
| `NoticeOut` | Response shape for one notice |
| `HostelPass` | Practice schema with `int` and `bool` |
| Request validation | JSON body checked before the function |
| `payload: NoticeCreate` | FastAPI treats this as the JSON body |
| `payload.title` | Attribute access on a model |
| `response_model=` | Outgoing JSON must match this class |
| `status_code=201` | Created stamp on the POST decorator |
| 422 Unprocessable Entity | Schema or type failure; function skipped |
| `detail` (422) | **List** of error objects |
| `loc` | Where it failed: `body` / `path` / `query` then the name |
| `msg` | Human reason |
| `type` | Machine error kind (`missing`, and similar) |
| Extra keys | Ignored on input by default; dropped on output by `response_model` |
| Empty string `""` | Valid `str`; not the same as a missing key |
| `JSONResponse` 404 | Error body that skips `NoticeOut` |
| `/docs` Schemas | Generated from your classes |
| `{notice_id}` | Path param; still 422 vs 404 as before |
| `python3 -m uvicorn main:app --reload` | Dev server, same as before |
| `Body(...)` | Previous dict body; replaced by a model today |
