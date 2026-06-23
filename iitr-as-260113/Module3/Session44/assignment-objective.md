# Assignment Objective

Total Questions: 10

Difficulty Flow: Easy → Moderate → Hard

Question Types:
- 6 MCQ (Single Correct): Q1–Q6
- 4 MSQ (Multiple Correct): Q7–Q10

---

## Q1 (MCQ, Easy)

**Riya** joins a company and asks the internal **HR chatbot**: *"How many paid leaves do full-time employees get?"* The bot first searches policy documents, then calls no other tool, and replies with **24 paid leaves** citing **HR Policy 002**.

Which step in the **enterprise agent pattern** is the **policy document search**?

A. Intent understanding only — no retrieval step exists  
B. **RAG retrieval** — pulling relevant business context before answering  
C. Random text generation without a knowledge base  
D. Deleting chat history after every message

**Correct Answer:** B

**Answer Explanation:**  
Policy search from a vector store is **retrieval-augmented generation (RAG)** — the agent grounds the answer in approved documents before replying.

**Why other options are wrong:**  
- A: Intent may happen first, but policy search is explicitly retrieval, not intent alone.  
- C: The scenario describes structured policy lookup, not blind generation.  
- D: Memory management is unrelated to retrieving leave policy.

---

## Q2 (MCQ, Easy)

A **finance team** builds an agent to **approve travel reimbursements**. An employee submits a claim for a **personal weekend trip**. The agent approves it without reading the reimbursement policy.

Why is this a serious **operational guardrail** failure?

A. Agents should always approve claims to keep employees happy  
B. **Approvals must trace to company policy** — random yes/no creates fraud and compliance risk  
C. GST filing is unrelated to reimbursements  
D. Vector databases cannot store policy text

**Correct Answer:** B

**Answer Explanation:**  
Finance agents must **read policy** before approve/reject. Personal travel paid by mistake is a **blunder** called out in enterprise finance patterns.

**Why other options are wrong:**  
- A: Policy-bound decisions override convenience.  
- C: GST is another finance use case, not the issue here.  
- D: Policies are commonly stored in vector DBs or document stores.

---

## Q3 (MCQ, Easy)

A developer builds a **lab demo** of an HR onboarding agent with five policy documents. Data can be lost when the script stops, and no advanced metadata filters are needed yet.

Which vector store choice fits **best** for this quick prototype?

A. **InMemoryVectorStore** — embeddings live in RAM for the running process  
B. A production Pinecone cluster with multi-region replication  
C. A handwritten Excel sheet with no embeddings  
D. Deleting all policy documents to save memory

**Correct Answer:** A

**Answer Explanation:**  
**InMemoryVectorStore** is fast to set up for small corpora in demos. Production teams often move to **Chroma** or hosted stores when persistence and filters matter.

**Why other options are wrong:**  
- B: Over-engineered for a five-document lab.  
- C: Excel without embeddings cannot power semantic RAG search.  
- D: Removes the knowledge base the agent needs.

---

## Q4 (MCQ, Easy)

After `agent.invoke(...)`, a developer prints the full result object. They see a long **ToolMessage** with the entire leave-policy paragraph, but the employee should only see a short summary with a citation.

Which message type should be shown to the **end user**?

A. **AIMessage** — the polished assistant reply after tool results are processed  
B. Raw ToolMessage only — paste the full policy chunk  
C. HumanMessage — the user's own question repeated  
D. Empty string always

**Correct Answer:** A

**Answer Explanation:**  
**ToolMessage** holds raw tool output for the LLM. The **AIMessage** summarises in plain language with evidence — often extracted via `result["messages"][-1].content`.

**Why other options are wrong:**  
- B: Dumping tool output confuses users and leaks verbose policy text.  
- C: HumanMessage is the user's input, not the answer.  
- D: The agent should return a helpful summary when evidence exists.

---

## Q5 (MCQ, Moderate)

**Karan** asks the HR onboarding agent: *"What mandatory trainings must a backend engineer complete?"* The agent has three tools: `search_hr_policy`, `get_employee_profile`, and `get_mandatory_trainings`.

Which tool is the **most direct** first choice?

A. `get_mandatory_trainings` — role-based training lists are its purpose  
B. `get_employee_profile` — only needed when personalising by employee ID  
C. `search_hr_policy` — only for weather forecasts  
D. No tool — the LLM should guess training names

**Correct Answer:** A

**Answer Explanation:**  
Training recommendations by **role** map to `get_mandatory_trainings`. Policy search may add context, but the dedicated training tool is the primary fit.

**Why other options are wrong:**  
- B: Profile lookup helps personalisation (e.g. work mode), not role-wide training lists.  
- C: Policy search covers leave/benefits-style questions, not weather.  
- D: Guessing violates grounded-agent design.

---

## Q6 (MCQ, Moderate)

A joiner asks: *"Is there a relocation bonus for eligible moves?"* The retriever returns **no matching policy chunk**. The system prompt says: *"Never invent a policy. If evidence is not found, say HR confirmation is required."*

What should the agent do?

A. Invent a ₹1,00,000 bonus so the user feels welcomed  
B. **Escalate** — state that **HR confirmation** is needed because evidence is missing  
C. Call `get_mandatory_trainings` and ignore the question  
D. Return the entire vector database dump

**Correct Answer:** B

**Answer Explanation:**  
**Escalation** hands off to humans when the corpus lacks proof. Inventing policy is a compliance and trust failure.

**Why other options are wrong:**  
- A: Hallucinated benefits create legal exposure.  
- C: Training tool does not answer relocation bonus questions.  
- D: Raw DB dumps are not user-facing answers.

---

## Q7 (MSQ, Moderate)

A product manager compares **finance reimbursement**, **HR onboarding**, and **LinkedIn content** agents. All three follow intent → retrieve → tool → validate → respond.

Which statements about **how they differ** are **correct**?

A. Finance agents need **strict policy-bound approve/reject** guardrails because money is involved  
B. HR onboarding agents need **high retrieval** on policy docs and tools for **employee profile** and **trainings**  
C. Content agents typically focus on **scheduling posts** and **brand tone** rather than leave-policy citations  
D. All three domains never use tools — only plain chat

**Correct Answers:** A, B, C

**Answer Explanation:**  
Each domain shares the enterprise skeleton but differs in **data sources**, **risk**, and **guardrails** — finance (money), HR (policy + personalisation), content (brand + schedule).

**Why other options are wrong:**  
- D: All three patterns in class use **tools** (payments, HR lookups, platform upload, etc.).

---

## Q8 (MSQ, Moderate)

An HR agent's system prompt requires every grounded answer to include structured parts for trust and audit.

Which components belong in a **well-designed HR response** (when applicable)?

A. **Answer** — concise professional text  
B. **Evidence** — policy source ID or document name  
C. **Actions taken** — which tool was triggered (e.g. searched leave policy)  
D. **Employee's personal bank PIN** — always included for transparency

**Correct Answers:** A, B, C

**Answer Explanation:**  
Class answer format: **Answer + Evidence + Actions + Escalation/next steps** when needed. Citations build trust; action lines aid debugging.

**Why other options are wrong:**  
- D: Sensitive credentials must never appear in agent replies — security and privacy violation.

---

## Q9 (MSQ, Hard)

An evaluation harness row tests the HR agent with:

- **Input:** *"What is the weather in Bangalore today?"*  
- **`should_refuse`:** `true`  
- **`forbidden_tools`:** includes `search_hr_policy`

The agent politely answers with a weather forecast and called `search_hr_policy` anyway.

Which failures does the harness correctly flag?

A. **Out-of-corpus** question answered instead of refused  
B. **Forbidden tool** used when it should not run  
C. Test passes because the weather text sounds fluent  
D. **`should_refuse`** expectation violated — valid in-domain leave questions should not refuse, but this weather case should

**Correct Answers:** A, B, D

**Answer Explanation:**  
Eval JSON checks **trajectory** (tools) and **refusal behaviour**, not fluency alone. Weather is **out-of-corpus** for an HR onboarding agent.

**Why other options are wrong:**  
- C: Polite wrong answers still fail grounded/refusal tests.

---

## Q10 (MSQ, Hard)

**TechNova** plans a **stakeholder demo** of the HR onboarding agent before go-live.

Which demo and risk practices are **sound**?

A. Show one **in-domain** win (e.g. leave count with **HR_POLICY_002** citation)  
B. Show one **out-of-corpus** question handled with **refusal or HR escalation** — no hallucination  
C. Mention **residual risks** such as hallucination if retrieval misses, or needing **human-in-the-loop** before irreversible HR actions  
D. Demo only happy paths and hide refusal behaviour so stakeholders stay impressed

**Correct Answers:** A, B, C

**Answer Explanation:**  
Stakeholder demos build trust with **grounded success**, **clean refusal**, and honest **risk/mitigation** talk (eval harness, Chroma for production, HITL).

**Why other options are wrong:**  
- D: Hiding failure modes creates false confidence and production surprises.
