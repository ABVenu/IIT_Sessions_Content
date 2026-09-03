# Assignment Question QC Report

**File:** `Q.md`  
**Track:** HDFC Life 2026 — MERN Fullstack  
**Week:** 31 August – 4 September 2026  
**Format:** Single subjective GitHub project (same pattern as Java Assignment03 / Assignment04)

---

## Iteration 1 — design notes (baked into `Q.md`)

| Issue | Severity | Fix |
|---|---|---|
| create-next-app now defaults to App Router | Ambiguity | Pages Router required; `app/` banned |
| TypeScript is a later live-calendar topic (10 Sep) | Presentation | JS or TS both allowed; routes listed as `.js` with `.ts`/`.tsx` accepted |
| Google OAuth needs a Cloud Console project students may not have | Logic risk | Credentials provider is the locked path; Google button still required; credentials work if Google env is empty |
| JWT in `localStorage` is the anti-pattern of the auth session | Ambiguity | JWT **session** via NextAuth cookies; README must contrast httpOnly vs `localStorage` |
| `pages/api` CRUD / `next/image` are 7 Sep on the live calendar | Scope leak | Only `api/auth` and `api/revalidate` (ISR lesson includes on-demand revalidate) |
| Catch-all vs optional catch-all are easy to swap | Ambiguity | `[...slug]` for category filters; `[[...slug]]` for `/docs` and `/docs/claims/file` |
| Formik already appeared on 24 Aug; 3 Sep repeats it | Coverage | Claim form is Formik + Yup only; react-hook-form banned for this brief |
| `useRouter` could be skipped if they only use `getStaticProps` params | Scope leak | Locked visible line `Policy id: HDFC-LIFE-1004` |
| Seed inlined in components would skip `fs` in `getStaticProps` | Ambiguity | Must read `data/policies.json` from disk |

Locked filters independently counted from the six-row seed: TERM+Active → `1001`, `1004`. ULIP (any status) → `1002`, `1005`. Claims file has four rows, first `CLM-01`, last `CLM-04`.

---

## Section-level QC

| Section | Type | Remarks |
|---|---|---|
| Seed | Data | Same policy numbers as Java Assignment01/04; four claims reused from earlier Java amounts |
| 1. Routing + layout | Practical | `Link`, `_app` header lock, `_document` `lang="en"` |
| 2. SSG + ISR | Practical | `getStaticProps` + `getStaticPaths` + `fallback: false` + `revalidate: 60` |
| 3. Catch-all | Practical | Required vs optional catch-all; two locked filter URLs |
| 4. SSR | Practical | `getServerSideProps` only on `/claims` |
| 5. NextAuth | Practical | Credentials lock + Google wired; desk redirect; JWT session |
| 6. Formik + Yup | Practical | Schema table; success line locked; empty-submit field errors |
| 7. ISR / middleware / env | Practical | `res.revalidate`, matcher `/desk/:path*`, `.env.local.example` |
| 8. README | Written | Route table with SSG/SSR/ISR + catalogue-vs-desk paragraph |
| Additional Solving | Optional | Official Next / NextAuth / Formik / Yup docs; `target="_blank"` |

---

## Curriculum coverage (live calendar, not detailed-curriculum row dates)

| Calendar session | Covered in `Q.md`? |
|---|---|
| 31 Aug — Next.js Fundamentals – Routing & Pages I / II | `pages/`, index, nested, `[id]`, catch-all, optional catch-all, `<Link>`, `useRouter`, `_app`, `_document` |
| 1 Sep — Next.js Pre-rendering – SSG & SSR I / II | `getStaticProps`, `getStaticPaths`, `fallback: false`, `notFound`, `getServerSideProps` |
| 2 Sep — Authentication in React & Next.js I / II | NextAuth Google + credentials, session, protect in `getServerSideProps`, httpOnly vs `localStorage` |
| 3 Sep — Forms & Validation with Formik & Yup I / II | `Formik`, Yup `required` / `email` / `min` / `max` / `matches` / `oneOf`, field errors |
| 4 Sep — Next.js Advanced – ISR, Middleware & Env I / II | `revalidate`, `res.revalidate()`, `middleware.js` matcher, `.env.local` vs `NEXT_PUBLIC_` |

Not required (later calendar): Next.js API CRUD, `next/image`, Git/GitHub week, Jest, React Native. TypeScript is optional, not required.

---

## Assignment-level QC

| Criteria | Rating / Status |
|---|---|
| Content Coverage | 5 |
| Creativity | 5 |
| Structural Adherence | 5 (seed, numbered sections, locked UI/HTTP, layout, GitHub submit, Additional Solving) |
| No Logical Mistakes | True |
| No Presentation Mistakes | True |
| No Previous Session Number References | True |
| No Metadata / internal author notes in the student brief | True |

---

## Final QC Decision

**Passed** after Iteration 1 design locks.

- Content Coverage, Creativity, Structural Adherence are all 5.
- Locked category filters and claim counts recomputed and match `Q.md`.
- Pages Router / JS / no API-CRUD choices match the live calendar for this week.
