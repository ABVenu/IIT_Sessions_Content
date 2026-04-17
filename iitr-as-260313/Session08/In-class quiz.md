# In-Class Quiz — Session 08: Agent Behavior & Understanding the LLM Layer

---

**Q1.** What is the core behavior of a Large Language Model (LLM)?

- A) It searches the internet and retrieves real-time information
- B) It receives text as input and produces text as output
- C) It executes code and returns computed results
- D) It stores facts in a database and looks them up when queried

**Answer:** B

**Explanation:** The fundamental behavior of an LLM is "Text In → Text Out." Everything the LLM does — answering questions, summarizing, translating, writing code — is a variation of this single pattern.

---

**Q2.** In the Observe → Think → Act agent loop, where does the LLM play its primary role?

- A) Observe — it gathers context from the environment
- B) Act — it executes tool calls and API requests
- C) Think — it processes context and decides the next step
- D) Both Observe and Act equally

**Answer:** C

**Explanation:** The LLM powers the **Think** stage. The agent sends a carefully constructed prompt to the LLM, the LLM reasons and returns a decision, and then the agent's Python code carries out the action in the Act stage.

---

**Q3.** Which of the following best describes "hallucination" in the context of LLMs?

- A) The model refuses to answer questions it is uncertain about
- B) The model generates factually incorrect information while sounding confident and accurate
- C) The model produces output in a language different from the input
- D) The model repeats the same sentence multiple times in its response

**Answer:** B

**Explanation:** Hallucination is when an LLM generates plausible-sounding but factually wrong information — such as inventing book titles, court cases, or statistics — and presents them with full confidence. This is one of the most critical limitations to understand when designing agentic systems.

---

**Q4.** What is a "token" in the context of LLMs, and why does it matter?

- A) A security key used to authenticate API requests to the LLM provider
- B) A small chunk of text (roughly 0.75 words) that is the LLM's basic unit of processing; it affects cost, speed, and context limits
- C) A single complete sentence that the model processes at one time
- D) A tag added to a prompt to tell the model which task to perform

**Answer:** B

**Explanation:** Tokens are the bite-size pieces LLMs break text into before processing. They matter because (1) every LLM has a context window limit measured in tokens, (2) API providers charge based on token count, and (3) more tokens mean slower responses.

---

**Q5.** Which of the following statements about the Transformer architecture and the attention mechanism is correct?

- A) Transformers read text one word at a time in strict sequence, just like older RNN models
- B) The attention mechanism allows the model to focus on only the first and last word of a sentence
- C) Attention allows every word in the input to consider every other word simultaneously, enabling the model to understand context and long-range relationships
- D) Transformers were invented by Meta AI as part of the LLaMA project in 2023

**Answer:** C

**Explanation:** The attention mechanism is the key innovation of the Transformer architecture (introduced in Google's 2017 paper "Attention Is All You Need"). Unlike older models that read sequentially, Transformers process the entire input at once, letting every word "look at" every other word — which is why LLMs understand context, tone, and meaning so well.

---
