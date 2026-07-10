# Assignment Question QC Report

## Reuse Decision

Peer-batch assignment from `iitr-as-260113/Module3/Session39` (same topic: LangChain Memory on Agents) was **reused with minor edits**:

- **Q1–Q9 (objective):** Reused as-is — fully aligned with `Lecture Notes Released.md`.
- **Q10 (objective):** Replaced — original referenced `n_messages` rolling history, which was **not taught** in this batch's live session.
- **Q1 (subjective):** Reused structure — updated stack to `ChatOllama` + `langchain_classic.agents` and order statuses to match released notes (`shipped` / `cancelled`).

---

## Question-wise QC

| Question Number | Type | Remarks |
| --- | --- | --- |
| Q1 | Objective (MCQ, Easy) | Correct option verified: B. Relevancy: Yes. Tests stateless LLM behavior in a practical support scenario. |
| Q2 | Objective (MCQ, Easy) | Correct option verified: B. Relevancy: Yes. Clarifies placeholder vs storage responsibility. |
| Q3 | Objective (MCQ, Easy) | Correct option verified: B. Relevancy: Yes. Tests `optional=True` for empty first-turn history. |
| Q4 | Objective (MCQ, Easy) | Correct option verified: B. Relevancy: Yes. Distinguishes scratchpad from long-term chat memory. |
| Q5 | Objective (MCQ, Moderate) | Correct option verified: B. Relevancy: Yes. Targets the missing-append wiring defect from released notes. |
| Q6 | Objective (MCQ, Moderate) | Correct option verified: A. Relevancy: Yes. Applied follow-up scenario requiring rolling history. |
| Q7 | Objective (MSQ, Moderate) | Correct options verified: A, B, D. Relevancy: Yes. Manual memory wiring best practices. |
| Q8 | Objective (MSQ, Moderate) | Correct options verified: A, B, C. Relevancy: Yes. Multi-user session isolation concepts. |
| Q9 | Objective (MSQ, Hard) | Correct options verified: A, B, D. Relevancy: Yes. Correct split between `chat_history` and `agent_scratchpad`. |
| Q10 | Objective (MSQ, Hard) | Correct options verified: A, B, D. Relevancy: Yes. Replaced peer Q10; tests stateless vs memory-enabled wiring, RAM persistence limits, and `input_messages_key` alignment (taught in this batch). |
| Q1 | Subjective (Practical, Medium) | Medium difficulty: Yes. Clear submission instructions (case c, single `.py`): Yes. Dataset need: Not required (`orders_db` specified in prompt). Stack aligned to batch (`ChatOllama`, `langchain_classic`). Covers manual memory, two-turn demo, append order, and history length check. |

---

## Overall QC Ratings

| QC Parameter | Rating / Status |
| --- | --- |
| Content Coverage (1-5) | 5 |
| Creativity (1-5) | 5 |
| Structural Adherence (1-5) | 5 |
| No Logical Mistakes (True/False) | True |
| No Presentation Mistakes (True/False) | True |

---

## Final QC Decision

All expected criteria are satisfied:
- 10 objective questions in Easy → Moderate → Hard order (6 MCQ + 4 MSQ).
- 1 medium subjective coding task with full answer explanation and reference solution.
- No session-reference phrasing in learner-facing questions.
- No out-of-syllabus content (`n_messages` removed from objective Q10).
- Content Coverage, Creativity, Structural Adherence are all 5.
- No logical or presentation mistakes identified.

---

## CSV Export QC (`AssignmentCreation.csv`)

**tagRelationships:** `6a5097119ff4faa8f873d90b`

| Check | Result |
|---|---|
| Row count | 11 (6 mcsc + 4 mcmc + 1 subjective) |
| CSV parsing | Pass — no parse errors |
| Question bodies start with content (no Q#/difficulty prefix) | Pass |
| Options start with content (no A./B. prefix) | Pass |
| `tagRelationships` on all rows | Pass |
| Q10 updated for this batch (stateless vs memory; no `n_messages`) | Pass |
| Subjective solution in `answerExplanation` only (ChatOllama stack) | Pass |
| Difficulty flow | Easy (0) → Moderate (0.5) → Hard (1) |
| Content matches `assignment-objective.md` / `assignment-subjective.md` | Pass |
