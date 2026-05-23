# Pre-read: Open-Source LLMs — Run the Brain on Your Own Machine

You have spent time learning **how to ask** an AI the right way — system rules, examples in the prompt, step-by-step thinking, and agent-style flows. That skill assumes something is already listening, usually a **cloud service**: your words travel over the internet, a company’s servers do the work, and the answer comes back.

For many learners, that setup feels fine until real life kicks in.

Picture **11:30 at night**. Your project almost works. You tweak the prompt and run again — **fifteen or twenty times**. Each run needs **stable Wi‑Fi**, may eat **API quota or money**, and sends half-finished notes to a server you do not control. The connection drops once; your evening stalls. You close the laptop not because the idea was bad, but because the **brain was rented**, not owned.

Or picture a team building on **placement data** or internal reports with a strict rule: *do not share this outside the institute.* Yet every test prompt goes to a datacenter far away. They need to **practice on their own desk** without treating privacy as an afterthought.

---

## The challenge we are solving

What if every time you wanted to **try** an AI idea, you depended on someone else’s servers, bill, and uptime?

What if social media told you to download the **biggest** language model on a normal student laptop — and your evening vanished into a **huge download**, a screaming fan, and a frozen screen? **Big on paper** does not mean **right for your machine**.

What if you already know **how to write a good prompt**, but you still cannot **demo in class** because the API failed or the free tier ran out?

These show up right before **agents**, **LangChain**, and **RAG** — when you need a **reliable language brain** you control, not just a browser tab.

---

## What we open in the live session

The next step is **open-source and local LLMs** — models you **download and run on your own computer** — plus **Ollama**, a tool that makes that practical on Windows, Mac, or Linux.

You will **install once**, **pull a light model** (e.g. **0.5B** or **1B** — **B** means **billions of parameters**, a rough “how big is the brain” score), chat from the **terminal**, then call the same model from **Python**. When your laptop is too small for a hard question, you switch to **Ollama Cloud** with an **API key** — same style of request, only **address** and **model size** change.

By the end, **one script** should work in **two modes**: **local** for free, private practice; **cloud** when you need a stronger answer. Upcoming agent sessions expect that foundation.

---

## A simple analogy from daily life

A **cloud LLM** is like ordering on **Swiggy** — powerful kitchens far away, but you pay per order and your food leaves home.

A **local LLM** is **cooking in your kitchen** — you control ingredients and privacy, but your stove (laptop) has limited firepower. For a big occasion you **rent a bigger kitchen** — that is **Ollama Cloud**, same brand, different location.

**Ollama** is like **Play Store plus a player** for AI: **install** a model once (`pull`), **open** it whenever you need (`run` or from Python).

---

In this pre-read, you'll discover:

- **Why** running a model **on your machine** changes agent learning — cost, privacy, and practice without burning cloud quota on every typo.
- **How** **Ollama** pulls a **light model**, chats from the **terminal**, and exposes a **local API** your Python code calls — the same message shape agents use later.
- **What** you trade with **very small** local models (weaker reasoning, more **hallucination** — confident but wrong answers) — and when **cloud** is worth it.
- **How** one Python script flips **local vs Ollama Cloud** by changing **host**, **model name**, and an **API key** kept out of your code.

---

## Words you will hear — explained right away

- **Open-source LLM**: Weight files are **publicly downloadable** — not locked in one company’s app only.
- **Local LLM**: Inference runs **on your computer**; prompts need not leave your machine.
- **Ollama**: Pulls, runs, and serves models; programs usually talk to **`localhost:11434`**.
- **`ollama pull` / `ollama run`**: **Download** once, then **chat** in the terminal.
- **Light vs heavy models**: Tags like `qwen2.5:0.5b` fit normal laptops; **70B+** needs **tens of GB RAM** and will freeze most student machines.
- **API key**: Secret for Ollama Cloud — set in the **environment**, never in GitHub or group chats.
- **Embeddings**: Text as **number patterns** for similarity — a preview of **RAG** in later sessions.
- **Modalities**: **Text**, **vision**, **audio**, or **video** — check before you pull the wrong heavy model.

**Prompt engineering** still matters: a small brain plus a **clear system message** (“If unsure, say you do not know”) beats a vague question to a giant model. Today you learn **where** the brain runs.

---

## Where this shows up in real work

- **Late-night debugging** without flaky Wi‑Fi or surprise API bills.
- **Sensitive drafts** that should stay on your laptop during experiments.
- **Class demos** that work when auditorium network fails.
- **Side-by-side tests**: same question **local vs cloud**, then explain **speed**, **privacy**, and **trust** in plain language.

---

## Questions we will tackle live

1. A classmate pulls a **70B** model on an **8 GB RAM** laptop. **What will likely happen**, and which **light model** should they use instead?
2. Your **local 0.5B** gives a **wrong exam date** confidently. Is Ollama broken — or is something else going on, and how do **better prompts** or later **RAG** help?
3. With **one Python file** and the **same math problem** in both modes, **what besides “sounds nicer”** should you compare — steps, invented numbers, speed, where the prompt went?

---

## After this session, you should be able to

- Explain **why local and open-source LLMs** matter for **learning, privacy, and cost** — and when **cloud** is better.
- **Install Ollama**, verify setup, **pull a light model**, and chat from the **CLI**.
- **Describe trade-offs** of tiny local models and why **heavy pulls** fail on student laptops.
- **Run Python** for **local Ollama**, then the **same script** on **Ollama Cloud** via **host** and **API key** — no secrets in code.
- **Compare** local and cloud on the **same prompt** and name **one** quality difference you would trust for homework vs a demo.
- **List** Ollama capabilities beyond chat — **embeddings**, and types for **vision**, **audio**, **video**.
- **Enter the next agent sessions** with one script that calls **either** local or cloud — so setup never blocks the logic you came to learn.
