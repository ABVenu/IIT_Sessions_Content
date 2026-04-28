# Assignment Question QC Report
**Session:** Session10 — Advanced Prompt Engineering for Agents  
**Module:** Module 2  
**Date:** 2026-04-28

---

## Objective Questions QC

| Q No. | Type | Correct Option | Correct Option Relevant to Question? | Remarks |
|-------|------|----------------|--------------------------------------|---------|
| Q1 | MCQ (Easy) | B — "Break down a problem into step-by-step reasoning before arriving at a final answer" | Yes | Directly and accurately defines CoT prompting as taught in the session. Distractors are clearly wrong without being trick questions. Question is scenario-framed (Riya learning prompt engineering). |
| Q2 | MCQ (Easy) | C — "Let's think step by step." | Yes | Zero-Shot CoT trigger phrase is explicitly covered in the session. Distractor B correctly points to Few-Shot CoT, making it a useful learning contrast. Scenario-framed (Arjun designing a prompt). |
| Q3 | MCQ (Easy) | C — "Constraints — it specifies what the AI must NOT do or must limit" | Yes | Constraints component is accurately identified; the other options are real components of Structured Prompts described correctly, making distractors plausible but clearly wrong in this context. Scenario-framed (Meera building a financial agent). |
| Q4 | MCQ (Easy) | B — "Clarity, Intent, Constraints, Output Specification" | Yes | CICO expansion is taken directly from the session content. Distractors A, C, D use realistic-sounding but fabricated expansions. Scenario-framed (Dev evaluating his agent prompt). |
| Q5 | MCQ (Moderate) | B — "The prompt violates best practices by using negative instructions and lacks a specific Role, Output Format, and clear Task" | Yes | Covers two best practices simultaneously (negative instructions + structural gaps), appropriate for moderate difficulty. Scenario-framed (Tanvi's customer support agent). Distractors are clearly incorrect but each addresses a real misconception. |
| Q6 | MCQ (Moderate) | C — "40–50%" | Yes | Stat is directly quoted from the session (GPT-4 CoT accuracy improvement research). Numeric distractors are plausible without being ambiguous. Scenario-framed (Karan justifying learning to team lead). |

---

## Objective MSQ Questions QC

| Q No. | Type | Correct Options | Correct Options Relevant to Question? | Remarks |
|-------|------|-----------------|---------------------------------------|---------|
| Q7 | MSQ (Moderate) | A, B, D, E | Yes | All four correct options are valid CoT triggers covered in the session. Distractor C ("shortest possible answer") is clearly the anti-CoT instruction — logical and unambiguous wrong choice. Scenario-framed (Sahil designing a financial agent). |
| Q8 | MSQ (Moderate) | A, B, D, E | Yes | All five best practices tested are directly from the session's Best Practices section. Distractor C ("change multiple components at once") directly contradicts the Iterative Refinement principle — clear and unambiguous. Scenario-framed (Deepika reviewing agent practices). |
| Q9 | MSQ (Hard) | A, B, C, E | Yes | Scenario closely mirrors the session's business analyst agent example. Each correct option maps to a specific technique (role anchoring, CoT, Python f-strings/placeholders, constraints). Distractor D is the only incorrect statement and directly tests whether students understand the value of Output Format. Scenario-framed (Rohan building BI agent). |
| Q10 | MSQ (Hard) | A, B, C, E | Yes | Tests nuanced understanding of Iterative Refinement. Each correct option maps to a specific principle from the 4-step loop. Distractor D ("rewrite entire prompt at once") is the most common student mistake and is a direct violation of the one-change-at-a-time rule. Scenario-framed (Nisha improving her agent prompt). |

---

## Subjective Question QC

| Q No. | Type | Difficulty | Submission Instructions Clear? | Dataset / External Resource Needed? | Remarks |
|-------|------|------------|-------------------------------|-------------------------------------|---------|
| Q1 | Coding Implementation (Python) | Medium | Yes — single `.py` file submission via code editor/answer box in LMS | No external dataset needed; all inputs are defined inline by the student as string variables | Question is creative and applied — students must design a complete agent prompt system (not just recall definitions). Covers all three major techniques (Structured Prompt, CoT, Reasoning Prompt) in one task. Three agent options are provided so students can choose based on interest. The "Demonstration" section tests reusability of the function. Ideal solution and alternative approaches are provided in Answer Explanation. Difficulty is appropriately medium — guided enough to be achievable, open-ended enough to require real thinking. |

---

## Overall QC Summary

| Category | Count | Status |
|----------|-------|--------|
| Easy MCQs | 4 | Pass — all scenario-framed, correct answers verified against session content |
| Moderate MCQs | 2 | Pass — both scenario-framed with plausible distractors |
| Moderate MSQs | 2 | Pass — correct option sets verified, distractors are clear misconceptions |
| Hard MSQs | 2 | Pass — scenario-based, each option maps to a specific session concept |
| Subjective (Coding) | 1 | Pass — medium difficulty, clear submission instructions, no external dataset required, creative applied question |
| **Total** | **11** | **All Pass** |
