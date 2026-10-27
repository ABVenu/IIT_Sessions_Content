# Capstone Project III – Agents & Full-Stack Integration

**CampusBite** has a **Vercel** UI and a **Render** API on **Supabase**. Individually they almost work; together they fail at **CORS**, **wrong JSON keys**, or **401** headers. This lesson completes **end-to-end** flows and adds **customer AI**: summarise or get insights on **your orders** using **Gemini** with data loaded from the database—no embeddings, no file uploads.

Applied **AI** here means a **server feature** your UI calls—not an autonomous agent placing orders.

## What you will learn in this lesson

- **Full-stack integration** — point Vercel `API_BASE_URL` to Render
- **Debug boundary bugs** — Network tab, logs, CORS
- **E2E gold path** — place → kitchen → deliver → review → return/refund
- **`POST /ai/orders/insights`** — context building + Gemini + rate limit
- **Graceful degradation** — app works if AI returns 503
- **Mentor integration milestone**

Connecting idea: Layers are instruments; integration is the **sound check** before demo day.

---

## Integration checklist

| Step | Check |
| --- | --- |
| Vercel env | `CAMPUS_BITE_API=https://your-app.onrender.com` |
| Render CORS | Includes `https://your-project.vercel.app` |
| HTTPS only | Mixed content blocked if API is http on prod |
| JWT on all protected routes | `apiFetch` attaches Bearer |
| Role pages | Customer cannot open owner URLs |

### Activity — five-box diagram

Draw: Browser → Render API → Supabase → Gemini. Mark where JWT is checked and where API key lives.

---

## Common integration defects

| Symptom | Layer | Fix |
| --- | --- | --- |
| CORS error in console | Config | Update `CORS_ORIGINS`, redeploy Render |
| 401 on every call | Auth | Token key name; expired JWT |
| 403 on owner route | RBAC | User missing `restaurant_id` |
| 200 but empty UI | Frontend | Parse `items` not `order_items` if contract differs |
| HTML error page | Backend | Crash—read Render logs |

**Rule:** Fix **one layer at a time**—do not rewrite entire app.

---

## E2E gold path (demo rehearsal)

Follow **`Capstone Flow Session.md` §11**:

1. Customer registers with **profile_image_url** → menu → cart → **place order** (`mock_paid`).
2. Owner **accepts → preparing → ready** → **assign** partner from dropdown.
3. Partner **out for delivery → delivered**.
4. Customer **review** (rating 1–5).
5. Customer **return request** with reason.
6. Owner **approves** → `refunded` + ledger credit.
7. Customer tries **cancel** on delivered → **409** toast.

Record screen recording backup for fest-day network issues.

---

## AI feature: order insights (no embeddings)

- **Official Definition:** **Retrieval-augmented style prompt** here means you **fetch rows from your DB** and paste them into the model context—no vector database.
- **In Simple Words:** The server shows Gemini **your real order printout**, then asks the question.
- **Real-Life Example:** Accountant opens your ledger before answering “how much did I spend?”

**Route:** `POST /ai/orders/insights`

**Request body**

```json
{
  "prompt_type": "summary",
  "question": "Summarise my last 5 orders and highlight anything still not delivered"
}
```

| `prompt_type` | Server behaviour |
| --- | --- |
| `summary` | Default question if `question` empty |
| `insights` | Uses `question` field |

---

## Full backend route (insights)

```python
import httpx  # HTTP client for Gemini
import os  # Environment variables

from fastapi import APIRouter, Depends, HTTPException  # Router and errors
from sqlalchemy import select  # Query builder
from sqlalchemy.orm import Session  # DB session type

from app.deps import get_current_user, get_db  # Auth dependencies
from app.models import Order, OrderItem, User  # ORM models
from app.rate_limit import rate_limit  # Rate limit helper
from app.schemas import InsightsIn, InsightsOut  # Pydantic models

router = APIRouter(prefix="/ai", tags=["ai"])  # AI routes group


def build_order_context(db: Session, user_id: int, limit: int = 10) -> str:
    orders = db.execute(
        select(Order).where(Order.customer_id == user_id).order_by(Order.placed_at.desc()).limit(limit)
    ).scalars().all()  # Recent orders only
    chunks = []  # Text blocks
    for order in orders:  # Each order
        items = db.execute(select(OrderItem).where(OrderItem.order_id == order.id)).scalars().all()  # Lines
        line_text = ", ".join(f"{i.item_name_snapshot} x{i.quantity}" for i in items)  # Readable items
        chunks.append(
            f"Order {order.id}: status={order.status}, payment={order.payment_status}, "
            f"total={order.subtotal_inr}, items=[{line_text}]"
        )  # One summary line per order
    return "\n".join(chunks) if chunks else "NO_ORDERS"  # Context string


async def call_gemini(system: str, user: str) -> str:
    key = os.getenv("GEMINI_API_KEY", "").strip()  # Secret on Render
    if not key:
        raise HTTPException(status_code=500, detail="AI not configured")  # Misconfig
    url = (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        "gemini-2.0-flash:generateContent?key=" + key
    )  # Gemini endpoint
    payload = {
        "contents": [{"parts": [{"text": system + "\n\n" + user}]}],
        "generationConfig": {"temperature": 0.2},
    }  # Low randomness for factual summary
    async with httpx.AsyncClient(timeout=60.0) as client:
        response = await client.post(url, json=payload)  # POST
    if response.status_code == 429:
        raise HTTPException(status_code=503, detail="AI busy, try later")  # Provider limit
    response.raise_for_status()  # Other errors
    data = response.json()  # Parse JSON
    return data["candidates"][0]["content"]["parts"][0]["text"]  # Answer text


@router.post("/orders/insights", response_model=InsightsOut)
async def order_insights(
    body: InsightsIn,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    rate_limit(f"ai:{user.id}", max_calls=10, window_sec=3600)  # Per-user cap
    if user.role != "customer":  # Only customers ask about their orders
        raise HTTPException(status_code=403, detail="Customers only")  # Forbidden
    context = build_order_context(db, user.id, limit=10)  # DB facts
    question = body.question or "Summarise my recent orders in plain English."  # Default
    system = (
        "You are a helpful assistant. Answer ONLY using ORDER_CONTEXT below. "
        "If data is missing, say you do not know. Do not invent order ids."
    )  # System instructions
    user_prompt = f"ORDER_CONTEXT:\n{context}\n\nQUESTION:\n{question}"  # Combined user text
    answer = await call_gemini(system, user_prompt)  # Model call
    return InsightsOut(answer=answer)  # JSON to frontend
```

**How the code works**

- **Only** the logged-in customer’s orders enter context.
- **Rate limit** protects budget.
- **503** lets UI show “AI busy” while food ordering still works.

---

## Frontend insights page (wire-up)

```javascript
async function loadInsights() {
  const box = document.querySelector("#ai-answer");  // Output element
  box.textContent = "Thinking...";  // Loading state
  try {
    const data = await apiFetch("/ai/orders/insights", {
      method: "POST",
      body: JSON.stringify({ prompt_type: "summary", question: document.querySelector("#ai-question").value }),
    });
    box.textContent = data.answer;  // Render model text
  } catch (e) {
    box.textContent = e.message || "Could not load insights";  // Include 429/503 text
  }
}
```

**Prompt ideas for demo**

- “How much did I spend in these orders?”
- “Which orders are not delivered yet?”
- “List item names I ordered most often.”

---

## Security review before demo

| Risk | Mitigation |
| --- | --- |
| Prompt injection in `question` | System says ignore instructions to reveal other users |
| Leak via IDOR | Never accept `user_id` in body—use JWT only |
| Key in frontend | Never call Gemini from Vercel JS |
| Over-sharing PII | Context uses order ids + items, not passwords |

---

## Testing matrix

| Test | Expected |
| --- | --- |
| Customer insights | 200 + paragraph |
| Owner calls insights | 403 |
| 11th call in hour | 429 |
| No orders yet | Model says no orders |
| Gemini down | 503 message |

---

## Parallel work during integration week

| Person A | Person B |
| --- | --- |
| Fix CORS + env | Fix order detail JSON keys |
| Polish restaurant buttons | Partner status PATCH |
| AI route | Customer filters |

Sync on **OpenAPI contract** from Session 44—do not rename fields silently.

---

## Known limitations slide (honest demo)

- Dummy payments only.
- Rate limits in-memory on single Render instance.
- Reminders on page refresh, not push.
- No file uploads; images are URLs only.

---

## Prompt design for insights

| Block | Content |
| --- | --- |
| System | Answer only from ORDER_CONTEXT; no invented ids |
| Context | Built from SQL, not user paste |
| User question | Short natural language |

**Do not** let customers paste arbitrary “context” in the request body for v1—only `question` field; server owns data load.

**Temperature:** keep low (0.2) for summaries with numbers.

---

## Layer isolation debugging workflow

1. Reproduce bug in browser Network tab.
2. Copy request URL, status, response JSON.
3. If CORS—fix Render env before touching UI CSS.
4. If 422—compare body to Pydantic schema in Session 44 doc.
5. If 409—read `detail`; update button visibility on frontend.
6. If 500—Render logs and traceback.

### Activity — write a bug ticket

Format: Steps, expected, actual, layer guess (FE/BE/DB/AI).

---

## AI off switch

Frontend toggle or message when `GET /health` includes `ai_enabled: false` if you implement feature flag—customers can still order food.

---

## Data privacy talking point

For demo interviews: explain that insights never send another user’s orders because `customer_id` filter comes from JWT `sub`, not from client input.

---

## Extended E2E edge cases

| Case | Expected |
| --- | --- |
| Customer cancel PLACED | 200, refunded ledger |
| Customer cancel DELIVERED | 409 |
| Owner reject return | return_status rejected |
| Partner wrong order id | 404 |
| Login without token on insights | 401 |

---

## Full-stack timing diagram (conceptual)

```text
Click Place Order -> POST /orders (200) -> Owner refresh -> PATCH status chain
-> Assign -> Partner PATCH -> DELIVERED -> POST review -> POST return-request
-> Owner POST return-decision -> GET /orders/me shows refunded
```

No websocket updates—each role hits **Refresh**.

---

## Gemini error mapping

| Provider | Your API |
| --- | --- |
| 429 | 503 + friendly message |
| 401 key | 500 config (fix env) |
| Timeout | 504 or 503 with retry hint |

---

## Team demo roles rehearsal

| Minute | Action |
| --- | --- |
| 0–1 | Pitch + stack |
| 1–2 | Customer order |
| 2–3 | Kitchen + assign |
| 3–4 | Deliver + review |
| 4–5 | Return + AI summary |

---

## Portfolio README sentence

“Built CampusBite: JWT RBAC, order state machine, Supabase, Render, Vercel, and Gemini insights grounded on SQL order history.”

---

## Integration with reminders

When owner loads dashboard, background job may create reminder—verify `GET /restaurant/reminders` populates banner after leaving order PLACED 15+ minutes in test data.

---

## Contract drift guard

Before merge, diff `docs/Capstone-API-Contract.md` against live `/docs`—field names must match `api.js` payloads.

---

## Return and refund integration (step-by-step)

1. Deliver order until `status=DELIVERED` and `payment_status=mock_paid`.
2. Customer opens order detail—confirm **items[]** names match kitchen reality.
3. Submit return with reason length ≥ 10 characters—expect `return_status=requested`.
4. Owner dashboard filter `return_status=requested`—open decision panel.
5. Approve—customer refreshes **my orders**; `payment_status=refunded`.
6. Optional: query `payment_ledger` in Supabase for `refund_credit` row.
7. Reject path on second test order—customer sees rejected state without refund.

**Common bug:** owner approves but frontend still shows `mock_paid` because UI reads wrong field—align JSON keys with Session 44 contract.

---

## Customer insights copy examples (for UI placeholder)

| Button label | `prompt_type` | Default question if empty |
| --- | --- | --- |
| Summarise recent orders | `summary` | Summarise my last 10 orders in bullet points |
| Spending check | `insights` | How much did I spend in the orders shown? |
| Delivery pending | `insights` | Which orders are not delivered yet? |

Keep buttons disabled until customer has at least one order—show friendly empty state.

---

## Owner and partner during AI demo

- Owner/partner roles should **not** call insights route—verify **403** once in `/docs` for learning.
- Demo focus stays customer-facing AI; kitchen flow is purely REST.

---

## Render + Vercel env sync checklist

| Variable | Platform | Symptom if wrong |
| --- | --- | --- |
| `CAMPUS_BITE_API` | Vercel | All fetch fail host not found |
| `CORS_ORIGINS` | Render | Browser blocks responses |
| `JWT_SECRET` | Render | Login works locally only if secret differs |
| `DATABASE_URL` | Render | 500 on every DB route |

Redeploy **both** after changing pairing.

---

## Performance expectations

- Order list with pagination should return under one second on seeded data.
- Insights route may take 2–5 seconds—show loading text; do not block menu page.

---

## Regression list before mentor sign-off

| # | Test |
| --- | --- |
| 1 | Register with avatar URL |
| 2 | Menu search `q=` |
| 3 | Place order |
| 4 | Full status chain |
| 5 | Assign + deliver |
| 6 | Review |
| 7 | Return approve |
| 8 | Insights |
| 9 | Rate limit login (optional) |
| 10 | 401 logout |

---

## Hands-on checklist

1. Run full gold path on production URLs.
2. Show profile avatar from register on customer navbar.
3. Demonstrate insights summary for seeded orders.
4. Trigger 409 cancel on delivered order in UI.
5. Fix one real bug found during integration and note it in README.
6. Record screen snippet of insights answer for submission appendix.

---

## Key Takeaways

- **Capstone Flow Session.md** remains the feature checklist during integration week—do not add embeddings or uploads mid-sprint without mentor approval.
- **Integration** bugs live at boundaries—test with Network tab and Render logs.
- **AI insights** = DB context + Gemini on the server; **no embeddings** in v1.
- **Rate limits** and **RBAC** apply to AI routes too.
- Core ordering must work when AI is off.
- Next lesson **documents and ships** the deployed capstone for submission.

## Important Commands, Terminologies used

| Name | Meaning |
| --- | --- |
| **E2E** | Full user path across UI, API, DB |
| **ORDER_CONTEXT** | Server-built text from SQL |
| **InsightsOut** | `{ answer: string }` response |
| **503** | AI unavailable / busy |
| **IDOR** | Insecure direct object reference |
| **Gold path** | Mentor demo script |
| **Applied AI** | Product feature, not autonomous agent |
| **CampusBite** | Capstone application |
| **build_order_context** | SQL-to-text for AI |
| **prompt_type** | summary vs insights |
| **Gemini 2.0 Flash** | Model id in URL |
| **temperature 0.2** | Low randomness for facts |
| **Network tab** | Browser integration debug |
| **Render logs** | Backend stack traces |
| **Contract drift** | FE/BE field mismatch |
| **Feature flag** | Optional ai_enabled |
| **Gold path** | Mentor demo script |
| **IDOR** | Insecure direct object reference |
| **Grounding** | Answers tied to SQL context |
| **503** | AI busy response |
| **Parallel integration** | Team split FE/BE fixes |
| **Bug ticket** | Structured defect report |
| **Refresh button** | Polling substitute |
| **return-decision** | End of refund path |
| **JWT sub** | Customer id for queries |
| **Capstone Flow Session.md** | E2E script section |
| **Portfolio line** | Resume one-liner |
| **Insights page** | customer/insights.html |
| **Provider 429** | Mapped to 503 |
| **SQL filter** | customer_id from token |
| **Demo rehearsal** | Role switching practice |
| **Honest limitations** | Demo closing slide |
| **OpenAPI diff** | Contract vs /docs check |
| **Background reminder** | Owner banner integration |
| **Layer guess** | Debug methodology |
| **AI off switch** | Order without Gemini |
| **ORDER_CONTEXT** | Prompt data block |
| **HTTPS prod** | Vercel + Render only in demo |
| **Screen snippet** | Optional submission evidence |
| **Regression list** | Ten-step pre-sign-off tests |
