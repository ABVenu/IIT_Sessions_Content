# Assignment Subjective

Total Questions: 1  
Difficulty: Easy  
Type: Applied Explanation (No Coding)

---

## Q1 (Applied Explanation, Easy)

**Ananya** is the HR lead at **GreenLeaf Tech**. The company is rolling out an **HR onboarding chat assistant** for new joiners. On the first day, two employees send these messages:

1. **Priya:** *"How many paid leaves does a full-time employee get per year?"*  
2. **Rahul:** *"What is the weather in Pune today?"*

GreenLeaf's assistant is built with:
- HR policy documents stored in a **vector database** (searchable by meaning)  
- Three tools: **`search_hr_policy`**, **`get_employee_profile`**, **`get_mandatory_trainings`**  
- System rules: **never invent policy**; if evidence is missing, say **HR confirmation is required**; include **evidence** and **actions taken** when answering policy questions  

**Your task:** Explain in your own words how a **well-designed** HR onboarding assistant should handle **Priya's question** and **Rahul's question** separately.

For **each** employee message, write a short explanation covering:

1. Whether the question is **in-domain** (answerable from HR policies/tools) or **out-of-corpus** (outside HR scope)  
2. Which **tool(s)** the agent should use — or whether it should **not** call HR tools  
3. What kind of **answer** the employee should see (include **evidence** or **refusal/escalation** as appropriate)  
4. One **risk** if the agent handles that message badly  

Keep your total answer between **150 and 250 words**. Write in clear paragraphs or bullet points. **No code** is required.

---

### Submission Instruction

- Type your answer in the answer box in the LMS

---

## Answer Explanation (Ideal Solution Walkthrough)

### Priya — leave policy question

| Point | Ideal answer |
|---|---|
| **Domain** | **In-domain** — leave count is in HR policy corpus |
| **Tool(s)** | **`search_hr_policy`** (primary). `get_employee_profile` is optional unless the answer must be personalised by employee record |
| **Answer shape** | Concise answer (e.g. full-time employees receive **24 paid leaves** per year), **evidence** citing policy source such as **HR_POLICY_002** / leave section, **actions taken** noting policy search — not the raw full PDF paragraph |
| **Risk if handled badly** | **Hallucinated** leave count or answer without citation — employee trusts wrong info; compliance issue |

### Rahul — weather question

| Point | Ideal answer |
|---|---|
| **Domain** | **Out-of-corpus** — weather is not in HR onboarding scope |
| **Tool(s)** | Should **not** call `search_hr_policy`, `get_employee_profile`, or `get_mandatory_trainings` for weather data |
| **Answer shape** | **Polite refusal** or redirect: assistant helps with onboarding, leave, benefits, trainings — not weather. Optionally suggest HR or general help channels. **No fabricated forecast** |
| **Risk if handled badly** | **Under-refusal** — inventing weather or misusing HR tools makes the agent untrustworthy and fails eval cases with `should_refuse: true` |

### Sample model answer (within word limit)

**Priya:** This is an in-domain HR question. The agent should call `search_hr_policy` to retrieve the leave-policy chunk, then reply with a short summary (e.g. 24 paid leaves for full-time staff), cite HR_POLICY_002 as evidence, and note that it searched the leave policy. A bad response would guess the number or paste the entire policy document.

**Rahul:** Weather is out-of-corpus for HR onboarding. The agent should refuse politely without calling HR tools — it is not a weather service. A bad response would make up a forecast or waste retrieval on irrelevant policies.

### Alternative valid approaches

- Mentioning **escalation to HR** for Priya only if retrieval returns no chunk — still in-domain but evidence missing.  
- Noting **`get_mandatory_trainings`** is irrelevant for both questions — shows tool-routing understanding.

### Common mistakes

- Treating both questions the same way.  
- Saying Rahul's question should use `search_hr_policy`.  
- Omitting **evidence** for Priya or **refusal** for Rahul.
