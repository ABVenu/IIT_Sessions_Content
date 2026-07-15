# In-Class Quiz QC Report — Session 32

**Batch:** `iitr-as-2603` · **Session folder:** `Module3/Session32`  
**Quiz file:** `In Class Quiz.md`  
**Aligned to:** `Lecture Notes.md` (Memory & Control Flow)  
**Review date:** 2026-07-15

---

## Scope

| Item | Target | Actual |
|---|---|---|
| Format | In-class MCQ only (surface level) | 10 single-correct MCQs |
| Coverage | All LOs from lecture “What you will learn” | 5 LOs × 2 questions each |
| Depth | Surface recall / light apply — no deep methodology | No multi-step planning, summarization deep-dive, or tool-planning asked |

### LOs covered

| LO# | Learning outcome | Quiz questions |
|---|---|---|
| 1 | Define an AI agent (perceive, reason, act, memory) | Q1, Q2 |
| 2 | Distinguish short-term vs long-term memory | Q3, Q4 |
| 3 | Persist and reload conversation history | Q5, Q6 |
| 4 | Implement loop termination | Q7, Q8 |
| 5 | Handle predictable errors with user-visible messages | Q9, Q10 |

---

## Iteration 1 — Question-level QC

| Q# | Type | Remarks |
|---|---|---|
| 1 | MCQ | Correct **B** — relevant **yes** (agent = perceive → reason → act + remember) |
| 2 | MCQ | Correct **A** — relevant **yes** (memory + controlled loop as beginner agent step) |
| 3 | MCQ | Correct **C** — relevant **yes** (open chat = short-term) |
| 4 | MCQ | Correct **D** — relevant **yes** (duration/scope contrast; demo needs short-term only) |
| 5 | MCQ | Correct **B** — relevant **yes** (persist = write durable storage / JSON) |
| 6 | MCQ | Correct **A** — relevant **yes** (`FileNotFoundError` → `[]`) |
| 7 | MCQ | Correct **C** — relevant **yes** (runaway loop + API cost risk) |
| 8 | MCQ | Correct **D** — relevant **yes** (`MAX_STEPS` hard ceiling) |
| 9 | MCQ | Correct **B** — relevant **yes** (friendly message vs traceback) |
| 10 | MCQ | Correct **A** — relevant **yes** (blank input → “Please type a question.”) |

---

## Iteration 1 — Criteria ratings

| Criterion | Rating / Result | Notes |
|---|---|---|
| Content Coverage | **5 / 5** | All five lecture LOs covered equally (2 each); all options grounded in notes; no out-of-syllabus topics (e.g. no deep summarization algorithms, multi-tool planners) |
| Creativity | **5 / 5** | ShopEasy / support-chat scenarios used lightly; distractors are plausible beginner mistakes |
| Structural Adherence | **5 / 5** | 2 MCQs per LO; single correct; self-contained wording; full answer explanations (correct + why others wrong); no “as taught in session” phrasing |
| No Logical Mistakes | **True** | Answers match definitions and lab behaviours in `Lecture Notes.md` |
| No Presentation Mistakes | **True** | Clear numbering; LO groupings; answer key consistent with body; varied correct letters |

**Quiz QC:** Passed.

---

## Checks from generation prompt (adapted for in-class quiz)

| Check | Result |
|---|---|
| Strictly within session scope | Pass |
| Surface-level only (no deep methodology) | Pass |
| Correct option relevant to stem | Pass (all 10) |
| Distractors clearly wrong vs notes | Pass |
| Explanations complete for Assess-style use | Pass |
| Grammar / spelling | Pass |

---

## Final verdict

All criteria at **5 / 5**; **No Logical Mistakes** and **No Presentation Mistakes** are **True**. No further modification cycle required.
