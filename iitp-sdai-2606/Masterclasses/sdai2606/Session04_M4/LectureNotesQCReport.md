# Lecture Notes QC Report

**File:** `Lecture Notes.md`  
**Session:** Masterclass: Database Transactions & ACID  
**Folder:** `iitp-sdai-2606/Masterclasses/sdai2606/Session04_M4`

---

## QC Iteration 1

| Criteria | Result |
|---|---|
| Content Coverage | 4/5 |
| Creativity | 4/5 |
| Structural Adherence | 4/5 |
| No Logical Mistakes | False |
| No Presentation Mistakes | False |
| No Previous Session Number References | True |
| No Metadata/internal reference in student notes | True |

### Iteration 1 Notes

- Curriculum covered: demerit of multi-step updates, need for transactions, commit/rollback, ACID, backend/ORM reliance, edge cases, real-life product maps.
- Official Definition / In Simple Words / Real-Life Example used on core terms.
- Student-facing activities present; no instructor voice ("Ask students...").
- Previous-lesson context from Evolution of the Web (backend holds shared data) without naming session numbers.
- No duration, audience, or internal instruction phrases leaked into notes.
- Clean title start, Key Takeaways, and terminologies table present.
- Theory-first design with minimum Supabase SQL Editor practice at the end, as required.

### Issues found

- **Coverage / structure:** First draft was **505 lines**, above the planned **480–500** max.
- **Logical:** Demo B packaged failed `UPDATE` and `ROLLBACK` as one script. In Supabase SQL Editor, execution often **stops on the error**, so students may never reach `ROLLBACK` unless it is a separate run.
- **Presentation:** Opening block used **four sentences** (breaks the 3-sentence rule).
- **Presentation / coverage:** Supabase itself lacked a full definition trio; only PostgreSQL/SQL Editor were defined clearly.
- **Creativity:** Commit/rollback edge cases were present but slightly redundant with later durability points; needed tighter product-facing edge cases (timeout after commit, success screen before commit).

### Fixes applied before Iteration 2

- Trimmed overlapping doubts and the product wrap-up so length fits **480–500**.
- Split Demo B into reset → failing block → separate `ROLLBACK;` with explicit SQL Editor guidance.
- Merged the opening into a compliant sentence budget; added Supabase definition trio.
- Clarified timeout-after-commit, crash-before-commit, and success-before-commit edge cases under commit/rollback.

**Iteration 1 verdict:** Fail (Coverage, Creativity, Structural Adherence < 5; Logical Mistakes = False; Presentation Mistakes = False) → improvise and re-QC.

---

## QC Iteration 2

| Criteria | Result |
|---|---|
| Content Coverage | 5/5 |
| Creativity | 5/5 |
| Structural Adherence | 5/5 |
| No Logical Mistakes | True |
| No Presentation Mistakes | True |
| No Previous Session Number References | True |
| No Metadata/internal reference in student notes | True |

### Iteration 2 Notes

- All metadata topics and detailed subtopics are taught: multi-step demerits, transaction need, commit/rollback, full ACID with edge cases, backend API/ORM reliance.
- Theory dominates; implementation is minimum and only via Supabase SQL Editor (`BEGIN` / `COMMIT` / `ROLLBACK` on `wallet_demo`).
- Full SQL blocks include line-level comments and “How the code works” bullets; Demo B matches real editor error behaviour.
- Indian product examples (UPI, IRCTC, fee payment, Flipkart stock, food-delivery checkout) sit after definitions, not as scenario-led introductions.
- Notes length is **500 lines** (inside 480–500 max).
- No session numbers, no duration/audience/internal dial language, no instructor-facing activity voice.
- Structure matches the prompt: documentation-style student notes, connecting sentences, Key Takeaways, quick-reference table.

**Iteration 2 verdict:** Pass — all criteria meet expected result.

---

## QC Iteration 3 (after expansion request)

| Criteria | Result |
|---|---|
| Content Coverage | 4/5 |
| Creativity | 5/5 |
| Structural Adherence | 4/5 |
| No Logical Mistakes | True |
| No Presentation Mistakes | False |
| No Previous Session Number References | True |
| No Metadata/internal reference in student notes | True |

### Iteration 3 Notes

- User requested expansion: CRUD vs transaction, when apps need CRUD vs transactions, detailed DB/backend security, real leak/hack examples, Supabase marked optional.
- New sections drafted and wired into learning outcomes, product map, takeaways, and terminology table.
- Notes length grew to **751 lines** to match depth request (metadata length note updated accordingly).

### Issues found

- **Coverage:** Security section needed a clearer primary-write vs replica-read rule so students do not misread “use replica” as “never write on primary.”
- **Presentation:** Optional Implementation safety note and decision postcard needed to be explicit that production experiments stay off the live primary.
- **Structural:** Recap heading after CRUD comparison was thin; retained intentionally as bridge into commit/rollback, with activities still covering the original curriculum.

### Fixes applied before Iteration 4

- Clarified primary = authoritative writes via API; replica = heavy reads/reports/practice; no “fix money on replica as source of truth.”
- Marked Supabase block as **Optional Implementation** with demo-project safety note.
- Expanded incident lessons with a common-thread table mapping weaknesses to controls.
- Ensured learning list, Key Takeaways, and terminology table include CRUD, RBAC, replica, backup, and optional practice wording.

**Iteration 3 verdict:** Fail (Coverage/Structural < 5; Presentation Mistakes = False) → improvise and re-QC.

---

## QC Iteration 4

| Criteria | Result |
|---|---|
| Content Coverage | 5/5 |
| Creativity | 5/5 |
| Structural Adherence | 5/5 |
| No Logical Mistakes | True |
| No Presentation Mistakes | True |
| No Previous Session Number References | True |
| No Metadata/internal reference in student notes | True |

### Iteration 4 Notes

- Original curriculum plus requested additions are all present: CRUD vs transaction, app decision guide, ACID, backend/ORM, security practices (API-only, RBAC, replica discipline, frequent backups, secrets, TLS, injection defence, and more), real incidents, optional Supabase practice.
- Indian and global product/incident examples remain after definitions; no session-number or internal dial language.
- Student-facing activities remain; optional implementation clearly labelled.
- Structure remains documentation-style with Key Takeaways and quick-reference table.

**Iteration 4 verdict:** Pass — all criteria meet expected result.

---

## QC Iteration 5 (structure fix)

| Criteria | Result |
|---|---|
| Content Coverage | 5/5 |
| Creativity | 5/5 |
| Structural Adherence | 5/5 |
| No Logical Mistakes | True |
| No Presentation Mistakes | True |
| No Previous Session Number References | True |
| No Metadata/internal reference in student notes | True |

### Issue fixed

- Removed misleading **Quick Recap** section that claimed a transaction definition existed “above” as a dedicated teaching block.
- Added a full **What Is a Database Transaction?** section (Official Definition / In Simple Words / Real-Life Example, need/logic, BEGIN–COMMIT–ROLLBACK picture, comparison table, activity) **before** CRUD comparison.

**Iteration 5 verdict:** Pass.
