# Assignment Question QC Report

## Question-wise QC

| Question Number | Type | Remarks |
| --- | --- | --- |
| Q1 | Objective (MCQ, Easy) | Correct option verified: B. Relevancy: Yes. Multimodal definition from released notes. |
| Q2 | Objective (MCQ, Easy) | Correct option verified: B. Relevancy: Yes. STT is first stage of speech pipeline. |
| Q3 | Objective (MCQ, Easy) | Correct option verified: B. Relevancy: Yes. YouTube auto-captions as STT example. |
| Q4 | Objective (MCQ, Easy) | Correct option verified: B. Relevancy: Yes. One `GROQ_API_KEY` for STT + summary; gTTS is not an LLM key. |
| Q5 | Objective (MCQ, Moderate) | Correct option verified: B. Relevancy: Yes. Vision as parallel input path. |
| Q6 | Objective (MCQ, Moderate) | Correct option verified: B. Relevancy: Yes. Multimodal parsing before chunking (LlamaParse / PyMuPDF). |
| Q7 | Objective (MSQ, Moderate) | Correct options verified: A, B, D. Relevancy: Yes. Transcript quality checklist from released notes. |
| Q8 | Objective (MSQ, Moderate) | Correct options verified: A, C. Relevancy: Yes. Groq Whisper + shared client; gTTS and Groq vision distractors rejected. |
| Q9 | Objective (MSQ, Hard) | Correct options verified: A, B, D. Relevancy: Yes. Real-world STT/TTS flows; photo + Whisper option correctly excluded. |
| Q10 | Objective (MSQ, Hard) | Correct options verified: A, B, D. Relevancy: Yes. Multimodal RAG parsing and chunking concepts. |
| Q1 | Subjective (Practical, Medium) | Medium difficulty: Yes. Clear submission instructions (case c — single `.py`): Yes. Sample audio URL and quality flags specified: Yes. Covers STT → summarize → TTS only (vision skipped — surface-level in notes). No out-of-syllabus APIs. |

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

## Scope Alignment Notes

- Questions align strictly with **`Lecture Notes Released.md`**: multimodal pipeline, Groq STT/summary, gTTS, parsing/multimodal RAG concepts, transcript quality, real-world STT/TTS examples.
- Hugging Face vision is tested only at conceptual level in objective items (Groq has no image models); **not** required in subjective implementation.
- No session-reference phrasing in question prompts.
- Objective structure: 6 MCQ (4 Easy Q1–Q4, 2 Moderate Q5–Q6) + 4 MSQ (2 Moderate Q7–Q8, 2 Hard Q9–Q10).

---

## Final QC Decision

All expected criteria are satisfied:
- Content Coverage, Creativity, Structural Adherence are all 5.
- No logical mistakes.
- No presentation mistakes.
