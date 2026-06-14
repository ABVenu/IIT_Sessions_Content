# Lecture Script: Hands-On LangChain

**Session Duration:** 1 hour 50 minutes  
**Target Audience:** Learners from diverse backgrounds, including those without prior technical training. Delivery stays concrete, cricket-themed, and jargon-light until terms are defined.

**How to use this document:** This file is for **timing and facilitation only**. It is not a transcript. Use the numbered blocks to pace the room, manage demos, and trigger participation; adapt wording to your style. Lean on `Lecture Notes.md` for definitions, code, and diagrams.

**Break rule:** After **55–65 minutes** of instruction, take **one** pause of **5–8 minutes** (not a numbered block). Do not add extra formal breaks in the run-of-show.

---

## 1. Welcome, Module 3 Map, and Setup Check (10 minutes)

- Welcome the group; frame today as a **Module 3 recap masterclass** — not a new theory lecture. One file, three phases, end-to-end LangChain.
- Screen-share the **Module 3 at a Glance** table from Lecture Notes (LCEL → tools → AgentExecutor → memory → RAG → integrated agent → eval preview).
- **Engagement — cold-call:** "Which row in this table did we use when the model had to *pick* between two actions?" (Tools / tool arbitration.)
- **Room action:** Ask everyone to open their IDE, confirm they have a project folder `langchain_hands_on` (or equivalent).
- **Engagement — thumbs up:** "Is Ollama running? Have you pulled `qwen2.5:0.5b` and `nomic-embed-text` before?" Circulate and help with `ollama list` / service not started.
- Quick poll: `python3 --version` and whether `venv` from earlier Module 3 work still exists.

**Bridge sentence:** "You have the map — next we see the one app that stitches every row together: the T20 Rules & Match Inquiry Assistant."

---

## 2. T20 App Story, Architecture, and Three-Phase Agenda (8 minutes)

- Narrate the domain: **T20 cricket** — rulebook search vs live match incident log vs polite refusal. Not another e-commerce bot.
- Screen-share the **broadcast analyst** and **two-source architecture** images from Lecture Notes.
- Walk the four-part table: `t20_rules_search_tool`, `get_match_incident`, `chat_history`, safety refusal.
- Show the **one file, three phases** diagram: `demo_lcel_chain()` → build → `run_eval()`.
- **Pair-share (2 min):** "In one sentence, why does a rules assistant need *two* data sources?" One volunteer reads aloud.

**Bridge sentence:** "Story is set — let's make sure every laptop can run the stack before we touch code."

---

## 3. Environment Setup and Full File Bootstrap (10 minutes)

- **Live-coding / screen-share:** Run setup commands from Lecture Notes:

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install langchain-core langchain-ollama langchain-chroma langchain-text-splitters langchain-classic
```

- **Room action:** Students mirror commands; circulate for pip errors and wrong interpreter.
- Create **`t20_rules_assistant.py`**; paste the **full file** from Lecture Notes (all three phases). Tell students: we will *run* sections in order, not hunt across seven files.
- **Engagement — thumbs up:** "Does your file open with the import block and three `PHASE` comment headers?"
- If someone is behind: share file via chat or repo link; they catch up during Phase 1.

**Bridge sentence:** "File is on disk — Phase 1 proves the simplest chain still works before we build the agent."

---

## 4. Phase 1 — LCEL Warm-Up and Swap-Topic Activity (12 minutes)

- **Live-coding:** Walk `demo_lcel_chain()` — `ChatPromptTemplate` → `ChatOllama` → `StrOutputParser` → `chain.invoke`.
- Narrate the pipe operator: output flows step by step (coffee filter / third-umpire DRS analogy from Notes).
- Students run:

```bash
python3 -c "from t20_rules_assistant import demo_lcel_chain; demo_lcel_chain()"
```

- **Room action:** Circulate; common failures: Ollama not running, wrong `base_url`, model not pulled.
- Screen-share **LCEL warm-up** diagram briefly.
- **Activity (3 min):** Students change invoke topic to `"wide ball rules in T20"`, re-run — only input changes; code stays identical.
- **Engagement — cold-call:** "What are the three runnables in the chain, left to right?" (Prompt, LLM, parser.)

**Bridge sentence:** "Warm-up passed — now we ingest the T20 rulebook and expose it as a searchable tool."

---

## 5. Phase 2a–2b — Rulebook Corpus and RAG Ingest Path (15 minutes)

- Scroll to **`T20_RULE_DOCS`** — six inline `Document` objects; production would use PDF loaders.
- **Live-coding:** Trace ingest path aloud: splitter → `OllamaEmbeddings` → `Chroma.from_documents` → `_retriever` → `create_retriever_tool`.
- Screen-share **RAG ingest path** and **powerplay aerial** images.
- Emphasize: same offline → online RAG flow from class; difference is retrieval lives **inside a tool** (agentic RAG).
- **Engagement — cold-call:** "What does `k=2` in `search_kwargs` control?" (How many chunks come back per search.)
- **Room action:** Students re-run Phase 1 only if Chroma first-time embed is slow on weak machines — narrate that embedding runs at import time when the full file loads.
- Quick table from Notes: powerplay / free hit / DRS → example user questions.

**Bridge sentence:** "Rulebook is indexed — next we add the live match log and teach the agent to choose the right tool."

---

## 6. Phase 2c — Tool Arbitration and `get_match_incident` (12 minutes)

- Walk **`MATCH_INCIDENTS`** dict and `@tool` decorator on `get_match_incident`.
- Screen-share **tool arbitration** diagram — rule question → search tool; `INC-xxx` → incident tool; IPL auction → neither.
- Read tool **descriptions** aloud — stress that routing failures are fixed here first, not by swapping model size.
- Show `TOOLS = [t20_rules_search_tool, get_match_incident]`.
- **Engagement — pair-share (2 min):** Fill two rows of the routing table mentally: powerplay fielders → which tool? INC-102 → which tool?
- **Cold-call:** "Why can't the rulebook tool answer incident INC-101?" (Static handbook ≠ live scorer's log.)

**Bridge sentence:** "Two tools are registered — now we wire the agent, memory, and the `ask()` interface."

---

## 7. Phase 2d — Agent, Memory, and `demo_live_queries()` (14 minutes)

- Walk `_agent_prompt`: system rules, `MessagesPlaceholder` for `chat_history` and `agent_scratchpad`.
- Contrast table from Notes: **chat_history** (you maintain across turns) vs **agent_scratchpad** (executor fills per run).
- Show `create_tool_calling_agent`, `AgentExecutor` (`verbose=True`, `max_iterations=4`, `handle_parsing_errors`).
- Walk `ask()` — invoke, then append `HumanMessage` / `AIMessage`.
- **Live-coding:** Run `demo_live_queries()` — narrate Q1–Q4; students watch **verbose** trace for tool names.
- **Engagement — thumbs up:** "Did Q1 show `t20_rules_search_tool` in your terminal trace?"

**Bridge sentence:** "The app runs — let's prove routing and memory deliberately, then break memory on purpose."

---

## 8. Tool Routing Table and Break-Memory Activity (11 minutes)

- **Activity — Tool Routing Table (6 min):** With `verbose=True`, students fill the table from Notes for all four demo queries.
- **Room action:** Circulate; if incident ID triggers rule search, prompt students to sharpen `get_match_incident` description — do not change model yet.
- **Activity — Break Memory on Purpose (5 min):** Comment out the two `chat_history.append` lines in `ask()`; re-run Q2 and Q3 — Turn 3 should forget INC-101.
- **Engagement — cold-call:** "What failure signature is that?" (Missing memory.)
- Restore append lines before moving on.

**Bridge sentence:** "You have seen live behaviour and one failure signature — Phase 3 turns that into a repeatable exam paper."

---

## 9. Phase 3 — EvalPack, Failure Signatures, and One Patch (10 minutes)

- Walk `EVAL_CASES` — three cases: powerplay rule, incident lookup, out-of-domain refusal.
- Explain `chat_history.clear()` between cases — prevents memory bleed into eval.
- Students run:

```bash
python3 -c "from t20_rules_assistant import run_eval; run_eval()"
```

- Screen-share **EvalPack** diagram and failure-signatures table from Notes.
- **Activity — One Patch Iteration (4 min):** If any case fails, change **one** thing — tool description, `chunk_size`, or one system-prompt line — re-run that case only.
- **Engagement — cold-call:** "Wrong tool on incident ID — what do you fix first?" (Tool description.)

**Bridge sentence:** "Eval gives you a feedback loop — we'll close by checking you can explain the file without looking."

---

## 10. Confidence Checkpoint, Takeaways, and Wrap-Up (8 minutes)

- Rapid-fire five questions from Lecture Notes **Confidence Checkpoint** — cold-call volunteers; pause for pair-help if stuck.
- Recite key takeaways: one file three phases; tool arbitration; `ask()` + memory; EvalPack + failure signatures → targeted fixes.
- Point to **Why Each Import and Package Is Needed** table for post-session revision.
- **Engagement — exit ticket (chat or verbal):** "Name one difference between `agent_scratchpad` and `chat_history` in your own words."
- Mention upcoming formal eval harness and multi-agent work — this lab is the bridge.

**Bridge sentence:** *(Session end — no further block.)*

---

## Timing Flex

| If you are **behind** | Cut or shorten |
|------------------------|----------------|
| 8–10 min late | Shorten Block 2 to 5 min; skip pair-share |
| 12–15 min late | Paste full file for everyone via chat; skip Block 5 table walk — only live trace in Block 7 |
| 18+ min late | Skip Break-Memory activity; describe outcome verbally |
| 20+ min late | Run instructor machine demo for `demo_live_queries()`; students only run Phase 1 + `run_eval()` |
| If you are **ahead** | Let students add one custom `EVAL_CASES` row; peer-review expected tool |

| If you are **ahead** | Add |
|----------------------|-----|
| 5–8 min spare | Students tweak `chunk_size` / `k` and note retrieval change on powerplay question |
| 10–15 min spare | Homework preview: add one new `Document` to `T20_RULE_DOCS` and re-index |

**Hard stop at 1 hour 50 minutes:** Ensure everyone has run Phase 1 successfully, seen at least one verbose tool trace in Phase 2, and executed `run_eval()` once.

---

## Lecture Notes Alignment Map

| Script block | Time | Lecture Notes section | Key functions / activities |
|--------------|------|------------------------|----------------------------|
| 1 | 10 min | Module 3 at a Glance + Before You Start | Ollama / venv check |
| 2 | 8 min | What You Will Build + Today's Hands-On Agenda | Architecture images; three-phase map |
| 3 | 10 min | Before You Start — Quick Setup + Complete App paste | `pip install`, `t20_rules_assistant.py` |
| 4 | 12 min | Phase 1 — LCEL Warm-Up | `demo_lcel_chain()`, swap-topic activity |
| 5 | 15 min | Phase 2 — 2a Rulebook + 2b Ingest path | `T20_RULE_DOCS`, Chroma, `t20_rules_search_tool` |
| 6 | 12 min | Phase 2 — 2c Match incident tool | `get_match_incident`, tool arbitration |
| 7 | 14 min | Phase 2 — 2d Memory + agent | `ask()`, `demo_live_queries()` |
| 8 | 11 min | Activities — Tool Routing + Break Memory | Verbose trace table; comment out `chat_history.append` |
| 9 | 10 min | Phase 3 — Eval and Debug Drill | `run_eval()`, failure signatures, one patch |
| 10 | 8 min | Confidence Checkpoint + Key Takeaways | Five questions; import table pointer |

**Break placement:** After Block 5 or early Block 6 (~55–65 min cumulative).

**Images to screen-share from Notes:**

- `masterclass01-creative-01-ipl-night-stadium.png` (Block 1)
- `masterclass01-02-t20-app-two-sources.png` (Block 2)
- `masterclass01-01-one-file-three-phases.png` (Block 2)
- `masterclass01-07-lcel-warmup.png` (Block 4)
- `masterclass01-03-rag-ingest-path.png` (Block 5)
- `masterclass01-04-tool-arbitration.png` (Block 6)
- `masterclass01-05-memory-scratchpad.png` (Block 7)
- `masterclass01-06-evalpack.png` (Block 9)
