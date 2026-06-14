# Lecture Notes QC Report — Prompt Versioning & API Rate Limits

**File reviewed:** `Lecture Notes.md`  
**Review date:** 2026-06-14  
**Iteration:** 1

---

## QC Criteria

| Criterion | Rating / Result | Notes |
|---|---|---|
| **Content Coverage** | **5 / 5** | All metadata topics: prompt versioning; config files; rate limits; retries and backoff. All four subtopics: versioned files + registry; qualitative v1 vs v2 eval; HTTP 429 + exponential backoff; retry logging. |
| **Creativity** | **5 / 5** | Recipe versions; Zomato menu; IRCTC filename; school timetable; chai taste test; RTO tokens; UPI busy server; shop ledger analogies. |
| **Structural Adherence** | **5 / 5** | `#` title only; Introduction + What you will learn; Official/Simple/Real-life on new terms; 6 full code blocks with line comments and "How the code works"; 3 student-facing activities; Key Takeaways; terminology table. |
| **No Logical Mistakes** | **True** | Registry bundles prompt+config+tools; eval uses shared context; backoff catches RateLimitError only; jitter + max_retries capped; mock demo mirrors real backoff math. |
| **No Presentation Mistakes** | **True** | No duration/audience metadata; no "Ask students to"; paragraphs ≤3 sentences; activities use imperative student voice. |
| **No Previous Session Number References** | **True** | Grep: no `Session N` / `session N`. Uses "previous session" without number only in Introduction. |
| **No Metadata/internal reference** | **True** | No objective/duration/target-audience leakage; no internal instruction phrasing in student text. |

---

## Expected Result

- Content Coverage, Creativity, Structural Adherence: all **≥ 5** — **Met**
- No Logical Mistakes, No Presentation Mistakes, No Previous Session Number References, No Metadata/internal reference: **True** — **Met**

**Outcome:** QC passed on iteration 1.

---

## Coverage Checklist (metadata subtopics)

| Subtopic | Section in notes |
|---|---|
| Store prompts and tool configs in versioned files or simple registry | Storing Prompts in Versioned Files; The Simple Registry Pattern |
| Compare two prompt versions against the same eval questions (qualitative) | Comparing Two Prompt Versions; Activity 1 |
| Explain HTTP rate limits and implement exponential backoff | HTTP Rate Limits; Exponential Backoff and Retries; Mock Backoff Demo |
| Log retry events so failures are visible during development | Logging Retry Events; Activity 3 |

**Line count:** ~732 lines.

---

## Iteration 2

**Trigger:** Second mandatory QC pass; add eval-loop rate-limit hygiene and standalone mock backoff demo for Activity 2.

| Criterion | Rating / Result | Notes |
|---|---|---|
| **Content Coverage** | **5 / 5** | Added `time.sleep(1)` in eval comparison loop; full **mock_backoff_demo.py** with FakeRateLimitError for quota-free practice. |
| **Creativity** | **5 / 5** | Mock demo framed as "practice without burning quota" — fits classroom shared-key reality. |
| **Structural Adherence** | **5 / 5** | Mock block includes full code + "How the code works"; Activity 2 steps updated to reference mock script. |
| **No Logical Mistakes** | **True** | compare_versions import adds `time`; mock attempt counter yields 3 calls (2 fail + 1 success); removed misleading hardcoded log_retry_success from pipeline demo. |
| **No Presentation Mistakes** | **True** | Re-grep: no session numbers, duration, or instructor-only phrasing. |
| **No Previous Session Number References** | **True** | Verified clean. |
| **No Metadata/internal reference** | **True** | Verified clean. |

**Outcome:** QC passed on iteration 2.

**Line count:** ~795 lines.

**Changes in iteration 2:**
- Added **`time.sleep(1)`** after each eval question pair in `compare_versions`
- Added **Mock Backoff Demo** section with complete runnable script
- Simplified **dev_pipeline_demo** "How the code works" bullets; removed unused import

---

## Activity checklist (3 total)

| Activity | Session segment | Subtopics covered |
|---|---|---|
| **Activity 1 — Run a Two-Version Eval** | ~35 min | Versioned files; registry; qualitative eval checklist |
| **Activity 2 — Observe Backoff Without Burning Quota** | ~35 min | HTTP rate limits; exponential backoff; retry logs (mock) |
| **Activity 3 — Build a Retry Audit Trail** | ~35 min | Logging retry events; reading `api_retries.log`; mini-report |
