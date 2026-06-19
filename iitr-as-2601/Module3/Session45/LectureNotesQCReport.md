# Lecture Notes QC Report — Prompt Versioning & API Rate Limits

**File reviewed:** `Lecture Notes Released.md`  
**Review date:** 2026-06-19  
**Iteration:** 1 (post live-session alignment)

---

## QC Criteria

| Criterion | Rating / Result | Notes |
|---|---|---|
| **Content Coverage** | **5 / 5** | All metadata subtopics covered and aligned to transcript: versioned files + registry; qualitative eval on same inputs; HTTP rate limits + exponential backoff; retry logging. Session extras added: prompt injection eval, Git versioning analogy, Tenacity library, Groq dashboard, jitter/synchronized retries. |
| **Creativity** | **5 / 5** | Zomato menu card; IRCTC PNR filenames; Big Bazaar store directory; RTO token counter; IRCTC Tatkal refresh; hospital form-filling injection analogy; shop ledger retry logs. |
| **Structural Adherence** | **5 / 5** | `#` title only; context + What you will learn; Official/Simple/Real-life on new terms; full code with line comments and "How the code works"; student-facing activities (3); Key Takeaways; terminology table; all 8 session images retained. |
| **No Logical Mistakes** | **True** | Tenacity `@retry` matches live demo; eval fairness rule preserved; registry bundles prompt + config; backoff capped at 4 attempts; logging via `before_sleep_log` matches session. |
| **No Presentation Mistakes** | **True** | No duration/audience metadata; no "Ask students to"; activities student-facing; paragraphs ≤3 sentences. |
| **No Previous Session Number References** | **True** | Grep: no `Session N` / `session N` in released notes. Uses **previous** only in introduction. |
| **No Metadata/internal reference** | **True** | No internal instruction leakage. |

---

## Expected Result

- Content Coverage, Creativity, Structural Adherence: all **≥ 5** — **Met**
- No Logical Mistakes, No Presentation Mistakes, No Previous Session Number References, No Metadata/internal reference: **True** — **Met**

**Outcome:** QC passed on iteration 1.

---

## Live-Session Alignment Changes (vs `Lecture Notes.md`)

| Change | Reason |
|---|---|
| Replaced manual `groq_with_backoff.py` / `mock_backoff_demo.py` with **Tenacity** demos | Session taught Tenacity `@retry`, not hand-written backoff loops |
| Removed `retry_logger.py` and `tail_retries.py` | Not covered; logging taught via `before_sleep_log` |
| Removed `dev_pipeline_demo.py` end-to-end script | Not walked through in session |
| Added **prompt injection** eval subsection + `compare_injection.py` | Extra content taught in live demo |
| Added **Git** code-versioning analogy | Taught in session |
| Removed **Retry-After** header and **503** retry references | Not covered in transcript |
| Added **Groq dashboard** rate-limit note | Taught in session |
| Updated activities and terminology table | Match Tenacity and injection content |

---

## Coverage Checklist (metadata subtopics)

| Subtopic | Section in released notes |
|---|---|
| Store prompts and tool configs in versioned files or registry | Storing Prompts in Versioned Files; Registry Pattern |
| Compare two prompt versions on same eval questions (qualitative) | Comparing Two Prompt Versions; Prompt Injection; checklist + Activity 1 |
| Explain HTTP rate limits and exponential backoff | HTTP Rate Limits; Exponential Backoff and Retries with Tenacity |
| Log retry events during development | Logging Retry Events; `before_sleep_log` in Tenacity demos |
