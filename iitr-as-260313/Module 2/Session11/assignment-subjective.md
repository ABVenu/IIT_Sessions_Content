# Subjective Assignment — Self-Reflection and Feedback Loops

---

## Practical Task — Build a Quality-Controlled Agent Prompt Flow

### Scenario

You are an AI workflow consultant hired by a regional coaching institute. The institute's grading team reviews hundreds of student essays each day, and they want to automate the feedback process using an AI agent.

Every piece of feedback the agent produces must:
- Acknowledge at least one specific strength in the student's writing
- Identify the single most important area for improvement
- Maintain an encouraging, constructive tone — never harsh or discouraging
- Stay under 120 words

The institute has been piloting an AI agent for two months, and the grading head has reported two recurring problems:

1. **Problem A:** The feedback often only criticises — it skips acknowledging the student's strengths entirely, which damages student motivation.
2. **Problem B:** The tone is inconsistent — some feedback reads as harsh and blunt, while others are warm and encouraging. Students from the same batch are getting completely different experiences.

---

### Your Task

Design a **complete, production-ready agent prompt flow** that solves both reported problems. Your prompt flow must include all five sections listed below, each clearly labelled.

---

**[ROLE]**
Define who this agent is:
- Its area of expertise and persona
- Its default communication tone
- At least one explicit constraint on what it must never do

---

**[TASK]**
Write a sample task with placeholders for:
- Student name
- Essay topic
- Essay content (the submitted essay text)

The task must make clear what the agent is expected to produce.

---

**[REFLECTION + FEEDBACK CRITERIA]**
Design exactly **4 measurable (Yes/No) criteria** the agent will use to self-evaluate its own output.

For each criterion, write **one sentence** explaining which of the two reported problems (Problem A or Problem B) it directly addresses and why.

---

**[OUTPUT FORMAT]**
Specify exactly how the final feedback should be presented:
- The structure (sections or flow)
- The word limit
- Any tone or language markers the agent must follow

---

**[LOOP INSTRUCTION]**
Write the loop instruction the agent will follow, including:
- What to do if any criterion is answered No
- The maximum number of revision cycles allowed
- What the agent should state if it cannot satisfy all criteria within that limit

---

**Design Note (Required)**

After your prompt flow, write a brief note of **3 to 5 sentences** that explains:
- Why you chose the specific constraints you placed in the ROLE section
- How your four reflection criteria specifically address Problem A and Problem B from the scenario
- What would happen to the agent's output if these criteria were removed

---

### Submission Instructions

- Create a Google Doc in your Google Drive. Suggested folder path (for your reference): `Module 2 > Session11 > Assignment Submission`
- Write your prompt flow with clearly labelled sections and proper formatting. Use headings for each section: [ROLE], [TASK], [REFLECTION + FEEDBACK CRITERIA], [OUTPUT FORMAT], [LOOP INSTRUCTION], and Design Note.
- Once the document is ready, click the **Share** button and copy the link.
- Make sure the sharing settings are set to **"Anyone with the link can view"** (public sharing is required for review).
- Paste and submit the Google Doc link in the answer box.

---

**Answer Explanation (Ideal Solution Walkthrough)**

A strong submission will show mastery of the four-component agent prompt flow structure covered in the session.

**[ROLE]** — A well-defined role anchors the agent's default behaviour. An ideal Role for this agent would establish a persona such as *"a supportive writing coach with expertise in student essay feedback"*, set the tone explicitly (*"always encouraging, never critical without a follow-up suggestion"*), and include a hard constraint such as *"never deliver feedback that does not include at least one specific positive observation."* This directly prevents Problem B (tone inconsistency) because the Role applies to every single run.

**[TASK]** — A clear task with placeholders ensures the agent always knows what it is working with. A strong task would read: *"Read the essay titled [ESSAY TOPIC] submitted by [STUDENT NAME]. Provide personalised feedback that acknowledges a specific strength, identifies the most important area to improve, and ends with an encouraging closing sentence. Keep the feedback under 120 words."*

**[REFLECTION CRITERIA]** — The four criteria must be measurable (Yes/No). An ideal set addressing both problems:
1. *"Does the feedback explicitly mention at least one specific thing the student did well? (Yes/No)"* — addresses Problem A directly.
2. *"Does the feedback identify exactly one area for improvement — not a list of criticisms? (Yes/No)"* — prevents the agent from defaulting to a criticism-heavy response.
3. *"Does the feedback use encouraging language and avoid harsh or blunt phrasing? (Yes/No)"* — addresses Problem B directly.
4. *"Is the feedback under 120 words? (Yes/No)"* — enforces the word limit criterion.

**[OUTPUT FORMAT]** — Specifying the format prevents structural inconsistency. An ideal format instruction: *"Present the feedback as 2–3 short paragraphs. Paragraph 1: specific strength. Paragraph 2: the improvement area with one actionable suggestion. Paragraph 3: encouraging closing. No bullet points. No technical grading language."*

**[LOOP INSTRUCTION]** — The loop instruction must include a cap: *"If any criterion is answered No, identify which criterion failed, revise the feedback, and re-evaluate. Maximum 3 cycles. If all criteria are still not satisfied after 3 cycles, deliver the best current version and flag: 'Criterion [X] could not be satisfied — manual review recommended.'"*

**Design Note** — The best notes will connect the ROLE constraints directly to Problem B (tone) and the reflection criteria directly to Problem A (missing strengths). They will also note that removing the criteria would mean the agent self-approves its first draft — reintroducing both original problems.

**Alternative approaches** that are also valid:
- Using an internal checklist format instead of explicit Yes/No criteria (as long as all four elements are present)
- Adding a fifth criterion for personalisation (e.g., mentioning the student's name or essay topic in the feedback body)
- Referencing the student's specific essay content in the improvement suggestion rather than giving generic advice
