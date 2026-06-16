# Assignment Objective

Total Questions: 10

Difficulty Flow: Easy → Moderate → Hard

Question Types:
- 6 MCQ (Single Correct): Q1–Q6
- 4 MSQ (Multiple Correct): Q7–Q10

---

## Q1 (MCQ, Easy)

A fintech startup tests its **loan FAQ chatbot** by checking only whether the final sentence *sounds polite*. Users report wrong answers: the bot cites the **EMI policy** when asked about **KYC documents**, but the sentence still reads well.

What is the **main gap** in this testing approach?

A. The bot should never use complete sentences in production  
B. Agent evaluation must also check **trajectory** — tools called, documents retrieved, and refusals — not only final text  
C. Polite answers automatically prove the correct policy document was used  
D. JSON test files are illegal for chatbot QA

**Correct Answer:** B

**Answer Explanation:**  
Agents take **multi-step paths** (tool calls, retrieval, refusal). A fluent final answer can hide wrong tools or wrong documents. Evaluation must inspect **behaviour**, not polish alone.

**Why other options are wrong:**  
- A: Answer format is unrelated to evaluation depth.  
- C: Politeness does not prove grounding or correct tool use.  
- D: Structured JSON cases are a standard regression pattern.

---

## Q2 (MCQ, Easy)

A QA engineer adds this row to `evaluation_cases.json` for a course helpdesk agent:

```json
"expected": {
  "must_use_tools": ["search_course_policy"],
  "forbidden_tools": [],
  "must_cite_doc_ids": ["refund_policy"],
  "must_contain": ["7 days"],
  "should_refuse": false
}
```

What does **`must_use_tools`** enforce?

A. The agent must **call** `search_course_policy` for this case to pass the tool check  
B. The agent must **never** call any tool  
C. The agent must delete the JSON file after answering  
D. The agent must return exactly seven words in every answer

**Correct Answer:** A

**Answer Explanation:**  
`must_use_tools` lists tools the agent **cannot skip** for that scenario. The runner compares this list against **tool traffic** captured in the trace.

**Why other options are wrong:**  
- B: That describes a refusal / forbidden-tool scenario, not `must_use_tools`.  
- C: File handling is unrelated to tool expectations.  
- D: `must_contain` checks keywords, not word count.

---

## Q3 (MCQ, Easy)

After running an evaluation suite, your team opens **`results.csv`** and sorts by the **`score`** column ascending.

What is the **primary purpose** of this file in the harness?

A. Store vector embeddings for Chroma  
B. Provide a **sortable mark sheet** — one row per case with status, score, failure type, and summary fields  
C. Replace `evaluation_cases.json` as the source of test inputs  
D. Train the LLM on historical chat logs

**Correct Answer:** B

**Answer Explanation:**  
`results.csv` is the **aggregated outcomes table** produced by the runner so teams can compare runs, rank weak cases, and share results in spreadsheet tools.

**Why other options are wrong:**  
- A: Embeddings live in a vector store, not the CSV.  
- C: Inputs still come from `evaluation_cases.json`.  
- D: CSV holds evaluation outcomes, not training data.

---

## Q4 (MCQ, Easy)

For the case *"Give me my instructor's personal phone number"*, the expected block includes:

```json
"forbidden_tools": ["search_course_policy", "calculate_refund_amount"],
"should_refuse": true
```

Why list tools under **`forbidden_tools`**?

A. To force the agent to call every listed tool twice  
B. To fail the case if the agent **calls** any tool that should stay idle for this out-of-scope / private-data query  
C. To store API keys for each tool  
D. To increase the LLM temperature automatically

**Correct Answer:** B

**Answer Explanation:**  
Private or out-of-scope queries should often **refuse without searching policies or calculators**. `forbidden_tools` flags tool calls that violate that expectation.

**Why other options are wrong:**  
- A: Forbidden means **do not call**, not call twice.  
- C: Keys belong in environment config, not eval JSON.  
- D: Temperature is unrelated to forbidden-tool checks.

---

## Q5 (MCQ, Moderate)

Your runner uses this rubric:

```
score = max(0, 1 − 0.25 × number_of_failures)
```

A case fails **two** independent checks (e.g. `missing_tool` and `missing_content`). What score is recorded?

A. 1.00  
B. 0.75  
C. 0.50  
D. 0.25

**Correct Answer:** C

**Answer Explanation:**  
Two failures → `1 − 0.25 × 2 = 0.50`. The formula deducts **0.25 per failure** until floored at 0.

**Why other options are wrong:**  
- A: Zero failures are needed for 1.00.  
- B: 0.75 corresponds to **one** failure.  
- D: 0.25 would require three failures before flooring (`1 − 0.75 = 0.25`).

---

## Q6 (MCQ, Moderate)

An engineer runs **100** evaluation cases in one script. Without isolation, tool-call logs from case 12 appear inside case 13's debug file.

Which technique from the evaluation lab **prevents trace mixing**?

A. Using `print()` instead of logging  
B. Resetting a per-case trace with Python **`contextvars`** (e.g. `_current_trace.set([])` at the start of each case)  
C. Deleting `evaluation_cases.json` after each case  
D. Setting LLM `temperature=0` only on case 1

**Correct Answer:** B

**Answer Explanation:**  
**`contextvars`** gives each test case its **own trace context** so events from different runs do not merge into one timeline.

**Why other options are wrong:**  
- A: `print()` does not isolate structured per-case traces.  
- C: The case file must persist for the full suite.  
- D: Temperature does not control trace boundaries.

---

## Q7 (MSQ, Moderate)

A **course support evaluation runner** (`agent_app_evaluation_runner.py`) is wired correctly. Which steps does it perform **for each case**?

A. Load the case from `evaluation_cases.json`  
B. Invoke the agent through `run_agent_case` and capture **trace + final response**  
C. Compare **expected** vs **actual** in `evaluate_case` and compute a score  
D. Fine-tune embedding weights inside the CSV writer

**Correct Answers:** A, B, C

**Answer Explanation:**  
The harness loop is: **load cases → run with tracing → score → write outputs** (`results.csv` and per-case trace JSON).

**Why other options are wrong:**  
- D: The runner scores behaviour; it does not fine-tune embeddings during CSV export.

---

## Q8 (MSQ, Moderate)

A failing row in `results.csv` shows:

`failure_type = weak_grounding` and `failures` contains `missing_citation: placement_policy`.

Which debugging actions are **appropriate**?

A. Open `traces/<case_id>.json` and inspect **retrieval** / `retrieved_doc_ids` events  
B. Check whether `must_cite_doc_ids` in the case expected the **placement_policy** document  
C. Assume the LLM tokenizer is broken and reinstall Python  
D. Verify the agent's policy search tool logged the document IDs the scorer reads

**Correct Answers:** A, B, D

**Answer Explanation:**  
**Weak grounding** means the agent did not retrieve or cite the expected document. Traces show what was actually retrieved; expected JSON shows what should have happened; tools must log retrieval IDs into the trace.

**Why other options are wrong:**  
- C: Tokenizer reinstall is unrelated to citation / retrieval mismatch.

---

## Q9 (MSQ, Hard)

The team adds a **`get_ticket_status`** tool next sprint. Which harness changes follow the **extensibility** pattern taught in the evaluation lab?

A. Register the new tool in the agent module  
B. Add new rows to `evaluation_cases.json` with `must_use_tools` / `forbidden_tools` as needed  
C. Delete all existing cases and rewrite the runner from scratch  
D. Keep the same runner flow: load JSON → invoke → trace → compare → `results.csv`

**Correct Answers:** A, B, D

**Answer Explanation:**  
Extensibility means **extend cases and tools** while preserving the **same evaluation philosophy** and runner pipeline.

**Why other options are wrong:**  
- C: Throwing away cases and rewriting the runner violates the institutionalized harness approach.

---

## Q10 (MSQ, Hard)

After a full suite run, the console prints:

```
Total cases: 6 | Passed: 4 | Failed: 2
Lowest-performing cases:
- placement_guarantee: score=0.75, failure_type=weak_answer
- private_phone_refusal: score=0.50, failure_type=refusal_mismatch
```

Which follow-up plans are **sound**?

A. Fix **`placement_guarantee` first** if it is the higher business priority, even though its score (0.75) is higher than the refusal case (0.50)  
B. Open `traces/private_phone_refusal.json` to see whether the agent called a forbidden tool or failed to refuse  
C. Ignore `results.csv` because partial scores never matter in AI systems  
D. Re-run the **same runner command** after prompt changes and diff the new `results.csv` against the old file

**Correct Answers:** A, B, D

**Answer Explanation:**  
Lowest-score sorting is a **default triage** hint, but teams may prioritize by risk. **Failure traces** explain refusal/tool mistakes. Re-running the harness proves whether fixes worked.

**Why other options are wrong:**  
- C: Partial scores and qualitative labels are explicitly used to rank and compare regression runs.
