## HDFC Life Advisor Portal

Create a **Next.js** site for HDFC Life advisors: a static policy catalogue, a server-rendered claims desk, **NextAuth** sign-in, a **Formik + Yup** claim form, **ISR**, and **middleware** that guards `/desk`.

This is a **new project**. You do not need last week's repo.

Use the **Pages Router** (`pages/`). Do **not** use the App Router (`app/`).

- Next.js **14** (Pages Router)
- **JavaScript or TypeScript** — either is fine (`.js` / `.jsx` or `.ts` / `.tsx`)
- **NextAuth.js v4**
- **Formik** + **Yup**
- Tailwind CSS is allowed. Plain CSS is allowed.

Do **not** use a separate Express server. Do **not** use Redux. Do **not** call a live HDFC API — read the seed JSON files in the repo.

---

### Seed data

Commit these files. Do not rename the keys.

`data/policies.json`

```json
[
  { "policyNo": "HDFC-LIFE-1001", "customer": "Anita Sharma", "type": "TERM", "basePremium": 18500, "status": "Active" },
  { "policyNo": "HDFC-LIFE-1002", "customer": "Rahul Mehta", "type": "ULIP", "basePremium": 42000, "status": "Active" },
  { "policyNo": "HDFC-LIFE-1003", "customer": "Priya Nair", "type": "ENDOWMENT", "basePremium": 27000, "status": "Lapsed" },
  { "policyNo": "HDFC-LIFE-1004", "customer": "Vikram Singh", "type": "TERM", "basePremium": 15200, "status": "Active" },
  { "policyNo": "HDFC-LIFE-1005", "customer": "Sneha Patel", "type": "ULIP", "basePremium": 36000, "status": "Active" },
  { "policyNo": "HDFC-LIFE-1006", "customer": "Anita Sharma", "type": "ENDOWMENT", "basePremium": 22000, "status": "Pending" }
]
```

`data/claims.json`

```json
[
  { "claimNo": "CLM-01", "policyNo": "HDFC-LIFE-1001", "customer": "Anita Sharma", "claimAmount": 25000, "urgency": "HIGH", "status": "SUBMITTED" },
  { "claimNo": "CLM-02", "policyNo": "HDFC-LIFE-1002", "customer": "Rahul Mehta", "claimAmount": 18000, "urgency": "MEDIUM", "status": "SUBMITTED" },
  { "claimNo": "CLM-03", "policyNo": "HDFC-LIFE-1005", "customer": "Sneha Patel", "claimAmount": 42000, "urgency": "HIGH", "status": "APPROVED" },
  { "claimNo": "CLM-04", "policyNo": "HDFC-LIFE-1004", "customer": "Vikram Singh", "claimAmount": 15000, "urgency": "LOW", "status": "SUBMITTED" }
]
```

Active policies → **`4`**. TERM + Active → **`2`** (`1001`, `1004`).

---

### 1. File-based routing and layout

Required routes (Pages Router). File names below use `.js`; `.jsx`, `.ts`, and `.tsx` are all accepted.

| File | URL | Role |
| ---- | --- | ---- |
| `pages/index.js` | `/` | Home |
| `pages/policies/index.js` | `/policies` | Policy catalogue |
| `pages/policies/[id].js` | `/policies/HDFC-LIFE-1004` | Policy detail |
| `pages/policies/category/[...slug].js` | `/policies/category/term/active` | Catch-all filter |
| `pages/docs/[[...slug]].js` | `/docs` and `/docs/claims/file` | Optional catch-all |
| `pages/claims/index.js` | `/claims` | Claims list (SSR) |
| `pages/claims/new.js` | `/claims/new` | Formik form |
| `pages/desk/index.js` | `/desk` | Protected advisor desk |
| `pages/auth/signin.js` | `/auth/signin` | Credentials + Google buttons |
| `pages/api/auth/[...nextauth].js` | NextAuth handler | Auth |
| `pages/api/revalidate.js` | On-demand ISR | Secret-gated revalidate |
| `pages/_app.js` | all pages | Shared layout |
| `pages/_document.js` | HTML shell | Required |

`_app.js` must render a header whose visible text is **exactly**:

```text
HDFC Life Advisor Portal
```

Nav must use `<Link>` (not `<a>`) for `/`, `/policies`, `/claims`, `/claims/new`, and `/desk`.

Home (`/`) must show `process.env.NEXT_PUBLIC_COMPANY_NAME` as visible text **`HDFC Life`**.

`_document.js` must set `<html lang="en">`.

---

### 2. Policy catalogue — SSG

`pages/policies/index.js`:

- `getStaticProps` reads `data/policies.json` from disk (`fs` + `path`). Do not fetch HTTP for this page.
- Return `{ props: { policies }, revalidate: 60 }` (ISR, 60 seconds).
- Visible heading: **`Policy Catalogue`**
- Visible count line: **`6 policies`**
- Render all six `policyNo` values. Each row links to `/policies/{policyNo}` with `<Link>`.

`pages/policies/[id].js`:

- `getStaticPaths` returns the six seed `policyNo` values.
- `fallback: false`
- `getStaticProps` loads that one policy. Unknown id → `{ notFound: true }`
- For `/policies/HDFC-LIFE-1004` the page must show all of:

```text
HDFC-LIFE-1004
Vikram Singh
TERM
15200
Active
```

- `useRouter().query.id` must be read in the page component (print it in a line `Policy id: HDFC-LIFE-1004` so the grader can see `useRouter` is used).

---

### 3. Catch-all and optional catch-all

`pages/policies/category/[...slug].js`:

- `slug[0]` is the type in **lowercase** (`term` / `ulip` / `endowment`)
- `slug[1]` if present is the status in **lowercase** (`active` / `lapsed` / `pending`)
- Filter the seed policies (SSG or `getServerSideProps` — your choice, but data must match the seed)
- Heading: **`Policy Category`**
- `/policies/category/term/active` must list **exactly** `HDFC-LIFE-1001` and `HDFC-LIFE-1004` (and no others)
- `/policies/category/ulip` must list **exactly** `HDFC-LIFE-1002` and `HDFC-LIFE-1005`

`pages/docs/[[...slug]].js`:

- `/docs` shows **`Advisor Docs`**
- `/docs/claims/file` shows **`Advisor Docs`** and the joined slug `claims/file`

---

### 4. Claims list — SSR

`pages/claims/index.js` must use **`getServerSideProps`** (not `getStaticProps`).

- Read `data/claims.json` on the server every request
- Heading: **`Claims Desk`**
- Visible count: **`4 claims`**
- First row claim number: **`CLM-01`**
- Last row claim number: **`CLM-04`**

Do not pre-render this page at build time.

---

### 5. Authentication — NextAuth v4

`pages/api/auth/[...nextauth].js` with:

1. **Credentials provider**
   - Email: `advisor@hdfclife.com`
   - Password: `Advisor@123`
   - Compare against an in-memory user. Do not call a database.
   - On success the session user email is `advisor@hdfclife.com` and name is `HDFC Advisor`
2. **Google provider**
   - Wired with `GOOGLE_CLIENT_ID` and `GOOGLE_CLIENT_SECRET`
   - The sign-in page must render a control whose visible text is **`Sign in with Google`**
   - If the env vars are missing, the credentials login must still work

Session strategy: **JWT**.

`pages/desk/index.js`:

- `getServerSideProps` calls `getSession` (or `getServerSession`)
- No session → `{ redirect: { destination: '/auth/signin', permanent: false } }`
- With session, show **`Advisor Desk`** and the email **`advisor@hdfclife.com`**

`pages/auth/signin.js`:

- Email and password fields
- Submit button text: **`Sign in`**
- Google button text: **`Sign in with Google`**
- After successful credentials login, `router.push('/desk')` or NextAuth `callbackUrl=/desk`

Do **not** store the password in `NEXT_PUBLIC_` variables.

README must explain, in 3–5 lines, why an **httpOnly** session cookie is safer than putting a JWT in `localStorage`.

---

### 6. Formik + Yup — new claim

`pages/claims/new.js` heading: **`File a Claim`**

Formik + Yup (not react-hook-form, not raw `useState` as the only validation).

| Field | Name | Yup rules |
| ----- | ---- | --------- |
| Policy number | `policyNo` | required, matches `^HDFC-LIFE-[0-9]{4}$` |
| Claim amount | `claimAmount` | required, number, `min(1)`, `max(500000)` |
| Urgency | `urgency` | required, `oneOf(['HIGH','MEDIUM','LOW'])` |
| Hospital | `hospitalName` | optional string |
| Advisor email | `email` | required, email |
| Notes | `remarks` | optional, `max(200)` |

Show **field-level** errors with Formik (`touched` + `errors` or `<ErrorMessage>`).

On valid submit:

- Prevent a real network claim API (you may `console.log` the values)
- Show a success line **exactly**: `Claim submitted for HDFC-LIFE-1001` when `policyNo` is `HDFC-LIFE-1001`

Invalid `policyNo` `ABC` must show a visible error (Yup `matches`).  
Empty submit must show errors on `policyNo`, `claimAmount`, `urgency`, and `email`.

---

### 7. ISR, middleware, and env

**ISR**

- `/policies` already uses `revalidate: 60`
- `pages/api/revalidate.js`:
  - `GET` or `POST` with query `secret` and `path`
  - If `secret` !== `process.env.REVALIDATE_SECRET` → `401` JSON `{ "ok": false }`
  - If secret matches, call `res.revalidate(path)` and return `{ "ok": true, "path": "/policies" }` when `path=/policies`
  - Wrap `revalidate` in try/catch; failure → `500` `{ "ok": false }`

**Middleware**

`middleware.js` at the project root (or `src/middleware.js` if you use `src/`):

- `matcher`: `/desk/:path*`
- If the request has no NextAuth session cookie (`next-auth.session-token` or `__Secure-next-auth.session-token`), `NextResponse.redirect` to `/auth/signin`
- Do not block `/auth/signin` or `/api/auth`

This is **in addition to** the `getServerSideProps` check on `/desk`.

**Env**

Commit `.env.local.example` (not `.env.local`):

```text
NEXTAUTH_URL=http://localhost:3000
NEXTAUTH_SECRET=replace-with-a-long-random-string
GOOGLE_CLIENT_ID=
GOOGLE_CLIENT_SECRET=
REVALIDATE_SECRET=hdfc-revalidate
NEXT_PUBLIC_COMPANY_NAME=HDFC Life
```

Rules:

- Secrets stay **off** `NEXT_PUBLIC_`
- `NEXT_PUBLIC_COMPANY_NAME` is the only public env var you must display (home page)
- `.gitignore` must include `.env.local`

---

### 8. README

`README.md` must include:

1. `npm install` / `npm run dev`  
2. Credentials for the advisor account  
3. Route table (URL → file → SSG / SSR / ISR / CSR)  
4. One short paragraph (4–6 lines) answering:

> A policy catalogue changes once a day. A claims desk changes every minute. Which of SSG, SSR, and ISR would you use for each, and why?

---

### Suggested layout

```text
hdfc-life-advisor-portal/
  data/policies.json
  data/claims.json
  pages/
    _app.js
    _document.js
    index.js
    policies/index.js
    policies/[id].js
    policies/category/[...slug].js
    docs/[[...slug]].js
    claims/index.js
    claims/new.js
    desk/index.js
    auth/signin.js
    api/auth/[...nextauth].js
    api/revalidate.js
  middleware.js
  .env.local.example
  .gitignore
  package.json
  README.md
```

You may add `components/` for the header and the claim form. Do not put `getStaticProps` inside a component file. Same files may use `.ts` / `.tsx` if you choose TypeScript.

---

### Pages the grader will open (locked text)

1. `/` → header `HDFC Life Advisor Portal` and company name `HDFC Life`  
2. `/policies` → `Policy Catalogue` and `6 policies` and link text / href for `HDFC-LIFE-1004`  
3. `/policies/HDFC-LIFE-1004` → `Vikram Singh`, `TERM`, `15200`, `Active`, and `Policy id: HDFC-LIFE-1004`  
4. `/policies/HDFC-LIFE-9999` → Next.js **404**  
5. `/policies/category/term/active` → `HDFC-LIFE-1001` and `HDFC-LIFE-1004` only  
6. `/policies/category/ulip` → `HDFC-LIFE-1002` and `HDFC-LIFE-1005` only  
7. `/docs` → `Advisor Docs`  
8. `/docs/claims/file` → `Advisor Docs` and `claims/file`  
9. `/claims` → `Claims Desk`, `4 claims`, `CLM-01`, `CLM-04`  
10. `/desk` while signed out → redirect to `/auth/signin` (middleware and/or `getServerSideProps`)  
11. Sign in with `advisor@hdfclife.com` / `Advisor@123` → `/desk` shows `Advisor Desk` and `advisor@hdfclife.com`  
12. `/claims/new` → heading `File a Claim`; invalid submit shows field errors; valid `HDFC-LIFE-1001` submit shows `Claim submitted for HDFC-LIFE-1001`  
13. `/api/revalidate?secret=wrong&path=/policies` → `401`  
14. `/api/revalidate?secret=hdfc-revalidate&path=/policies` → `200` and `"ok": true` (only if `REVALIDATE_SECRET` matches the example)

---

### Submission Guidelines

Submit the **GitHub repository link**.

- Push the full Next.js project (`pages`, `data`, `middleware.js`, `README.md`, `.gitignore`, `.env.local.example`)
- Repo must be **public**
- Do **not** commit `.env.local`, `node_modules/`, or `.next/`
- Submit the GitHub repo URL as your answer

### Additional Solving

- <a href="https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts" target="_blank" rel="noopener noreferrer">Next.js Pages and Layouts</a>
- <a href="https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props" target="_blank" rel="noopener noreferrer">getStaticProps</a>
- <a href="https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props" target="_blank" rel="noopener noreferrer">getServerSideProps</a>
- <a href="https://nextjs.org/docs/pages/building-your-application/data-fetching/incremental-static-regeneration" target="_blank" rel="noopener noreferrer">Incremental Static Regeneration</a>
- <a href="https://next-auth.js.org/configuration/providers/credentials" target="_blank" rel="noopener noreferrer">NextAuth Credentials Provider</a>
- <a href="https://formik.org/docs/guides/validation" target="_blank" rel="noopener noreferrer">Formik Validation</a>
- <a href="https://github.com/jquense/yup#api" target="_blank" rel="noopener noreferrer">Yup API</a>
