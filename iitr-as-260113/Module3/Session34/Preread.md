# Pre-read: Ollama — Exploring Another World of LLMs

You have already met the idea of an **LLM** — a model that reads and writes language, not just numbers in a spreadsheet. It can draft replies, summarise notes, and soon it will sit behind the **agents** you are building. For most people so far, that power has lived **only in the cloud**: open a website, type a prompt, wait, read the answer somewhere far away.

Picture **11:30 at night**. Your agent almost works — one line of code is wrong. You change the prompt and run again. And again. **Twenty times**. Each run needs **internet**, eats **API quota**, and sends your messy draft to a server you do not control. Wi‑Fi flickers. The script hangs. You shut the laptop not because you cannot think, but because your **brain was rented**, not owned.

Or picture a shop owner who wants a small assistant inside their billing software — they cannot send every customer name to a public website all day. They need something that runs **on their own machine**, when the net is slow or down.

**The problem**

What if every agent you build needs a **language brain** behind it, but that brain only exists **online**? Practice runs are not free tries — they cost quota or money. Private drafts leave your desk. A blocked API or bad Wi‑Fi kills the whole demo mid-class.

What if social media tells you to **pull the biggest model** on a normal student laptop — and your evening disappears into a huge download, an overheating fan, and a frozen screen? Big on paper does not mean right for **your** machine.

Many learners hit this wall right before agent sessions: the code is ready, but the **LLM backend** is not. This session closes that gap.

**The idea we will build toward**

We introduce **Ollama** — a way to **download, run, and call** language models **on your own laptop**, then switch to **Ollama Cloud** when you need a stronger answer, still on a **free tier** while you learn.

In simple terms: **install once, pull a light model, talk from the terminal, then from Python** — and later change only **where** your script connects (**host**) and **which key** it uses, so the **same file** works for **local** and **cloud**. You are not learning two separate tools; you are learning **one pattern** with two power sources.

That pattern matters because the next modules assume you already have a **working, cost-free LLM setup** before you wire agents on top.

**A simple analogy**

Think of **Ollama on your laptop** like a **home inverter**. For daily study — many small runs, late-night debugging — you run from **your own battery**: quick, predictable, no begging the grid. When you need **heavy load** for a demo or a harder prompt, you plug into the **main line** — that is **Ollama Cloud**. The **wiring in your house** (your Python script) stays the same; you only choose **which power source** you use today.

Another picture: **pulling a model** is like **downloading an app** to your phone instead of streaming the same movie every time. Once it is on disk, you can open it offline. **Light models** (around **0.5B** or **1B** — **B** means **billions of parameters**, a rough size score) are the **scooter** in a city of trucks: not glamorous, but they get you to class on a real student laptop.

**Local vs cloud (conceptual)**

*Local* means rerun freely on your desk, keep drafts private, and spare your RAM — but answers may be shallower and **hallucinate** more. *Cloud* means stronger models on Ollama’s servers (free tier while you learn) — often sharper on hard prompts, but your text leaves the machine. In class you will **run the same prompt both ways**; that side-by-side test teaches more than any slide.

**In plain language**

- **Ollama**: A tool that lets you run LLMs on your machine and optionally call **Ollama Cloud** with the same style of API.
- **Pull a model**: **Download** that model’s files into Ollama so you can use it again without re-downloading every time.
- **Light vs heavy models**: **Light** (e.g. 0.5B, 1B) fits normal laptops; **heavy** models can choke RAM, heat, and patience — avoid them until you know your machine can cope.
- **Parameters (B)**: A rough “how big is the brain” score; larger often means smarter answers but **heavier** files and slower runs locally.
- **Hallucination**: The model **sounds sure** but is **wrong** — more common when the model is very small or the question needs deep knowledge; there is no built-in fact checker in the box.
- **API**: A **fixed doorway** your Python code knocks on to send a prompt and get text back.
- **Host**: **Which address** your code calls — your own machine (`localhost`) or Ollama’s servers on the internet.
- **API key**: A **secret passcode** for Ollama Cloud; treat it like an ATM PIN — never paste it in public chats or GitHub repos.
- **Embeddings**: Turning text into **number patterns** so software can search or “remember” meaning — useful later when agents need memory or RAG-style lookup.
- **Capabilities**: Besides chat, Ollama supports **text generation**, **embeddings**, and model families for **vision** (images), **audio**, and **video** as your projects grow.

**Where this shows up (so it feels real)**

- **Late-night debugging**: dozens of agent test runs without burning cloud quota or waiting on flaky Wi‑Fi.
- **Privacy-sensitive drafts**: internship reports, client notes, or internal text that should not leave your laptop during experiments.
- **Class and placement demos**: a script on your machine that still works when the auditorium network misbehaves.
- **Stepping up quality**: same code, stronger model in the cloud when the assignment needs better answers.

**Ollama inside agentic thinking**

Every agent needs a **brain** that turns user language into the next reply or tool call. If that brain is always a paid, fragile cloud tab, you spend the course fighting **quota and Wi‑Fi** instead of learning **logic and tools**. Ollama gives you a **personal lab on your desk**: debug fifty times, keep drafts private, then **dial up** cloud only when quality demands it. The agent code you write later will assume this backend already exists — today is where you **own the brain**, not just visit it in a browser.

**Questions we will answer in the live session**

- Why can **local Ollama** change how you practise compared to dozens of **cloud API calls** — even when both seem “free”?
- What can go wrong if you **pull the largest model** on a **weak laptop**, and what is a **smarter first model** to pull?
- How do **host** and **API key** let **one Python script** serve both **local** and **Ollama Cloud**?
- When you ask local and cloud the **same question**, how do you spot **hallucination** and explain the difference to someone non-technical?
- What can Ollama do beyond **chat** — and which **model types** (text, vision, audio, video) might matter for future agent features?

**After this session, you should be able to**

- Explain why running an LLM **locally** helps learning agents — fewer quota surprises, more control, work offline for basic runs.
- **Install Ollama**, pull a **light model**, and prove it works from the **terminal**.
- Describe why **heavy models** are a bad default on regular student laptops and what you **trade away** with very small local models (speed and privacy vs shallower answers and more hallucination).
- **Run a Python script** that calls your **local** Ollama through the API and prints a real response.
- **Create an Ollama account**, generate a **free-tier API key**, and update the **same script** to call **Ollama Cloud** by changing **host** and **key**.
- **Compare** local light-model output with cloud output on the **same prompt** in your own words.
- **List** main Ollama capabilities — chat, text generation, embeddings — and **name** model families available (text, vision, audio, video) at a high level.
- **Enter the next agent-building sessions** with one working script that can call **either** local Ollama or Ollama Cloud — without “I could not set up the LLM” blocking you.
