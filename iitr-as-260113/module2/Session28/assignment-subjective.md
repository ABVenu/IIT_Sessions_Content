# Subjective Question

### Task: Help ShopEase Fix Their AI Support Assistant

### Scenario

**ShopEase** is an online shopping company. Its support team handles questions about *returns, refunds, shipping, and warranty*.

The company recently tried a ChatGPT-style chatbot for its support team — just a plain LLM, with no extra setup. The chatbot often gave **wrong or made-up answers** about ShopEase's own policies, so the pilot was paused.

You have been asked to write a **short note** explaining *what went wrong* and *how a RAG-based assistant would fix it.*

> This is a writing task, not a coding task. Keep your language simple, specific, and clear. Use **real-looking ShopEase documents and realistic customer questions** in your answers — vague, generic answers will not score well.

---

**Q1. Why did the plain ChatGPT-style chatbot give wrong answers?** *(target length: ~100–150 words)*

Be **specific**. Do not just define limitations in general — explain *exactly* why a plain LLM fails for a ShopEase use case. Your answer must clearly cover all three of the following:

- **The root cause** — e.g., the LLM has no access to ShopEase's internal policy documents (*lack of domain-specific context*), and anything updated recently is beyond its training cutoff (*static knowledge*).
- **What hallucination means** — and why it happens when the LLM has no real information to rely on.
- **One realistic wrong-answer example at ShopEase** — use a real-looking number or policy line, e.g. *"the chatbot told a customer that refunds take 3 days, when ShopEase's actual refund timeline is 7 working days."* Make the example concrete, not generic.

---

**Q2. What should the new assistant "read from" to give correct answers?**

List **3 to 5 real-sounding ShopEase documents** the assistant should be grounded on. For each, write **one line** describing the kind of question it helps answer.

*(Example format: "Returns & Replacements Policy — answers questions about return windows, damaged products, and exchange rules.")*

---

**Q3. Walk through the 4-step RAG flow for one realistic ShopEase customer question.** *(target length: ~150–200 words)*

Pick **one realistic** customer question (example: *"I received a damaged mixer-grinder 5 days ago. Can I still get a replacement?"*). Then explain each of the four RAG steps **in proper detail** — not in one line each. Your answer must clearly show:

1. **Query** — the exact customer question that reaches the assistant.
2. **Retrieve** — *which* ShopEase document is looked into, and *what is actually retrieved* (include a realistic 2–3 line example chunk from that document, e.g. a real-sounding rule from the Returns Policy).
3. **Context** — *how* the retrieved chunk is used — i.e., it is placed alongside the customer's question in the prompt given to the LLM, so the LLM now has both the question and the correct policy text in front of it.
4. **Generate** — *how the retrieved context helps produce the final answer*, and the final grounded answer the assistant gives the customer. Make it clear that the answer is built *from the retrieved chunk*, not from the LLM's guesswork.

---

### Submission

Submit **any one** of the following:

- Public **GitHub repository** link containing `solution.md`
- Public **Google Doc** link
- or directly type the answer in the answer box

---

## Answer Explanation — Ideal Answers

> Reference answers used for grading. Learner submissions do not need to match exactly but should cover the same ideas in simple language with the same level of specificity.

### Q1 — Sample Answer (~130 words)

A plain LLM fails for ShopEase because it has **never read ShopEase's internal policies** — things like the Returns Policy, Refund Rules, or Shipping SLA are private company documents, and the LLM has no access to them. This is the problem of **lack of domain-specific context**. On top of that, its knowledge is **static** — anything ShopEase updated recently (for example, a new 48-hour pickup rule) is beyond the model's training cutoff.

When the chatbot is asked about *"our refund timeline"*, it does not actually know the answer, so it invents a fluent, confident one. This is called **hallucination**. For example, the chatbot could tell a customer that ShopEase processes refunds in *3 business days*, when the real ShopEase policy is *7 working days*. The answer *sounds* correct, but it is completely made up — and an agent repeating this creates a false promise ShopEase cannot keep.

### Q2 — Sample Answer

- **Returns & Replacements Policy** — answers questions about return windows, damaged products, and exchange rules.
- **Refund Rules & Timelines** — answers questions about refund timelines for different payment methods (UPI, card, COD, wallet).
- **Shipping & Delivery Policy** — answers questions about expected delivery windows by region and delay-compensation rules.
- **Warranty & After-Sales Policy** — answers questions about how warranty claims are raised and processed.
- **Payment & COD Rules** — answers questions about COD eligibility, prepaid discounts, and failed-payment handling.

### Q3 — Sample Answer (~180 words)

**Customer question:** *"I received a damaged mixer-grinder 5 days ago. Can I still get a replacement, and what is the process?"*

1. **Query:** The customer's exact sentence above is sent to the assistant.

2. **Retrieve:** The system looks into the **Returns & Replacements Policy** document and brings back the most relevant chunk, for example:
   > *"Small kitchen appliances reported as damaged within 7 days of delivery are eligible for a free replacement. Customer must upload photo proof; pickup is scheduled within 48 hours; replacement dispatched within 3 working days. — Returns Policy, Section 4.1."*

3. **Context:** This retrieved chunk is placed *next to* the customer's question inside the prompt that goes to the LLM. So now the LLM is not answering blindly — it has both the customer's question *and* the exact ShopEase rule in front of it as supporting material.

4. **Generate:** Using the retrieved chunk as its source, the LLM produces a grounded answer:
   > *"Yes — as per ShopEase's Returns Policy (Section 4.1), damaged small-appliance reports are valid within 7 days of delivery. Since you are on day 5, you qualify for a free replacement. Please upload photo proof; a pickup will be scheduled within 48 hours and a replacement dispatched within 3 working days."*

This answer is **specific**, **grounded in a real ShopEase document**, and **directly usable** — not LLM guesswork.

---

### Grading Rubric (internal)

| Question | Weight | Key Check |
|---|---|---|
| Q1 — Why the chatbot failed | 30% | Names the real root cause (no access to ShopEase policies / static knowledge) + hallucination, with a **specific, realistic** ShopEase wrong-answer example. Length ~100–150 words. |
| Q2 — Documents the assistant should read from | 25% | 3–5 distinct, real-sounding ShopEase documents with a clear one-line purpose each. |
| Q3 — RAG 4-step flow walkthrough | 45% | All four steps explained *in detail*, realistic retrieved chunk with real-looking content, clear explanation of how the retrieved context helps produce the final grounded answer. Length ~150–200 words. |

### Alternative Acceptable Approaches

- A different **non-sensitive** company (e.g., an internal IT helpdesk, a bank's FAQ assistant, a SaaS product-documentation assistant) is acceptable, as long as all 3 questions are answered with the same level of specificity and realism.
- Learners do **not** need to discuss vector databases, embeddings, chunk sizes, top-k, or evaluation — those topics are covered in later sessions.
