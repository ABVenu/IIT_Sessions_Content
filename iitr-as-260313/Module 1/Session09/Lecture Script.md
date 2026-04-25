# Lecture Script: Prompt Engineering, Business Use Cases & Framework Overview

**Session Duration:** 2 hours 15 minutes (≈ 130 min of blocks + one 5–8 min break)  
**Audience:** Absolute Beginners (Indian students from any background, no prior tech assumed). Students already know *what AI agents are* and *how LLMs work at a surface level* from earlier sessions. Today is a **prompting-heavy, hands-on** class — five in-session practices plus one capstone activity.

---

## How to use this document

This file is for **timing and facilitation only**. It is not a substitute for the Lecture Notes. Use it to manage pacing, screen-sharing, room circulation, live-prompting, and quick engagement checks. Keep the Lecture Notes open on a second tab for full definitions, example prompts, and analogies.

---

## Break rule

After **60–75 minutes** of instruction and live prompting, take **one** pause of **5–8 minutes**. Do not schedule the break as a numbered teaching block; resume with the next block's bridge sentence. A natural break point is suggested after Block 7 (Practice 3 — Fix the Weak Prompt).

---

## Environment setup (before class)

- Have **ChatGPT** (free plan is fine) open on the projector in a fresh chat. Keep **Gemini** and **Claude** as backups in separate tabs so a student can answer *"sir, does it work the same in Gemini?"* in 10 seconds.
- Keep a **Google Doc / Notes app** open beside the chat window — you will paste 3–5 different prompt outputs side-by-side during Practices 2, 3 and 5.
- Keep the Lecture Notes scrolled to the **"Example Prompts for Different Formats"** and **"Side-by-Side Comparison Table"** sections — these are the two screen-share hotspots.
- Students need **only one device** with a browser and a free ChatGPT/Gemini account. **No coding environment needed today** — repeat this at the start so nobody panics about Python.

---

# PART A — Prompt Engineering Fundamentals (≈ 65 minutes)

---

## 1. Opener — Why prompt engineering is a real skill (6 minutes)

- **Screen-share:** Write the word **PROMPT** on one line. Below it: *"garbage in = garbage out"*.
- **Say it plainly:** *"Till now we learnt **what** AI agents are and **how** LLMs work. Today we learn the one skill that actually **controls** them — asking them in the right way."*
- **Relatable hook (30 sec):** The **auto-rickshaw example** from the Lecture Notes — *"Bhaiya, chalo"* vs *"Bhaiya, HSR Sector 4, 5th Main, near the bakery, shortest route"*. Same driver, different destination.
- **Set the plan out loud:** *"This is a **hands-on class**. Five live practices, one mini-project. Keep ChatGPT open in another tab from minute one."*
- **Myth-bust in one line:** *"Prompt Engineer is a real job title today — Flipkart, Swiggy, and Meesho hire for it. It is not a fancy word for 'ChatGPT user'."*
- **Check:** **Thumbs up** — *"ChatGPT or Gemini open in a tab, ready to type?"*

**Bridge sentence:** *"Every prompt you ever write sits on top of a hidden prompt the developer already wrote. Let us meet that hidden one first — the **System Prompt**."*

---

## 2. System Prompts — the agent's job description (10 minutes)

- **Screen-share:** Two boxes side-by-side — **"What you type"** vs **"What the developer set"**. The second box is the **System Prompt**.
- **Definition (one line from notes):** *"A System Prompt is the hidden instruction that fixes the AI's identity, tone, boundaries, format, and scope for the **entire** conversation."*
- **Relatable hook (30 sec):** The **restaurant waiter briefing** — "*namaste greet, chef's special first, no non-veg for Jain customers*". That briefing is the waiter's system prompt.
- **Screen-share the 5 things a system prompt controls** — one line each, 10 seconds per bullet:
  - **Identity** — who the AI *is*.
  - **Tone** — *how* it speaks.
  - **Boundaries** — what it must *not* do.
  - **Format** — how answers *look*.
  - **Scope** — what topics it can discuss.
- **Live-demo the "SehatBot" example from the Lecture Notes.** Paste the 5-line system prompt into a fresh ChatGPT chat as the **first message** (prefix it with *"Follow these rules for the rest of this conversation."*). Then type three user questions back-to-back:
  1. *"Mujhe sardi-khansi ke liye kya karna chahiye?"* — observe health-style answer.
  2. *"What is the dose of paracetamol for a 5-year-old?"* — observe the *"consult a doctor"* refusal.
  3. *"Who won IPL 2025?"* — observe the *"I can only help with health queries"* boundary.
- **Narrate what happened:** Same model (GPT-4), three very different behaviors — **just because of the system prompt**.
- **One student doubt to pre-empt:** *"Can a user override it?"* → *"Generally no. System prompt has highest priority. That is why companies use it to protect their product."*
- **Check:** **Thumbs up** — *"Clear that the system prompt is the **frame**, and every user message lives **inside** it?"*

**Bridge sentence:** *"Enough theory — now **you** are going to write one yourself in the next 10 minutes."*

---

## 3. In-Session Practice 1 — Build Your Own System Prompt (10 minutes)

- **Screen-share:** The task card from the Lecture Notes — build **"PaisaBachao Bot"** for Indian college students.
- **Say it crisply:** *"Your bot must have all 5 things — identity, tone, boundaries, format, scope. If any one is missing, the bot will break when we test it."*
- **Timing split (announce out loud):**
  - **4 min** — everyone writes their system prompt in their notebook or a doc.
  - **3 min** — paste into ChatGPT as the first message and test with the **three provided user questions** (₹2000 saving, iPhone loan, cricket score).
  - **3 min** — pair up (person next to you): *"Where did the bot break? Fix one rule."*
- **Circulate the room.** Stop at 2–3 laptops. Look for the classic miss: students forget **scope**, so the bot happily answers the cricket question.
- **Cold-call at the end:** Ask **two volunteers** — *"Did your bot refuse the loan question? Did it refuse the cricket question? If not, which rule was too weak?"*
- **Lock-in line:** *"This is the exact exercise a developer at a fintech company does on Day 1 — you already did it."*

**Bridge sentence:** *"System prompt sets the whole chat. But even inside a normal chat, you can instantly upgrade an answer with one trick — **Role Prompting**."*

---

## 4. Role Prompting — "Pretend you are a…" (7 minutes)

- **Screen-share:** *"You are a ___."* with an empty blank.
- **Definition (one line):** *"Role Prompting assigns a **persona or profession** to the LLM so its answer matches the expertise and style of that role."*
- **Relatable hook (20 sec):** Asking a **stranger** vs asking a **CA** about saving money. Same question, completely different answer. Role prompting makes the AI behave like the CA.
- **Screen-share the common roles list** (5 seconds per role — just read them): teacher / senior engineer / financial analyst / motivational speaker / interview panelist.
- **Live-demo the "compound interest" comparison** from the Lecture Notes:
  1. Ask plainly: *"Explain compound interest."* → textbook definition.
  2. Ask with role: *"You are a friendly bank relationship manager. Explain compound interest to a 40-year-old shopkeeper."* → example with his shop savings, Hindi-English mix, real numbers.
- **Narrate side-by-side on screen:** *"Same model, same topic, 10 seconds apart. The role changed the depth, vocabulary, and the example."*
- **Why it works (one line):** *"LLMs were trained on how teachers, doctors, lawyers **actually write**. Assigning a role pulls that specific style out of its memory."*
- **Cold-call:** *"Give me one role you would assign if you wanted to practice for a product manager interview."* (Accept: *"strict PM interviewer from Flipkart"*, *"senior product manager at Swiggy"*, etc.)

**Bridge sentence:** *"Now you are going to feel this difference yourself — one question, five roles."*

---

## 5. In-Session Practice 2 — Same Question, Five Roles (10 minutes)

- **Screen-share:** The fixed question: *"Should I start learning Python in 2026?"* and the 5 roles from the Lecture Notes (10-year-old / school principal / Silicon Valley CEO / stand-up comedian / SEBI career counsellor).
- **Say clearly:** *"Do **not** change the question. Only change the role. Copy each reply into a doc — you are collecting evidence."*
- **Timing split (announce):**
  - **6 min** — run all 5 prompts, paste outputs into a doc.
  - **3 min** — groups of 3: rank which was **most useful**, **most fun**, **most unexpected**.
  - **1 min** — one student from each group shares their **favourite role** in a single sentence.
- **Circulate.** If someone is stuck on prompt wording, give them the copy-paste starter from the Lecture Notes.
- **Lock-in line (say twice):** *"After this exercise, you will **never** again ask ChatGPT a question without a role. Promise yourself that."*
- **Check:** **Thumbs up** — *"Did the 10-year-old's answer and the CEO's answer feel like two different people wrote them?"*

**Bridge sentence:** *"Role is one dimension. The **body of the prompt** — the actual ask — is where most beginners lose quality. Let us fix that with a formula."*

---

## 6. Writing Effective Prompts — the C-I-F-C formula (8 minutes)

- **Screen-share:** Write **C-I-F-C** big on the screen: **C**ontext — **I**nstruction — **F**ormat — **C**onstraints.
- **Make students say it out loud:** *"Context, Instruction, Format, Constraints."* Repeat once.
- **Relatable hook (30 sec):** The **maid WhatsApp message** from the notes — *"Aaj subzi bana do"* vs *"Aloo-gobhi, kam teekha, 2 logon ke liye, 12 baje tak."* Same request, zero confusion in the second.
- **Live-demo the "Diwali speech" comparison:**
  1. Type the weak one: *"Write something about Diwali."* → generic Wikipedia-style answer.
  2. Type the strong one (read it out, bit by bit, pointing at each C-I-F-C piece): *"I am a school teacher (**C**). Write a short speech on Diwali for Class 5 students (**I**). Use 5 bullet points, each one line (**F**). Keep language simple and avoid any religious controversy (**C**)."*
- **Point at the output:** *"This one is ready to **use**. The first one was ready to **edit**. That is the difference the formula makes."*
- **Screen-share the "Common Mistakes" list** (10 seconds per bullet): too short / too long / no examples / forgetting the audience.
- **Check:** **Thumbs up** — *"Everyone has C-I-F-C written down? We will use it non-stop for the rest of the class."*

**Bridge sentence:** *"Theory understood. Now you rewrite 4 weak prompts in the next 12 minutes — this is where C-I-F-C enters your muscle memory."*

---

## 7. In-Session Practice 3 — Fix the Weak Prompt (12 minutes)

- **Screen-share:** The 4 weak prompts from the Lecture Notes — *Write an email / Give me a business idea / Summarise this article / Plan my trip*.
- **Timing split (announce clearly):**
  - **5 min** — rewrite all 4 using C-I-F-C in a notebook or doc. **Solo**, no talking.
  - **5 min** — run both versions (weak + your strong) in ChatGPT side-by-side. Paste outputs into the doc.
  - **2 min** — groups of 4 vote on the best rewrite of each prompt.
- **Circulate aggressively.** Look for two common misses:
  - Students skip **Constraints** (word limit, tone) → their "strong" prompt is still loose.
  - Students stuff too much into **Instruction** → the AI juggles 3 things and does all of them badly.
- **Pause at ~8 min to show one good student rewrite on the projector.** 30 seconds — point at C, I, F, C in their prompt.
- **Cold-call 2 pairs at the end:** *"Read your strong prompt out loud. Which of the four letters was hardest to add?"* (Usually **Constraints**.)
- **Lock-in line:** *"This formula is free. Using it adds 10 minutes to your prompt and saves you 2 hours of cleanup on the output."*

> **[BREAK RULE]** We are now ~60–65 minutes in. Take the **5–8 minute pause** here. Resume at Block 8 with the bridge sentence below.

**Bridge sentence (post-break):** *"Prompts written. Now a simple but business-critical skill — **forcing the output into the shape you need**."*

---

# PART B — Output Control, Variations & Business Use Cases (≈ 45 minutes)

---

## 8. Controlling Output Format (7 minutes)

- **Screen-share:** *"Paragraphs are for humans. Tables, JSON, and CSV are for software."* Write this on a whiteboard-style slide.
- **Definition (one line):** *"Output Format Control is telling the model **exactly how** to structure its answer — bullets, steps, table, JSON, short line, markdown."*
- **Relatable hook (20 sec):** Zomato delivery partner asking for directions — a **step-by-step list** is 10× more useful than a long paragraph. Format = delivery.
- **Screen-share the 6 popular formats list** (5 seconds each): bullets / numbered steps / tables / JSON / 1-line / markdown.
- **Live-demo 4 format prompts back-to-back from the Lecture Notes** (all on the topic of *phones / router / city info / yoga*):
  1. **Table:** *"Compare iPhone 15 vs Samsung S24 in a markdown table with columns: Feature, iPhone 15, Samsung S24."*
  2. **Steps:** *"Give step-by-step instructions to reset a Wi-Fi router, numbered 1 to 6."*
  3. **JSON:** *"Extract name, age, city from this sentence and return **ONLY** a JSON object — no explanation: 'Rahul, 27, lives in Pune.'"*
  4. **Bullets:** *"List 5 benefits of yoga in one-line bullets, no explanations."*
- **Point at the JSON output:** *"See the word **ONLY**? That single word is what stops the model from adding 'Here is your JSON:' before the object — which would break any code reading it."*
- **Pro-tip (one line):** *"When the output is going into **Excel, code, or an app**, ask for **JSON or CSV**. When it is going to a **human**, ask for bullets or a table."*

**Bridge sentence:** *"Let us make this muscle memory — one piece of information, four different shapes."*

---

## 9. In-Session Practice 4 — Same Data, Four Formats (8 minutes)

- **Screen-share:** The topic — *"Top 5 most populous cities in India"* — and the 4 required prompts from the Lecture Notes (paragraph / bullets / markdown table / JSON).
- **Timing split:**
  - **5 min** — run all 4 prompts one after the other, screenshot or paste each output into the doc.
  - **3 min** — pair with the person next to you; decide: *"Which format would you send to a friend on WhatsApp? Your boss in an email? A developer building an app? A reporter writing a story?"*
- **Lock-in line (say twice):** *"**Format is not decoration. Format is delivery.** Wrong format = output gets rewritten by a human = your AI just wasted effort."*
- **Cold-call:** *"If you had to paste this into a Google Sheet tomorrow, which format wins?"* (JSON or markdown table.)

**Bridge sentence:** *"Now — same prompt, small tweaks, very different outputs. That is what real Prompt Engineers do all day — **test variations**."*

---

## 10. Prompt Variations — the A/B testing mindset (6 minutes)

- **Screen-share:** Write **Zero-shot / One-shot / Few-shot** on the screen. Translate each in one line: *"0 examples / 1 example / 2–3 examples inside the prompt."*
- **Relatable hook (20 sec):** A **photographer clicks the same pose from 5 angles** before picking one for Instagram. Same with prompts — try 5, ship the best.
- **Screen-share the 5 things you can vary** (5 seconds each): role / tone / length / format / number of examples.
- **Live-demo the "EMI" mini-comparison from the Lecture Notes** — run all 4 versions back-to-back:
  1. Plain: *"Explain EMI."*
  2. Role: *"As a bank manager, explain EMI to a first-time loan taker."*
  3. Format: *"Explain EMI in 3 bullets, each under 15 words."*
  4. Example-based: *"Explain EMI using the example of a ₹5 lakh car loan for 5 years."*
- **Narrate:** Point at the progression — generic → friendly → crisp → concrete. Same topic, four flavours.
- **Lock-in line:** *"Companies hire Prompt Engineers **specifically** to do this testing. They are paid to find the version that converts, not the first one that runs."*

**Bridge sentence:** *"You are going to do exactly that job in the next 10 minutes — write a product description and A/B test 3 versions."*

---

## 11. In-Session Practice 5 — Prompt A/B Testing Challenge (10 minutes)

- **Screen-share:** The challenge card — *product description for a cotton kurta on a Meesho-like app*, and the 3 prompt variations (Zero-shot / Role+Format / Few-shot) from the Lecture Notes.
- **Timing split:**
  - **5 min** — run all 3 variations in ChatGPT, paste outputs into a doc side-by-side.
  - **3 min** — score each output out of 5 on **Clarity**, **Appeal**, **Length**. Pick a winner.
  - **2 min** — two volunteers share their winner and the *reason* it won.
- **Circulate.** Check that students actually ran **few-shot** with the sample description included — many will forget and run it like one-shot.
- **One student doubt to pre-empt:** *"Which version is always the best?"* → *"There is no single winner — that is why A/B testing exists. Short product listings → few-shot usually wins. Long essays → role-based. **Always test.**"*
- **Lock-in line:** *"You just wrote your first Prompt Engineering report — three versions, scored, with a recommendation. Put this in your portfolio."*

**Bridge sentence:** *"Theory and practice done for prompts. Now let us zoom out — **where** is all of this actually being used in companies?"*

---

## 12. Real-World Use Cases (6 minutes)

- **Screen-share:** The 10-use-case list from the Lecture Notes as two columns (title + 1-line description).
- **Say crisply:** *"These are not futuristic dreams — each of these is running in a real Indian company **right now**."*
- **Narrate each row in 10 seconds** — name the company students know:
  - Support bots → **Flipkart, Swiggy, Zomato**.
  - Coding assistants → **GitHub Copilot, Cursor**.
  - Research assistants → **Perplexity, NotebookLM**.
  - Sales email writers → **HubSpot, Apollo**.
  - Resume screeners → **Naukri, LinkedIn**.
  - Content creators → **Jasper, Copy.ai**.
  - Data analyst bots → **ChatGPT Code Interpreter, Julius AI**.
  - Legal assistants → **Harvey, Spellbook**.
  - Medical triage → **Practo's chatbot**.
  - Learning tutors → **Byju's AI, Khanmigo**.
- **Screen-share the 5-point "Good Use Case" checklist** from the notes — read once.
- **Cold-call:** *"Your college's hostel mess — could an AI agent help there? Which use case fits?"* (Accept: feedback summariser, menu suggestor, complaint-to-action bot.)

**Bridge sentence:** *"Picking a use case is half the job. The other half is **matching the right kind of agent** to that use case."*

---

## 13. Mapping Use Case → Agent Behavior (5 minutes)

- **Screen-share:** The **Quick Mapping Table** from the Lecture Notes (Use Case → Agent Needs To... → Key Tool).
- **Say it plainly:** *"A customer support bot and a research agent are **not the same thing**. Different personality, different tools, different memory."*
- **Relatable hook (20 sec):** The **hospital analogy** from the notes — receptionist / doctor / pharmacist. Same hospital, different roles. AI agents work the same way.
- **Narrate 2 rows of the table in detail:**
  - **Support bot** → needs FAQ knowledge + polite tone + escalation rule.
  - **Coding agent** → needs code tools + terminal access + debugger logic.
- **Cold-call:** *"For a **sales email writer** agent — what tools must it have?"* (CRM data + tone control + sample library.)
- **Check:** **Thumbs up** — *"Clear that the agent design **follows** the use case, not the other way around?"*

**Bridge sentence:** *"Designing this from scratch is exhausting. That is exactly why **frameworks** exist."*

---

# PART C — Frameworks & Agent Flow (≈ 22 minutes)

---

## 14. Why Frameworks Exist (5 minutes)

- **Screen-share:** *"Build a car from nuts and bolts?"* vs *"Buy a ready chassis?"*
- **Definition (one line):** *"An AI Agent Framework is a pre-built toolkit — memory, tools, planning, multi-agent — so you assemble agents instead of inventing every part."*
- **Relatable hook (30 sec):** The **MTR masala** analogy from the notes — grinding your own masala vs using a ready mix. Frameworks are the MTR masala of AI.
- **Screen-share the 6 things frameworks provide** (5 seconds each): LLM connectors / memory / tools / planning / multi-agent / logging.
- **Say it clearly:** *"Raw ChatGPT has **no memory of your business**, **cannot click buttons**, **cannot call another agent**. Frameworks add all three."*
- **Check:** **Thumbs up** — *"Clear that 'ChatGPT alone' ≠ 'AI agent'?"*

**Bridge sentence:** *"The three frameworks you will see on every job post — **LangChain, CrewAI, AutoGen**. One at a time, 3 minutes each."*

---

## 15. LangChain → CrewAI → AutoGen — fast tour (10 minutes)

- **Say it upfront:** *"You do not need to master all three today. You need to know **which one fits which situation**."*

- **LangChain (3 min):**
  - **Definition:** *"LEGO blocks for AI — pick a model block, a memory block, a tool block, snap them together."*
  - **Analogy:** Mumbai's **dabbawala network** — LangChain is the full workflow connector that picks up data, routes it, and delivers the answer.
  - **Best for:** *one smart agent with many tools* and *RAG* (answering from your own PDFs/docs).
  - **Name-drop real use:** Most chatbot-on-your-PDF products are built on LangChain.

- **CrewAI (3 min):**
  - **Definition:** *"A team of AI workers with defined roles, goals, and deadlines — like an office."*
  - **Analogy:** A **newspaper office** — reporter, editor, photographer, publisher. Each has a job. No one alone can run the paper.
  - **Show the 4-agent blog-writing crew from the notes:** Researcher → Writer → Editor → Publisher.
  - **Best for:** multi-step workflows with **clear role separation**.

- **AutoGen (3 min):**
  - **Definition:** *"A WhatsApp group for AI agents — they chat, argue, write code, agree on an answer."*
  - **Analogy:** Creating a WhatsApp group with a **CA + lawyer + doctor** for tough advice.
  - **Show the debugging conversation example** from the notes — coder agent + reviewer agent + user proxy.
  - **Best for:** **collaborative problem-solving**, especially where agents need to **run code** and verify.

- **One student doubt to pre-empt (1 min):** *"Can I use them together?"* → *"Yes — real projects often use **LangChain for tools** and **CrewAI or AutoGen for orchestration**. They are building blocks, not competitors."*

**Bridge sentence:** *"Three frameworks in 10 minutes. Now let us decide which one you pick **when**."*

---

## 16. Comparing Frameworks — the decision rule (4 minutes)

- **Screen-share:** The **Side-by-Side Comparison Table** from the Lecture Notes. Read across 3 rows in 60 seconds: **Main Idea / Best For / Multi-Agent Support**.
- **Burn the decision rule into memory — say it twice:**
  - *"One agent + your data → **LangChain**."*
  - *"Team of agents with roles → **CrewAI**."*
  - *"Agents chatting + running code → **AutoGen**."*
- **Cold-call 3 students back-to-back** (10 seconds each):
  - *"Build a chatbot to answer from our company's HR policy PDF — which framework?"* (LangChain.)
  - *"Build a content factory — researcher + writer + editor agents — which framework?"* (CrewAI.)
  - *"Build a data analysis agent that writes Python, runs it, and fixes errors itself — which framework?"* (AutoGen.)
- **Lock-in line:** *"If you can answer these three questions in an interview, you are already ahead of most people who say they 'know AI agents'."*

**Bridge sentence:** *"Frameworks understood. Now let us design an actual agent flow — pen and paper, no code."*

---

## 17. Designing a Simple Agent Flow (5 minutes)

- **Screen-share:** The 4 building blocks — **Input (Prompt) → Brain (LLM) → Hands (Tools) → Output (Result)**.
- **Say it crisply:** *"Every AI agent, even the fanciest one, is **this loop**. Just the tools and the prompt change."*
- **Relatable hook (20 sec):** The **food delivery flow** — take order → go to restaurant → pick food → deliver → take payment. Agents run the same kind of simple loop.
- **Walk through the "Career Advisor Agent" flow from the Lecture Notes** — read all 6 steps on the screen, point at each:
  1. User goal → 2. System prompt sets role → 3. LLM reasoning → 4. **Tool call** (job portal search) → 5. LLM writes final answer → 6. Output returned.
- **Call out Step 4:** *"**This** — the tool call — is the ONE thing that separates a real agent from a normal chatbot. Without tools, it is just ChatGPT."*
- **Check:** **Thumbs up** — *"Clear that Prompt → LLM → Tool → Output is the **backbone** of every agent we will build this course?"*

**Bridge sentence:** *"Now the capstone — you design **your own** agent in the next 8 minutes. Zero coding."*

---

## 18. Guided Mini Activity — "SaveSmart" Finance Coach Agent (8 minutes)

- **Screen-share:** The 6-step instructions from the Lecture Notes (Design System Prompt → Choose Role → Write User Prompt with C-I-F-C → Control Output → Try 3 Variations → Compare).
- **Say it clearly:** *"This activity combines **everything** we learnt today — system prompt + role + C-I-F-C + format + variations. All in one go."*
- **Timing split (announce):**
  - **4 min** — write your system prompt + user prompt (Steps 1–4) in a doc. Run it once in ChatGPT.
  - **3 min** — run **any 2 of the 3 variations** (A: strict father, B: 5 bullets no table, C: has a 2-year-old kid). Paste outputs side-by-side.
  - **1 min** — in a pair, decide which variation gave the **most useful and realistic** advice.
- **Circulate aggressively.** This is the exercise where every skill from today must show up — stop at 2–3 laptops and check *"where is your Context? where is your Constraint?"*
- **Lock-in line (say at 7-min mark):** *"You just built an agent. No Python, no LangChain, no API keys. This is the **foundation**. Everything in the rest of this course is just adding tools and automation on top of this."*

**Bridge sentence:** *"Let us wrap with the quick-recall table and the session's one-line takeaway."*

---

## 19. Summary, Cheat Sheet & Exit (3 minutes)

- **Screen-share:** The **"Important Concepts, Commands & Frameworks"** reference table from the Lecture Notes. Skim the 14 rows in 60 seconds — just *recognition*, not memorisation.
- **Say out loud the 5 things that must stick:**
  1. **System prompt** = identity, tone, boundaries.
  2. **Role prompting** = instant upgrade to any answer.
  3. **C-I-F-C formula** = every strong prompt.
  4. **Output format** = bullets for humans, JSON for machines.
  5. **LangChain / CrewAI / AutoGen** = one agent / team of agents / chatting agents.
- **Students do (60 seconds):** Write **one** prompt pattern you will reuse this week — either a system prompt idea or a C-I-F-C template.
- **Closing line:** *"Today you did **5 practices + 1 mini-project**. That is real Prompt Engineering experience, not just reading. From next class, we start wiring prompts to **tools** — that is when these prompts turn into actual **agents**."*

---

## Timing flex — if you are running late

- **Cut first from PART A:**
  - Block 5 (Practice 2 — 5 roles) — compress to **3 roles only** (kid / CEO / career counsellor). Saves ~4 min.
  - Block 7 (Practice 3 — Fix the Weak Prompt) — have students rewrite **2 of 4** weak prompts instead of all 4. Saves ~4 min.
  - Do **not** skip Practice 1 — that is the one that proves system prompts actually control behavior.

- **Cut first from PART B:**
  - Block 9 (Practice 4 — 4 formats) — drop the paragraph version; run only bullets / table / JSON. Saves ~2 min.
  - Block 11 (Practice 5 — A/B testing) — drop the "scoring out of 5" step; just ask for a winner and a one-line reason. Saves ~3 min.
  - Block 12 (Use Cases) — narrate only **5 of the 10** rows; skim the rest. Saves ~2 min.

- **Cut first from PART C:**
  - Block 15 (framework tour) — show only **LangChain + CrewAI** live; reduce AutoGen to 60 seconds of definition + analogy. Saves ~2 min.
  - Block 17 (Agent Flow) — skip the 6-step Career Advisor walk-through; just show the 4 building blocks on screen. Saves ~2 min.

- **Demo-only (no student activity):** Block 10 (Prompt Variations EMI demo) — show the 4 versions, skip the 5-minute student reproduction step if time is tight.

- **Minimum viable session:**
  - **Prompt Engineering intro** (Block 1).
  - **System Prompts** (Block 2) + **Practice 1** (Block 3).
  - **Role Prompting** (Block 4, demo only — skip Practice 2).
  - **C-I-F-C formula** (Block 6) + **Practice 3 trimmed** (2 prompts only).
  - **Output Format** (Block 8, demo only — skip Practice 4).
  - **Prompt Variations** (Block 10, demo only — skip Practice 5).
  - **Use Cases** (Block 12, narrate 5 rows).
  - **Frameworks decision rule** (Block 16 — the 3 cold-call questions).
  - **Mini Activity SaveSmart** (Block 18, trimmed to 5 min — run main prompt + 1 variation only).
  - **Exit** (Block 19).

- **If ahead of schedule:**
  - In Block 5 (Practice 2), add a **6th role** of the students' own choosing — most creative role wins applause.
  - In Block 11 (Practice 5), add a **4th variation** — chain-of-thought prompting (*"Think step-by-step before writing the description."*) — so students taste one more real technique.
  - After Block 16, add a **3-minute live debug** — deliberately write a terrible prompt (*"write email"*), show the bad output, then fix it live with C-I-F-C while narrating each addition.
  - In Block 18, ask 2 volunteers to share their **full SaveSmart prompt + output** on the projector for the class to critique in 60 seconds each.
