# Introduction to the Capstone Project

You have built **Python** fundamentals, a **frontend** that calls APIs, a persistent **`campus_api`** with **FastAPI** and **SQLAlchemy**, and you have practiced **LLM integration**, **structured AI features**, and **terminal-assisted** development. The capstone is where those skills become **one product** you can **demo**, **defend in interviews**, and **extend** after the course.

The cohort builds **CampusBite**—a **restaurant order and delivery** app: customers place orders (with **dummy payment**), restaurant owners **CRUD dishes** and run the kitchen queue, delivery partners complete assigned runs, and customers **rate**, **request return**, and receive **dummy refunds** when the owner approves. Full session-by-session milestones, RBAC, status rules, and deployment targets are in **`Capstone Flow Session.md`** in this folder—treat that file as your master blueprint.

This lesson is **design-first**: **high-level design (HLD)**, **low-level design (LLD)**, **tech stack** choices, **database schema**, and **scope**. You will **not** list every HTTP route or auth flow here—that contract work belongs in the **next** planning lesson so architecture and API security stay separate.

## What you will learn in this lesson

- **Architecture design** — HLD boxes and LLD zoom-in for **CampusBite**
- **Tech stack selection** — **Vercel** (frontend), **Render** (API), **Supabase** (PostgreSQL), plus server-side AI
- **Database schema** — users, restaurants, menu, orders, reviews, payment ledger
- **Planning** — scope including **return/refund** (no real payment gateway)
- **Hands-on** — one vertical slice: place order → deliver → review → return → owner refund

Connecting idea: Code is bricklaying; capstone week needs **approved plans** so you do not pour concrete for a pool the plot cannot hold.

---

## Why design before another line of code

- **Official Definition:** **Software architecture** is the set of structures needed to reason about the system—components, relationships, and constraints.
- **In Simple Words:** A **map** of parts before you drive nails.
- **Real-Life Example:** Municipal **building plans** show kitchen, bedrooms, and plumbing before workers arrive.

| Pain if you skip design | What design gives you |
| --- | --- |
| Frontend calls wrong URLs | Shared nouns: **Order**, **MenuItem**, **status** |
| AI feature with no user table | Schema shows missing **users** early |
| Eleven half buttons | One **vertical slice** finished |

**Need:** Mentors can review diagrams and schema **before** merge conflicts eat your weekends.

**Common mistake:** Choosing a trendy database you have never run locally.

### Activity — one journey only

Pick **one** user journey that must work on demo day (example: “customer places order → partner delivers → customer requests return → owner approves dummy refund”). Write six steps from login to confirmation.

---

![CampusBite HLD: Vercel frontend, Render FastAPI backend, Supabase Postgres, and optional Gemini AI](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module4/session43/session43-01-hld-architecture.png?v=20261028)


## High-level design (HLD)

- **Official Definition:** **High-level design** describes major subsystems and data flow without every class or line of code.
- **In Simple Words:** Bird’s-eye **boxes and arrows**.
- **Real-Life Example:** Mall directory map—food court, cinema, parking, not each shop’s shelf layout.

**Typical capstone boxes**

| Component | Responsibility |
| --- | --- |
| **Web client** | HTML/CSS/JS pages, forms, `fetch` |
| **API server** | FastAPI routes, validation, auth later |
| **Database** | **Supabase** (PostgreSQL) via SQLAlchemy |
| **AI service** | Optional routes calling LLM/embeddings on **server** |

**ASCII HLD (CampusBite deployment)**

```text
[ Browser on Vercel ] --HTTPS JSON--> [ FastAPI on Render ] --SQL--> [ Supabase PostgreSQL ]
                                              |
                                              +----HTTPS----> [ LLM provider ]
                                              (keys in Render env only)
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
| **Screen list** | Login, menu/cart, checkout (dummy pay), my orders, restaurant queue, delivery list |
| **API touchpoints** | Names only: `create_order`, `assign_partner`, `return_decision` (details later) |
| **Entity list** | User, Restaurant, MenuItem, Order, OrderItem, Review, PaymentLedger |
| **State notes** | Order status transitions; cancel only in PLACED; return only after DELIVERED |

**Order flow (LLD bullets)**

1. Customer opens **menu** → API returns available dishes for one restaurant.
2. Customer **checks out** → order `PLACED`, **mock_paid** ledger row.
3. Owner advances **ACCEPTED → PREPARING → READY**, **assigns** delivery partner.
4. Partner marks **DELIVERED** → customer **reviews** or **requests return** → owner **approves refund** (dummy).

**Common doubt:** “Is LLD the same as database schema?” — Related but not identical; schema is **storage**; LLD includes **screens and steps**.

### Activity — mark out-of-scope

List two features you will **not** build in v1 (real UPI gateway, live map tracking). One sentence each on why deferring helps.

---

![Match each layer to course tools: React on Vercel, FastAPI on Render, Postgres on Supabase](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module4/session43/session43-03-tech-stack-layers.png?v=20261028)


## Tech stack selection

- **Official Definition:** A **tech stack** is the set of languages, frameworks, libraries, and services used to implement the product.
- **In Simple Words:** Your **toolbox** for this build.
- **Real-Life Example:** Choosing **scooter vs metro**—both reach, but time and skill differ.

**Cohort capstone stack (locked)**

| Layer | Choice | Justification sentence |
| --- | --- | --- |
| Frontend | HTML, CSS, vanilla JS on **Vercel** | Matches labs; static hosting with env for API URL |
| Backend | **FastAPI** on **Render** | You already know `/docs`, Pydantic, routers |
| ORM | **SQLAlchemy 2** | Same patterns as **`campus_api`** |
| DB | **Supabase** (PostgreSQL) | Production-shaped DB; connection string on Render |
| AI | One provider API on Render | Reuse **`campus_ai_api`** patterns; keys never on Vercel |

**Trade-off table**

| Option | Pros | Cons |
| --- | --- | --- |
| Supabase | Hosted Postgres + dashboard | Requires connection string discipline |
| SQLite local only | Fast offline dev | Differs from prod—mirror Supabase early |
| React SPA | Rich UI | More tooling for short timeline |
| Vanilla JS | Fast to learn curve | Manual DOM work |

**AI placement rule:** Model calls sit **behind** FastAPI routes you control—never expose keys in static JS.

**Common mistake:** Adding Kubernetes because it sounds impressive—scope dies, demo suffers.

Connecting idea: Stack choices must match the **schema** you can actually query.

---

![Core entities—users, restaurants, menu items, orders, and delivery—before you write migrations](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module4/session43/session43-02-entity-relationship.png?v=20261028)


## Database schema design

- **Official Definition:** A **database schema** defines tables, columns, types, keys, and relationships.
- **In Simple Words:** **Nouns** your API will persist.
- **Real-Life Example:** Attendance register columns—roll, name, hostel—not free paragraphs.

**Core tables (CampusBite)**

| Table | Purpose |
| --- | --- |
| **users** | customer, restaurant_owner, delivery_partner; `role` + optional `restaurant_id` |
| **restaurants** | Outlet metadata |
| **menu_items** | Dish CRUD scope for owner |
| **orders** | Status, dummy **payment_status**, **return_status**, partner assignment |
| **order_items** | Line snapshots (`unit_price_snapshot`, `item_name_snapshot`) |
| **reviews** | One per delivered order |
| **payment_ledger** | `mock_charge` and `refund_credit` rows (no gateway) |

**SQLAlchemy-style column sketch**

```python
# Teaching sketch — see Capstone Flow Session.md for full columns
# orders.status: PLACED .. DELIVERED, CANCELLED
# orders.payment_status: mock_paid, refunded, refund_rejected, ...
# orders.return_status: none, requested, approved, rejected
```

**Relationship rules**

| Rule | Meaning |
| --- | --- |
| **1 restaurant → many menu_items** | FK `menu_items.restaurant_id` |
| **1 customer → many orders** | FK `orders.customer_id` |
| **1 order → many order_items** | Snapshots protect history when menu price changes |

**ERD (text)**

```text
restaurants (1) ----< menu_items
users (customer) (1) ----< orders >---- (1) restaurants
orders (1) ----< order_items
orders (1) ---- 0..1 reviews
orders (1) ---- * payment_ledger
```

**Normalization instinct**

- Store **price and dish name on `order_items`** at place time.
- Store **`password_hash`**, never plain password (implementation in security lesson).

**Optional AI tables (only if in scope)**

| Table | Stores |
| --- | --- |
| **faq_entries** | question, answer, embedding blob or separate vector table |
| **uploads** | file path, uploader, created_at |

If AI is **out of v1**, leave tables out—do not schema-plan fiction.

### Activity — column challenge

Add **partial refund** without a payment gateway: which fields on `orders` and `payment_ledger` change? Write one paragraph; mentors discuss in class.

---

## Scope and core features

- **Official Definition:** **Project scope** is the boundary of work agreed for delivery—what is in v1 vs later.
- **In Simple Words:** **Promise list** you can keep.
- **Real-Life Example:** Wedding menu—veg, Jain, dessert—not every global cuisine.

**MoSCoW sorting**

| Label | Example feature |
| --- | --- |
| **Must** | Login, menu, place order (mock pay), kitchen flow, deliver, review |
| **Should** | Return request + owner refund decision, dashboard filters |
| **Could** | Menu image upload, AI menu FAQ |
| **Won’t (now)** | Real payment gateway, maps, websockets |

**Vertical slice definition**

> A path from UI → API → DB that proves persistence and error handling for **deliver + review + return/refund**, plus **409** when customer tries to cancel a **DELIVERED** order.

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

**Example one-liner:** “Students order from campus restaurants with tracked delivery and fair return handling—without WhatsApp chaos.”

---

## Mapping course work to capstone

| Earlier work | Capstone reuse |
| --- | --- |
| **`campus_api` CRUD** | Restaurant menu + order patterns |
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
| Schema has PKs, FKs, order status + payment ledger | |
| Scope lists **won’t** items | |
| AI keys stay server-side on diagram | |

---

## Non-functional requirements (light touch)

| NFR | Student-friendly meaning | Capstone example |
| --- | --- | --- |
| **Availability** | App works during demo | Run on laptop + backup video |
| **Performance** | List pages feel snappy | Paginate orders if >50 rows |
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

## Example LLD screen notes (CampusBite)

| Screen | Elements | API touchpoint name |
| --- | --- | --- |
| Login | email, password, submit | `login` (auth detail later) |
| Menu | dishes, add to cart | `get_menu` |
| Checkout | address, dummy pay confirm | `create_order` |
| My orders | status filters | `list_my_orders` |
| Restaurant queue | status buttons, assign partner | `update_order_status`, `assign` |
| Delivery | my list, mark delivered | `delivery_orders` |

Wireframes can be pencil sketches—clarity beats colour.

---

## Order, cancel, return, and refund rules (logic without code)

| Rule | Storage / behaviour |
| --- | --- |
| Customer cancel | Only while `status=PLACED` |
| Delivered order | No delete; no cancel |
| Dummy payment | `mock_paid` + ledger `mock_charge` on place |
| Return request | After `DELIVERED`; `return_status=requested` |
| Refund | Owner approves → ledger `refund_credit`, `payment_status=refunded` |

**Edge case discussion:** Customer tries to delete a **DELIVERED** order—API returns **409**; only **return-request** path applies.

### Activity — write acceptance criteria

For “cancel order”, write three **Given / When / Then** lines (example: Given order is PREPARING, When customer calls cancel, Then API returns 409).

---

## AI feature decision tree

```text
Does v1 need AI to solve the core problem?
  |-- No --> Ship without AI; add in v2 if time
  |-- Yes --> Pick ONE:
        (a) FAQ search via embeddings
        (b) Menu / allergy FAQ from `faq_entries`
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

![Plan → security → frontend → backend → integration → documentation and deployment](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module4/session43/session43-04-capstone-session-flow.png?v=20261028)


## Capstone flow across build sessions

Use **`Capstone Flow Session.md`** for the full checklist. In short:

| Build phase | You deliver |
| --- | --- |
| Architecture (this lesson) | HLD, ERD, MoSCoW, vertical slice story |
| API & security plan | Route contracts, JWT, RBAC matrix |
| Frontend | Vercel dashboards + `localStorage` token |
| Backend | Render + Supabase + transition guards |
| Integration | E2E demo + `/ai/ask` |
| Ship | README, env docs, live URLs |

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
3. Which table stores **dummy refund** history?
4. What did you consciously leave out of v1?
5. If Gemini is down, does placing and delivering orders still work?

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

In 30 seconds, describe your capstone to a non-tech friend: user, problem, and one screen they would recognise. If you mention “AI” before “ordering” (or your core verb), reorder the pitch.

---

## What this lesson deliberately does not cover

Detailed **API endpoint tables**, **request/response JSON contracts**, **JWT flows**, and **security hardening checklists** are the **next** lesson so you finish **blueprints** before debating query parameters. Implementation sprints (frontend pages, backend routes) follow planning sessions in the module.

---

## Key Takeaways

- **HLD** shows components and trust boundaries—especially where **AI keys** live.
- **LLD** turns one **demo journey** into screens and API touchpoint names.
- **Schema** is a promise to your future self—design **orders**, **ledger**, and **roles** before hacks.
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
| **Supabase** | Hosted PostgreSQL for capstone |
| **Vercel / Render** | Preferred FE / BE hosting |
| **payment_ledger** | Dummy charge and refund audit rows |
| **mock_paid** | Payment status without gateway |
| **return_status** | Customer return + owner decision |
| **CampusBite** | Cohort restaurant delivery capstone |
| **Capstone Flow Session.md** | Master blueprint for sessions 43–48 |
| **password_hash** | Stored credential, not plain text |
| **AI service** | Server-side LLM routes optional in v1 |
