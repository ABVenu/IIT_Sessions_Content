# Introduction to Backend Development & FastAPI Setup

In Module 1 you learned **basic coding with Python** — variables, functions, lists, dictionaries, and running `.py` files on your laptop with **VS Code** and the **Terminal**.  
In Module 2 you learned **HTML**, **CSS**, and **JavaScript**. That stack is required for **frontend** work because **Python does not run inside the browser**. The browser understands HTML for structure, CSS for look, and JavaScript for clicks and `fetch()`.

In the previous session you used **AI coding assistants** to draft layouts, write small JavaScript, and **debug client-side Fetch GET** calls. You were always the **client**: you asked a public URL for JSON and painted it on the page.  
This session starts **backend**. You will open the other side of that conversation — a Python program that **listens**, **receives GET requests**, and **sends JSON back**.

Backend can be written in many languages: **Python**, **JavaScript (Node.js)**, **Java**, and others. This course uses **Python**, so the language you already practise becomes the language of the server.

## What you will learn in this session

- What **backend** is, why a website cannot live on frontend alone, and the **backend developer’s role**
- How a typical backend folder is organised: **venv**, **pip**, **project structure**, and **environment variables**
- How to create a **FastAPI** app and start the **development server**
- How to write and test a **basic GET endpoint** in the browser

You will not add extra HTTP methods or a dedicated API tester today. Those skills come in upcoming sessions. Today the goal is a clean project and one working GET route.

## Why frontend alone is not sufficient

A page you save as `index.html` and open from your laptop is useful for layout practice.  
It cannot be the full product. Real apps need a **shared brain** that many users can trust.

- **Frontend**  
  - *Official Definition:* The client-side layer that runs in the browser: structure (HTML), style (CSS), and interactivity (JavaScript).  
  - *In Simple Words:* Everything the user sees and taps.  
  - *Real-Life Example:* On **Swiggy**, the restaurant cards, search box, and “Place order” button are frontend.
- **Backend**  
  - *Official Definition:* The server-side layer that receives HTTP requests, applies business rules, talks to storage and other services, and returns a response.  
  - *In Simple Words:* The kitchen and accounts office behind the dining hall.  
  - *Real-Life Example:* Swiggy’s servers check whether the restaurant is open, calculate bill and GST, and record the order. That work is not CSS.
- Need: If every student’s marks lived only inside each browser tab, there would be **no single source of truth**. A teacher could not publish one result list. The backend holds the shared record.
- Logic: Frontend can **display** a hall ticket. Backend **decides** whether you are eligible, **stores** the roll number, and **returns** JSON or HTML the browser can show.
- Common doubt: “I already used `fetch` to get posts. Is that backend?” No. `fetch` is the **client** asking. Someone else wrote the server that answered. Today you start writing that server.
- Common error: Putting passwords, marks, or payment logic only in JavaScript files. Anyone can open DevTools and read frontend code. Secrets and rules belong on the server.

| Layer | Runs where | Typical job | What you already practised |
|-------|------------|-------------|----------------------------|
| Frontend | Browser | UI, forms, `fetch` GET | HTML, CSS, JS, DOM, Promises |
| Backend | Server process on a computer | Validate, decide, store, respond | Python (now used as a web server) |

Connecting idea: HTTP is the same language you learned earlier — **GET**, **JSON**, status **200**. Previously you sent GET. Now you **answer** GET.

### What the backend must do that HTML cannot

A static HTML file has no memory that survives closing the tab, and no way to share one honest list with a thousand students.  
The backend exists for those jobs.  
Keep this list in mind whenever someone asks “why not only frontend?”

- **Shared data:** One attendance sheet for the whole class, not a copy inside each phone’s JavaScript.
- **Rules:** “Only the exam cell can publish marks.” That check runs on the server, where users cannot edit it in DevTools.
- **Secrets:** Payment keys, database passwords, and private tokens never ship inside a `.js` file the browser downloads.
- **Work for many clients:** The same `GET /health` can serve Chrome today and a mobile app later. The UI changes; the endpoint stays.
- Logic: Frontend is the **shop window**. Backend is the **stock register**. A window without a register cannot run a real shop.

### Student activity: one app, two layers

1. Pick **IRCTC**, **GPay**, or your college portal.
2. Write two lines: **Frontend shows …** and **Backend must …**
3. Check that the backend line is something the browser **cannot** safely do alone (for example: confirm payment, store all students’ attendance).

## The backend developer’s role

Once you see two layers, the job description becomes clear.  
A backend developer does not choose button colours. They own the **contract** the frontend (and later, mobile apps) will call.

- **Backend developer**  
  - *Official Definition:* An engineer who designs and implements server-side application logic, APIs, and integrations that clients consume over the network.  
  - *In Simple Words:* The person who builds the counters that take orders and send stamped replies.  
  - *Real-Life Example:* In a railway reservation office, clerks do not paint the waiting hall. They check seats and print tickets. Backend is that clerk’s computer program.
- Typical responsibilities in a web application:
  - Expose **endpoints** (URLs + HTTP methods) such as `GET /health`
  - Return **structured data** (usually JSON) with a correct **status code**
  - Keep **business rules** in one place (who can see what, what is allowed)
  - Later: talk to a **database**, other APIs, and authentication — you will add those in upcoming sessions
- What is **not** the backend’s job today: pixel-perfect layout, Flexbox, or DOM updates. The frontend you already built still does that.
- **API (Application Programming Interface)**  
  - *Official Definition:* A documented set of request rules (path, method, data shape) that one program uses to talk to another.  
  - *In Simple Words:* The menu of counters: “this URL, this method, this reply.”  
  - *Real-Life Example:* `GET https://jsonplaceholder.typicode.com/posts` was an API you already called. You will now host a tiny API on your own machine.
- Common doubt: “Is backend only databases?” No. Storage is one later piece. Today the server can return a fixed JSON message with **no database**.
- Common error: Thinking “backend” means a special cloud you cannot touch. Your **laptop running Uvicorn** is a backend for local learning.

## Many languages can build backend — this course uses Python

A server is just a long-running program that **listens on a port** (a numbered door on the machine).  
That program can be written in more than one language.

| Language | Common backend style | Why you may hear the name |
|----------|----------------------|---------------------------|
| **Python** | FastAPI, Django, Flask | Readable syntax; strong for APIs and later AI features |
| **JavaScript** | Node.js (Express, Nest) | Same language as the browser, but Node runs **on the server**, not in Chrome |
| **Java** | Spring Boot | Very common in large enterprise systems |

- Need: Companies pick a language for hiring, libraries, and existing code. There is no single “correct” backend language.
- Logic: You already write Python. Using Python for backend means you reuse **functions**, **dictionaries**, and **modules** instead of learning a third language this week.
- Common doubt: “If JavaScript runs in the browser, can I use it on the server too?” Yes — **Node.js** does that. We still use **Python** here so Module 1 skills transfer directly.
- Common error: Trying to `import` Python inside an HTML file. The browser will not run it. Python belongs in a **server process** you start from Terminal.

Connecting idea: Language choice is settled. Next you need a **project box** so packages do not mix with other Python work on the same laptop.

## Typical backend project setup

A backend project is not one random `script.py` on the Desktop.  
It is a **folder** with an isolated Python, a list of packages, a start file, and settings that are not hard-coded.

- **Official Definition:** A **backend project setup** is the folder layout, isolated runtime, dependency list, and configuration files needed to run a server the same way on every machine.
- **In Simple Words:** A tiffin box with labelled dabbas — interpreter, libraries, app file, secrets — so nothing spills into other meals.
- **Real-Life Example:** A college lab PC is used by many students. If everyone `pip install`s into the **system** Python, packages collide. A **virtual environment** is your own labelled kit inside the project folder.

Minimum pieces you will create today:

| Piece | File or folder | Why it exists |
|-------|----------------|---------------|
| Project root | `campus-api/` | One home for this server |
| Virtual environment | `.venv/` | Isolated Python + packages |
| Dependency list | `requirements.txt` | So another laptop can install the same libraries |
| App entry | `main.py` | FastAPI application and routes |
| Secrets / config | `.env` | Values that change per machine and must not be committed |
| Git ignore | `.gitignore` | Stops `.venv` and `.env` from going to GitHub |

You already use **Git**. Treat `.venv` as generated machinery and `.env` as private notes. Only source files and `requirements.txt` belong in the remote repo.

Target layout after this session (names can vary; the **roles** should match):

```text
campus-api/
  .venv/              # Created by python3 -m venv — do not edit by hand
  .env                # APP_NAME=... — local only
  .gitignore          # Ignores .venv/ and .env
  requirements.txt    # Output of pip freeze
  main.py             # FastAPI app and GET routes
```

- Common error: Putting `main.py` on the Desktop **outside** the folder that contains `.venv`. Then Uvicorn and pip point at the wrong place.
- Common error: Creating a second venv inside a venv. Always `cd campus-api` first, then `python3 -m venv .venv` **once**.

## Create and activate a virtual environment

You installed **Python 3** and used **`python3`** for local DSA work.  
That global interpreter is shared. Backend projects add many packages; they must stay **inside the project**.

- **Virtual environment (venv)**  
  - *Official Definition:* A directory that contains a Python interpreter and its own `site-packages`, created with the standard library module `venv`.  
  - *In Simple Words:* A private Python cupboard for this project only.  
  - *Real-Life Example:* A hostel mess plate vs a tiffin from home. `venv` is your tiffin — FastAPI lives there, not in the shared mess (system Python).
- Need: FastAPI’s version for this project must not break an older package you used for a different assignment.
- Logic: You **create** the folder once, **activate** it every time you work, then `pip install` while it is active.
- Common error: Running `pip install fastapi` **without** activating venv. Packages go to the wrong Python; the server later says `ModuleNotFoundError`.
- Common doubt: “Do I upload `.venv` to GitHub?” No. Recreate it with `requirements.txt` on each machine.

**Create the folder and venv** (macOS / Linux / Git Bash). Use the same `python3` habit as before:

```bash
mkdir campus-api          # Create the project folder
cd campus-api             # Enter the folder
python3 -m venv .venv     # Build an isolated Python named .venv
```

**How the code works:**

- `mkdir` and `cd` make and enter the project root.
- `python3 -m venv .venv` runs the **venv** module and writes interpreter files under `.venv`.
- The dot in `.venv` hides the folder on some systems; that is a convention, not a requirement.

**Activate** so Terminal uses the project Python:

```bash
source .venv/bin/activate    # macOS / Linux: put .venv Python first on PATH
```

On **Windows Command Prompt**:

```bat
.venv\Scripts\activate.bat    # Windows: switch this session to the venv interpreter
```

On **Windows PowerShell** (if the script is blocked, use Command Prompt instead):

```powershell
.venv\Scripts\Activate.ps1    # PowerShell: same idea as activate.bat
```

**How the code works:**

- Activation changes **PATH** for **this Terminal only**. Close the tab, and you must activate again.
- A healthy prompt often shows `(.venv)` at the start of the line.
- Confirm with `python3 --version` and, on macOS/Linux, `which python3` — the path should include `.venv`.
- Leave the environment with `deactivate` when you switch to another project.
- `python3 -m venv` is safe to re-run only if you intend to **rebuild**. If `.venv` already works, do not delete it without a reason.
- If VS Code’s Terminal was opened **before** activation, click the Terminal tab and activate there too — the editor and Terminal must use the same cupboard.

### Student activity: prove the cupboard is yours

1. Create `campus-api`, run `python3 -m venv .venv`, and activate.
2. Confirm the prompt shows `(.venv)` (or that `which python3` points inside `.venv`).
3. If activation fails, you are in the wrong folder or used the wrong OS command — fix that before installing packages.

## Install packages with pip and freeze requirements

Activation is not enough. The empty venv has Python, not FastAPI.  
**pip** is the installer you run **after** the prompt shows the venv.

- **pip**  
  - *Official Definition:* The package installer for Python; it downloads projects from the Python Package Index (PyPI) into the current environment.  
  - *In Simple Words:* The store app for Python libraries.  
  - *Real-Life Example:* Play Store installs WhatsApp into your phone. `pip` installs FastAPI into `.venv`.
- **requirements.txt**  
  - *Official Definition:* A text file listing package names (and often versions) so `pip install -r requirements.txt` recreates the same environment.  
  - *In Simple Words:* The grocery list for this project.  
  - *Real-Life Example:* A lab recipe card: “buy these three items,” not “buy whatever is on sale.”

Install the three libraries this session needs:

```bash
python3 -m pip install fastapi uvicorn python-dotenv   # Install API framework, server, and .env loader
python3 -m pip freeze > requirements.txt               # Write the exact installed versions into a file
```

**How the code works:**

- `python3 -m pip` uses the **active** interpreter’s pip, which is safer than a random `pip` on PATH.
- **FastAPI** is the web framework you write routes in.
- **Uvicorn** is the **ASGI** server that keeps the process running and accepts HTTP.
- **python-dotenv** loads key-value pairs from a `.env` file into the process.
- `pip freeze` prints every installed package; `>` saves that list to `requirements.txt`.
- Common error: Forgetting `-m pip` and installing into a different Python. Always install while `(.venv)` is visible.
- A teammate later runs `python3 -m pip install -r requirements.txt` inside a fresh venv. They should not copy your `.venv` folder.
- Open `requirements.txt` once. You will see **fastapi**, **uvicorn**, **python-dotenv**, and extra helper packages pip pulled in automatically. You still **import** only what `main.py` needs.
- Confirm the install:

```bash
python3 -m pip show fastapi   # Print FastAPI name and version from the active venv
```

**How the code works:**

- `pip show` fails if FastAPI is missing from **this** interpreter — a quick health check before you write routes.
- If `show` works but Uvicorn later fails, you may have two Terminals: one activated, one not. Activate in the Terminal that runs the server.

Connecting idea: Libraries are listed. Next, keep secrets out of `main.py` so the same code can run on your laptop and on a lab machine with different names.

## Environment variables

Hard-coding `app_name = "Rohit’s API"` inside Python works for one person.  
It fails when the value should change without editing code — and it is dangerous for passwords.

- **Environment variable**  
  - *Official Definition:* A named value provided by the operating system or a loader (such as a `.env` file) and read at runtime with `os.getenv`.  
  - *In Simple Words:* A sticky note on the machine, not a line tattooed in the source file.  
  - *Real-Life Example:* Your Wi-Fi password is not printed on the hostel notice board. It lives in the router settings. **`.env`** is that private settings panel.
- **`.env` file**  
  - *Official Definition:* A local text file of `KEY=value` lines loaded into the process before the app starts.  
  - *In Simple Words:* A small notepad of settings next to `main.py`.  
  - *Real-Life Example:* `APP_NAME=campus-api` is like writing the shop name on a card in the cash drawer, not on the public menu poster.
- Need: Upcoming work will use API keys and database URLs. The habit starts now with a harmless `APP_NAME`.
- Logic: Code calls `os.getenv("APP_NAME")`. You change `.env` on each computer. Git ignores `.env`.
- Common error: Committing `.env` to GitHub. Treat it like a password notebook even if today’s value looks boring.
- Common doubt: “Can I put APP_NAME in `main.py` today?” You could, but then you skip the professional pattern this session is meant to build.

Create `.env` in `campus-api`:

```env
APP_NAME=campus-api
```

Create `.gitignore` in the same folder:

```gitignore
.venv/
.env
```

**How the code works:**

- `.gitignore` tells Git not to track the virtual environment or the env file.
- `requirements.txt` and `main.py` **are** tracked, so others can rebuild the project.
- After you change `.env`, **restart** the server. Uvicorn reload watches Python files, not `.env`, by default.

## Introduction to FastAPI

You now have a box (venv), groceries (`requirements.txt`), and a settings card (`.env`).  
The program inside the box is a **web framework** — it maps URLs to Python functions.

- **FastAPI**  
  - *Official Definition:* A Python web framework for building HTTP APIs; route functions return data (usually a dict) that FastAPI sends as JSON.  
  - *In Simple Words:* A helper that turns “when GET hits `/`, run this function” into a real server.  
  - *Real-Life Example:* FastAPI is the receptionist desk: you define counters (`/` and `/health`); it handles the queue of HTTP visitors.
- **Uvicorn**  
  - *Official Definition:* An ASGI server that hosts Python web apps and keeps listening for HTTP connections.  
  - *In Simple Words:* The process that **listens on a port** (usually **8000**) and forwards each request to FastAPI.  
  - *Real-Life Example:* If FastAPI is the receptionist script, Uvicorn is the office that stays open and answers the doorbell.
- **ASGI** means a standard way for Python servers to talk to web apps. You do not configure ASGI by hand today; Uvicorn implements it.
- Need: Writing raw sockets and HTTP parsing would take weeks. FastAPI + Uvicorn give you a correct GET in a few lines.
- Logic: You create an `app = FastAPI()` object, decorate functions with `@app.get("/path")`, then point Uvicorn at `main:app` (file `main.py`, variable `app`).
- Common doubt: “Is FastAPI a language?” No. It is a **framework** you import as a Python package.
- Common error: Running `python3 main.py` and expecting a website. Unless you start Uvicorn, nothing listens on port 8000.
- FastAPI can also prepare **interactive API documentation** in the browser. You will use that explorer in an upcoming session. Today, test by opening your paths directly.

### Read the localhost URL in three pieces

You already split public URLs into host and path.  
The same reading applies to your laptop server.

| Piece | Example | Meaning |
|-------|---------|---------|
| Scheme | `http://` | Local class work uses plain HTTP, not HTTPS |
| Host | `127.0.0.1` | Loopback — this computer |
| Port | `8000` | The door Uvicorn opened |
| Path | `/` or `/health` | Which GET function runs |

- Full welcome URL: `http://127.0.0.1:8000/`
- Full health URL: `http://127.0.0.1:8000/health`
- `localhost` and `127.0.0.1` usually mean the same machine. Pick one and stay consistent so you do not think you started two servers.
- Common error: Visiting `http://127.0.0.1/` **without** `:8000`. The browser then hits port **80**, not your FastAPI process.

Connecting idea: One decorated function is enough for a first **GET endpoint**. Keep the path **fixed** (no `{id}` in the URL). Dynamic paths and extra HTTP methods are upcoming work.

## Build a minimal FastAPI application and run the dev server

Stay inside `campus-api` with **venv activated**.  
Create `main.py` with the complete program below. Every line is commented.

```python
from fastapi import FastAPI  # Import the FastAPI class to create the web app
from dotenv import load_dotenv  # Import helper that reads the .env file
import os  # Import os so we can call os.getenv for APP_NAME

load_dotenv()  # Load KEY=value pairs from .env into this process

app = FastAPI()  # Create the application object Uvicorn will serve


@app.get("/")  # Register a GET handler for the path /
def home():  # Function that runs when a client GETs /
    app_name = os.getenv("APP_NAME", "campus-api")  # Read APP_NAME; use default if missing
    return {"message": "Hello from the backend", "app": app_name}  # Dict becomes JSON automatically


@app.get("/health")  # Register a GET handler for the path /health
def health():  # Function that runs when a client GETs /health
    return {"status": "ok"}  # Simple JSON so you can confirm the server is alive
```

**How the code works:**

- `load_dotenv()` must run **before** `os.getenv`, or `.env` values stay invisible.
- `app` is the object named in the Uvicorn command `main:app`.
- `@app.get("/")` is a **decorator**: it tells FastAPI “this function is the GET counter for `/`.”
- Returning a **dict** is enough. FastAPI converts it to a JSON **response** with status **200** when the function finishes normally.
- `/health` is a second **fixed** GET. The path is a constant string, not a placeholder in the URL.
- `os.getenv("APP_NAME", "campus-api")` uses the second argument if `.env` was forgotten — the server still starts.

**Expected JSON** if `.env` has `APP_NAME=campus-api` and you GET `/`:

```json
{"message": "Hello from the backend", "app": "campus-api"}
```

**Expected JSON** for GET `/health`:

```json
{"status": "ok"}
```

Key order on screen may differ slightly; the **keys and values** must match.

Start the **development server**:

```bash
python3 -m uvicorn main:app --reload --host 127.0.0.1 --port 8000   # Serve app from main.py on localhost port 8000
```

**How the code works:**

- `python3 -m uvicorn` starts the server using the **active** interpreter, the same pattern as `python3 -m pip`.
- `main:app` means “module `main`, variable `app`.” The file must be named `main.py`.
- `--reload` restarts when you save `.py` files. Handy while learning; you still restart after `.env` edits.
- `127.0.0.1` (localhost) means **only your machine** can call this server. That is the safe default for class.
- Port **8000** is the door number. The browser URL becomes `http://127.0.0.1:8000/`.
- Leave this Terminal **running**. Open a second Terminal if you need another command. Stop the server with **Ctrl + C**.
- Common error: `Address already in use` — another program (or an old Uvicorn) still holds 8000. Close it or pick `--port 8001` and use that port in the browser.
- Common error: `Could not import module "main"` — you ran Uvicorn from the **parent** folder, not from `campus-api`.

Terminal should print that Uvicorn is running. That line means the doorbell is on.

### Student activity: start and stop once

1. Activate venv, confirm `main.py` is in the current folder.
2. Run the Uvicorn command and wait until you see a “running” message.
3. Press **Ctrl + C**, start it again, and keep it running for the tests below.

## First GET endpoint — write and test

You already know **GET** means “read this resource” and that JSON looks like `{"key": "value"}`.  
Testing today is done in the **browser address bar**. A browser visit is a GET. Other methods need different tools, which you will practise later.

- **Endpoint**  
  - *Official Definition:* A specific combination of HTTP method and URL path that the server implements.  
  - *In Simple Words:* One labelled counter.  
  - *Real-Life Example:* `GET /health` is the “are you open?” window; `GET /` is the welcome desk.
- **GET route**  
  - *Official Definition:* A handler registered for HTTP GET on a path, here via `@app.get`.  
  - *In Simple Words:* “If someone asks to read this path, run this function.”  
  - *Real-Life Example:* Checking the canteen menu on the wall — you look; you do not rewrite the menu (that would be a different method, later).

**Test in the browser:**

1. Keep Uvicorn running.
2. Open Chrome (or any browser) and visit `http://127.0.0.1:8000/`.
3. You should see JSON: a **message** and an **app** name from `.env`.
4. Visit `http://127.0.0.1:8000/health` and confirm `{"status":"ok"}`.
5. Change the string `"Hello from the backend"` in `main.py`, save, wait for reload, then refresh the browser.
6. Optional: DevTools → **Network**, reload `/`, click the document row, confirm **method GET** and **status 200** — the same reading skill you used on public sites.

If the page says “Unable to connect,” Uvicorn is not running or the port in the URL does not match.

### From browser GET to your function (one round trip)

Walk this sequence once so FastAPI does not feel like magic.

1. You type `http://127.0.0.1:8000/health` and press Enter.
2. The browser sends **GET** `/health` to **127.0.0.1** port **8000**.
3. **Uvicorn** accepts the TCP connection and passes the HTTP request to **FastAPI**.
4. FastAPI sees `@app.get("/health")` and calls `health()`.
5. The function **returns a dict**. FastAPI packs it as JSON and status **200**.
6. The browser shows the JSON (or a formatted tree, depending on the browser).

- Need: If step 4 never runs, you either used the wrong path (`/Health` vs `/health` — paths are case-sensitive) or the server is down.
- Logic: This is the same **request–response cycle** you traced on IRCTC, except the server is **your** `main.py`.
- Common error: Typing a different path than the decorator. Register `/health` and visit `/health`. Capital letters and extra words in the path are a different endpoint.

This lesson stops at **GET** on a **fixed path**. Other HTTP methods, request bodies, dynamic URL pieces, API tester tools, and calling this server from an HTML `fetch` page are upcoming skills. Today, type the API URL in the browser.

### Student activity: prove GET is yours

1. Load `/` and write down the JSON keys you see.
2. Edit `.env` to `APP_NAME=my-first-api`, stop Uvicorn (**Ctrl + C**), start it again, refresh `/`.
3. Confirm the **app** field changed. If it did not, you edited the wrong `.env` or forgot to restart.

## If something breaks — check this list

| What you see | Likely cause | What to do |
|--------------|--------------|------------|
| `No module named uvicorn` | venv not active, or packages not installed | Activate `.venv`, then `python3 -m pip install -r requirements.txt` |
| `ModuleNotFoundError: fastapi` | Installed with a different Python | Activate venv; install again with `python3 -m pip` |
| Browser cannot connect | Server not running, or wrong port | Start Uvicorn; match `--port` in the URL |
| JSON has `"app": "campus-api"` after you changed `.env` | Server not restarted | Stop and start Uvicorn after `.env` changes |
| `Address already in use` | Port 8000 busy | Stop the old process or use another port |
| Git wants to add `.venv` | Missing `.gitignore` | Add `.venv/` and `.env` to `.gitignore` |

Connecting idea: A first GET on localhost is the same **request–response cycle** you traced before — only now **you** wrote the function that built the JSON.

## Key Takeaways

- **Frontend** (HTML/CSS/JS) runs in the browser; **backend** is a server program. Python cannot replace JavaScript in Chrome, but Python **can** implement the server that `fetch` talks to.
- Backend can be built in Python, JavaScript (Node.js), Java, and more; this course uses **Python** plus **FastAPI** and **Uvicorn**.
- A professional setup uses a **venv**, **pip** / **requirements.txt**, a clear folder, and **environment variables** in `.env` (never committed).
- `@app.get("/")` plus `python3 -m uvicorn main:app --reload` is enough to serve JSON for a **GET**. You test it by opening `http://127.0.0.1:8000/` in the browser.
- Upcoming sessions add more HTTP methods, request bodies, API testers, dynamic paths, and validation. Keep this project; you will grow the same `app` object.

## Important Commands, Libraries, Terminologies used

| Name | Meaning in this session |
|------|-------------------------|
| Backend | Server-side logic that answers HTTP and holds shared rules |
| Frontend | Browser UI; cannot safely store secrets or the only copy of data |
| API / endpoint | Method + path the client may call (`GET /health`) |
| venv / `.venv` | Isolated Python cupboard for one project |
| `python3 -m venv .venv` | Create the virtual environment |
| `source .venv/bin/activate` | Activate on macOS / Linux |
| `.venv\Scripts\activate.bat` | Activate on Windows Command Prompt |
| `deactivate` | Leave the virtual environment |
| pip / PyPI | Installer and public package index |
| `python3 -m pip install …` | Install into the **active** interpreter |
| `requirements.txt` | Frozen grocery list of packages |
| Environment variable / `.env` | Runtime config loaded by `python-dotenv` |
| `os.getenv` | Read one env value in Python |
| `.gitignore` | Keep `.venv` and `.env` off GitHub |
| FastAPI | Python framework for HTTP APIs |
| `app = FastAPI()` | Application object Uvicorn serves |
| `@app.get("/path")` | Register a GET handler |
| Uvicorn | ASGI server; listens on a **port** |
| `python3 -m uvicorn main:app --reload` | Dev command: file `main.py`, variable `app` |
| `127.0.0.1` / localhost | This computer only |
| Port 8000 | Default door for today’s server |
| JSON dict return | FastAPI turns a Python dict into a JSON body |
| GET in the browser | Visiting the URL sends GET; enough to test today |
