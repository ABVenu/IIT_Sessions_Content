# Capstone Project II – Backend Development

The **Vercel** frontend sends JWT-backed requests to your API contract. This lesson implements **CampusBite** on **Render** with **Supabase PostgreSQL**: models, auth, RBAC, order state machine, dummy payment ledger, return/refund, stats, middleware, rate limits, and **background reminders** for restaurant admins.

Reference **`Capstone Flow Session.md`** for statuses and tables. Session 44 planned security; today you **enforce** it in Python.

## What you will learn in this lesson

- **Supabase + SQLAlchemy** connection on Render
- **Auth routes** — register/login, bcrypt, JWT
- **RBAC dependencies** — `get_current_user`, `require_roles`
- **Menu and order CRUD** with edge rules
- **`assert_order_transition`** — 409 on illegal changes
- **Aggregates** — restaurant stats (GROUP BY)
- **Middleware** — request logging
- **Rate limiting** — login and AI routes
- **BackgroundTasks** — stale-order reminders
- **Hands-on** — gold-path API in `/docs`

Connecting idea: The frontend is the face; the backend is the **source of truth** that survives restarts.

---

## Backend layout

```text
backend/
  app/
    main.py
    config.py
    db.py
    models.py
    schemas.py
    auth.py
    deps.py
    routes/
      auth.py
      orders.py
      restaurant.py
      delivery.py
      ai.py
    services/
      orders.py
      payments.py
      reminders.py
    middleware.py
    rate_limit.py
  requirements.txt
```

**requirements.txt (core)**

```text
fastapi
uvicorn[standard]
sqlalchemy
psycopg2-binary
python-dotenv
passlib[bcrypt]
pyjwt
httpx
```

**`DATABASE_URL`** — Supabase connection string on Render (SSL).

---

## User model and profile URL

```python
class User(Base):  # SQLAlchemy model
    __tablename__ = "users"  # Table name
    id = Column(Integer, primary_key=True)  # Primary key
    email = Column(String, unique=True, nullable=False)  # Login
    password_hash = Column(String, nullable=False)  # Never plain text
    full_name = Column(String, nullable=False)  # Display name
    role = Column(String, nullable=False)  # customer, restaurant_owner, delivery_partner
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"), nullable=True)  # Owner scope
    profile_image_url = Column(String, nullable=True)  # HTTPS URL only
```

**Register validation (Pydantic)**

```python
from pydantic import BaseModel, HttpUrl, field_validator  # Validation tools


class RegisterIn(BaseModel):  # Request body
    email: str  # Email format checked separately or use EmailStr
    password: str  # Min length in validator
    full_name: str  # Required
    role: str = "customer"  # Default customer
    profile_image_url: HttpUrl | None = None  # Optional HTTPS URL

    @field_validator("password")
    @classmethod
    def password_min(cls, v: str) -> str:
        if len(v) < 8:  # Teaching rule
            raise ValueError("Password must be at least 8 characters")  # 422 response
        return v  # OK
```

---

## Auth routes (summary)

| Route | Logic |
| --- | --- |
| `POST /auth/register` | Hash password, insert user, return JWT |
| `POST /auth/login` | Verify hash, return JWT |
| `GET /auth/me` | Return user from `get_current_user` |

Use **`create_access_token`** from Session 44 pattern.

**Rate limit** `login` and `register` via dependency or middleware (see below).

---

## Order service: transitions

```python
ALLOWED = {  # (current_status, new_status, role)
    ("PLACED", "CANCELLED", "customer"),
    ("PLACED", "ACCEPTED", "restaurant_owner"),
    ("ACCEPTED", "PREPARING", "restaurant_owner"),
    ("PREPARING", "READY", "restaurant_owner"),
    ("READY", "ASSIGNED", "restaurant_owner"),
    ("ASSIGNED", "OUT_FOR_DELIVERY", "delivery_partner"),
    ("OUT_FOR_DELIVERY", "DELIVERED", "delivery_partner"),
}


def assert_order_transition(order, new_status: str, role: str) -> None:  # Raise if illegal
    key = (order.status, new_status, role)  # Tuple lookup
    if key not in ALLOWED:  # Not permitted
        raise HTTPException(status_code=409, detail=f"Cannot move {order.status} to {new_status} as {role}")  # Conflict
```

Extend table for restaurant cancel policy if documented.

---

## Place order + dummy payment

```python
def place_order(db, customer, payload):  # Business function
    subtotal = 0.0  # Running total
    lines = []  # ORM order_items list
    for item in payload.items:  # Each cart line
        dish = db.get(MenuItem, item.menu_item_id)  # Load menu row
        if not dish or not dish.is_available:  # Guard
            raise HTTPException(status_code=400, detail="Dish unavailable")  # Bad request
        subtotal += float(dish.price_inr) * item.quantity  # Math
        lines.append(
            OrderItem(
                menu_item_id=dish.id,
                item_name_snapshot=dish.name,
                unit_price_snapshot=dish.price_inr,
                quantity=item.quantity,
            )
        )  # Snapshot line
    order = Order(
        customer_id=customer.id,
        restaurant_id=payload.restaurant_id,
        status="PLACED",
        payment_status="mock_paid",
        return_status="none",
        delivery_address_text=payload.delivery_address_text,
        subtotal_inr=subtotal,
    )  # New order row
    db.add(order)  # Stage order
    db.flush()  # Get order.id
    for line in lines:
        line.order_id = order.id  # Attach FK
        db.add(line)  # Stage lines
    db.add(
        PaymentLedger(
            order_id=order.id,
            entry_type="mock_charge",
            amount_inr=subtotal,
            note="Dummy payment at place",
            created_by_user_id=customer.id,
        )
    )  # Ledger row
    db.commit()  # Persist
    return order  # Return to route
```

**Customer cancel PLACED only** — set CANCELLED + refund ledger if `mock_paid`.

---

## Order detail with items

```python
@router.get("/orders/{order_id}")  # Customer route example
def get_order(order_id: int, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    order = db.get(Order, order_id)  # Load order
    if not order or order.customer_id != user.id:  # Row-level
        raise HTTPException(status_code=404, detail="Order not found")  # Hide existence
    items = db.execute(select(OrderItem).where(OrderItem.order_id == order.id)).scalars().all()  # JOIN via query
    return OrderDetailOut.from_orm_with_items(order, items)  # Pydantic response
```

---

## Restaurant stats (SQL aggregate)

```python
from sqlalchemy import func, select  # Aggregate helpers


def restaurant_stats(db, restaurant_id: int):
    today = func.date(Order.placed_at) == func.current_date()  # Today filter example
    counts = db.execute(
        select(Order.status, func.count())
        .where(Order.restaurant_id == restaurant_id)
        .group_by(Order.status)
    ).all()  # GROUP BY status
    return {status: count for status, count in counts}  # Dict for JSON
```

**Avg rating** — `func.avg(Review.rating)` join orders for restaurant.

---

## Delivery partners list

```python
@router.get("/restaurant/delivery-partners")
def list_partners(user: User = Depends(require_roles("restaurant_owner")), db: Session = Depends(get_db)):
    rows = db.execute(select(User).where(User.role == "delivery_partner")).scalars().all()  # All partners
    return [{"id": u.id, "full_name": u.full_name, "profile_image_url": u.profile_image_url} for u in rows]  # Dropdown JSON
```

---

## Return and refund (owner)

On approve: `return_status=approved`, `payment_status=refunded`, ledger `refund_credit` for `subtotal_inr`.

On reject: `return_status=rejected`, keep `mock_paid`.

---

## Middleware (logging)

```python
import time  # For duration ms
from starlette.requests import Request  # Request type


@app.middleware("http")  # Register middleware
async def log_requests(request: Request, call_next):  # Wrap each request
    start = time.perf_counter()  # Start timer
    response = await call_next(request)  # Run route
    ms = (time.perf_counter() - start) * 1000  # Elapsed
    print(f"{request.method} {request.url.path} -> {response.status_code} ({ms:.1f}ms)")  # Simple log
    return response  # Pass response through
```

Document in README—Render logs capture stdout.

---

## Rate limiting (in-memory sketch)

```python
from collections import defaultdict  # IP -> timestamps list
import time  # Unix time

HITS: dict[str, list[float]] = defaultdict(list)  # Module-level store


def rate_limit(key: str, max_calls: int, window_sec: int) -> None:  # Raise if exceeded
    now = time.time()  # Current time
    HITS[key] = [t for t in HITS[key] if now - t < window_sec]  # Drop old hits
    if len(HITS[key]) >= max_calls:  # Over limit
        raise HTTPException(status_code=429, detail="Too many requests")  # Stop
    HITS[key].append(now)  # Record hit
```

Call `rate_limit(request.client.host, 10, 60)` on login route.

For AI: key = `f"ai:{user.id}"`, 10 per hour.

---

## Background admin reminders

```python
from fastapi import BackgroundTasks  # FastAPI background helper


def check_stale_orders(db, restaurant_id: int) -> None:  # Runs after response sent
    stale = db.execute(
        select(Order).where(
            Order.restaurant_id == restaurant_id,
            Order.status.in_(["PLACED", "ACCEPTED"]),
            Order.updated_at < func.now() - text("interval '15 minutes'"),
        )
    ).scalars().all()  # Old orders
    for order in stale:
        db.add(
            AdminReminderLog(
                order_id=order.id,
                restaurant_id=restaurant_id,
                message=f"Order #{order.id} still {order.status} — please update status",
            )
        )  # Log reminder
    db.commit()  # Save logs


@router.get("/restaurant/orders")
def list_orders(background_tasks: BackgroundTasks, user: User = Depends(require_roles("restaurant_owner")), db: Session = Depends(get_db)):
    background_tasks.add_task(check_stale_orders, db, user.restaurant_id)  # Schedule nudge
    # ... return order list
```

Partner refreshes dashboard to see banner from `GET /restaurant/reminders`.

---

## CORS on Render

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("CORS_ORIGINS", "").split(","),  # Vercel URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## Seed script

- 1 restaurant, 1 owner, 2 delivery partners, 1 customer, 5 menu items.
- Document emails/passwords in README for demo.

---

## Menu routes (owner)

```python
@router.post("/restaurant/menu-items")
def create_item(payload: MenuItemIn, user: User = Depends(require_roles("restaurant_owner")), db: Session = Depends(get_db)):
    item = MenuItem(restaurant_id=user.restaurant_id, **payload.model_dump())  # Scope restaurant
    db.add(item)  # Insert
    db.commit()  # Save
    return item  # Response


@router.get("/restaurants/{rid}/menu")
def public_menu(rid: int, q: str | None = None, max_price: float | None = None, db: Session = Depends(get_db)):
    stmt = select(MenuItem).where(MenuItem.restaurant_id == rid, MenuItem.is_available == True)  # Base query
    if q:
        stmt = stmt.where(MenuItem.name.ilike(f"%{q}%"))  # Search filter
    if max_price is not None:
        stmt = stmt.where(MenuItem.price_inr <= max_price)  # Price ceiling
    return db.execute(stmt).scalars().all()  # List dishes
```

---

## Review endpoint validation

```python
class ReviewIn(BaseModel):
    rating: int  # Star score
    comment: str | None = None  # Optional text

    @field_validator("rating")
    @classmethod
    def rating_range(cls, v: int) -> int:
        if v < 1 or v > 5:  # Enforce range
            raise ValueError("rating must be 1-5")  # 422
        return v  # OK
```

Reject review if order not `DELIVERED` or duplicate review exists—**409**.

---

## Pagination helper

```python
def paginate(stmt, page: int, limit: int):
    page = max(page, 1)  # Floor page
    limit = min(max(limit, 1), 50)  # Cap limit
    total = db.execute(select(func.count()).select_from(stmt.subquery())).scalar()  # Count
    rows = db.execute(stmt.offset((page - 1) * limit).limit(limit)).scalars().all()  # Page slice
    return rows, {"page": page, "limit": limit, "total_pages": (total + limit - 1) // limit}  # Meta
```

---

## Delivery status route

```python
@router.patch("/delivery/orders/{order_id}/status")
def partner_status(order_id: int, payload: StatusIn, user: User = Depends(require_roles("delivery_partner")), db: Session = Depends(get_db)):
    order = db.get(Order, order_id)  # Load
    if not order or order.delivery_partner_id != user.id:  # Must be assignee
        raise HTTPException(status_code=404, detail="Order not found")  # Hide
    assert_order_transition(order, payload.status, user.role)  # Guard
    order.status = payload.status  # Apply
    db.commit()  # Save
    return order  # JSON
```

---

## Local vs Supabase

| Mode | DATABASE_URL |
| --- | --- |
| Local dev | Supabase dev project or local Postgres |
| Render prod | Supabase prod connection string |

Use same models—avoid SQLite-only types in production.

### Activity — 409 test

In `/docs`, try partner marking DELIVERED on unassigned order. Confirm **409** body explains rule.

---

## Hands-on checklist

1. Connect Supabase; run migrations/create tables.
2. Register customer with `profile_image_url`; verify in DB.
3. Place order; confirm ledger `mock_charge`.
4. Illegal transition returns **409**.
5. `GET /orders/{id}` returns items array.
6. Stats endpoint returns counts by status.
7. Trigger rate limit on login in dev.
8. Load restaurant orders twice; see reminder log row.

---

## Key Takeaways

- **Supabase** persists orders; Render serves FastAPI with secrets.
- **RBAC + transitions** belong in services, not scattered in routes.
- **Middleware and rate limits** match Session 44 plan.
- **BackgroundTasks** nudge owners without websockets.
- Next lesson **wires Vercel to Render** and ships **AI order insights**.

## Important Commands, Terminologies used

| Name | Meaning |
| --- | --- |
| **Supabase** | Hosted PostgreSQL |
| **Render** | Backend host |
| **assert_order_transition** | Central status guard |
| **PaymentLedger** | Dummy charge/refund audit |
| **BackgroundTasks** | Post-response jobs |
| **GROUP BY** | Stats aggregation |
| **429** | Rate limit response |
| **profile_image_url** | URL column on users |
| **OrderItem snapshot** | Historical line pricing |
| **AdminReminderLog** | Stale order nudge storage |
| **check_stale_orders** | Background task function |
| **ilike** | Case-insensitive menu search |
| **passlib** | Password hashing library |
| **psycopg2** | Postgres driver for SQLAlchemy |
| **StatusIn** | Pydantic body for status PATCH |
| **MenuItemIn** | Create dish payload |
| **return-decision** | Owner approve/reject return |
| **refund_credit** | Ledger entry on approve |
| **require_roles** | RBAC dependency factory |
| **func.count** | SQL aggregate helper |
| **SSL mode** | Supabase require ssl |
| **Render logs** | stdout from middleware |
| **Seed script** | Demo users and menu |
| **create_all** | Teaching table creation |
| **409** | Illegal transition response |
| **Capstone Flow Session.md** | Status and schema source |
