# Mastering Prompt Engineering

## What We Covered So Far & What's Coming Next

In our last session, we took a deep dive into the **world of LLMs (Large Language Models)** — we learned how classical machine learning models like regression and decision trees struggle with language tasks. We understood how neural networks are built layer by layer, how LLMs learn from vast chunks of internet data during **pre-training**, and why they generate text probabilistically instead of looking up stored answers. We also explored key concepts like **tokens**, **context windows**, **temperature**, and **hallucinations** — the very building blocks that explain how and why an LLM behaves the way it does.

Now that you understand *what* an LLM is and *how* it generates text, the next powerful question is: **how do you communicate with it effectively?** Simply typing a question and hoping for a good answer is like hiring a brilliant consultant and giving them no brief. This session is entirely about **Prompt Engineering** — the art and science of giving the AI the right instructions to get exactly what you need.

![Vague vs specific prompts — clear, detailed instructions get reliable outputs; fuzzy wishes do not](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module2/session10/session10-vague-vs-specific-prompt.png)

**In this session, you will learn:**
- The difference between **System Prompts** and **User Prompts** and why both matter
- What **Zero-Shot** and **Few-Shot** prompting are and when to use each
- How **Chain-of-Thought (CoT) prompting** forces an AI to reason step by step
- How to build professional **Prompt Templates** using a structured five-component framework
- How to design **Self-Correction Prompts** that make an AI check and fix its own output
- How **Iterative Prompting** lets you refine a response over multiple rounds to perfection
- How to design a complete **Agent Prompt Flow** that works reliably without you being present

---

## System Prompts vs User Prompts

**Official Definition:** In any LLM-based interaction, a **System Prompt** is a set of persistent, background instructions that define the AI's role, personality, and rules for the entire conversation. A **User Prompt** is the real-time message sent by the user in each interaction.

**In Simple Words:** Think of a restaurant. Before opening, the owner briefs all staff: "We serve North Indian food only, always be polite, and if something is unavailable, suggest a similar item." That briefing is the **System Prompt** — it shapes how every staff member behaves for every customer interaction.

When a customer walks in and says "I want a paneer butter masala" — that is the **User Prompt**. The customer does not know about the backstage rules. They just give their request and get a response that is already shaped by those rules.

**Real-Life Example:** When you use a banking chatbot and it says "I can only help with banking-related queries" — that boundary was not set by you. It was set in the System Prompt by the bank's tech team. Your messages are the User Prompts; the chatbot's consistent personality and limits come from the System Prompt.

### How System Prompts and User Prompts Work Together

- **System Prompts** are sent to the LLM *before* the conversation begins — they set the stage, define the persona, establish constraints, and tell the AI what it is and what it is not allowed to do.
- **User Prompts** are the live, back-and-forth messages in the conversation — every time you type something to an AI, that is a User Prompt.
- **The AI always sees both** — the System Prompt stays active throughout the session, and every User Prompt is interpreted *within the context* of that system instruction.

### Writing an Effective System Prompt

A well-designed System Prompt has three key ingredients:

| Ingredient | What It Does | Example |
|---|---|---|
| **Persona** | Defines who the AI is — role, name, personality traits | "You are Riya, a warm and patient HR assistant at a logistics company." |
| **Scope** | Defines what the AI *will* and *will not* handle | "Only answer questions related to HR policies, leave applications, and payroll. For all other queries, politely redirect." |
| **Tone & Rules** | Defines how the AI communicates | "Always use simple language. Never give legal advice. When unsure, say 'I will check and get back to you.'" |

```python
# A complete System Prompt for a learning assistant agent

system_prompt = """
You are Arjun, a friendly and patient academic mentor for undergraduate students 
in India who are new to the world of AI and technology.

Your job is to explain concepts simply, using everyday Indian examples — 
from cricket, chai, and local markets to Bollywood and board exams.

Scope:
- Only answer questions related to AI, machine learning, and prompt engineering.
- If asked about unrelated topics, say: "That's outside my area — let me stay 
  on our AI journey together!"

Rules:
- Never use jargon without immediately explaining it in simple words.
- Always end explanations with one practical thing the student can try.
- If a student says they are confused, respond with: "No problem! Let's try a 
  different angle..." and use a fresh analogy.
"""
```

**How the code works:**
- The `system_prompt` variable holds the full set of background rules — this is sent to the LLM API *before* the student's first message
- The **Persona** (Arjun, patient academic mentor) ensures every response has the same warm, consistent tone — no matter what the student asks
- The **Scope** rules act as an automatic filter — if someone asks about stock markets, the agent stays on topic rather than going off-track
- The `"If confused"` edge case instruction ensures the agent never leaves a struggling student with a cold response

### System Prompt vs User Prompt — Side by Side

```
System Prompt (set once, before the conversation):
"You are a recipe assistant. Only suggest vegetarian Indian recipes. 
Always list ingredients first, then steps. Keep all recipes under 30 minutes."

---

User Prompt (sent each time by the user):
"What can I make for breakfast with leftover rice?"

---

AI Response (shaped by both):
"Great question! Here's a quick Poha-style rice recipe using leftover rice:

Ingredients: Leftover rice (1 cup), onion (1 small), mustard seeds, 
curry leaves, green chilli, turmeric, lemon juice, salt.

Steps:
1. Heat oil, add mustard seeds until they splutter.
2. Add onions and chilli — cook until soft (3 min).
3. Add rice, turmeric, and salt — mix well (2 min).
4. Squeeze lemon juice, add curry leaves. Serve hot.
Total time: 10 minutes."
```

The response is vegetarian, Indian, lists ingredients first, and is under 30 minutes — all because of the System Prompt, not the User Prompt.

### Behind the scenes: apps, hidden system messages, and institute context

**Official idea:** In production, an **application** (a website or chatbot) usually sends more than your typed line to the model: it combines a **system prompt**, your **user message**, and sometimes extra **organisation (institute) context** in one request.

**In simple words:** You only see the box you type in. The server may quietly attach rules you did not write and short facts about your school or company so answers stay on-brand and accurate.

**What often happens in an institute setup:** The organisation builds a small site or bot that sends the **student’s question** to the LLM API **together with** the system prompt and **institute context** drawn from that organisation’s own material.

**ChatGPT vs the LLM:** **ChatGPT** is the user-facing **application**; it is not the language model by itself. Your text is a **user** message that gets combined internally with a confidential **system** message before the call reaches the underlying model — which is why you cannot see ChatGPT’s full system prompt.

**Note for later:** Pulling live facts from documents into the prompt (**RAG** — retrieval-augmented generation) goes one step beyond static institute context. That pattern is covered in a **later session**.

> **[ Student Activity ]**
>
> **Write Your First System Prompt**
>
> Think of a role you would want an AI assistant to play in your real life — a study buddy, a fitness coach, a small business advisor, or a creative writing partner.
> - Write a System Prompt for that assistant with all three ingredients: **Persona**, **Scope**, and **Tone & Rules**.
> - Keep it to 5–8 lines.
> - Swap with the person next to you. Can they tell — just from reading your System Prompt — what this assistant will *always* do and *never* do?
>
> *Instructor note: Pick 2–3 students to read their System Prompts aloud. Point out which part defines persona, which defines scope, and which defines tone. A missing scope is the most common gap — help students add it.*

---

## Zero-Shot vs Few-Shot Prompting

Now that you know how System and User Prompts work, the next key concept is *how much context* you give the AI inside a User Prompt itself.

**Official Definition:**
- **Zero-Shot Prompting** is asking the AI to perform a task with no examples given — just the instruction itself.
- **Few-Shot Prompting** is providing one or more worked examples *inside the prompt* before asking the AI to solve your actual task, so the AI can learn the pattern from those examples.

**In Simple Words:** Imagine you are asking a new assistant to format reports in a specific way. Zero-shot is saying "Please format this report" — the assistant figures out the format on their own. Few-shot is saying "Here are two already-formatted reports — now please format this new one in the same way."

**Real-Life Example:** In school, zero-shot is a teacher saying "Write an essay on water conservation" — you figure out the format yourself. Few-shot is the teacher sharing two sample essays first and saying "Now write yours in this style." The sample essays guide your approach immediately.

### Zero-Shot Prompting — When It Works

Zero-shot works best when:
- The task is **simple, factual, or commonly known** — the AI has seen enough similar examples in training
- The **format and output are obvious** — no special structure needed
- You need a **quick answer** and precision is not critical

```
Zero-Shot Example:

Prompt: "Translate this sentence to Hindi: The library opens at 9 AM."

AI Response: "पुस्तकालय सुबह 9 बजे खुलता है।"
```

```
Zero-Shot Example (slightly complex):

Prompt: "List 3 benefits of regular exercise for a student."

AI Response:
1. Improves focus and concentration during study hours.
2. Reduces stress and anxiety before exams.
3. Builds stamina and keeps energy levels consistent throughout the day.
```

These are both zero-shot — no examples given, just the instruction. The AI handles them well because they follow common patterns it has seen before.

### Where Zero-Shot Falls Short

Zero-shot fails when:
- The **output format is non-standard** — the AI does not know your specific format preference
- The task involves **your unique context** — the AI has no way to infer your company's tone, your product's details, or your personal style
- The task requires **consistent structure** across multiple outputs — each response might look slightly different

### Few-Shot Prompting — Adding Examples for Clarity

Few-shot prompting solves these gaps by providing **worked examples inside the prompt**. The AI reads those examples, identifies the pattern, and applies that exact pattern to your new input.

```
Few-Shot Example:

I want to write product taglines in a specific style. Here are two examples:

Product: Air purifier
Tagline: "Breathe what you deserve — pure, clean, and effortless."

Product: Reusable water bottle
Tagline: "Stay hydrated, stay kind — to yourself and the planet."

Now write a tagline for this product:
Product: Noise-cancelling headphones
Tagline: [AI fills this in]

AI Response:
"Your world. Your soundtrack. Zero interruptions."
```

The AI matched the structure — short, two-part tagline, poetic tone — purely from the two examples. No instruction about structure was needed.

### Zero-Shot vs Few-Shot — A Quick Comparison

| Aspect | Zero-Shot | Few-Shot |
|---|---|---|
| **Examples given** | None | 1 to 5 examples |
| **Best for** | Simple, standard tasks | Custom formats, specific styles, unusual patterns |
| **AI relies on** | Its training data patterns | The examples you provided |
| **Risk** | Output format may vary | Adds length to the prompt |
| **Use in agents** | Quick lookups, simple Q&A | Output formatting, classification, tone-matching |

> **[ Student Activity ]**
>
> **Same Task, Two Approaches**
>
> **Task:** Write a short "customer testimonial" for a fictional online tutoring app called "StudyPath."
>
> - **Round 1 (Zero-Shot):** Give the AI only this instruction: *"Write a customer testimonial for an online tutoring app called StudyPath."* Note the style and format you get.
> - **Round 2 (Few-Shot):** Before the same instruction, provide two example testimonials in a specific style — short, enthusiastic, mentions one specific feature.
> - Compare the two outputs. How much did the examples change the style and structure?
>
> *Instructor note: This activity makes the difference concrete and observable. Point out how few-shot constrains the AI's creative choices toward a reliable, predictable format — which is exactly what agents need.*

---

## Chain-of-Thought Prompting

Now that you understand the basics of prompting, let's explore one of the most powerful techniques in advanced prompt engineering — **Chain-of-Thought (CoT) Prompting**.

**Official Definition:** Chain-of-Thought (CoT) Prompting is a technique where you instruct or demonstrate to an LLM to break down a problem into intermediate reasoning steps before arriving at the final answer, rather than jumping directly to a conclusion.

**In Simple Words:** Imagine you ask a student "What is 17 × 8?" If the student just blurts out "136" without showing any working, you have no way to verify the reasoning. But if they say "17 × 8 = 17 × 4 × 2 = 68 × 2 = 136," they are showing their work step by step — and each step keeps the next step on track.

**Real-Life Example:** Think of a doctor diagnosing a patient. A bad doctor says "You have fever, take paracetamol" after 2 seconds. A good doctor says "Let me check your symptoms one by one — you have fever since 3 days, your throat is red, you have body ache — this looks like viral fever, not bacterial, so antibiotics won't help. I recommend rest, fluids, and paracetamol." The second doctor is doing Chain-of-Thought reasoning.

![Chain-of-Thought prompting — step-by-step reasoning keeps the model on track instead of jumping to a shallow answer](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module2/session10/session10-chain-of-thought-flow.png)

### Why CoT Improves Accuracy

- **LLMs are next-token predictors.** They predict the next word based on patterns. When you ask for a direct answer, the model picks the most common pattern — which is often a shallow, popular answer, not the correct one.
- **Forcing step-by-step thinking** makes the model "commit" to intermediate correct steps, and each step acts as a constraint on the next. This reduces errors on many reasoning-style tasks.
- **From class:** Trigger phrases such as *"Let's think step by step"* or *"Show your reasoning first"* encourage visible intermediate steps before the final answer. The instructor also pointed to **Prompting Guide** ([promptingguide.ai](https://www.promptingguide.ai)) as a useful reference for chain-of-thought patterns and examples.

### How CoT Connects to Zero-Shot and Few-Shot

CoT works hand in hand with the two prompting styles you already know:

- **Zero-Shot CoT** — You add a trigger phrase and the AI reasons on its own without any examples: *"Let's think step by step," "Walk me through your reasoning," "Break this problem down first."*
- **Few-Shot CoT** — You show 1–2 solved examples *with the reasoning visible*, then ask your question. The AI mirrors the same structured reasoning pattern from your examples.

```
Zero-Shot CoT Example:

Prompt: A train leaves Mumbai at 6 AM at 80 km/h. Another leaves Pune 
(150 km away) at 8 AM at 100 km/h towards Mumbai. When do they meet? 
Let's think step by step.
```

```
Few-Shot CoT Example:

Example:
Q: A shopkeeper buys apples at ₹10 and sells at ₹15. He sells 20 apples. What is the profit?
Reasoning: Cost = 20 × 10 = ₹200. Revenue = 20 × 15 = ₹300. Profit = ₹100.
A: ₹100.

Now solve:
Q: A vendor buys pens at ₹5, sells at ₹8, sells 50 per day. Daily profit?
Reasoning: [think step by step]
```

### Applying CoT in Agent Prompts

When you are building an AI agent, you often add CoT instructions directly into the **system prompt** so the agent always reasons carefully:

```python
# This is a system prompt for an AI agent that handles customer complaints

system_prompt = """
You are a customer support agent for an e-commerce company.

When a customer reports a problem, you MUST follow these steps before responding:
Step 1: Identify what the customer's core problem is.
Step 2: Check if this is a delivery issue, a product issue, or a payment issue.
Step 3: Based on the category, think about the best solution.
Step 4: Draft a response that is empathetic, clear, and offers a concrete next step.

Only respond after completing all 4 steps internally.
"""
```

**How the code works:**
- The `system_prompt` variable holds the agent's core instructions — this is sent to the LLM before every conversation
- The numbered steps force the agent to *categorise* the problem before answering — this prevents generic, unhelpful responses
- `"think about the best solution"` is a CoT trigger embedded in the workflow
- `"Only respond after completing all 4 steps internally"` ensures the model does not shortcut its reasoning

> **[ Student Activity ]**
>
> **Trigger the Thinking**
>
> You are given this basic prompt: *"Should I learn Python or SQL first for a data career?"*
> - **Part A (3 min):** Rewrite it as a **Zero-Shot CoT** prompt by adding one or two phrases that trigger step-by-step reasoning. Do not add any examples — just the trigger phrase.
> - **Part B (4 min):** Now write a **Few-Shot CoT** version. Create one solved example (with reasoning shown) before asking the main question.
> - Compare your Part A and Part B. Which one do you think would give the AI more useful guidance?
>
> *Instructor note: Ask 2 students to read their Zero-Shot versions. Show how different trigger phrases (e.g., "walk me through" vs "step by step") can produce slightly different reasoning styles.*

---

## Prompt Templates: The Structured Prompt

Chain-of-Thought gets the AI to reason better — but we also need to ensure the AI's output is *predictable and professional*. That is where **Structured Prompts (Prompt Templates)** come in.

**Official Definition:** A Structured Prompt is a prompt built using a defined template with specific components — typically Role, Task, Instructions, Constraints, and Output Format — to produce consistent and predictable responses from an LLM.

**In Simple Words:** Imagine you are filling a job application form. The form has separate boxes for your name, education, experience, and skills — because of this structure, every applicant fills in the same information in the same place. A Structured Prompt does the same thing for AI: it puts every piece of information in the right box so the AI knows exactly what is expected.

**Real-Life Example:** Think of a police FIR (First Information Report). It has a defined structure: Name of complainant, Date and time of incident, Location, Description of the event, Witnesses. Because of this structure, no important detail is missed. A Structured Prompt ensures no important instruction is missing from your AI request.

### The 5 Building Blocks of a Structured Prompt

| Component | What It Tells the AI | Example |
|-----------|---------------------|---------|
| **Role** | Who you are / what persona to adopt | "You are a senior financial advisor" |
| **Task** | What specific job needs to be done | "Analyse this mutual fund portfolio" |
| **Instructions** | How to do the task (step by step if needed) | "First check the risk level, then check returns, then suggest improvements" |
| **Constraints** | What NOT to do, or limits to follow | "Do not recommend direct stocks. Keep advice simple. Use no jargon." |
| **Output Format** | How the response should look | "Give me a 3-section report: Risk Summary, Performance Summary, Recommendations" |

![The five building blocks of a structured prompt — Role, Task, Instructions, Constraints, and Output Format](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module2/session10/session10-structured-prompt-five-components.png)

### A Fully Assembled Structured Prompt

Here is what all five components look like when combined into one ready-to-use prompt:

```
[ROLE]
You are a career counsellor with 15 years of experience helping students from 
non-technical backgrounds transition into the tech industry.

[TASK]
Recommend the top 3 career paths that match the student's profile.

[INSTRUCTIONS]
1. Understand the student's educational background.
2. Identify their top 2 interests from what they share.
3. Match these to realistic tech careers that don't require heavy coding.
4. Explain each career in simple, jargon-free language.

[CONSTRAINTS]
- Do NOT recommend careers requiring a CS degree.
- Keep each recommendation under 100 words.
- Do not use technical jargon without explaining it.

[OUTPUT FORMAT]
Career 1: [Name]
- What you will do: [2 sentences]
- Why it suits you: [1 sentence]
- Starting salary in India: [range]
Career 2: ... Career 3: ...

Student Background: BCom graduate, 2 years experience in sales.
Student Interests: Talking to people, organising data in Excel.
```

**Why this works:**
- The **Role** tells the AI what expertise and perspective to adopt — not generic advice, but experienced counsellor thinking
- The **Instructions** create a natural chain-of-thought — the AI *must* follow the 4 steps in sequence
- The **Constraints** act as guardrails — they prevent impractical or off-topic advice
- The **Output Format** ensures the result is always structured and immediately usable

> **[ Student Activity ]**
>
> **Build Your Own Structured Prompt**
>
> Think of a real task you would want an AI agent to help you with — from your own studies, your job, your college project, or your personal life.
> - Write all **5 components** for your prompt: Role, Task, Instructions, Constraints, Output Format.
> - Keep each component to 2–4 lines.
> - Once done, swap your prompt with the person next to you. Can they tell — just by reading your prompt — exactly what the AI should produce?
>
> *Instructor note: Pick 2–3 students to read their Role + Output Format aloud. Point out: a strong Role + clear Output Format is often what separates a good prompt from a bad one.*

---

## Self-Correction Prompts

You now know how to build a well-structured prompt. But here is the reality of working with AI in the real world — **even the best-structured prompt can sometimes produce a weak, incomplete, or vague answer**. The question is: what do you do about it?

The answer is to build the quality check *into the prompt itself* — using **Self-Correction Prompts**.

**Official Definition:** A self-correction prompt is a prompt that explicitly instructs the AI to verify, critique, and fix its own response within the same interaction, before delivering the final answer.

**In Simple Words:** You are not just asking the AI to answer — you are asking it to be its own quality checker. You say: *"Answer this, then check your own answer, then fix whatever is wrong."*

**Real-Life Example:** Think of a **bank loan officer**. Before approving a loan, they fill out a form. Then a second officer reviews the same form for errors before it goes for final approval. The second review is the self-correction step — the system catches mistakes before they become problems.

### Seeing the Difference — Without vs With Self-Correction

![Without reflection the model stops at a vague first draft; with reflection it checks criteria and produces specific, actionable steps](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module2/session11/session11-without-vs-with-reflection.png)

**Without Self-Correction:**
```
Prompt: Write a short description of a healthy morning routine for a beginner.

AI Response:
A healthy morning routine includes waking up early, exercising, and eating 
a good breakfast. Staying hydrated is also important.
```

This is too vague — "exercising" gives no guidance, "good breakfast" tells the beginner nothing practical.

**With Self-Correction:**
```
Prompt: Write a short description of a healthy morning routine for a beginner.

After writing your description, check:
- Does it have at least 4 specific, actionable steps?
- Is it simple enough for someone with no prior fitness habit?
- Does it include a time estimate for each step?

If any answer is No, rewrite it until all answers are Yes.
```

The AI now produces a detailed, time-stamped, beginner-friendly routine — because it was asked to *check its own work* against specific criteria.

### The Three-Stage Structure

A good self-correction prompt always has three distinct stages:

![Self-correction in three stages — generate a draft, critique gaps, then rewrite using that critique](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module2/session11/session11-self-correction-three-stages.png)

- **Stage 1 — Generate:** Ask the AI to produce an initial response to the task.
- **Stage 2 — Critique:** Ask the AI to review what it just wrote and identify what is missing, incorrect, or weak.
- **Stage 3 — Rewrite:** Ask the AI to produce a new, improved version based on its own critique.

Keeping these three stages **separate and explicit** is the key. If you merge them into one vague instruction like *"Write a perfect answer,"* the AI does not reliably apply all three stages.

### Self-Correction in Action

```
Prompt:
Stage 1 — Answer: Explain why sleep is important for students.
Stage 2 — Critique: What important facts, reasons, or details are missing?
Stage 3 — Rewrite: Fix all the gaps you identified.

---
Stage 1 (Initial): "Sleep is very important for students. It helps them feel rested."

Stage 2 (Critique): Too vague — missing: what happens in the brain, how many hours, 
consequences of sleep deprivation, and any practical advice.

Stage 3 (Improved): "Sleep is the brain's nightly 'Save' button — it processes and 
stores everything learned during the day. Students getting 7–9 hours retain 
information 40% better than those getting under 6. The practical rule: same bedtime 
every night — your brain learns your schedule and becomes more efficient at recovery."
```

The critique step is the engine — once the AI named exactly what was missing, Stage 3 practically wrote itself.

### Tips for Designing Effective Self-Correction Prompts

- **Separate the stages with clear labels** — "Stage 1", "Stage 2", "Stage 3." Without clear labels, the AI tends to skip the critique step entirely.
- **Tell the AI what to look for in the critique** — Instead of "find any issues," say "check for missing facts" or "check if the explanation is clear for a beginner."
- **Common Mistake:** Writing a single line like *"Give me a detailed, perfect answer"* — this sounds like self-correction, but it does not force the three-stage structure. The AI just gives a slightly longer version of the same answer.

---

## Iterative Prompting

Self-correction happens *within* a single prompt. But what if the task is so complex that even after self-correction you still need to refine things across multiple rounds? That is where **Iterative Prompting** comes in.

**Official Definition:** Iterative prompting is the practice of sending a sequence of targeted follow-up prompts, where each prompt builds on the previous response to progressively improve the quality, depth, or accuracy of the output.

**In Simple Words:** You start with a first version, look at what is missing or weak, and then give the AI specific instructions to fix that one thing. Then you look again, fix the next thing. You keep going until the output is exactly what you need.

**Real-Life Example:** Think of how a sculptor works. They start with a rough block of stone — the general shape is there, but it is not finished. They chisel away one section at a time, refining details with each pass. Iterative prompting works the same way — each round of prompting chisels the response closer to the final form you want.

### The Iterative Prompting Cycle

![The iterative prompting cycle — draft, review, refine one thing at a time, repeat until the output meets your bar](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module2/session11/session11-iterative-prompting-cycle.png)

1. **Draft** — Send an initial prompt to get the first version. Do not expect perfection here.
2. **Review** — Read the output carefully. Ask: *What is missing? What is too vague? What is incorrect?* Pick the **single most important thing** to fix first.
3. **Refine** — Send a follow-up prompt that targets *only* that one thing.
4. **Repeat** — After each refinement, do another review. Keep going until the output meets your standard.

### Full Example — Three Rounds of Iterative Prompting

**Task:** Explain how ATMs work, for a village school student who has never seen one.

```
Round 1 — Draft:
Prompt: Explain how an ATM works for a village school student who has 
never seen one before.

AI Response (Round 1):
An ATM is a machine that gives you cash. You insert your debit card, 
enter your PIN, select the amount, and the machine gives you money. 
It is connected to your bank account.
```

**Review after Round 1:** The explanation is technically accurate but too compressed. A student who has never seen an ATM has no mental model for "debit card," "PIN," or "bank account."

```
Round 2 — Refine:
Prompt: Good start. But this student has never seen a debit card or heard 
the word PIN. Rewrite and first introduce what a debit card and a PIN are 
using simple village-life comparisons.

AI Response (Round 2):
Think of a debit card like a special pass your bank gives you — like how 
a school ID proves you are a student of that school, the card proves you 
have money in a bank account.

A PIN is a secret code — like the lock on your trunk at home that only 
you know the combination to.

Here is how an ATM works:
1. You put your card into the ATM slot — like showing your ID at a gate.
2. You type your secret PIN — like entering your trunk's combination.
3. You tell the ATM how much money you want.
4. The ATM checks with your bank: "Does this person have that much money?"
5. If yes, the ATM counts out the cash and hands it to you.
```

**Why Round 2 is already dramatically better:** One targeted follow-up prompt — fixing only the missing vocabulary — transformed a confusing technical answer into something a village student can actually follow. That is iterative prompting at work.

### Best Practices for Iterative Prompting

- **Fix one thing at a time** — Do not send a follow-up that asks the AI to fix five different things simultaneously. Pick the most important gap and target it.
- **Acknowledge what is working** — Start your follow-up with what to keep: *"The structure is great. Now make the examples more specific."*
- **Know when to stop** — 3 to 5 rounds is the healthy range. If you are on Round 7 and still unhappy, go back and redesign the initial prompt from scratch.
- **Common Mistake:** Saying *"This is bad, try again"* without specifying what is bad. The AI will just produce another version of the same quality. Be specific about exactly what failed.

---

## Agent Prompt Design: Putting It All Together

You have now learned all the individual techniques — System Prompts, Zero-shot, Few-shot, CoT, Structured Prompts, Self-correction, and Iterative Prompting. Now it is time to see how **real agent prompts are designed** by combining these techniques into a single, reliable flow.

### What Is an Agent Prompt Flow?

**Official Definition:** An agent prompt flow is a structured, reusable sequence of prompts that guides an AI agent through a task from start to finish — combining role definition, task execution, self-reflection, feedback evaluation, and output formatting into a single orchestrated workflow.

**In Simple Words:** Instead of asking the AI one question at a time, you design a *recipe* for the agent — each step in the recipe has a purpose, and the agent follows the steps in order. The agent does not stop until it produces a result that meets your standard.

**Real-Life Example:** Think of a hospital discharge process. When a patient is ready to leave, they do not just walk out. There is a checklist: the doctor reviews the final diagnosis, the nurse confirms medications, billing processes insurance, and the patient signs a form. Each person has a defined role and a quality checkpoint. An agent prompt flow gives AI the same kind of structured, accountable process.

### The Four Components of an Agent Prompt Flow

![The four parts of an agent prompt flow — role, task, reflection or feedback criteria, and output format](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module2/session11/session11-agent-prompt-flow-four-components.png)

1. **Role (System Instruction)** — Defines *who* the agent is and *what its core job is*. Think of this as the job description.
2. **Task** — Defines *what the agent must do* in this specific instance. This is the concrete, specific assignment.
3. **Reflection + Feedback Criteria** — Defines *how the agent checks its own work*. These are the measurable quality criteria the agent uses before accepting its own output.
4. **Output Format** — Defines *what the final answer should look like*. This controls structure, length, and presentation.

### Full Example — A Complete Agent Prompt Flow

```python
# Complete system prompt for a Student Study Assistant Agent
# This prompt uses Role, CoT, Structured Format, Constraints, and Reflection

study_agent_system_prompt = """
You are Arya, a patient and encouraging academic tutor specialising in helping 
undergraduate students understand difficult concepts. You have taught students 
from non-engineering backgrounds for over 10 years.

Your core capabilities:
1. Explain any academic concept in simple language with relatable Indian examples
2. Create short practice questions to test understanding
3. Break down complex problems step by step

When a student asks you to explain a topic, ALWAYS follow this process:
Step 1: Check if they have any prior knowledge — ask one quick question if needed
Step 2: Give a simple analogy or real-life example FIRST, before the technical definition
Step 3: Then provide the technical definition
Step 4: Give 1-2 examples with increasing complexity
Step 5: Ask the student to summarise what they learned in their own words

Constraints:
- Never give a direct answer to a practice question — guide the student to the answer
- Do not use academic jargon without immediately explaining it in brackets
- Never make the student feel bad for not knowing something
- Keep all explanations under 200 words unless the student asks for more detail

If the student says "I don't understand" or "This is too hard", respond with:
"Totally okay! Let's try a different approach..." and use a different analogy.
"""

# This prompt is sent to the LLM API as the 'system' message
# Every student message after this would be the 'user' message
print("Study Agent system prompt is ready.")
print(f"Prompt length: {len(study_agent_system_prompt)} characters")
```

**How the code works:**
- The **Role** is given a *name* (Arya) and specific personality traits — making the agent far more consistent than a nameless, trait-less role
- The **CoT process** (Steps 1–5) is embedded as the agent's "when a student asks" workflow — so every explanation follows a logical teaching sequence
- The **Constraints** prevent common agent failures: giving away answers, using jargon, discouraging students
- The **edge case handling** ensures the agent never gets stuck when a student struggles
- `len(study_agent_system_prompt)` measures character count — in real LLM APIs, you are charged by tokens (~4 characters = 1 token), so prompt length management matters

### The Feedback Loop — Making Agents Self-Regulating

When building agents that run *without you present*, you need them to check and fix their own output automatically. This is a **Feedback Loop** — the agent generates an output, evaluates it against a checklist, and revises if needed.

![User feedback loops vs internal feedback loops — human steering versus checklist-driven self-evaluation in the prompt](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module2/session11/session11-feedback-loop-user-vs-internal.png)

**Internal Feedback Loop Example:**
```
Prompt: "Write a 2-sentence product disclaimer for a health supplement.

After writing it, evaluate:
- Is it under 30 words? (Yes/No)
- Does it include a warning that results may vary? (Yes/No)
- Does it recommend consulting a doctor? (Yes/No)

If any answer is No, rewrite and re-evaluate until all three are Yes."
```

No human involved. The agent finds its own gaps and loops until all criteria pass.

> **[ Student Activity ]**
>
> **Build Your Complete Agent**
>
> This is your session capstone. Design a **complete system prompt** for an AI agent that helps *you* with something in your real life — your studies, your work, your side project, or your daily routine.
>
> Your system prompt **must include all four of these:**
> - **Role** — Give the agent a name and a specific persona with 2–3 personality traits
> - **CoT Process** — Write at least 3 numbered steps the agent must follow before responding
> - **Constraints** — Write at least 2 guardrails (what the agent must NOT do)
> - **Output Format** — Specify how the agent's response should be structured
>
> *Examples: a "daily planner" agent, a "mock interviewer" agent, a "side hustle advisor" agent, or a "fitness coach" agent.*
>
> Once done, read your Role and Constraints to the batch. The class votes: does this agent sound reliable and useful?
>
> *Instructor note: Give students the full 10 minutes. Walk around and help students who are stuck on the Role or CoT steps. In the last 2 minutes, pick 2–3 students to share. Point out what makes each agent prompt strong.*

---

## Key Takeaways

- **System Prompts** set the permanent rules and persona for an agent — they define who the AI is, what it handles, and how it communicates for the entire conversation. **User Prompts** are the live messages that the system prompt shapes and filters.
- **Zero-Shot prompting** works for simple, standard tasks where the AI's training data has enough context. **Few-Shot prompting** is essential when you need a specific output style, format, or tone that the AI cannot infer on its own — showing it 1–2 examples makes the pattern explicit.
- **Chain-of-Thought (CoT)** works by forcing the LLM to reason step by step before answering — adding phrases like *"Let's think step by step"* or embedding numbered reasoning steps in a system prompt often improves quality on logic, reasoning, and multi-factor problems.
- **Structured Prompt Templates** with five components — Role, Task, Instructions, Constraints, Output Format — are the professional standard for building agent prompts because they eliminate ambiguity and produce predictable, formatted outputs every time.
- **Self-correction prompts** and **iterative prompting** are the two tools for improving AI output — self-correction asks the AI to evaluate and rewrite *within a single prompt*, while iterative prompting refines output across *multiple rounds* of targeted follow-up.
- In later sessions, you will connect these prompt designs to **full agent frameworks and production setups**, where prompt design remains the main lever for how an agent thinks, reasons, and acts.

---

## Important Commands, Libraries, Terminologies Used

| Term / Concept | Category | Meaning |
|---|---|---|
| **System Prompt** | LLM Concept | Persistent background instruction sent to an LLM before the conversation — defines persona, scope, and rules |
| **User Prompt** | LLM Concept | The real-time message sent by the user in each conversation turn |
| **Zero-Shot Prompting** | Technique | Asking the AI to perform a task with no examples — relies on the AI's training data patterns |
| **Few-Shot Prompting** | Technique | Providing 1–5 worked examples inside the prompt before asking your actual question |
| **Prompt Engineering** | Concept | The discipline of designing and refining AI inputs to reliably produce accurate, useful outputs |
| **Chain-of-Thought (CoT)** | Technique | Asking the LLM to show reasoning steps before giving a final answer |
| **Zero-Shot CoT** | Technique | Triggering step-by-step reasoning with a phrase only — e.g., "Let's think step by step" |
| **Few-Shot CoT** | Technique | Showing 1–2 solved examples with reasoning before asking your question |
| **Structured Prompt** | Technique | A prompt template with defined components: Role, Task, Instructions, Constraints, Output Format |
| **Role** | Prompt Component | Defines who the AI is and what persona to adopt |
| **Task** | Prompt Component | States what the AI must deliver |
| **Instructions** | Prompt Component | Step-by-step guidance on how to complete the task |
| **Constraints** | Prompt Component | Guardrails — what the AI must NOT do or must limit |
| **Output Format** | Prompt Component | Specifies the structure, length, and style of the expected response |
| **Self-Correction Prompt** | Technique | A three-stage prompt (Generate → Critique → Rewrite) that makes the AI check and fix its own output |
| **Iterative Prompting** | Technique | Multiple rounds of targeted follow-up prompts, each fixing one specific gap in the previous output |
| **Agent Prompt Flow** | Concept | A four-component workflow (Role + Task + Reflection Criteria + Output Format) for reliable agent behaviour |
| **Feedback Loop** | Concept | A cycle where the agent evaluates its own output against criteria and revises until the criteria are met |
| **Reflection-Based Prompting** | Technique | The AI self-verifies and iterates using criteria embedded in the prompt — no human needed |
| **f-string** | Python | Python syntax (`f"..."`) for embedding variables inside strings — used to inject data into prompts |
| **LLM (Large Language Model)** | Concept | AI models like GPT-4, Gemini, Claude that generate text — the engine behind AI agents |
| **Token** | LLM Concept | The basic unit of text that LLMs process (~4 characters = 1 token); API costs are measured in tokens |
| **`"""..."""`** | Python | Triple-quoted multi-line string — used to write long prompts cleanly in Python |
| **`.format()`** | Python | Python string method to replace placeholders like `{name}` with actual values |
