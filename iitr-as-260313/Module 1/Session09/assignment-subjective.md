# Subjective Question

### Task: Design the AI Brain Behind "CampusConnect"

### Scenario

**CampusConnect** is a startup building an AI assistant for Indian engineering college students. The assistant, called **"GyanBot"**, should help students with three tasks:

1. **Doubt solving** — answer academic doubts in simple language.
2. **Career guidance** — suggest careers, internship paths, and skill gaps based on a student's branch and interests.
3. **Event discovery** — recommend relevant hackathons, workshops, and college fests happening in the next 30 days.

The founding team has a basic ChatGPT subscription. They have built nothing yet — no code, no database. Their first step is to **design GyanBot on paper** before any development begins.

You are the **AI Product Designer** hired for a day. Your job is to deliver a complete design document for GyanBot — not code, but a well-reasoned blueprint using everything you have learned about prompt engineering and AI agent frameworks.

> This is a design and reasoning task, not a coding task. Vague or generic answers will not score well. All prompts you write must be specific, usable, and grounded in the session concepts (C-I-F-C, system prompts, role prompting, output formats, frameworks, agent flow). Use realistic Indian college context in your examples — generic answers score lower.

---

**Part 1 — Write GyanBot's System Prompt** *(target length: 100–150 words)*

Design a complete system prompt for GyanBot. Your system prompt **must explicitly include and label** all five components:

- **Identity** — who GyanBot is and what it does.
- **Tone** — how it should communicate (remember: the audience is stressed engineering students).
- **Boundaries** — at least two things GyanBot must never do.
- **Format** — one rule about how answers should be structured.
- **Scope** — what topics are in-scope and what falls outside.

After writing the prompt, add **2–3 lines** explaining *why* one specific boundary or scope rule you chose matters for this product.

---

**Part 2 — Write One Strong User Prompt Using C-I-F-C** *(target length: 80–120 words)*

A 3rd-year Computer Science student named Aryan has these details:
- Skills: Python, basic ML, good communication.
- Goal: Land a data science internship by December.
- Problem: He does not know which specific skills are missing or which companies to target.

Write the **user-side prompt** Aryan should type into GyanBot, using the **C-I-F-C formula**. Clearly label each part (Context / Instruction / Format / Constraints) either inline or in a short note below the prompt. The prompt must be ready-to-use — not a template with blanks.

---

**Part 3 — Choose the Right Framework and Justify** *(target length: 120–160 words)*

The CampusConnect team is debating which framework to use. They have narrowed it down to **LangChain**, **CrewAI**, or **AutoGen**.

Given that GyanBot:
- Needs to pull answers from a database of **college-specific FAQs and syllabus PDFs** (not just public internet knowledge),
- Is a single assistant (not a team of agents),
- Must reply fast, in a single clean response, without back-and-forth debate,

**State which framework you recommend** and write a clear justification (3–4 sentences) explaining *why* it fits this use case and *why the other two are less suitable* here. Reference specific framework characteristics from the session in your reasoning — do not just use the framework names without explanation.

---

**Part 4 — Sketch the Agent Flow for the Career Guidance Feature** *(target length: 100–150 words)*

The career guidance feature works like this: a student describes their skills and goal → GyanBot searches a career resource database → it returns a structured recommendation.

Write the **step-by-step agent flow** for this feature using the 4 building blocks: **Input (Prompt)**, **Brain (LLM)**, **Hands (Tools)**, **Output (Result)**.

Your answer must:
- Show **at least 5 steps** (e.g., Step 1: user input → Step 2: system prompt sets role → … → Step N: final output).
- Clearly show **where the tool call happens** and what it fetches.
- End with a description of what the final output looks like (format and content), as the student would see it.

---

### Submission

Submit **any one** of the following:

- Public **GitHub repository** link containing `solution.md`
- Public **Google Doc** link
- Directly type your answer in the answer box (use clear headings for each Part)
