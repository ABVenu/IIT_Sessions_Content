# Assignment Subjective

Total Questions: 1  
Difficulty: Medium  
Type: Applied prompt design (document + Groq Playground validation)

---

## Q1 (Applied, Medium)

**CampusShelf** — a college library — wants a **Book Recommendation Assistant** for first-year students. Students will paste their **degree, favourite subjects, and reading time available**; the assistant must suggest **three books** with a one-line reason each — nothing outside academics and leisure reading.

You are the prompt engineer. Design, test, and document one **beginner single-agent prompt package** using **Groq Playground** (`console.groq.com`).

---

### What you must deliver (in one Google Doc)

Your document must contain **all six parts** below. Write in clear, professional English.

#### Part 1 — System prompt (bounded agent)

Write the full **system prompt** you would paste in the Groq **system** slot. It must include:

- A **named persona** (e.g. librarian assistant name)  
- **Scope** — what the bot will and will not answer  
- One **refusal line** for off-topic requests (e.g. exam paper leaks, personal health)  
- A **grounding / hallucination guardrail** (e.g. do not invent book titles not commonly known; say when unsure)  
- An explicit **output format** with three labelled book entries  

#### Part 2 — User message template

Write a **user message template** with a clearly marked placeholder, e.g. `[STUDENT PROFILE]`, that a student would fill each time. Show **one filled example** using this profile:

> BCom first year. Likes business biographies and light fiction. Has 30 minutes per day to read.

#### Part 3 — Five building blocks map

Add a short table mapping your prompt to the five template blocks:

| Block | Where it appears in your design (quote one line each) |
|---|---|
| Role | |
| Task | |
| Instructions | |
| Constraints | |
| Output format | |

#### Part 4 — Technique choice (applied reasoning)

In **3–5 sentences**, justify which prompting layer you relied on most:

- **Zero-shot** only,  
- **Few-shot** (include the examples you added), or  
- **Chain-of-thought** (list the numbered steps in your system prompt),  

and explain **why** that choice fits a book-recommendation task better than the other two options.

#### Part 5 — Groq Playground tests (evidence)

Test your prompts in Groq Playground with **Llama 3.3** (or any available Groq model). Add **two screenshots**:

1. **On-topic test** — use the filled student profile from Part 2.  
2. **Off-topic test** — ask something outside scope (e.g. *"Write my entire economics exam answers"*).  

Under each screenshot, write **2–3 lines** noting whether the assistant followed **scope**, **output format**, and **guardrails**.

#### Part 6 — Token-awareness note

In **2–3 sentences**, explain which part of your prompt would cost the **most tokens** if you scaled this to thousands of students per day, and one change you could make to reduce cost **without** removing safety rules.

---

### Submission instructions

- Create a **Google Doc** in your Google Drive.  
  Suggested folder path: `Module3` → `Session24` → `CampusShelf-Prompt-Design`  
- Write all six parts neatly. **Embed both Groq screenshots** in the doc.  
- When ready, click **Share** → set access to **Anyone with the link** → **Viewer**.  
- Submit the **public Google Doc link** in the LMS answer box.

---

### Answer Explanation (for assessors)

**Ideal approach walkthrough**

**Part 1 — Sample system prompt (acceptable variation allowed):**

```text
You are Priya, a friendly campus library assistant for first-year college students in India.

Scope:
- Recommend books for study and leisure reading based on the student's profile.
- Suggest exactly three books per request with a one-line reason each.
- Do not answer exam cheating requests, medical advice, or political debates.

Refusal:
- If asked off-topic, say: "I help with book recommendations only — please ask the library desk for other queries."

Grounding:
- Recommend well-known, real book titles. If unsure a title exists, say so instead of inventing.

Output format:
Book 1: <title> / <author if known> / Why it fits: <one line>
Book 2: ...
Book 3: ...
Keep total reply under 200 words.
```

**Part 2 — Sample user template:**

```text
[STUDENT PROFILE]
Degree: BCom first year. Likes business biographies and light fiction. 30 minutes/day to read.

Please recommend three books.
```

**Part 3 — Building blocks map (sample):**

| Block | Example line from design |
|---|---|
| Role | *"You are Priya, a friendly campus library assistant…"* |
| Task | *"Recommend exactly three books per request…"* |
| Instructions | *"Read profile → match genres → give one-line reasons"* (may be implicit in Task) |
| Constraints | Refusal line + grounding rule + word limit |
| Output format | Three labelled `Book 1 / Book 2 / Book 3` lines |

**Part 4 — Technique justification (sample):**  
Most designs will be **zero-shot + strong system prompt** with five-block structure — book recommendation is a general language task where format and scope are set in system, not taught via many examples. **Few-shot** is acceptable if the learner adds 1–2 sample book entries to lock tone. **CoT** is optional but valid if they embed numbered steps (*read profile → shortlist genres → pick three → format*). Mark correct if justification matches their chosen technique.

**Part 5 — Screenshots:**  
On-topic: three books in requested format. Off-topic: refusal or scope message, not full exam answers.

**Part 6 — Token note (sample):**  
Long system prompts and few-shot blocks cost the most; shortening examples or moving stable rules to a concise system prompt saves tokens while keeping refusal and grounding lines.

**Alternative valid approaches:**  
- Few-shot with two sample book recommendations before the real profile.  
- Light CoT with 3–4 numbered steps in system prompt.  
- Different persona names or output labels if structure stays predictable.

**Common mistakes to watch for:**  
- All rules in user message only (no system prompt).  
- No off-topic test or screenshot.  
- No grounding rule — model may invent obscure titles.  
- Claiming CoT is required but providing no numbered steps.

**Grading rubric (suggested):**

| Criterion | Points |
|---|---|
| Complete system prompt with persona, scope, refusal, grounding, output format | 25% |
| User template + filled example | 15% |
| Five-block map with accurate quotes | 15% |
| Technique justification logically matches design | 15% |
| Two Groq screenshots with brief analysis | 20% |
| Token-awareness note | 10% |
