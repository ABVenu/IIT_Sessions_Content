# Subjective Question

### Task: Help ShopEase Fix Their AI Support Assistant

### Scenario

**ShopEase** is an online shopping company. Its support team handles questions about *returns, refunds, shipping, and warranty*.

The company recently tried a ChatGPT-style chatbot for its support team — just a plain LLM, with no extra setup. The chatbot often gave **wrong or made-up answers** about ShopEase's own policies, so the pilot was paused.

You have been asked to write a **short note** explaining *what went wrong* and *how a RAG-based assistant would fix it.*

> This is a writing task, not a coding task. Keep your language simple and clear.


---

**Q1. Why did the plain ChatGPT-style chatbot give wrong answers?**

Explain using:

- any **one** LLM limitation (e.g., *static knowledge* or *lack of domain-specific context*),
- the idea of **hallucination**, and
- **one short example** of a wrong answer it could have given ShopEase (for example, a fake refund timeline).

---

**Q2. What should the new assistant "read from" to give correct answers?**

List **3 to 5 ShopEase documents** the assistant should be grounded on. For each one, write **one line** about the kind of question it helps answer.

*(Example format: "Returns Policy — answers questions about return windows, damaged products, and exchange rules.")*

---

**Q3. Walk through the 4-step RAG flow for one customer question.**

Pick **one** customer question (example: *"Can I return a damaged product I received 5 days ago?"*). Then explain, in plain English, what happens in each of the four RAG steps:

1. **Query** — what the user asks.
2. **Retrieve** — which ShopEase document the system looks into (show a 1–2 line *example chunk* it might bring back).
3. **Context** — how the retrieved chunk is placed along with the question before the LLM answers.
4. **Generate** — the final grounded answer the assistant gives the user.

---

### Submission

Submit **any one** of the following:

- Public **GitHub repository** link containing `solution.md`
- Public **Google Doc** link
- or Directly type the answer in the answer box 

---

## Answer Explanation — Ideal Answers

> Reference answers used for grading. Learner submissions do not need to match exactly but should cover the same ideas in simple language.

### Q1 — Sample Answer

A plain LLM has never read ShopEase's internal documents — this is the problem of **lack of domain-specific context**. On top of that, its knowledge is **static**, so any recent policy change is invisible to it. When asked something it does not actually know, the LLM still answers in a confident tone — this is called **hallucination**. For example, it might tell an agent that ShopEase processes refunds in *3 days*, when the real policy is *7 days*. The answer sounds correct, but it is made up.

### Q2 — Sample Answer

- **Returns & Replacements Policy** — answers questions about return windows, damaged products, and exchange rules.
- **Refund Rules** — answers questions about refund timelines for different payment methods (UPI, card, COD, wallet).
- **Shipping & Delivery Policy** — answers questions about expected delivery times and delay compensation.
- **Warranty Policy** — answers questions about how warranty claims are raised and processed.
- **Payment Rules** — answers questions about COD eligibility and prepaid order rules.

### Q3 — Sample Answer

**Customer question:** *"Can I return a damaged product I received 5 days ago?"*

1. **Query:** The above question is sent to the assistant.
2. **Retrieve:** The system looks into the **Returns Policy** document and brings back a relevant chunk, for example:
   > *"Damaged products reported within 7 days of delivery are eligible for a free replacement. Customer must upload photo proof; pickup is scheduled within 48 hours."*
3. **Context:** That retrieved chunk is placed next to the customer's question in the prompt that goes to the LLM — so the LLM can see *both* the question and the correct policy text.
4. **Generate:** The assistant replies:
   > *"Yes — as per ShopEase's Returns Policy, damaged products reported within 7 days are eligible for a free replacement. Since you are on day 5, please upload photo proof and a pickup will be scheduled within 48 hours."*

This answer is **correct**, **specific to ShopEase**, and **based on a real document** — not on LLM guesswork.

---


