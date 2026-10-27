# Introduction to the Capstone Project

You have built **Python** fundamentals, a **frontend** that calls APIs, a persistent **`campus_api`** with **FastAPI** and **SQLAlchemy**, and you have practiced **LLM integration**, **structured AI features**, and **terminal-assisted** development. The capstone is where those skills become **one product** you can **demo**, **defend in interviews**, and **extend** after the course.

This lesson is **design-first**: **high-level design (HLD)**, **low-level design (LLD)**, **tech stack** choices, **database schema**, and **scope**. You will **not** list every HTTP route or auth flow here—that contract work belongs in the **next** planning lesson so architecture and API security stay separate.

## What you will learn in this lesson

- **Architecture design** — HLD boxes and LLD zoom-in for your idea
- **Tech stack selection** — frontend, backend, database, and AI tools you can ship
- **Database schema** — tables, keys, and relationships for core entities
- **Planning** — in-scope features vs deferred nice-to-haves
- **Hands-on** — one vertical slice blueprint for a **campus event booking** style app

Connecting idea: Code is bricklaying; capstone week needs **approved plans** so you do not pour concrete for a pool the plot cannot hold.

---

## Why design before another line of code

- **Official Definition:** **Software architecture** is the set of structures needed to reason about the system—components, relationships, and constraints.
- **In Simple Words:** A **map** of parts before you drive nails.
- **Real-Life Example:** Municipal **building plans** show kitchen, bedrooms, and plumbing before workers arrive.

| Pain if you skip design | What design gives you |
| --- | --- |
| Frontend calls wrong URLs | Shared nouns: **Event**, **Booking** |
| AI feature with no user table | Schema shows missing **users** early |
| Eleven half buttons | One **vertical slice** finished |

**Need:** Mentors can review diagrams and schema **before** merge conflicts eat your weekends.

**Common mistake:** Choosing a trendy database you have never run locally.

### Activity — one journey only

Pick **one** user journey that must work on demo day (example: “student books a seat for an event”). Write six steps from login to confirmation.

---

## High-level design (HLD)

- **Official Definition:** **High-level design** describes major subsystems and data flow without every class or line of code.
- **In Simple Words:** Bird’s-eye **boxes and arrows**.
- **Real-Life Example:** Mall directory map—food court, cinema, parking, not each shop’s shelf layout.

**Typical capstone boxes**

| Component | Responsibility |
| --- | --- |
| **Web client** | HTML/CSS/JS pages, forms, `fetch` |
| **API server** | FastAPI routes, validation, auth later |
| **Database** | SQLite or PostgreSQL tables via SQLAlchemy |
| **AI service** | Optional routes calling LLM/embeddings on **server** |

**ASCII HLD (event booking example)**

```text
[ Browser ] --HTTPS JSON--> [ FastAPI app ] --SQL--> [ Database ]
                                |
                                +----HTTPS----> [ LLM provider ]
                                (keys in .env only)
```

**Data flow narrative (three sentences max per arrow)**

- Browser sends **JSON** to your API—not to the LLM directly.
- API reads/writes **persistent** rows; no fake in-memory lists for core entities.
- AI routes return **draft or search** results; humans confirm critical fields.

**Security at HLD level (no route list yet)**

- Secrets live on **API server** only.
- Browser holds **session/token** later, not provider keys.

Connecting idea: HLD names the cast; **LLD** gives each actor a script for one journey.

---

## Low-level design (LLD)

- **Official Definition:** **Low-level design** refines HLD into modules, main entities, key screens, and critical interactions for chosen flows.
- **In Simple Words:** **Scene-by-scene** plan for the demo path.
- **Real-Life Example:** Wedding **run sheet**—who speaks when, not the full guest biography.

**LLD artefacts to produce**

| Artefact | Contents |
| --- | --- |
| **Screen list** | Login, event list, event detail, booking confirm |
| **API touchpoints** | Names only: `list_events`, `create_booking` (details later) |
| **Entity list** | User, Event, Booking (+ optional HostelClub) |
| **State notes** | What happens if event full? waitlist in or out of scope? |

**Booking flow (LLD bullets)**

1. User opens **event list** → API returns published events.
2. User opens **detail** → sees seats remaining (computed field).
3. User clicks **book** → API checks capacity → inserts booking row.
4. UI shows **confirmation** with booking id.

**Common doubt:** “Is LLD the same as database schema?” — Related but not identical; schema is **storage**; LLD includes **screens and steps**.

### Activity — mark out-of-scope

List two features you will **not** build in v1 (payment gateway, waitlist, chat bot). One sentence each on why deferring helps.

---

## Tech stack selection

- **Official Definition:** A **tech stack** is the set of languages, frameworks, libraries, and services used to implement the product.
- **In Simple Words:** Your **toolbox** for this build.
- **Real-Life Example:** Choosing **scooter vs metro**—both reach, but time and skill differ.

**Recommended course-aligned stack**

| Layer | Choice | Justification sentence |
| --- | --- | --- |
| Frontend | HTML, CSS, vanilla JS | Matches labs; no build step required |
| Backend | **FastAPI** | You already know `/docs`, Pydantic, routers |
| ORM | **SQLAlchemy 2** | Same patterns as **`campus_api`** |
| DB | **SQLite** locally | File-based, easy mentor review |
| AI | One provider API | Reuse **`campus_ai_api`** patterns |

**Trade-off table**

| Option | Pros | Cons |
| --- | --- | --- |
| SQLite | Zero setup | Weaker concurrency story |
| PostgreSQL | Production-like | Extra install burden |
| React SPA | Rich UI | More tooling for short timeline |
| Vanilla JS | Fast to learn curve | Manual DOM work |

**AI placement rule:** Model calls sit **behind** FastAPI routes you control—never expose keys in static JS.

**Common mistake:** Adding Kubernetes because it sounds impressive—scope dies, demo suffers.

Connecting idea: Stack choices must match the **schema** you can actually query.

---

## Database schema design

- **Official Definition:** A **database schema** defines tables, columns, types, keys, and relationships.
- **In Simple Words:** **Nouns** your API will persist.
- **Real-Life Example:** Attendance register columns—roll, name, hostel—not free paragraphs.

**Core tables (event booking example)**

| Table | Purpose |
| --- | --- |
| **users** | Who can log in and book |
| **events** | What can be booked |
| **bookings** | Who booked which event |

**SQLAlchemy-style column sketch**

```python
# Teaching sketch — align names with your ERD before coding
# users: id PK, email unique, password_hash, full_name, created_at
# events: id PK, title, description, starts_at, capacity, created_by_user_id FK
# bookings: id PK, user_id FK, event_id FK, status, created_at
# UNIQUE (user_id, event_id) optional — one seat per user per event
```

**Relationship rules**

| Rule | Meaning |
| --- | --- |
| **1 user → many bookings** | FK `bookings.user_id` |
| **1 event → many bookings** | FK `bookings.event_id` |
| **capacity** | Integer on **events**; count bookings before insert |

**ERD (text)**

```text
users (1) ----< bookings >---- (1) events
```

**Normalization instinct**

- Store **`event_id`** on booking, not duplicate entire event row.
- Store **`password_hash`**, never plain password (implementation in security lesson).

**Optional AI tables (only if in scope)**

| Table | Stores |
| --- | --- |
| **faq_entries** | question, answer, embedding blob or separate vector table |
| **uploads** | file path, uploader, created_at |

If AI is **out of v1**, leave tables out—do not schema-plan fiction.

### Activity — column challenge

Add **waitlist** without new features: which table gains a column or new table? Write one paragraph; mentors discuss in class.

---

## Scope and core features

- **Official Definition:** **Project scope** is the boundary of work agreed for delivery—what is in v1 vs later.
- **In Simple Words:** **Promise list** you can keep.
- **Real-Life Example:** Wedding menu—veg, Jain, dessert—not every global cuisine.

**MoSCoW sorting**

| Label | Example feature |
| --- | --- |
| **Must** | Login, list events, create booking |
| **Should** | Admin create event |
| **Could** | FAQ semantic search |
| **Won’t (now)** | Payment gateway |

**Vertical slice definition**

> A path from UI → API → DB that proves persistence and error handling for **one** happy journey plus **one** failure (event full).

**Time honesty**

| Team size | Realistic v1 |
| --- | --- |
| Solo | Thinner admin, strong one journey |
| Pair | Split frontend/backend along API names from LLD |

**Integrated AI scope:** If you include AI, tie it to **one** user-visible win (FAQ search or notice summarise)—not five half agents.

---

## Sample capstone problem statement (template)

Fill this one page before coding:

```text
Product name:
One-line problem:
Primary user:
Must-have journey:
Out of scope:
Stack choices (4 bullets):
HLD diagram (paste ASCII):
Tables (list):
Risks (keys, PII, fest traffic):
```

**Example one-liner:** “Students book seats for campus club events without WhatsApp chaos.”

---

## Mapping course work to capstone

| Earlier work | Capstone reuse |
| --- | --- |
| **`campus_api` CRUD** | Admin event management |
| **Frontend fetch labs** | List/detail pages |
| **Prompt + `/ai/chat`** | Optional helpdesk line |
| **Structured FAQ ingest** | Optional knowledge base |
| **Claude Code LOOP** | Faster fixes during build weeks |

You are **not** graded on using every feature—coherence beats checkbox tourism.

---

## Review checklist for mentors

| Item | Ready? |
| --- | --- |
| HLD diagram readable in 30 seconds | |
| LLD covers demo journey only | |
| Stack justified in plain English | |
| Schema has PKs, FKs, capacity story | |
| Scope lists **won’t** items | |
| AI keys stay server-side on diagram | |

---

## Non-functional requirements (light touch)

| NFR | Student-friendly meaning | Capstone example |
| --- | --- | --- |
| **Availability** | App works during demo | Run on laptop + backup video |
| **Performance** | List pages feel snappy | Paginate events if >50 rows |
| **Security** | Secrets and passwords protected | Keys only in `.env` on API |
| **Maintainability** | Teammate can read your code | Match `campus_api` folder layout |

You are not building Netflix—still name **one** NFR you will test before demo.

---

## Team working agreements

| Agreement | Why |
| --- | --- |
| Shared Git remote early | Avoids “two truths” |
| Main branch protected | Pull requests or buddy review |
| Naming convention doc | `snake_case` in Python, `camelCase` in JS if chosen |
| Daily 10-minute sync | Surfaces blockers before lecture |

**Conflict resolver:** When frontend and backend disagree on a field name, **schema wins** until the API contract lesson updates it formally.

---

## Example LLD screen notes (event booking)

| Screen | Elements | API touchpoint name |
| --- | --- | --- |
| Login | email, password, submit | `login` (auth detail later) |
| Event list | cards with title, date | `list_events` |
| Event detail | description, seats left | `get_event` |
| Booking confirm | success message, id | `create_booking` |

Wireframes can be pencil sketches—clarity beats colour.

---

## Capacity and booking rules (logic without code)

| Rule | Storage |
| --- | --- |
| Event has max seats | `events.capacity` integer |
| Each booking consumes one seat | row in **bookings** |
| Prevent overbooking | Count bookings before insert |
| Cancel policy | `status` column: `confirmed` / `cancelled` |

**Edge case discussion:** Two users book last seat at once—database transaction or unique constraint story; full fix in implementation week, but **name** the race in LLD.

### Activity — write acceptance criteria

For “create booking”, write three **Given / When / Then** lines (example: Given event has 1 seat left, When two users submit, Then only one succeeds).

---

## AI feature decision tree

```text
Does v1 need AI to solve the core problem?
  |-- No --> Ship without AI; add in v2 if time
  |-- Yes --> Pick ONE:
        (a) FAQ search via embeddings
        (b) Short summarise of event description
        (c) Upload notice Q&A with human confirm
```

If you choose (a), your HLD must show **FAQ storage**—not a lone chat bubble.

---

## Common design failures (integrated)

| Failure | Early signal | Fix in design phase |
| --- | --- | --- |
| **God table** | One table with 40 columns | Split entities |
| **No users** | AI remembers chat only | Add **users** |
| **Hidden lists** | “We’ll use array in JS” | Persist in DB |
| **Mystery AI** | Box labelled “AI” with no arrow | Name route purpose |

---

## Alternative capstone domains (same design method)

| Domain | Core entities (starter) |
| --- | --- |
| Study group matcher | users, groups, memberships |
| Hostel complaint tracker | users, complaints, status_history |
| Club announcement board | users, posts, tags |

Swap nouns in ERD—the **method** stays: HLD → LLD → schema → scope.

**Pick problems you can interview about:** real users, real constraints, not blockchain for its own sake.

---

## Versioning and milestones

| Milestone | Deliverable |
| --- | --- |
| M0 | This design packet approved |
| M1 | Empty repo + health route |
| M2 | Schema migrated + seed data |
| M3 | Demo journey working |
| M4 | Polish + optional AI |

Dates belong on your team calendar—not in these notes—but **order** matters more than heroics in week four.

---

## Glossary bridge (design ↔ code)

| Design word | Code word you will see later |
| --- | --- |
| Entity | SQLAlchemy model class |
| Relationship | Foreign key + relationship() |
| Screen | HTML page + JS handler |
| Touchpoint | Route handler function name |
| Contract | Request/response JSON shape (next lesson) |

---

## Mentor questions you should answer aloud

1. What problem does your app solve without AI?
2. Show me where the database lives on your HLD.
3. Which table enforces “no double booking”?
4. What did you consciously leave out of v1?
5. If Gemini is down, does core booking still work?

Prepare one-sentence answers before stand-up.

---

## Risk register (starter)

| Risk | Likelihood | Mitigation |
| --- | --- | --- |
| Scope creep | High | MoSCoW + weekly cut list |
| Schema churn | Medium | Freeze ERD after mentor sign-off |
| AI key leak | Low if disciplined | Server-only keys, no screenshots |
| Demo network fail | Medium | Record 2-minute backup video |
| Team member dropout | Medium | Document setup in README |

Add one risk specific to your idea (example: college fest traffic spike).

### Activity — risk to task

Pick the highest likelihood risk above and write **one** engineering task that reduces it before M2.

---

## Hands-on workshop steps (in class)

1. Draft **HLD** ASCII for your team idea on paper or whiteboard tool.
2. Write **LLD** bullets for six demo steps only.
3. Draw **ERD** with three core tables minimum.
4. Fill **MoSCoW** with at least five **won’t** items.
5. Write **four-sentence stack justification** aloud to a partner.
6. Trade diagrams with another team and find one **missing arrow** (auth? AI?).

### Activity — elevator pitch

In 30 seconds, describe your capstone to a non-tech friend: user, problem, and one screen they would recognise. If you mention “AI” before “booking” (or your core verb), reorder the pitch.

---

## What this lesson deliberately does not cover

Detailed **API endpoint tables**, **request/response JSON contracts**, **JWT flows**, and **security hardening checklists** are the **next** lesson so you finish **blueprints** before debating query parameters. Implementation sprints (frontend pages, backend routes) follow planning sessions in the module.

---

## Key Takeaways

- **HLD** shows components and trust boundaries—especially where **AI keys** live.
- **LLD** turns one **demo journey** into screens and API touchpoint names.
- **Schema** is a promise to your future self—design **users**, **events**, and **bookings** before hacks.
- **Scope** protects demo day—**must** features beat **could** features.
- Upcoming work turns this blueprint into **route contracts** and then into code.

## Important Commands, Libraries, Terminologies used

| Name | Meaning in this lesson |
| --- | --- |
| **Capstone** | Integrating course skills in one shipped project |
| **HLD** | High-level component and data-flow design |
| **LLD** | Low-level flow, screens, and module plan |
| **Tech stack** | Languages and frameworks chosen for delivery |
| **Schema** | Tables, columns, keys, relationships |
| **ERD** | Entity-relationship diagram |
| **Primary key (PK)** | Unique row identifier |
| **Foreign key (FK)** | Link between tables |
| **Vertical slice** | End-to-end thin feature path |
| **MoSCoW** | Must / Should / Could / Won’t prioritisation |
| **Scope** | Agreed in/out boundaries for v1 |
| **FastAPI** | Backend framework from course labs |
| **SQLAlchemy** | ORM for database access |
| **SQLite** | File database for local capstone |
| **users / events / bookings** | Example core entities |
| **capacity** | Event limit enforced before booking |
| **password_hash** | Stored credential, not plain text |
| **AI service** | Server-side LLM routes optional in v1 |
