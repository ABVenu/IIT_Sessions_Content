# Assignment — Objective (Session 35: Introduction to LangChain — Concepts, Chains, and Prompt Templates)

**Instructions:** Choose the best answer for MCQs (single correct). For MSQs, **select all that apply** unless stated otherwise. Submit via the LMS objective assessment.

**Difficulty order:** Questions 1–4 (Easy, MCQ) → 5–6 (Moderate, MCQ) → 7–8 (Moderate, MSQ) → 9–10 (Hard, MSQ).

**Note:** After each question, this file lists the **correct option(s)** and **explanation** (for the Assess *Answer explanation* field and instructor use).

---

### Question 1 *(Easy — MCQ)*

Priya is building a **campus food-order** chatbot. Besides calling an LLM, her backend must read the **menu database**, apply **dietary filters**, remember the student’s **last order**, and format a friendly reply. Her tech lead says a framework like **LangChain** is worth adopting because:

- A) LangChain replaces the LLM so she never needs a model API again  
- B) Real LLM products combine model calls with **pre-processing**, **post-processing**, and often **memory**, **retrieval**, and **tools** — not a single prompt in isolation  
- C) Frameworks are only for teams that refuse to use Python  
- D) A one-line `invoke()` demo is always longer in LangChain than in raw SDK code, so frameworks are never useful  

**Correct option:** **B**

**Explanation:** Modern LLM apps need **orchestration** around the model (data prep, tools, memory, formatting). **A** is false — LangChain composes apps; it does not replace the LLM. **C** is irrelevant. **D** ignores that value appears when apps grow beyond a single static prompt.

---

### Question 2 *(Easy — MCQ)*

In the **agentic stack**, where does LangChain most naturally sit when your **React frontend** talks to your **FastAPI backend**?

- A) Inside the user’s browser replacing JavaScript  
- B) As an **orchestration layer** in the backend between your app logic and LLMs, vector DBs, tools, and external APIs  
- C) Only inside the GPU driver, below the operating system  
- D) Exclusively inside the vector database, replacing embeddings  

**Correct option:** **B**

**Explanation:** LangChain coordinates **models, retrievers, tools, and workflows** from the backend — the taught “middle layer.” **A**, **C**, and **D** misplace LangChain in the stack.

---

### Question 3 *(Easy — MCQ)*

Dev replaces a **hard-coded** prompt string in code with a **PromptTemplate** that uses `{topic}` and `{audience}`. Tomorrow marketing wants the same explanation style for **“vector databases”** aimed at **“data engineers.”** What is the main win?

- A) The template deletes the need for an LLM  
- B) He changes **variable values at runtime** without rewriting the whole prompt skeleton in source code  
- C) Placeholders automatically download PDFs from the internet  
- D) `format()` and `invoke()` are illegal in production Python  

**Correct option:** **B**

**Explanation:** **PromptTemplate** separates **structure** from **runtime values** — the core reuse benefit. **A**, **C**, and **D** are incorrect.

---

### Question 4 *(Easy — MCQ)*

Which description best matches a LangChain **Runnable**?

- A) A unit of work you can **invoke** (and later stream or batch) and **compose** with other runnables — like one LEGO brick in a pipeline  
- B) A CSS class that styles chat bubbles in the UI  
- C) A Git branch that stores only `.env` files  
- D) A database index that stores only JPEG images  

**Correct option:** **A**

**Explanation:** **Runnables** are composable, invokable steps (prompt, model, parser, etc.). **B**, **C**, and **D** are unrelated distractors.

---

### Question 5 *(Moderate — MCQ)*

Ankit writes this LCEL chain:

```python
chain = prompt | llm | output_parser
result = chain.invoke({"topic": "REST APIs", "audience": "beginners", "tone": "simple", "limit": "150"})
```

His template ends with `Keep the response within {limit} words` but his dict uses `"word_count": "150"` instead of `"limit"`. What happens?

- A) LangChain silently maps `word_count` to `limit`  
- B) He likely gets a **missing variable** error because **dict keys must match placeholder names exactly**  
- C) The model always returns exactly 150 tokens regardless of keys  
- D) `StrOutputParser` converts missing keys into emojis  

**Correct option:** **B**

**Explanation:** Template variables and `invoke` keys must **match exactly** — a common mistake from class. **A**, **C**, and **D** are false.

---

### Question 6 *(Moderate — MCQ)*

Without **`StrOutputParser`** at the end of `prompt | llm`, what does `print(result)` typically show after `result = chain.invoke({...})` when `llm` is `ChatOpenAI`?

- A) Only a plain string with no metadata  
- B) A **rich response object** (e.g. `.content`, token usage, model metadata) — you must read `.content` yourself for just the answer text  
- C) A compiled SQL query plan  
- D) An empty list because chat models never return content  

**Correct option:** **B**

**Explanation:** Without a parser, the LLM step returns the **full message object**. **`StrOutputParser`** strips that to a **string** for UI use. **A** describes the *with-parser* case. **C** and **D** are wrong.

---

### Question 7 *(Moderate — MSQ)* — Select all that apply

Which statements are **fair reasons** teams adopt LangChain instead of only raw provider SDK calls as apps grow?

- A) **Reusable PromptTemplates** instead of copy-pasting long prompt strings  
- B) **Chains** that pass each step’s output to the next in a declared pipeline  
- C) LangChain guarantees every local 0.5B model beats GPT-4 on medical diagnosis  
- D) **Provider abstraction** — swap model classes with smaller changes when moving vendors  

**Correct options:** **A, B, D**

**Explanation:** **A**, **B**, and **D** match composability, templates, and provider switching from the notes. **C** is false — framework choice does not change model intelligence.

---

### Question 8 *(Moderate — MSQ)* — Select all that apply

The six **core building blocks** overview groups LangChain features. Which pairings are **correct**?

- A) **Memory** — keeps context across conversation turns  
- B) **Indexes** — help organise and retrieve document chunks for RAG-style apps  
- C) **Agents** — always mean a fixed PromptTemplate → LLM chain with no decisions  
- D) **Embedding models** — produce vectors used in semantic search / RAG pipelines  

**Correct options:** **A, B, D**

**Explanation:** **A**, **B**, and **D** align with the six-component overview. **C** is false — **agents** **decide actions/tools**; a fixed template→LLM pipeline is a **chain**, not an agent.

---

### Question 9 *(Hard — MSQ)* — Select all that apply

You are setting up the **first LCEL chain** on a new laptop (`ChatOpenAI`, `PromptTemplate`, `StrOutputParser`). Which statements are **correct**?

- A) Installing only `langchain` and skipping `langchain-openai` can cause **import errors** for `ChatOpenAI`  
- B) `from langchain_core.prompts import PromptTemplate` is the correct import family (not a typo like `langchain.core.compts`)  
- C) With `StrOutputParser` last, `chain.invoke({...})` can return a **plain string** ready to print in the UI  
- D) `export OPENAI_API_KEY` is irrelevant when using OpenAI through `langchain-openai`  

**Correct options:** **A, B, C**

**Explanation:** **A–C** match setup and parser behaviour from class. **D** is false — the OpenAI key is still required for cloud calls.

---

### Question 10 *(Hard — MSQ)* — Select all that apply

A video platform uploads a lecture recording. **Copyright scan**, **caption generation**, and **720p transcoding** can run at the same time because they do not need each other’s output first. Which LangChain **overview** ideas fit this situation?

- A) That pattern is an example of **parallel** work when steps are **independent**  
- B) A **sequential chain** always runs B, C, and D in parallel with no ordering  
- C) An **agent** may later **choose tools** (e.g. weather API vs calculator) based on the user question — different from today’s fixed `prompt | llm` chain  
- D) **LCEL** uses the pipe operator `|` so runnables compose without manually wiring “step 1 then step 2” in separate functions for that chain  

**Correct options:** **A, C, D**

**Explanation:** **A** matches the parallel-upload analogy. **C** contrasts **agents** (dynamic tool choice) with fixed chains. **D** states LCEL composition. **B** is false — **sequential** chains pass output **in order**, not arbitrary parallel execution of dependent steps.

---

**End of objective assignment.**
