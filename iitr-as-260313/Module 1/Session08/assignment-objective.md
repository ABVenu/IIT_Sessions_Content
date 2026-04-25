# Assignment — Objective (Agent Behavior & Understanding the LLM Layer)

**Instructions:** Answer all questions. For multiple-select questions (MSQ), select **all** options that apply.

**Scope:** This quiz covers introductory LLM–agent material: what an LLM is; **text in → text out**; the LLM as the reasoning core in the **Think** stage; capabilities; **prompts**; strengths and limitations (**hallucination**, **training cutoff**, math, **inconsistency**, **context window**); major **model providers**; **APIs**; **tokens**; **Transformer** intuition (whole prompt at once); Observe → Think → Act; failure-aware design.

---

## Section A — Multiple Choice, Single Correct (MCQ)

### Q1 (Easy)

A startup is pitching their product as “an AI that reads goals and writes the next step in plain English.” Under the **standard definition** of an LLM used in agentic systems, what is the **simplest accurate description** of its core behaviour?

- A) Image in → labels out  
- B) Text in → text out  
- C) Audio in → transcript out only  
- D) Structured JSON in → database rows out only  

**Answer Explanation (for Assess):**  
**Correct answer: B.** An LLM is fundamentally **text in → text out**; Q&A, code, summaries, etc. are variations of that pattern.  
**A** is wrong: multimodal models exist, but the core LLM pattern emphasized here is **text in → text out**. **C** and **D** describe narrow interfaces, not that general pattern.

---

### Q2 (Easy)

In a typical **Observe → Think → Act** agent architecture, where does the LLM **primarily** operate?

- A) It mainly runs during **Observe**, to collect sensor data  
- B) It mainly runs during **Think**, to plan, reason, or decide the next step  
- C) It mainly runs during **Act**, to physically click buttons in the browser  
- D) It runs equally at every stage with no distinction  

**Answer Explanation (for Assess):**  
**Correct answer: B.** The LLM powers **Think**: the agent sends constructed text (context + instructions) to the model and interprets the reply as the “thinking.”  
**A** is wrong: Observe is about gathering context and tool outputs. **C** is wrong: Act is execution via tools/code; the LLM is not “running” the tool call itself. **D** is wrong: the LLM is invoked at decision points (Think), not continuously in every substage in the same way.

---

### Q3 (Easy)

In standard LLM usage, what is a **prompt**?

- A) The LLM’s internal parameter count  
- B) The output text returned by the API  
- C) The input text you give the LLM to instruct it on the task, tone, and format  
- D) The list of tools the agent is allowed to call  

**Answer Explanation (for Assess):**  
**Correct answer: C.** A prompt is the **input** text that steers what the model should do and how it should respond.  
**A** describes scale (“large”), not prompts. **B** is the **completion/response**, not the prompt. **D** is agent configuration, not the definition of “prompt.”

---

### Q4 (Easy)

Which **company** is widely known for releasing **open-source** **LLaMA** weights that developers can download and run locally?

- A) OpenAI  
- B) Google DeepMind  
- C) Anthropic  
- D) Meta AI  

**Answer Explanation (for Assess):**  
**Correct answer: D.** **Meta** releases **LLaMA** with open weights for local use; the other listed providers are best known for proprietary APIs or cloud products.

---

### Q5 (Moderate)

A user asks a chat-only assistant: “Who won yesterday’s IPL match?” The assistant answers with a confident scoreline. **Without** live data or tools, what is the **most important conceptual issue** with trusting that answer?

- A) LLMs cannot translate languages  
- B) The model may lack **real-time** knowledge after its **training cutoff** and might still sound confident  
- C) LLMs cannot summarize text  
- D) Tokenization prevents any sports questions  

**Answer Explanation (for Assess):**  
**Correct answer: B.** Models have **no guaranteed real-time knowledge** beyond their **training cutoff**; for current events, a **search tool** (or similar) is usually required—otherwise the model may guess or hallucinate.  
**A** and **C** are false: translation and summarization are typical strengths. **D** is wrong: tokenization affects chunks and limits, not whether sports questions are allowed.

---

### Q6 (Moderate)

An agent pastes a 600-page PDF into **one** API call. The combined prompt exceeds the model’s **context window**. Which statement is **most accurate**?

- A) The model silently keeps only the first paragraph  
- B) The model automatically uploads the file to Google Drive  
- C) The input may not be fully processed—context limits mean you often must **chunk** or otherwise split work  
- D) Tokens become free after 1 million characters  

**Answer Explanation (for Assess):**  
**Correct answer: C.** A **context window** is a **maximum token** limit per call; oversized input cannot be fully handled in one go—strategies such as **chunking** are required.  
**A** is not a reliable general rule. **B** and **D** are incorrect.

---

## Section B — Multiple Select, Multiple Correct (MSQ)

*Select all correct options.*

### Q7 (Moderate — MSQ)

Which items are **recognized limitations** of general-purpose LLMs in introductory treatments?

- A) **Hallucination** — plausible-sounding but incorrect “facts”  
- B) **No real-time knowledge** beyond the training cutoff  
- C) **Poor at precise multi-step arithmetic** without tooling  
- D) Guaranteed bitwise-identical answers on every run for the same prompt  

**Answer Explanation (for Assess):**  
**Correct answers: A, B, C.** These are standard limitations (hallucination; cutoff; weak precise arithmetic without tools). **Inconsistency** / randomness also means outputs are **not** guaranteed identical.  
**D** is **incorrect**: outputs can vary between runs (e.g., sampling settings), so bitwise-identical answers are **not** guaranteed.

---

### Q8 (Moderate — MSQ)

A well-structured **prompt for an agent** may include which of the following **elements**?

- A) **Role** (who the model should act as)  
- B) **Context** (facts about the user, order, or tool output)  
- C) **Task** (what decision or output is needed)  
- D) **Format instruction** (length, tone, bullet vs paragraph)  

**Answer Explanation (for Assess):**  
**Correct answers: A, B, C, D.** Role, context, task, and format instructions are standard building blocks for agent prompts.

---

### Q9 (Hard — MSQ)

An **accounting agent** must compute **total revenue across 50 invoices** and **percentage growth vs last year**. The team notices wrong totals when the LLM does the arithmetic in natural language. Which mitigations align with **sound agent design** for this workload?

- A) Route arithmetic through a **code execution** / calculator-style tool and use computed results  
- B) Assume the LLM is always exact at mental math if the prompt says “be careful”  
- C) Treat spreadsheet-scale summation as a task where **tooling**, not raw LLM arithmetic, should dominate  
- D) Increase the model’s context window so invoices no longer exist  

**Answer Explanation (for Assess):**  
**Correct answers: A, C.** LLMs are unreliable for **precise multi-step arithmetic** at scale; **code execution** (or a calculator tool) should produce the numbers the model then explains or formats.  
**B** is wrong: instruction alone does not make the model a reliable calculator. **D** confuses context size with correctness—more tokens do not fix arithmetic reliability.

---

### Q10 (Hard — MSQ)

Which statements about **tokens** and **typical hosted API** cost and limits are **accurate**?

- A) Text is split into **tokens** before the model processes it  
- B) **Context window** is a cap on how many tokens can be handled in one call  
- C) Providers charge based in part on **how many tokens** are processed (input and output)  
- D) Shorter prompts usually mean **faster** responses, all else equal  
- E) On typical hosted APIs, **token usage has no impact on billing** — only the model name matters  

**Answer Explanation (for Assess):**  
**Correct answers: A, B, C, D.** Tokenization; context limits; token-based pricing; and longer prompts tending to slow responses are all standard points.  
**E** is wrong: **billing** on hosted APIs typically depends on **token** usage (input and output), not only the model name.

---

*End of objective assignment.*
