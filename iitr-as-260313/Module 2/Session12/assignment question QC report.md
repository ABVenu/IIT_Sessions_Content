# Assignment Question QC Report — Introduction to Memory in AI Agents

---

## Question-Level QC

| Question No. | Type | Remarks |
|---|---|---|
| Q1 | MCQ (Single Correct) | Correct Answer: B — Relevant ✅. Tests stateless agent identification from a real scenario. |
| Q2 | MCQ (Single Correct) | Correct Answer: B — Relevant ✅. Tests understanding of "state" through the doctor analogy used in session. |
| Q3 | MCQ (Single Correct) | Correct Answer: A — Relevant ✅. Tests the repetition problem as a named limitation from the session. |
| Q4 | MCQ (Single Correct) | Correct Answer: C — Relevant ✅. Tests correct identification of short-term (in-context) memory. |
| Q5 | MCQ (Single Correct) | Correct Answer: A — Relevant ✅. Tests context loss in a multi-turn scenario using the Goa trip example pattern. |
| Q6 | MCQ (Single Correct) | Correct Answer: C — Relevant ✅. Tests correct architecture choice (long-term memory + retrieval into context window) for a multi-session product. |
| Q7 | MSQ (Multiple Correct) | Correct Answers: A, C, E — Relevant ✅. All three stateful choices involve multi-turn, personalisation, or continuity; B and D are clearly single-turn one-off tasks. No ambiguity. |
| Q8 | MSQ (Multiple Correct) | Correct Answers: A, B, C, E — Relevant ✅. All four match the 7-step agent memory flow taught in the session; D is explicitly contradicted in the notes (model has no memory of users from training). |
| Q9 | MSQ (Multiple Correct) | Correct Answers: A, C, E — Relevant ✅. Injury, duration preference, and weight goal are durable, future-useful, and session-aligned. Greeting, trivia, and temporary mood are correctly excluded per session's selectivity guidance. |
| Q10 | MSQ (Multiple Correct) | Correct Answers: A, C, D, F — Relevant ✅. All four match explicit session guidance. B and E are clearly contradicted: B violates selectivity principle; E contradicts the session's privacy section (DPDP Act / GDPR). |
| S1 (Subjective) | Practical Task — Applied Theory | Medium difficulty ✅. Creative scenario-based (TalentBot recruitment AI). Submission instructions clearly stated (Google Doc, case b). No dataset required — all scenario data is embedded in the question. All four sections test distinct session concepts: stateless limitations, memory types & design, context assembly, privacy. Answer Explanation provided with ideal walkthrough and alternative approaches. |

---

## Overall Assignment QC Ratings

| Criterion | Rating (1–5) | Notes |
|---|---|---|
| Content Coverage | 5 | Objective covers: stateless/stateful, state concept, repetition problem, short-term memory, context loss, stateful use cases, memory flow steps, memory design (what to store), memory types, privacy. Subjective covers: stateless limitations, all memory types, context assembly, and privacy — together the two assignments span the full session scope. |
| Creativity | 5 | Objective uses fresh real-world scenarios (food delivery, travel assistant, fitness coach, career coach, banking) distinct from the notes' own examples. Subjective uses a novel recruitment AI context not present in notes or objective, requiring applied analysis rather than recall. |
| Structural Adherence | 5 | Objective: exactly 6 MCQs (4 Easy, 2 Moderate) + 4 MSQs (2 Moderate, 2 Hard), ordered Easy → Moderate → Hard. Answer explanations provided for every question including wrong option reasoning. Subjective: exactly 1 practical task, medium difficulty, document-style submission (case b), answer explanation with ideal walkthrough and alternative approaches. |
| No Logical Mistakes | True | All correct answers verified against session notes. Distractors are plausible but clearly incorrect based on session content. Subjective scenario data is internally consistent (Divya's memory items align with her application state). |
| No Presentation Mistakes | True | No spelling errors, grammatical issues, or formatting inconsistencies identified. Tables render correctly. Submission instructions are clear and complete. Section labels are unambiguous. |
