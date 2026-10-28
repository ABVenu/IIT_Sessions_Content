# Capstone Project IV – Documentation & Deployment

**CampusBite** runs on **Vercel** (frontend), **Render** (FastAPI), and **Supabase** (PostgreSQL), with **JWT** auth and optional **Gemini** insights. This lesson finishes **documentation**, **deployment hardening**, **demo prep**, and **submission** so mentors and reviewers can run your project without guessing.

## What you will learn in this lesson

- **README** structure for capstone reviewers
- **Environment variables** per platform
- **Deploy** and redeploy workflow
- **API documentation** — `/docs` and contract file
- **Demo script** and submission checklist
- **Post-deploy smoke tests**

Connecting idea: Building is half the job; **shipping provably** is what interviews and grading see.

---

![Graders expect live URLs, demo accounts, setup steps, env vars, features, and known limits](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module4/session48/session48-01-readme-structure.png?v=20261028)


## README template (copy and fill)

```markdown
# CampusBite

Campus restaurant ordering with customer, kitchen, and delivery dashboards.

## Live URLs
- Frontend (Vercel): https://...
- API (Render): https://.../docs
- Database: Supabase project (private)

## Demo accounts
| Role | Email | Password |
| --- | --- | --- |
| Customer | demo@c... | ... |
| Owner | owner@c... | ... |
| Partner | rider@c... | ... |

## Local setup
### Backend
cd backend && python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # fill DATABASE_URL, JWT_SECRET, GEMINI_API_KEY
uvicorn app.main:app --reload

### Frontend
cd frontend && npx serve .  # or python -m http.server
Set API_BASE_URL to http://127.0.0.1:8000

## Environment variables
### Render
- DATABASE_URL (Supabase)
- JWT_SECRET
- GEMINI_API_KEY
- CORS_ORIGINS=https://your.vercel.app

### Vercel
- CAMPUS_BITE_API=https://your.onrender.com

## Features
- JWT RBAC (customer / restaurant_owner / delivery_partner)
- Order lifecycle + dummy payment ledger
- Return/refund owner approval
- Menu CRUD, stats, partner assign
- AI order insights (Gemini, rate limited)
- Profile images via URL at register (no upload)

## Known limitations
- No real payments, maps, websockets, or file uploads
```

---

## Supabase setup

| Step | Action |
| --- | --- |
| 1 | Create project in Supabase dashboard |
| 2 | Copy **connection string** (URI) for SQLAlchemy |
| 3 | Run migrations or `create_all` once from local against prod (careful) or use SQL editor |
| 4 | Run seed script for demo users |
| 5 | Enable SSL in connection string (`?sslmode=require`) |

**Never** commit service role key to Git; use `DATABASE_URL` on Render only.

---

![Production triangle: Vercel frontend, Render API, Supabase database—with CORS on the edge](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module4/session48/session48-02-deploy-triangle.png?v=20261028)


## Render backend deploy

| Setting | Value |
| --- | --- |
| Runtime | Python 3.11+ |
| Build | `pip install -r requirements.txt` |
| Start | `uvicorn app.main:app --host 0.0.0.0 --port $PORT` |
| Health | `GET /health` returns 200 |

**Cold starts:** Free tier may sleep—first demo request wakes service; mention in demo.

**Logs:** Middleware print lines appear in Render log stream—useful for debugging.

---

## Vercel frontend deploy

| Option | Notes |
| --- | --- |
| Root `frontend/` | Set output directory in Vercel |
| Env | `CAMPUS_BITE_API` injected at build or runtime in `index.html` |
| SPA routing | Use separate HTML files per page (capstone style) |

Redeploy frontend after changing API URL.

---

## CORS final check

```python
# Render env example
CORS_ORIGINS=https://campusbite.vercel.app,https://campusbite-*.vercel.app
```

Test from browser console on Vercel:

```javascript
fetch("https://YOUR_API/health").then((r) => r.json()).then(console.log);
```

---

## API documentation deliverables

| Artefact | Location |
| --- | --- |
| Live Swagger | `https://api.../docs` |
| Exported OpenAPI | `docs/openapi.json` optional download |
| Session 44 contract | `docs/Capstone-API-Contract.md` in repo |

Reviewers compare contract vs `/docs` for drift.

---

## Security submission checklist

| Item | Verified |
| --- | --- |
| No `.env` in Git | |
| `JWT_SECRET` strong random | |
| Passwords hashed | |
| RBAC tested per role | |
| AI key only on Render | |
| Rate limit on login + AI | |
| `profile_image_url` https validated | |

---

![After deploy, verify health, auth, a sample order, CORS from Vercel, and OpenAPI docs](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module4/session48/session48-04-smoke-tests.png?v=20261028)


## Smoke tests after deploy

| # | Test |
| --- | --- |
| 1 | `GET /health` |
| 2 | Register + login customer |
| 3 | Place order |
| 4 | Owner advances status |
| 5 | Partner delivers |
| 6 | Review + return path |
| 7 | Insights endpoint once |
| 8 | 401 after logout |

---

![Time-box the mentor demo: hook, core flows, AI highlight, honest limitations, close](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module4/session48/session48-03-demo-script-timeline.png?v=20261028)


## Demo script (3–5 minutes)

1. **Intro** — problem (campus food chaos), stack one sentence.
2. **Customer** — show avatar URL, order, mock pay confirmation.
3. **Owner** — queue, reminder banner if stale, assign partner.
4. **Partner** — deliver.
5. **Customer** — review + AI “summarise my orders”.
6. **Return** — owner approves refund; show ledger concept in `/docs` or DB screenshot.
7. **Close** — limitations honest.

Practice **role switch** via three browser profiles or logout/login.

---

## Submission package

| Include | Format |
| --- | --- |
| Git repo URL | main branch |
| Vercel + Render URLs | README |
| Short screen recording | optional backup |
| Team members | README |

---

## Troubleshooting production

| Issue | Action |
| --- | --- |
| 502 Render | Check start command and logs |
| DB connection | Verify Supabase URL and IP allowlist if used |
| CORS | Match exact Vercel URL scheme |
| AI 500 | Missing `GEMINI_API_KEY` on Render |
| Slow first hit | Render wake-up |

---

## Maintenance after course

- Rotate `JWT_SECRET` if repo was ever public with leaks.
- Supabase pause on free tier—document how to resume.
- Keep seed passwords only for demo—not production.

### Activity — reviewer drill

Swap laptops with a classmate; they run README local setup for **frontend only** while you watch—fix README gaps.

---

## `.env.example` (backend)

```text
DATABASE_URL=postgresql://user:pass@host:5432/postgres?sslmode=require
JWT_SECRET=change-me-to-long-random-string
JWT_ALGORITHM=HS256
GEMINI_API_KEY=your_key
CORS_ORIGINS=http://localhost:5500,https://your-app.vercel.app
```

Commit **example only**—never real values.

---

## Git submission hygiene

| Rule | Why |
| --- | --- |
| `.gitignore` includes `.env`, `.venv` | Secrets |
| Meaningful commit messages | Review |
| `main` deploys match tagged release | Repro |

### Activity — clone test

Clone your own repo fresh in a new folder and follow README—note every missing step.

---

## Vercel environment UI steps

1. Project → Settings → Environment Variables.
2. Add `CAMPUS_BITE_API` for Production.
3. Redeploy from Deployments tab.
4. Hard-refresh browser (cache).

---

## Render environment UI steps

1. Service → Environment → add variables.
2. Manual Deploy after env change.
3. Verify **Logs** show Uvicorn listening on `$PORT`.

---

## Supabase backup note

Export schema SQL from dashboard for portfolio—shows you understand persistence layer.

---

## Grading alignment (typical rubric)

| Area | Evidence |
| --- | --- |
| Auth | JWT + RBAC demo |
| CRUD | Menu + orders |
| Business rules | 409 transitions |
| AI | Insights screenshot |
| Deploy | Live URLs |
| Docs | README |

---

## Post-course extensions (optional mention in README)

- Email notifications (out of scope now).
- Real payment sandbox.
- Multi-restaurant marketplace.

Keeps v1 scope honest.

---

## Interview questions you can answer

1. How do you prevent partners seeing others’ orders?
2. Where is Gemini key stored?
3. What happens on dummy refund?
4. Why localStorage JWT for demo?

Prepare two-sentence answers.

---

## Final submission email template

```text
Subject: CampusBite capstone submission

Team:
Frontend: ...
API docs: .../docs
Repo: ...
Demo users: (see README)
```

---

## README section-by-section guide

**Live URLs** — Mentors click these first. Broken links cost time; test in incognito.

**Demo accounts** — Use weak passwords acceptable for sandbox only; never reuse real passwords.

**Local setup** — Split backend and frontend; Windows users need `venv\Scripts\activate` note if applicable.

**Environment variables** — Table format matches Session 44 planning; copy names exactly from code `config.py`.

**Features** — Bullet list mirroring MoSCoW Must items from flow doc—proves scope met.

**Known limitations** — Shows maturity; list no uploads, no real pay, no maps, in-memory rate limit.

**Architecture** — One paragraph: Vercel static JS → Render FastAPI → Supabase; Gemini on Render.

**AI feature** — Explain insights uses SQL context, not embeddings.

**Auth** — JWT in localStorage; RBAC enforced server-side.

---

## Documenting middleware and rate limits for graders

Add subsection under **Security**:

- Request log middleware prints path and duration.
- Login limited per IP; insights limited per user id.
- Link to code file `middleware.py` and `rate_limit.py`.

---

## OpenAPI / docs screenshot

Include one PNG of `/docs` showing auth + orders + ai tags—helps offline reviewers.

---

## Video demo tips

- Zoom browser to 125% for readability.
- Narrate role switches aloud.
- Keep under five minutes unless mentor specifies otherwise.
- Show one failure recovery (409 message) to prove rules work.

---

## Supabase row verification (optional appendix)

Screenshot of `orders` and `payment_ledger` after refund—proves persistence for skeptical reviewers.

---

## Team responsibilities table (README)

| Member | Owned area |
| --- | --- |
| A | Frontend customer + Vercel |
| B | Backend orders + Render |
| C | Auth + restaurant routes |
| D | AI insights + docs |

Adjust for team size—solo lists all.

---

## Version tag suggestion

`git tag v1.0-capstone-demo` before submission—frozen demo state.

---

## After submission maintenance

- Pin dependency versions in `requirements.txt` for reproducibility.
- Note Python version used on Render.

---

## Capstone reflection prompts (portfolio blog)

- What was hardest: CORS, transitions, or AI context?
- What would you add with two more weeks?
- How does RBAC differ from hiding buttons?

Two paragraphs each—good LinkedIn material.

---

## Hands-on checklist

1. Complete README all sections.
2. Deploy Render + Vercel; paste live links.
3. Run eight smoke tests; tick checklist.
4. Record 3-minute demo or rehearse live.
5. Export or link OpenAPI.
6. Submit repo + URLs per mentor instructions.
7. Tag release `v1.0-capstone-demo` after smoke tests pass.
8. Archive `.env.example` with every key name your code reads.
9. Ask a classmate to run smoke test #3 using only your README—fix gaps same day.

---

## Key Takeaways

- Align submission README with **Capstone Flow Session.md** so graders see the same scope you built.
- **Documentation** is part of the product—URLs, env vars, and demo users matter.
- **Vercel + Render + Supabase** is the cohort reference architecture.
- **Smoke tests** catch CORS and auth issues before grading.
- Honest **limitations** build trust in demos.
- You have shipped a **full-stack, AI-augmented** capstone—extend it in your portfolio.

## Important Commands, Terminologies used

| Name | Meaning |
| --- | --- |
| **Smoke test** | Quick production sanity checks |
| **CORS_ORIGINS** | Allowed frontend origins |
| **Cold start** | Render sleep wake delay |
| **DATABASE_URL** | Supabase Postgres URI |
| **JWT_SECRET** | Signing key for tokens |
| **OpenAPI** | Machine-readable API spec |
| **README** | Reviewer entry point |
| **CampusBite** | Capstone project name |
| **Vercel** | Frontend host |
| **Render** | Backend host |
| **Supabase** | Managed PostgreSQL |
| **`.env.example`** | Safe template for secrets |
| **Clone test** | Fresh machine README verify |
| **Cold start** | Render wake delay |
| **Smoke test** | Eight-step prod checklist |
| **Demo script** | Timed role walkthrough |
| **Screen recording** | Backup if live net fails |
| **OpenAPI export** | API artefact for graders |
| **Service role key** | Supabase secret—not in Git |
| **sslmode=require** | Postgres SSL param |
| **Manual deploy** | Render after env change |
| **Hard refresh** | Cache bust after Vercel deploy |
| **Grading rubric** | Auth CRUD AI deploy docs |
| **Post-course extension** | README future work section |
| **Interview prep** | Two-sentence answers |
| **Submission email** | Mentor handoff template |
| **JWT_SECRET rotation** | If leak suspected |
| **Free tier pause** | Supabase resume note |
| **Health endpoint** | Deploy verification |
| **CORS_ORIGINS** | Comma-separated origins |
| **Capstone Flow Session.md** | Feature scope reference |
| **Capstone-API-Contract.md** | Session 44 output file |
| **Live /docs** | Swagger on Render |
| **Team charter** | Names in README |
| **Portfolio** | Resume + repo link |
| **nginx** | Not used—static Vercel |
| **Docker** | Optional—not required |
| **uvicorn** | ASGI server on Render |
| **npx serve** | Local static frontend |
| **pgAdmin** | Optional Supabase UI |
| **Demo users table** | README credentials |
| **Limitations list** | Honest scope boundary |
| **v1.0-capstone-demo** | Suggested git tag |
| **Peer README test** | Classmate clone validation |
| **Reflection prompts** | Portfolio blog starters |
| **Screenshot appendix** | Optional Supabase proof |
| **Team table** | README responsibility split |
| **Middleware docs** | Grader-facing security note |
