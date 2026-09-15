# Advanced FastAPI – Dependency Injection & Middleware

Have you been through a college office where the library, the mess rebate desk, and the hostel late-pass window all ask for the same ID?  
If every clerk writes the rule in a private notebook, one window will forget — and someone walks through without the check.

You do not want five copies of the same instruction. You want **one** checker that those counters share.

The campus gate is a different job. Everyone who enters or leaves gets a stamp, whether they are going to the library or the hostel.  
No building should invent its own gate register.

![Library, mess, and hostel share one ID checker; the campus gate stamps every visit](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module3/session29/session29-01-shared-checker-and-gate.png?v=20260915)

This session is those two ideas in FastAPI: **dependency injection** (one shared check on the counters you choose) and **middleware** (one stamp on every visit).

You already check the **shape** of JSON with **Pydantic**. That printed form does not replace a shared ID checker, and it does not replace the gate.  
Keep the form. Today you attach **reusable work** to routes, and a **wrapper** around every visit.

Activate your project **venv** and start Uvicorn the same way as before:

```bash
python3 -m uvicorn main:app --reload --host 127.0.0.1 --port 8000   # Serve the FastAPI app on localhost port 8000
```

You will still test in **`/docs`**. The sample below is a notices board used only to practise shared logic. Keep your Pydantic models; do not relearn them.

## What you will learn in this session

- What **dependency injection** is and why FastAPI uses it
- How to **create** a reusable dependency function
- How to **inject** it into route functions with `Depends`
- How to **apply the same dependency** on more than one endpoint
- What **middleware** is, **when** to use it, and how to stamp every response

Schemas stay on POST/PUT. Today’s new work is **who runs before the route**, and **what wraps every request**.

## Why copy-paste inside routes does not scale

You can call a helper yourself: `settings = get_settings()` at the top of each function.  
That is ordinary Python. FastAPI will not know about it, Swagger will not show extra parameters, and you must remember every route.

| Approach | Who calls the helper | Who sees it in `/docs` |
|----------|----------------------|------------------------|
| Copy the code in each route | You, by hand | Nothing extra |
| Call `get_settings()` inside the route | You, by hand | Nothing extra |
| `Depends(get_settings)` | FastAPI, before the route | Whatever that function declares (query, and so on) |

- Need: Write routes (`POST`, `PUT`, `DELETE`) should share one access check. Read routes can stay open. A wrapper that hits **all** URLs (including `/docs`) is a different job.
- Logic: **Dependencies** are opt-in per route (or per group of routes). **Middleware** is the outer belt for every HTTP call.
- Common error: Solving “every response needs a header” by adding `response.headers[...]` in each return. You will miss `/health` and `/docs`.
- Common doubt: “Is this the same as Pydantic?” No. Pydantic checks **data shape**. Dependencies and middleware run **code**.

- **Modular (in this session)**  
  - *Official Definition:* An application design where shared behaviour is defined once and attached where needed, instead of duplicated inside each handler.  
  - *In Simple Words:* One helper, many doors — not five copies of the same `if`.  
  - *Real-Life Example:* One college circular for “ID on the desk,” posted on every notice board, not rewritten by each department.

Connecting idea: Declare shared behaviour next to the decorator, the same way you already declare `response_model` — but for **functions**, not for JSON classes.

## What dependency injection is

- **Dependency injection (DI)**  
  - *Official Definition:* A pattern where the framework **creates** and **passes in** objects or values a function needs, instead of the function constructing them itself.  
  - *In Simple Words:* You list what the route needs. FastAPI fetches it and hands it over.  
  - *Real-Life Example:* The exam hall does not ask each student to bring the question paper. The invigilator **issues** the paper as you sit down.
- **Dependency**  
  - *Official Definition:* A callable (usually a function) FastAPI runs before the path operation; its return value can be injected as an argument.  
  - *In Simple Words:* A reusable helper with an official doorway into the route.  
  - *Real-Life Example:* One ID-card checker at the library gate, reused for reading room, stacks, and issue desk — not a new checker written inside each room.
- **`Depends`**  
  - *Official Definition:* FastAPI’s marker (`fastapi.Depends`) that tells the framework to run that callable and inject the result.  
  - *In Simple Words:* The tag that says “do not treat this as a normal default; **run** this function.”  
  - *Real-Life Example:* A form field labelled “Office use — do not fill.” The office fills it, not you.

Benefits in FastAPI (why this exists):

- **One change, many routes:** Edit `require_access_key` once; every decorated write route follows.
- **Swagger stays true:** If the dependency needs `access_key` as a query, `/docs` shows that box **only** on routes that inject it.
- **The route stays short:** Create-notice code talks about titles and ids, not about how keys are read from `.env`.
- **You choose the set:** Middleware cannot easily say “only POST and PUT.” Dependencies can.

- Logic: `def create_notice(..., access_key: str = Depends(require_access_key))` — FastAPI calls `require_access_key` first. If it raises, your create function **does not run**.
- Common error: Writing `access_key: str = require_access_key` (**no** `Depends`). That stores the **function object** as a default. FastAPI will not run your check.
- Common error: Calling `require_access_key()` yourself inside the route and also using `Depends`. Pick injection; let FastAPI call it.
- Common doubt: “Does DI replace `import`?” No. You still import `Depends`. Injection is about **when** the function runs, not about finding the file.

### Student activity: name the missing tag

1. On paper, write `def list_notices(settings: dict = get_settings):`.
2. Circle what is missing so FastAPI **runs** `get_settings`.
3. Write the corrected parameter in one line.

Connecting idea: A dependency is an ordinary function. The special part is how the **route** asks for it.

## Create a reusable dependency

A dependency is a Python function. FastAPI inspects its **parameters** the same way it inspects a route.

Two shapes you will use today:

| Function | Parameters | Typical job |
|----------|------------|-------------|
| `get_settings()` | None | Return a small dict (app name from `.env`) |
| `require_access_key(access_key: str)` | `access_key: str` with **no default** | Required **query** `access_key`; compare to `.env`; return the key or **401** |

- Need: Settings should not be pasted as a string in five handlers. An access check should not be a private `if` inside only `create_notice`.
- Logic: No extra parameters → nothing new in Swagger; the route just receives a dict. A required `str` argument → Swagger shows a query box, because that name is **not** in the path.
- Common error: Putting `{access_key}` in the path **and** in the dependency. Then it becomes a **path** slot. Today the key is a **query** on write routes only.
- Common doubt: “Must I return something?” If the route names an argument (`settings`, `access_key`), return the value. A dependency that only raises can still return the key on success so the route can log it.

**`get_settings` — shared read, no extra query**

- Reads `APP_NAME` once in one function.
- Injected into `/`, `/health`, and `GET /notices` so all three JSON bodies can echo the same app name.
- Change `.env` and all three stay in sync after reload.

**`require_access_key` — shared guard on writes**

- Compares `access_key` to `ACCESS_KEY` in `.env` (fallback `"demo-key"` in code for class practise).
- Wrong value → `HTTPException` with status **401** and a `detail` **string** (same key name as 404, not the 422 **list**).
- Missing query → FastAPI **422** (required query), **before** your `if`. The function body of `require_access_key` does not run if the query is absent.

- **401**  
  - *Official Definition:* HTTP Unauthorized — the request is understood but the credential is not accepted.  
  - *In Simple Words:* The key was present but not the right one.  
  - *Real-Life Example:* You showed an ID card; it is expired. The desk does not start the paperwork.
- **`HTTPException`**  
  - *Official Definition:* FastAPI/Starlette exception that turns into an HTTP error response (`status_code`, `detail`).  
  - *In Simple Words:* A structured way to stop the route and send an error stamp.  
  - *Real-Life Example:* The clerk stamps “rejected” and returns the file; the inner office never opens it.

![Missing access_key is 422; wrong access_key is 401](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module3/session29/session29-04-422-vs-401.png?v=20260915)

### Student activity: 422 vs 401

1. Missing `access_key` on POST — **422** or **401**? Does `create_notice` run?
2. `access_key=wrong` — **422** or **401**? Does `require_access_key` run?
3. `access_key=demo-key` (matching `.env` / fallback) — which function runs after the check?

Connecting idea: The same `Depends(...)` line can be pasted onto every write route. That is “apply across multiple endpoints.”

Example `.env` (no quotes around values). Save the file in the project folder you already use:

```bash
APP_NAME=notice-api
ACCESS_KEY=demo-key
```

- If a line is missing, the code fallbacks still run (`notice-api`, `demo-key`).
- Do not put this file in a screenshot or chat. It is a class key, not a public password design.
- Common error: `access_key: str = "demo-key"` **inside** the dependency. That default makes the query **optional**. A missing key would skip 422 and then compare `demo-key` to `demo-key` — every guest would pass. Keep **no default** on `access_key`.

## Inject dependencies into route functions

Put `Depends` in the **route signature**, not inside the `def` body.

- Write `settings: dict = Depends(get_settings)` on each route that should receive the dict.
- Write `access_key: str = Depends(require_access_key)` on each write route. FastAPI runs the callable **before** `create_notice` / `update_notice` / `delete_notice`.
- The full `main.py` later shows both on a working app. Do not call those functions yourself inside the handler.

- A route may take **more than one** injected value, plus path params, plus a Pydantic body. FastAPI sorts them by type and name, as before.
- Order in the signature does not have to match Swagger’s visual order. Names must match what you use in the body.
- Need: POST still needs `NoticeCreate`. The access check is a **second** parameter. Do not fold the key into the JSON body unless you design it that way; today it is a **query** so GET-like tools can send it without a body, and Swagger shows a separate box.
- Logic: Path `notice_id: int` stays a path param because `{notice_id}` is in the decorator. `access_key` is not in the path, so it is a query **declared by the dependency**.
- Common error: Decorating the **dependency** with `@app.get`. Dependencies are not routes. Only path functions get decorators.
- Common error: Reusing the name `request` as a dependency return by mistake. Keep names `settings` and `access_key`.

**Same dependency, several endpoints**

![POST, PUT, and DELETE share require_access_key; GET list and GET-one stay open](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module3/session29/session29-02-depends-write-routes.png?v=20260915)

| Route | `Depends(get_settings)` | `Depends(require_access_key)` |
|-------|-------------------------|-------------------------------|
| `GET /` | Yes | No |
| `GET /health` | Yes | No |
| `GET /notices` | Yes | No |
| `GET /notices/{notice_id}` | No | No |
| `POST /notices` | No | Yes |
| `PUT /notices/{notice_id}` | No | Yes |
| `DELETE /notices/{notice_id}` | No | Yes |

GET-one is left without both on purpose: you will see in `/docs` that **not every** card has `access_key`. That is the point of opt-in.

### Student activity: predict Swagger boxes

1. Open the table above. Which methods show `access_key` in `/docs`?
2. Which methods echo `app` from settings?
3. Does `GET /notices/{notice_id}` require a key? Write yes/no.

Connecting idea: Dependencies wrap **chosen** functions. Middleware wraps the **app**.

## What middleware is and when to use it

- **Middleware**  
  - *Official Definition:* A layer that processes every HTTP request (and later the response) around the routed endpoint, typically by receiving `request` and a `call_next` callable.  
  - *In Simple Words:* A belt around the whole shop: in, then the counter, then out.  
  - *Real-Life Example:* Security at the campus gate timestamps **everyone** going in and out — mess, library, hostel office — not one clerk copied into each building.

![Request path: middleware in, dependencies, route function, middleware out, response headers](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module3/session29/session29-03-middleware-request-chain.png?v=20260915)

- **`call_next`**  
  - *Official Definition:* The awaitable that continues the chain (routing, dependencies, path function) and returns the `Response`.  
  - *In Simple Words:* “Please run the rest of the app, then give me the reply.”  
  - *Real-Life Example:* The gate guard lets you into campus, waits until you finish, then stamps the exit time.
- **`Request`**  
  - *Official Definition:* The Starlette/FastAPI object that represents the incoming HTTP call (method, URL, headers).  
  - *In Simple Words:* The envelope of the letter, not the JSON body you already validate with Pydantic.  
  - *Real-Life Example:* The stamp and address on the cover — method `GET`, path `/health` — before anyone opens the slip inside.

**When to use middleware**

- You need something on **all** (or nearly all) HTTP traffic: a timing header, a custom `X-API` label, a log of method + path.
- The work is about the **envelope** (URL, method, headers out), not about one resource’s business rule.

**When not to use middleware (use a dependency instead)**

- Only **some** routes need the behaviour (write routes need a key; reads do not).
- You need Swagger to show an extra **parameter** on those routes.
- You need to **return a value** into the function (`settings["app"]`).

**Which tool? Pick one row.**

| Need | Tool |
|------|------|
| Echo `APP_NAME` on `/`, `/health`, and the list | `Depends(get_settings)` on those three |
| Block POST/PUT/DELETE unless the query key matches | `Depends(require_access_key)` on those three |
| Put `X-API` on **every** reply, including `/docs` | HTTP middleware |
| Check JSON `title` / `message` | Pydantic body (already known); not DI, not middleware |

- Need: Timing **one** handler with `time` inside that function misses `/health` and the docs page. Middleware times the whole round trip.
- Logic: Code **before** `await call_next(request)` runs on the way **in**. Code **after** runs on the way **out**, when you have a `response` and can set headers.
- Common error: Forgetting `await` on `call_next`. The chain never finishes correctly.
- Common error: Not `return response`. The client hangs or errors.
- Common error: Using middleware for the access key. Then `/docs` itself would demand the key, and you could not open Swagger.
- Common doubt: “Why is this function `async` when my routes are `def`?” This wrapper must **wait** for the rest of the chain. Routes today stay ordinary `def`. Do not copy `async` onto every handler.

FastAPI registers this kind of hook with `@app.middleware("http")`.  
That decorator is enough for today’s custom timing-and-label layer.

Order you should remember (one direction):

1. Middleware (in)
2. Route match + **dependencies**
3. Your path function
4. Middleware (out) — set headers on the **response**

### Student activity: in or out?

1. Measuring elapsed time needs a clock **before** and **after** the route — which side of `call_next` is the second clock?
2. Adding `X-API` on the reply — before or after `call_next`?
3. If middleware raises **before** `call_next`, does `GET /health` run?

Connecting idea: You will implement **one** timing-and-label middleware and **two** dependencies in the same `main.py`.

## Build a simple middleware and shared dependencies

Use this complete program as `main.py`.  
Every line is commented. Put `ACCESS_KEY=demo-key` in `.env` if you want to override the fallback.

```python
from fastapi import FastAPI, Depends, HTTPException, Request  # App, injection marker, error stamp, HTTP envelope
from fastapi.responses import JSONResponse  # 404 bodies
from pydantic import BaseModel  # Request/response schemas you already know
from dotenv import load_dotenv  # Read .env
import os  # getenv for APP_NAME and ACCESS_KEY
import time  # Clock for process time

load_dotenv()  # Fill environment first

app = FastAPI(  # Uvicorn serves this object
    title="Notice Board API",  # Swagger title
    description="Shared settings, write-route access key, and timing middleware",  # Subtitle
    version="0.4.0",  # OpenAPI version label
)  # End FastAPI()

notices = []  # In-memory board; empty after restart


class NoticeCreate(BaseModel):  # JSON for POST and PUT
    title: str  # Required text
    message: str  # Required text


class NoticeOut(BaseModel):  # JSON for one notice
    id: int  # Server id
    title: str  # Stored title
    message: str  # Stored message


def get_settings():  # Dependency: no extra query
    app_name = os.getenv("APP_NAME", "notice-api")  # Name from .env or fallback
    return {"app": app_name}  # Small dict injected into routes


def require_access_key(access_key: str):  # Dependency: required query access_key
    expected = os.getenv("ACCESS_KEY", "demo-key")  # Secret from .env or class fallback
    if access_key != expected:  # Present but wrong
        raise HTTPException(status_code=401, detail="Invalid access_key")  # Stop; string detail
    return access_key  # Injected into the route on success


@app.middleware("http")  # Run around every HTTP request
async def stamp_response(request: Request, call_next):  # Must wait for the rest of the chain
    started = time.perf_counter()  # Clock on the way in
    response = await call_next(request)  # Route + dependencies + handler
    elapsed_ms = (time.perf_counter() - started) * 1000  # Clock on the way out
    response.headers["X-Process-Time-Ms"] = str(round(elapsed_ms, 2))  # Timing header
    response.headers["X-API"] = "notice-board"  # Label header on every reply
    return response  # Always return the response


@app.get("/")  # Welcome
def home(settings: dict = Depends(get_settings)):  # Inject settings
    return {"message": "Hello from the backend", "app": settings["app"]}  # 200


@app.get("/health")  # Liveness
def health(settings: dict = Depends(get_settings)):  # Same dependency, second route
    return {"status": "ok", "app": settings["app"]}  # 200


@app.get("/notices")  # List
def list_notices(settings: dict = Depends(get_settings)):  # Same dependency, third route
    return {"app": settings["app"], "notices": notices}  # No access_key on reads


@app.get("/notices/{notice_id}", response_model=NoticeOut)  # GET one — no Depends today
def get_notice(notice_id: int):  # Path param only
    for item in notices:  # Search
        if item["id"] == notice_id:  # Match
            return item  # NoticeOut
    return JSONResponse(status_code=404, content={"detail": "Notice not found"})  # 404


@app.post("/notices", response_model=NoticeOut, status_code=201)  # Create
def create_notice(payload: NoticeCreate, access_key: str = Depends(require_access_key)):  # Body + key
    ids = []  # Collect ids
    for item in notices:  # Walk
        ids.append(item["id"])  # Integer ids
    new_id = 1  # First pin
    if len(ids) > 0:  # Not empty
        new_id = max(ids) + 1  # Next id
    notice = {"id": new_id, "title": payload.title, "message": payload.message}  # Row
    notices.append(notice)  # Store
    return notice  # 201 NoticeOut


@app.put("/notices/{notice_id}", response_model=NoticeOut)  # Replace
def update_notice(notice_id: int, payload: NoticeCreate, access_key: str = Depends(require_access_key)):  # Path + body + key
    for item in notices:  # Search
        if item["id"] == notice_id:  # Match
            item["title"] = payload.title  # Replace
            item["message"] = payload.message  # Replace
            return item  # 200
    return JSONResponse(status_code=404, content={"detail": "Notice not found"})  # 404


@app.delete("/notices/{notice_id}")  # Remove
def delete_notice(notice_id: int, access_key: str = Depends(require_access_key)):  # Path + same key dependency
    index = -1  # Not found
    i = 0  # Index
    for item in notices:  # Search
        if item["id"] == notice_id:  # Match
            index = i  # Remember
            break  # Stop
        i = i + 1  # Next
    if index == -1:  # Missing
        return JSONResponse(status_code=404, content={"detail": "Notice not found"})  # 404
    removed = notices.pop(index)  # Remove
    return {"message": "deleted", "notice": removed, "by": access_key}  # 200; shows injected key
```

**How the code works:**

- `get_settings` is injected on **three** GET routes. One function, three endpoints. That is reusable DI.
- `require_access_key` is injected on **POST, PUT, and DELETE**. Same callable, three write endpoints. GET list and GET-one stay open.
- Missing `access_key` → **422** from FastAPI (query required). Wrong key → **401** from `HTTPException` inside the dependency. `create_notice` runs only after a match.
- `@app.middleware("http")` runs for **every** HTTP call, including `/docs`. It does not add `access_key` to Swagger. It adds **response headers**.
- `await call_next(request)` is the only place the route and its dependencies run. Elapsed time uses a clock on both sides of that line.
- On the way in you could read `request.method` and `request.url.path` (the envelope). Today we only stamp **outgoing** headers so `/docs` stays easy to open.
- `NoticeCreate` / `NoticeOut` / `JSONResponse` 404 behave as in the previous session. They are not the lesson; they keep the sample a real API.
- DELETE returns `"by": access_key` so you can **see** the injected value once in JSON. Other write routes do not need to echo it.
- `get_settings` has no `access_key` parameter, so those three GETs do not grow a new Swagger box. The write guard does, because it declares `access_key: str`.
- Custom header names start with `X-` here only as a classroom label. They are ordinary response headers; browsers do not treat them as special cookies.

### Student activity: two tools, two scopes

1. Count how many route functions use `get_settings`. Count how many use `require_access_key`.
2. Write one sentence: why `/docs` still opens **without** `access_key`.
3. Write one sentence: why you still expect `X-API` on a GET `/health` response.

## Hands-on — shared dependency and middleware in Swagger

Keep Uvicorn running. Open `http://127.0.0.1:8000/docs`.  
Title **Notice Board API**, version **0.4.0**.

**Settings on three GETs**

1. Execute **GET /**. Confirm JSON includes `"app"`.
2. Execute **GET /health**. Confirm the same `"app"` string.
3. Execute **GET /notices**. Confirm `"app"` and `"notices"`.
4. If you set `APP_NAME` in `.env`, confirm all three show that string after save and reload.
5. Confirm **GET /notices/{notice_id}** has **no** `access_key` box and **no** extra settings parameter.

**Write routes share one guard**

1. Expand **POST /notices**. Confirm a query box **access_key** (from the dependency, not from `NoticeCreate`).
2. The JSON editor is the **body**. The key is **not** a field inside `title` / `message`. Fill both.
3. Execute with a valid body and **no** key. Expect **422**. `loc` should mention `query` and `access_key`.
4. Execute with `access_key` `wrong` and a valid body. Expect **401** and a string `detail`.
5. Execute with `access_key` `demo-key` (or your `.env` value) and a valid body. Expect **201**.
6. Repeat the wrong-key test on **PUT** and **DELETE**. Same dependency, same **401**.
7. GET the new id **without** a key. Expect **200**. The guard is not on GET-one.

**Middleware headers (every response)**

1. After any successful GET, open the response **Headers** in Swagger (or the browser Network panel).
2. Find `X-Process-Time-Ms` (a number) and `X-API` = `notice-board`.
3. Repeat on **GET /health** and on **POST** (after a valid key). Same two headers. No extra Python in those handlers.
4. Load `/docs` itself; in Network, the document response can also carry `X-API`. Middleware does not skip the docs page.

**Injected value on DELETE**

1. POST one notice with a valid key. Copy `id`.
2. DELETE that id with `access_key` `demo-key`.
3. Read `"by"` in the JSON. That string came from `Depends`, not from the path.

### Student activity: receipt card

1. Write one **422** `loc` for a missing key on POST.
2. Write one **401** `detail` for a wrong key on PUT.
3. Copy the two custom **header names** from GET `/health`.
4. Name the one GET that uses **neither** dependency.

## If something breaks — check this list

| What you see | Likely cause | What to do |
|--------------|--------------|------------|
| `/docs` will not load | Uvicorn down, or `/doc` | Start server; use `/docs` |
| Access check never runs | Missing `Depends(...)` | Use `= Depends(require_access_key)` |
| Function object in JSON / odd default | `= get_settings` without `Depends` | Add `Depends` |
| POST has no `access_key` box | Dependency not on that route | Put `Depends(require_access_key)` on POST/PUT/DELETE |
| `/docs` asks for a key | Guard placed in middleware | Keep the key as a **dependency** on write routes only |
| No `X-API` header | Middleware not registered, or old process | Save; `--reload`; check `@app.middleware("http")` |
| Hang / error after adding middleware | Forgot `await` or `return response` | `response = await call_next(request)` then `return response` |
| **401** when you omitted the query | You sent a blank string, not “no key” | Empty string is present; compare fails → 401. Omit the key for **422** |
| **422** on POST body | `NoticeCreate` missing a field | Still a schema issue; fix JSON, then the key |
| `401` `detail` is a list | You expected 422 shape | 401 uses a **string** `detail`; 422 uses a **list** |
| GET list requires a key | You injected the guard on GET | Follow the table; reads stay open |
| `async` copied onto `def home` | Misread the middleware note | Only the middleware function is `async` today |
| Everyone can POST without typing a key | `access_key` has a default in the dependency | Remove the default; missing must be **422** |
| `X-Process-Time-Ms` missing in Swagger | Looking at JSON body only | Open the **Headers** section of the response |

Connecting idea: **Depends** shares a function with the routes you list. **Middleware** stamps the envelope for every call. Pydantic still checks the JSON **body**.

## Key Takeaways

- **Dependency injection** means FastAPI **runs** a callable and **passes** the result into the route. Mark it with `Depends`.
- Reuse one function on many endpoints: `get_settings` on three GETs; `require_access_key` on POST, PUT, and DELETE. Missing query → **422**; wrong key → **401**.
- **Middleware** wraps **every** HTTP request/response. Use `await call_next(request)`, then set headers such as `X-Process-Time-Ms`. Do not put opt-in business rules here if they would lock `/docs`.
- Choose **dependency** for selected routes and injected values; choose **middleware** for envelope-wide behaviour. Further FastAPI features still sit on this same chain; they do not replace `Depends` or this HTTP wrapper.

## Important Commands, Libraries, Terminologies used

| Name | Meaning in this session |
|------|-------------------------|
| Modular | Shared logic in one place; routes declare they need it |
| Dependency injection | Framework supplies what the function lists |
| Dependency | Callable FastAPI runs before the route |
| `Depends` | Marker to run that callable and inject the result |
| `get_settings` | Shared dict (`APP_NAME`); three GET routes |
| `require_access_key` | Shared query check; POST, PUT, DELETE |
| `access_key` | Required query declared by the dependency |
| `HTTPException` | Stop the chain with an HTTP error |
| 401 | Wrong key (credential rejected) |
| 422 (query) | Required `access_key` omitted |
| 404 | Valid id, row missing (`JSONResponse`) |
| Middleware | Layer around every HTTP request/response |
| `@app.middleware("http")` | Register a simple HTTP wrapper |
| `call_next` | Continue to routing, dependencies, handler |
| `await` | Wait for that continuation to finish |
| `Request` | Incoming HTTP envelope in middleware |
| `response.headers` | Outgoing headers you can stamp |
| `X-Process-Time-Ms` | Timing header from middleware |
| `X-API` | Label header from middleware |
| `time.perf_counter` | Clock for elapsed milliseconds |
| Opt-in vs all traffic | Depends on chosen routes; middleware on all |
| `ACCESS_KEY` / `demo-key` | Expected key from `.env` or fallback |
| `APP_NAME` | Injected via `get_settings` |
| `NoticeCreate` / `NoticeOut` | Same schemas as before; not the lesson |
| `python3 -m uvicorn main:app --reload` | Dev server, same as before |
| `/docs` | Tester; must stay reachable without the write key |
| Query vs body | `access_key` is query; `title` is JSON body |
| Opt-in | You list `Depends` only on the routes that need it |
| Envelope | Method, path, headers — middleware’s usual job |
