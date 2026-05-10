# Pre-read: Mastering Prompt Engineering

You have probably seen someone open ChatGPT, type one vague line, get a flat reply, and mutter that *“AI is overrated.”* The same tool, in another person’s hands, returns crisp reports and useful step-by-step explanations. The gap is usually **how clearly they ask**.

Last time, you met the **LLM** (large language model): software that predicts the next words from patterns in huge text. It does not know your boss or your college — only what you put in the chat or what an app sends for you. So the next question matters for your career: **How do you talk to these systems so you reliably get what you need?**

---

## When “just ask nicely” is not enough

Imagine hiring a sharp freelancer and saying only, *“Help me with my work.”* They guess — sometimes fine, often shallow or wrong format. Give them a brief: goal, audience, what to avoid, and how the deliverable should look. Same person — **much** better output.

An LLM responds the same way, only faster. **Prompt engineering** means designing those briefs on purpose. In class we treat it like any communication skill you can practise — not a secret club for experts.

---

## The idea that ties the whole session together

Picture a **restaurant** before the lunch rush. The owner does not shout a new rule for every customer. Once, at the start, the staff are told: *We only serve vegetarian food, stay polite, and if something is unavailable, suggest a close alternative.* That one backstage briefing shapes every plate that leaves the kitchen.

When a guest walks in and says, *“I want something quick with paneer,”* that order is a single, fresh request. The guest does not repeat the house rules — but the answer they get still follows them.

In AI tools, the **long-lived backstage briefing** is called a **system prompt** (who the assistant is, what topics it covers, what tone to use). Each message you type in the chat is a **user prompt**. The model is always influenced by both: the backstage rules plus your live question. Once you see that split, a lot of confusing behaviour (“Why did it refuse that?” “Why is it so formal?”) suddenly makes sense — those answers often came from instructions you never saw.

---

In this pre-read, you'll discover:

- **Why** vague wishes produce weak AI answers — and how a clear “brief” changes the game.
- **How** showing two short examples inside your question can lock in tone and format, while a plain instruction without examples still works for simple jobs.
- **Why** asking the model to *think in steps* (like showing working in a maths notebook) sharpens answers on tricky questions.
- **How** professionals combine prompts that **structure** output, **check** their own draft, and **improve** across a few back-and-forth rounds — the kind of workflow real **AI agents** need.

---

## A quick tour of the tools — in simple words

You will meet a few **techniques** with names, but each has an everyday meaning:

- **Zero-shot** means: *“Do this task — no examples.”* Fine for quick translations, simple lists, or things the model has seen millions of times online.
- **Few-shot** means: *“Here are one or two solved mini-examples in the exact style I want — now do the same for my new case.”* That is how you steer tone, layout, and branding without writing a long rulebook.

- **Chain-of-thought** means: *“Show the middle steps, not only the final line.”* That habit often lifts accuracy on logic and maths-style tasks, because each step constrains the next.

- **Structured prompt templates** mean: you fill clear boxes — **role** (who should answer), **task** (what to deliver), **instructions** (how to proceed), **constraints** (what to avoid), and **output format** (headings, bullet limits, length). Think of it like a **government form or FIR layout**: the structure forces every important field to appear.

- **Self-correction** means: *“Write a draft → say what is weak → rewrite.”* **Iterative prompting** means: you do that improvement **across several chat turns**, fixing **one** gap at a time until the answer matches your bar — like a sculptor refining a block of stone pass by pass.

- Finally, **agent prompt design** stitches these pieces into a **repeatable flow** so an assistant can run with a checklist even when you are not watching — similar to a **hospital discharge process**: each station has a job and a quality check before the patient leaves.

---

## After this session, what becomes easy?

You will be able to:

- Explain **system** versus **user** prompts to a teammate — and know why chatbots in banking or college portals behave the way they do.
- Choose between **quick one-line** prompts and **example-based** prompts for real tasks you care about.
- Use **step-by-step reasoning** when a problem has moving parts — exams, business trade-offs, planning.
- Build a **structured request** you could hand to an AI product or paste into code later.
- Design prompts that **review and upgrade** their own output, and know when to **stop** after a few refinement rounds.

---

## Questions we will crack in the live class

1. **You need twenty product descriptions in *your* company’s voice, same layout every time.** Is a single sentence enough, or do you “show the pattern” with samples — and how would you word that?
2. **Two students ask an AI whether to learn Python or SQL first for a data career.** One prompt gets a flashy one-liner; yours uses chain-of-thought. What exactly do you add — without pasting an essay of rules — to make the reasoning visible and useful?
3. **You are building a small “study buddy” that runs while you sleep.** How do you combine **role**, **numbered steps**, **guardrails**, and **output shape** in one **system prompt** so replies stay kind, on-topic, and consistently formatted?

Bring one real task — a report, mail, project note, or interview prep. If you can describe the messy version in one short paragraph, you have material for the exercises. See you in class.
