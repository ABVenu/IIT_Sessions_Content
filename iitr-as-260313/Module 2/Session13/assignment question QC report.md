# Assignment Question QC Report
## Session: Short-Term vs Long-Term Memory in AI Agents
### Module 2 | Session 13

---

## Assignment 1 — Objective Questions QC

| Q# | Type | Correct Option(s) | Correct Option Relevant to Q? | Remarks |
|---|---|---|---|---|
| Q1 | MCQ – Easy | B – Short-Term Memory | Yes | Scenario correctly isolates STM (within-session recall, disappears on close). Distractors are meaningfully wrong — LTM would persist, Procedural/Semantic are unrelated types. |
| Q2 | MCQ – Easy | C – Context Window | Yes | "Desk" analogy directly mirrors lecture material. Distractors are real concepts but clearly distinguishable. Clean and unambiguous. |
| Q3 | MCQ – Easy | D – Buffer Memory | Yes | "No deletions, no compressions" uniquely identifies Buffer. Distractors (Window, Summary) are the other two strategies covered in the session. |
| Q4 | MCQ – Easy | C – Semantic Memory | Yes | Knowledge base of general medical facts = Semantic. Episodic would need a specific event; Procedural would be a workflow. Buffer Memory is a distractor from a different category entirely. |
| Q5 | MCQ – Moderate | C – Knee injury dropped from window | Yes | Tests practical consequence of Window Memory's core limitation. Requires understanding of "sliding window" behaviour, not just the definition. Options A, B, D are plausible but incorrect for the described scenario. |
| Q6 | MCQ – Moderate | D – 6 messages | Yes | Tests direct code comprehension of `full_history[-WINDOW_SIZE:]`. Requires knowing Python list slicing. Distractors (20, 14, 8) are plausible mis-readings of the code. |
| Q7 | MSQ – Moderate | B, C, D | Yes | All three correct answers map directly to the three named limitations from the lecture (cost, token ceiling, performance degradation). Distractors A and E describe impossible/incorrect behaviours to catch misconceptions. |
| Q8 | MSQ – Moderate | B, C, D | Yes | Three distinct accurate properties of Summary Memory (compression, LLM overhead, verbatim loss). Distractors A and E describe Buffer Memory and a false equivalence with Window Memory respectively. |
| Q9 | MSQ – Hard | A, C, D, E | Yes | Requires correct classification of all four items across Episodic, Semantic, and Procedural types. Items 1 and 4 are both Episodic but for different reasons — tests depth of understanding. Distractors B and F are intentional misclassifications. |
| Q10 | MSQ – Hard | B, C, E, F | Yes | Applied system-design question requiring reasoning across cost, scalability, and memory type selection. Distractors A (Buffer at scale) and D (single JSON file for 50K users) are common beginner mistakes. |

---

## Assignment 2 — Subjective Question QC

| Q# | Type | Difficulty | Submission Instructions Clear? | Dataset / External Resource Needed? | Remarks |
|---|---|---|---|---|---|
| Q1 | Practical Coding — Window Memory Agent | Medium | Yes — Case C (single `.py` file submitted in LMS code editor) | No — simulated LLM, no API key or external dataset required | Builds on all three memory strategy concepts; "pinned context" twist adds creative applied depth beyond a direct implementation copy. Self-contained and runnable without any dependencies. |

---

## Overall Assignment Quality Ratings

| Criterion | Objective Assignment | Subjective Assignment |
|---|---|---|
| **Content Coverage** (1–5) | 5 | 5 |
| **Creativity** (1–5) | 5 | 5 |
| **Structural Adherence** (1–5) | 5 | 5 |
| **No Logical Mistakes** | True | True |
| **No Presentation Mistakes** | True | True |

---

## QC Justification Notes

### Content Coverage — 5/5 (Both)
The objective assignment covers every major topic from the session:
- Q1–Q2: STM definition and context window
- Q3–Q4: Buffer Memory (STM strategy) and Semantic Memory (LTM type)
- Q5: Window Memory failure mode in practice
- Q6: Code comprehension of Window Memory implementation
- Q7: All three context window limitations (token, cost, performance)
- Q8: Summary Memory characteristics
- Q9: All three LTM types (Episodic, Semantic, Procedural) in one complex scenario
- Q10: Applied system design spanning STM strategies + LTM storage

The subjective question covers Window Memory implementation, pinned context design pattern, and final report analysis — synthesising both code understanding and design reasoning.

### Creativity — 5/5 (Both)
All questions are scenario-based with relatable real-world contexts (fitness coach, legal assistant, medical AI, university tutor, study assistant) rather than dry definitions. No question directly asks "define X" or "what is Y." The subjective question introduces the "pinned context" extension not explicitly coded in the lecture, requiring the student to compose concepts rather than copy code.

### Structural Adherence — 5/5 (Both)
- **Objective:** 10 questions total — 6 MCQs (4 Easy + 2 Moderate) + 4 MSQs (2 Moderate + 2 Hard), ordered progressively Easy → Moderate → Hard. Matches specification exactly.
- **Subjective:** 1 practical task with step-by-step requirements, expected output sample, submission instructions (Case C: single `.py` file), and complete ideal solution with alternative approaches in the Answer Explanation section.

### No Logical Mistakes — True (Both)
- All correct answers verified against lecture content
- Python code in Q6 and the subjective answer is syntactically and logically correct
- No scenario involves an impossible or contradictory setup
- All distractor options in MCQs and MSQs are meaningfully different from the correct answer and represent common conceptual errors, not random choices

### No Presentation Mistakes — True (Both)
- No grammatical or spelling errors
- Tables are properly formatted
- Code blocks use correct Python syntax
- All questions are self-contained with sufficient context
- Answer explanations address both correct and incorrect options clearly
