# Lecture Script: Masterclass: Database Transactions & ACID

**Session duration:** 2 hours  
**Audience:** Absolute beginners (Indian students; any background, not necessarily tech)

**Examples in the Lecture Notes:** The notes include tables, edge cases, security practices, incident summaries, and an optional Supabase SQL Editor practice. The **same** document is **shared with students**. This script does **not** require covering every table row or every incident live. For each topic, pick a **small, clear** set that fits the clock; point learners to the rest in the notes for homework.

**How to use this file:** Each block lists *what happens in the room* and its **duration in minutes**. This is timing and facilitation only—definitions, full explanations, and diagrams stay with your **Lecture Notes** (slides, board, or shared doc). Skim headings aloud; let visuals and short activities carry the structure. This is a **theory-first** masterclass; keep live coding optional and light.

**Break (only pause in this plan):** After **roughly 60–70 minutes** of session clock time (after **Commit and Rollback**), take **one** pause of **5–8 minutes**, then continue. Every numbered section below is **teaching or activity**—there are **no** “break” rows in the numbered list.

---

## 1. Welcome and why this lesson (6 minutes)

- Greet; confirm Lecture Notes for this masterclass are open (browser or PDF).
- One-line bridge from previous learning: backend holds **shared data, rules, and secrets**; today asks what happens when several related rows must change and something fails halfway.
- Hook aloud: UPI transfer, railway seat booking, college fee — each changes **more than one fact**.
- State outcomes in plain words: spot half-updates, know **transaction** vs **CRUD**, name **ACID**, list security habits, optional Supabase feel at the end if time.
- **Cold-call 2 students:** “If money left your wallet but never reached the merchant, is the app still honest?”
- **Check for thumbs up:** notes open; chat ready for short answers.

**Bridge:** “Products promise correctness. Let’s see what goes wrong when related updates are not protected together.”

---

## 2. Why related updates are dangerous (11 minutes)

- Screen-share the **unsafe multi-step / half-update** image from notes.
- Teach in three beats: multi-step update definition → need → logic (step 1 saves, step 2 fails → partial lie).
- Walk **two rows only** from the unsafe table live (wallet debit/credit; seat reserved without booking). Point students to the full table in notes.
- Kill the doubt in one line: an API error does **not** always mean nothing changed.
- **Activity — Spot the half-update (3 min):** pay ₹200 wallet → merchant; students write three steps and circle what is wrong if step 2 fails. Circulate / spot-check Zoom notebooks.
- **Cold-call 1 student** to read the circled risk (wallet reduced, merchant not credited).

**Bridge:** “That all-or-nothing need has a name—**database transaction**. Let’s define it clearly.”

---

## 3. What is a database transaction (10 minutes)

- Official / simple / real-life definition trio — keep under 90 seconds; bank form vs Confirm stamp analogy.
- Screen-share the **transaction lifecycle** image (BEGIN → draft → COMMIT / ROLLBACK).
- Board the four words only: **BEGIN**, writes, **COMMIT**, **ROLLBACK**.
- Flash the without vs with transaction table; do not read every cell—stress “temporary until stamped.”
- Common doubt (30 sec): not only for money — booking, stock, marks totals too.
- **Activity — Name the unit (2 min):** IRCTC berth facts that must change together; sentence “These must be one transaction because ___.”
- **Check for thumbs up:** everyone can say BEGIN opens a draft.

**Bridge:** “You already know everyday Create-Read-Update-Delete. Next we separate plain **CRUD** from a **transaction**.”

---

## 4. Simple CRUD vs a transaction (10 minutes)

- Define **CRUD** quickly with the student-register example.
- Screen-share the **CRUD vs Transaction** image; narrate left = independent facts, right = all-or-nothing unit.
- Walk three comparison rows only: typical size, success meaning, best for.
- Common doubts (1 min): single statement often atomic alone; long transactions around every SELECT are not “more safe.”
- **Activity — Label C or T (3 min):** snack menu read; profile email update; order + stock; delete OTP; wallet transfer. Reveal: C, C, T, C, T.
- **Pair-share (1 min):** partner explains one T example in one sentence.

**Bridge:** “So do all apps need only transactions, or only CRUD? Real products use **both**—for different features.”

---

## 5. When CRUD is enough and when a transaction is required (8 minutes)

- One sentence: no serious product is “CRUD only forever” or “transaction for every click.”
- Flash the app-style table; live-teach only **catalogue** vs **ecommerce/UPI** rows.
- Decision guide on board: “If step 1 succeeds and step 2 fails, is the product still honest?” No → transaction. Yes → CRUD may be enough.
- **Activity — Feature triage (3 min):** campus food app five features from notes; students mark CRUD or Transaction. Spot-check chat.
- **Cold-call:** “Place order — why is that a transaction?”

**Bridge:** “When you do use a transaction, it must end cleanly. That ending is **commit** or **rollback**.”

---

## 6. Commit and rollback (11 minutes)

- Definition trios for **commit** and **rollback**; stamp vs tear-up slip.
- Outcome table: COMMIT / ROLLBACK / long idle open transaction (locks).
- Edge cases — pick **two** live only: timeout after commit (blind retry risk); success screen before commit (lying UI). Point to crash-before-commit in notes.
- Common doubt (30 sec): rollback does **not** delete the whole table; cannot un-commit.
- **Activity — C or R (2 min):** four cases from notes. Reveal C, R, R, C.
- **Check for thumbs up:** everyone can say commit = keep, rollback = discard.
- **Break timing:** this is the natural **end of first half**—after this section, take the **5–8 minute** pause per the rule at the top.

**Bridge:** “After the break, we name the four promises that make transactions trustworthy—**ACID**.”

---

## 7. ACID overview (7 minutes)

- Expand A-C-I-D once; screen-share the **ACID four pillars** image.
- One-line promise each: all or nothing; rules hold; safe concurrency; survives crash.
- Tell students the next blocks unpack each letter with one edge case—not a memory dump of every row.
- **Cold-call 1:** “Which letter stops half-saved money?” (**Atomicity**)

**Bridge:** “Start with Atomicity and Consistency—honest units and allowed results.”

---

## 8. Atomicity and Consistency (11 minutes)

- **Atomicity:** all or nothing; UPI wallet example; one edge case (second write fails → full rollback).
- Activity light (1 min): return product + refund — both in one unit.
- **Consistency:** valid state to valid state; constraints vs app rules.
- Show one broken-consistency row (negative wallet) and the guard (CHECK / app check).
- **Activity — Name one rule (2 min):** food-delivery checkout consistency rule + rollback if fail.
- **Pair-share (1 min):** partner names which property is “rules still hold.”

**Bridge:** “Rules are not enough if two users race. That is **Isolation**—then **Durability** for what survives a crash.”

---

## 9. Isolation and Durability (10 minutes)

- **Isolation:** last seat / stock = 1 race; name dirty read and lost update in one breath each (skip deep isolation-level names).
- **Activity — Last seat race (2 min):** safe vs unsafe outcomes; circle Isolation.
- **Durability:** committed data survives restart; SMS only after commit.
- **Activity — Trust the SMS? (1 min):** yes/no — send before commit? Expected **no**.
- Common doubt (30 sec): durability ≠ backup (backups return in security).

**Bridge:** “ACID lives in the database. The **backend API** and **ORM** are who must open that boundary on each multi-step write.”

---

## 10. Why backend APIs and ORMs rely on transactions (8 minutes)

- Four-layer table skim: Frontend intent → API decides → ORM/client issues BEGIN/COMMIT → DB enforces ACID.
- Safe write pattern on board: begin → validate → writes → rollback or commit.
- Two doubts fast: ORM auto-save is not automatic safety; frontend must **not** hold DB credentials or start DB transactions.
- Edge cases — pick **two**: double-click Pay (idempotency); SMS after commit only.
- **Activity — API boundary sketch (2 min):** four boxes; star on API + Database for commit ownership.
- **Check for thumbs up:** “Pay button asks; backend decides; database stamps.”

**Bridge:** “Correct data still fails the product if anyone can open the vault. Next: **security practices** for DBs and backends.”

---

## 11. Security practices for databases and backends (12 minutes)

- Frame: reliability (ACID) + security (access and recovery) travel together.
- Screen-share **API owns database** image; teach API-only access (no direct client SQL; no DB password in the app).
- RBAC in one minute: student / teacher / exam cell — not everyone needs full CRUD; least privilege at API **and** DB user.
- Screen-share **primary / replica / backups** image; rules: writes on **primary** via API; heavy reads/reports on **replica**; never experiment on live primary; frequent **tested** backups.
- Flash the “other practices” table—live-name only **secrets out of Git**, **parameterized queries / SQL injection**, **TLS**, **private networking**. Rest = homework skim.
- **Activity — Security checklist (3 min):** “student updates phone” — five controls; students star any they missed.
- **Cold-call:** “Where should a heavy sales dashboard query run—primary or replica?”

**Bridge:** “These rules feel abstract until you see real leaks. We’ll map a few incidents to the controls—not attack recipes.”

---

## 12. Real incidents, product map, and close (8 minutes)

- Teach **three** incidents only (suggest Equifax unpatched edge; Uber/secrets in repo pattern; Air India/SITA vendor boundary). Point to Domino’s India / LinkedIn / Capital One in notes for reading.
- Common-thread table: one weakness → one safer habit (API-only, least privilege, backups).
- **Activity — Map an incident (2 min):** “This risk shrinks if we enforce ___.”
- Flash **Putting It Together** postcard: CRUD vs transaction decision; RBAC; replica; backups.
- Optional Supabase: **announce as optional homework / if ahead** — do not start a full lab unless Timing Flex says you have 8+ spare minutes.
- Key takeaways aloud (5 bullets max); end with the double question: which ACID promise protects correctness, which security control protects access and recovery?
- **Check for thumbs up:** students can name COMMIT vs ROLLBACK and one security rule.

**Bridge:** “That’s the session. Use the notes tables for revision; optional SQL Editor practice is there if you want to feel BEGIN and ROLLBACK once.”

---

## Timing Flex

**If running late (cut in this order):**

1. Skip live walkthrough of more than **two** unsafe-table rows and more than **three** incidents—send students to notes.
2. Collapse Atomicity+Consistency and Isolation+Durability into **one shorter ACID pass** (definition + one edge case each).
3. Security “other practices” table → students self-read; keep only API-only, RBAC, primary/replica/backup.
4. **Do not** start Optional Supabase in-room if behind; assign as optional practice.
5. Cut pair-shares first; keep one cold-call and one written activity per half.

**If running early (use spare minutes):**

1. Run Optional Supabase Demo A only (setup + COMMIT transfer); Demo B if still ahead.
2. Extra cold-calls on the product map table (UPI, last seat, fee + receipt).
3. Students write a 4-line “security postcard” for a campus fee portal.

**If Zoom energy drops:** switch to chat polls (C/T, C/R, primary vs replica) instead of long verbal answers; keep screen on one image for 60 seconds of silence while they write.
