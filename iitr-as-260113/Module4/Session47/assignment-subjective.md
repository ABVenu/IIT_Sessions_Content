# Assignment Subjective

Total Questions: 1  
Difficulty: Medium  
Type: Practical Implementation (n8n — two workflows)

---

## Q1 (Practical, Medium)

**GreenMart** is a grocery delivery startup. Customers place orders for **three products**. Each product’s orders must be stored in a **separate tab** inside one Google Spreadsheet. The store manager also wants a **Get Order Status** action that shows **total orders**, **pending orders**, and **total order value** — using simple counting and addition only (**no LLM**).

Build everything in your **local n8n** instance (Docker on `localhost:5678`).

---

## Big picture (read this first)

You will create **two workflows** and **one Google Spreadsheet**.

| Workflow | Name (suggested) | Trigger | Purpose | Total nodes |
|---|---|---|---|---|
| **Workflow 1** | `GreenMart Place Order` | **On form submission** | Route order to the correct product tab | **5 nodes** |
| **Workflow 2** | `GreenMart Get Order Status` | **Trigger manually** | Read all tabs → compute totals → write summary | **6 nodes** |

**Grand total: 11 nodes** across both workflows (same Google OAuth credential for all Sheets nodes).

![GreenMart assignment big picture — Workflow 1 Place Order routes form submissions via Switch to Rice, Dal, and Oil tabs; Workflow 2 Get Order Status reads all tabs, Python Code computes totals, writes Order Summary](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module4/session47/session47-06-greenmart-assignment-big-picture.png)

### Visual map — Workflow 1

```text
[1] Form: Place Order
        |
        v
[2] Switch: route by product (3 rules)
    |           |           |
    v           v           v
[3] Append    [4] Append    [5] Append
  Rice tab      Dal tab       Oil tab
```

### Visual map — Workflow 2

```text
[1] Manual Trigger
        |
   +----+----+----+
   v    v    v    |
[2] Get [3] Get [4] Get rows (one node per product tab)
 rows   rows   rows
   |    |    |
   +----+----+
        v
[5] Code: count + sum (copy template below)
        |
        v
[6] Append row → Order Summary tab
```

---

## Part A — Google Spreadsheet setup (do this before n8n)

Create one spreadsheet named **`GreenMart Orders`**.

### Tab 1: `Rice Orders`

| email | name | product | quantity | unit_price | order_value | status |
|---|---|---|---|---|---|---|

### Tab 2: `Dal Orders`

Same column headers as above.

### Tab 3: `Oil Orders`

Same column headers as above.

### Tab 4: `Order Summary`

| last_updated | total_orders | pending_orders | total_order_value |
|---|---|---|---|

Leave all tabs empty except the header row.

**Product names (use exactly — spelling matters for Switch rules):**

| Product | Tab name |
|---|---|
| Basmati Rice | Rice Orders |
| Toor Dal | Dal Orders |
| Sunflower Oil | Oil Orders |

---

## Part B — Google OAuth (one time)

If you already connected Google Sheets in practice, reuse the same credential.

1. Google Cloud project → enable **Google Sheets API** + **Google Drive API**
2. OAuth consent screen (External) → add yourself as **test user** if needed
3. Create **Web application** OAuth client → paste n8n redirect URI
4. In n8n: **Credentials → Google Sheets OAuth2** → Client ID + Secret → **Sign in with Google**

---

## Part C — Workflow 1: Place Order (5 nodes)

### Node 1 — On form submission (trigger)

| Setting | Value |
|---|---|
| Workflow name | `GreenMart Place Order` |
| Form title | GreenMart Place Order |
| Authentication | None |
| Respond when | Form is submitted |

**Form fields (create exactly):**

| Field label | Type | Required | Notes |
|---|---|---|---|
| Email | Text (email) | Yes | |
| Name | Text | Yes | |
| Product | Dropdown | Yes | Options: `Basmati Rice`, `Toor Dal`, `Sunflower Oil` |
| Quantity | Number | Yes | Whole number ≥ 1 |
| Unit price | Number | Yes | Price per unit in ₹ |
| Status | Dropdown | Yes | Options: `Pending`, `Completed` |

> **Why unit price on the form?** So `order_value` is a simple multiplication — no LLM, no extra Set nodes.

---

### Node 2 — Switch (route by product)

1. Click **+** after the form → **Flow** → **Switch**
2. Connect: **Form → Switch**
3. Mode: **Rules**
4. Add **3 rules**:

| Rule | Field | Condition | Value | Output |
|---|---|---|---|---|
| 1 | `product` | equals | `Basmati Rice` | Output 0 |
| 2 | `product` | equals | `Toor Dal` | Output 1 |
| 3 | `product` | equals | `Sunflower Oil` | Output 2 |

> **Switch vs IF:** Switch is one node with three exits — like three IF checks in one box. If your n8n version does not show Switch, use **two IF nodes** instead (see **Plan B** at the end).

---

### Nodes 3, 4, 5 — Google Sheets → Append row (one per product tab)

Create **three** Append row nodes. Connect each Switch output to its own Append node:

| Node name (suggested) | Switch output | Sheet tab |
|---|---|---|
| Append Rice Order | Output 0 | `Rice Orders` |
| Append Dal Order | Output 1 | `Dal Orders` |
| Append Oil Order | Output 2 | `Oil Orders` |

**For every Append node, configure the same way:**

1. Credential: your Google Sheets OAuth2
2. Document: `GreenMart Orders`
3. Operation: **Append row**
4. Sheet: the tab from the table above
5. Map columns using **expressions** (drag from form output — do **not** type fixed names):

| Sheet column | Map from |
|---|---|
| `email` | Form → Email |
| `name` | Form → Name |
| `product` | Form → Product |
| `quantity` | Form → Quantity |
| `unit_price` | Form → Unit price |
| `order_value` | **Expression:** `quantity × unit_price` (see below) |
| `status` | Form → Status |

**`order_value` expression (type in the expression editor):**

```text
={{ $json.quantity * $json.unit_price }}
```

6. **Execute step** once per branch (test each product separately) to confirm rows land in the **correct tab**.

---

### Workflow 1 — Test data (run after unpinning form data)

**Unpin** any pinned sample data on the form trigger before final tests.

Execute the **full workflow** three times:

| Run | Email | Name | Product | Qty | Unit price | Status | Expected tab | order_value |
|---|---|---|---|---|---|---|---|---|
| 1 | `ananya@gmail.com` | Ananya | Basmati Rice | 2 | 80 | Pending | Rice Orders | 160 |
| 2 | `rahul@gmail.com` | Rahul | Toor Dal | 1 | 120 | Completed | Dal Orders | 120 |
| 3 | `kavya@gmail.com` | Kavya | Sunflower Oil | 3 | 150 | Pending | Oil Orders | 450 |

After these three runs, your product tabs should have **one row each** in the correct tab (not all in one tab).

---

## Part D — Workflow 2: Get Order Status (6 nodes)

Create a **new workflow** named `GreenMart Get Order Status`.

### Node 1 — Trigger manually

Add **Trigger manually** (Manual Trigger). This is your **Get Order Status** button — click **Execute workflow** to refresh totals.

---

### Nodes 2, 3, 4 — Google Sheets → Get row(s) in sheet

Add **three** separate **Get row(s) in sheet** nodes (all connected from the Manual Trigger).

| Node name (suggested) | Sheet tab | Settings |
|---|---|---|
| Get Rice Rows | `Rice Orders` | Return all rows |
| Get Dal Rows | `Dal Orders` | Return all rows |
| Get Oil Rows | `Oil Orders` | Return all rows |

Connect: **Manual Trigger → all three Get nodes** (one trigger fanning out to three reads).

> Each Get node outputs the rows from its tab. The Code node in the next step will merge them.

---

### Node 5 — Code (Python) — compute totals

1. Add a **Code** node after the three Get nodes
2. Connect **all three Get nodes → Code node** (Code receives items from all tabs)
3. In the Code node, set language to **Python**
4. Paste this code **as-is** (then read the comments to understand it):

```python
from datetime import datetime, timezone

# Collect every order row from all three sheet reads
all_rows = [item.json for item in _input.all()]

# Count total orders
total_orders = len(all_rows)

# Count only rows where status is Pending
pending_orders = sum(
    1 for row in all_rows
    if str(row.get("status", "")).strip() == "Pending"
)

# Sum the order_value column (convert text to number safely)
total_order_value = sum(
    float(row.get("order_value") or 0) for row in all_rows
)

# Return one summary item for the next node
return [
    {
        "json": {
            "last_updated": datetime.now(timezone.utc).isoformat(),
            "total_orders": total_orders,
            "pending_orders": pending_orders,
            "total_order_value": total_order_value,
        }
    }
]
```

> **Note:** n8n’s Code node supports **Python** and **JavaScript**. Use **Python** here — you do not need JavaScript for this assignment.

**What this code does (plain English):**

- Merges rows from Rice + Dal + Oil tabs
- **total_orders** = how many rows exist across all tabs
- **pending_orders** = rows where `status` is exactly `Pending`
- **total_order_value** = sum of all `order_value` cells

---

### Node 6 — Google Sheets → Append row (Order Summary)

1. Operation: **Append row**
2. Document: `GreenMart Orders`
3. Sheet: `Order Summary`
4. Map columns from Code node output:

| Sheet column | Map from Code output |
|---|---|
| `last_updated` | `last_updated` |
| `total_orders` | `total_orders` |
| `pending_orders` | `pending_orders` |
| `total_order_value` | `total_order_value` |

---

### Workflow 2 — Expected result (after Part C test data)

Click **Execute workflow** on `GreenMart Get Order Status`.

**Order Summary** tab should get a new row like:

| last_updated | total_orders | pending_orders | total_order_value |
|---|---|---|---|
| (timestamp) | **3** | **2** | **730** |

**How 730 is calculated:** 160 + 120 + 450 = **730**  
**How 2 pending:** Ananya (Pending) + Kavya (Pending); Rahul is Completed.

Run **Get Order Status** again — a **second summary row** will append (that is OK for this assignment).

---

## Part E — What to submit (Google Doc)

Create a Google Doc with:

1. **Workflow 1 canvas screenshot** — all 5 nodes visible (Form → Switch → 3 Append nodes)
2. **Workflow 2 canvas screenshot** — all 6 nodes visible (Manual → 3 Get → Code → Append)
3. **Spreadsheet screenshot** — all four tabs visible (or one composite image) showing:
   - One order row in each product tab (after 3 test orders)
   - Order Summary row with `3`, `2`, `730`
4. **Execution screenshot** — Switch node highlighting the correct branch for one product
5. Short write-up (**100–150 words**) answering:
   - Why orders go to **separate tabs** instead of one mixed sheet
   - What the **Switch** node does compared to a single Append node
   - How **total_order_value** is calculated (one sentence — no LLM)

### Submission Instruction

- create a google doc in your google drive - suggested folder (for your ref) is module name in that session name in that the submission file
- write properly and neatly after reasearching duly - do add images wherever needed
- once the doc is ready - submit the doc link (click share button and copy the link)
- make sure the sharing settings is `View anyone with the link` (sharing should be public)

---

## Plan B — If Switch node is not available (use 7 nodes instead)

Replace the **Switch** node with **two IF nodes**:

```text
Form
  → IF: product equals "Basmati Rice"?
      true  → Append Rice tab
      false → IF: product equals "Toor Dal"?
                  true  → Append Dal tab
                  false → Append Oil tab
```

| Workflow | Nodes with Plan B |
|---|---|
| Workflow 1 | **7 nodes** (1 Form + 2 IF + 3 Append + still 3 appends) = 1+2+3 = 6... wait: Form + IF + IF + 3 Append = 6 nodes |

Actually: 1 Form + 2 IF + 3 Append = **6 nodes** for Workflow 1 with Plan B.

---

## Common mistakes (save yourself debugging time)

| Mistake | What happens | Fix |
|---|---|---|
| Product spelling mismatch | Switch sends nothing to any tab | Dropdown values must exactly match Switch rules |
| All orders in one tab | Switch not connected to three Append nodes | Each Switch output → its own Append node |
| `order_value` is empty | Hard-coded number instead of expression | Use `={{ $json.quantity * $json.unit_price }}` |
| Pinned form data | Same order repeats | Unpin before final tests |
| Get rows returns header as data | Count is wrong | In Get node, skip header row if option exists; or ensure only data rows return |
| Code node not connected to all 3 Get nodes | Totals count only one tab | Connect Rice + Dal + Oil Get nodes → Code |
| Only Sheets API enabled | OAuth works but Drive fails | Enable **Drive API** too |

---

## Answer Explanation (Ideal Solution Walkthrough)

### Node checklist

| Workflow | # | Node type | Purpose |
|---|---|---|---|
| 1 | 1 | On form submission | Collect order details |
| 1 | 2 | Switch (or 2× IF) | Route by product |
| 1 | 3–5 | Google Sheets Append ×3 | Write to Rice / Dal / Oil tab |
| 2 | 1 | Trigger manually | Run Get Order Status on demand |
| 2 | 2–4 | Google Sheets Get rows ×3 | Read all product tabs |
| 2 | 5 | Code (Python) | Count orders, count pending, sum values |
| 2 | 6 | Google Sheets Append | Write summary row |

### Grading checklist (for evaluators)

| Check | Pass criteria |
|---|---|
| Spreadsheet structure | 4 tabs with correct headers |
| Workflow 1 routing | 3 test orders land in **correct** tabs |
| order_value | Correct arithmetic per row (qty × unit_price) |
| Workflow 2 trigger | Manual trigger runs without form |
| Summary metrics | total_orders=3, pending_orders=2, total_order_value=730 after standard test data |
| No LLM | No AI/LLM nodes used |
| Evidence | Google Doc with both workflow screenshots + sheet proof |

### Alternative approaches

- **Separate spreadsheets per product** instead of tabs — acceptable if routing logic is correct, but **tabs in one sheet** is preferred.
- **Append or update** on Order Summary instead of append — acceptable if latest metrics are visible.
- **Plan B (two IF nodes)** instead of Switch — fully acceptable.
