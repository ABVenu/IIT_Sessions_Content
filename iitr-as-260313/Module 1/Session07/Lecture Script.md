# Lecture Script: Defining Agentic Systems & Core Components

**Session duration:** 2 hours 15 minutes  
**Audience:** Indian students from varied backgrounds; limited or no prior tech exposure. Delivery should stay concrete, analogy-heavy, and avoid jargon without a plain-language gloss.

---

## How to use this document

This file is for **timing and facilitation only**. It is not a verbatim transcript. Use the blocks to pace the room, manage screen-share and activities, and decide when to pause for checks. Adapt wording to your voice; keep the time boxes and engagement beats.

---

## Break rule (not a numbered block)

After roughly **60–75 minutes** of instruction, take **one** break of **5–8 minutes**. Do not schedule multiple formal breaks in the script. If you start late or need to compress, shorten the break or merge light content (see Timing flex at the end).

---

## 1. Opening, learning outcomes, and “What is an AI agent?” (16 minutes)

**Facilitator actions**

- Screen-share the session title slide or first section of the lecture notes; read the objective aloud in one sentence: *fundamental components that make an AI system agentic*.
- Quick poll (hands or chat): “Who has used Google Maps turn-by-turn, Swiggy/Zomato, or a bank chatbot in the last week?” Acknowledge—this session names what is happening behind those experiences.
- Teach the core idea: goal + autonomy—Maps plans the route and reroutes; you did not script every turn. Tie to **official definition** (perceive → decide → act toward a goal without step-by-step human steering).
- Give **two India-relatable examples** from the notes: food apps (find, compare, pay) and placement officer matching “5 engineers” without micromanagement.
- **Python bridge (2 minutes):** Remind them prior sessions covered `if`, `for`, `def`, `class`—today is **concepts**; building agents in Python comes later. Ask for a **thumbs up** if that distinction is clear.

**Students do**

- Recall one app that “felt smart” and be ready to name it if cold-called.
- Note mentally: today = vocabulary and mental model, not coding yet.

**Engagement**

- **Cold-call** one student: “In one line, what did *you* ask the app to do vs what the app figured out itself?”

**Bridge sentence**

“Now that we have a working picture of an agent, we need to sharpen what it is *not*—because most software you have used is built the other way.”

---

## 2. Traditional systems vs AI agents (12 minutes)

**Facilitator actions**

- Contrast **traditional** (fixed recipe, breaks on surprise) with **agent** (reason, adapt, use tools). Use **ATM** and **traffic light** vs **support bot** and **smart traffic** from the notes.
- Walk the **side-by-side table** on screen; read the “key difference in one line” slowly.
- Optional **pair-share (2 minutes):** In pairs, name one traditional tool and one agent-like tool they used this week; pair reports one example.

**Students do**

- Classify mentally: “fixed rules” vs “thinks toward a goal.”

**Engagement**

- **Thumbs up / thumbs sideways:** “Comfortable explaining to a friend why an ATM is *not* an AI agent in the sense we mean today?”

**Bridge sentence**

“Agents are not magic—they are built from pieces. Every agent, simple or fancy, stands on four pillars; we will spend most of today on those four.”

---

## 3. The four pillars — overview and Component 1: Planning (20 minutes)

**Facilitator actions**

- List the four: **Planning, Reasoning, Memory, Action.** Introduce the **secretary / annual event** metaphor; say you will reuse it.
- **Planning — deep dive:**
  - Assignment and **IRCTC** step list; emphasize **order matters** (cannot pay before passenger details).
  - **Cricket captain field placement** — plan before random action.
  - Walk **how planning works inside an agent:** goal → decompose → order → checklist → complete.
  - **Biryani disaster** without sequence—light humour, serious point.
  - Show the **Python list** mental model (`plan = [...]`, `for` loop). No live coding required unless you want a 60-second demo in IDE.
- Address **common doubt:** internal written plan / “task plan” / chain of thought—preview that frameworks make this visible later.

**Students do**

- Silently order two steps for a familiar task (e.g. “submit assignment online”)—then compare with your spoken answer.

**Engagement**

- **Cold-call:** “Which IRCTC step would break if you swapped it with payment?”

**Bridge sentence**

“A plan tells you *what* to do in order; next we cover what happens when the world refuses to cooperate—that is reasoning.”

---

## 4. Component 2: Reasoning (16 minutes)

**Facilitator actions**

- Open with **train fully booked** scenario: traditional message vs agent considering waitlist / alternate route.
- Definitions: analyze, conclude, choose under uncertainty.
- **Doctor** and **cricket captain 40th over** examples—keep each tight.
- Walk the **five-step** reasoning flow (context → options → evaluate → best action → update).
- **Crucial distinction:** Planning = *before* you start; Reasoning = *as you go*. Repeat **dressing-room strategy vs on-field captain** and **route before drive vs U-turn when jammed**.
- Rapid-fire **types:** if-else, comparison, fallback, clarification—link if-else to Python.
- **Common mistake:** reasoning vs random guessing—why wrong matters for real tasks.

**Students do**

- Think of one “unexpected thing” that could happen mid–train booking.

**Engagement**

- **Pair-share (90 seconds):** One partner states a plan; the other names one thing that could go wrong and what they would do next.

**Bridge sentence**

“Reasoning needs good inputs—and it needs to remember what already happened. That is memory.”

---

## 5. Component 3: Memory — short-term vs long-term (16 minutes)

**Facilitator actions**

- **Bank call-center** frustration story → why memory matters.
- **WhatsApp history** and **kirana shopkeeper** examples.
- **Why memory is glue:** no repeat searches, personalization, smart vs dumb bot.
- **Two types:**  
  - **Short-term / working / context:** RAM analogy, exam problem numbers, current chat.  
  - **Long-term:** SSD/notebook, travel preferences, Spotify Wrapped.
- Walk the **comparison table** (duration, storage, speed, lost when, Python-ish equivalent).
- **Both needed** + **common mistake:** only short-term → user repeats forever.

**Students do**

- Point to chat: one example of something that should be short-term only vs long-term for a real assistant.

**Engagement**

- **Thumbs check:** “Short-term = this conversation only. Long-term = still there next month. Clear?”

**Bridge sentence**

“Internal work is useless if nothing ever reaches the outside world—actions are what users see and feel.”

---

## 6. Component 4: Action (10 minutes)

**Facilitator actions**

- **Waiter** and **manager phone call** analogies—action completes the loop.
- **Types:** API, web search, file ops, code execution, comms, DB—one sentence each.
- Mini **news summary** example chaining search + code + reply.
- **Visibility:** planning/reasoning/memory hidden; actions visible—why bad actions hurt.
- **Doubt:** generating text *is* an action. Show tiny `send_confirmation` snippet if projecting notes.

**Students do**

- Name one “small” action and one “big” action from the list.

**Bridge sentence**

“We have four parts; agents do not run in a straight line—they cycle. Here is the heartbeat: Observe, Think, Act.”

---

## 7. The agent loop: Observe → Think → Act (12 minutes)

**Facilitator actions**

- Draw or display the **loop diagram** from the notes step by step.
- Walk **order cancellation** example across Observe / Think / Act rounds—including shipped vs not shipped branch.
- **Why a loop:** new information after each action; **cooking** and **detective** analogies—short.
- **How many loops:** 2+2 vs full Goa trip—sets expectations.

**Students do**

- Trace with you: after “Act,” what becomes the next “Observe”?

**Engagement**

- **Cold-call:** “In the cancellation story, what did the agent *observe* right after calling the API?”

**Bridge sentence**

“Now we snap the four components into one picture and stress-test with full stories.”

---

## 8. How the four work together + Food ordering use case (14 minutes)

**Facilitator actions**

- **Secretary table** (Planning / Reasoning / Memory / Action) — read as a chain, not silos.
- **Failure of one link** — quick four bullets (poor memory → wrong reasoning, etc.).
- **Food ordering walkthrough** from notes: read rounds at a steady pace; highlight **no address asked** (LTM), **speed vs rating** (reasoning), multiple loops, real APIs.
- Pause once: “What made this *agentic*?”

**Students do**

- Follow along on split screen or PDF; optional annotation on a printed one-pager if you distribute it.

**Engagement**

- **Quick show of hands:** “Which component saved the most back-and-forth with the user in this example?”

**Bridge sentence**

“Same machinery applies to something closer to your careers—job search—and then we look at when agents fail.”

---

## 9. Job application use case, failure modes, wrap-up, quick reference (19 minutes)

**Facilitator actions**

- **Job assistant:** outline steps 1–7; stress **reasoning checkpoints** (LinkedIn only, stale posting, PDF vs Word); **memory** (resume path, profile); **actions** listed.
- **Failure modes (keep punchy):** Bad planning (wrong order, skipped verification); Memory failure (repeat DOB); Reasoning error (budget vs proximity); Wrong action (bad email, wrong column). One line each on **why agent failures are worse** than chatbot wrong answers.
- **Big picture recap:** four components + loop + what makes behavior “agentic.”
- **What is next:** Python implementation tease.
- Flash the **Quick Reference table**—offer to leave it on screen for photos; no need to read every row aloud.

**Students do**

- Self-check: can they name one failure type and one fix?

**Engagement**

- **Exit ticket (chat or slip):** “One component you want to see in code first—and one risk you will watch for when building agents.”

**Bridge sentence**

“That closes our conceptual map; next sessions turn these ideas into working logic—see you with Python and patience for edge cases.”

---

## Timing flex

**If you are 10–15 minutes behind**

- Shorten Block 2 (pair-share optional).  
- In Block 4, cover reasoning *types* as a list only, skip extended pair-share.  
- In Block 8, narrate the food use case at high level (rounds 1–2 only) instead of every line.

**If you are 15–25 minutes behind**

- Merge Block 6 (Action) into Block 7: define action types in one slide, then go straight into Observe–Think–Act with the news-summary bullet as the only chained example.  
- Cover **Job use case** as a bullet list, not a full walkthrough.  
- Summarize **failure modes** as a four-row table with examples only, no extended discussion.

**If you finish early**

- Deepen **failure mode** discussion with a live “what would you verify?” on sales report or hotel booking.  
- Optional: 5-minute **silent read** of Quick Reference + ask three terms cold-call style.

**Break placement**

- If you took the break after Block 5, resume with Block 6 (Action). If the room is fatigued earlier, break after Block 4 and trim Block 9’s exit ticket.
