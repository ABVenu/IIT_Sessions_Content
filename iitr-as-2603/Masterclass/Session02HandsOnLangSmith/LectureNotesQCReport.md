# Lecture Notes QC Report — LangSmith: LLM Application Evaluation and Monitoring

**File reviewed:** `Lecture Notes.md`  
**Folder:** `IIT_Sessions_Content/iitr-as-2603/Masterclass/Session02HandsOnLangSmith`  
**Review date:** 2026-09-20

---

## Iteration 1 (first full draft)

### QC Criteria

| Criterion | Rating / Result | Notes |
|---|---|---|
| **Content Coverage** | **4 / 5** | Direct LangSmith intro, vs local EvalPack, LCEL + LangGraph desk, dataset/experiment, monitoring all present. Draft was **546 lines** (metadata target **480–500**). Duplicate setup tables; folder tree; Phase-1-only command; skipped-imports table bloated the band. |
| **Creativity** | **5 / 5** | Continues the T20 desk from previous LangChain work; LangGraph classify → rules/incident/refuse so students who already know graphs see **nested spans**; project vs Datasets door is a real UI gotcha. |
| **Structural Adherence** | **4 / 5** | Clean `#` title; Official / Simple / Real-Life on LangSmith, traces, `@traceable`, monitoring. **Dataset / evaluator** shared a thin experiment-only triad. Several code list rows uncommented. “How the code works” Phase 2/3 bullets exceeded the 3-sentence rule. |
| **No Logical Mistakes** | **False** | `setdefault` on `LANGSMITH_TRACING` would leave tracing **off** if the shell exported `false`. Rules-path keyword `2` could fail if Groq wrote **two**. FIFA empty keywords already used `score=None` (good). |
| **No Presentation Mistakes** | **True** | No duration / audience in body; four S3 images; student-facing activities. |
| **No Previous Session Number References** | **True** | Previous work named as LangChain / T20 assistant / LangGraph nodes only. |
| **No Metadata/Internal References in Student Text** | **True** | No lite/keep-it-light/instructor labels. |

### Expected Result

- Not met (coverage 4, structure 4, logical mistake True→False required; line count over band)

**Outcome:** QC failed. Improvise, then re-run.

### Improvisation applied (iteration 1 → 2)

1. Cut to metadata band: merged env/package tables, dropped folder tree and Phase-1-only command, compacted signatures / span table / skipped-imports, tightened RULEBOOK and evaluate() call.
2. Force `LANGSMITH_TRACING` and `LANGCHAIN_TRACING_V2` **on**; keep `setdefault` only for the project name.
3. Rules system line: **use digits for counts**; INC-102 keywords taken from the **dict**, not the LLM.
4. End-of-line comments on RULEBOOK, INC rows, live queries, and CASES.
5. Split Phase 2/3 “How the code works” bullets; added Dataset + Evaluator triads.
6. Four lecture images uploaded to S3 and linked.

---

## Iteration 2 (after improvise)

**Line count:** 500 (upper bound of 480–500).

### QC Criteria

| Criterion | Rating / Result | Notes |
|---|---|---|
| **Content Coverage** | **5 / 5** | Direct LangSmith intro; advantages / disadvantages; vs EvalPack; traces/spans/`@traceable`; LCEL Phase 1; one-file T20 LangGraph desk; dataset + `evaluate()`; N/A keywords; v1 vs v2 patch; monitoring tiles; Groq + langgraph + langsmith stack. Prior LangGraph (nodes, edges, state, checkpoints, retries) and LangChain LCEL named without session ids. |
| **Creativity** | **5 / 5** | Same T20 product, new **control-room** layer; graph branches as clickable spans; Datasets vs project run list taught as two doors. |
| **Structural Adherence** | **5 / 5** | `#` title only; previous-work context; connecting sentences; Official / Simple / Real-Life on LangSmith, EvalPack, trace/span, `@traceable`, instrumented desk, dataset/experiment, evaluator, monitoring; full file + How the code works; student activities; Key Takeaways; terminology table. |
| **No Logical Mistakes** | **True** | Tracing forced on; digit instruction for keyword `2`; incident keywords from INC-102 text; history not needed (one-shot tickets); empty keywords `None`; idempotent dataset seed; teaching samples labelled non-ICC; graph vs chain jobs not conflated. |
| **No Presentation Mistakes** | **True** | No duration/audience; four S3 architecture/eval/monitoring figures (no 1/5 badges); scannable tables. |
| **No Previous Session Number References** | **True** | Grep clean for `Session N` / `session N` in student prose (image keys use `session02-` filenames only). |
| **No Metadata/Internal References in Student Text** | **True** | No keep-it-light / lite version / instructor-only headings. |

### Expected Result

- All criteria **Met**

**Outcome:** QC passed on iteration 2.

---

## Coverage Checklist (metadata subtopics)

| Subtopic | Section in notes |
|---|---|
| Direct LangSmith intro (not scenario-first) | What Is LangSmith |
| Building blocks; advantages; disadvantages; vs EvalPack | What Is LangSmith; LangSmith and a Local EvalPack |
| Prior LangGraph / LangChain / golden EvalPack, no session numbers | Context of This Session |
| Env vars: `LANGSMITH_TRACING`, API key, project, `LANGCHAIN_TRACING_V2` | Before You Start — Setup |
| LCEL: `ChatPromptTemplate \| ChatGroq \| StrOutputParser` | Phase 1 in the file; LCEL mentioned in build table |
| One file, three phases | What You Will Build; complete `t20_langsmith_lab.py` |
| T20 LangGraph classify → rules / incident / refuse | The Complete App |
| Nested spans + `@traceable` | Traces, Spans, and Nested Runs; extract/lookup helpers |
| Dataset, `evaluate()`, route + keywords, N/A refusal | Phase 3; How the code works |
| Experiment compare after one patch | Dataset, evaluators, and one patch |
| Monitoring: errors, latency, tokens, pass rate | Monitoring — after many runs |
| Groq + langgraph + langsmith | Setup + terminology table |

---

## Differentiation Check vs This Batch’s LangGraph / LangChain Work

| Aspect | Already taught | This masterclass | OK? |
|---|---|---|---|
| Picture | Nodes, edges, shared state, checkpoints, retries | Same graph **watched** as nested LangSmith spans | Yes |
| LangChain | LCEL, AgentExecutor T20 assistant, local EvalPack | Env-based tracing of that file; new graph desk scored as a **dataset experiment** | Yes |
| App | T20 rulebook + INC log | Same domain; RAG/Chroma skipped on purpose | Yes |
| Model | `ChatGroq` + `llama-3.1-8b-instant` | Same classroom Groq id | Yes |

---

## Iteration 3 (verification pass — required even after pass)

Re-read the live `Lecture Notes.md` against `LectureNotesPrompt4.md` + `LectureNotesQC.md` + `metadata.md`.

**Line count:** 500. Images resolve under `iitr-as-2603/masterclass/session02-hands-on-langsmith/`. Tracing force-on, digit keyword, N/A `score=None`, and evaluator triad re-checked. No session-number or metadata leaks in student prose.

### QC Criteria

| Criterion | Rating / Result |
|---|---|
| **Content Coverage** | **5 / 5** |
| **Creativity** | **5 / 5** |
| **Structural Adherence** | **5 / 5** |
| **No Logical Mistakes** | **True** |
| **No Presentation Mistakes** | **True** |
| **No Previous Session Number References** | **True** |
| **No Metadata/Internal References in Student Text** | **True** |

### Expected Result

- All criteria **Met**

**Outcome:** QC passed on iteration 3. No further improvisation required at that time.

---

## Iteration 4 (prior-knowledge correction — LangGraph only)

**Change request:** Do not treat **LangChain** as previous work. One batch has not learnt LangChain. Both batches have learnt **LangGraph**.

### QC Criteria (before this pass)

| Criterion | Rating / Result | Notes |
|---|---|---|
| **Content Coverage** | **4 / 5** | LangSmith coverage intact, but context assumed LCEL, EvalPack, and `t20_rules_assistant.py`. |
| **Creativity** | **4 / 5** | T20 desk was framed as a continuation of a LangChain assistant one batch never built. |
| **Structural Adherence** | **4 / 5** | Previous-work paragraph named LangChain as prior. |
| **No Logical Mistakes** | **False** | Students without LangChain could not follow “re-run the previous T20 file” or “you already ship an EvalPack.” |
| **No Presentation Mistakes** | **True** | |
| **No Previous Session Number References** | **True** | |
| **No Metadata/Internal References in Student Text** | **True** | |

**Outcome:** QC failed on shared-batch prior knowledge. Improvise, then re-run.

### Improvisation applied (iteration 4 → 5)

1. Context now names only **LangGraph** (nodes, edges, state, checkpoints, retries, golden questions).
2. Phase 1 is `demo_graph_trace()` — one `graph.invoke`, not an LCEL warm-up.
3. Local **EvalPack** wording → **golden pack** (matches graph labs). Removed `t20_rules_assistant.py` activity; replaced with “trace any previous LangGraph invoke.”
4. Stack image regenerated without LangChain as a prior layer. ChatGroq kept only as the LLM **inside nodes**.
5. Takeaways / confidence Q1 compare LangSmith with **LangGraph** only.

---

## Iteration 5 (after prior-knowledge fix)

**Line count:** 496 (inside 480–500).

### QC Criteria

| Criterion | Rating / Result | Notes |
|---|---|---|
| **Content Coverage** | **5 / 5** | Direct LangSmith intro; vs local golden pack; traces/spans/`@traceable`; Phase 1 graph invoke; T20 LangGraph desk; dataset + `evaluate()`; N/A keywords; v1 vs v2; monitoring. Prior knowledge is LangGraph + Groq + golden questions only. |
| **Creativity** | **5 / 5** | Same T20 graph product, control-room layer, Datasets vs project doors. |
| **Structural Adherence** | **5 / 5** | `#` title; previous-work context without LangChain; Official / Simple / Real-Life; full file; student activities; takeaways; terminology table. |
| **No Logical Mistakes** | **True** | No assumed LangChain assistant; tracing forced on; digit keyword; incident keywords from dict; empty keywords `None`. `langchain-core` / `LANGCHAIN_TRACING_V2` remain as **install/env names**, not prior curriculum. |
| **No Presentation Mistakes** | **True** | Four S3 images; stack figure is LangGraph-first. |
| **No Previous Session Number References** | **True** | |
| **No Metadata/Internal References in Student Text** | **True** | |

### Expected Result

- All criteria **Met**

**Outcome:** QC passed on iteration 5.

---

## Iteration 6 (verification pass — required even after pass)

Re-read live `Lecture Notes.md`. Grep clean for LangChain / LCEL / EvalPack / `t20_rules_assistant` as **student prior knowledge**. Remaining `langchain-*` strings are pip packages, `LANGCHAIN_TRACING_V2`, and smith.langchain.com — product names, not “you already learnt this.” Line count **496**.

### QC Criteria

| Criterion | Rating / Result |
|---|---|
| **Content Coverage** | **5 / 5** |
| **Creativity** | **5 / 5** |
| **Structural Adherence** | **5 / 5** |
| **No Logical Mistakes** | **True** |
| **No Presentation Mistakes** | **True** |
| **No Previous Session Number References** | **True** |
| **No Metadata/Internal References in Student Text** | **True** |

### Expected Result

- All criteria **Met**

**Outcome:** QC passed on iteration 6. No further improvisation required.
