# Objective Assignment — Advanced Prompt Engineering for Agents

---

## Q1 (MCQ | Easy)

Riya is learning about prompt engineering and reads that Chain-of-Thought (CoT) prompting dramatically improves AI accuracy. What does Chain-of-Thought prompting specifically instruct the LLM to do?

A) Summarise the user's question before answering it  
B) Break down a problem into step-by-step reasoning before arriving at a final answer  
C) Skip intermediate steps and directly produce the most common pattern-matched answer  
D) Translate the prompt into multiple languages to find the best interpretation  

**Correct Answer:** B

**Explanation:**  
Chain-of-Thought (CoT) Prompting forces the LLM to reason through intermediate steps before giving a final answer — similar to a student "showing their work." This keeps each reasoning step on track and dramatically reduces errors.  
- A is incorrect: summarising the question is not CoT — CoT is about reasoning through the *answer*.  
- C is incorrect: that is exactly what basic (non-CoT) prompting does — CoT was invented to fix this.  
- D is incorrect: CoT has nothing to do with language translation.

---

## Q2 (MCQ | Easy)

Arjun wants to use Zero-Shot Chain-of-Thought prompting without giving the AI any examples. He wants to trigger step-by-step reasoning with just a phrase added to his prompt. Which of the following phrases achieves this?

A) "Give me the most concise answer possible."  
B) "Here is a solved example — now solve this:"  
C) "Let's think step by step."  
D) "You are a helpful AI assistant."  

**Correct Answer:** C

**Explanation:**  
Zero-Shot CoT uses a trigger phrase alone — no examples are needed. "Let's think step by step" is the classic Zero-Shot CoT trigger that instructs the model to reason sequentially before answering.  
- A is incorrect: asking for concise answers discourages step-by-step reasoning.  
- B is incorrect: providing a solved example is Few-Shot CoT, not Zero-Shot CoT.  
- D is incorrect: this is a Role instruction, not a CoT trigger.

---

## Q3 (MCQ | Easy)

In a Structured Prompt, there are five key components: Role, Task, Instructions, Constraints, and Output Format. Meera is building an agent that must never recommend stocks directly and must keep advice under 200 words. Which component of the structured prompt should contain these rules?

A) Role — it defines the AI's persona and expertise  
B) Task — it specifies what the AI is supposed to deliver  
C) Constraints — it specifies what the AI must NOT do or must limit  
D) Output Format — it specifies how the response should look  

**Correct Answer:** C

**Explanation:**  
Constraints are the "guardrails" of a Structured Prompt. Rules like "never recommend direct stocks" and "keep advice under 200 words" are restrictions on the AI's behaviour — they belong in the Constraints section.  
- A is incorrect: Role defines who the AI is (e.g., "You are a senior financial advisor"), not what it cannot do.  
- B is incorrect: Task states the specific job to be done, not the limits.  
- D is incorrect: Output Format specifies structure and style (e.g., bullet points, sections), not behavioural limits.

---

## Q4 (MCQ | Easy)

After building his first agent prompt, Dev wants to evaluate whether it is ready to use. His instructor teaches him a quick evaluation checklist. What does the CICO Framework stand for?

A) Context, Instructions, Commands, Output  
B) Clarity, Intent, Constraints, Output Specification  
C) Content, Implementation, Complexity, Optimisation  
D) Character, Instruction, Concept, Operation  

**Correct Answer:** B

**Explanation:**  
The CICO Framework is a 4-point checklist for evaluating prompt quality: **C**larity (is every instruction crystal clear?), **I**ntent (does the prompt communicate the goal?), **C**onstraints (are guardrails in place?), **O**utput Specification (is the format and length defined?).  
- A, C, and D are incorrect: they are fabricated expansions that do not match the framework taught in the session.

---

## Q5 (MCQ | Moderate)

Tanvi is building a customer support AI agent. Her system prompt reads: *"You are an AI. Don't give wrong answers. Don't be rude. Help users with their problems."* After deployment, the agent gives inconsistent responses — sometimes too verbose, sometimes too brief — and occasionally goes off-topic. Based on Structured Prompt and Best Practices principles, what is the PRIMARY reason her prompt fails?

A) The prompt is too short — it needs to be at least 500 words long to work properly  
B) The prompt violates best practices by using negative instructions and lacks a specific Role, Output Format, and clear Task  
C) The AI model is not powerful enough to follow short instructions  
D) The prompt should be written in Python code, not plain English  

**Correct Answer:** B

**Explanation:**  
Tanvi's prompt has two compounding problems: (1) It uses negative instructions ("Don't give wrong answers", "Don't be rude") instead of positive ones — best practice says to write what the AI *should* do, not what it shouldn't. (2) The Role is just "You are an AI" — there are no specific traits, no Task clarity, no Output Format, and no Constraints that positively guide the behaviour. These are the root causes of inconsistency.  
- A is incorrect: prompt quality is about structure and specificity, not word count.  
- C is incorrect: even powerful models produce inconsistent outputs with vague prompts.  
- D is incorrect: system prompts are written in natural language and passed as strings.

---

## Q6 (MCQ | Moderate)

Karan is trying to convince his team lead to invest time in learning advanced prompt engineering. He wants to cite research on the impact of Chain-of-Thought prompting. According to the session, what is the approximate improvement in accuracy on logical and math problems when CoT prompting is applied to models like GPT-4?

A) 10–15%  
B) 25–30%  
C) 40–50%  
D) 70–80%  

**Correct Answer:** C

**Explanation:**  
Research on GPT-4 and similar large language models shows that adding a CoT trigger like "Let's think step by step" improves accuracy on logical and math problems by approximately **40–50%**. This is because forcing step-by-step reasoning prevents the model from pattern-matching to shallow, common answers and instead commits it to logically correct intermediate steps.  
- A and B underestimate the documented improvement.  
- D overstates the improvement — 70–80% is not supported by the research cited in the session.

---

## Q7 (MSQ | Moderate)

Sahil is designing a system prompt for an AI financial planning agent. He wants to embed Chain-of-Thought reasoning directly into the agent's instructions so it always reasons carefully before answering. Which of the following phrases or instructions are valid ways to trigger CoT reasoning in a prompt? **Select all that apply.**

A) "Let's think step by step."  
B) "Walk me through your reasoning before giving a final answer."  
C) "Give me the shortest possible answer without any explanation."  
D) "Break this problem down first, then provide your recommendation."  
E) "Think carefully before answering."  

**Correct Answer:** A, B, D, E

**Explanation:**  
All four — A, B, D, and E — are valid CoT triggers. They instruct the model to reason before concluding. Each triggers the "show your work" behaviour in slightly different ways:  
- A ("Let's think step by step") is the classic Zero-Shot CoT phrase.  
- B ("Walk me through your reasoning") explicitly demands visible reasoning.  
- D ("Break this problem down first") instructs decomposition before answering.  
- E ("Think carefully before answering") is a gentler CoT trigger.  
- C is incorrect: asking for the "shortest possible answer without explanation" actively suppresses CoT reasoning — it is the opposite of what CoT intends.

---

## Q8 (MSQ | Moderate)

Deepika is reviewing a set of Agent Prompt Design Best Practices before finalising her AI agent. Which of the following are recommended best practices for designing agent prompts, as covered in the session? **Select all that apply.**

A) Use positive instructions ("Give specific answers") instead of negative ones ("Don't be vague")  
B) Anchor the AI's persona with 2–3 specific personality traits in the Role, not just "You are an AI"  
C) If a prompt fails, change the Role, Constraints, and Output Format all at once to fix problems faster  
D) Specify what the agent should do in edge cases (e.g., when a question is outside its expertise)  
E) Place the most critical instruction at the very end of the prompt, as LLMs pay more attention to the end  

**Correct Answer:** A, B, D, E

**Explanation:**  
- A is correct: LLMs sometimes over-focus on negated concepts. Positive instructions are clearer and more effective.  
- B is correct: A vague role like "You are an AI" produces inconsistent behaviour. Specific traits ("patient, encouraging, specialised in...") make the persona consistent.  
- C is incorrect: this violates Iterative Prompt Refinement principles. You should change only ONE component at a time so you know which change actually fixed the problem.  
- D is correct: always adding fallback instructions prevents the agent from hallucinating answers outside its scope.  
- E is correct: research shows LLMs pay more attention to instructions at the beginning and end of a prompt — the most important instruction should be placed last.

---

## Q9 (MSQ | Hard)

Rohan is building a Business Intelligence AI agent in Python that evaluates startup ideas and gives GO/NO-GO recommendations. He wants to apply all the advanced techniques from this session. His agent prompt includes the following elements:

- A named persona: *"You are Priya, a Business Intelligence Analyst specialising in Indian early-stage startups."*
- A 6-step numbered reasoning process embedded in the prompt
- A constraint: *"Do not give a vague answer — your recommendation must be clearly GO or NO-GO."*
- An output format with bold headers for each step
- A Python placeholder `{startup_description}` replaced via `.format()` in code

Which of these design decisions are **correctly aligned** with the advanced prompt engineering techniques covered in the session? **Select all that apply.**

A) Naming the persona ("Priya") and giving her a specific specialisation anchors the role firmly, producing more consistent agent behaviour  
B) The 6-step numbered reasoning process embeds Chain-of-Thought directly into the agent's system prompt  
C) Using a Python placeholder `{startup_description}` makes the prompt reusable for any startup, not just one  
D) Bold headers in the output format are unnecessary and add no value to the agent's consistency  
E) The constraint "clearly GO or NO-GO" prevents vague, uncommitted outputs from the agent  

**Correct Answer:** A, B, C, E

**Explanation:**  
- A is correct: best practices say to anchor the persona with 2–3 specific details; a named, specialised role produces far more consistent outputs than "You are an AI."  
- B is correct: embedding a numbered step-by-step reasoning process directly in the system prompt is exactly how CoT is applied inside agent prompts.  
- C is correct: using placeholders like `{startup_description}` with `.format()` or f-strings makes the prompt dynamically reusable for any input — a core Python prompt design pattern covered in the session.  
- D is incorrect: specifying output format (including bold headers) is one of the five building blocks of a Structured Prompt. It ensures every evaluation follows the same readable, comparable structure.  
- E is correct: the constraint forces a definitive answer and prevents the agent from producing the vague "it depends" responses common in under-constrained prompts.

---

## Q10 (MSQ | Hard)

Nisha is working on improving her AI agent's prompt using the Iterative Prompt Refinement process. She runs her initial prompt and receives a generic, unfocused output that could apply to any situation. She now wants to systematically fix it. Which of the following statements about Iterative Prompt Refinement are **TRUE**? **Select all that apply.**

A) You should change only ONE component of the prompt at a time between test runs, so you know exactly which change improved the output  
B) If the AI's output is too generic and lacks context-specific insight, the correct diagnosis is to add more Role and Context to the prompt  
C) If the AI's output has the wrong structure (e.g., paragraphs instead of bullet points), the correct fix is to add or improve the Output Format specification  
D) Rewriting the entire prompt from scratch at once is the most efficient way to resolve multiple quality problems simultaneously  
E) Keeping a log of what you changed and how the output improved helps build long-term intuition for prompt design  

**Correct Answer:** A, B, C, E

**Explanation:**  
- A is correct: changing only one component at a time is the cardinal rule of Iterative Prompt Refinement — it isolates the cause-and-effect relationship between the prompt change and the output quality change.  
- B is correct: a generic, context-free output signals that the AI has no Role or background to anchor its reasoning — adding more specific Role/Context is the correct diagnosis for "too generic" outputs.  
- C is correct: wrong output structure (format mismatch) is a direct sign that the Output Format specification is missing or unclear — fixing that specific component is the right move.  
- D is incorrect: rewriting the entire prompt at once violates the core principle of Iterative Refinement. If everything changes at once, you cannot identify which fix actually worked, making future iterations harder.  
- E is correct: tracking iterations builds "prompt design intuition" — the session explicitly recommends maintaining an iteration log for this reason.
