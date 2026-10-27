# CampusBite — Capstone Flow (Sessions 43–48)

This document is the **single source of truth** for the cohort capstone: **CampusBite**, a campus-area **restaurant ordering and delivery** application. Lecture notes for capstone sessions follow this flow, metadata subtopics, and the business rules below.

**Product summary:** Customers browse menus, place orders (with **dummy payment**), track status, rate food, and optionally **request return/refund**. Restaurant owners **CRUD dishes**, manage orders through the kitchen pipeline, **assign delivery partners**, and **approve or reject** return/refund requests. Delivery partners see **only their assignments** and mark **out for delivery** / **delivered**. No real payment gateways, no websockets, no maps.

---

## 1. Goals and non-goals

### Goals

- Full-stack app using course stack: **vanilla JS**, **FastAPI**, **SQLAlchemy**, **PostgreSQL (Supabase)**.
- **REST APIs only**; dashboards with **filters** (status, date).
- **RBAC**: customer, restaurant_owner, delivery_partner (optional seeded admin).
- **Order lifecycle** with valid transitions enforced on the **server**.
- **Menu CRUD** by restaurant owner; **order CRUD with care** for customers (no delete after delivery; cancel only when allowed).
- **Dummy payment** recorded at order place; **refund/return** decided by **restaurant admin**, stored as ledger fields (no Razorpay/Stripe).
- **Applied AI** (customer): **order insights / summarise my orders** — server loads the customer’s order rows from DB, calls Gemini with that context, returns text for the UI (no embeddings).
- **Cross-cutting (planned in HLD/LLD, built in backend sessions):** request **middleware** (logging, timing) and **rate limiting** on auth + AI routes.
- **Background tasks:** reminder nudge for **restaurant admins** when orders sit too long without status updates (no websockets).
- **Profile images:** **URL only** at signup (`profile_image_url`) — **no file upload** anywhere in capstone v1.
- **Deploy**: frontend **Vercel**, backend **Render**, database **Supabase**; document env vars and CORS.

### Non-goals (v1)

- Real payment integration, UPI, webhooks from gateways.
- Live GPS, driver maps, websockets, push notifications.
- Multi-restaurant cart (one restaurant per order).
- Auto-dispatch algorithms for delivery partners.

---

## 2. Roles and access (RBAC)

| Role | `users.role` | Scoped data |
| --- | --- | --- |
| **Customer** | `customer` | Own orders, own reviews, own return requests |
| **Restaurant owner** | `restaurant_owner` | One `restaurant_id`; menu items; orders for that restaurant; return/refund decisions |
| **Delivery partner** | `delivery_partner` | Orders where `delivery_partner_id = my user id` |
| **Admin** (optional) | `admin` | Seed restaurants/users; not required for demo if SQL seed scripts exist |

**Auth pattern (capstone)**

- `POST /auth/register`, `POST /auth/login` → JWT `access_token` + `role` (+ `restaurant_id` if owner).
- Frontend stores token (and role) in **`localStorage`**; every `fetch` sends `Authorization: Bearer <token>`.
- **Server enforces RBAC on every route**; UI hiding buttons is not security.

**Row-level rules (examples)**

- Customer `GET /orders/{id}` → 404 if `order.customer_id != current_user.id`.
- Owner `GET /restaurant/orders` → `WHERE restaurant_id = current_user.restaurant_id`.
- Partner `GET /delivery/orders` → `WHERE delivery_partner_id = current_user.id`.

---

## 3. High-level architecture (HLD)

```text
[ Browser on Vercel ]
   static HTML/CSS/JS
   localStorage: JWT
        |
        | HTTPS JSON (CORS: Vercel origin -> Render API)
        v
[ FastAPI on Render ]
   JWT verify, RBAC, business rules, dummy payment/refund
        |
        +------ SQL (SQLAlchemy) ------> [ Supabase PostgreSQL ]
        |
        +------ HTTPS -----------------> [ LLM provider ]
               GEMINI_API_KEY in Render env only
```

**Environment split**

| Layer | Host | Secrets |
| --- | --- | --- |
| Frontend | Vercel | Public `API_BASE_URL` only |
| Backend | Render | `DATABASE_URL`, `JWT_SECRET`, `GEMINI_API_KEY`, `CORS_ORIGINS` |
| Database | Supabase | Connection string in Render; not in Git |

**Local dev:** SQLite or local Supabase connection; same code paths; `.env` not committed.

### 3.1 Cross-cutting concerns (document in HLD / LLD / Session 44 plan)

| Concern | Purpose | Capstone scope |
| --- | --- | --- |
| **Middleware** | Log method + path + latency; optional request id | FastAPI `@app.middleware("http")` |
| **Rate limiting** | Protect `/auth/login`, `/ai/*` from abuse | In-memory or simple sliding window per IP/user |
| **JWT expiry** | Tokens stop working after `exp` | Frontend clears `localStorage` on **401** |
| **CORS** | Vercel origin only | `CORS_ORIGINS` on Render |
| **Pagination** | Large order lists | `?page=1&limit=20` on list endpoints |
| **Validation** | Pydantic on every body | rating 1–5, quantities, URL format for profile image |

**LLD note:** Draw middleware **before** routes box in HLD; AI and auth routes annotated “rate limited”.

---

## 4. Database schema (Supabase / PostgreSQL)

### 4.1 Core tables

**users**

| Column | Type | Notes |
| --- | --- | --- |
| id | UUID or serial PK | |
| email | unique | login |
| password_hash | string | bcrypt or passlib |
| full_name | string | |
| role | enum | customer, restaurant_owner, delivery_partner, admin |
| restaurant_id | FK nullable | set for restaurant_owner |
| profile_image_url | string nullable | **HTTPS image URL** at register; shown in UI; no upload |
| created_at | timestamptz | |

**restaurants**

| Column | Type | Notes |
| --- | --- | --- |
| id | PK | |
| name | string | |
| address_text | string | no maps |
| is_active | boolean | |
| owner_user_id | FK users | optional duplicate of users.restaurant_id |

**menu_items**

| Column | Type | Notes |
| --- | --- | --- |
| id | PK | |
| restaurant_id | FK | |
| name | string | |
| description | text | |
| price_inr | decimal | > 0 |
| is_available | boolean | soft “delete” |
| image_url | string nullable | optional **external** dish image URL (no upload) |
| created_at | timestamptz | |

**orders**

| Column | Type | Notes |
| --- | --- | --- |
| id | PK | |
| customer_id | FK users | |
| restaurant_id | FK | |
| delivery_partner_id | FK users nullable | set on assign |
| status | enum | see §5 |
| delivery_address_text | text | |
| notes | text nullable | |
| subtotal_inr | decimal | sum of lines at place time |
| **payment_status** | enum | `mock_paid`, `refund_pending`, `refunded`, `refund_rejected` |
| **return_status** | enum nullable | `none`, `requested`, `approved`, `rejected` |
| placed_at | timestamptz | |
| updated_at | timestamptz | |

**order_items**

| Column | Type | Notes |
| --- | --- | --- |
| id | PK | |
| order_id | FK | |
| menu_item_id | FK | |
| item_name_snapshot | string | copy at order time |
| unit_price_snapshot | decimal | copy at order time |
| quantity | int | >= 1 |

**reviews**

| Column | Type | Notes |
| --- | --- | --- |
| id | PK | |
| order_id | FK unique | one review per order |
| customer_id | FK | |
| rating | int | 1–5 |
| comment | text nullable | |
| created_at | timestamptz | |

**payment_ledger** (dummy finance audit)

| Column | Type | Notes |
| --- | --- | --- |
| id | PK | |
| order_id | FK | |
| entry_type | enum | `mock_charge`, `refund_credit` |
| amount_inr | decimal | |
| note | text | e.g. “Dummy payment at place” |
| created_by_user_id | FK | customer or owner |
| created_at | timestamptz | |

**admin_reminder_log** (background task audit)

| Column | Type | Notes |
| --- | --- | --- |
| id | PK | |
| order_id | FK | |
| restaurant_id | FK | |
| message | text | e.g. “Order #12 still PLACED > 15 min” |
| created_at | timestamptz | |

### 4.2 Relationships (text ERD)

```text
restaurants 1 --- * menu_items
users (customer) 1 --- * orders
restaurants 1 --- * orders
orders 1 --- * order_items
orders 1 --- 0..1 reviews
orders 1 --- * payment_ledger
users (delivery) 1 --- * orders (as delivery_partner_id)
```

---

## 5. Order status machine (fulfillment)

**`orders.status`** — enforce transitions in one backend function e.g. `assert_order_transition(order, new_status, role)`.

```text
PLACED
  |-- customer cancel --> CANCELLED
  |-- owner accept --> ACCEPTED
ACCEPTED
  |-- owner cancel (optional policy) --> CANCELLED
  |-- owner --> PREPARING
PREPARING
  |-- owner --> READY
READY
  |-- owner assign partner --> ASSIGNED  (sets delivery_partner_id)
ASSIGNED
  |-- partner --> OUT_FOR_DELIVERY
OUT_FOR_DELIVERY
  |-- partner --> DELIVERED
DELIVERED
  (immutable for line items / cancel; return/refund is separate §6)
CANCELLED
  (terminal; mock refund rules §6 if payment was mock_paid)
```

**Invalid transition** → HTTP **409 Conflict** with clear `detail` string.

**Who can trigger what**

| Transition | Role |
| --- | --- |
| PLACED → CANCELLED | customer (only while PLACED) |
| PLACED → ACCEPTED → … → READY | restaurant_owner |
| READY → ASSIGNED | restaurant_owner (body: `delivery_partner_id`) |
| ASSIGNED → OUT_FOR_DELIVERY → DELIVERED | delivery_partner (assigned only) |
| * → CANCELLED (after accept) | restaurant_owner only if policy allows before OUT_FOR_DELIVERY |

---

## 6. Dummy payment, return, and refund

### 6.1 Dummy payment (no gateway)

On **`POST /orders`** success:

1. Create order + line items with snapshots.
2. Set `payment_status = mock_paid`.
3. Insert `payment_ledger` row: `entry_type=mock_charge`, `amount_inr=subtotal`, note `"Dummy payment – no gateway"`.

**No** card fields, no redirect, no webhooks.

### 6.2 Return request (customer, after delivery)

After `status = DELIVERED`:

- Customer may `POST /orders/{id}/return-request` with `reason` text (once).
- Set `return_status = requested`; order row otherwise unchanged.

**Not allowed:** return request if not `DELIVERED`, or if `return_status` already set.

### 6.3 Restaurant decision (return + refund)

Owner for that restaurant:

- `POST /orders/{id}/return-decision` body: `{ "decision": "approve" | "reject", "admin_note": "..." }`

**On approve**

- `return_status = approved`
- `payment_status = refund_pending` then immediately process dummy refund:
  - `payment_status = refunded`
  - Ledger: `entry_type=refund_credit`, `amount_inr=subtotal` (or partial if you document partial v2; v1 = full subtotal)
- Optional: set `status` to `REFUNDED` **or** keep `DELIVERED` and rely on `payment_status` (pick one; recommended: add terminal status **`REFUNDED`** for dashboard filters).

**On reject**

- `return_status = rejected`
- `payment_status = refund_rejected` (or remain `mock_paid` with `return_status=rejected` only—document one pattern; recommended: `payment_status` stays `mock_paid`, `return_status=rejected`).

### 6.4 Cancel before delivery (mock refund)

If customer cancels at **PLACED** only:

- `status = CANCELLED`
- If `mock_paid`: insert ledger `refund_credit` (dummy instant refund) and set `payment_status = refunded`.

If restaurant cancels after accept:

- Same dummy refund policy in v1 (full subtotal credit row).

**Delivered orders:** customer **cannot** cancel; only **return-request** path.

---

## 7. CRUD matrices

### 7.1 Restaurant owner — menu_items

| Action | Endpoint style | Rules |
| --- | --- | --- |
| Create | `POST /restaurant/menu-items` | Own restaurant only |
| Read | `GET /restaurants/{id}/menu` public; owner sees unavailable too | |
| Update | `PATCH /restaurant/menu-items/{id}` | Own restaurant; price change does not alter past orders |
| Delete | Prefer `PATCH` set `is_available=false` | No hard delete if referenced in order_items |

### 7.2 Customer — orders

| Action | Allowed | Forbidden |
| --- | --- | --- |
| Create | `POST /orders` | Empty cart, wrong restaurant, unavailable dish |
| Read | `GET /orders/me`, `GET /orders/{id}` own | Other users’ orders |
| Update items/address | Only if `status=PLACED` (v1 strict) | After accept |
| Cancel | `PATCH /orders/{id}/cancel` only if `PLACED` | PREPARING+, DELIVERED |
| Delete HTTP | **No DELETE** | Use cancel / return flows |
| Review | `POST /orders/{id}/review` if DELIVERED, one per order | Before delivery |
| Return | `POST /orders/{id}/return-request` if DELIVERED | Before delivery |

### 7.3 Delivery partner

| Action | Rule |
| --- | --- |
| List | Filter own assignments |
| Status | Only ASSIGNED → OUT_FOR_DELIVERY → DELIVERED |

### 7.4 Reviews

- Create after **DELIVERED**; unique per `order_id`.
- v1: no edit/delete review (optional stretch).

---

## 8. Dashboards and filters

### 8.1 Customer dashboard

- **My orders** table: columns status, payment_status, return_status, total, placed_at.
- **Filters:** `status`, `from_date`, `to_date`, `payment_status`.
- Actions (buttons gated by server rules): Cancel (PLACED), Track, Review (DELIVERED), Request return (DELIVERED, return none).

### 8.2 Restaurant dashboard

- **Orders queue:** PLACED → … → READY.
- **Filters:** status, date, assigned (yes/no), return_status.
- Actions: Accept, Preparing, Ready, Assign partner (dropdown of delivery users), Return decision.
- **Menu management** page: dish CRUD.

### 8.3 Delivery partner dashboard

- **My deliveries:** ASSIGNED, OUT_FOR_DELIVERY.
- **Filters:** status, today.
- Actions: Start delivery, Mark delivered.

**Refresh pattern:** manual **Refresh** button or reload page—no websockets.

---

## 9. Applied AI (Session 47 integration)

**No embeddings / vector DB in capstone v1.**

**Primary feature: Order insights & summaries (customer)**

- `POST /ai/orders/insights` — body: `{ "prompt_type": "summary" | "insights", "question": "optional string" }`
- Server steps:
  1. Authenticate **customer**; load their orders (and line items) from Supabase — same filters as dashboard (`?limit=` last N).
  2. Build a **context block** (order ids, statuses, dates, items, totals) — no other customers’ data.
  3. Call **Gemini** with system prompt: “Answer only from ORDER_CONTEXT; no invented orders.”
  4. Return `{ "answer": "..." }` for UI display.
- Examples: “Summarise my last 5 orders”, “Which orders are still not delivered?”, “How much did I spend this week?” (computed hints in context help the model).
- **Rate limited** (e.g. 10 requests / hour / user) — plan in Session 44.
- Keys only on Render; Vercel never sees `GEMINI_API_KEY`.

**Not in scope:** autonomous ordering, embeddings, vision, streaming required for demo (buffered JSON is fine).

---

## 9.1 Background tasks (restaurant admin reminders)

- On a schedule **or** after `GET /restaurant/orders`, run `BackgroundTasks` check:
  - Orders in `PLACED` or `ACCEPTED` older than **15 minutes** (configurable) without `updated_at` change.
  - Insert `admin_reminder_log` row; expose `GET /restaurant/reminders` for dashboard banner.
- **Not** push notifications — owner refreshes page or sees banner on load.
- Teaches FastAPI **BackgroundTasks** from Module 3 without new infrastructure.

---

## 10. Session-by-session flow and deliverables

### Session 43 — Introduction to the Capstone Project

**Focus:** HLD/LLD, schema, stack justification, scope.

**Deliverables**

- Team charter + problem statement (CampusBite).
- HLD diagram (Vercel / Render / Supabase / LLM).
- ERD for tables in §4.
- MoSCoW feature list aligned with §1.
- One **vertical slice** story written: place order → deliver → review → return request → owner refund.
- Read this **Capstone Flow Session.md** end-to-end.

**Lecture notes:** Architecture and schema for **restaurant** domain (not event booking).

---

### Session 44 — API Endpoints & Security Planning

**Focus:** **Auth, JWT, and RBAC first** (first formal pass in course) + API contracts + security/middleware/rate-limit **plan**.

**Deliverables**

- **JWT design:** `sub`, `role`, `restaurant_id`, `exp`; register/login request bodies including `profile_image_url` (HTTPS URL).
- **RBAC matrix:** every route × roles (customer / owner / partner / public).
- **OpenAPI-style table** for all routes (reference §12); **order detail** includes `items[]`; pagination query params documented.
- `GET /restaurant/delivery-partners`, `GET /restaurant/stats`, menu `?q=&max_price=`.
- **Middleware & rate-limit plan** in HLD/LLD appendix (which routes, limits, 429 response shape).
- Security checklist: CORS, bcrypt, no secrets on Vercel, 401 handling on frontend.
- **State transition table** from §5–§6 for Session 46.
- Error convention: 401, 403, 404, 409, 422, 429.

**Implementation:** auth skeleton + `/docs` optional; milestone is **document + understanding**.

---

### Session 45 — Capstone I: Frontend Development

**Focus:** UI and client logic; may use mock API or early Render deploy.

**Deliverables**

- Vercel project structure: `index.html`, role-based pages or SPA-lite routing.
- Pages: Login/Register, Customer (menu, cart, checkout dummy pay, my orders), Restaurant (orders + menu CRUD UI), Delivery (my deliveries).
- `api.js`: `API_BASE_URL`, `authHeaders()`, error handling.
- localStorage login persistence; redirect if wrong role.
- Filters wired to query params (even if backend mock returns static JSON first).
- Mentor checkpoint: one role flow navigable in UI.

---

### Session 46 — Capstone II: Backend Development

**Focus:** FastAPI + SQLAlchemy + Supabase; business logic.

**Deliverables**

- Render service with `DATABASE_URL` from Supabase.
- Models matching §4; migrations or `create_all` for teaching.
- All REST endpoints from Session 44 doc.
- `assert_order_transition` + payment/return helpers.
- Seed script: 1 restaurant, 1 owner, 2 partners, 1 customer, sample menu.
- `/docs` smoke tests for happy path and **409** on illegal cancel.
- CORS allows Vercel preview URL.

---

### Session 47 — Capstone III: Agents & Full-Stack Integration

**Focus:** Replace mocks; E2E; AI route.

**Deliverables**

- Vercel `API_BASE_URL` → Render production URL.
- E2E path demonstrated live:
  1. Customer places order (mock paid).
  2. Restaurant advances to READY, assigns partner.
  3. Partner delivers.
  4. Customer reviews.
  5. Customer return-request; owner approves → ledger refund row.
- `POST /ai/orders/insights` working from customer page (summary / insights).
- Debug log: fix at least one real integration bug (CORS, 401, JSON key mismatch).
- Graceful degradation if LLM rate-limited (503 message).

---

### Session 48 — Capstone IV: Documentation & Deployment

**Focus:** Ship and submit.

**Deliverables**

- **README**: local setup, env vars (Render + Vercel + Supabase), seed users, demo script.
- API doc link (Render `/docs` or exported OpenAPI).
- Vercel production URL + Render health check.
- Supabase dashboard screenshot or table list (no passwords).
- Submission checklist: RBAC tested, return/refund path tested, no keys in repo.
- 3–5 minute demo outline with roles switching.

**Deployment steps (reference)**

1. Supabase: create project → connection string → run schema/seed.
2. Render: Web Service → Python → `uvicorn main:app --host 0.0.0.0 --port $PORT` → env vars.
3. Vercel: static site or framework preset → set `VITE_API_URL` or inline config → redeploy.
4. Update Render `CORS_ORIGINS` with Vercel domain.

---

## 11. End-to-end demo script (mentor gold path)

| Step | Actor | Action | Expected |
| --- | --- | --- | --- |
| 1 | Customer | Login, add dishes, checkout | Order PLACED, mock_paid, ledger charge |
| 2 | Owner | Accept → Preparing → Ready | Status advances |
| 3 | Owner | Assign partner | ASSIGNED, partner_id set |
| 4 | Partner | Out for delivery → Delivered | DELIVERED |
| 5 | Customer | Submit 5-star review | review row |
| 6 | Customer | Return request | return_status requested |
| 7 | Owner | Approve return | refunded + ledger credit |
| 8 | Customer | Try cancel delivered order | 409 |

---

## 12. API route index (for Session 44 detail)

| Method | Path | Role |
| --- | --- | --- |
| POST | `/auth/register` | public (body includes `profile_image_url` optional) |
| POST | `/auth/login` | public (rate limited) |
| GET | `/auth/me` | any authenticated |
| GET | `/restaurants` | public |
| GET | `/restaurants/{id}/menu` | public (`?q=`, `?max_price=`) |
| GET | `/restaurants/{id}/stats` | public read avg rating |
| POST | `/restaurant/menu-items` | owner |
| PATCH | `/restaurant/menu-items/{id}` | owner |
| POST | `/orders` | customer |
| GET | `/orders/me` | customer (`?status=`, `?page=`, `?limit=`) |
| GET | `/orders/{id}` | customer (own; includes **order_items**) |
| PATCH | `/orders/{id}/cancel` | customer (PLACED only) |
| POST | `/orders/{id}/review` | customer |
| POST | `/orders/{id}/return-request` | customer |
| GET | `/restaurant/delivery-partners` | owner |
| GET | `/restaurant/stats` | owner (counts by status, today) |
| GET | `/restaurant/reminders` | owner (stale order nudges) |
| GET | `/restaurant/orders` | owner (`?status=`, pagination) |
| PATCH | `/restaurant/orders/{id}/status` | owner |
| PATCH | `/restaurant/orders/{id}/assign` | owner |
| POST | `/restaurant/orders/{id}/return-decision` | owner |
| GET | `/delivery/orders` | partner |
| PATCH | `/delivery/orders/{id}/status` | partner |
| POST | `/ai/orders/insights` | customer (rate limited) |
| GET | `/health` | public |

Session 44 lecture notes expand each with request/response bodies.

---

## 13. MoSCoW (cohort default)

| Must | Should | Could | Won’t |
| --- | --- | --- | --- |
| RBAC + JWT + `profile_image_url` | Multi-restaurant browse | Partial refund | Real payments |
| Menu CRUD owner | Menu search `?q=` / max price | Dish external image URL | File upload |
| Order lifecycle + **detail w/ items** | **Stats** (GROUP BY) + avg rating | Admin portal | Maps |
| Dummy pay + ledger | **Delivery partner list** | | Websockets |
| Deliver + review + return/refund | **Middleware + rate limits** | | Embeddings |
| **AI order summary/insights** | Background admin reminders | | |
| Pagination on lists | JWT expiry + 401 UX | | Multi-cart |

---

## 14. Repository layout (suggested)

```text
campusbite/
  backend/          # FastAPI → Render
    app/
    requirements.txt
    .env.example
  frontend/         # static → Vercel
    js/api.js
    pages/
  docs/
    Capstone-API-Contract.md   # output of Session 44
  README.md
```

---

## 15. Alignment with course skills

| Prior learning | CampusBite usage |
| --- | --- |
| `campus_api` CRUD | Menu + orders |
| Pydantic / `/docs` | Session 44 contracts |
| SQL JOINs | Order + items + restaurant |
| CORS (M3) | Vercel → Render |
| Background tasks (M3) | Admin stale-order reminders |
| Middleware (M3) | Logging + rate limit plan |
| LLM API (M4) | `/ai/orders/insights` with DB context |
| Claude Code (M4) | Build/debug loops |

---

## 16. Change log

| Date | Change |
| --- | --- |
| 2026-03-27 | Initial CampusBite flow: restaurant delivery, dummy payment, return/refund by owner, Vercel/Render/Supabase |
| 2026-03-27 | Profile image URLs only; AI order insights; middleware/rate limits; admin BG reminders; no uploads/embeddings |

---

**Next:** Session 44 lecture notes implement the API contract and security sections from §10–§12. Session 45–48 notes reference this file for milestones and E2E script §11.
