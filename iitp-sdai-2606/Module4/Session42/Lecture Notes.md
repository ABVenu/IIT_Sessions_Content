# Claude Code for AI Development

You already know how to **brief a model** (roles, constraints, JSON) and how to **call LLM APIs** from FastAPI with keys on the server. You also used **browser-based** assistants during GenAI labs to draft **`campus_api`** routes. The gap is **working inside your real project folder**—small steps, file context, and **diffs you review** before you run **`uvicorn`**.

**Claude Code** is a **command-line** coding assistant that treats your repository as the workspace. This lesson covers **installation**, **CLI basics**, an **iterative workflow**, and **debugging prompts**. It does **not** design capstone architecture—that blueprint work comes **next**.

## What you will learn in this lesson

- **Installation and setup** — getting Claude Code running safely on your machine
- **CLI basics** — starting in the correct directory and scoped tasks
- **Development workflow** — thin slices: change → run → verify → commit
- **Debugging** — feeding tracebacks, file paths, and constraints
- **Prompting habits** — reusing discipline from earlier lessons inside the terminal
- **Hands-on** — a repeatable loop on a practice bug in a small repo

Connecting idea: FastAPI integration moved AI to the **server**; Claude Code moves AI to the **editor’s chair**—with you still holding the red pen.

---

## What Claude Code is (and is not)

- **Official Definition:** **Claude Code** is an agentic CLI tool that reads project files, proposes edits, runs commands (when allowed), and iterates with you in a terminal session.
- **In Simple Words:** A pair programmer that can **see your folders**, not only a chat box you paste into.
- **Real-Life Example:** A workshop **apprentice** with a tool belt—fetches clamps and holds boards; **you** check every joint.

| Browser chat | Claude Code |
| --- | --- |
| You paste snippets manually | Tool **reads paths** you point to |
| Easy to lose project context | Works from **repo root** |
| Suggests big rewrites | Can propose **patch-sized** edits |
| You copy changes by hand | You **review diffs** then accept |

**Is not:** A replacement for reading tracebacks, Git basics, or course rubrics.

**Common mistake:** Asking “fix my entire capstone” and accepting file renames you never requested.

### Activity — rewrite one vague ask

Change “make login work” into a prompt with **file path**, **observed error**, **expected behaviour**, and **constraint** (“do not add new npm packages”).

---

## Installation and configuration

- **Official Definition:** **Installation** means installing the Claude Code CLI package and authenticating with your Anthropic account per vendor docs.
- **In Simple Words:** Download the tool, sign in once, keep credentials out of Git.
- **Real-Life Example:** Installing UPI app and linking bank—once setup is right, daily use is fast.

**Typical setup flow (check official docs for updates)**

| Step | Action |
| --- | --- |
| 1 | Install CLI via vendor instructions (npm/global installer or packaged binary) |
| 2 | Run login / API setup command shown in docs |
| 3 | Verify version command prints a number |
| 4 | Open terminal in **project root** (where `.git` or `main.py` lives) |

**Environment hygiene**

| Item | Rule |
| --- | --- |
| **`.env`** | Never paste contents into prompts |
| **API keys** | Stay in env files; tool should read code, not secrets |
| **`.gitignore`** | Must list `.env`, `node_modules`, `.venv` |

**Need:** Same security model as **`GEMINI_API_KEY`**—the assistant is not a vault.

**Common doubt:** “Can it run any shell command?” — Depends on settings; **you** approve risky commands in class demos.

Connecting idea: After install, you **start a session** in the repo you are actually shipping.

---

## CLI basics and project initialization

- **Official Definition:** The **CLI** (command-line interface) accepts text commands and natural-language tasks in a terminal attached to a working directory.
- **In Simple Words:** You talk to the tool where your code already lives.
- **Real-Life Example:** Calling the electrician **inside your flat**, not describing wires from a café.

**Before you type a task**

| Check | Why |
| --- | --- |
| `pwd` shows project root | Relative paths resolve correctly |
| Virtualenv active for Python | Suggested installs match your environment |
| Server not secretly running old code | Restart **`uvicorn`** after backend edits |

**Useful starter commands (names may vary by version—read `help` output)**

```bash
claude --help  # List subcommands and flags for your installed version
claude  # Start interactive session in current directory
```

**Project context tips**

- Mention **stack**: FastAPI, SQLAlchemy 2, vanilla JS—matches your course.
- Point to **one file** per task when possible: `routes/students.py`.
- Say what **must not change**: “Do not remove CORS middleware.”

**Initialization mindset:** You are not “creating a new project” each time—you **anchor** the tool to an existing repo (capstone or **`campus_api`** fork).

### Activity — inventory three files

Without opening Claude, list three files you would attach to a task “add query param filter on list students.” Paths only.

---

## Iterative development workflow

- **Official Definition:** **Iterative development** repeats small plan → edit → test → refine cycles until acceptance criteria pass.
- **In Simple Words:** Fix one window before painting the whole building.
- **Real-Life Example:** Exam prep one chapter per day with mock questions—not cramming the book overnight.

**The LOOP you will use in class**

| Letter | Meaning | Your action |
| --- | --- | --- |
| **L** | Limit scope | One route, one bug, one UI handler |
| **O** | Observe | Run app, read console/network |
| **O** | Offer context | Error text + file + constraint prompt |
| **P** | Patch review | Read diff line by line |

**Good task sizes**

| Too big | Right size |
| --- | --- |
| “Build capstone backend” | “Add `GET /students?city=` using existing `select()` pattern” |
| “Fix all lint” | “Fix NameError in `get_db` import” |
| “Upgrade every dependency” | “Pin httpx version to course requirements” |

**Git habits (same as human teammates)**

- Commit after each working slice.
- Message mentions **what** changed, not “AI stuff.”
- If diff touches files you did not mention, **stop** and ask why.

**Integrated quality gate:** Run **`/docs`** or browser test **before** you accept the next suggestion.

Connecting idea: When something breaks, you switch from LOOP to **debug mode** prompts.

---

## Debugging with Claude Code

- **Official Definition:** **Debugging** is isolating why program behaviour differs from expectation by inspecting errors, state, and recent changes.
- **In Simple Words:** Follow the smoke to the spark.
- **Real-Life Example:** Fuse trips → you check the geyser, not repaint the house.

**Debug prompt template (copy and fill)**

```text
Role: FastAPI debugger for our course stack.
Context: Branch main, Python 3.11, SQLAlchemy 2 style select().
File: app/routes/students.py (only edit this file unless I approve).
Error (full traceback):
(paste here)
What I tried: restarted uvicorn, same error.
Task: Explain root cause in 3 bullets, then propose minimal fix.
Format: Explanation bullets, then patched function only.
Constraints: No new dependencies. Keep StudentOut schema unchanged.
```

**What to include**

| Include | Skip |
| --- | --- |
| Full traceback | Entire 2 MB log file |
| HTTP method + URL | “it doesn't work” |
| Expected vs actual | Blaming the model |

**What to do when the tool is wrong**

- Reject the diff.
- Narrow the file scope.
- Reproduce manually in Python shell or `/docs`.
- Compare with working **`campus_api`** pattern from memory.

**Common errors**

| Tool behaviour | Your response |
| --- | --- |
| Invented package | Reject; cite `requirements.txt` |
| Deleted CORS | Reject; add constraint |
| Renamed models | Reject; ask for minimal diff |

### Activity — traceback drill

Given `ImportError: cannot import name 'get_db'`, write the **smallest** question that still includes file path and line number.

---

## Prompting best practices inside the terminal

You already use **role, context, task, format, constraints** in prompt engineering. Claude Code rewards the same blocks—just shorter and **path-specific**.

| Block | Terminal-friendly example |
| --- | --- |
| Role | “You are a cautious FastAPI tutor.” |
| Context | “`list_students` returns 500 when `city` query missing.” |
| Task | “Make `city` optional; return all if omitted.” |
| Format | “Return only the updated function.” |
| Constraints | “Use `select(Student)` not legacy `.query`.” |

**Few-shot in repo context:** Point to a **working** sibling function: “Match error handling style of `get_student_by_id`.”

**Chain-of-thought:** Ask for **bullets first**, code second—reduces blind edits.

**Temperature analogy:** Urgent bugfix → demand **minimal** change; exploration → ask for **two options** with trade-offs, still no auto-merge.

---

## Full walkthrough: fix a broken fetch URL (vanilla JS)

**Scenario (practice repo):** Login button never calls API because `API_BASE` is wrong.

**`login.js` (before)**

```javascript
const API_BASE = "http://localhost:8000";  // Wrong port — backend runs on 8010
const form = document.querySelector("#login-form");  // Grab form element
form.addEventListener("submit", async (event) => {  // Listen for submit
  event.preventDefault();  // Stop page reload
  const email = document.querySelector("#email").value;  // Read email input
  const password = document.querySelector("#password").value;  // Read password input
  const response = await fetch(`${API_BASE}/auth/login`, {  // Call backend
    method: "POST",  // JSON login
    headers: { "Content-Type": "application/json" },  // JSON header
    body: JSON.stringify({ email, password }),  // Body payload
  });  // End fetch options
  const data = await response.json();  // Parse JSON response
  console.log("login result", data);  // Debug log
});  // End listener
```

**Prompt you would type in Claude Code**

```text
File: frontend/login.js
Bug: Network error on submit — backend is at http://127.0.0.1:8010 per README.
Task: Fix API_BASE only; keep handler structure.
Constraint: Do not add frameworks.
```

**`login.js` (after)**

```javascript
const API_BASE = "http://127.0.0.1:8010";  // Match uvicorn port from README
const form = document.querySelector("#login-form");  // Grab form element
form.addEventListener("submit", async (event) => {  // Listen for submit
  event.preventDefault();  // Stop page reload
  const email = document.querySelector("#email").value;  // Read email input
  const password = document.querySelector("#password").value;  // Read password input
  const response = await fetch(`${API_BASE}/auth/login`, {  // Call backend
    method: "POST",  // JSON login
    headers: { "Content-Type": "application/json" },  // JSON header
    body: JSON.stringify({ email, password }),  // Body payload
  });  // End fetch options
  if (!response.ok) {  // Handle non-2xx responses
    console.error("login failed", response.status);  // Visible status for debugging
    return;  // Stop happy-path logic
  }  // End error guard
  const data = await response.json();  // Parse JSON response
  console.log("login result", data);  // Debug log
});  // End listener
```

**How the code works**

- Port mismatch was the root bug—classic integration issue.
- Added **`response.ok`** guard so future errors are visible.
- You still **run** the page and watch Network tab—tool does not replace testing.

---

## Safety and academic integrity

| Rule | Reason |
| --- | --- |
| You must explain every merged change | Interviews ask **why**, not **who typed** |
| No uploading graded solutions to public repos | Plagiarism and key leaks |
| Cite when whole functions are AI-assisted | Team transparency |

**Claude Code + LLM APIs:** Keys for production models stay in **backend `.env`**, not in terminal transcripts you share.

---

## Working with FastAPI repos (course pattern)

| Task type | Prompt hint |
| --- | --- |
| New route | “Match existing router style in `main.py`” |
| Pydantic model | “Mirror `StudentOut` naming; read-only fields documented” |
| DB session | “Use `Depends(get_db)` pattern already in project” |
| AI route | “Do not move `GEMINI_API_KEY` to frontend” |

**Run commands you should type yourself after edits**

```bash
source .venv/bin/activate  # Activate virtual environment
uvicorn main:app --reload --port 8010  # Start API for manual test
```

**OpenAPI check:** Visit `/docs` and hit the route the tool changed—screenshot for mentor review if required.

**Common mistake:** Letting the tool add **global exception handlers** you do not understand—reject and ask for explanation bullets first.

### Activity — constraint list

Write five **must-not** rules for your capstone repo (examples: no deleting tests, no new ORM, no removing CORS). Keep them in `CONTRIBUTING.md` for your team.

---

## Reviewing diffs like a pull request

| Diff signal | Question to ask |
| --- | --- |
| New import | Is package already in `requirements.txt`? |
| Deleted file | Was it intentional? |
| Reformatted entire file | Can you accept noise vs real fix? |
| Changed port/env | Does README still match? |

**Accept criteria before merge**

- App starts without traceback.
- Happy path tested in browser or `/docs`.
- You can explain the change in **two sentences** aloud.

**Integrated teamwork:** If two teammates use AI tools, **pull before prompt** so context matches Git.

---

## Prompt library (save in your notes)

**Explain file**

```text
Explain app/dependencies.py in plain English for a beginner.
Format: bullet per function, max 12 words each.
Do not suggest edits.
```

**Add feature**

```text
Add GET /health/details returning {"db":"ok"} using existing engine.
Touch only routes/health.py and include router in main.py.
```

**Refactor safely**

```text
Rename variable student_list to students in list_students only.
No behaviour change. Show diff hunks only.
```

Copy these patterns during capstone weeks—swap paths to match your tree.

---

## Troubleshooting install and auth

| Symptom | Check |
| --- | --- |
| Command not found | PATH / reinstall CLI |
| Auth expired | Re-run login command from docs |
| Wrong workspace | `cd` to repo root |
| EACCES errors | Avoid sudo npm; fix folder permissions |

**Never** paste OAuth tokens into class Slack—rotate if leaked.

---

## Session rhythm for capstone weeks

| Phase | Your focus | Tool role |
| --- | --- | --- |
| Read error | Understand traceback | Ask for explanation only |
| Plan fix | Decide smallest change | Ask for options A/B |
| Apply patch | Review diff | Accept or reject |
| Verify | Run server/tests | You drive commands |
| Commit | Write message | Tool does not commit for you unless allowed |

**Pomodoro-friendly slice:** 25 minutes on **one function**, not one subsystem.

**Pairing with classmates:** One person operates terminal; other reads diff aloud—catches silly deletes.

### Activity — rejection practice

Intentionally **reject** one AI suggestion in practice and rewrite the prompt with tighter **Constraints**. Note how the second diff shrinks.

---

## Documenting what the tool did

| Field | Example |
| --- | --- |
| Task | “Fix optional city filter” |
| Files touched | `routes/students.py` |
| Verified by | `/docs` GET with and without `city` |
| Human decision | “Kept SQLAlchemy `select()` style” |

Keep a short log in your capstone README—interviewers like honest process stories.

---

## When not to use Claude Code

| Situation | Better approach |
| --- | --- |
| Learning syntax first time | Type yourself, small examples |
| Drawing capstone HLD | Whiteboard/paper first |
| Secrets rotation | Provider console, not chat |
| Large dependency upgrades | Manual reading of changelogs |

---

## What this lesson deliberately does not cover

**Capstone HLD, database schema, and API security planning** are the focus of the **next** lessons—do not skip drawing boxes and tables because the CLI feels fast. **Structured outputs, vision, and embeddings** were covered in the integration track; only **reference** them when debugging related routes.

---

## Comparing Claude Code to browser GenAI labs

| Dimension | Browser assistant | Claude Code |
| --- | --- | --- |
| Context | What you paste | Files it can read |
| Edits | Manual copy | Proposed patches |
| Best for | Explanations | Repo changes |
| Risk | Over-wide paste leaks secrets | Over-wide diff breaks repo |

**Bridge habit:** Use browser for **concept questions**; use CLI for **file-scoped** edits after you understand the bug.

**Course alignment:** GenAI lab rules (one TASK, stack constraints) apply unchanged—only the **interface** moved to terminal.

---

## Keyboard and terminal ergonomics

| Tip | Benefit |
| --- | --- |
| Split pane: editor + terminal | See diff and logs together |
| `clear` between attempts | Less scroll confusion |
| Copy traceback with line numbers | Faster debug prompts |
| Name terminal tab by repo | Avoid editing wrong folder |

### Activity — two-terminal drill

Terminal A runs **`uvicorn`**; Terminal B runs Claude Code. After a fix, restart A and hit one endpoint—note whether you forgot restart in the past.

---

## Hands-on checklist

1. Install CLI and run **`--help`**; save one line about how to start a session.
2. Fix one real typo in your repo with a **single-file** prompt; reject any extra file edits.
3. Run LOOP on a **`campus_api`**-style bug you seed (wrong status code).
4. Practice a **debug template** prompt with full traceback from a missing import.
5. After a successful fix, make a Git commit with a human-written message.

---

## Key Takeaways

- **Claude Code** shines when tasks are **scoped**, repo-rooted, and reviewed like a teammate’s PR.
- **Install + CLI context** matter as much as clever wording—wrong directory equals wrong fix.
- **Iterative loops** beat one-shot “fix everything” prompts.
- **Debugging prompts** need tracebacks, paths, and constraints—not vibes.
- Next you will **design** the capstone before coding spikes—tools speed bricklaying, not building permits.

## Important Commands, Libraries, Terminologies used

| Name | Meaning in this lesson |
| --- | --- |
| **Claude Code** | Terminal-based agentic coding assistant |
| **CLI** | Command-line interface for tools |
| **Repository root** | Top folder of your project |
| **Diff** | Line-by-line comparison of file changes |
| **Iterative development** | Small repeated edit-test cycles |
| **Debug prompt** | Structured request with traceback and constraints |
| **LOOP** | Limit → Observe → Offer context → Patch review |
| **Scope** | Explicit boundary of files and behaviour |
| **`claude --help`** | Discover installed subcommands |
| **Git commit** | Save reviewed snapshot after each slice |
| **GenAI lab habit** | Trust but verify against running server |
| **API_BASE** | Frontend constant for backend URL |
| **`response.ok`** | Fetch guard for HTTP success range |
| **Academic integrity** | You explain work you submit |
| **`.env` hygiene** | Never paste secrets into AI chats |
