# Assignment Objective

Total Questions: 10

Difficulty Flow: Easy -> Moderate -> Hard

Question Types:
- 6 MCQ (Single Correct): Q1-Q6
- 4 MSQ (Multiple Correct): Q7-Q10

---

## Q1 (MCQ, Easy)

Priya is tuning a CampusHelp policy bot. She changes chunk size, top-k, and the answer prompt on the same day, then claims retrieval improved. Why is her conclusion unreliable?

A. Prompt changes never affect answers  
B. She did not use a **fixed eval set** with the same questions before and after each change  
C. Vector databases cannot store hostel policies  
D. Hit rate only applies to SQL agents  

**Correct Answer:** B

**Answer Explanation:**  
Without a **frozen eval set**, you cannot compare scores fairly across changes. You may fix one question and break another without noticing.

**Why other options are wrong:**  
- A: Prompts do affect answers, but that is not why her comparison is unreliable.  
- C: Vector DBs can store policy text; the issue is evaluation method.  
- D: Hit rate is a retrieval metric for RAG eval sets, not SQL-only agents.

---

## Q2 (MCQ, Easy)

A retrieval eval run has **5 answerable questions**. Expected documents appear in top-k for **3** of them. What is the informal hit rate?

A. 20%  
B. 40%  
C. 60%  
D. 100%  

**Correct Answer:** C

**Answer Explanation:**  
Hit rate = hits ÷ answerable questions = 3 ÷ 5 = **0.60 (60%)**.

**Why other options are wrong:**  
- A and B: Under-count hits or over-count questions.  
- D: Two questions still missed retrieval support.

---

## Q3 (MCQ, Easy)

In the **RAG triad**, which dimension most directly tells you whether the **right chunks** were retrieved for the user question?

A. Groundedness  
B. Answer relevance  
C. Context relevance  
D. Git commit cleanliness  

**Correct Answer:** C

**Answer Explanation:**  
**Context relevance** judges retrieval quality — did the retriever bring the right evidence?

**Why other options are wrong:**  
- A: Groundedness checks if the answer is supported by retrieved text.  
- B: Answer relevance checks if the reply addresses the question.  
- D: Unrelated to RAG evaluation.

---

## Q4 (MCQ, Easy)

In a fixed eval item, what is an **expected supporting document**?

A. The final polished answer shown to the user  
B. The gold source (for example `doc_id`) that should appear in retrieval for a hit  
C. The embedding model name used at indexing time  
D. The SQL table that stores order rows  

**Correct Answer:** B

**Answer Explanation:**  
Expected supporting documents are **gold retrieval labels** — which policy or chunk should be in top-k for the question to count as a retrieval success.

**Why other options are wrong:**  
- A: Final answers are evaluated separately from retrieval labels.  
- C: Model choice is a tuning knob, not an eval label.  
- D: SQL tables are structured data paths, not RAG chunk labels.

---

## Q5 (MCQ, Moderate)

CampusHelp eval question: *"Can I submit an assignment 1 day late?"* Expected doc: **`D2`**. Retrieved top-k: **`D5`, `D3`, `D1`**. The final answer still mentions a late penalty. What is the best **first** failure classification and fix direction?

A. Generation failure — rewrite the prompt only  
B. Retrieval failure — tune retrieval (chunking, embedding, or `k`) before blaming the prompt  
C. Database failure — rebuild the SQL schema  
D. No failure — any answer about penalties is acceptable  

**Correct Answer:** B

**Answer Explanation:**  
Expected **`D2`** never appeared in retrieval, so the model lacked the right evidence. That is a **retrieval failure**; prompt-only edits are a weak first fix.

**Why other options are wrong:**  
- A: Prompt edits do not replace missing evidence.  
- C: This scenario is policy retrieval, not SQL schema design.  
- D: Wrong evidence path means retrieval did not meet the eval label.

---

## Q6 (MCQ, Moderate)

Your team uses **LLM-as-judge** to score RAG answers. Which setup best reduces bias?

A. Use the **same** model that generated the answer as the judge  
B. Use a **separate**, usually stronger, model as the judge  
C. Disable all retrieval and judge only the user question  
D. Let end users vote once and skip structured scores  

**Correct Answer:** B

**Answer Explanation:**  
A different judge model improves objectivity. The same model judging itself tends to be lenient.

**Why other options are wrong:**  
- A: Same-model judging is biased.  
- C: Judges need the response (and often context) to score quality.  
- D: Informal votes do not replace triad-style checks.

---

## Q7 (MSQ, Moderate)

Which practices belong in a **well-designed fixed eval set** for RAG retrieval tuning?

A. Write **expected `doc_id`s** before running retrieval  
B. Include at least one **no-answer** question (no supporting doc in corpus)  
C. Change the question list after every experiment so results feel fresh  
D. Keep the set small enough to score hits and misses by hand  

**Correct Answers:** A, B, D

**Answer Explanation:**  
Gold labels upfront, no-answer cases, and a small scorable set are core eval habits. Freezing questions enables fair before/after comparison.

**Why option C is wrong:**  
Changing questions between runs breaks comparability.

---

## Q8 (MSQ, Moderate)

Hit rate stays low and **context relevance** judge scores are weak. Which are sensible **retrieval-side** experiments on the **same** frozen eval set?

A. Try **semantic chunking** instead of naive fixed-size splits  
B. Swap or upgrade the **embedding model** (for example a stronger model than your baseline)  
C. Increase **top-k** when the right chunk may be ranked low  
D. Only increase temperature on the answer model  

**Correct Answers:** A, B, C

**Answer Explanation:**  
Chunker type, embeddings, and `k` directly affect which chunks enter context. These are standard retrieval fixes when evidence is missing or wrong.

**Why option D is wrong:**  
Temperature affects generation randomness, not which chunks are retrieved.

---

## Q9 (MSQ, Hard)

Which scenarios are best classified as a **retrieval failure** (expected supporting document **missing** from top-k)?

A. Expected **`D4`** for a mess-refund question, but top-k returns only `D2`, `D5`, `D1`  
B. Expected **`D3`** is in top-k, but the answer says the library is open 24/7 on Sunday  
C. Expected **`D2`** for a late-submission question, but top-k returns `D5`, `D3`, `D1`  
D. Expected **`D5`** is in top-k and the answer correctly explains guest Wi-Fi pass rules  

**Correct Answers:** A, C

**Answer Explanation:**  
Retrieval failure means the **gold document never entered top-k**. Cases A and C match that pattern.

**Why options B and D are wrong:**  
- B: Expected doc was retrieved — that is a **generation** misread, not retrieval miss.  
- D: Retrieval succeeded; this is a pass case, not a failure.

---

## Q10 (MSQ, Hard)

An **agentic RAG** e-commerce support bot routes between tools. Which statements are correct?

A. **SQL agent tool** fits live order status from a structured database  
B. **RAG retriever tool** fits return or shipping policy questions from embedded documents  
C. A **top-level agent** chooses which tool to call per user question  
D. Agentic RAG means retrieval replaces all SQL queries permanently  

**Correct Answers:** A, B, C

**Answer Explanation:**  
Agentic RAG combines structured SQL tools and unstructured policy retrieval under one routing agent.

**Why option D is wrong:**  
SQL and RAG serve different data types; one does not permanently replace the other.
