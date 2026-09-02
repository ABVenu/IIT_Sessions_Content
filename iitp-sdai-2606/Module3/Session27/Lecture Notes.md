# FastAPI Dynamic Routes, Parameters & Swagger Docs

In the previous session you grew `campus-api` into **CRUD**: **GET /notices**, **POST /notices**, **PUT** and **DELETE** with a small **id slot**, JSON bodies, and tests in **Postman**.  
You already used `{notice_id}` so DELETE could stay without a body.  
This session treats that slot as a real topic — **path parameters** — then adds **query parameters** and the **Swagger** page FastAPI builds for you.

Keep the same folder, **venv**, and Uvicorn command:

```bash
python3 -m uvicorn main:app --reload --host 127.0.0.1 --port 8000   # Serve campus-api on localhost port 8000
```

You will test today’s routes mainly in the browser at **`/docs`**, not by relearning Postman.

## What you will learn in this session

- How **dynamic routes** use **path parameters** (typed slots such as `int` and `str`)
- How **query parameters** filter a list — **required**, **optional**, and **defaults**
- How FastAPI **auto-generates OpenAPI** and shows it as **Swagger UI**
- How to **Try it out** on parameterized GET routes in `/docs`

Stricter body **schemas** (dedicated model classes) are an upcoming skill. Today the body on POST/PUT stays a **dict**, as before.

## Path versus query in a URL

You already split a public URL into host, port, and path. Add one more reading skill: what sits **in** the path versus what sits **after `?`**.

| Piece | Example | Job |
|-------|---------|-----|
| Path | `/notices/1` | **Which** resource (notice number 1) |
| Query string | `/notices?limit=2&q=wifi` | **How** to filter or trim the list |

![Browser URL anatomy — GET /notices/1 highlights path parameter 1; GET /notices?limit=2&q=wifi highlights query parameters after the question mark](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module3/session27/session27-01-url-anatomy-path-query.png?v=20260902r2)

- **Path parameter**  
  - *Official Definition:* A variable segment of the URL path, written `{name}` in FastAPI, bound to a function argument of the same name.  
  - *In Simple Words:* A labelled blank in the corridor address — room **12**, not “some room.”  
  - *Real-Life Example:* Hostel block **A**, floor **3** in `/hostels/A/floor/3`.
- **Query parameter**  
  - *Official Definition:* A key-value pair after `?`, separated by `&`, that is **not** part of the path template.  
  - *In Simple Words:* Sticky notes on the request: “only two cards,” “search wifi.”  
  - *Real-Life Example:* IRCTC-style filters: `from=Pune&to=Nagpur` — extra description, not a different station building.
- Need: PUT `/notices` without an id was the wrong counter. The id belongs in the path. Search text does **not** belong in the path; it is a filter on GET `/notices`.
- Logic: FastAPI decides the kind of parameter by **where the name appears**. If `{notice_id}` is in the decorator path, it is a path param. If `limit` is only in the function, it is a query param.
- Common error: Writing `/notices/{notice_id}` in the browser with the curly braces still there. Clients send `/notices/1`. Braces are for **your** Python file only.
- Common doubt: “Is `?q=wifi` a second path?” No. The path is still `/notices`. The query is extra data on the same counter.

### Student activity: split one address

1. Write `http://127.0.0.1:8000/notices/1` — circle the **path parameter** value.
2. Write `http://127.0.0.1:8000/notices?limit=2` — circle the **query** part.
3. Confirm the first URL has no `?` and the second has no `{ }`.

## Path parameters — dynamic route segments

A **dynamic route** is a path template that matches many concrete URLs.

- **Dynamic route**  
  - *Official Definition:* A route whose path includes one or more `{placeholders}` filled in at request time.  
  - *In Simple Words:* One decorator, many doors: `/notices/1`, `/notices/2`, `/notices/9`.  
  - *Real-Life Example:* One hostel rule “floor N” instead of painting a separate sign for every floor.
- Need: You cannot register `@app.get("/notices/1")`, `@app.get("/notices/2")`, … for every id.
- Logic: `@app.get("/notices/{notice_id}")` plus `def get_notice(notice_id: int)` makes FastAPI parse the segment and pass it in.

![Path parameter binding — decorator /notices/{notice_id}, incoming GET /notices/1, function argument notice_id = 1 as an integer](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module3/session27/session27-02-path-param-binding.png?v=20260902r2)

- Common error: Declaring `{notice_id}` in the path but naming the argument `id`. Names must **match**.
- Common error: Putting `/notices/{notice_id}` **above** a static path that you still need as a different string — keep **`GET /notices`** (list) and **`GET /notices/{notice_id}`** (one item). FastAPI treats them as different templates.

**Typed path params:** the annotation `notice_id: int` or `hostel_name: str` is not decoration.

| Annotation | URL segment | FastAPI behaviour |
|------------|-------------|-------------------|
| `notice_id: int` | `1` | Passes Python integer `1` |
| `notice_id: int` | `abc` | **422** — not a number; your function does **not** run |
| `hostel_name: str` | `Ganga` | Passes the text `Ganga` |
| `floor_no: int` | `2` | Passes integer `2` |

- Need: Comparing `"1"` (text) to stored id `1` (number) would miss the notice. `int` converts and checks.
- Logic: **422 Unprocessable Entity** here means “the slot was the wrong type,” not “notice missing.” Missing id after a valid integer is **404** from your `JSONResponse`.
- Common doubt: “Is this the same 422 as a missing JSON body?” Same **status family**, different cause. Path `abc` fails type; empty POST body fails body parse.

![int path validation — GET /notices/abc fails type check with 422 and get_notice is not called; GET /notices/99 passes int, function runs, missing row returns 404](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module3/session27/session27-03-int-validation-422-404.png?v=20260902r2)

- Two slots in one path: `/hostels/{hostel_name}/floor/{floor_no}` — text then number. Order in the URL is the order of the segments.

Connecting idea: Path params pick **one resource**. Query params **narrow a list** without inventing a new path for every search.

## Several path slots in one route

`/hostels/{hostel_name}/floor/{floor_no}` is still **one** GET endpoint.  
The URL has two blanks. FastAPI fills two arguments.

![URL template versus request — /hostels/{hostel_name}/floor/{floor_no} aligned with /hostels/Ganga/floor/3 so Ganga maps to str and 3 maps to int](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module3/session27/session27-04-two-path-segments-url.png?v=20260902r2)

- Left-to-right in the path is the only order that matters: name first, floor second.
- `hostel_name: str` accepts `Ganga` or `Kaveri`. It does not turn into a number.
- `floor_no: int` still rejects `Ganga/floor/two` with **422**.
- Need: Real campus apps often nest “which hostel” then “which floor.” You do not need a database to practise the **shape**.
- Common error: `/hostels/3/floor/Ganga` if you swapped the slots in your head. Types will 422 or return odd JSON.
- You will call this route in Swagger with two boxes, not with `?`.

## Query parameters — optional, required, defaults

Query params never appear inside `{ }`. They appear after `?`.

- **Optional query parameter**  
  - *Official Definition:* A query key the client may omit; FastAPI uses a **default** (including `None`).  
  - *In Simple Words:* “If they did not say how many, show ten.”  
  - *Real-Life Example:* Mess menu without “spicy / less spicy” still serves a default plate.
- **Required query parameter**  
  - *Official Definition:* A query key with **no default** and a type annotation, so omitting it yields **422**.  
  - *In Simple Words:* The clerk will not search if you did not say the **keyword**.  
  - *Real-Life Example:* Library desk: “Search” with a blank slip is rejected.
- **Default**  
  - *Official Definition:* The Python value used when the query key is absent (`limit: int = 10`).  
  - *In Simple Words:* The fallback count.  
  - *Real-Life Example:* Printer “copies = 1” if you did not type a number.
- Need: `GET /notices` should still work with no `?`. Listing should not require a search box. A dedicated `/search` counter can demand `keyword`.
- Logic: `limit: int = 10` and `q: str = None` are optional. `keyword: str` with no `=` is required.
- Common error: Putting search text in the path (`/notices/wifi`) and hoping it filters. That hits **GET /notices/{notice_id}** and tries to parse `wifi` as an **int** → **422**.
- Common error: `limit=ten` (letters). `limit` is typed `int` → **422**.
- Common doubt: “Do I import a Query class?” Not today. Function arguments that are **not** in the path are already query params.

Examples you will call:

| Request | Meaning |
|---------|---------|
| `GET /notices` | All notices, up to default `limit` |
| `GET /notices?limit=2` | At most two items |
| `GET /notices?q=wifi` | Title or message contains `wifi` (case ignored) |
| `GET /search?keyword=mess` | Required keyword; omit `keyword` → **422** |
| `GET /hostels/Ganga/floor/3` | Two path params, no query |

GET with a query string is still **GET**. You may type it in the **browser** as well as in Swagger:

- `http://127.0.0.1:8000/notices?limit=2`
- `http://127.0.0.1:8000/search?keyword=wifi`
- `http://127.0.0.1:8000/hostels/Ganga/floor/3`

The browser cannot send POST bodies. It **can** send these GETs. Swagger is still the place to see **required** boxes and **422** without crafting the URL by hand.

### When the value goes in the path vs after `?`

Use this rule while you design GET routes.

| You need to identify… | Put it in the… | Example |
|-----------------------|----------------|---------|
| One notice, one floor, one hostel name | **Path** | `/notices/1`, `/hostels/Ganga/floor/3` |
| How many to show, a search word, a flag | **Query** | `?limit=2&q=wifi` |
| A new notice’s title and message | **JSON body** (POST/PUT) | Not a path, not a query |

- Need: Mixing these is how you get 422 on `/notices/wifi`.
- Logic: Path = **identity**. Query = **options**. Body = **payload** for write methods.
- Common error: `?notice_id=1` on GET `/notices` while also having GET `/notices/{notice_id}`. Two different designs. This session’s “one notice” route uses the **path**.

## Build parameterized routes

Replace `main.py` with the complete program.  
Every line is commented. Keep `.env` with `APP_NAME`. POST/PUT/DELETE stay so the board can hold data for GET-one and filters.

```python
from fastapi import FastAPI, Request, Body  # App, Request envelope, JSON body for POST/PUT
from fastapi.responses import JSONResponse  # Custom stamps 201, 400, 404
from dotenv import load_dotenv  # Load APP_NAME from .env
import os  # os.getenv for the welcome route

load_dotenv()  # Read environment variables first

app = FastAPI(  # Application Uvicorn serves; metadata appears in /docs
    title="Campus API",  # Title at the top of Swagger UI
    description="Notices board with path and query parameters",  # Short subtitle in /docs
    version="0.2.0",  # Version label in the generated OpenAPI file
)  # End of FastAPI() arguments

notices = []  # In-memory list; empty after restart


@app.get("/")  # GET / welcome
def home():  # Welcome handler
    app_name = os.getenv("APP_NAME", "campus-api")  # Name from .env
    return {"message": "Hello from the backend", "app": app_name}  # JSON 200


@app.get("/health")  # GET /health
def health():  # Liveness
    return {"status": "ok"}  # JSON 200


@app.get("/debug-request")  # GET envelope demo
def debug_request(request: Request):  # Inject Request
    return {  # Small JSON map
        "method": request.method,  # Verb
        "path": request.url.path,  # Path without query
        "query": str(request.url.query),  # Raw query string, may be empty
    }  # 200


@app.get("/notices")  # GET list with optional query params
def list_notices(limit: int = 10, q: str = None):  # limit defaults to 10; q optional
    result = []  # Filtered copy
    for item in notices:  # Walk stored notices
        if q is None:  # No search text
            result.append(item)  # Keep every item
        else:  # Search in title or message
            needle = q.lower()  # Case-insensitive needle
            title = item["title"].lower()  # Lower title
            message = item["message"].lower()  # Lower message
            if needle in title or needle in message:  # Substring match
                result.append(item)  # Keep matches only
    return {"notices": result[:limit], "limit": limit, "q": q}  # Slice to limit; echo filters


@app.get("/notices/{notice_id}")  # GET one — path param
def get_notice(notice_id: int):  # Typed as int
    for item in notices:  # Search by id
        if item["id"] == notice_id:  # Integer compare
            return item  # 200 and that dict
    return JSONResponse(status_code=404, content={"detail": "Notice not found"})  # Valid int, missing row


@app.get("/search")  # GET search — required query
def search_notices(keyword: str):  # No default → required
    result = []  # Matches
    needle = keyword.lower()  # Case-insensitive
    for item in notices:  # Walk board
        title = item["title"].lower()  # Lower title
        message = item["message"].lower()  # Lower message
        if needle in title or needle in message:  # Substring
            result.append(item)  # Keep
    return {"keyword": keyword, "notices": result}  # Echo keyword


@app.get("/hostels/{hostel_name}/floor/{floor_no}")  # Two path params
def hostel_floor(hostel_name: str, floor_no: int):  # str then int
    return {  # Demo JSON — no database
        "hostel": hostel_name,  # Text slot
        "floor": floor_no,  # Number slot
        "message": "Two path parameters in one route",  # Teaching line
    }  # 200


@app.post("/notices")  # POST create — same idea as previous session
def create_notice(request: Request, payload: dict = Body(...)):  # Required JSON dict
    title = payload.get("title")  # Read title
    message = payload.get("message")  # Read message
    if title is None or message is None or title == "" or message == "":  # Incomplete slip
        return JSONResponse(status_code=400, content={"detail": "title and message are required"})  # 400
    ids = []  # Collect ids
    for item in notices:  # Walk
        ids.append(item["id"])  # Integer ids
    new_id = 1  # First pin
    if len(ids) > 0:  # Board not empty
        new_id = max(ids) + 1  # Next id
    notice = {"id": new_id, "title": title, "message": message}  # New dict
    notices.append(notice)  # Store
    return JSONResponse(status_code=201, content=notice)  # Created


@app.put("/notices/{notice_id}")  # PUT update — path id plus body
def update_notice(notice_id: int, payload: dict = Body(...)):  # Typed path + JSON
    title = payload.get("title")  # New title
    message = payload.get("message")  # New message
    if title is None or message is None or title == "" or message == "":  # Incomplete
        return JSONResponse(status_code=400, content={"detail": "title and message are required"})  # 400
    for item in notices:  # Search
        if item["id"] == notice_id:  # Match
            item["title"] = title  # Replace
            item["message"] = message  # Replace
            return item  # 200
    return JSONResponse(status_code=404, content={"detail": "Notice not found"})  # 404


@app.delete("/notices/{notice_id}")  # DELETE — path only
def delete_notice(notice_id: int):  # Typed path
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
    return {"message": "deleted", "notice": removed}  # 200
```

**How the code works:**

- `FastAPI(title=..., description=..., version=...)` fills the **OpenAPI** header. You will see those strings in `/docs`.
- `list_notices(limit: int = 10, q: str = None)` — both names are **absent** from the path, so they are **query** params. Defaults make them optional.
- `result[:limit]` uses list slicing you already know. `q` filters with `in` on lowered strings.
- `get_notice(notice_id: int)` — `{notice_id}` is in the path, so this is a **path** param. `abc` never enters the `for` loop; FastAPI returns **422** first.
- `search_notices(keyword: str)` has **no default**. Swagger will mark `keyword` as required. Skip it → **422**.
- `hostel_floor` shows **two** path types in one URL. It does not use the notices list.
- POST/PUT/DELETE are unchanged in behaviour so you can fill the board before GET-one and `q=`.
- `debug_request` now returns `query`. Call `GET /debug-request?limit=2` in the browser and read the `query` field. Path stays `/debug-request`.
- `list_notices` echoes `"q": null` in JSON when you omit `q`. That is Python `None`, not a bug.
- Register **GET /notices** and **GET /notices/{notice_id}** as two functions. One list, one item.

### Student activity: predict the stamp

1. Empty board. `GET /notices/1` — **404** or **422**?
2. `GET /notices/abc` — **404** or **422**?
3. `GET /search` with no query — **422** or empty list?

## OpenAPI and Swagger UI

FastAPI does not only run routes. It **describes** them in a standard file, then serves a clickable website for that file.

- **OpenAPI**  
  - *Official Definition:* A language-agnostic specification (JSON or YAML) that lists paths, methods, parameters, and response shapes for an HTTP API.  
  - *In Simple Words:* The printed menu of every counter, for humans and other programs.  
  - *Real-Life Example:* A railway enquiry printout: train number, from, to — not the train itself.
- **Swagger UI**  
  - *Official Definition:* A browser app that reads an OpenAPI document and draws expandable operations with **Try it out**. FastAPI mounts it at **`/docs`**.  
  - *In Simple Words:* An interactive menu that can send the request for you.  
  - *Real-Life Example:* A canteen kiosk: pick an item, fill quantity, press pay — you still read the receipt stamp.

![FastAPI toolchain — Python route generates openapi.json, which Swagger UI at /docs renders so Try it out sends GET /notices/{notice_id}](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module3/session27/session27-05-openapi-to-docs.png?v=20260902r2)

- Need: Typing long query URLs by hand is slow. `/docs` shows **path slots** and **query boxes** generated from your function signatures.
- Logic: Decorators + type hints + `Body(...)` → OpenAPI JSON → Swagger draws the page. You do not write that JSON by hand today.
- Common doubt: “Is `/docs` my notices data?” No. It is **documentation of the API**. The data still lives in the `notices` list.
- Common error: Opening `/doc` (missing **s**). The path is **`/docs`**.
- Sibling page **`/redoc`** is another skin for the same OpenAPI file. This session uses **Swagger** at `/docs`.
- Raw spec: **`http://127.0.0.1:8000/openapi.json`** — machine-readable. Students can glance at `"paths"`; no need to edit it.

A quick look inside `openapi.json` (do not memorise the whole file):

- `"openapi"` — specification version FastAPI chose.
- `"info"` — your `title`, `description`, `version`.
- `"paths"` — each URL template such as `/notices/{notice_id}`.
- Under a path, `"get"` / `"post"` — methods you decorated.
- `"parameters"` — path and query slots with `"in": "path"` or `"in": "query"`.

That is **auto-generation**: you wrote Python; FastAPI wrote this JSON.

**What Swagger shows because of today’s code:**

| In Python | In `/docs` |
|-----------|------------|
| `{notice_id}` + `int` | Path field, type integer |
| `limit: int = 10` | Query field, default 10, not required |
| `q: str = None` | Query field, optional |
| `keyword: str` | Query field, required |
| `Body(...)` on POST | Request body editor |

Connecting idea: Postman is still a valid client. Today the **course tester** is Swagger so you see how documentation and live calls stay in sync.

### What you click in `/docs`

After **Try it out**, Swagger unlocks input boxes. **Execute** sends a real HTTP request to **your** Uvicorn process (same port **8000**).

- The **Responses** panel shows status, JSON body, and often a generated **curl** line. You do not need to run curl yourself.
- **Parameters** grouped as **path** vs **query** match today’s two kinds of slots.
- Empty optional query boxes: if Swagger sends `limit` as a blank string, you may see **422**. Put `10` back, or do not clear the default.
- **Schemas** at the bottom describe bodies. You are not writing a separate model class yet. POST still uses a JSON object with `title` and `message`.
- Click **Cancel** if you opened Try it out by mistake and want the description view back.
- Scroll the list: GET, POST, PUT, and DELETE on `/notices` are **separate** cards — one decorator each.
- Green GET vs orange POST colours in Swagger are only labels. They do not change your Python.

## Hands-on — test parameterized routes in Swagger

Keep Uvicorn running. Use Chrome (or any browser).

**Open the docs**

1. Visit `http://127.0.0.1:8000/docs`.
2. Confirm the title **Campus API** and version **0.2.0**.
3. Expand **GET /** and **GET /health** — same routes as before, now listed automatically.
4. Ignore **Authorize** if it appears. This API has no login yet.

**Fill the board (needed for GET-one)**

1. Expand **POST /notices** → **Try it out**.
2. In the request body, keep JSON with `"title"` and `"message"` (double quotes).
3. **Execute**. Read **201** and copy `id`.
4. Execute a second POST with a different title (for example include the word `wifi` in the message).

**Path parameter — GET one**

1. Expand **GET /notices/{notice_id}** → **Try it out**.
2. Type your first id (for example `1`) in the path field. **Execute**. Expect **200** and that notice.
3. Type `99`. **Execute**. Expect **404** and your `detail` string.
4. Type `abc`. **Execute**. Expect **422**. Your `get_notice` function did not run.

**Two path params**

1. Expand **GET /hostels/{hostel_name}/floor/{floor_no}**.
2. Try `Ganga` and `3`. Expect JSON echoing both values.
3. Put letters in `floor_no`. Expect **422**.

**Optional query — list**

1. Expand **GET /notices**.
2. Leave `limit` and `q` empty → **Execute**. Expect default limit behaviour and `q: null`.
3. Set `limit` to `1`. Expect at most one notice in the array.
4. Set `q` to `wifi`. Expect only notices whose title or message contains that text.

**Required query — search**

1. Expand **GET /search**.
2. **Execute** without `keyword`. Expect **422**.
3. Set `keyword` to `mess` or `wifi` and Execute. Expect `{ "keyword": "...", "notices": [ ... ] }`.

**Read the OpenAPI file once**

1. Open `http://127.0.0.1:8000/openapi.json` in a new tab.
2. Search for `"/notices/{notice_id}"` and for `"limit"`.
3. Close the tab. You do not edit this file by hand.

### Student activity: find `in: query`

1. In `openapi.json`, search for the word `limit`.
2. Note whether it sits under `"in": "query"` or `"in": "path"`.
3. Search `notice_id` and confirm `"in": "path"`.

### Student activity: Swagger receipt

1. Create two notices in `/docs`.
2. GET one by path id. Write the status.
3. GET `/notices` with `q` that matches only one title. How many objects in `notices`?
4. Force a **422** with a non-numeric path id. Write “function ran? yes/no.”

### Student activity: two slots

1. In `/docs`, call **GET /hostels/{hostel_name}/floor/{floor_no}** with your hostel name and floor `2`.
2. Write the JSON keys you received.
3. Change floor to `two` (letters). Confirm **422** before any hostel JSON.

## If something breaks — check this list

| What you see | Likely cause | What to do |
|--------------|--------------|------------|
| `/docs` will not load | Uvicorn down, or typo `/doc` | Start server; use `/docs` |
| Swagger empty or old routes | `main.py` not saved, or old process | Save file; `--reload`; refresh `/docs` |
| GET `/notices/wifi` → 422 | `wifi` parsed as `notice_id: int` | Use query `?q=wifi` on GET `/notices` |
| GET `/notices/1` → 404 | Board empty or wrong id | POST a notice first; use that `id` |
| `/search` → 422 | Missing `keyword` | Required query; fill it in Swagger |
| `q` does nothing | You searched with path, not query | Query on **GET /notices**, not GET-one |
| Title **FastAPI** not Campus API | Old `app = FastAPI()` without title | Use the `title=` version in `main.py` |
| Swagger 422 on GET `/notices` after clearing `limit` | Blank string is not an integer | Set `limit` to `10` or leave the generated default |
| `/search` works in browser with `?keyword=` empty | Empty string may pass `str` but find nothing | Required means the **key** must be present; still type a real word |
| Two path boxes swapped | Hostel name in the floor field | Floor is `int`; name is `str` — match the labels in `/docs` |
| GET list ignores `q=Wi-Fi` | Hyphen or different spelling vs stored text | Filter is substring on lowered title/message; POST a matching word first |

Connecting idea: Path slots name **which pin**. Query keys **filter the board**. Swagger is the menu that stays true to those signatures.

## Key Takeaways

- **Path parameters** (`{notice_id}`, `{hostel_name}`, `{floor_no}`) sit in the URL path. Type hints such as `int` convert and reject bad segments with **422**; your **404** still means “valid id, no row.”
- **Query parameters** sit after `?`. Defaults make them optional (`limit=10`, `q=None`). No default (`keyword: str`) makes them **required**.
- FastAPI **auto-generates OpenAPI** from routes and types. **Swagger UI** at `/docs` is that spec as a Try-it-out client. `/openapi.json` is the raw file.
- Test GET-one, two path slots, optional filters, and required search **in Swagger**. Keep POST so the in-memory board has rows.
- Upcoming work adds dedicated **schema classes** for JSON bodies. Your path and query skills stay; the letter inside POST will get stricter checks.

## Important Commands, Libraries, Terminologies used

| Name | Meaning in this session |
|------|-------------------------|
| Dynamic route | Path template with `{placeholders}` |
| Path parameter | Slot in the path; name matches the argument |
| Query parameter | Key after `?`; argument **not** in the path |
| Typed path param | e.g. `notice_id: int` |
| Optional query | Has a default (`limit: int = 10`) |
| Required query | No default (`keyword: str`) |
| Default | Value when the client omits the key |
| `q: str = None` | Optional search substring |
| `result[:limit]` | Slice the filtered list |
| OpenAPI | Auto-generated API description |
| Swagger UI | Interactive docs at `/docs` |
| `/openapi.json` | Raw OpenAPI document |
| `/redoc` | Alternate docs skin; optional |
| Try it out / Execute | Send a live request from `/docs` |
| 422 (path/query) | Wrong type or missing required query |
| 404 | Integer id parsed, row missing |
| `FastAPI(title=...)` | Metadata shown in Swagger |
| `request.url.query` | Raw query string on Request |
| `python3 -m uvicorn main:app --reload` | Dev server, same as before |
| Path vs query | Identity in the path; filters after `?` |
| `q: null` in JSON | Optional query was omitted (`None`) |
| Generated curl in Swagger | Copy of the request; you do not have to run it |
| `title` / `description` / `version` | OpenAPI header fields on `FastAPI()` |
| `in: path` / `in: query` | OpenAPI location of a parameter |
| Cancel (Swagger) | Leave Try it out without sending |
| `{hostel_name}` | Example `str` path slot |
| `{floor_no}` | Example `int` path slot |
| `keyword` | Required query on GET `/search` |
| `limit` | Optional query; default 10 |
| `needle` / `.lower()` | Case-insensitive substring filter |
| `/hostels/{hostel_name}/floor/{floor_no}` | Two path parameters, one GET |
