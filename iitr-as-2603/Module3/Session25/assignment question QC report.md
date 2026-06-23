# Assignment Question QC Report

## Question-wise QC

| Question Number | Type | Remarks |
| --- | --- | --- |
| Q1 | Objective (MCQ, Easy) | Correct option verified: C. Relevancy: Yes. Input + output token billing via QuickKart API bill scenario. |
| Q2 | Objective (MCQ, Easy) | Correct option verified: B. Relevancy: Yes. Subword tokenisation ("unbelievable" → 3 tokens) and design impact on cost/context. |
| Q3 | Objective (MCQ, Easy) | Correct option verified: C. Relevancy: Yes. Context window = input + output in one request (hostel helpdesk stack). |
| Q4 | Objective (MCQ, Easy) | Correct option verified: B. Relevancy: Yes. Critical rules pinned in system prompt (CampusPay scope rule). |
| Q5 | Objective (MCQ, Moderate) | Correct option verified: B. Relevancy: Yes. Arithmetic: usable input 7,192 vs stack 7,430 → overflow; distractors on silent truncation addressed. |
| Q6 | Objective (MCQ, Moderate) | Correct option verified: A. Relevancy: Yes. JSON A/B test flaw — high temperature + single run. |
| Q7 | Objective (MSQ, Moderate) | Correct options verified: A, B, D. Relevancy: Yes. Input size drivers for billing + latency; C/E are valid distractors. |
| Q8 | Objective (MSQ, Moderate) | Correct options verified: A, B, D. Relevancy: Yes. Silent truncation, system-slot fix, overflow symptoms; C/E distractors. |
| Q9 | Objective (MSQ, Hard) | Correct options verified: A, B, C. Relevancy: Yes. Task→temperature/max_tokens/testing pairing; D/E distractors on truncation and routing. |
| Q10 | Objective (MSQ, Hard) | Correct options verified: A, B, D, E. Relevancy: Yes. Designer checklist: audit, Groq logs, max_tokens, reply reserve; C/F distractors. |
| Q1 | Subjective (Applied, Medium) | Medium difficulty: Yes. QuickBite canteen scenario applies classifier + creative temperature contrast + usage tokens. Submission case c: Yes — single `quickbite_internals.py`, env key, LMS code box. No external dataset required. Groq API key dependency stated. Complete sample solution in answer explanation. |

---

## Overall QC Ratings

| QC Parameter | Rating / Status |
| --- | --- |
| Content Coverage (1–5) | 5 |
| Creativity (1–5) | 5 |
| Structural Adherence (1–5) | 5 |
| No Logical Mistakes (True/False) | True |
| No Presentation Mistakes (True/False) | True |

---

## Final QC Decision

All expected criteria are satisfied:

- 10 objective questions in Easy → Moderate → Hard order (6 MCQ + 4 MSQ).
- 1 medium subjective applied coding task (Groq API, temperature, max_tokens, usage tokens).
- Complete answer explanations for every objective and subjective question.
- No “as taught in session” / “mentioned in lecture” phrasing in learner-facing questions.
- Subjective scope aligned to released notes: Groq Python client, temperature trade-off, max_tokens, response.usage monitoring — no untaught seed parameter or full tiktoken audit implementation as subjective (tiktoken covered in objective only at easy level).
- Q5 arithmetic re-verified: 8192 − 800 − 200 = 7192 usable; 350 + 280 + 600 + 6200 = 7430 > 7192.
- Content Coverage, Creativity, and Structural Adherence are all 5.
- No logical or presentation mistakes identified.

**QC iteration:** 1 — passed.

---

## Coverage Checklist (released lecture notes)

| Concept in notes | Objective / Subjective coverage |
| --- | --- |
| Tokens vs words / subword tokenisation | Q2 |
| Input vs output token billing | Q1, Q10 |
| Billing + latency trade-offs | Q7 |
| Context window definition | Q3 |
| System prompt vs history placement | Q4, Q8 |
| Context budget / overflow arithmetic | Q5 |
| Temperature consistency vs creativity | Q6, Q9; Subjective Calls B & C |
| max_tokens output cap | Q9, Q10; Subjective all calls |
| Silent truncation / overflow symptoms | Q8 |
| Groq Activity / request ID monitoring | Q10 |
| Groq Python API (`chat.completions.create`) | Subjective Q1 |
| `response.usage` token counts | Subjective Q1 |
| tiktoken / token audit (introduced) | Q10 (audit via tiktoken or dashboard); not subjective implementation |

---

## CSV Export QC (`AssignmentCreation.csv`)

**Trigger:** CSV export with `tagRelationships` = `6a3a2be233ef23ca9e59f722`.

| Check | Result |
| --- | --- |
| Row count | 11 (10 objective + 1 subjective) + header |
| Question types | 6 `mcsc` + 4 `mcmc` + 1 `subjective` |
| `tagRelationships` on all rows | `6a3a2be233ef23ca9e59f722` |
| Difficulty levels | Q1–Q4: 0; Q5–Q8: 0.5; Q9–Q10 + subjective: 1 |
| `mcscAnswer` values | Q1=3, Q2=2, Q3=3, Q4=2, Q5=2, Q6=1 |
| `mcmcAnswer` values | Q7=`1, 2, 4`; Q8=`1, 2, 4`; Q9=`1, 2, 3`; Q10=`1, 2, 4, 5` |
| Option format | No A)/B) prefixes — content only |
| Question bodies | Start with scenario content, no Q-number/difficulty labels |
| Subjective `answerExplanation` | Full solution code only (no rubric/grading table) |
| CSV parse test | Python `csv.DictReader` — 12 rows, 21 columns each, no parse errors |
| Content fidelity | All question/option/explanation text matches assignment markdown sources |

### CSV Overall QC Ratings

| QC Parameter | Rating / Status |
| --- | --- |
| Content Coverage (1–5) | 5 |
| Creativity (1–5) | 5 |
| Structural Adherence (1–5) | 5 |
| No Logical Mistakes (True/False) | True |
| No Presentation Mistakes (True/False) | True |

**CSV QC iteration:** 1 — passed.
