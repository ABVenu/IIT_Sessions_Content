# Lecture Notes QC Report — LLM Internals for Designers

**File reviewed:** `Lecture Notes.md`  
**Review date:** 2026-06-14  
**Iteration:** 1

---

## QC Criteria

| Criterion | Rating / Result | Notes |
|---|---|---|
| **Content Coverage** | **5 / 5** | All metadata topics covered: tokens vs words; context limits; temperature and determinism; practical RAG/agent implications. All four subtopics: tokens ↔ billing/latency/prompt length; context limits ↔ RAG and memory design; temperature/seed configuration; user-visible truncation/overload in multi-turn loops. |
| **Creativity** | **5 / 5** | DMRC metro capacity; ration shop kilograms; tiffin box compartments; IRCTC screen limits; doctor case sheet; auto-rickshaw negotiation; ShopEasy feature temperature activity. |
| **Structural Adherence** | **5 / 5** | `#` title only; context + What you will learn; Official/Simple/Real-life on new terms; full code with line comments and "How the code works"; student-facing activities (10); Key Takeaways; terminology table; mermaid diagram. |
| **No Logical Mistakes** | **True** | Builds on prior Tesla RAG, memory JSON, ReAct/Groq patterns; temperature=0 aligned with prior labs; truncation simulation correctly drops oldest messages; token budgeting logic sound. |
| **No Presentation Mistakes** | **True** | No duration/audience metadata; no "Ask students to"; paragraphs ≤3 sentences; activities student-facing. |
| **No Previous Session Number References** | **True** | Grep: no `Session N` / `session N` in notes. Uses **previous**, **upcoming**, **prior** only. |
| **No Metadata/internal reference** | **True** | No internal instruction leakage (duration, target audience, "without model-engineering depth", "Keep it Lite"). |

---

## Expected Result

- Content Coverage, Creativity, Structural Adherence: all **≥ 5** — **Met**
- No Logical Mistakes, No Presentation Mistakes, No Previous Session Number References, No Metadata/internal reference: **True** — **Met**

**Outcome:** QC passed on iteration 1.

---

## Coverage Checklist (metadata subtopics)

| Subtopic | Section in notes |
|---|---|
| Relate tokens to billing, latency, and prompt length decisions | Tokens vs Words; Measuring Tokens in Python |
| Explain how context limits constrain RAG and memory design choice | Context Limits; How Context Limits Constrain RAG Design; How Context Limits Constrain Memory and Agent Loops |
| Configure temperature or seed (where available) to trade creativity vs consistency | Temperature, Determinism, and Seed; Full Example — Same Prompt, Two Temperatures |
| Predict user-visible effects when context is truncated or overloaded in multi-turn agent loops | Simulating Truncation; Randomness in Multi-Turn Agent Loops; Activity — Diagnose a Bug Report |

**Line count:** ~556 lines.

---

## Iteration 2

**Trigger:** Second mandatory QC pass; tighten tiktoken/Groq accuracy note and remove instructor-style label.

| Criterion | Rating / Result | Notes |
|---|---|---|
| **Content Coverage** | **5 / 5** | Unchanged subtopic coverage. Added Groq/Llama tiktoken approximation caveat under "How the code works" for token counting. |
| **Creativity** | **5 / 5** | Unchanged analogies and activities. |
| **Structural Adherence** | **5 / 5** | Replaced "Why this session now:" instructor label with integrated student-facing bullet. |
| **No Logical Mistakes** | **True** | tiktoken noted as budgeting approximation; provider counter recommended for exact Groq billing — avoids false precision claim. |
| **No Presentation Mistakes** | **True** | Verified: no duration, no session numbers, student-facing activities. |
| **No Previous Session Number References** | **True** | Re-grep confirmed clean. |
| **No Metadata/internal reference** | **True** | No objective/metadata phrasing leaked into student text. |

**Outcome:** QC passed on iteration 2.

**Line count:** ~558 lines.

**Changes in iteration 2:**
- Added **Groq / Llama note** under tiktoken "How the code works"
- Replaced **Why this session now:** with plain integrated bullet

---

## Iteration 3

**Trigger:** Make notes standalone — remove previous-session and lab-specific references from core body; keep document-style introduction only.

| Criterion | Rating / Result | Notes |
|---|---|---|
| **Content Coverage** | **5 / 5** | All subtopics unchanged. Examples generalised to Acme Corp, ShopEasy, generic `chat_history.json`. |
| **Creativity** | **5 / 5** | Analogies unchanged; activities reframed as self-contained exercises. |
| **Structural Adherence** | **5 / 5** | Renamed **Context of This Session** → **Introduction** (document-style). Core sections read as standalone textbook chapter. |
| **No Logical Mistakes** | **True** | Generic examples preserve same technical logic. |
| **No Presentation Mistakes** | **True** | No "you already", "prior labs", "today you learn", or Tesla lab file paths in core notes. |
| **No Previous Session Number References** | **True** | No session numbers; intro no longer depends on prior session narrative. |
| **No Metadata/internal reference** | **True** | Removed "without model-engineering depth" from introduction. |

**Outcome:** QC passed on iteration 3.

**Standalone edits:** Introduction rewritten as general document opener; Tesla/`tesla_chat_history.json`/`./Tesla_db`/lab callbacks replaced with Acme Corp and generic patterns throughout core sections.

---

## Iteration 4

**Trigger:** Ensure activities are present across all subtopics; rerun QC after activity expansion.

| Criterion | Rating / Result | Notes |
|---|---|---|
| **Content Coverage** | **5 / 5** | All four metadata subtopics covered. **16 student-facing activities** — at least one per major section. New activities: Words vs Tokens Guess; Estimate Billing and Latency Impact; Run the Context Budget Cap; Observe Temperature in Three Runs; Seed for Regression Tests; Match Symptom to Cause; Build Your Own Request Anatomy. |
| **Creativity** | **5 / 5** | ShopEasy URL token guess; ₹ billing math; symptom-to-cause matching table; QA seed policy draft; peer spec swap retained. |
| **Structural Adherence** | **5 / 5** | `#` title; Introduction + What you will learn; Official/Simple/Real-life on new terms; 4 full code blocks with line comments and "How the code works"; activities student-facing (no "Ask students to"); Key Takeaways; terminology table. Standalone document style preserved. |
| **No Logical Mistakes** | **True** | Billing activity math consistent (4500/1000×0.002 + 350/1000×0.004 per turn); context cap script logic unchanged; truncation simulation correct; temperature/seed guidance aligned. |
| **No Presentation Mistakes** | **True** | No duration/audience metadata; paragraphs ≤3 sentences; activities use imperative student voice; fixed forward-reference in Token Budget activity (self-contained delimiter pattern). |
| **No Previous Session Number References** | **True** | Grep: no session numbers or prior-lab callbacks. |
| **No Metadata/internal reference** | **True** | No internal instruction leakage. |

**Outcome:** QC passed on iteration 4.

**Line count:** ~645 lines.

### Activity checklist (16 total)

| Activity | Maps to subtopic / section |
|---|---|
| Map a RAG + Memory Stack to Internals | Overview — prompt anatomy |
| Words vs Tokens Guess | Tokens vs words |
| Token Budget for One RAG Call | Prompt length / token measurement |
| Estimate Billing and Latency Impact | Billing, latency, prompt length |
| Context Budget Planner | Context limits |
| Run the Context Budget Cap | RAG design under token budget |
| Compare k=3 vs k=8 on Paper | RAG + context limits |
| Spot the Forgotten Rule | Memory truncation — user-visible |
| Observe Temperature in Three Runs | Temperature vs consistency |
| Seed for Regression Tests | Seed configuration |
| Pick Temperature per Feature | Temperature in agent features |
| Match Symptom to Cause | User-visible truncation/overload |
| Trace a Five-Step ReAct Budget | Multi-turn agent token overload |
| Write a Designer Spec Snippet | Practical designer playbook |
| Build Your Own Request Anatomy | End-to-end request budgeting |
| Diagnose a Bug Report | Truncation + temperature — user-visible effects |

---

## Iteration 5

**Trigger:** Reduce activities to **3** — sufficient for a 2-hour session.

| Criterion | Rating / Result | Notes |
|---|---|---|
| **Content Coverage** | **5 / 5** | All four metadata subtopics retained in lecture body. Three consolidated activities cover full session arc: Activity 1 (tokens, billing, latency, prompt length); Activity 2 (context limits, RAG/memory design, truncation UX); Activity 3 (temperature, seed, agent overload). |
| **Creativity** | **5 / 5** | ShopEasy feature table; truncation bug report; ₹ billing in Activity 1. |
| **Structural Adherence** | **5 / 5** | Three numbered activities (`Activity 1–3`); placed after relevant code sections; student-facing; Key Takeaways and terminology table unchanged. |
| **No Logical Mistakes** | **True** | Activity 2 moved after truncation simulation script; forward-reference fixed. |
| **No Presentation Mistakes** | **True** | No duration mentioned; no "Ask students to"; standalone document style preserved. |
| **No Previous Session Number References** | **True** | Verified. |
| **No Metadata/internal reference** | **True** | Verified. |

**Outcome:** QC passed on iteration 5.

**Line count:** ~508 lines (down from ~645).

**Activities kept (3):**

| Activity | Session segment | Subtopics covered |
|---|---|---|
| **Activity 1 — Token Budget for One RAG Call** | ~40 min | Tokens vs words; billing; latency; prompt length |
| **Activity 2 — Context Budget Planner** | ~40 min | Context limits; RAG/memory design; truncation user-visible effects |
| **Activity 3 — Temperature, Seed, and Feature Design** | ~40 min | Temperature; seed; creativity vs consistency; multi-turn overload |

