# FastAPI Deep Dive – Request/Response & Full CRUD

In the previous session you set up a **backend** project: **venv**, **pip**, **`.env`**, **FastAPI**, and **Uvicorn**.  
You answered **GET** on `/` and `/health` and tested those URLs in the **browser**.  
You were the kitchen for **read-only** orders.

A browser address bar can only send **GET**. Real apps also **create**, **change**, and **remove** records.  
That needs **JSON bodies**, the other **HTTP methods** you already named in Module 2, and a tool that can send them.  
This session grows the same `campus-api` app into **CRUD** and tests every route in **Postman**.

## What you will learn in this session

- How FastAPI turns an incoming **request** into your function, and how it builds an outgoing **response**
- How **CRUD** maps to **GET**, **POST**, **PUT**, and **DELETE**
- How to accept a **JSON request body** and return structured JSON
- How to test all four methods in **Postman** (the browser cannot do this job alone)

Keep **venv activated** and start Uvicorn the same way as before:

```bash
python3 -m uvicorn main:app --reload --host 127.0.0.1 --port 8000   # Serve campus-api on localhost port 8000
```

Fixed paths plus a small **id slot** on PUT and DELETE are enough for CRUD today. Extra URL patterns, query strings, and the interactive docs page are upcoming skills.

## Why GET in the browser is not enough

You already know the four common methods from the **client–server** lesson.

| Method | CRUD job | Typical body | Can the address bar send it? |
|--------|----------|--------------|------------------------------|
| **GET** | Read | Usually none | Yes — you type the URL |
| **POST** | Create | JSON with the new record | No |
| **PUT** | Update (replace fields) | JSON with the new title and message | No |
| **DELETE** | Remove | Usually none | No |

![Campus office with four counters — GET /notices to read, POST /notices to create with a JSON slip, PUT /notices/1 to update, DELETE /notices/2 to remove — same door, different verbs](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module3/session26/session26-03-four-method-counters.png?v=20260902)

- **CRUD**  
  - *Official Definition:* Create, Read, Update, Delete — the four basic operations on a collection of records.  
  - *In Simple Words:* Add a row, look at rows, edit a row, throw a row away.  
  - *Real-Life Example:* A hostel **notice board**: pin a new notice, read the board, replace a wrong date, take a notice down.

![Hostel notice board showing Create pin, Read the board, Update rewrite a date, and Delete take a paper down — CRUD as four jobs on one board](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module3/session26/session26-01-notice-board-crud.png?v=20260902)

- Need: `GET /health` proved the doorbell works. A product still needs **write** operations. Marks, orders, and notices change.
- Logic: The **method** is the verb; the **path** is which counter; the **body** is the slip of paper for create/update.
- Common doubt: “Can I test POST by pasting JSON in the address bar?” No. The address bar does not attach a JSON body or change the method.
- Common error: Using GET for create because it is easy to click. GET must stay **safe to repeat**. Creating twice by refreshing would duplicate notices.

Connecting idea: FastAPI already received a GET and packed JSON for you. Now you look at that incoming and outgoing mail as **objects**, then attach POST, PUT, and DELETE.

## How FastAPI handles requests and responses

Every call is still one **request–response cycle**. FastAPI’s job is to parse the request, run your function, and serialise the response.

- **Request**  
  - *Official Definition:* The incoming HTTP message FastAPI exposes as a `Request` object — method, URL, headers, and (when present) body.  
  - *In Simple Words:* The order slip that arrived at the counter.  
  - *Real-Life Example:* “POST /notices, here is a JSON slip with title and message.”
- **Response**  
  - *Official Definition:* The outgoing HTTP message — **status code**, headers, and body — that FastAPI sends back to the client.  
  - *In Simple Words:* The stamped plate that leaves the kitchen.  
  - *Real-Life Example:* Status **201** plus `{"id": 1, "title": "Mess timing"}` after a successful create.
- **`Request` object**  
  - *Official Definition:* A Starlette/FastAPI class your function can accept as a parameter named `request` to read `method`, `url`, and `headers`.  
  - *In Simple Words:* A Python object that answers “what verb, what path, what labels came in?”  
  - *Real-Life Example:* Reading the top of a courier pouch before you open the parcel (the JSON body).
- **`JSONResponse`**  
  - *Official Definition:* A response class that sets a status code and a JSON body when a plain `return dict` is not enough (for example **201** or **404**).  
  - *In Simple Words:* You choose the stamp, not only the food.  
  - *Real-Life Example:* “Notice not found” should not look like success **200**.
- Need: Returning a dict is fine for **200**. Create should often be **201**. Missing ids should be **404**. Wrong JSON should be **400**.
- Logic: FastAPI matches **method + path** to a decorator (`@app.post`, `@app.put`, …), then injects parameters (request object, JSON body, path id).
- Common doubt: “Is the Request the JSON?” No. The Request is the **envelope**. The JSON body is the **letter** inside, for POST and PUT.

![Courier envelope labelled Request with POST and path /notices, opened to a JSON letter with title and message — envelope is the Request object, letter is the body](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module3/session26/session26-02-request-envelope-letter.png?v=20260902)

- Common error: Ignoring status codes and only reading the JSON. Postman shows both. A **404** body can still look like a sentence.

You already used **200** on GET. Add these stamps for CRUD:

| Status | Meaning in this session |
|--------|-------------------------|
| **200** | Read, update, or delete succeeded |
| **201** | Create succeeded — a new notice exists |
| **400** | JSON missing `title` or `message` |
| **404** | That `id` is not on the board |

### One POST from Postman to your function

Walk this once. The other methods reuse the same envelope story.

1. Postman sets method **POST** and URL `http://127.0.0.1:8000/notices`.
2. The raw JSON body travels as bytes with `Content-Type: application/json`.
3. **Uvicorn** accepts the connection and hands the HTTP message to **FastAPI**.
4. FastAPI sees `@app.post("/notices")`, not GET `/notices`. Method and path both must match.
5. It builds a **Request** object and parses the JSON into `payload`.
6. Your function either stores a dict and returns **201**, or returns **400** if keys are missing.
7. Postman shows the status stamp and the JSON body.

- Need: If step 4 misses, you used the wrong method or a typo in `/notices`.
- Logic: GET `/notices` and POST `/notices` share a path but are **different endpoints**. FastAPI stores them separately.
- Common error: Sending POST, then reading only the body and ignoring **201** vs **400**. Always read the stamp first.

![POST round trip — Postman Send to http://127.0.0.1:8000/notices, Uvicorn door on port 8000, FastAPI @app.post /notices, JSON with id 1 and stamp 201 Created](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module3/session26/session26-04-post-round-trip.png?v=20260902)

### Student activity: name the envelope

1. Write one line for a successful create: **method**, **path**, **status**.
2. Write one line for updating notice `2`: **method**, **path**.
3. Check that create is **POST** `/notices` and update is **PUT** with an id in the path.

## JSON request bodies

POST and PUT carry data. That data is a JSON object — the same format you parsed with `fetch` as a client.

- **Request body**  
  - *Official Definition:* The optional payload of an HTTP request; for JSON APIs it is a UTF-8 object or array with `Content-Type: application/json`.  
  - *In Simple Words:* The filled form stapled behind the verb.  
  - *Real-Life Example:* `{"title": "Wi-Fi", "message": "Lab down 5–6 p.m."}` is the new notice text.
- **`Body(...)`**  
  - *Official Definition:* A FastAPI parameter default that tells the framework to read the JSON body into a Python **dict**. The `...` (Ellipsis) means the body is **required**.  
  - *In Simple Words:* “Do not run this function until JSON arrives.”  
  - *Real-Life Example:* The clerk will not pin a blank slip. No JSON, no create.
- Need: A function cannot guess the title. The client must send it.
- Logic: `payload.get("title")` reads one key. Missing keys return `None`. You then send **400**.
- Common error: Sending JSON with single quotes (`{'title': 'Hi'}`). JSON requires **double quotes**.
- Common error: Choosing form-data in Postman instead of **raw JSON**. FastAPI will not see your keys.
- Common doubt: “Why not a Python class for the body?” You will add stricter schemas in an upcoming session. Today a **dict** is enough to learn the cycle.

Example body for **POST /notices**:

```json
{
  "title": "Mess timing",
  "message": "Dinner from 8 p.m. this week"
}
```

Example body for **PUT /notices/1** (path holds the id; body holds the new text):

```json
{
  "title": "Mess timing",
  "message": "Dinner from 7.30 p.m. this week"
}
```

**What success JSON looks like** after POST (ids may differ):

```json
{
  "id": 1,
  "title": "Mess timing",
  "message": "Dinner from 8 p.m. this week"
}
```

**What a 400 body looks like:**

```json
{
  "detail": "title and message are required"
}
```

**What a 404 body looks like:**

```json
{
  "detail": "Notice not found"
}
```

Connecting idea: The id in the PUT path is only a **slot** so DELETE can stay without a body (as you learned for HTTP). You will practise more URL slots and filters later.

## POST versus PUT — do not mix the verbs

Both send JSON. They are not interchangeable.

- **POST /notices** always **adds** a new dict and a new `id`. Two identical POSTs create two notices.
- **PUT /notices/1** **edits** the notice whose id is already `1`. If that id is missing, you get **404**, not a new row.
- **GET /notices** never uses a body. Repeating GET must not create rows.
- Need: If you “fix a typo” with POST, you leave the old wrong notice on the board.
- Logic: Create = new pin. Update = rewrite the paper on an existing pin. Delete = remove the pin.
- Common error: PUT without the id in the URL (`PUT /notices`). That path is not registered for PUT. FastAPI returns **405 Method Not Allowed**. Use `PUT /notices/1`.

### Student activity: pick the verb

1. “Add a fresh Wi-Fi notice.” Which method and path?
2. “Correct the time on notice 1.” Which method and path?
3. If you use POST for question 2, how many Wi-Fi notices will GET show after two mistakes?

## In-memory notices — no database yet

The board lives in a Python **list** of dictionaries while Uvicorn runs.

- **In-memory store**  
  - *Official Definition:* Application data kept in process memory (a list/dict) rather than in a database file.  
  - *In Simple Words:* Sticky notes on the kitchen wall — gone if you close the kitchen.  
  - *Real-Life Example:* Restart Uvicorn and the notices list starts empty again. That is expected today.
- Need: You can practise full CRUD without installing a database.
- Logic: `notices.append` is Create. A `for` loop finds an `id` for Update and Delete. Returning the list is Read.
- Common doubt: “Is this production?” No. Upcoming sessions persist data. Today the list is a teaching register.

## Build full CRUD on FastAPI

Replace `main.py` with the complete program below.  
Every line is commented. Keep `.env` with `APP_NAME` as before.

```python
from fastapi import FastAPI, Request, Body  # App, incoming request object, JSON body helper
from fastapi.responses import JSONResponse  # Lets you choose status codes such as 201 and 404
from dotenv import load_dotenv  # Loads .env into the process
import os  # Reads APP_NAME with os.getenv

load_dotenv()  # Read APP_NAME from .env before routes run

app = FastAPI()  # Application object Uvicorn serves as main:app

notices = []  # In-memory list of notice dictionaries; empty when the server starts


@app.get("/")  # GET / — welcome, unchanged idea from the previous session
def home():  # Handler for the welcome counter
    app_name = os.getenv("APP_NAME", "campus-api")  # Shop name from .env, with a default
    return {"message": "Hello from the backend", "app": app_name}  # Dict becomes JSON with status 200


@app.get("/health")  # GET /health — liveness check
def health():  # Handler for the health counter
    return {"status": "ok"}  # Simple JSON so Postman can ping the server


@app.get("/debug-request")  # GET /debug-request — show the Request envelope
def debug_request(request: Request):  # FastAPI injects the Request object
    return {  # Build a small JSON map of envelope fields
        "method": request.method,  # HTTP verb, for example GET
        "path": request.url.path,  # Path only, for example /debug-request
        "content_type": request.headers.get("content-type"),  # Header value, or None
    }  # Default status 200


@app.get("/notices")  # GET /notices — Read all notices
def list_notices():  # Handler that returns the whole board
    return {"notices": notices}  # Wrap the list so the JSON has a clear key


@app.post("/notices")  # POST /notices — Create one notice
def create_notice(request: Request, payload: dict = Body(...)):  # Envelope plus required JSON dict
    title = payload.get("title")  # Read title; missing key gives None
    message = payload.get("message")  # Read message; missing key gives None
    if title is None or message is None or title == "" or message == "":  # Both fields must be non-empty
        return JSONResponse(  # Stop and tell the client the slip is incomplete
            status_code=400,  # Bad Request
            content={"detail": "title and message are required"},  # JSON error body
        )  # No notice is stored
    ids = []  # Collect existing ids so the new id is unique
    for item in notices:  # Walk the current list
        ids.append(item["id"])  # Each notice dict has an integer id
    new_id = 1  # First notice on an empty board
    if len(ids) > 0:  # If the board already has rows
        new_id = max(ids) + 1  # Next integer after the largest id
    notice = {"id": new_id, "title": title, "message": message}  # New record
    notices.append(notice)  # Create: add to the in-memory list
    return JSONResponse(status_code=201, content=notice)  # Created, return the stored dict


@app.put("/notices/{notice_id}")  # PUT — Update; {notice_id} is the slot in the path
def update_notice(notice_id: int, payload: dict = Body(...)):  # Path id plus required JSON dict
    title = payload.get("title")  # New title
    message = payload.get("message")  # New message
    if title is None or message is None or title == "" or message == "":  # Same completeness rule as create
        return JSONResponse(  # Reject incomplete update slips
            status_code=400,  # Bad Request
            content={"detail": "title and message are required"},  # JSON error body
        )  # List unchanged
    for item in notices:  # Search the board
        if item["id"] == notice_id:  # Match the path id to a stored id
            item["title"] = title  # Replace title in place
            item["message"] = message  # Replace message in place
            return item  # 200 and the updated dict
    return JSONResponse(  # Loop finished with no match
        status_code=404,  # Not Found
        content={"detail": "Notice not found"},  # JSON error body
    )  # List unchanged


@app.delete("/notices/{notice_id}")  # DELETE — Remove; no JSON body
def delete_notice(notice_id: int):  # Only the path id is required
    index = -1  # -1 means not found yet
    i = 0  # Manual index for pop
    for item in notices:  # Search the board
        if item["id"] == notice_id:  # Same integer comparison as PUT
            index = i  # Remember where to pop
            break  # Stop at the first match
        i = i + 1  # Move to the next position
    if index == -1:  # Never found that id
        return JSONResponse(  # Tell the client the pin is missing
            status_code=404,  # Not Found
            content={"detail": "Notice not found"},  # JSON error body
        )  # List unchanged
    removed = notices.pop(index)  # Remove that dict from the list
    return {"message": "deleted", "notice": removed}  # 200 and a copy of what was removed
```

**How the code works:**

- `notices` is shared by all routes in this process. Two POST calls add two dicts. Restart Uvicorn and the list is empty.
- `debug_request` shows the **Request** envelope. Call it with GET in Postman and read `method` and `path`.
- `create_notice` uses both `Request` (you can log `request.method`) and `payload` (the letter).
- `Body(...)` means Postman must send **Body → raw → JSON**. An empty body fails before your `if`.
- `JSONResponse` is how you pick **201**, **400**, and **404**. A plain `return dict` is **200**.
- `{notice_id}` is a path **slot**. FastAPI turns that text into the `int` argument. You will go deeper on slots and query strings in an upcoming session.
- PUT **replaces** title and message on the matched dict. DELETE **pops** it. GET **reads** the whole list.
- Ids are integers. In JSON, send `1` not `"1"` in the path (the path is not quoted).
- `request.headers.get("content-type")` on GET `/debug-request` is often `None` because GET has no body. On POST, Postman usually sends `application/json`.

**CRUD map for this file:**

| Job | Method and path | Body | Success status |
|-----|-----------------|------|----------------|
| Read all | `GET /notices` | none | 200 |
| Create | `POST /notices` | `title`, `message` | 201 |
| Update | `PUT /notices/{notice_id}` | `title`, `message` | 200 |
| Delete | `DELETE /notices/{notice_id}` | none | 200 |

### Student activity: predict before you send

1. Board is empty. What does `GET /notices` return for the `notices` key?
2. You POST one notice, then PUT `/notices/9`. Which status do you expect?
3. You DELETE `/notices/1` twice. Which status is the second call?

## Introduction to Postman

- **Postman**  
  - *Official Definition:* An API client application that sends HTTP requests with a chosen method, URL, headers, and body, then shows the status and response body.  
  - *In Simple Words:* A remote control for your kitchen — any verb, not only GET.  
  - *Real-Life Example:* The browser is a customer walking in and asking “what is on the board?” Postman can also hand in a new slip, replace a slip, or take one down.
- Need: You must see **201** and **404**, not only pretty JSON in a tab.
- Logic: Method dropdown + URL + optional Body + **Send**. The lower panel is the **response**.
- Common error: URL `http://127.0.0.1:8000/notices` while Uvicorn is stopped. Connection errors are the doorbell, not FastAPI logic.
- Common error: POST to `/notice` (singular) while the decorator says `/notices`. Paths must match exactly.
- Prefer the **Postman desktop app** for localhost. The cloud editor is not required today.

**Install and open (once):**

1. Download Postman from [https://www.postman.com/downloads/](https://www.postman.com/downloads/) and install it like any desktop app.
2. Skip extra account features if they appear. A local request does not need a team workspace.
3. Click **New** → **HTTP Request** (wording may be **Blank request**).

**Postman window — what to touch:**

| Control | What you set |
|---------|----------------|
| Method dropdown | GET, POST, PUT, or DELETE |
| URL box | Full URL, including `http://` and `:8000` |
| **Body** tab | For POST and PUT: **raw**, then **JSON** in the format dropdown |
| **Send** | Fires the request |
| Status (right of the response) | `200 OK`, `201 Created`, `400`, `404` |
| Response body | JSON from FastAPI |

![Postman on a laptop — method POST, URL localhost port 8000 /notices, Body raw JSON with title and message, Send, response panel showing 201 Created and id 1](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module3/session26/session26-05-postman-crud-tester.png?v=20260902)

**How the client works:**

- Postman sets `Content-Type: application/json` when you pick raw JSON. You should not need to type that header by hand.
- GET and DELETE: leave Body unused (or none). PUT and POST: paste valid JSON with double quotes.
- Each **Send** is one cycle. Change method or URL, Send again.
- If the response is **422** and `detail` is a list (not your string), Postman did not send JSON FastAPI could parse. Switch to **raw** + **JSON** and check double quotes.
- Do not use the **Params** tab to add `title` as a query string. That is a different style of input you will practise later. Today `title` lives in the **Body**.

### Test every CRUD route

Keep Uvicorn running. In Postman, run this order so ids exist before PUT and DELETE.

**1. Envelope check — GET**

- Method **GET**, URL `http://127.0.0.1:8000/debug-request`
- Send. Confirm JSON `method` is `GET` and `path` is `/debug-request`.
- Optional: GET `http://127.0.0.1:8000/health` and confirm `{"status":"ok"}`.

**2. Read empty board — GET**

- Method **GET**, URL `http://127.0.0.1:8000/notices`
- Send. Expect **200** and `"notices": []`.

**3. Create — POST**

- Method **POST**, URL `http://127.0.0.1:8000/notices`
- Body → **raw** → **JSON**:

```json
{
  "title": "Wi-Fi",
  "message": "Router restart at 6 p.m."
}
```

- Send. Expect **201** and an `id` (usually `1`). Copy that id.
- Send the same POST again. Expect **201** and `id` `2`. Create is not GET — each Send adds a row.

**4. Read again — GET**

- GET `/notices` again. Expect two objects inside `notices`.

**5. Update — PUT**

- Method **PUT**, URL `http://127.0.0.1:8000/notices/1` (use your first id).
- Body → raw → JSON:

```json
{
  "title": "Wi-Fi",
  "message": "Router restart moved to 7 p.m."
}
```

- Send. Expect **200** and the new `message`.
- PUT `http://127.0.0.1:8000/notices/99` with the same JSON. Expect **404**.

**6. Delete — DELETE**

- Method **DELETE**, URL `http://127.0.0.1:8000/notices/2` (no body).
- Send. Expect **200** and a `deleted` message.
- DELETE the same URL again. Expect **404**.
- GET `/notices`. Expect only the notice you did not delete.

**7. Bad body — POST**

- POST `/notices` with `{"title": "Only title"}`.
- Expect **400** and `title and message are required`.

### Student activity: run the board yourself

1. Create two notices with different titles.
2. Update the first. Confirm GET shows the new message.
3. Delete the second. Confirm GET no longer lists it.
4. Force a **404** with PUT or DELETE on an id you never created. Write the status on paper.

## If something breaks — check this list

| What you see | Likely cause | What to do |
|--------------|--------------|------------|
| Could not send request / connection error | Uvicorn not running, or wrong port | Start the server; URL must include `:8000` |
| `404 Not Found` on POST `/notices` | Path typo, or old `main.py` still running | Save `main.py`; confirm `--reload`; path is `/notices` |
| `422 Unprocessable Entity` | No JSON body, or Body not set to raw JSON | Body → raw → JSON; include `{ ... }` |
| `400` with your `detail` string | `title` or `message` missing or empty | Add both keys with non-empty strings |
| PUT/DELETE always 404 | Id does not match a stored integer | GET `/notices` first; use that `id` in the path |
| `405 Method Not Allowed` | Right path, wrong verb (for example PUT `/notices`) | Use PUT `/notices/{id}`; POST is the create verb |
| POST always creates, never updates | You used POST for an edit | Edits are **PUT** with the id in the path |
| Empty board after you added rows | Server restarted | In-memory list reset; POST again |
| JSON parse error in Postman | Single quotes or a trailing comma | Use double quotes; last property has no comma |

Connecting idea: Postman is a **client**, just like the browser or `fetch`. FastAPI does not care which client sent the envelope — only method, path, and body.

## Key Takeaways

- FastAPI receives a **Request** (method, path, headers, optional JSON body) and returns a **Response** (status + JSON). Use `JSONResponse` when the stamp is not **200**.
- **CRUD** on this board is `GET /notices`, `POST /notices`, `PUT /notices/{notice_id}`, `DELETE /notices/{notice_id}`, with data in a Python list until the process stops.
- **POST** and **PUT** need a **JSON body** (`title`, `message`) via `Body(...)`. Incomplete slips return **400**. Unknown ids return **404**. Successful create returns **201**.
- **Postman** is how you send every method. Test in order: ping, empty GET, POST, GET, PUT, DELETE, then a 400 and a 404.
- Upcoming sessions add richer URL slots, query filters, interactive docs, and stricter body schemas. Keep this `notices` list as the same kitchen.

## Important Commands, Libraries, Terminologies used

| Name | Meaning in this session |
|------|-------------------------|
| CRUD | Create, Read, Update, Delete |
| Request | Incoming HTTP envelope (`Request` object) |
| Response | Outgoing status + body |
| `JSONResponse` | Set status (201, 400, 404) and JSON content |
| Request body | JSON object on POST/PUT |
| `Body(...)` | Required JSON dict parameter |
| `payload.get("title")` | Read a key; missing → `None` |
| `Content-Type: application/json` | Body is JSON (Postman raw JSON sets this) |
| `@app.get` / `post` / `put` / `delete` | Register one method + path |
| `{notice_id}` | Path slot for which notice to change or remove |
| In-memory list | `notices = []`; resets on restart |
| Status 200 | Success for read, update, delete |
| Status 201 | Create succeeded |
| Status 400 | Incomplete JSON |
| Status 404 | Id not on the board |
| Status 405 | Method not allowed on that path |
| Postman | Desktop API client; method + URL + Send |
| Body raw JSON | Postman mode for POST/PUT |
| `python3 -m uvicorn main:app --reload` | Dev server, same as previous session |
| `request.method` | HTTP verb on the Request object |
| `request.url.path` | Path string on the Request object |
| `notices.pop(index)` | Remove one stored dict from the list |
| 422 | FastAPI could not parse the body; fix Postman JSON |
