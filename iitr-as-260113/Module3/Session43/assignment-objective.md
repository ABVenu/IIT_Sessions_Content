# Assignment Objective

Total Questions: 10

Difficulty Flow: Easy → Moderate → Hard

Question Types:
- 6 MCQ (Single Correct): Q1–Q6
- 4 MSQ (Multiple Correct): Q7–Q10

---

## Q1 (MCQ, Easy)

Priya's **UPI payment** fails at a tea stall. Instead of guessing, she checks whether the issue is **network**, **wrong PIN**, or **bank server downtime** before trying again.

Which definition best matches **debugging** in software?

A. Rewriting the entire application whenever one user complains  
B. Finding the **root cause** of incorrect behaviour and fixing it so the system works as expected  
C. Changing the LLM model name without reading logs  
D. Deleting all test cases so failures disappear from reports

**Correct Answer:** B

**Answer Explanation:**  
Debugging is a two-step discipline: **locate** where things break, then **repair** the underlying cause — not mask symptoms.

**Why other options are wrong:**  
- A: Full rewrites without diagnosis waste time and hide regressions.  
- C: Model swaps without checking prompt, tools, or retrieval are a common anti-pattern.  
- D: Removing tests does not fix bugs.

---

## Q2 (MCQ, Easy)

A team tests a **GST calculator agent** by comparing only the **final sentence** to an expected answer. Traces show the agent called **`search_course_policy`** instead of **`calculate_gst`**, but the final text still sounds confident.

What is the **main limitation** of final-answer-only debugging here?

A. Trajectory checks are illegal for LangChain agents  
B. The polite final text can hide a **wrong tool path** — you must inspect tools, retrievals, and refusals too  
C. GST questions never need tools  
D. CSV files cannot store failure types

**Correct Answer:** B

**Answer Explanation:**  
**Trajectory debugging** inspects the step-by-step path. A correct-sounding answer built on the wrong tool is still a failure.

**Why other options are wrong:**  
- A: Trajectory inspection is standard professional practice.  
- C: Arithmetic cases often require a calculator tool.  
- D: `results.csv` and traces are designed for this workflow.

---

## Q3 (MCQ, Easy)

Your lead files an incident as **failure class: weak retrieval** after users complain that policy answers cite irrelevant paragraphs.

What does **failure class** mean in agent debugging?

A. A random nickname for any bug  
B. A **category of defect** (e.g. wrong tool, weak retrieval) used to pick the right fix  
C. The Python class name of the LangChain retriever  
D. The number of tokens in the system prompt

**Correct Answer:** B

**Answer Explanation:**  
Failure classes **group** similar mistakes so remediation is targeted — like sorting railway delays by signal vs crew issues.

**Why other options are wrong:**  
- A: The label is purposeful, not random.  
- C: It is a QA concept, not a code class name.  
- D: Token count relates to cost metrics, not defect taxonomy.

---

## Q4 (MCQ, Easy)

A user asks about **return policy**, but the agent calls **`get_weather`**. The engineer notices the weather tool's **description** still says *"use for any user question."*

What is the **most likely** failure class and first fix direction?

A. Excessive tool calling — add `max_iterations` only  
B. **Wrong tool selection** — apply a **tool patch** (clearer name and description)  
C. Slow response — buy a faster laptop  
D. Under-refusal — remove all guardrails

**Correct Answer:** B

**Answer Explanation:**  
Vague tool metadata steers the LLM to the wrong worker. Sharpening **tool name/description** is the classic **tool patch** for wrong-tool failures.

**Why other options are wrong:**  
- A: Loops are not described; one wrong tool was picked.  
- C: Latency is unrelated to tool routing.  
- D: The agent answered via the wrong tool, not refusal tuning.

---

## Q5 (MCQ, Moderate)

A **course support bot** refuses a valid question: *"What is the refund window for my batch?"* with *"I cannot discuss unrelated topics."*

Which failure class applies?

A. **Over-refusal** — guardrails are too strict for an in-domain query  
B. **Under-refusal** — the bot answered an out-of-domain cricket score  
C. **Bad tool arguments** — empty `order_id` was passed  
D. **Hallucinated response** — the bot invented a phone number

**Correct Answer:** A

**Answer Explanation:**  
**Over-refusal** rejects questions the product **should** answer. Fix direction: **relax** prompt guardrails for in-domain topics.

**Why other options are wrong:**  
- B: Under-refusal means answering what should be blocked.  
- C: No tool argument issue is described.  
- D: No fabricated contact info is described.

---

## Q6 (MCQ, Moderate)

A ShopEasy RAG bot uses **`chunk_size=50`**. For *"What is the return window for electronics items?"*, similarity search returns a chunk containing **"electronics"** but not **"seven days"**. The LLM replies: *"I don't know based on the provided documents."*

What is the **best** failure class label?

A. Missing API key  
B. **Weak retrieval** caused by **bad chunking** — tune `chunk_size` / `chunk_overlap`  
C. Excessive tool calling loop  
D. Under-refusal on out-of-domain query

**Correct Answer:** B

**Answer Explanation:**  
The retriever surfaced a **partially relevant** chunk — keyword match without the policy sentence. This is **weak retrieval** fixed by **retrieval tuning**, not a new LLM.

**Why other options are wrong:**  
- A: The pipeline ran; retrieval content was insufficient.  
- C: No retry loop is described.  
- D: The query is in-domain; the bot tried but lacked context.

---

## Q7 (MSQ, Moderate)

An agent keeps answering GST math questions **without** calling **`calculate_gst`**, even though the tool exists.

Which remediation steps are **appropriate** (first iteration)?

A. **Prompt patch** — add *"You **must** call `calculate_gst` for tax and percentage questions"*  
B. **Tool patch** — rewrite the calculator tool description with explicit use cases  
C. Delete the vector database to force tool use  
D. Add one or two **few-shot examples** in the system prompt showing calculator routing

**Correct Answers:** A, B, D

**Answer Explanation:**  
**Missing tool call** failures are addressed by clearer **prompt** enforcement, sharper **tool metadata**, and examples — small controlled changes.

**Why other options are wrong:**  
- C: Wiping Chroma does not teach the LLM to call a calculator; it breaks unrelated RAG cases.

---

## Q8 (MSQ, Moderate)

A production agent serves **millions** of chats per day. The SRE team sets up **observability**.

Which signals should they **monitor** with automated alerts?

A. **Latency** — response time drifting above a healthy band (e.g. p95 > 3 seconds)  
B. **Memory usage** — context or leaks pushing the service toward OOM  
C. **Token utilization** — sudden 2× daily token spend without traffic growth  
D. **IDE font size** used by developers

**Correct Answers:** A, B, C

**Answer Explanation:**  
Production observability tracks **time**, **memory**, **failures**, and **cost proxies** like tokens — not manual spot checks per chat.

**Why other options are wrong:**  
- D: Editor settings have no bearing on runtime health.

---

## Q9 (MSQ, Hard)

An engineer raises retrieval **`k`** from **3** to **8** chunks. Answer quality improves on policy questions, but the monthly **OpenAI bill** rises sharply and p95 latency increases.

Which statements about the **cost–latency trade-off** are **correct**?

A. More chunks increase **input tokens** passed to the LLM, which raises cost  
B. Higher `k` can improve context quality but is not free — teams pick a budget and latency target  
C. Token usage is unrelated to prompt size  
D. Doubling `k` and chunk size together without measuring is a common mistake

**Correct Answers:** A, B, D

**Answer Explanation:**  
**Trade-off** means gaining quality by paying **tokens and time**. Professional teams tune one knob, re-measure, and stop when the bar is met.

**Why other options are wrong:**  
- C: Cost is directly tied to tokens consumed (input + output).

---

## Q10 (MSQ, Hard)

After reading **`results.csv`**, your team sees four **wrong-tool** failures and two **over-refusal** failures. Everyone proposes changes the same afternoon: full prompt rewrite, rename all tools, and double chunk size.

Which iteration practices are **sound**?

A. Group failures by **failure class** and apply **one controlled change** per experiment when possible  
B. Re-run the **same evaluation harness** after each patch and compare pass rates  
C. Change prompt, tools, and retrieval simultaneously so the sprint finishes faster  
D. Check **token usage and latency** on a representative workflow — not only pass count

**Correct Answers:** A, B, D

**Answer Explanation:**  
Disciplined iteration uses **targeted patches**, **before/after metrics**, and **resource awareness**. Blanket same-day rewrites cause regressions nobody can explain.

**Why other options are wrong:**  
- C: Simultaneous multi-knob changes violate controlled configuration change practice.
