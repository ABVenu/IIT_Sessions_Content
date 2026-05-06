# Subjective Assignment — Introduction to Memory in AI Agents

---

## The TalentBot Memory Audit

### Background

**TalentBot** is an AI recruitment assistant built by a startup. Job applicants use it over several weeks — first to check eligibility, then to schedule interviews, then to get updates. The product team believed a stateless design was "good enough" for a simple hiring workflow.

They were wrong.

The team has just received this batch of user feedback:

> **Feedback 1 — Priya (Applicant, Applied for Product Manager Role):**
> *"I told TalentBot my role, my experience level, and my preferred interview slot — all in the first conversation. Three days later I came back to ask about the next round. It had no idea who I was or what role I had applied for. I had to repeat everything. Felt like my application didn't matter."*

> **Feedback 2 — Karan (Applicant, Applied for Data Analyst Role):**
> *"I mentioned I have two years of Python experience and no SQL background. TalentBot later sent me a 'technical prep guide' that was entirely focused on SQL. It clearly didn't remember what I said."*

> **Feedback 3 — HR Team Member:**
> *"We wanted TalentBot to remember which candidates it already rejected so it doesn't accidentally invite them to interview again. Right now it has no idea — and we've had awkward situations."*

The CTO has asked you — a junior AI systems consultant — to **audit TalentBot's memory design and submit a redesign proposal**.

---

### Your Task

Write a **TalentBot Memory Redesign Proposal** as a structured document. Your proposal must cover the following four sections:

---

**Section 1 — What Went Wrong and Why**

Analyse the three feedback points above. For each one:
- Identify the specific memory problem it demonstrates (use the correct term from the session)
- Explain in one sentence why the stateless design caused this exact failure

*(You are explaining root causes, not just describing what happened.)*

---

**Section 2 — Memory Architecture Design**

Design what TalentBot should remember about each applicant. Create a table with at least **7 entries**, using this format:

| Information to Store | Memory Type (Short-Term / Long-Term Episodic / Long-Term Semantic / Long-Term Procedural) | Memory Lifetime | Why It Matters |
|---|---|---|---|

After the table, list **2 specific pieces of information TalentBot should NOT store in long-term memory** and give a reason for each. At least one reason must relate to privacy.

---

**Section 3 — Context Assembly for a Live Request**

An applicant named **Divya** opens TalentBot and says:

> *"What should I prepare for my next round?"*

TalentBot's memory for Divya contains:
- Applied for UX Designer role, 4 years of experience
- Cleared Round 1 (portfolio review) — interviewer note: "strong visual work, weak on user research process"
- Round 2 is a case study presentation, scheduled for next Tuesday
- Divya mentioned she gets nervous in live presentations
- She once asked an unrelated question about TalentBot's refund policy for a paid feature
- She prefers bullet-point style communication

Write the **assembled context brief** that TalentBot should send to the AI model before generating the response. Format it as a short paragraph (5–7 sentences) starting with: *"Divya is applying for…"*

Also state — in one line — which memory from the list above should NOT be retrieved, and why.

---

**Section 4 — One Critical Privacy Rule for a Recruitment Context**

Recruitment is sensitive — TalentBot stores rejection decisions, skill assessments, and interview notes. Write **one privacy rule** that you believe is the most important for TalentBot to follow. Make a case for it in 3–5 sentences, specifically addressing the risks that arise in a hiring context if this rule is ignored.

---

### Submission Instructions

- Create a Google Doc in your Google Drive. Suggested folder path (for your reference): `Module 2 > Session12 > Assignment Submission`
- Write all four sections clearly labelled as **Section 1**, **Section 2**, **Section 3**, and **Section 4**
- Use the table format for Section 2
- Keep the writing concise and well-organised
- Once the document is ready, click the **Share** button and copy the link
- Make sure sharing is set to **"Anyone with the link can view"** (public sharing required for review)
- Paste and submit the Google Doc link in the answer box

---

**Answer Explanation (Ideal Solution Walkthrough)**

**Section 1 — What Went Wrong and Why**

A strong answer identifies the following:
- **Priya's feedback** → *Repetition Problem* and *Loss of Context Problem*. The stateless design stored nothing from her previous session, so TalentBot treated her return as a brand-new interaction, forcing her to repeat role, experience, and preferences.
- **Karan's feedback** → *Loss of Context / Poor Personalisation*. A memory-powered agent would have stored Karan's Python background and SQL gap; the stateless design had no user profile, so the prep guide was generic rather than tailored.
- **HR team feedback** → *Incoherence Problem in Multi-Step Tasks*. Without episodic memory of past rejection decisions, TalentBot cannot track the state of each candidate's journey across sessions, leading to contradictory or embarrassing actions.

**Section 2 — Memory Architecture Design**

Strong answers will include entries such as:

| Information | Memory Type | Lifetime | Why It Matters |
|---|---|---|---|
| Applicant's name and applied role | Long-Term (Semantic) | Until application closes | Core identity — needed in every session |
| Technical skills declared by applicant | Long-Term (Semantic) | Permanent (application-scoped) | Enables personalised prep and role matching |
| Current stage in the hiring process | Long-Term (Episodic) | Until application closes | Tracks task progress across sessions |
| Interview feedback from previous rounds | Long-Term (Episodic) | Until application closes | Avoids inconsistent guidance |
| Applicant's preferred communication style | Long-Term (Semantic) | Permanent (application-scoped) | Shapes tone and format of future replies |
| Rejection decisions | Long-Term (Episodic) | Long-term archive | Prevents accidental re-engagement |
| Interview slot preference | Long-Term (Semantic) | Medium-lived | Scheduling continuity |

*Do NOT store:* Random queries unrelated to the application (low future value); emotionally sensitive notes from interviewers that could bias future interactions or create legal risk (privacy/legal risk).

Alternative approaches that are also valid: Grouping memory into profile memory, progress memory, and preference memory. Using a memory expiry policy tied to application status (active, rejected, hired).

**Section 3 — Context Assembly for a Live Request**

A strong assembled context brief:

*"Divya is applying for the UX Designer role with 4 years of experience. She cleared Round 1 (portfolio review); the interviewer noted strong visual work but a weak user research process. Her next round is a case study presentation scheduled for this Tuesday. She has mentioned she gets nervous during live presentations. She prefers bullet-point style communication. The current request is: what should she prepare for the next round? Respond with a focused, bullet-point preparation guide for a case study presentation, acknowledging the weak area flagged in Round 1 and her nervousness around live presenting."*

The refund policy query should NOT be retrieved — it is a one-time, unrelated administrative question with no bearing on interview preparation, and including it wastes context window space.

**Section 4 — One Critical Privacy Rule**

Strong answers may include: candidates must be informed about what TalentBot stores about them; rejection decisions must not be used outside the current application cycle without consent; skill assessments must be access-restricted to authorised HR personnel only. The strongest answers connect the rule to real risk — e.g., if rejection notes and biases are stored and retrieved without control, they can influence future applications by the same candidate unfairly, raising legal and ethical concerns under India's DPDP Act or similar regulations.
