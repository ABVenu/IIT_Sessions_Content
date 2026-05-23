# Assignment Question QC Report — IITR-CYB-2510 (23 May 26)

**Source notes:** `Lecture Notes Released.md`  
**Artifacts reviewed:** `Assignments.md` (draft), then `assignment-objective.md`, `assignment-subjective.md`  
**Guidelines:** `Command Center/prompts/OS_Assignment_Questions_GenerationPrompt.md`

---

## Per-question QC table

| # | Type | Remarks |
|---|------|---------|
| Q1 | MCQ — Easy | Correct: **D**; relevancy: **Yes** (symmetric = one shared secret key). |
| Q2 | MCQ — Easy | Correct: **C**; relevancy: **Yes** (hash collision = different inputs, same output). |
| Q3 | MCQ — Easy | Correct: **B**; relevancy: **Yes** (Argon2id memory-hard + auto-salt). |
| Q4 | MCQ — Easy | Correct: **B**; relevancy: **Yes** (`return str(e)` leaks internals to caller). |
| Q5 | MCQ — Moderate | Correct: **C**; relevancy: **Yes** (FIPS → PBKDF2 ~600K iterations). |
| Q6 | MCQ — Moderate | Correct: **C**; relevancy: **Yes** (CrackStation = pre-computed lookup on unsalted SHA-256). |
| Q7 | MSQ — Moderate | Correct: **B, D**; relevancy: **Yes** (Argon2id + bcrypt auto-salt; A/C require manual salt). |
| Q8 | MSQ — Moderate | Correct: **B, D**; relevancy: **Yes** (`secrets` tokens + generic login failure; A/C insecure). |
| Q9 | MSQ — Hard | Correct: **A, B, D, E**; relevancy: **Yes** (bcrypt, salting, vault/.env, generic errors; C is crypto category error). |
| Q10 | MSQ — Hard | Correct: **A, B, C**; relevancy: **Yes** (Bandit Python SAST, Semgrep multi-language overlap, weak-hash flags; D false on zero findings). |
| Subjective | Python — bcrypt + secrets refactor | Medium difficulty: **Yes**; submission (Case C): **Yes** (after fix); dataset required: **No**; sample I/O inlined: **Yes**. |

---

## Overall QC ratings (both assignments)

| Criterion | Rating (1–5) | Notes |
|-----------|--------------|-------|
| Content Coverage | 5 | Symmetric/asymmetric, hashing attacks, salting, algorithm choice (Argon2id/bcrypt/scrypt/PBKDF2/FIPS), CrackStation, secure errors, secrets, Bandit/Semgrep; subjective implements bcrypt password flow + `secrets` reset token. |
| Creativity | 5 | Scenario-based stems (onboarding, audit, FIPS contract, pen-test dump, CI/CD SAST); subjective auth-service refactor mirrors lab patterns without “as taught in session” phrasing. |
| Structural Adherence | 5 | 10 objective: 4 Easy MCQ + 2 Moderate MCQ + 2 Moderate MSQ + 2 Hard MSQ, progressive order; 1 subjective practical task; split files; Case C submission; full answer explanations. |
| No Logical Mistakes | True | All keys verified against lecture notes; Q9 C is intentional false option; subjective `secrets` now used in `generate_reset_token`. |
| No Presentation Mistakes | True | Grammar checked; no session-reference phrasing in stems; lab-specific wording softened in Q10 stem. |

---

## Initial QC findings (`Assignments.md` draft)

| Issue | Severity | Resolution |
|-------|----------|------------|
| Combined draft in `Assignments.md` instead of `assignment-objective.md` / `assignment-subjective.md` | Structural | Split into two files per guidelines. |
| Subjective submission used generic “paste in text box” only, not Case C bullets | Structural | Added explicit Case C instructions in `assignment-subjective.md`. |
| Subjective required `secrets` import but no function used it | Logical | Added `generate_reset_token()` with `secrets.token_urlsafe(32)`. |
| Q10 options tied to “the lab run” in stem | Presentation | Rephrased to generic “vulnerable Python file / sample code” wording. |
| Q8 explanation referenced “the lab’s `generate_reset_token`” | Presentation | Generalized explanation text in objective file. |

---

## Improvisation log

- **Round 1:** QC on `Assignments.md` — structure, keys, and scope checked; issues logged above.  
- **Round 2:** Created `assignment-objective.md` and `assignment-subjective.md` with fixes; subjective QC re-run — all criteria meet thresholds.  
- **Round 3:** Final objective + subjective pass — ratings confirmed at 5; logical and presentation flags **True**.

---

**QC sign-off:** Expected result satisfied — Content Coverage, Creativity, and Structural Adherence are **not less than 5**; **No Logical Mistakes** and **No Presentation Mistakes** are **True**.
