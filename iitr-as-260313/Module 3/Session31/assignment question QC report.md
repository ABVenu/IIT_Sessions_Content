# Assignment Question QC Report — Session31 (`iitr-as-260313`)

## Reuse Decision (from `iitr-as-260113` / Module3 / Session40)

| Item | Can reuse as-is? | Reason |
|---|---|---|
| Session40 `assignment-objective.md` | **No** | Many items require **LCEL**, `RunnablePassthrough`, `StrOutputParser`, OpenAI `text-embedding-3-*`, `DirectoryLoader`/`persist_directory` handbook flow not taught in this batch’s **Released** notes |
| Session40 `assignment-subjective.md` | **No** | Full **LCEL** chain + OpenAI embeddings + Markdown ingest + persist reload — out of syllabus for Session31 Released notes (imperative retrieve → delimiters → **Groq** / GTE-large) |

**Partial concept overlap (do not copy questions):** need for RAG, chunk overlap idea, grounding “I don’t know”, top-k / retriever basics.

**Action taken:** Wrote **new** `assignment-objective.md` and `assignment-subjective.md` aligned to `Lecture Notes Released.md` for this session.

---

## QC Iteration 1 — New Assignments

### Overall scores

| Criteria | Score |
|---|---|
| Content Coverage | **5 / 5** |
| Creativity | **5 / 5** |
| Structural Adherence | **5 / 5** |
| No Logical Mistakes | **True** |
| No Presentation Mistakes | **True** |

### Objective questions (Q1–Q10)

| Question | Type | Remarks |
|---|---|---|
| Q1 | MCQ Easy | Correct **A** — relevancy **Yes** (needs retrieved company docs) |
| Q2 | MCQ Easy | Correct **A** — relevancy **Yes** (`PyPDFDirectoryLoader` → Documents) |
| Q3 | MCQ Easy | Correct **A** — relevancy **Yes** (`chunk_overlap`) |
| Q4 | MCQ Easy | Correct **A** — relevancy **Yes** (`##context` / `##question`) |
| Q5 | MCQ Moderate | Correct **A** — relevancy **Yes** (same-model / GTE mismatch) |
| Q6 | MCQ Moderate | Correct **A** — relevancy **Yes** (latency vs high **k**) |
| Q7 | MSQ Moderate | Correct **A, B, D** — relevancy **Yes** (offline prepare; C is online) |
| Q8 | MSQ Moderate | Correct **A, B** — relevancy **Yes** (grounded system rules) |
| Q9 | MSQ Hard | Correct **A, C, D** — relevancy **Yes**; **B** wrong because temp=0 is recommended |
| Q10 | MSQ Hard | Correct **A, B, C** — relevancy **Yes**; **D** excludes untaught LCEL requirement |

**Structure check:** 6 MCQ (4 Easy + 2 Moderate) + 4 MSQ (2 Moderate + 2 Hard); Easy → Moderate → Hard order respected. Explanations include correct answer + wrong-option reasons. No “as taught in the session” phrasing.

### Subjective question (Q1)

| Question | Type | Remarks |
|---|---|---|
| Q1 | Practical Medium | Medium difficulty **Yes**; submission instructions (case **d** GitHub) **Yes**; policy text provided in-prompt **Yes**; dataset/extra downloads not required **N/A**; matches taught stack (GTE-large, Chroma, `get_relevant_documents`, delimiters, Groq `temperature=0`); **does not** require LCEL |

**Loader note:** Subjective allows `DirectoryLoader`/`TextLoader` for the two `.md` files (mentioned in Released notes alongside PDF loaders) to avoid forcing students to manufacture PDFs, while keeping the imperative RAG path identical to class.

---

## Expected-result gate

| Gate | Met? |
|---|---|
| Coverage / Creativity / Structure ≥ 5 | **Yes** |
| No logical mistakes | **Yes** |
| No presentation mistakes | **Yes** |
| No out-of-syllabus asks (vs Released notes) | **Yes** (LCEL / OpenAI handbook path excluded) |

**Final verdict:** **PASS** — new Session31 assignments ready; Session40 pack should **not** be released to this batch unchanged.
