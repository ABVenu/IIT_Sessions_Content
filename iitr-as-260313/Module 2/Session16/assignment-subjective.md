# Assignment — Subjective (Session 16)

**Theme:** Explain **why** modern AI help systems use embeddings and semantic search instead of plain keyword lookup.

**Difficulty:** Medium

---

## Scenario

You have joined a company as an **Agentic Systems Designer**. The internal **employee help chatbot** you inherited works like this:

- **Structured questions** (user ID, order ID, leave balance) are answered with **plain SQL** on company tables.
- **Policy and FAQ questions** are answered with **text-only matching**: `SQL LIKE`, keyword search, or Ctrl+F-style lookup on stored FAQ lines.
- The previous team also proposed a growing **synonym dictionary** (manual word pairs) instead of changing the retrieval design.

Leadership wants the bot to handle **real employee wording** (paraphrases, informal language, different terms for the same request). As the specialist, you must write a short **design rationale** explaining what is wrong with the current FAQ approach and why the system should move toward **embeddings and semantic search** (with **cosine similarity** used inside the comparison step—not coded by you in this task).

**No code required**—this is a written explanation only.

---

## Task (single response)

Write **one structured answer** (about **250–400 words**) that covers **all four** points below. Use **concrete examples** from this company help-bot context (HR policy, IT access, refunds, leave rules, etc.—you may invent realistic lines).

1. **Plain / keyword search limits** — Why can plain search fail when the user’s words and the best FAQ line use **different wording** for the **same intent**? Give **one concrete** user question and **one FAQ sentence** that would **not** match on shared keywords.

2. **Why semantic search is needed** — What does semantic search do differently (search by **meaning / intent**, not only shared words)?

3. **Why embeddings are needed** — Why must text be turned into **vectors** (lists of numbers) before the system can compare meaning? (Computers do not “understand” English directly.)

4. **Why not only a synonym dictionary** — Why is a hand-built **synonym / keyword mapping table** a weak long-term fix compared to **embedding-based** semantic search? Mention at least **one** problem such as new phrasing, scale, or maintenance.

**Optional (one sentence):** Where does **cosine similarity** fit in—what is its job after embeddings exist? (Concept only; no formula.)

---

## Quality bar

- Write in **complete sentences** (not only bullet fragments).
- Do **not** copy lecture headings verbatim; explain in your own words.
- Stay within topics from this session (keyword vs semantic, embeddings, vectors, chunking/RAG only if needed for examples)—**no** vector-database setup, **no** dot-product maths, **no** code.

---

## Submission instructions (**case a** — written answer)

- Type your full answer in the LMS **answer box** for this question.
- Proofread once for clarity and grammar before submitting.

---

## Answer explanation (for facilitators / LMS)

### Model answer outline (not exhaustive)

**1. Plain search:** Example — user: *“I forgot my login password”*; FAQ: *“Recover account access from Settings > Security”* — few or no shared keywords, so `LIKE '%password%'` on stored text may miss the right FAQ even though a human sees the same intent.

**2. Semantic search:** Retrieves by **meaning** (e.g. remote work policy vs work-from-home rules), handles paraphrases and informal wording better than exact term match.

**3. Embeddings:** Models map text to **fixed-length number lists** so the machine can **compare** which FAQ vectors are **closer** to the question vector—same idea as “closer numbers ≈ similar meaning” from class.

**4. Synonym dictionary limits:** Every new phrase needs manual rules; Hindi-English mix, typos, and long-tail questions explode maintenance; embeddings generalize from learned representation instead of enumerating every word pair.

**Cosine (optional):** After embeddings exist, **cosine similarity** (handled by library/vector DB) picks **which stored vector is closest** to the query vector—learners need not derive the formula.

### What a strong learner answer demonstrates

- Applied reasoning with a **specific** mismatch example (not generic “keywords bad”).
- Clear chain: **keyword failure → semantic search → embeddings as numbers → why lookup tables don’t scale**.
- No requirement to implement retrieval code (aligned with live class: concepts and workflow, implementation deferred).

### Common weak answers

- Only defines embeddings without explaining **why** keywords fail on the example.
- Suggests “use ChatGPT instead” with no retrieval/embeddings link.
- Proposes coding cosine by hand as the main solution (out of session scope).
