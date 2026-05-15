# Assignment — Subjective (Session: Prompt Engineering)

**Difficulty:** Medium  
**Type:** Applied design + short research (document)

---

## Scenario

You volunteer for a college cultural fest. The fest desk gets repetitive messages: event timings, venue map doubts, refund policy for cancelled shows, and last-minute performer changes. You want a **single AI assistant** that can answer students consistently, stay on-topic, and avoid making up timings or policies.

**Task:** Design **one complete agent-style system prompt** (as plain text) for this assistant **and** justify your design choices in a short companion write-up.

### What your system prompt must include (all mandatory)

1. **Role:** Name the assistant and give **2–3** personality traits suited for stressed students.  
2. **Scope:** What it **will** handle and what it **must refuse** or escalate (be explicit).  
3. **Workflow (CoT-style):** At least **4 numbered steps** the assistant must follow **before** answering a student query (example steps might include triage, fact priority, tone check—choose what fits your scenario).  
4. **Self-correction / quality gate:** A clear **3-stage** structure (**Generate → Critique → Rewrite**) *or* an equivalent explicit checklist the assistant must run on its own draft (either is acceptable if it is staged and measurable).  
5. **Constraints:** At least **3** guardrails (e.g., no fabricated schedules, no legal promises, how to handle missing official info).  
6. **Output format:** Specify exactly how every final reply should be structured (sections/headings/bullets—your choice, but must be unambiguous).

### What the companion write-up must explain (mandatory)

- Why you split responsibilities the way you did between **scope** vs **constraints**.  
- One paragraph on **when your assistant should stop answering from memory** and what it should do instead (connect this to accuracy risks you learned about with LLMs).  
- **One** external reference you consulted while designing (any credible page: university helpdesk guidelines, event ops blog, prompting reference—cite title + URL).  

---

## Submission instructions (Case B — document style)

- Create a **Google Doc** in your Google Drive.  
- Suggested folder path (for your own organisation): **Module3 → Session36** (create if needed).  
- Write clearly: paste the **full system prompt** in a monospace or quoted block, then your write-up with headings. Add **images** only if they genuinely help (e.g., a simple flow sketch or screenshot of an official schedule page you relied on—**no** personal data).  
- When finished, click **Share** and set access to **Anyone with the link can view**.  
- Submit **only the Google Doc link** in the LMS answer field.

---

## Answer Explanation (for Assess platform)

**Ideal solution characteristics**

- **Role** is concrete (name + traits), not generic “helpful AI.”  
- **Scope** distinguishes fest info vs medical/legal/finance topics; includes an escalation path (“direct to official notice / link / human desk”).  
- **Numbered workflow** forces triage and reduces rushed wrong answers; steps should reflect real desk work (clarify intent, check if info is official vs rumor, etc.).  
- **Self-correction** must be staged with explicit criteria (e.g., “check: timings sourced? policy cited? tone calm?”) and a rewrite rule if checks fail.  
- **Constraints** should explicitly block hallucinated schedules/policies and forbid overclaiming.  
- **Output format** should be repeatable (e.g., TL;DR → verified facts → next steps → disclaimer).  
- **Write-up** should show applied understanding: scope vs constraints, memory vs verified info, plus a real citation.

**Alternative approaches:** Students may use a table for the output format, or embed a mini “if missing info, ask one clarifying question” rule—acceptable if guardrails remain strict.

**Sample outline (not unique):**  
Role: “Meera…”; Scope: timings/venues/policies only from official fest channels; Steps: classify query → retrieve official fact priority → draft → self-check → respond; Self-correction stages with checks for fabricated details; Constraints: never invent performer times, never promise refunds without policy text; Output: sections for Answer / Sources / If unsure; Write-up cites an official student-events page or credible prompting guide.

---

**End of subjective assignment**
