# Advanced FastAPI – CORS, Background Tasks & File Handling

Have you uploaded a marks card, a passport photo, or a government ID on an exam portal or a job site?  
You click upload, the page says it is processing, and only after a short wait the document shows as submitted.

That is not a simple “I sent a letter, I got a reply.”  
After the site has already told you “we received it,” work still continues behind the scenes — storing the file, checking it, updating your application.

Now think of the office behind that website — your backend. Its door can be found by anyone on the internet.

What if a stranger builds their own website and quietly plugs it into your office: your students’ files, your data?  
That is not acceptable. You must allow **only your own front desk** to talk to your office.

![Your exam portal is allowed to call your backend; a stranger site is blocked](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module3/session30/session30-01-own-frontend-guest-list.png?v=20260915)

This session covers those everyday needs: **file upload and download** (the marks card), **background tasks** (the processing after the receipt), and **CORS** (the guest list so only your frontend may use your backend).

You already share checks across routes and stamp every visit. Keep that. Today you add **who may call you from a webpage**, **how a file arrives and goes back**, and **work that continues after the stamp**.

Activate your project **venv** and start Uvicorn the same way as before:

```bash
python3 -m uvicorn main:app --reload --host 127.0.0.1 --port 8000   # Serve the FastAPI app on localhost port 8000
```

You will still use **`/docs`** for upload, download, and background tasks. CORS is a **browser** rule, so you will also use a small HTML page on **port 5500**. The sample `main.py` below is only for today’s three features.

## What you will learn in this session

- What an **origin** is and why the browser blocks some **cross-origin** calls
- How to **configure CORS middleware** so a frontend can talk to this backend
- How **background tasks** run **after** the response is sent
- How to **upload** a file with `UploadFile` and **download** it with `FileResponse`

You will not rewrite `Depends` or a `call_next` wrapper. CORS uses a **provided** middleware class. You only pass the settings.

## Why the browser cares about origin

JavaScript in a page may call `fetch(url)`.  
The browser, not Python, decides whether the page is allowed to **see** that response.

- **Origin**  
  - *Official Definition:* The triple **scheme + host + port** of a page or API (for example `http://127.0.0.1:8000`).  
  - *In Simple Words:* The full address of the “building,” including the door number (port).  
  - *Real-Life Example:* `http://127.0.0.1:8000` and `http://127.0.0.1:5500` are two buildings on the same street — different ports, different origins.
- **Cross-origin request**  
  - *Official Definition:* An HTTP request whose Origin header does not match the URL being called.  
  - *In Simple Words:* The page lives at one address; the API lives at another.  
  - *Real-Life Example:* A hostel notice board (port 5500) asking the campus office (port 8000) for a file.

| Page URL | API URL | Same origin? |
|----------|---------|--------------|
| `http://127.0.0.1:8000/docs` | `http://127.0.0.1:8000/health` | Yes — Swagger will **not** show a CORS failure |
| `http://127.0.0.1:5500/page.html` | `http://127.0.0.1:8000/health` | **No** — the browser needs CORS headers |
| `http://localhost:5500/...` | `http://127.0.0.1:8000/...` | **No** — `localhost` and `127.0.0.1` are different hosts |

- Need: Real frontends (HTML/JS you already practised) are often **not** served by Uvicorn. Without CORS, `fetch` fails in the **browser console**, while `/docs` still looks fine.
- Logic: FastAPI can answer **200** and still be unusable from JS if `Access-Control-Allow-Origin` is missing. That is a browser lock, not a Python crash.
- Common error: Testing CORS only inside `/docs`. Same origin, so CORS never runs as a problem.
- Common doubt: “Is CORS a FastAPI login?” No. It is a **browser** permission model. `curl` and Postman are not browsers; they ignore CORS.

Connecting idea: The API must **declare** which page origins may read responses. FastAPI does that with **CORS middleware**.

## Configure CORS middleware

- **CORS (Cross-Origin Resource Sharing)**  
  - *Official Definition:* An HTTP header protocol that lets a server state which origins, methods, and headers a browser may use for cross-origin calls.  
  - *In Simple Words:* The API puts a guest list on the door: “pages from this address may read my replies.”  
  - *Real-Life Example:* A library that allows readers from College A’s ID, not from any random campus.
- **`CORSMiddleware`**  
  - *Official Definition:* Starlette/FastAPI middleware that adds CORS headers and answers browser **OPTIONS** preflight checks.  
  - *In Simple Words:* A ready-made wrapper. You do not write `call_next`. You pass **which origins** are allowed.  
  - *Real-Life Example:* A printed visitor policy at the gate, not a new guard you invent each morning.

![Page on port 5500 calling API on port 8000; CORSMiddleware allow_origins is the guest list](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module3/session30/session30-02-two-origins-cors.png?v=20260915)

- **Preflight**  
  - *Official Definition:* An automatic **OPTIONS** request the browser sends before some cross-origin calls (for example JSON POST) to ask what is allowed.  
  - *In Simple Words:* A “may I?” message before the real letter.  
  - *Real-Life Example:* Asking the clerk if the counter accepts a parcel, then sending the parcel.

Register it with `app.add_middleware(...)` **after** `app = FastAPI(...)`.

| Setting | What you pass today | Meaning |
|---------|---------------------|---------|
| `allow_origins` | `http://127.0.0.1:5500` and `http://localhost:5500` | Exact page origins (include scheme and port) |
| `allow_methods` | `["*"]` | GET, POST, OPTIONS, and the rest |
| `allow_headers` | `["*"]` | Request headers the page may send |
| `allow_credentials` | `False` | No cookies in this classroom demo |

- Need: Frontend–backend communication in the browser **requires** these headers. Python `requests` on the server does not.
- Logic: The Origin the browser sends must **match one string** in `allow_origins`. A trailing slash or the wrong port will fail.
- Common error: `allow_origins=["*"]` together with `allow_credentials=True`. That combination is not a valid CORS setup. Today credentials stay **False**.
- Common error: Listing `http://127.0.0.1:8000` as the only origin. That is the **API**, not the HTML page.
- Common doubt: “Do I add an `@app.options` route?” No. `CORSMiddleware` handles OPTIONS for you.

- **`Access-Control-Allow-Origin`**  
  - *Official Definition:* The response header that names which origin may read the body (a specific origin string, or `*` when credentials are not used).  
  - *In Simple Words:* The stamp on the reply: “this page is allowed to look.”  
  - *Real-Life Example:* A visitor pass with **one** college name printed on it — not a blank pass for the whole city.

You can confirm the header **without** HTML by sending an `Origin` yourself:

```bash
curl -i -H "Origin: http://127.0.0.1:5500" http://127.0.0.1:8000/health   # Show response headers including CORS
```

Look for `access-control-allow-origin: http://127.0.0.1:5500`. If the header is missing, the HTML button will fail even when `/health` returns 200 in `/docs`.

Connecting idea: CORS answers “may this **page** read the API?” Background tasks answer “may Python finish a job **after** I already replied?”

### Student activity: same origin or not?

1. Write the origin of `http://127.0.0.1:8000/health` (scheme, host, port only).
2. Write the origin of `http://127.0.0.1:5500/page.html`.
3. Circle whether `fetch` from the second to the first is cross-origin.

## Background tasks — work after the response

- **Background task**  
  - *Official Definition:* A callable FastAPI runs **after** the response has been sent to the client.  
  - *In Simple Words:* Stamp the receipt first, then write the register. The student does not wait for the register.  
  - *Real-Life Example:* The mess prints your coupon immediately; the count of plates is updated a moment later.
- **`BackgroundTasks`**  
  - *Official Definition:* A FastAPI parameter type. You call `.add_task(func, ...)` inside the route; FastAPI runs `func` after sending the response.  
  - *In Simple Words:* A to-do slip attached to this one request, done **after** JSON goes out.  
  - *Real-Life Example:* A sticky note on the file: “file this after the student leaves the window.”

![Client gets accepted JSON first; server.log is written after the response](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module3/session30/session30-03-background-task-after-response.png?v=20260915)

```python
def append_log(line: str):  # Ordinary function; runs after the response
    with open("server.log", "a", encoding="utf-8") as log_file:  # Append a text line
        log_file.write(line + "\n")  # One line per call


@app.post("/notes")  # JSON route
def create_note(payload: NoteCreate, background_tasks: BackgroundTasks):  # Extra parameter, not a body field
    background_tasks.add_task(append_log, "note:" + payload.text)  # Schedule; do not call append_log yourself
    return {"status": "accepted", "text": payload.text}  # Client gets this first
```

**How that fragment fits later:** the full `main.py` includes this pattern. The client’s **200** body does not wait for the disk write.

- Need: Logging or a short file note should not delay the HTTP stamp. The user already received `accepted`.
- Logic: `background_tasks` is **not** in the JSON body. FastAPI injects the helper because of its type, similar in *spirit* to other framework-supplied parameters — you still do **not** wrap it in `Depends` today.
- Common error: Putting slow work **before** `return`. That is a normal function call; the client waits. Use `add_task` for after-response work.
- Common error: Expecting the new log line to appear **inside** the same JSON. It will not. Open `server.log` after Execute.
- Common doubt: “Is this a second server?” No. Same Uvicorn process. A tiny delay after the reply is normal.
- Common doubt: “Can I run a one-hour job here?” This tool is for **small** follow-up (a log line). Heavy jobs need other systems; not today.

### Student activity: before or after?

1. `return` then `add_task` — which does the client see first: JSON or the log line?
2. If `append_log` raises **after** the response, did the client already get **200**?
3. Should `append_log` be declared as a route with `@app.post`? Write yes/no.

Connecting idea: Notes are JSON. Photos and PDFs are **files**. The next two skills send bytes, not only `BaseModel` fields.

## File upload

JSON bodies (`NoteCreate`) are text.  
A file is a stream of **bytes** with a **filename**. Browsers send that as **multipart** form data, not as a JSON object.

![POST /upload stores bytes in uploads/; GET /download returns FileResponse; basename blocks unsafe names](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module3/session30/session30-04-upload-download-files.png?v=20260915)

- **Multipart**  
  - *Official Definition:* An HTTP body type (`multipart/form-data`) that can carry file parts plus fields in one request.  
  - *In Simple Words:* An envelope that can hold a document, not only a written note.  
  - *Real-Life Example:* A courier pouch with a form on top and a photocopied certificate inside.

- **`UploadFile`**  
  - *Official Definition:* FastAPI’s wrapper around an uploaded file (filename, content type, file handle).  
  - *In Simple Words:* The packet the client attached: name + contents.  
  - *Real-Life Example:* A photocopied marksheet in a plastic sleeve, with the student’s name on the tab.
- **`File(...)`**  
  - *Official Definition:* FastAPI marker that this parameter comes from the multipart **file** part of the request, not from JSON.  
  - *In Simple Words:* “This box is a file picker, not a JSON key.”  
  - *Real-Life Example:* The “attach document” slot on a form, not the “name” line.

```python
@app.post("/upload")  # Multipart, not JSON
def upload_file(file: UploadFile = File(...)):  # Swagger shows a file picker
    raw = file.file.read()  # Bytes from the upload
    safe_name = os.path.basename(file.filename or "unnamed")  # Drop any folder prefix
    path = os.path.join("uploads", safe_name)  # Save under uploads/
    with open(path, "wb") as out:  # Binary write
        out.write(raw)  # Store bytes
    return {"filename": safe_name, "bytes": len(raw)}  # JSON receipt, not the file itself
```

- Need: Profile photos, CSV dumps, and PDFs cannot live in `{"title": "..."}`.
- Logic: `/docs` **Try it out** becomes a **Choose file** control. You do not paste JSON for this route.
- Common error: Sending JSON `{"file": "..."}` to `/upload`. Wrong encoding. Use the file picker (or form-data in a client).
- Common error: Trusting `file.filename` with `../`. `os.path.basename` keeps only the last part of the name.
- Common error: Forgetting to create the `uploads` folder. The sample code creates it at startup.
- Common doubt: “Why is this `def` not `async`?” `file.file.read()` is a normal read. You do not need `await` for today’s upload.
- `file.content_type` (for example `text/plain`) is extra metadata. Today’s JSON receipt uses **name** and **size** only.

Swagger: **POST /upload** → Try it out → **Choose File** → Execute. Expect JSON with `filename` and `bytes`.

### Student activity: JSON vs file

1. Which route uses a JSON editor: **POST /notes** or **POST /upload**?
2. Which route uses a file picker?
3. After a successful upload, is the file in the HTTP **response body** or on the **server disk**?

Connecting idea: Upload **stores** bytes. Download **returns** those bytes as the HTTP body.

## File download

- **`FileResponse`**  
  - *Official Definition:* A Starlette response that streams a file from disk and sets headers such as `Content-Disposition` so the browser can save it.  
  - *In Simple Words:* The API answers with the file itself, not with `{"filename": ...}`.  
  - *Real-Life Example:* The office hands you the photocopied sheet, not a slip that only names the sheet.
- **`Content-Disposition`**  
  - *Official Definition:* An HTTP header that can mark the body as an attachment and suggest a filename.  
  - *In Simple Words:* A label on the parcel: “save this as notes.txt.”  
  - *Real-Life Example:* A courier sticker with the document title, not the document’s inner text.

```python
@app.get("/download/{name}")  # Path is the stored filename
def download_file(name: str):  # One file per call
    safe_name = os.path.basename(name)  # Block folder tricks
    path = os.path.join("uploads", safe_name)  # Same folder as upload
    if safe_name != name or not os.path.isfile(path):  # Missing or unsafe name
        return JSONResponse(status_code=404, content={"detail": "File not found"})  # JSON error
    return FileResponse(path, filename=safe_name)  # Bytes + download name
```

- Need: Clients must **get the file back**. A JSON receipt from upload is not the file.
- Logic: **200** from `FileResponse` is the file. **404** stays JSON so a missing name is readable in `/docs`.
- Common error: Returning `{"path": "uploads/a.png"}` and expecting the browser to download the image. That is only text.
- Common error: Using a path from the client without `basename`. Keep names inside `uploads/`.
- Common doubt: “Can I open this in `/docs`?” Execute may **download** or show binary. That is success, not a broken JSON pretty-printer.

Connecting idea: CORS, background log, upload, and download all live in **one** `main.py`. CORS is app-wide; the other three are routes.

**What runs when (today’s app)**

| Moment | What runs |
|--------|-----------|
| Browser on 5500 calls `/health` | `CORSMiddleware` adds allow-origin headers |
| POST `/notes` returns JSON | Then `append_log` writes `server.log` |
| POST `/upload` | Bytes saved under `uploads/` |
| GET `/download/{name}` | `FileResponse` sends those bytes |

### Student activity: match the tool

1. Guest list for a page on another port — CORS or `FileResponse`?
2. Write `server.log` after JSON — `add_task` or `UploadFile`?
3. Choose-file in Swagger — `/notes` or `/upload`?

## Build CORS, background tasks, and files into one app

Use this complete program as `main.py`.  
Create `page.html` next to it (full file after the Python). Every Python line is commented.

```python
from fastapi import FastAPI, BackgroundTasks, File, UploadFile  # App, after-response jobs, file part
from fastapi.middleware.cors import CORSMiddleware  # Ready-made CORS wrapper
from fastapi.responses import JSONResponse, FileResponse  # JSON errors and file bytes
from pydantic import BaseModel  # Small JSON body for /notes
import os  # Paths and folder create

app = FastAPI(  # Uvicorn serves this object
    title="Files and CORS API",  # Swagger title
    description="CORS for a page on port 5500, background log, upload and download",  # Subtitle
    version="0.5.0",  # OpenAPI version label
)  # End FastAPI()

app.add_middleware(  # Attach CORS to every browser call
    CORSMiddleware,  # Provided class; not a call_next function you write
    allow_origins=[  # Exact page origins
        "http://127.0.0.1:5500",  # python http.server / Live Server on 5500
        "http://localhost:5500",  # Same port, other host name
    ],  # End list
    allow_credentials=False,  # No cookies in this demo
    allow_methods=["*"],  # GET, POST, OPTIONS, ...
    allow_headers=["*"],  # Headers the page may send
)  # End add_middleware

UPLOAD_DIR = "uploads"  # Folder for saved files
os.makedirs(UPLOAD_DIR, exist_ok=True)  # Create if missing; no error if it exists


class NoteCreate(BaseModel):  # JSON for POST /notes
    text: str  # Required line of text


def append_log(line: str):  # Background callable; not a route
    with open("server.log", "a", encoding="utf-8") as log_file:  # Append mode
        log_file.write(line + "\n")  # One line


@app.get("/health")  # Liveness; used by the HTML fetch
def health():  # No file, no background work
    return {"status": "ok"}  # JSON 200


@app.post("/notes")  # JSON in; schedule log after reply
def create_note(payload: NoteCreate, background_tasks: BackgroundTasks):  # Body + task helper
    background_tasks.add_task(append_log, "note:" + payload.text)  # After response
    return {"status": "accepted", "text": payload.text}  # Client sees this first


@app.post("/upload")  # Multipart file
def upload_file(file: UploadFile = File(...)):  # File picker in /docs
    raw = file.file.read()  # Read all bytes
    safe_name = os.path.basename(file.filename or "unnamed")  # No folders in the name
    if safe_name == "":  # Empty name
        return JSONResponse(status_code=400, content={"detail": "filename required"})  # 400
    path = os.path.join(UPLOAD_DIR, safe_name)  # uploads/<name>
    with open(path, "wb") as out:  # Binary
        out.write(raw)  # Save
    return {"filename": safe_name, "bytes": len(raw)}  # Receipt JSON


@app.get("/download/{name}")  # Return stored bytes
def download_file(name: str):  # Path param is the file name
    safe_name = os.path.basename(name)  # Strip any extra path
    path = os.path.join(UPLOAD_DIR, safe_name)  # Look in uploads/
    if name != safe_name or not os.path.isfile(path):  # Unsafe or missing
        return JSONResponse(status_code=404, content={"detail": "File not found"})  # JSON 404
    return FileResponse(path, filename=safe_name)  # File body
```

**How the code works:**

- `add_middleware(CORSMiddleware, ...)` is **configuration**, not a new `async def` wrapper. Browser calls from port **5500** receive CORS headers. `/docs` on 8000 is same-origin and does not prove CORS.
- `allow_origins` is a **list of full origins**. Both `127.0.0.1` and `localhost` are listed because students type both.
- `create_note` returns JSON immediately. `append_log` writes `server.log` **after**. Open that file on disk; do not look for the line in the JSON.
- `UploadFile` + `File(...)` makes **POST /upload** a file field. Bytes land in `uploads/`.
- `FileResponse` on **GET /download/{name}** sends those bytes back. `basename` stops `../` names from leaving the folder.
- There is **no** `Depends` and **no** custom `@app.middleware("http")` in this file. Those remain previous skills; this file isolates today’s three features.
- `GET /health` exists so the HTML page has a tiny JSON target. CORS is tested on that call, not on `/docs`.
- `NoteCreate` has one field, `text`. It is only here so POST `/notes` can show `BackgroundTasks` next to a JSON body.
- Upload and download share the same `UPLOAD_DIR`. Download a name that was never uploaded → **404**, not an empty file.
- If `page.html` is not in the folder where you started `http.server`, the browser will 404 the page. `cd` first.

Save this **complete** `page.html` in the **same folder** (or any folder you will serve on 5500):

```html
<!DOCTYPE html>  <!-- HTML5 document -->
<html>  <!-- Root -->
  <head>  <!-- Metadata -->
    <meta charset="utf-8" />  <!-- Text encoding -->
    <title>CORS check</title>  <!-- Tab title -->
  </head>  <!-- End head -->
  <body>  <!-- Visible page -->
    <p>This page is origin http://127.0.0.1:5500 — not port 8000.</p>  <!-- Reminder -->
    <button id="btn" type="button">GET /health on port 8000</button>  <!-- Triggers fetch -->
    <pre id="out"></pre>  <!-- Result text -->
    <script>  <!-- Browser JavaScript -->
      document.getElementById("btn").onclick = async function () {  // Click handler
        var box = document.getElementById("out");  // Output node
        box.textContent = "calling...";  // Immediate feedback
        try {  // fetch can fail (network or CORS)
          var res = await fetch("http://127.0.0.1:8000/health");  // Cross-origin GET
          var data = await res.json();  // Parse JSON if CORS allows reading
          box.textContent = JSON.stringify(data);  // Show {"status":"ok"}
        } catch (err) {  // Blocked or network error
          box.textContent = String(err);  // Often a TypeError if CORS fails
        }  // End try
      };  // End handler
    </script>  <!-- End script -->
  </body>  <!-- End body -->
</html>  <!-- End document -->
```

Serve the HTML from a **second** terminal, from the folder that contains `page.html`:

```bash
python3 -m http.server 5500   # Static files on port 5500; keep Uvicorn on 8000
```

Open `http://127.0.0.1:5500/page.html` (not the file:// path, and not port 8000).

You now have **two processes**: Uvicorn (**8000**, API) and `http.server` (**5500**, HTML). Stop them separately with Ctrl+C in each terminal. Mixing the ports (HTML on 8000, API on 5500) will break both CORS and `/docs`.

### Student activity: two ports

1. Confirm Uvicorn is **8000** and `http.server` is **5500**.
2. Click the button. Write the text that appears in `<pre>`.
3. If you temporarily remove `CORSMiddleware` and reload both, what happens to the button? (Then put the middleware back.)

## Hands-on — `/docs`, log file, and the HTML page

Keep Uvicorn on **8000**. Title **Files and CORS API**, version **0.5.0**.

**Background task**

1. Expand **POST /notes** → Try it out. Body `{"text": "hello"}`.
2. Execute. Expect **200** and `"status": "accepted"` at once.
3. Open `server.log` in the project folder. Confirm a line `note:hello`.
4. Execute again with different text. Confirm a **second** line. The JSON never contains the file contents.

**Upload**

1. Create a small `.txt` on your laptop (a few words).
2. **POST /upload** → Choose File → that text file → Execute.
3. Expect JSON `filename` and `bytes`.
4. Confirm `uploads/<filename>` exists on disk.

**Download**

1. **GET /download/{name}** with the same filename.
2. Execute. Save or open the file. Contents should match what you uploaded.
3. Try a name you never uploaded. Expect **404** JSON `detail`.
4. Try a name like `../main.py`. Expect **404** (basename / safety check), not your source file.

**CORS with the HTML page**

1. Start `python3 -m http.server 5500` in the folder with `page.html`.
2. Browser: `http://127.0.0.1:5500/page.html`. Click the button.
3. Expect `{"status": "ok"}`.
4. Optional: DevTools → Network → the `/health` row → Response headers. Look for `access-control-allow-origin` with `http://127.0.0.1:5500`.
5. Run the `curl -i -H "Origin: ..."` command from the CORS section. Confirm the same header.
6. Do **not** treat success on `http://127.0.0.1:8000/docs` as a CORS test.

### Student activity: receipt card

1. Write whether POST `/notes` JSON includes the log line (yes/no).
2. Write the folder name where uploads are stored.
3. Write the two ports: API vs HTML page.
4. Copy the `allow_origins` values from `main.py`.
5. After `curl -i` with `Origin`, write whether you saw `access-control-allow-origin`.
6. Write yes/no: did `/docs` alone prove CORS?

## If something breaks — check this list

| What you see | Likely cause | What to do |
|--------------|--------------|------------|
| `/docs` will not load | Uvicorn down | Start Uvicorn on **8000** |
| HTML button error / `TypeError` | CORS missing, wrong origin, or API down | Middleware on; origin list matches the page URL; Uvicorn running |
| CORS “fails” in `/docs` | Same origin | Use port **5500** page, not `/docs`, to test CORS |
| `localhost:5500` blocked, `127.0.0.1:5500` works | Host string not in the list | Keep **both** origins in `allow_origins` |
| Opened `page.html` as `file://` | Not an origin in the list | Use `http.server` **5500** |
| Log line missing | Looking in JSON, or different working directory | Read `server.log` next to `main.py`; Execute POST `/notes` again |
| Upload 422 | Sent JSON to `/upload` | Use **Choose file**, not the JSON editor |
| `uploads` missing / save error | Folder not created | Sample calls `os.makedirs`; check you saved this `main.py` |
| Download is JSON path text | Returned a dict, not `FileResponse` | Return `FileResponse(path, filename=...)` |
| Download got `main.py` | Used a raw `../` path | Keep `basename` check; expect 404 for `../` |
| Port 5500 already in use | Another Live Server | Pick a free port **and** add that origin to `allow_origins` |
| OPTIONS 400 in Network | Preflight to a path that crashed | Confirm middleware is registered; restart Uvicorn |
| curl shows 200 but no `access-control-allow-origin` | `Origin` header omitted or origin not in the list | Pass `-H "Origin: http://127.0.0.1:5500"`; match `allow_origins` |
| HTML works, curl has no CORS header | Forgot `-H Origin` | CORS headers are added when Origin is sent |
| Two Uvicorns | Old process still on 8000 | Stop the extra process; one API only |
| `server.log` in another folder | Uvicorn started from a different directory | `cd` to the folder with `main.py` first |

Connecting idea: **CORS** is a guest list for **browsers**. **Background tasks** write after the stamp. **Upload** stores bytes; **download** returns them.

## Key Takeaways

- An **origin** is scheme + host + port. A page on **5500** calling an API on **8000** is **cross-origin**. `CORSMiddleware` plus an exact `allow_origins` list lets that page **read** the response.
- **`BackgroundTasks.add_task`** runs a function **after** the client already has the JSON. Use it for a small log line, not for work the client must see in the same body.
- **`UploadFile` + `File(...)`** accepts multipart files into `uploads/`. **`FileResponse`** sends those bytes back. Use `os.path.basename` so names stay inside that folder.
- `/docs` does not prove CORS. Further API features you add later still sit on this same Uvicorn app; they do not replace these three tools.

## Important Commands, Libraries, Terminologies used

| Name | Meaning in this session |
|------|-------------------------|
| Origin | Scheme + host + port |
| Cross-origin | Page origin ≠ API origin |
| CORS | Headers that allow the browser to share the response |
| `CORSMiddleware` | Provided middleware you configure |
| `app.add_middleware` | Attach that class to the app |
| `allow_origins` | Exact page origins (include port) |
| `allow_credentials=False` | Classroom setup; no cookies |
| Preflight | Browser **OPTIONS** before some calls |
| `BackgroundTasks` | Schedule work after the response |
| `add_task` | Register the callable |
| `append_log` / `server.log` | Sample after-response write |
| `UploadFile` | Uploaded file object |
| `File(...)` | Parameter is a file part, not JSON |
| Multipart | Encoding browsers use for file forms |
| `uploads/` | Folder created at startup |
| `os.path.basename` | Keep only the file name |
| `FileResponse` | HTTP body is the file |
| `filename=` on FileResponse | Name the browser uses to save |
| `page.html` | Cross-origin `fetch` demo |
| `python3 -m http.server 5500` | Serve the HTML page |
| `/docs` | Same origin as the API; not a CORS test |
| `python3 -m uvicorn main:app --reload` | Dev server on **8000** |
| `curl -i -H "Origin: ..."` | See CORS headers without a page |
| `Access-Control-Allow-Origin` | Header the browser reads |
| `server.log` | Lines written after POST `/notes` |
| `content_type` | Upload metadata; not required in today’s JSON |
| `os.makedirs(..., exist_ok=True)` | Create `uploads/` if missing |
| `JSONResponse` 404 | Missing download name |
| `Content-Disposition` | Save-as name on download |
| Port 8000 | Uvicorn / API / `/docs` |
| Port 5500 | HTML page origin |
| `NoteCreate` | JSON body `{ "text": "..." }` for POST `/notes` |
| `exist_ok=True` | Do not crash if `uploads/` already exists |
