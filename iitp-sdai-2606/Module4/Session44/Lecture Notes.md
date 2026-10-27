# Capstone Project Planning – API Endpoints & Security

You designed **CampusBite** in the architecture lesson: roles, order states, dummy payment, return/refund, and deployment on **Vercel**, **Render**, and **Supabase**. The **`Capstone Flow Session.md`** blueprint in the previous folder lists entities and the demo path. This lesson is where security becomes **concrete**—you plan **authentication**, **JWT**, **RBAC**, **middleware**, **rate limiting**, and **API contracts** before the frontend and backend build weeks.

You are learning **auth as a system** for the first time in the capstone track. Earlier backend labs used API keys in query params for notices; CampusBite uses **logged-in users** with **roles** and **row-level access**. The browser may store a token in **`localStorage`**, but **every rule is enforced again on the server**.

## What you will learn in this lesson

- **Authentication vs authorization** — who you are vs what you may do
- **JWT** — signed token, claims, expiry, Bearer header
- **RBAC** — customer, restaurant_owner, delivery_partner
- **Register/login contracts** — including optional **`profile_image_url`** (HTTPS only, no file upload)
- **API endpoint planning** — methods, paths, payloads, pagination, filters
- **Middleware & rate limiting** — planned in HLD/LLD and documented per route
- **Security checklist** — CORS, hashing, 401/403/409/429 responses
- **Hands-on** — RBAC matrix + JWT payload design + two endpoint contracts on paper

Connecting idea: Architecture named the actors; today you write the **rules of the door**—who enters which room with which key.

---

## Authentication and authorization

- **Official Definition:** **Authentication** verifies identity; **authorization** decides whether that identity may perform an action on a resource.
- **In Simple Words:** Login proves **who** you are; RBAC proves **what** you’re allowed to touch.
- **Real-Life Example:** College ID at the gate (auth) vs hostel wing access (authz).

| Term | CampusBite meaning |
| --- | --- |
| **Credential** | Email + password at login |
| **Session alternative** | **JWT** stored client-side for capstone |
| **Principal** | The user id inside the token (`sub`) |
| **Resource** | An order, menu row, review |

**Need:** Delivery partners must not list another partner’s orders even if they guess an order id.

**Common mistake:** Hiding a button in HTML and assuming the API is safe.

### Activity — two failures

Write one sentence each: what happens if (a) token is missing, (b) token is valid but role is `customer` calling owner route.

---

## JWT (JSON Web Token) for CampusBite

- **Official Definition:** A **JWT** is a compact, signed string encoding **claims** (JSON fields) so the server can verify integrity without storing session state in memory.
- **In Simple Words:** A tamper-evident **ID card** the server issued; you show it on each request.
- **Real-Life Example:** Laminated fest pass with expiry date printed on it.

**Capstone JWT contents (claims)**

| Claim | Purpose |
| --- | --- |
| `sub` | User id (string or int) |
| `role` | `customer` \| `restaurant_owner` \| `delivery_partner` |
| `restaurant_id` | Present for owners; null for others |
| `exp` | Expiry unix time |
| `iat` | Issued-at (optional) |

**Transport**

```http
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Server flow**

1. Login validates password hash.
2. Server signs JWT with **`JWT_SECRET`** from Render env.
3. Client stores `access_token` in **`localStorage`**.
4. Client attaches header on each `fetch`.
5. Dependency `get_current_user` decodes JWT, loads user, raises **401** if invalid/expired.

**Frontend on 401**

- Clear `localStorage` token and redirect to login page.
- Show “Session expired—please log in again.”

**Common doubt:** “Is JWT in localStorage safe?” — For learning/demo yes with HTTPS; production often prefers httpOnly cookies. Document the trade-off in README.

Connecting idea: JWT proves identity; **RBAC** maps role to routes.

---

## Register and login API contracts

**No file uploads.** Profile photos use a **URL string** the user pastes at signup (e.g. hosted image link).

### `POST /auth/register`

**Request body (Pydantic)**

```json
{
  "email": "riya@campus.test",
  "password": "StrongPass123",
  "full_name": "Riya Sharma",
  "role": "customer",
  "profile_image_url": "https://example.com/avatars/riya.png"
}
```

| Field | Validation |
| --- | --- |
| `email` | Valid email, unique |
| `password` | Min length 8 (document exact rule) |
| `role` | For v1 demo, restrict register to `customer` only; owners/partners seeded by mentor |
| `profile_image_url` | Optional; must start with `https://` if present |

**Response 201**

```json
{
  "access_token": "<jwt>",
  "token_type": "bearer",
  "role": "customer",
  "user": {
    "id": 1,
    "email": "riya@campus.test",
    "full_name": "Riya Sharma",
    "profile_image_url": "https://example.com/avatars/riya.png"
  }
}
```

### `POST /auth/login`

**Request**

```json
{ "email": "riya@campus.test", "password": "StrongPass123" }
```

**Response 200** — same token shape as register.

**Errors**

| Code | When |
| --- | --- |
| 401 | Wrong password |
| 422 | Invalid email format |
| 429 | Rate limit (see below) |

### `GET /auth/me`

Returns current user from JWT—used to paint navbar avatar from **`profile_image_url`**.

---

## Password security

| Rule | Implementation |
| --- | --- |
| Never store plain password | `password_hash` column only |
| Hash on register | passlib bcrypt or equivalent |
| Verify on login | constant-time compare via library |
| Never log password | Not even in debug |

**Common mistake:** Returning password hash in `/auth/me` JSON.

---

## RBAC matrix (planning artefact)

Fill this table in your team doc—Session 46 implements it in code.

| Route | public | customer | restaurant_owner | delivery_partner |
| --- | --- | --- | --- | --- |
| `GET /restaurants` | ✓ | ✓ | ✓ | ✓ |
| `POST /orders` | | ✓ | | |
| `GET /orders/me` | | ✓ (own) | | |
| `GET /orders/{id}` | | ✓ (own + items) | | |
| `GET /restaurant/orders` | | | ✓ (own restaurant) | |
| `PATCH /restaurant/orders/{id}/status` | | | ✓ | |
| `PATCH /restaurant/orders/{id}/assign` | | | ✓ | |
| `GET /delivery/orders` | | | | ✓ (assigned) |
| `POST /ai/orders/insights` | | ✓ | | |

**Row-level checks (examples)**

- Owner: `order.restaurant_id == current_user.restaurant_id`
- Partner: `order.delivery_partner_id == current_user.id`
- Customer: `order.customer_id == current_user.id`

**403 vs 404**

- **404** when resource does not exist OR exists but must be hidden from this user (pick team policy; many APIs use 404 to avoid leaking ids).
- **403** when user is known but role forbids action.

### Activity — fill one row

Add RBAC row for `POST /orders/{id}/return-request` and write the row-level rule in one sentence.

---

## API endpoint planning (CampusBite index)

Use **`Capstone Flow Session.md` §12** as master list. This lesson adds **contract detail** for high-traffic routes.

### Order detail (JOIN teaching point)

**`GET /orders/{id}`** response must include line items:

```json
{
  "id": 42,
  "status": "DELIVERED",
  "payment_status": "mock_paid",
  "return_status": "none",
  "subtotal_inr": 320.0,
  "items": [
    {
      "item_name_snapshot": "Masala Dosa",
      "unit_price_snapshot": 80.0,
      "quantity": 2
    }
  ]
}
```

### List pagination & filters

| Endpoint | Query params |
| --- | --- |
| `GET /orders/me` | `status`, `page`, `limit`, `from_date`, `to_date` |
| `GET /restaurant/orders` | same + `assigned=true/false` |
| `GET /delivery/orders` | `status`, `page`, `limit` |
| `GET /restaurants/{id}/menu` | `q` (search name), `max_price` |

**Default:** `page=1`, `limit=20`, max `limit=50`.

### Owner helpers

| Endpoint | Purpose |
| --- | --- |
| `GET /restaurant/delivery-partners` | Dropdown for assign |
| `GET /restaurant/stats` | COUNT by status, optional today filter |
| `GET /restaurant/reminders` | Stale order banner data |

### Stats example response

```json
{
  "orders_today": 12,
  "by_status": { "PLACED": 2, "PREPARING": 3, "DELIVERED": 7 },
  "avg_rating": 4.3
}
```

Uses **GROUP BY** you practiced in SQL lessons.

---

## Request/response design habits

| Habit | Why |
| --- | --- |
| Stable JSON keys | Frontend on Vercel does not break silently |
| ISO dates in JSON | `placed_at` as UTC string |
| Money as number | `subtotal_inr` with 2 decimal places in docs |
| Error body shape | `{ "detail": "human readable" }` FastAPI default |

**Validation examples (422)**

| Endpoint | Rule |
| --- | --- |
| Review | `rating` integer 1–5 |
| Order create | each `quantity` >= 1 |
| Return request | `reason` min 10 chars |
| Register | `profile_image_url` https only |

**Conflict (409)**

- Cancel order not in `PLACED`
- Invalid status transition
- Review twice on same order

---

## Middleware (HLD / LLD + implementation plan)

- **Official Definition:** **Middleware** runs on every request before/after your route handler.
- **In Simple Words:** Security guard and reception log at the building entrance.
- **Real-Life Example:** Every visitor signs the register before entering the office.

**CampusBite planned middleware**

| Middleware | Action |
| --- | --- |
| Request log | method, path, status code, duration ms |
| CORS | Already via `CORSMiddleware`—list Vercel origin explicitly |

**LLD diagram addition**

```text
Client -> [CORS] -> [Log middleware] -> [Rate limiter on /auth/* and /ai/*] -> Route handler
```

Document in team HLD before Session 46 coding.

---

## Rate limiting (plan)

- **Official Definition:** **Rate limiting** caps how many requests a client may make in a time window.
- **In Simple Words:** “Only N login tries per minute.”
- **Real-Life Example:** ATM wrong-PIN lockout.

| Route group | Suggested cap (teaching) | Response |
| --- | --- | --- |
| `POST /auth/login` | 10 / minute / IP | 429 |
| `POST /auth/register` | 5 / minute / IP | 429 |
| `POST /ai/orders/insights` | 10 / hour / user id | 429 |

**429 body**

```json
{ "detail": "Too many requests. Try again later." }
```

**Note:** In-memory limiter is fine for Render single instance demo; document limitation in README.

**Common mistake:** Rate limiting only on frontend—bots skip UI.

---

## CORS and secrets (deployment planning)

| Variable | Where |
| --- | --- |
| `DATABASE_URL` | Render only |
| `JWT_SECRET` | Render only |
| `GEMINI_API_KEY` | Render only |
| `CORS_ORIGINS` | Render, comma-separated Vercel URL |
| `API_BASE_URL` | Vercel env for frontend JS |

**Never** commit `.env` to Git.

---

## Full code sketch: JWT dependency (implementation preview)

```python
from datetime import datetime, timedelta, timezone  # Time helpers for JWT expiry
from typing import Annotated  # Type alias for Depends

import jwt  # PyJWT library for encode/decode
from fastapi import Depends, HTTPException, status  # Web framework errors
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer  # Bearer header

from app.config import JWT_SECRET, JWT_ALGORITHM  # Settings from environment
from app.db import get_db  # Database session dependency
from app.models import User  # SQLAlchemy user model

security = HTTPBearer()  # Reads Authorization: Bearer header


def create_access_token(user: User) -> str:  # Called after successful login
    expire = datetime.now(timezone.utc) + timedelta(hours=8)  # Token lifetime
    payload = {  # Claims stored inside JWT
        "sub": str(user.id),  # Subject = user id
        "role": user.role,  # RBAC role string
        "restaurant_id": user.restaurant_id,  # Owner scope
        "exp": expire,  # Expiry claim
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)  # Signed token


def get_current_user(
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)],  # Bearer token
    db: Annotated[Session, Depends(get_db)],  # DB session
) -> User:
    token = credentials.credentials  # Raw JWT string from header
    try:
        data = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])  # Verify signature
    except jwt.PyJWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")  # Reject
    user_id = int(data["sub"])  # Parse subject
    user = db.get(User, user_id)  # Load user row
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")  # Reject
    return user  # Inject into route


def require_roles(*roles: str):  # Factory for RBAC dependencies
    def checker(user: Annotated[User, Depends(get_current_user)]) -> User:
        if user.role not in roles:  # Role not allowed
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")  # Stop
        return user  # Allowed

    return checker  # Use as Depends(require_roles("restaurant_owner"))
```

**How the code works**

- **`HTTPBearer`** expects `Authorization: Bearer <token>`.
- **`get_current_user`** centralises JWT verification.
- **`require_roles`** wraps routes like owner menu CRUD.

---

## AI route contract (plan only)

**`POST /ai/orders/insights`** — customer only, rate limited.

**Request**

```json
{
  "prompt_type": "summary",
  "question": "Summarise my last 5 orders and total spend"
}
```

**Server behaviour (design)**

1. Load last N orders + items for `current_user` only.
2. Build `ORDER_CONTEXT` text block.
3. Call Gemini with “answer only from context.”
4. Return `{ "answer": "..." }`.

No embeddings; no file upload.

---

## Security checklist (team sign-off)

| Item | Done? |
| --- | --- |
| RBAC matrix complete | |
| JWT claims documented | |
| Password hashing chosen | |
| 401/403/409/429 documented per route | |
| CORS origins listed | |
| Rate limits on login + AI | |
| `profile_image_url` https validation | |
| Order detail includes items | |
| Partner list endpoint for assign | |
| Pagination on order lists | |

---

## Hands-on checklist

1. Complete RBAC matrix for all §12 routes in flow doc.
2. Write register/login JSON examples with `profile_image_url`.
3. Draw middleware + rate limit on your HLD.
4. Document three 409 cases for orders.
5. Draft `GET /orders/{id}` response with two line items.
6. List env vars for Render vs Vercel in a table.

---

## Key Takeaways

- **JWT + RBAC** are the capstone security backbone—localStorage is storage, not enforcement.
- **Register** accepts **profile image URLs**, not uploaded files.
- **API contracts** (pagination, filters, order items, stats, partner list) prevent frontend/backend drift.
- **Middleware and rate limiting** belong in the architecture plan and ship with the backend.
- Next lessons **build** the Vercel UI and Render API using this document as law.

## Important Commands, Libraries, Terminologies used

| Name | Meaning in this lesson |
| --- | --- |
| **Authentication** | Proving user identity |
| **Authorization** | Permitting actions on resources |
| **JWT** | Signed token with claims |
| **Bearer token** | `Authorization: Bearer ...` header |
| **RBAC** | Role-based access control |
| **`sub` claim** | User id inside JWT |
| **`exp` claim** | Token expiry time |
| **401 Unauthorized** | Missing/invalid token |
| **403 Forbidden** | Valid user, wrong role |
| **409 Conflict** | Illegal state transition |
| **429 Too Many Requests** | Rate limit hit |
| **`profile_image_url`** | HTTPS avatar link at register |
| **Row-level security** | Filter SQL by owner/customer/partner |
| **Pagination** | `page` and `limit` query params |
| **Middleware** | Code running before each route |
| **Rate limiting** | Cap requests per IP/user |
| **CORS** | Browser cross-origin permission |
| **`HTTPBearer`** | FastAPI Bearer auth extractor |
| **`get_current_user`** | JWT verification dependency |
| **CampusBite** | Cohort capstone product name |
| **`/ai/orders/insights`** | Gemini summary over user’s orders |
