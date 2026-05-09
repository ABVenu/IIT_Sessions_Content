# Subjective Assignment — Evaluating and Improving RAG Systems

**Total Questions:** 1 | **Type:** Applied Theory Task | **Difficulty:** Medium

---

## Question 1

### Scenario

You have just joined as a junior AI engineer at **MediAssist**, a healthcare startup that has built a RAG-powered chatbot to help patients interact with a large multi-specialty hospital chain. The chatbot answers queries using a knowledge base of hospital policy documents — appointment booking rules, cancellation and rescheduling procedures, insurance eligibility guidelines, emergency walk-in protocols, and billing policies.

The chatbot is ready for deployment, but before going live, your CTO says: *"We cannot afford wrong answers in a healthcare context. A patient who gets incorrect insurance eligibility information could face denied claims. A patient who misunderstands the cancellation policy could lose their appointment slot. We need a proper evaluation plan before this launches."*

Your task is to **design and document a comprehensive RAG Evaluation Plan** for the MediAssist chatbot. This is not a coding task — it is a structured analytical and design exercise.

---

### What You Must Include in Your Document

Your evaluation plan must cover the following four sections:

**Section 1 — Sample Evaluation Dataset**
Create a sample evaluation dataset with at least **5 test query entries**. Present this as a table with three columns: User Query | Expected Document to Retrieve | Expected Correct Answer. Use realistic healthcare scenarios (appointments, insurance, billing, cancellations). Do not copy e-commerce examples from the session.

**Section 2 — Failure Case Analysis**
Identify **2 specific failure scenarios** that could occur with this healthcare chatbot. For each, write:
- A concrete example (what the user asked, what the system got wrong)
- The root cause (outdated document, similar-looking queries confusing the retriever, hallucination, etc.)
- How you would detect it during evaluation

**Section 3 — Strong Prompt Template**
Write a complete prompt template for the MediAssist chatbot that:
- Restricts the LLM to use only the retrieved policy context
- Explicitly prevents hallucination of medical or policy details
- Instructs the system to say *"I don't have that information — please contact our support team"* when the answer is not in the context
- Ensures specific timelines, eligibility conditions, and limitations are stated when available

**Section 4 — Continuous Improvement Plan**
Describe the improvement loop in brief:
- The user feedback mechanism you would implement (e.g., thumbs up/down with follow-up questions)
- At least **3 real-world changes** in a healthcare environment that would trigger a re-evaluation (e.g., updated insurance partner list, new specialist added, revised cancellation fee)

---

### Submission Instructions

- Create a **Google Doc** in your Google Drive.
  - Suggested folder path (for your reference): `module2 > Session31 > Subjective Assignment`
- Write your evaluation plan neatly and clearly, structured by the sections as above.
- Add diagrams, tables, or flowcharts wherever they improve clarity (e.g., a table for the evaluation dataset, a flowchart for the continuous improvement loop).
- Once your document is ready, click **Share**, set sharing to **"Anyone with the link can view"**, and copy the link.
- Submit the Google Doc link in the LMS answer box.

---

### Answer Explanation (for Evaluators)

**What a strong submission looks like:**

**Section 1 — Evaluation Dataset** should contain realistic healthcare queries such as:
- *"Can I book an appointment for my elderly parent online?"* → Appointment Booking Policy → Yes/No based on dependent booking rules
- *"Is my insurance accepted for an MRI scan?"* → Insurance Eligibility Policy → Depends on insurer tie-up details
- *"What is the fee if I cancel 2 hours before my appointment?"* → Cancellation Policy → Specific penalty amount or free-cancellation window

**Section 2 — Failure Cases** should demonstrate awareness of:
- *Confusion between similar queries:* "reschedule my appointment" vs. "cancel my appointment" — both relate to appointment + time change but require different policy sections
- *Outdated document:* Insurance partner list changes frequently; an old document may list an insurer that is no longer accepted, causing a hallucination of valid coverage
- Root causes should point to the Retriever, not the LLM, per the session's core principle

**Section 3 — Prompt Template** should include: a role definition (healthcare support agent), strict instruction to use ONLY provided context, an explicit no-hallucination clause, a fallback statement (*"I don't have that information — please contact our support team"*), and a directive to state specific timelines and eligibility conditions.

**Section 4 — Continuous Improvement** should mention a patient feedback mechanism (thumbs up/down + follow-up questions like "Was the answer accurate?"), and real-world triggers such as: new insurance partner added/removed, new specialist department opened, revised cancellation fee policy, or new payment method introduced.
