# Subjective Assignment — Advanced Prompt Engineering for Agents

---

## Q1 (Practical Coding Task | Medium Difficulty)

### The Prompt Engineer's Toolbox

You have just learned the three most powerful advanced prompting techniques: **Chain-of-Thought (CoT)**, **Structured Prompts**, and **Reasoning Prompts**. Now it is time to move from understanding to building.

Your task is to build a **Python-based Prompt Builder** for a real-world AI agent use case of your choice from the list below:

**Choose ONE agent to build a prompt for:**
- A **Mock Interview Agent** — helps students prepare for data/AI job interviews by asking questions and giving structured feedback
- A **Code Review Agent** — reviews a Python code snippet and provides feedback on bugs, readability, and improvements
- A **Product Launch Advisor Agent** — evaluates whether a new product idea is ready to launch, giving a GO/NO-GO recommendation

---

### What You Must Build (in a single Python file):

**Part 1 — Structured Prompt Builder Function**

Write a Python function called `build_agent_prompt(...)` that:
- Accepts at least **2 dynamic input parameters** relevant to your chosen agent (e.g., user background, product description, code snippet)
- Constructs a complete **Structured Prompt** using all **5 components** as separate variables:
  - `role` — Give the agent a name and at least 2 specific personality traits
  - `task` — One clear sentence defining the agent's deliverable
  - `instructions` — At least **4 numbered steps** that embed **Chain-of-Thought reasoning** (the agent must follow these steps before responding)
  - `constraints` — At least **3 guardrails** written as positive instructions (what the agent MUST do, not what it must NOT do — apply Best Practice #2)
  - `output_format` — Clearly specify sections, headers, or structure of the expected response
- Combines all components using an **f-string** into a single `full_prompt` string
- Returns `full_prompt`

**Part 2 — Reasoning Prompt Section**

Inside the same file, write a **separate string variable** called `reasoning_prompt` that demonstrates one of the three Reasoning Prompt types (Comparison, Causal, or Decision-Making) — relevant to your agent's domain. This should be a standalone prompt (not inside the function), showing criteria-based evaluation and a request for a final recommendation.

**Part 3 — Demonstration**

At the bottom of the file:
- Call `build_agent_prompt(...)` with **two different sets of inputs** (simulate two different users or scenarios)
- Print both outputs with clear separator lines
- Add a `print` statement that outputs the **character count** of each generated prompt (for token cost awareness)

---

### Example Output (for reference — your output will differ based on your chosen agent):

```
============================================================
AGENT PROMPT — Scenario 1
============================================================
[Full assembled prompt with all 5 components visible]
Prompt length: 1842 characters

============================================================
AGENT PROMPT — Scenario 2
============================================================
[Full assembled prompt with different inputs injected]
Prompt length: 1796 characters
```

---

### Submission Instructions

- Code all the parts mentioned above in VS Code in a single `.py` file named `prompt_builder.py`
- Run the code and verify both scenario outputs are printed correctly with character counts
- Then submit the code in the code editor / answer box in the LMS

---

### Answer Explanation (Ideal Solution Walkthrough)

**What a high-quality solution looks like:**

```python
# prompt_builder.py
# AI Agent Prompt Builder — Mock Interview Agent example

def build_agent_prompt(candidate_background, target_role):
    
    role = """You are Riya, a sharp and encouraging technical interview coach 
    with 12 years of experience preparing candidates for data and AI roles 
    at top Indian tech companies. You are known for asking precise, 
    scenario-based questions and giving actionable, constructive feedback."""
    
    task = f"Conduct a focused mock interview for a candidate targeting a {target_role} role and provide structured feedback on their responses."
    
    instructions = """Follow this process for each interview question:
    Step 1: Ask one scenario-based question relevant to the target role — not a theoretical definition question.
    Step 2: After the candidate responds, identify the strongest point in their answer.
    Step 3: Identify the one biggest gap or missing concept in their answer.
    Step 4: Give specific, actionable advice on how to improve that answer.
    Step 5: Rate the response on a scale of 1–5 with a one-line justification."""
    
    constraints = """Interview Guidelines:
    - Ask one question at a time — wait for the candidate's response before proceeding.
    - Frame all feedback constructively and encouragingly — treat the candidate as capable and motivated.
    - Ground every piece of feedback in a specific skill or concept, not a vague "be more detailed."
    - Keep each feedback section under 100 words.
    - If the candidate's answer is completely off-track, guide them with one Socratic hint before revealing the correct direction."""
    
    output_format = """Structure each exchange as:
    **Question:** [Your scenario-based interview question]
    **Candidate's Strongest Point:** [1 sentence]
    **Gap Identified:** [1 sentence]
    **Improvement Advice:** [2–3 actionable sentences]
    **Score:** [X/5] — [One-line justification]"""
    
    full_prompt = f"""
    {role}
    
    Task: {task}
    
    {instructions}
    
    {constraints}
    
    {output_format}
    
    Candidate Background: {candidate_background}
    Target Role: {target_role}
    """
    
    return full_prompt


# Part 2 — Reasoning Prompt (Decision-Making type)
reasoning_prompt = """
I am preparing for interviews for two different roles — Data Analyst and ML Engineer.
I have 6 months to prepare and can dedicate 2 hours per day.
My background: BCom graduate, 1 year experience in Excel-based data reporting, 
completed a Python basics course.

Given these constraints (background, time, and preparation capacity), which role should I target first?

Reason through both options considering:
1. Skill gap to bridge for each role
2. Time required to reach interview-ready level
3. Availability of entry-level positions in India
4. Salary range at the entry level

Then give me a clear final recommendation with your reasoning.
"""

# Part 3 — Demonstration

separator = "=" * 60

prompt_1 = build_agent_prompt(
    candidate_background="BCom graduate, 2 years experience in sales analytics using Excel, completed Python basics course",
    target_role="Data Analyst"
)

prompt_2 = build_agent_prompt(
    candidate_background="B.Sc. Statistics, 1 year internship in data labelling, knows pandas and basic ML concepts",
    target_role="Junior ML Engineer"
)

print(separator)
print("AGENT PROMPT — Scenario 1")
print(separator)
print(prompt_1)
print(f"Prompt length: {len(prompt_1)} characters")

print()
print(separator)
print("AGENT PROMPT — Scenario 2")
print(separator)
print(prompt_2)
print(f"Prompt length: {len(prompt_2)} characters")
```

**Key things the solution demonstrates:**
- Each of the 5 Structured Prompt components is stored as a separate variable — easy to update individually
- The Role gives the agent a name ("Riya") and 3 specific traits — firmly anchored persona
- Instructions Steps 1–5 embed CoT reasoning directly — agent must follow them in sequence
- Constraints use positive framing ("frame all feedback constructively") not negative ("don't be mean")
- Output Format uses bold headers for consistent, readable structure
- The f-string injects dynamic inputs cleanly
- The reasoning prompt uses the Decision-Making type with defined criteria and a final recommendation demand
- Two different scenarios show the function's reusability

**Alternative approaches:**
- Could use a Python class with prompt components as attributes and a `generate()` method
- Could use a dictionary to store components and join them for more modular prompt management
- Could add a `refine_prompt()` function that implements the 4-step Iterative Refinement loop
