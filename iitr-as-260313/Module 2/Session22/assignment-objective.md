# Objective Assignment: Evaluating and Improving RAG Systems

## Instructions

- Questions 1 to 6 are **MCQs**. Choose **one correct option**.
- Questions 7 to 10 are **MSQs**. Choose **all correct options**.
- The questions are ordered from Easy to Moderate to Hard.

---

## Question 1

**Type:** MCQ  
**Difficulty:** Easy

A ShopKart customer asks about **returning an opened laptop charger**. The bot’s **Rank 1** chunk is from **shipping_policy.txt** and mentions delivery timelines—not return eligibility. The final answer talks about express delivery. What **failure mode** best describes this?

A. Retrieval problem  
B. Generation problem  
C. Hallucination  
D. API rate-limit problem

**Correct Answer:** A

**Answer Explanation:**  
A is correct because the wrong policy area and wrong chunk were retrieved before generation ran.

B is incorrect because generation misreads **good** evidence—the evidence here was the wrong chunk. C is incorrect because the main issue is surfacing the wrong policy, not inventing facts absent from retrieved text (though the answer may also be wrong). D is incorrect because rate limits affect whether answers generate, not which chunk ranks first.

---

## Question 2

**Type:** MCQ  
**Difficulty:** Easy

Priya is debugging a wrong ShopKart reply. Her team lead says: *“Do not touch the prompt until you have read what evidence the bot actually saw.”* What should Priya inspect **first** in the terminal?

A. The Groq model name in `.env`  
B. **Rank 1** retrieved chunk—category, source, and text  
C. The Python version installed on her laptop  
D. The number of lines in `rag_pipeline.py`

**Correct Answer:** B

**Answer Explanation:**  
B is correct because Rank 1 shows what retrieval surfaced—the first step in separating retrieval failure from generation failure.

A is incorrect because the model name does not show which policy excerpt was used. C and D are unrelated to diagnosing a specific wrong answer.

---

## Question 3

**Type:** MCQ  
**Difficulty:** Easy

A customer asks: *“Is UPI refund available for prepaid orders?”* Retrieved excerpts mention **COD refunds to UPI/bank only**—there is **no prepaid UPI rule**. The bot replies with a detailed **prepaid UPI refund workflow** not found in any excerpt. What failure mode is this?

A. Retrieval problem  
B. Generation problem only  
C. Hallucination  
D. Chunk overlap misconfiguration

**Correct Answer:** C

**Answer Explanation:**  
C is correct because the answer adds authoritative-sounding facts not supported by retrieved policy text.

A is incorrect if excerpts were at least partially relevant—the issue is invented prepaid steps. B alone is too narrow when the model fabricates policy that never appeared in context. D is incorrect because overlap settings do not explain invented payment workflows.

---

## Question 4

**Type:** MCQ  
**Difficulty:** Easy

A junior engineer wants to fix a bad RAG answer by immediately raising **top-k**, rewriting the **system prompt**, and adding a **metadata filter**—all in one commit. What is the **best first step** before changing anything?

A. Diagnose whether retrieval, generation, or hallucination caused the failure  
B. Delete the Chroma collection and rebuild from scratch  
C. Switch to a larger paid LLM  
D. Add ten more policy PDFs to the folder

**Correct Answer:** A

**Answer Explanation:**  
A is correct because each failure mode maps to a different lever—changing everything at once hides what actually helped.

B might be needed after chunk changes but is not the first diagnostic step. C and D do not identify which pipeline stage failed.

---

## Question 5

**Type:** MCQ  
**Difficulty:** Moderate

For the query *“Can I return a laptop charger if the box is opened?”*, **Rank 1** shows **returns** category but only the **unopened 7-day** sentence. The **opened-item rule** exists in **Rank 3**. The answer ignores opened-box eligibility. What is the **best first fix** to try?

A. Rewrite the grounding prompt only—retrieval already found returns  
B. Raise **top-k** (e.g. from 3 to 5) or improve chunk boundaries so the opened rule surfaces earlier  
C. Change the refusal sentence to be more polite  
D. Lower LLM temperature and hope Rank 3 is read automatically

**Correct Answer:** B

**Answer Explanation:**  
B is correct because the right policy area was found but the **incomplete chunk set** is a retrieval tuning problem—more ranks or better chunking can surface the opened rule.

A is incorrect because the generator never received the opened rule in the top context. C does not add missing evidence. D is incorrect—the LLM only sees the chunks you pass in; temperature does not fetch Rank 3 by itself.

---

## Question 6

**Type:** MCQ  
**Difficulty:** Moderate

Your `guess_category()` function returns **`None`** for the query *“Do you offer gift wrapping on bulk corporate orders?”* because no keyword matches. In the **improved run** with `use_filter=True`, what should `retrieve_filtered(...)` do?

A. Return zero chunks and skip generation  
B. Search the **full index** without a `where` category filter  
C. Force category `"returns"` as a default  
D. Raise a Python exception and stop the script

**Correct Answer:** B

**Answer Explanation:**  
B is correct because `None` means no category filter—the search should fall back to the entire Chroma collection.

A is incorrect because no match should not block retrieval. C invents a category with no keyword basis. D is incorrect—the lab design uses graceful fallback, not a crash.

---

## Question 7

**Type:** MSQ  
**Difficulty:** Moderate

Which situations are best classified as **retrieval problems**? Select **all** that apply.

A. A warranty question retrieves **shipping** chunks in Rank 1  
B. Rank 1 is **returns** but text only shows the unopened rule while the opened rule is in Rank 4  
C. Rank 1 excerpts clearly state **5–7 business days**, but the answer says **instant refund**  
D. The wrong **refunds** chunk is retrieved even though a better refunds paragraph exists in the index

**Correct Answers:** A, B, D

**Answer Explanation:**  
A, B, and D are correct because wrong category, incomplete top ranks, or wrong chunk selection are retrieval-stage failures.

C is incorrect because good excerpts were retrieved but the final answer misread them—that is generation (or hallucination if facts were invented), not retrieval.

---

## Question 8

**Type:** MSQ  
**Difficulty:** Moderate

ShopKart runs a **baseline** pass and an **improved** pass on the same `TEST_QUERIES`. Which settings belong to the **improved** pass? Select **all** that apply.

A. `top_k=5`  
B. `use_filter=True` with `guess_category()`  
C. `generate_strict_answer()` with explicit **do not invent** rules  
D. `top_k=3`, `use_filter=False`, and `generate_grounded_answer()` only

**Correct Answers:** A, B, C

**Answer Explanation:**  
A, B, and C are correct—they are the three levers applied together in the improved run: higher top-k, metadata filter, and stricter grounding prompt.

D is incorrect because it describes the **baseline** configuration, not the improved pass.

---

## Question 9

**Type:** MSQ  
**Difficulty:** Hard

A QA engineer pairs each symptom with a **recommended first lever**. Which pairings are **sound**? Select **all** that apply.

A. Answer invents **coupon codes** not in excerpts → tighten **grounding prompt** with refusal rules  
B. Rank 1 has the right category but misses the second half of a split rule → raise **top-k** or tune **chunk overlap**  
C. Returns questions keep pulling **shipping** paragraphs → add **metadata filter** by category  
D. Rank 1 is **warranty** but answer adds facts not in excerpts → increase **chunk size** only (no prompt change)

**Correct Answers:** A, B, C

**Answer Explanation:**  
A is correct— invented offers are generation/hallucination issues; stricter prompts help. B is correct—incomplete retrieval suggests top-k or chunking fixes. C is correct—wrong policy type surfacing is a precision/filter problem.

D is incorrect because facts not in excerpts when Rank 1 category is already right points to **generation/hallucination**—a stricter prompt should be tried before or alongside chunk tuning, not chunk size alone with no prompt change.

---

## Question 10

**Type:** MSQ  
**Difficulty:** Hard

Your team uses `guess_category()` plus Chroma `where={"category": ...}` filtering. Which statements are **true**? Select **all** that apply.

A. The filter restricts similarity search to chunks whose metadata matches the guessed category  
B. A question needing both **refunds** and **shipping** evidence may get incomplete answers when only one category is searched  
C. When `guess_category()` returns `None`, retrieval can still run across the **full** index  
D. Keyword routing guarantees the correct category for every possible customer phrasing

**Correct Answers:** A, B, C

**Answer Explanation:**  
A is correct—that is how Chroma metadata filtering works in the lab. B is correct—the single-category limitation was demonstrated when multi-policy answers need merged retrieval. C is correct—`None` triggers full-index fallback.

D is incorrect because `guess_category()` is a simple hit-and-trial keyword router, not a guarantee for all phrasing.
