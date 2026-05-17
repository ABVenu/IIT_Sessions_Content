# Lecture Script: Open-Source LLMs

**Session duration:** 2 hours 15 minutes  
**Audience:** Absolute beginners — Indian learners who may have no formal tech background; goal is to install Ollama, run a small local model, call it from Python, and optionally try Ollama Cloud — not deep ML theory.

---

**How to use this document**  
This file is **for timing and facilitation only**. It does not replace the lecture notes or student handouts; it tells you *what to do in the room*, where to circulate, how to demo, and when to pause for checks. Lean on `Lecture Notes.md` for definitions, examples, full code, and troubleshooting tables.

**Break rule**  
After **approximately 58–68 minutes from session start**, take **one pause of 5–8 minutes**. Do **not** count the break as a numbered block below; resume afterward with Python + local Ollama.

---

## 1. Opening, Recap Bridge & Today's Map (8 minutes)

- Screen-share the opening section of Lecture Notes.md — **one minute** recap: last time was **prompt engineering** (system vs user, few-shot, chain-of-thought, agent flows); today is **where the model runs** (your laptop vs cloud).
- Read the outcome bullets aloud; emphasize: *install once, practise free, same Python pattern later for RAG and agents*.
- Show cloud-vs-local image briefly (`session37-01-cloud-vs-local.png`) — Swiggy vs home-cooking analogy in your own words.
- **Cold-call:** "Why might a college team keep placement data on a local model instead of a US API?"
- **Thumbs up:** "Who already tried ChatGPT or any LLM in a browser?" — normalize mixed experience.

**Bridge sentence:** "Prompts are how you ask; today we choose *which kitchen* cooks the answer — cloud or your own machine."

---

## 2. Cloud vs Local & What Is Ollama (12 minutes)

- Walk the limits table: cost, privacy, learning, agent path — mention **upcoming RAG topics** plug into Ollama like OpenAI (one line, no deep dive).
- **Common doubt** aloud: "If local is free, why OpenAI?" — quality and hardware answer in 30 seconds.
- Transition to **What is Ollama**: app store + player analogy; show `session37-02-what-is-ollama.png`.
- Skim capabilities table — highlight **chat** today, **embeddings** as teaser for the library/RAG arc ahead; vision/audio = "exists, not our lab focus."
- Point to `localhost:11434` on slide — "This port is your local AI counter."

**Bridge sentence:** "Theory is useless until Ollama is on your machine — let's install and prove it with a version command."

---

## 3. Install Ollama & Verify (14 minutes)

- Screen-share OS-specific steps from notes (Windows / Mac / Linux tabs or slides); keep download page open: [ollama.com/download](https://ollama.com/download).
- Live demo on instructor machine: `ollama --version` and `ollama list` (empty list is fine).
- **Room action:** Post the three-row health-check table; students run steps 1–2 on their laptops.
- **Circulate** — top failures: Ollama app not running, Windows PATH, corporate firewall blocking download.
- **Check for hands:** "Raise hand when `ollama --version` prints a number."

**Integrated activity (~6–8 min inside this block)** — from Lecture Notes *Install & Verify*:
- Students complete install + `ollama list`; neighbour helps if stuck.
- Note one volunteer per OS for later debugging stories.

**Bridge sentence:** "Ollama is installed — next we download a *small* brain so nobody's laptop catches fire."

---

## 4. Pull a Light Model & CLI Prompt Battle (16 minutes)

- **Warn before pull:** standardize class model tag (e.g. `qwen2.5:0.5b` or `llama3.2:1b`); show **avoid 70B+** slide/table — scooter vs truck.
- Live terminal: `ollama pull <class-model>` then `ollama run <class-model>` with one simple prompt (photosynthesis or breakfast example from notes).
- Mention `/bye` or Ctrl+D exit; flash `ollama list` and `ollama ps`.
- Show `session37-04-small-vs-heavy-models.png` if time.

**Student activity — CLI Prompt Battle (~10–12 min)**  
- Everyone uses the **same** model tag.  
- Three prompts on screen: (1) math word problem, (2) Hindi translation, (3) 50-word story.  
- **Pair-share:** one hallucination or vague line spotted in partner's output.  
- **Cold-call** one pair: "What did the tiny model get wrong?"

> **Break placement:** If this block ends near **58–68 minutes**, announce **5–8 minute break** now. If you are still before ~55 minutes, add a 3-minute trade-offs teaser (Block 5 preview) or extra pair-share until the window, then break. If you are **past 72 minutes**, take break immediately and trim post-break activities per Timing flex.

---

**Break:** 5–8 minutes. Students restart Ollama app if it slept; defer long cloud billing questions to Block 7.

---

## 5. Trade-offs of Very Small Local Models (7 minutes)

- Exam-essay / first-year lawyer analogies — **hallucination** on obscure facts is expected.
- Walk advantage vs disadvantage table quickly.
- Tie to prompt engineering: "If unsure, say you don't know" + later **RAG** for facts.
- **Thumbs up:** "Who saw our model sound confident but wrong in the CLI battle?"

**Bridge sentence:** "Small models are fine for learning APIs — your code will talk to Ollama the same way production does."

---

## 6. Python Local Call — Teach & Activity (16 minutes)

- Show API flow image (`session37-05-ollama-api-flow.png`): Python → `localhost:11434` → reply.
- `pip install ollama` on screen; open `ask_ollama_local.py` from notes — scroll with **line-by-line** comments, do not rush.
- Run once live; show connection error fix checklist (app open? model pulled?).
- **Circulate** during student run.

**Student activity — Python Local Call (~8–10 min)**  
- Run script with class prompt: *"Explain blockchain to my grandmother in 80 words."*  
- Change only `user_question` and re-run once.  
- **Cold-call** one student: read first sentence of output aloud.

**Bridge sentence:** "Local is free practice; when the laptop is too small, Ollama Cloud rents a bigger kitchen — same recipe, different address."

---

## 7. Ollama Cloud — Account, API Key & Python Client (14 minutes)

- Walk sign-up and API key creation ([ollama.com/settings/keys](https://ollama.com/settings/keys)); **never** paste keys into chat or GitHub — env vars only.
- Demo `export OLLAMA_API_KEY=...` (or PowerShell equivalent) on instructor machine — blur key on screen-share.
- Open `ask_ollama_cloud.py` — highlight only what changed: `Client`, `host=https://ollama.com`, `Authorization` header.
- Run one cloud call if network allows; if not, show recorded output or instructor-only fallback.
- Optional: mention `ollama signin` and cloud-tagged pulls — do not let class pull huge models during lab.

**Bridge sentence:** "Same question, two kitchens — let's compare answers fairly."

---

## 8. Local vs Ollama Cloud Comparison (10 minutes)

- Put **one standardized prompt** on screen (notes suggest blockchain or agent definition — pick one and keep all year).
- Run local script vs cloud script back-to-back on projector; read **one** quality difference aloud (reasoning depth, language, factual caution).
- Skim comparison table in notes — trust vs hackathon framing.

**Student activity — shortened Local vs Cloud Showdown (~5–6 min if time)**  
- Pairs run both modes OR instructor posts two outputs in shared doc.  
- Quick vote: **trust for homework** vs **trust for demo**.  
- If behind schedule: instructor-only demo, students discuss in pairs from projected text.

**Bridge sentence:** "You've seen text models; Ollama also offers other input types and the numbers behind search — quick tour, then one script to rule both modes."

---

## 9. Model Types & Embeddings Preview (9 minutes)

- Table walk: text / vision / audio / video — "pull only what you need."
- **Embeddings** section: meaning-space analogy; show `session37-08-embeddings-meaning-space.png`.
- Run **minimal** `embed` snippet live OR pre-run output — print vector length + first five numbers only.
- One closing line: *"Next topics store these numbers in a vector database and retrieve them for RAG."*
- `ollama pull nomic-embed-text` — assign as homework if not done live.

**Bridge sentence:** "Last capstone: one Python file, one flag — local or cloud — so you never maintain two projects."

---

## 10. Unified Script — Local or Cloud Capstone (12 minutes)

- Screen-share `ask_ollama.py` — focus on `USE_CLOUD`, `ask_local`, `ask_cloud`, `main()` only (skip line-by-line if behind).
- Toggle `USE_CLOUD=0` then `1` on projector if API key available.
- Show `session37-09-one-script-toggle.png`.

**Capstone checklist — room check (~5–6 min)**  
- **Circulate** with checklist from notes; spot-check **three** laptops for: version, pull, local answer, cloud answer (cloud optional if keys missing).  
- **Hands:** who completed all local items?  
- Do **not** require every student to finish cloud in class if keys are still generating.

**Bridge sentence:** "Ollama is one tool in a bigger open ecosystem — thirty seconds of context, then we close."

---

## 11. Ecosystem Teaser, Takeaways & Close (6 minutes)

- Three bullets: Hugging Face, llama.cpp/vLLM, **read licenses** before commercial use.
- Rapid recap: local privacy/cost, `pull`/`run`, tiny-model limits, Python + env keys, one toggle script.
- Skim terminology table — spotlight `localhost:11434`, `OLLAMA_API_KEY`, `embed`, **RAG** as coming attraction.
- **Exit ticket (verbal):** "One command you'll run tonight to practise."
- Logistics: homework = finish capstone checklist; pre-pull embed model for upcoming library/RAG topics.

---

## Timing flex — if you are behind schedule

Cut in this **order** (fastest wins first):

1. Shorten Blocks **1** and **11**; glossary table → "read in notes."
2. Block **8** — instructor-only comparison; drop pair vote.
3. Block **9** — embeddings: show screenshot of output instead of live `embed`.
4. Block **10** — demo capstone on projector only; checklist becomes homework.
5. Block **7** — explain cloud env vars without live cloud call if API/network blocks class.
6. Block **4** — reduce CLI battle to **two** prompts instead of three.

**Never cut first:** install verify (Block 3), one successful `ollama run` (Block 4), one local Python call (Block 6).

If you are **ahead**, extend Block **4** CLI discussion or Block **8** pair comparisons; optional volunteer screen-share of worst hallucination — keep **hands-on terminal time** over extra slides.

**If break was skipped early**, take it before Block 6 so Python lab has fresh attention.
