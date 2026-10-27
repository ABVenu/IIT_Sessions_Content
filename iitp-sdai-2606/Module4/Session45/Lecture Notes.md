# Capstone Project I – Frontend Development

You planned **CampusBite** security and APIs in the previous lesson: **JWT** in **`localStorage`**, **RBAC**, pagination, order detail with **items**, and customer **AI insights** later on the server. This lesson builds the **Vercel-hosted** frontend: HTML/CSS/vanilla JS pages for **customer**, **restaurant owner**, and **delivery partner**, wired to your API contract (mock or early Render URL).

No file uploads—avatars use **`profile_image_url`** from register. Dashboards use **filters** and **Refresh**, not websockets.

## What you will learn in this lesson

- **Frontend structure** for a multi-role capstone
- **`api.js`** — `API_BASE_URL`, Bearer headers, 401 handling
- **Customer UI** — menu search, cart, checkout, my orders, review/return
- **Restaurant UI** — order queue, status buttons, assign partner, menu CRUD, reminders banner
- **Delivery UI** — assigned orders, status updates
- **Profile images** — render URL from auth response
- **Mentor milestone** — one role flow complete in browser

Connecting idea: Session 44 wrote the contract; today you build the screens that **consume** it.

---

## Project layout on Vercel

```text
frontend/
  index.html          # landing / role redirect
  login.html
  register.html
  customer/
    menu.html
    orders.html
    insights.html     # AI panel (calls API when backend ready)
  restaurant/
    dashboard.html
    menu-manage.html
  delivery/
    dashboard.html
  css/styles.css
  js/api.js
  js/auth.js
  js/cart.js
```

**`API_BASE_URL`**

```javascript
const API_BASE_URL = window.CAMPUS_BITE_API || "http://127.0.0.1:8000";  // Vercel env injects prod URL
```

Set in Vercel project settings as build env or inline script in `index.html` for static sites.

---

## Auth helpers (`auth.js`)

- **Official Definition:** **Client-side auth state** holds the token and role for UI routing; it does not replace server RBAC.
- **In Simple Words:** Your browser remembers the pass; the bouncer still checks it.
- **Real-Life Example:** Wristband colour tells you which counter to join.

```javascript
function saveAuth(payload) {  // After login/register
  localStorage.setItem("access_token", payload.access_token);  // JWT string
  localStorage.setItem("role", payload.role);  // customer | restaurant_owner | delivery_partner
  localStorage.setItem("user_json", JSON.stringify(payload.user));  // Includes profile_image_url
}

function getToken() {
  return localStorage.getItem("access_token");  // May be null
}

function clearAuth() {
  localStorage.removeItem("access_token");  // Logout
  localStorage.removeItem("role");
  localStorage.removeItem("user_json");
}

function requireRole(expectedRole) {
  const role = localStorage.getItem("role");  // Current role
  if (role !== expectedRole) {
    window.location.href = "/login.html";  // Redirect intruders
  }
}
```

**Profile avatar**

```javascript
function renderNavbarUser() {
  const user = JSON.parse(localStorage.getItem("user_json") || "{}");  // Parse stored user
  const img = document.querySelector("#nav-avatar");  // img element in navbar
  if (img && user.profile_image_url) {
    img.src = user.profile_image_url;  // Show HTTPS URL from register
    img.alt = user.full_name || "Profile";  // Accessibility
  }
}
```

### Activity — logout path

Add a logout button that calls `clearAuth()` and redirects to `login.html`. Confirm back button does not restore token without login.

---

## API wrapper (`api.js`)

```javascript
async function apiFetch(path, options = {}) {
  const headers = { "Content-Type": "application/json", ...(options.headers || {}) };  // Default JSON
  const token = getToken();  // Read JWT
  if (token) headers["Authorization"] = `Bearer ${token}`;  // Attach Bearer
  const response = await fetch(`${API_BASE_URL}${path}`, { ...options, headers });  // Call Render API
  if (response.status === 401) {
    clearAuth();  // Expired or invalid token
    window.location.href = "/login.html";  // Force re-login
    throw new Error("Unauthorized");  // Stop caller
  }
  if (!response.ok) {
    const err = await response.json().catch(() => ({}));  // Parse FastAPI detail
    throw new Error(err.detail || `HTTP ${response.status}`);  // Surface message
  }
  return response.json();  // Happy path
}
```

**How the code works**

- Centralises **401** so every page behaves the same.
- Surfaces **`detail`** from FastAPI validation errors.

---

## Register page

**Form fields:** email, password, full_name, optional **profile image URL** (not a file input).

```javascript
async function handleRegister(event) {
  event.preventDefault();  // No full page reload
  const body = {
    email: document.querySelector("#email").value,
    password: document.querySelector("#password").value,
    full_name: document.querySelector("#full_name").value,
    role: "customer",  // Capstone v1 public register
    profile_image_url: document.querySelector("#profile_image_url").value || null,
  };
  const data = await apiFetch("/auth/register", { method: "POST", body: JSON.stringify(body) });  // POST JSON
  saveAuth(data);  // Store token
  window.location.href = "/customer/menu.html";  // Enter app
}
```

**UX hint:** Show preview `<img>` when URL field blurs and starts with `https://`.

---

## Customer menu and cart

**Menu fetch with filters**

```javascript
async function loadMenu(restaurantId) {
  const q = document.querySelector("#search").value;  // Search text
  const maxPrice = document.querySelector("#max_price").value;  // Optional filter
  const params = new URLSearchParams();  // Query string builder
  if (q) params.set("q", q);
  if (maxPrice) params.set("max_price", maxPrice);
  const menu = await apiFetch(`/restaurants/${restaurantId}/menu?${params}`);  // GET menu
  renderMenuCards(menu);  // Your DOM loop
}
```

**Cart (client-only until checkout)**

- Store `cart` array in `sessionStorage`: `{ menu_item_id, name, price, quantity }`.
- One restaurant per cart—clear cart if user switches restaurant.

**Checkout**

```javascript
async function placeOrder() {
  const cart = JSON.parse(sessionStorage.getItem("cart") || "[]");  // Read cart
  const body = {
    restaurant_id: Number(document.querySelector("#restaurant_id").value),
    delivery_address_text: document.querySelector("#address").value,
    items: cart.map((line) => ({ menu_item_id: line.menu_item_id, quantity: line.quantity })),
  };
  await apiFetch("/orders", { method: "POST", body: JSON.stringify(body) });  // Dummy pay on server
  sessionStorage.removeItem("cart");  // Clear cart
  window.location.href = "/customer/orders.html";  // See my orders
}
```

---

## Customer orders dashboard

| UI control | API |
| --- | --- |
| Status filter dropdown | `GET /orders/me?status=PLACED` |
| Date inputs | `from_date`, `to_date` query params |
| Pagination | `page`, `limit` |
| Order row click | `GET /orders/{id}` shows **items[]** in modal |

**Cancel button**

- Visible only when `status === "PLACED"` (UI hint).
- Calls `PATCH /orders/{id}/cancel`; display **409** message if server rejects.

**Review form (DELIVERED)**

```javascript
await apiFetch(`/orders/${orderId}/review`, {
  method: "POST",
  body: JSON.stringify({ rating: 5, comment: "Hot and fresh" }),
});
```

**Return request**

```javascript
await apiFetch(`/orders/${orderId}/return-request`, {
  method: "POST",
  body: JSON.stringify({ reason: "Wrong item delivered, details in note..." }),
});
```

---

## Restaurant dashboard

**Order queue table**

- Fetch `GET /restaurant/orders?status=&page=1`.
- Buttons call `PATCH /restaurant/orders/{id}/status` with `{ "status": "PREPARING" }` etc.
- **Assign partner:** load `GET /restaurant/delivery-partners`, populate `<select>`, POST assign endpoint.

**Reminders banner**

```javascript
async function loadReminders() {
  const data = await apiFetch("/restaurant/reminders");  // Stale order nudges
  const banner = document.querySelector("#reminder-banner");  // Top alert box
  if (data.items && data.items.length) {
    banner.textContent = data.items[0].message;  // Show latest nudge
    banner.hidden = false;  // Visible
  }
}
```

**Stats cards (optional this week)**

- `GET /restaurant/stats` → render counts by status.

---

## Menu management (owner)

| Action | API |
| --- | --- |
| Add dish | `POST /restaurant/menu-items` |
| Edit | `PATCH /restaurant/menu-items/{id}` |
| Disable | `PATCH` with `is_available: false` |

Optional **dish image**: text field `image_url` (external HTTPS)—not upload.

---

## Delivery partner dashboard

```javascript
async function loadMyDeliveries() {
  const status = document.querySelector("#status-filter").value;  // Filter UI
  const orders = await apiFetch(`/delivery/orders?status=${status}`);  // Scoped to partner
  renderDeliveryTable(orders);  // DOM
}

async function markDelivered(orderId) {
  await apiFetch(`/delivery/orders/${orderId}/status`, {
    method: "PATCH",
    body: JSON.stringify({ status: "DELIVERED" }),
  });
  loadMyDeliveries();  // Refresh table
}
```

---

## AI insights page (customer)

Placeholder UI until Session 47 integration:

```javascript
async function askInsights() {
  const question = document.querySelector("#ai-question").value;  // User text
  const data = await apiFetch("/ai/orders/insights", {
    method: "POST",
    body: JSON.stringify({ prompt_type: "insights", question }),
  });
  document.querySelector("#ai-answer").textContent = data.answer;  // Show model text
}
```

Show friendly message on **429** (rate limit).

---

## CSS and layout

- Use **flexbox/grid** from earlier web modules.
- Role-specific accent colour helps demos (customer blue, kitchen orange, delivery green).
- Tables: responsive scroll on mobile.

### Activity — role guard

Open restaurant dashboard URL as logged-in customer. Confirm `requireRole` redirects to login.

---

## Mock API milestone (if Render not ready)

| Approach | When |
| --- | --- |
| `json-server` or static `mocks/*.json` | Frontend week start |
| Switch `API_BASE_URL` to Render | When backend milestone passes |

Document switch in README.

---

## Common frontend bugs

| Symptom | Fix |
| --- | --- |
| CORS error | Add Vercel URL to Render `CORS_ORIGINS` |
| 401 loop | Check token saved; clock skew rare |
| Empty orders | Wrong role or filter too strict |
| Key mismatch | `delivery_address_text` must match Pydantic field |

---

## Login page

```javascript
async function handleLogin(event) {
  event.preventDefault();  // Keep SPA-like behaviour
  const body = {
    email: document.querySelector("#email").value,  // User email
    password: document.querySelector("#password").value,  // User password
  };
  const data = await apiFetch("/auth/login", { method: "POST", body: JSON.stringify(body) });  // Auth call
  saveAuth(data);  // Persist JWT
  if (data.role === "restaurant_owner") window.location.href = "/restaurant/dashboard.html";  // Route by role
  else if (data.role === "delivery_partner") window.location.href = "/delivery/dashboard.html";  // Partner home
  else window.location.href = "/customer/menu.html";  // Default customer
}
```

**Rate limit UX:** if login throws “Too many requests”, show cooldown message—matches Session 44 plan.

---

## Pagination controls

```javascript
let currentPage = 1;  // Page state

function renderPager(meta) {
  document.querySelector("#page-label").textContent = `Page ${meta.page} of ${meta.total_pages}`;  // Label
  document.querySelector("#prev-page").disabled = meta.page <= 1;  // Disable prev
  document.querySelector("#next-page").disabled = meta.page >= meta.total_pages;  // Disable next
}

async function loadOrdersPage() {
  const status = document.querySelector("#status-filter").value;  // Filter
  const data = await apiFetch(`/orders/me?status=${status}&page=${currentPage}&limit=10`);  // Paged API
  renderOrdersTable(data.items);  // Rows
  renderPager(data.meta);  // Footer
}
```

Backend may return `{ items, meta: { page, limit, total_pages } }`—match Session 44 contract.

---

## Restaurant return decision UI

```javascript
async function decideReturn(orderId, decision) {
  await apiFetch(`/restaurant/orders/${orderId}/return-decision`, {
    method: "POST",
    body: JSON.stringify({ decision, admin_note: document.querySelector("#admin-note").value }),
  });
  loadRestaurantOrders();  // Refresh queue
}
```

Show button only when `return_status === "requested"`.

---

## Accessibility and UX

- Buttons need text, not colour alone, for status.
- Form labels tied to inputs with `for`/`id`.
- Error toasts readable for 409/422 messages from `detail`.

### Activity — mobile table

Make order table horizontally scrollable with CSS `overflow-x: auto` on small screens.

---

## Mentor checkpoint rubric (self-check)

| Criterion | Met? |
| --- | --- |
| Three role home pages exist | |
| JWT attached on protected fetch | |
| 401 redirects to login | |
| Customer can complete cart UI | |
| Owner sees order table | |
| Partner sees only delivery list | |
| Profile image renders from URL | |

---

## Hands-on checklist

1. Register with `profile_image_url` and see avatar in navbar.
2. Build cart + place order against mock or live API.
3. Restaurant page advances one order through READY.
4. Assign partner from dropdown populated by API.
5. Partner marks DELIVERED.
6. Customer leaves review; try cancel on DELIVERED and show error toast.
7. Add filters on at least one dashboard.

---

## Key Takeaways

- **Vercel** hosts static role-based pages; **Render** hosts truth.
- **`api.js` + `auth.js`** patterns repeat across every capstone screen.
- **Profile images** are URLs from signup—no multipart forms.
- Dashboards use **query params** for filters aligned with Session 44 contracts.
- Next lesson implements the **backend** that makes every button real.

## Important Commands, Libraries, Terminologies used

| Name | Meaning in this lesson |
| --- | --- |
| **API_BASE_URL** | Render API root on Vercel |
| **localStorage** | Stores JWT and role |
| **Bearer header** | `Authorization: Bearer <jwt>` |
| **apiFetch** | Wrapper with 401 handling |
| **requireRole** | Client-side page guard |
| **profile_image_url** | Avatar HTTPS link |
| **sessionStorage cart** | Pre-checkout basket |
| **Query params** | Filters and pagination |
| **409 error toast** | Show illegal cancel message |
| **CORS** | Browser cross-origin rule |
| **CampusBite** | Capstone frontend app |
| **return_status** | Column driving return UI buttons |
| **payment_status** | mock_paid / refunded labels in table |
| **Assign partner** | Owner action after READY |
| **Reminder banner** | Stale order nudge from API |
| **Mock API** | Temporary JSON while backend lags |
| **Toast** | Short error message for 409/422 |
| **Role redirect** | Login sends user to correct dashboard |
| **Checkout** | POST /orders from cart |
| **sessionStorage** | Cart persistence per tab |
| **Vercel env** | Injects production API URL |
| **Hard refresh** | Clear cached JS after deploy |
| **Modal** | Order detail with items list |
| **Status filter** | Query param on list endpoints |
| **insights.html** | Customer AI summary page |
| **menu-manage.html** | Owner dish CRUD screen |
| **delivery dashboard** | Partner-only deliveries |
| **409 toast** | Illegal cancel feedback |
| **HTTPS avatar** | profile_image_url in img src |
| **Capstone Flow Session.md** | Blueprint reference in repo |
| **fetch API** | Browser HTTP client used throughout |
