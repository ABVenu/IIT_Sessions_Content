# Software Development – Workshop Series (15 Hands-On Sessions)

> **Design rule:** Each session is **2 hours** — first **30 minutes** theory/concept framing, remaining **1.5 hours** pure implementation.
> **Difficulty mix:** 10 Beginner, 3 Intermediate, 2 Advanced.

### Topic Distribution

| Track | Count | Sessions |
|---|---|---|
| Frontend (HTML / CSS / DOM) | 3 | 1, 2, 3 |
| Pure JavaScript — Project-Based | 2 | 4, 5 |
| Full-Stack + SQL Database (Python / FastAPI) | 3 | 6, 7, 8 |
| Misc Engineering (Docker, CI/CD, Auth) | 3 | 9, 10, 11 |
| WebSockets & Real-Time | 1 | 12 |
| Caching & Batching | 1 | 13 |
| NoSQL Database (MongoDB) | 1 | 14 |
| DSA | 1 | 15 |

---

## Session 1: Landing Page Lab — Design for Every Screen

**Level:** Beginner

**Prerequisite:** Comfort with a code editor and opening HTML files in a browser. No prior web-dev experience required.

**Learning Objective / Outcome:** Learners will build a pixel-accurate, fully responsive product landing page (“ShopLane”) using semantic HTML, Flexbox, and CSS Grid — with identical HTML across mobile, tablet, and desktop. By the end they will confidently reason about the box model, choose Flexbox vs Grid, and ship mobile-first CSS.

### Detailed Subtopics

**First 30 minutes — Theory & Concept**
- Semantic HTML structure and why it matters (SEO, a11y, readability)
- The CSS box model and `box-sizing: border-box`
- Flexbox vs Grid: the 1D-vs-2D decision rule
- Mobile-first thinking and the role of media queries
- CSS custom properties as design tokens

**Remaining 1.5 hours — Implementation**
- Scaffold the HTML for navbar, hero, product grid, footer
- Build a sticky navbar with Flexbox + a mobile hamburger via CSS only
- Build a hero section (side-by-side on desktop → stacked on mobile)
- Build a self-responsive product grid using `grid-template-columns: repeat(auto-fit, minmax(240px, 1fr))`
- Apply fluid typography with `clamp()`
- Debug layout using Chrome DevTools Grid / Flexbox inspectors
- **AI-assisted block:** use AI to audit CSS for redundant values and accessibility issues

### Tools / Tech Stack / AI Tools
- HTML5, CSS3 (no framework, no utility library)
- Chrome DevTools (Grid / Flexbox inspectors)
- VS Code / Cursor
- Cursor AI or ChatGPT for CSS refactor + a11y audit

### By the End of This Workshop, Students Should Be Able To
Build a fully responsive, mobile-first landing page from scratch using only HTML and CSS — confidently reaching for Flexbox or Grid based on the layout need, applying fluid typography with `clamp()`, and debugging layout issues inside Chrome DevTools. They will feel the power of modern CSS, where a single HTML file adapts beautifully from a 360px phone to a 1440px monitor without writing a single line of JavaScript.

---

## Session 2: DOM Playground — Turn Clicks into Features

**Level:** Beginner

**Prerequisite:** Basic HTML & CSS (Session 1 is helpful but not required). No JS frameworks needed.

**Learning Objective / Outcome:** Learners will build a no-framework notes dashboard that adds, deletes, filters, and searches notes with live DOM updates — gaining muscle memory with the APIs that every frontend framework abstracts.

### Detailed Subtopics

**First 30 minutes — Theory & Concept**
- The DOM as a live tree and how the browser renders updates
- The event flow: capture → target → bubble
- Why re-rendering 1,000 nodes costs more than updating 10
- Event delegation as a performance and memory pattern
- “Single source of truth” — state drives the DOM, not the other way around

**Remaining 1.5 hours — Implementation**
- Build a state object and a `render()` function as the only place that touches the DOM
- Use `querySelector` + `dataset` attributes to identify nodes
- Create and append nodes with `document.createElement` (no `innerHTML` string hacks)
- Handle form submit with `FormData` + validation
- Implement event delegation on the notes list for delete clicks
- Add a 300ms debounced search input
- Implement live tag filtering with chip toggles
- Keep a `Showing X of Y` counter in sync
- **AI-assisted block:** ask AI to find a seeded bug or generate 5 unit tests for the render logic

### Tools / Tech Stack / AI Tools
- Vanilla JavaScript (ES6+), HTML, CSS
- Chrome DevTools (Performance tab to observe re-render cost)
- VS Code / Cursor
- Cursor AI / ChatGPT for bug-hunt drill and test generation

### By the End of This Workshop, Students Should Be Able To
Build a snappy, framework-free web app that reads form input, renders dynamic lists, and reacts to events in real time. Students will internalize the power of vanilla JavaScript — understanding how state drives the DOM, why event delegation saves memory, and how a simple debounce transforms a sluggish search into a smooth, professional one. They will walk away confident that the DOM is no longer a mystery.

---

## Session 3: Motion Studio — Build a Portfolio That Feels Alive

**Level:** Beginner

**Prerequisite:** Working knowledge of HTML/CSS. JS is not required — we use one provided 10-line snippet.

**Learning Objective / Outcome:** Learners will build an animated, mobile-first personal portfolio that feels smooth at 60fps, respects user motion preferences, and works from 360px to 1440px.

### Detailed Subtopics

**First 30 minutes — Theory & Concept**
- Cheap animation properties (`transform`, `opacity`) vs expensive ones (`width`, `top`, `margin`)
- `transition` vs `@keyframes animation` — when to pick which
- Mobile-first: the default targets phones, not the other way around
- `prefers-reduced-motion` and animation accessibility
- `IntersectionObserver` as a replacement for scroll listeners

**Remaining 1.5 hours — Implementation**
- Mobile-first CSS base with progressive `min-width` media queries
- Typewriter hero headline with `@keyframes` + `steps()` + blinking cursor
- Hover-tilt product cards using `transform` + `transition` + `will-change`
- Animated skill bars that fill when scrolled into view (via `IntersectionObserver`)
- Floating back-to-top button with scroll-based visibility + click-spin
- Reduced-motion override using `@media (prefers-reduced-motion: reduce)`
- Observe dropped frames in DevTools Performance tab for a poorly-animated property
- **AI-assisted block:** ask AI to audit all animations and flag anything that animates `width`/`top`

### Tools / Tech Stack / AI Tools
- HTML, CSS, tiny vanilla JS (provided)
- Chrome DevTools (Performance panel, Rendering tab)
- VS Code / Cursor
- Cursor AI / ChatGPT for animation audit + easing suggestions

### By the End of This Workshop, Students Should Be Able To
Add smooth, performant, and accessible animations to any web page — picking the right property to animate, triggering reveals on scroll, and respecting users who prefer reduced motion. They will feel the real difference between animations that delight users and ones that drop frames, and will confidently ship a mobile-first portfolio that looks alive on every device.

---

## Session 4: Slideshow Sprint — Make JavaScript Move

**Level:** Beginner

**Prerequisite:** Comfort with HTML/CSS basics. No prior JS experience required.

**Learning Objective / Outcome:** Learners will build a feature-complete image slideshow app from scratch — with auto-play, manual navigation, keyboard support, and a thumbnail strip — internalizing modern JavaScript fundamentals (ES6+, closures, timers, events) through a visual, instantly-gratifying project.

### Detailed Subtopics

**First 30 minutes — Theory & Concept**
- `var` vs `let` vs `const` and block scope
- Arrow functions, default params, spread/rest operators
- Object and array destructuring
- Closures in plain English (“a function that remembers its birthplace”)
- Timers: `setInterval`, `setTimeout`, `clearInterval` lifecycle
- Event handling basics (`click`, `keydown`) and event object
- Array methods: `map`, `forEach`, `find`, `indexOf`, modulo for circular navigation

**Remaining 1.5 hours — Implementation**
- Set up an image slides array with captions + URLs
- Render slides dynamically into the DOM with `document.createElement`
- Build prev/next buttons with circular index logic (`(i + 1) % slides.length`)
- Add auto-play using `setInterval`, with pause on hover
- Build a play/pause toggle button with proper state
- Add a thumbnail strip — clicking a thumbnail jumps to that slide
- Add keyboard navigation: ← / → arrows + spacebar to toggle play
- Add a smooth crossfade between slides using CSS `opacity` transitions
- Use a closure to encapsulate `currentIndex` state so it’s not global
- **AI-assisted block:** ask AI to refactor timer logic into a reusable class + generate test cases

### Tools / Tech Stack / AI Tools
- Vanilla JavaScript (ES6+), HTML, CSS
- Unsplash free image URLs (or any image list)
- Chrome DevTools Console for state inspection
- Cursor AI / ChatGPT for refactor into class-based structure

### By the End of This Workshop, Students Should Be Able To
Build a polished, interactive web app using only vanilla JavaScript — manipulating the DOM dynamically, managing state through closures, coordinating timers, and wiring up keyboard and mouse events smoothly. Students will feel how modern JavaScript (ES6+, arrow functions, destructuring, array methods) turns a static HTML page into a living application, and will walk away with a slideshow they can proudly put in their portfolio.

---

## Session 5: API Explorer — Build with Live Data

**Level:** Intermediate

**Prerequisite:** Session 4 or equivalent JS comfort. Understanding of objects, arrays, and basic DOM.

**Learning Objective / Outcome:** Learners will build a real-world API-powered dashboard from scratch — fetching live data, handling loading / error / empty states, debouncing input, cancelling stale requests, and persisting history — mastering `async/await` and the fetch API through a genuinely useful tool.

> **Instructor option:** Pick any live public API the batch finds exciting — **Weather** (OpenWeatherMap / Open-Meteo), **YouTube Search** (YouTube Data API v3), or **GitHub User Search**. Concepts and code structure are identical; the data source changes.

### Detailed Subtopics

**First 30 minutes — Theory & Concept**
- Synchronous vs asynchronous JS and the event loop (1-slide intuition)
- Callbacks → Promises → `async/await` evolution
- The Fetch API: headers, status codes, `response.ok`, `response.json()`
- Try/catch for async errors and HTTP error handling
- `AbortController` for cancelling stale requests
- `Promise.all` for parallel API calls
- Debouncing input to avoid API spam
- Keeping API keys out of the client (environment variable briefing)

**Remaining 1.5 hours — Implementation**
- Wire a search input with a 400ms debounce
- Call the chosen API with `fetch` + `async/await`
- Render results into a beautiful card grid
- Handle all 4 UI states: idle, loading, success, error (with distinct visuals)
- Use `AbortController` to cancel a previous request when the user types again
- Fire two parallel API calls (e.g., current + forecast, or search + trending) with `Promise.all`
- Use a browser capability: `navigator.geolocation` (weather use-case) OR an embedded iframe preview (YouTube use-case)
- Save the last 5 searches to `localStorage` and render them as clickable chips
- **AI-assisted block:** paste your `fetchData` function and ask AI to add retry-with-exponential-backoff and review error handling

### Tools / Tech Stack / AI Tools
- Vanilla JavaScript (ES Modules), Fetch API, AbortController
- Any live public API: OpenWeatherMap / Open-Meteo / YouTube Data API v3 / GitHub API
- Chrome DevTools Network tab for inspecting requests/responses
- Cursor AI / ChatGPT for retry-logic scaffolding and error-handling review

### By the End of This Workshop, Students Should Be Able To
Create an interactive web application that integrates with real-world APIs, fetches data from the server, and renders it beautifully in the UI. Students will feel the real power of JavaScript that lets them store data in `localStorage`, access browser capabilities like geolocation, cancel stale requests with `AbortController`, handle real-world network failures gracefully, and debounce user input to respect rate limits — every single pattern they’ll use in any frontend job.

---

## Session 6: Frontend Meets Backend — Build a Real Task Tracker

**Level:** Beginner

**Prerequisite:** Basic Python and JS. Any of Sessions 2/4 is great warm-up.

**Learning Objective / Outcome:** Learners will build a **complete full-stack app**: a FastAPI backend with CRUD endpoints and Pydantic validation, plus a vanilla JS frontend that talks to it. By the end they will have wired HTTP, CORS, validation, and UI state — end-to-end.

### Detailed Subtopics

**First 30 minutes — Theory & Concept**
- Client-server model and HTTP request/response cycle
- REST principles: resources, verbs, status codes
- Pydantic validation at the API boundary (why it matters)
- CORS: what it is and why browsers block your first fetch
- JSON as a contract between frontend and backend
- FastAPI auto-generated Swagger UI as a dev tool

**Remaining 1.5 hours — Implementation**

*Backend (FastAPI):*
- Scaffold FastAPI project, install `fastapi`, `uvicorn`, `pydantic`
- Define `TaskCreate`, `TaskUpdate`, `TaskOut` Pydantic models
- Build endpoints: `POST /tasks`, `GET /tasks`, `GET /tasks/{id}`, `PATCH /tasks/{id}`, `DELETE /tasks/{id}`
- Add in-memory storage (`dict`) with auto-incrementing IDs
- Enable CORS via `CORSMiddleware` for the frontend origin
- Verify every endpoint via Swagger UI at `/docs`

*Frontend (Vanilla JS + HTML/CSS):*
- Build a minimal HTML form + task list
- `fetch()` the backend for GET/POST/PATCH/DELETE operations
- Render tasks live with DOM manipulation
- Show inline loading/error states
- Add a toggle-complete button that PATCHes the task
- Add a delete button that calls DELETE and re-renders

*Integration:*
- Run backend on `localhost:8000`, frontend on `localhost:5500`
- Debug CORS together live
- **AI-assisted block:** ask AI to generate frontend fetch functions from the OpenAPI spec at `/openapi.json`

### Tools / Tech Stack / AI Tools
- Backend: Python 3.11+, FastAPI, Pydantic v2, Uvicorn
- Frontend: Vanilla JS (ES6+), HTML, CSS
- Swagger UI + VS Code Live Server (or Python `http.server`)
- Cursor AI / ChatGPT for generating fetch functions from OpenAPI spec

### By the End of This Workshop, Students Should Be Able To
Build a complete full-stack application end-to-end — a validated REST API on the backend and a vanilla-JS frontend that talks to it over HTTP. Students will feel the whole picture: how JSON flows between a browser and a Python server, why CORS exists (and why it blocks their first fetch), how Pydantic protects their API from bad data, and how Swagger UI turns documentation into a live testing playground. This is the moment “frontend” and “backend” stop being two separate worlds.

---

## Session 7: Data to Backend — Design, Query, Connect

**Level:** Beginner

**Prerequisite:** Session 6 (FastAPI basics). Any SQL exposure is helpful but not required.

**Learning Objective / Outcome:** Learners will take an e-commerce PM brief, design a normalized schema, write working SQL, and then plug it into a FastAPI app via SQLAlchemy — so their Session-6 API is now backed by a real database instead of an in-memory dict.

### Detailed Subtopics

**First 30 minutes — Theory & Concept**
- Entities, relationships, cardinalities (1-1, 1-M, M-M)
- Normalization (1NF / 2NF / 3NF) in plain English
- Primary keys, foreign keys, composite keys, `UNIQUE` / `CHECK` constraints
- JOIN vocabulary (INNER vs LEFT) and when you need each
- ORM vs raw SQL — when each wins
- SQLAlchemy mental model: engine, session, declarative base

**Remaining 1.5 hours — Implementation**

*Part A — Design the schema (30 min)*
- Extract entities from the “MiniKart” brief: customers, products, orders, order_items
- Draft an ER diagram on dbdiagram.io
- Write `schema.sql` with all tables + constraints + indexes
- Seed the DB with realistic data

*Part B — Write SQL queries (20 min)*
- 10 recent orders with customer name (INNER JOIN)
- Customers with zero orders (LEFT JOIN + `IS NULL`)
- Top-selling products (GROUP BY + SUM + ORDER BY + LIMIT)
- Monthly revenue (`strftime` bucketing)

*Part C — Wire to FastAPI via SQLAlchemy (40 min)*
- Install `sqlalchemy` and define `Task` SQLAlchemy model
- Create a `get_db()` dependency using `yield`
- Rewrite Session-6 CRUD endpoints to use the DB session
- Hit `POST /tasks` → see the row appear in SQLite via DB Browser
- **AI-assisted block:** ask AI to translate between raw SQL and SQLAlchemy queries and explain differences

### Tools / Tech Stack / AI Tools
- SQLite (zero-setup), dbdiagram.io for ERD
- SQLAlchemy 2.x ORM, FastAPI
- DB Browser for SQLite / TablePlus (visual inspection)
- Cursor AI / ChatGPT for SQL ↔ SQLAlchemy translation

### By the End of This Workshop, Students Should Be Able To
Design a normalized database schema from a business requirement, write production-quality SQL queries (JOINs, aggregations, CTEs), and connect that schema to a FastAPI backend using SQLAlchemy. Students will feel how a well-designed data model makes every future feature easier to build — and will never again be intimidated by the word “database.” They will leave with a running app that persists real data across restarts.

---

## Session 8: No-Backend Builder — Ship a Realtime App Fast

**Level:** Intermediate

**Prerequisite:** Basic JS + comfort with any database concept. Session 7 helps.

**Learning Objective / Outcome:** Learners will stand up a production-style backend **without writing a backend** — using Supabase for database, authentication, storage, and realtime subscriptions. They will ship a tiny “Realtime Notes” app where changes propagate live across browser tabs.

### Detailed Subtopics

**First 30 minutes — Theory & Concept**
- Backend-as-a-Service (BaaS): what it is, when to reach for it
- Supabase’s four pillars: **Postgres DB**, **Auth**, **Storage**, **Realtime**
- Row Level Security (RLS) — your data security lives in the DB
- Public anon key vs service role key (and where each belongs)
- Supabase Realtime — Postgres logical replication under the hood
- When NOT to use a BaaS (heavy compute, custom business logic, data residency)

**Remaining 1.5 hours — Implementation**
- Create a free Supabase project (2 min)
- Create a `notes` table from the Supabase dashboard with columns + FK to `auth.users`
- Enable **Row Level Security** and write a policy: “users can only see their own notes”
- Install `@supabase/supabase-js` in a vanilla JS app
- Implement **email + password signup and login** using Supabase Auth UI flow
- Build a simple Notes UI: list, create, delete (all via `supabase.from('notes').select()` etc.)
- Subscribe to realtime changes — open 2 tabs and watch changes sync live
- Upload a profile picture to Supabase Storage and display it
- **AI-assisted block:** ask AI to review your RLS policies for common mistakes (missing policies, over-permissive policies)

### Tools / Tech Stack / AI Tools
- Supabase (free tier): Postgres, Auth, Storage, Realtime
- `@supabase/supabase-js` v2 client
- Vanilla JS, HTML, CSS (no framework)
- Cursor AI / ChatGPT for RLS policy review

### By the End of This Workshop, Students Should Be Able To
Ship a realtime, authenticated web application **without writing a single line of backend code**. Students will feel the power of modern BaaS — authenticating users, enforcing row-level security from the database itself, subscribing to live database changes so multiple browser tabs stay in sync, and storing files to cloud storage — all from a tiny vanilla-JS frontend. They will walk away with a genuine “wow, that was fast” moment.

---

## Session 9: Docker Made Useful — Package and Run Anywhere

**Level:** Advanced

**Prerequisite:** Comfort with a terminal and a small Python/FastAPI app. Docker Desktop installed beforehand.

**Learning Objective / Outcome:** Learners will feel **why Docker exists**, learn every core command and concept (image, container, port, volume, Docker Hub), dockerize a simple FastAPI backend, prove that **the app runs even without Python installed on the machine**, push their image to Docker Hub, and finally orchestrate a 2-service app with `docker-compose` — publishing that to Docker Hub too.

### Detailed Subtopics

**First 30 minutes — Theory & Concept**

*The pain Docker solves*
- “It works on my machine” — the single most common team problem
- Dev, staging, and prod drifting apart over time
- Why installing 12 dependencies on every new machine is not scalable

*The core analogies (keep these in the slides)*
- **Image** = a frozen snapshot / recipe of your app + everything it needs (Python, libraries, code)
- **Container** = a live instance of that image (the cooked dish from the recipe)
- **Dockerfile** = the recipe itself (the steps to build the image)
- **Docker Hub** = GitHub for Docker images — pull public ones, push yours
- **Port mapping** (`-p 8000:8000`) = phone extension connecting the outside world to your container
- **Volume** = a shared folder between host and container (for persistent data / logs)

*The commands you will use today*
- `docker --version`
- `docker pull <image>` — download an image from Docker Hub
- `docker images` — list local images
- `docker run <image>` — start a new container
- `docker run -p host:container <image>` — with port mapping
- `docker run -d` (detached) / `docker run --rm` (auto-clean)
- `docker ps` / `docker ps -a` — running / all containers
- `docker stop <id>` / `docker rm <id>` / `docker rmi <image>`
- `docker logs <id>` / `docker exec -it <id> bash`
- `docker build -t <name> .` — build an image from a Dockerfile
- `docker tag <image> <user>/<name>:<tag>`
- `docker login` / `docker push` — publish to Docker Hub
- `docker compose up` / `docker compose down`

*Dockerfile anatomy*
- `FROM`, `WORKDIR`, `COPY`, `RUN`, `EXPOSE`, `CMD`

*When one container isn’t enough*
- `docker-compose` — run multiple linked services with a single command

**Remaining 1.5 hours — Implementation**

*Part A — Taste Docker (no writing, just running) — 10 min*
- `docker pull hello-world` → `docker run hello-world` (first container!)
- `docker pull python:3.11-slim`
- `docker run --rm -it python:3.11-slim python --version` → running Python from a container
- `docker images`, `docker ps`, `docker ps -a` — explore state

*Part B — Dockerize a simple FastAPI backend — 25 min*
- Create a minimal FastAPI app (one `GET /` route returning a hello JSON) and a `requirements.txt` with FastAPI + Uvicorn
- Write a simple **Dockerfile** using `FROM python:3.11-slim`, `WORKDIR`, `COPY`, `RUN pip install -r requirements.txt`, `EXPOSE 8000`, and a `CMD` that starts Uvicorn on `0.0.0.0:8000`
- Build the image: `docker build -t my-api .`
- Run the container: `docker run -p 8000:8000 my-api`
- Hit `http://localhost:8000` → it works
- Inspect live state with `docker ps` and `docker logs <id>`

*Part C — The “no Python” magic demo — 15 min*
- Stop the container: `docker stop <id>`
- **Uninstall Python** from the host machine (or deactivate the venv and remove Python from PATH — instructor picks the safest demo for the batch)
- Run `python --version` → **command not found**
- Now run: `docker run -p 8000:8000 my-api` → **the app still works perfectly**
- Teaching beat: the image ships its own Python, its own dependencies, and its own code. The host machine doesn’t need any of them.
- (Alternative demo: ask a classmate without Python installed to `docker pull` + `docker run` your image — same effect)

*Part D — Push to Docker Hub — 15 min*
- Create a free Docker Hub account
- `docker login`
- `docker tag my-api <your-username>/my-api:v1`
- `docker push <your-username>/my-api:v1`
- Verify the image appears at `hub.docker.com/r/<your-username>/my-api`
- On a fresh terminal (or another machine): `docker pull <your-username>/my-api:v1` → `docker run -p 8000:8000 <your-username>/my-api:v1`
- Same code, different computer, zero installation.

*Part E — Multi-service with docker-compose — 20 min*
- Real-world apps need more than one container — let’s add Postgres
- Write a `docker-compose.yml` that defines two services:
  - An `api` service built from the current Dockerfile, publishing port `8000`, with a `DATABASE_URL` pointing to hostname `db`
  - A `db` service using the official `postgres:16` image, with password + database name via environment variables, and a named volume for persistence
- Bring everything up with a single command: `docker compose up --build`
- Notice: the API reaches the DB simply at hostname `db` — Docker provides service discovery for free
- Tear everything down cleanly with `docker compose down`
- (Optional) Push the updated API image to Docker Hub with a `v2` tag

*AI-assisted block*
- Paste your Dockerfile and ask AI to suggest 2–3 size / security improvements
- Ask AI to explain any command output you don’t understand

### Tools / Tech Stack / AI Tools
- Docker Desktop / Docker Engine + `docker compose`
- FastAPI + Uvicorn (minimal backend target)
- Postgres (official image from Docker Hub, for the compose demo)
- Docker Hub (free account)
- Cursor AI / ChatGPT for Dockerfile review + command explanation

### By the End of This Workshop, Students Should Be Able To
Dockerize any Python application, run it on a machine that doesn’t even have Python installed, and share it with the world via Docker Hub with a single `docker push`. Students will **feel** the real power of containers — an image is a portable, self-contained snapshot of your entire app — and will intuitively understand images, containers, ports, volumes, and Docker Hub through real commands, not slides. They will walk away knowing that “works on my machine” is no longer an excuse.

---

## Session 10: Push to Production — Automate Testing and Deploys

**Level:** Beginner

**Prerequisite:** A GitHub account + any small repo. No prior CI/CD experience.

**Learning Objective / Outcome:** Learners will author **two concrete GitHub Actions workflows** end-to-end: one that **auto-deploys a static frontend (HTML/CSS)** to GitHub Pages on every push to `main`, and one that **runs backend tests** on every push / PR and blocks merging on failure. Focus is on the `.yml`, not on code.

> The app code is intentionally minimal. The star of this session is the workflow file.

### Detailed Subtopics

**First 30 minutes — Theory & Concept**
- CI vs CD vs Continuous Deployment
- Anatomy of a GitHub Actions workflow: `on`, `jobs`, `steps`, `runs-on`
- Event triggers: `push`, `pull_request`, `workflow_dispatch`
- Actions marketplace — reusable building blocks (`actions/checkout`, `actions/setup-python`, `actions/deploy-pages`)
- Secrets, environments, branch protection rules
- Status badges and PR checks

**Remaining 1.5 hours — Implementation**

*Workflow 1 — Auto-Deploy Frontend to GitHub Pages (~35 min)*
- Create a tiny `index.html` + `styles.css` (10 lines each)
- Enable GitHub Pages on the repo (source: GitHub Actions)
- Write `.github/workflows/deploy-frontend.yml`:
  - Trigger on `push` to `main`
  - Use `actions/checkout` → `actions/upload-pages-artifact` → `actions/deploy-pages`
- Push a change to `index.html` → watch the workflow run → see the live site update

*Workflow 2 — Test Backend on Every Push (~35 min)*
- Ship a 20-line FastAPI app + 5 pytest tests (`tests/test_health.py`)
- Write `.github/workflows/test-backend.yml`:
  - Trigger on `push` + `pull_request`
  - Matrix over Python `3.10` / `3.11` / `3.12`
  - Steps: checkout → setup-python → install deps → run `pytest`
- Intentionally break a test, push → watch the red X appear on the PR
- Enable **branch protection** requiring this check to pass before merge
- Add a README status badge linking to the workflow

*AI-assisted block*
- Paste a failing workflow log and ask AI to diagnose the failure step-by-step

### Tools / Tech Stack / AI Tools
- GitHub Actions (YAML workflows)
- GitHub Pages (free static hosting)
- Python 3.x + Pytest (backend test target)
- Cursor AI / ChatGPT for workflow drafting + failure diagnosis

### By the End of This Workshop, Students Should Be Able To
Write GitHub Actions workflows that auto-deploy a static site to GitHub Pages on every push, and run backend tests automatically on every pull request — blocking merges when tests fail. Students will feel how CI/CD turns their Git repository into a self-testing, self-deploying product. No more manual deploys, no more “the build broke on my teammate’s PR” — a green checkmark means shippable, a red X means don’t merge.

---

## Session 11: Login to CRUD — Build Secure User Flows

**Level:** Beginner

**Prerequisite:** Basic FastAPI + JS (Sessions 6). Helpful: Session 2 or 4 for DOM muscle memory.

**Learning Objective / Outcome:** Learners will ship a **complete auth flow end-to-end**: a FastAPI backend with signup, login, and JWT-protected endpoints, **plus** a minimal vanilla-JS frontend (signup page, login page, Todo CRUD) that stores the token and calls protected endpoints. Frontend scaffolding is **AI-assisted** so the spotlight stays on auth concepts.

### Detailed Subtopics

**First 30 minutes — Theory & Concept**
- Authentication vs Authorization in plain English
- Password hashing (bcrypt) — never store plaintext
- JSON Web Tokens: structure (header.payload.signature), signing, expiry
- Stateless vs stateful sessions — why JWT wins for APIs
- Where tokens live (header, cookie, localStorage) and trade-offs
- `Authorization: Bearer <token>` flow
- Common mistakes: long-lived tokens, no HTTPS, leaking secret keys

**Remaining 1.5 hours — Implementation**

*Backend (FastAPI) — 50 min*
- Add a `users` table (email + hashed_password)
- `POST /auth/signup` — hash password with `passlib[bcrypt]`
- `POST /auth/login` — verify password, return signed JWT via `python-jose`
- Write `get_current_user` dependency that validates Bearer tokens
- Protect `/todos` endpoints with `Depends(get_current_user)` — users only see their own todos
- Test everything via Swagger UI with the Authorize button

*Frontend (Vanilla JS, AI-assisted) — 40 min*
- Prompt AI to generate 3 pages: `signup.html`, `login.html`, `todos.html`
- Wire login form → `POST /auth/login` → store JWT in `localStorage`
- Add `Authorization: Bearer ${token}` header to every fetch from `todos.html`
- Implement Todo CRUD calls (add / list / toggle / delete)
- Add logout button that clears the token and redirects
- Handle 401 errors → redirect to login

*AI-assisted block*
- Ask AI to review the backend for auth mistakes (token lifetime, missing rate limits, CSRF exposure)

### Tools / Tech Stack / AI Tools
- Backend: FastAPI, `passlib[bcrypt]`, `python-jose`, SQLAlchemy (from Session 7)
- Frontend: Vanilla JS, HTML, CSS — generated with AI assistance
- Swagger UI for API testing
- Cursor AI / ChatGPT to generate the frontend pages + review auth for mistakes

### By the End of This Workshop, Students Should Be Able To
Build a complete authenticated full-stack application — with secure signup, login, and protected CRUD endpoints using JWTs. Students will feel the complete auth flow end-to-end: how passwords are safely hashed with bcrypt, how tokens are signed and verified, how the browser attaches them to every request, and how row-level authorization keeps one user’s data private from another’s. They will leave knowing exactly what happens when they click “Login” on any modern web app.

---

## Session 12: Live Chat Lab — Messages That Appear Instantly

**Level:** Beginner

**Prerequisite:** Basic FastAPI (Session 6) + basic DOM (Session 2).

**Learning Objective / Outcome:** Learners will build a working real-time chat application — **backend and frontend together** — where multiple browser tabs see messages instantly. Both sides are implemented in the same session so learners see the full picture.

### Detailed Subtopics

**First 30 minutes — Theory & Concept**
- HTTP (stateless request/response) vs WebSockets (persistent full-duplex)
- The WebSocket handshake: HTTP upgrade → long-lived connection
- When to choose WebSockets vs SSE vs long polling
- Message framing: JSON as the transport
- Connection lifecycle: `onopen`, `onmessage`, `onclose`, `onerror`
- Fan-out patterns: broadcast, direct, room-based
- Basic reconnection strategy

**Remaining 1.5 hours — Implementation**

*Backend (FastAPI) — 40 min*
- Set up a `WebSocket` endpoint at `/ws/{username}`
- Build a `ConnectionManager` class that tracks all active clients
- On `connect`: add to active list, broadcast “user joined”
- On `receive`: broadcast the message to all connected users
- On `disconnect`: remove + broadcast “user left”
- Handle malformed JSON / disconnect gracefully

*Frontend (Vanilla JS) — 40 min*
- Ship a simple `chat.html`: username input → enter chat → message input + send button + messages list
- On enter: open `new WebSocket('ws://localhost:8000/ws/' + username)`
- Hook `onmessage` → append message to the UI
- Hook send button → `socket.send(JSON.stringify({text, from: username}))`
- Style the current user’s messages differently from others
- Open **3 browser tabs** simultaneously — watch messages flow in real time

*AI-assisted block (10 min)*
- Ask AI to harden the backend for malformed payloads + suggest a message schema

### Tools / Tech Stack / AI Tools
- Backend: FastAPI + `WebSocket`, Uvicorn
- Frontend: Vanilla JS (browser `WebSocket` API), HTML, CSS
- Chrome DevTools Network tab → WS frame inspection
- Cursor AI / ChatGPT for payload validation + reconnect logic

### By the End of This Workshop, Students Should Be Able To
Build a real-time chat application where messages sync instantly across multiple browser tabs. Students will feel the difference between traditional HTTP (ask → wait → answer) and a persistent WebSocket connection (always on, messages flow both ways). They will understand server-side connection management, broadcast patterns, and client reconnection logic — the same primitives that power every modern chat, collaborative tool, and live dashboard on the internet.

---

## Session 13: Resolve Server Load — Cache, Queue, Batch

**Level:** Advanced

**Prerequisite:** Comfort with FastAPI (Session 6) and Python. Session 7 (DB) helpful.

**Learning Objective / Outcome:** Learners will add **Redis-backed caching and batch-update** layers to a FastAPI app and measure the before/after latency — understanding when to cache, how to invalidate, how Redis fits into a real backend, and how to turn “write on every request” into “buffer and flush in batches”.

### Detailed Subtopics

**First 30 minutes — Theory & Concept**
- Why cache: the 80/20 rule — most reads hit a small hot set
- Cache types: in-process (LRU/TTL) vs external (Redis) — pros, cons, when to use each
- What Redis actually is: an in-memory key-value store that sits between your API and DB
- Core Redis data types you’ll touch today: `STRING`, `HASH`, `INCR`, `EXPIRE`
- Cache-aside pattern: read cache → miss → hit DB → populate cache → serve next time
- Cache invalidation — one of the two hard things in computer science
- TTL vs explicit invalidation (when each wins)
- Batch updates: coalescing many small writes into one big write
- Write-behind vs write-through vs write-around
- How to measure: p50/p95 latency, requests per second

**Remaining 1.5 hours — Implementation**

*Part A — In-Process Caching Baseline (~25 min)*
- Add a GET `/products/{id}` endpoint that hits the DB
- Use `@functools.lru_cache` on the DB fetcher and benchmark with `ab` or `hey`
- Build a tiny `TTLCache` class (`set`, `get`, `expire_at`) to understand what a cache really is
- Note the limits: lost on restart, not shared across workers/replicas → motivation for Redis

*Part B — Caching with Redis (~35 min)*
- Run Redis locally via a single `docker run` command (tie back to Session 9)
- Install `redis-py` and connect from FastAPI (`redis.asyncio.Redis`)
- Implement **cache-aside** on `/products/{id}`:
  - Build a key convention (`product:{id}`)
  - On read: `GET` from Redis → if miss, query DB, then `SET` with `EX` (TTL)
  - On write (`PATCH /products/{id}`): update DB, then `DEL` the key (explicit invalidation)
- Add a `/health/cache` endpoint that returns Redis hit/miss counters using `INCR`
- Benchmark cold vs warm cache with `hey` / `ab` and observe p50/p95 drop
- Inspect keys live with `redis-cli` (`KEYS *`, `TTL product:1`, `GET product:1`)

*Part C — Batch Updates with Redis (~30 min)*
- Simulate a “page-view counter” that receives high-frequency hits
- Naive version: one DB write per request → measure the crush
- Smarter version using Redis as a write buffer:
  - Each request does `INCR views:{page_id}` in Redis (O(1), in-memory)
  - An `asyncio` background task flushes counters to the DB every 2 seconds (or every N events)
- Compare DB load before vs after — huge difference
- Discuss failure modes: server crash mid-flush = small data loss (fine for counters, not for money)

*AI-assisted block*
- Ask AI to review your Redis key schema for collisions and suggest a TTL strategy per endpoint
- Use AI to generate a small load-test script and interpret the latency histogram

### Tools / Tech Stack / AI Tools
- Python 3.11+, FastAPI, `functools.lru_cache`, `asyncio`
- **Redis** (run via Docker), `redis-py` / `redis.asyncio`
- `redis-cli` for live inspection
- `hey` or `ab` (Apache Bench) for load testing
- Cursor AI / ChatGPT for cache-key review + TTL strategy

### By the End of This Workshop, Students Should Be Able To
Make a slow API significantly faster by putting **Redis in front of the database** as a cache-aside layer with proper TTLs and explicit invalidation, and by batching high-frequency writes through Redis before flushing them to the DB. Students will feel the power of these patterns by measuring real p50/p95 latency drops with load-test tools, inspect live keys via `redis-cli`, and walk away knowing how real production systems absorb traffic spikes without melting the database — plus exactly when caching is worth the added complexity and when it isn’t.

---

## Session 14: Mongo Made Simple — NoSQL DB, a Different World

**Level:** Beginner

**Prerequisite:** Basic Python + FastAPI (Session 6 ideal). No MongoDB experience required.

**Learning Objective / Outcome:** Learners will stand up a **MongoDB** database, perform CRUD operations visually using **MongoDB Compass**, and then wire the same collection to a FastAPI + Pydantic backend for programmatic CRUD — gaining intuition for when a document store beats a relational one.

### Detailed Subtopics

**First 30 minutes — Theory & Concept**
- Relational vs Document databases — when to use NoSQL vs SQL
- MongoDB vocabulary: **database → collection → document → field**
- BSON (Binary JSON) vs JSON: what changes and why
- `_id` and `ObjectId` — how Mongo auto-generates primary keys
- The four CRUD operations: `insertOne`, `find`, `updateOne`, `deleteOne`
- Embedded documents vs references (when to nest, when to link)
- Schemaless ≠ schema-free: why Pydantic still matters
- Indexes in MongoDB (1-slide intro)

**Remaining 1.5 hours — Implementation**

*Part A — CRUD Visually in MongoDB Compass (~25 min)*
- Install MongoDB locally OR create a free MongoDB Atlas cluster (3 min setup)
- Connect Compass to the instance
- Create a `bookstore` database with a `books` collection
- Insert 5 sample book documents via the Compass GUI (no code)
- Run find queries with filters: `{ "author": "R.K. Narayan" }`
- Update a document via Compass UI
- Delete a document via Compass UI
- Peek at the underlying BSON

*Part B — Same CRUD via FastAPI + Pydantic + PyMongo (~55 min)*
- `pip install fastapi uvicorn pymongo pydantic`
- Create a `main.py`, connect to MongoDB via `MongoClient`
- Define Pydantic `BookCreate` and `BookOut` models (with `_id` as string)
- Build all 5 endpoints:
  - `POST /books` → `collection.insert_one(...)`
  - `GET /books` → `collection.find()`
  - `GET /books/{id}` → `collection.find_one({"_id": ObjectId(id)})`
  - `PATCH /books/{id}` → `collection.update_one(...)`
  - `DELETE /books/{id}` → `collection.delete_one(...)`
- Convert Mongo `_id` (ObjectId) ↔ string in Pydantic response models
- Test every endpoint via Swagger UI at `/docs`
- Add a filter: `GET /books?author=xxx`

*Part C — Indexing & Observability (~10 min)*
- Create an index on the `author` field from Compass
- Re-run the same filter query and compare using `explain()`
- Discuss when to add indexes vs when they hurt

*AI-assisted block*
- Ask AI which fields should be indexed based on your most common queries

### Tools / Tech Stack / AI Tools
- MongoDB Community Server OR MongoDB Atlas (free tier)
- MongoDB Compass (visual GUI)
- Python 3.11+, FastAPI, Pydantic v2, PyMongo
- Swagger UI for API testing
- Cursor AI / ChatGPT for index strategy + schema suggestions

### By the End of This Workshop, Students Should Be Able To
Model data for a document database, perform CRUD operations both visually (MongoDB Compass) and programmatically (FastAPI + Pydantic + PyMongo), and confidently decide when NoSQL is the right tool for a project versus a relational database. Students will feel the flexibility of schemaless modeling — fields can differ per document, nested objects are first-class — and understand how a document store differs fundamentally from tables-and-rows SQL.

---

## Session 15: Think Like a Solver — Build a Math Evaluator

**Level:** Intermediate

**Prerequisite:** Python functions, basic arrays, `if/else`. Any level of DSA comfort is fine — the session builds intuition from scratch.

**Learning Objective / Outcome:** Learners will build a working arithmetic expression evaluator (with parentheses and operator precedence) **two different ways** — via recursive descent and via an explicit stack (shunting-yard + RPN) — and see firsthand that recursion and stacks are the same idea in different shapes.

### Detailed Subtopics

**First 30 minutes — Theory & Concept**
- The OS call stack: every recursive call is a frame push
- Explicit stacks using a Python list (`append` / `pop` are O(1))
- Recursion’s three parts: base case, recursive case, progress toward base
- Operator precedence expressed via function call order
- Shunting-yard algorithm in intuition form
- When to pick recursion vs an explicit stack
- Time and space complexity intuition (O(n) vs O(n²) in plain language)

**Remaining 1.5 hours — Implementation**
- Tokenizer: split `"3 + 4 * (2 - 1)"` into a list of tokens
- Recursive descent: `parse_expr` → `parse_term` → `parse_factor`
- Watch how precedence falls out of the function-call hierarchy
- Write an explicit-stack version using shunting-yard → RPN → evaluator
- Verify both versions return identical results on 5+ inputs
- Add graceful error messages for malformed input (`"3 + * 2"`)
- Handle negative numbers and the modulo operator
- (Stretch) add right-associative `^` for power
- (Stretch) write 8 pytest test cases covering edge cases
- **AI-assisted block:** ask AI to compare your two implementations for readability, memory usage, and extensibility

### Tools / Tech Stack / AI Tools
- Python 3.11+, Pytest
- VS Code / Cursor
- Cursor AI / ChatGPT for approach comparison + edge-case generation

### By the End of This Workshop, Students Should Be Able To
Build a working arithmetic expression evaluator using two completely different approaches — recursion and explicit stacks — and explain exactly why both produce the same result. Students will feel the deep connection between recursion and stacks (they are the same idea in different shapes), and will walk away with the confidence to break down any parsing, tree-walking, or nested-structure problem into small, well-defined functions. This is the single session that most separates “I can write loops” from “I can write a real program.”

---

## Difficulty Distribution

Matches the guideline split of **10 / 3 / 2**:

| Level | Count | Sessions |
|---|---|---|
| Beginner | 10 | 1, 2, 3, 4, 6, 7, 10, 11, 12, 14 |
| Intermediate | 3 | 5, 8, 15 |
| Advanced | 2 | 9, 13 |

Every session is independently executable, follows the **30-min theory + 1.5-hr implementation** structure, integrates AI assistants (Cursor / ChatGPT) as a practical pair-programmer, and closes with a clear student-facing outcome statement.
