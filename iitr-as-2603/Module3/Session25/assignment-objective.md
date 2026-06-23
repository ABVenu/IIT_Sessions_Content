# Assignment Objective

Total Questions: 10

Difficulty Flow: Easy → Moderate → Hard

Question Types:
- 6 MCQ (Single Correct): Q1–Q6
- 4 MSQ (Multiple Correct): Q7–Q10

---

## Q1 (MCQ, Easy)

**QuickKart** noticed its LLM API bill jumped after engineers started pasting full product catalogues into every customer chat. The finance team asks what metric the provider actually multiplies by its per-million rate.

What do LLM providers primarily bill for?

A. Total word count in the user message only  
B. Number of API calls at a flat fee per request, ignoring message size  
C. **Input tokens** (everything sent) and **output tokens** (everything generated), usually priced separately  
D. Character count excluding spaces and punctuation  

**Correct Answer:** C

**Answer Explanation:**  
API pricing is **token-based**. **Input tokens** cover system prompt, examples, history, documents, and the user message. **Output tokens** cover the model's reply — and are often priced **higher** than input.

**Why other options are wrong:**  
- A: Billing includes all input layers, not only the latest user message; output is billed too.  
- B: Cost scales with tokens processed, not a flat per-call fee.  
- D: Providers use tokenisers, not raw character counts.

---

## Q2 (MCQ, Easy)

While auditing a prompt, **Dev** tokenises the English word **"unbelievable"** and sees **three** subword tokens instead of one.

What is the most important **product design** lesson from this?

A. English word count always equals token count  
B. **One word can become multiple tokens**, so cost, latency, and context usage can exceed word-based estimates  
C. Subword tokenisation applies only to JSON payloads  
D. Every token is always exactly four characters long  

**Correct Answer:** B

**Answer Explanation:**  
Tokenisers split text into reusable **subword pieces**. Designers who plan budgets by **word count** often **underestimate** bills and context consumption — especially for long rare words, code, and symbols.

**Why other options are wrong:**  
- A: Directly contradicted by the example.  
- C: Subword splitting applies broadly, not only to JSON.  
- D: Token length varies; there is no fixed four-character rule.

---

## Q3 (MCQ, Easy)

A hostel helpdesk bot sends **system rules + few-shot examples + 35 prior chat turns + today's question** in a single Groq API call. The model then writes its reply.

What hard limit must **input + output together** stay within?

A. The model's original training dataset size  
B. The **`max_tokens`** parameter alone  
C. The model's **context window** for one request  
D. The length of the Groq **request ID** string  

**Correct Answer:** C

**Answer Explanation:**  
The **context window** is the maximum tokens an LLM can process in **one request** — full input **plus** generated output. Everything in the prompt stack and the reply shares that single budget.

**Why other options are wrong:**  
- A: Training data size is unrelated to per-call limits.  
- B: `max_tokens` caps **output length** only; it does not define the full window.  
- D: Request IDs are trace labels, not size limits.

---

## Q4 (MCQ, Easy)

**CampusPay** must enforce: *"Never quote live stock prices — only explain UPI refund policy."* The bot will run for long support threads.

Where should this rule live so it is least likely to disappear as chat history grows?

A. Only in the **first user message** on turn 1  
B. In the **system prompt**, resent on every API call  
C. In a previous **assistant** reply the user liked  
D. Only in the Groq dashboard notes field  

**Correct Answer:** B

**Answer Explanation:**  
**Stable rules** belong in the **system** slot — they are pinned each call. Rules buried in early **user** turns are among the first content dropped when **history overflows**.

**Why other options are wrong:**  
- A: Turn-1 user text is not pinned; it can truncate.  
- C: Past assistant messages are not authoritative configuration.  
- D: Dashboard notes are not sent to the model.

---

## Q5 (MCQ, Moderate)

A team uses a model with an **8,192-token** context window. They reserve **800 tokens** for the reply and **200** as a safety buffer.

Their input stack per call:

- System prompt: **350 tokens**  
- Few-shot examples: **280 tokens**  
- FAQ chunk: **600 tokens**  
- Chat history: **6,200 tokens**  

What is the correct conclusion?

A. The stack fits comfortably with more than 1,500 tokens to spare  
B. **Usable input is exceeded** — overflow/truncation is likely; history or other layers must be trimmed  
C. Only **output** tokens will be truncated; input always fits  
D. The API will always show a red error banner before answering  

**Correct Answer:** B

**Answer Explanation:**  
Usable input budget = 8,192 − 800 − 200 = **7,192 tokens**.  
Stack total = 350 + 280 + 600 + 6,200 = **7,430 tokens** → **238 tokens over** usable input. Expect **silent truncation** or quality collapse — not a guaranteed UI error.

**Why other options are wrong:**  
- A: Arithmetic shows overflow, not spare capacity.  
- C: Input can exceed the window; truncation often drops **early/middle** input.  
- D: Overflow is often **silent** — a common product pitfall.

---

## Q6 (MCQ, Moderate)

**Riya** compares two JSON extraction prompts. She runs each **once** at **temperature 0.9** and picks the winner because one JSON "looked nicer."

What is the main flaw in her test method?

A. JSON tasks should use **low temperature** (near 0) and **multiple runs** to compare **structure**, not luck  
B. `max_tokens` must be set to 0 for JSON tasks  
C. Temperature 0.9 guarantees identical outputs every run  
D. Groq cannot return structured text at any temperature setting  

**Correct Answer:** A

**Answer Explanation:**  
High temperature adds **sampling randomness**. A single run at 0.9 may reflect **luck**, not better prompt design. For JSON keys and field names, lock **temperature ≈ 0** and rerun to verify **consistency**.

**Why other options are wrong:**  
- B: `max_tokens=0` would block output entirely.  
- C: High temperature increases variation, not consistency.  
- D: Models can return JSON-like text; the issue is testing methodology.

---

## Q7 (MSQ, Moderate)

**FoodLoop** is optimising a Groq-powered canteen bot. Which changes typically increase **both** API **billing** and user-perceived **latency** for the same task?

A. Pasting a **12,000-token** hygiene policy into every request  
B. Adding a long **chain-of-thought** workflow to the system prompt  
C. Setting **`max_tokens=20`** on a one-word classification reply  
D. Sending the **full 25-turn** chat history on every call  
E. Reducing temperature from **0.7** to **0.0** for routing labels  

**Correct Answers:** A, B, D

**Answer Explanation:**  
**Larger input** (policies, CoT steps, full history) costs more **input tokens** and takes longer to **process** before the first output token — raising bill and latency.

**Why other options are wrong:**  
- C: A low `max_tokens` cap **reduces** output cost and length.  
- E: Lower temperature mainly improves **consistency**; it does not materially increase input size.

---

## Q8 (MSQ, Moderate)

After **40 minutes**, a campus FAQ bot starts quoting **wrong fee amounts** and ignores *"answer only from the FAQ text"* even though developers swear the rule is still in the codebase. Users see no error banner.

Which explanations and fixes are **plausible**?

A. **Context overflow** dropped early FAQ or instruction text — trim history or **re-send/re-retrieve** grounding each turn  
B. The scope rule lived only in **turn 2's user message** — move critical rules to the **system prompt**  
C. **Temperature 0 alone** always fixes truncation with no other changes  
D. **Silent truncation** — the model cannot read what fell outside the window  
E. The model became "tired" after 40 minutes like a human support agent  

**Correct Answers:** A, B, D

**Answer Explanation:**  
Long threads overflow the **context window**. Content drops **silently**; **grounding** and **scope rules** vanish from what the model actually reads. Pin rules in **system** and manage **history**.

**Why other options are wrong:**  
- C: Temperature controls randomness, not window size.  
- E: This is a **context budget** failure, not model fatigue.

---

## Q9 (MSQ, Hard)

Match each **real task** to the **best default design choice**:

| Task | Best default choice |
|---|---|
| 1. Classify UPI tickets as Billing / Technical / Other (**one word**) | ? |
| 2. Brainstorm varied ad taglines for a new masala chai brand | ? |
| 3. Verify whether a prompt edit changed **JSON field names** | ? |
| 4. Ask questions about **year 1** messages in a **multi-year WhatsApp export** uploaded to a 1M-context chat UI | ? |

Which **task → choice** pairings are **correct**?

A. Task 1 → **`temperature ≈ 0`** with a tight **`max_tokens`** cap  
B. Task 2 → **Higher temperature** (e.g. 0.8–1.0) to encourage wording variation  
C. Task 3 → **Lock temperature near 0** and compare **structure** across multiple identical runs  
D. Task 4 → Assume the **entire export is always visible** with **no truncation and no extra cost**  
E. Task 1 → **`temperature = 1.5`** for maximum creative routing labels  

**Correct Answers:** A, B, C

**Answer Explanation:**  
**Routing/JSON** needs **low temperature** and short output caps. **Creative copy** needs higher temperature. **Prompt A/B tests** need controlled randomness. **Huge chat exports** can still **truncate** and always consume tokens — early messages may be invisible.

**Why other options are wrong:**  
- D: Large attachments can exceed even long windows; billing and truncation still apply.  
- E: High temperature harms stable one-word classification.

---

## Q10 (MSQ, Hard)

**Arjun** is launching a Groq-powered library assistant. Which practices reflect **sound LLM internals** design before go-live?

A. **Audit token layers** (system, examples, history, docs) with `tiktoken` or the provider dashboard  
B. Use Groq **Activity logs** and **request IDs** to trace latency or token spikes  
C. Add **fifteen few-shot examples** to every call to be extra safe  
D. Set **`max_tokens`** on replies to limit output cost and rambling  
E. **Reserve token space** for the assistant reply instead of filling 100% of the window with input  
F. Ignore **input token** counts because providers bill **only** completion tokens  

**Correct Answers:** A, B, D, E

**Answer Explanation:**  
Designers **measure** layers, **monitor** production calls, **cap** outputs, and **reserve** reply space. Few-shot examples are paid **every call** — two strong examples usually beat fifteen.

**Why other options are wrong:**  
- C: Excessive few-shot blocks steal **context** and raise **cost**.  
- F: **Input tokens** are billed separately and drive **latency**.
