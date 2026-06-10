# Objective Assignment: Memory & Control Flow

## Instructions

- Questions 1 to 6 are **MCQs**. Choose **one correct option**.
- Questions 7 to 10 are **MSQs**. Choose **all correct options**.
- The questions are ordered from Easy to Moderate to Hard.

---

## Question 1

**Type:** MCQ  
**Difficulty:** Easy

An analyst asks a Tesla report bot: *"What is the annual revenue in 2022?"* and gets a correct answer. She then types only *"And in 2023?"* — no year repeated, no *"revenue"* repeated. The bot treats it as a brand-new question and asks her to repeat herself.

What is the **most likely** missing piece?

A. **Short-term memory** — prior user and assistant turns are not kept in conversation history  
B. A long-term vector database that stores analyst preferences across months  
C. Setting Groq `temperature` above 1.0 for creative follow-ups  
D. Re-chunking the Tesla PDF after every message

**Correct Answer:** A

**Answer Explanation:**  
A is correct because multi-turn follow-ups need the running chat history so *"And in 2023?"* still carries revenue context from turn 1.

B is incorrect because long-term memory is for cross-session facts, not the immediate follow-up problem. C is incorrect because temperature affects generation style, not whether earlier turns are remembered. D is incorrect because chunking is a prepare-step concern, not per-turn chat memory.

---

## Question 2

**Type:** MCQ  
**Difficulty:** Easy

Which pair best matches **short-term** vs **long-term** memory in a report-assistant product?

A. Short-term: running chat history for this session; Long-term: facts stored across sessions (for example in a database or vector store)  
B. Short-term: Chroma vector index; Long-term: Groq API key file  
C. Short-term: PDF chunk overlap size; Long-term: retriever value of k  
D. Short-term: system message only; Long-term: user messages only

**Correct Answer:** A

**Answer Explanation:**  
A is correct because short-term is the current session's message list; long-term persists knowledge across sessions.

B is incorrect because Chroma stores document chunks, not chat turns as the primary short-term pattern. C is incorrect because chunk overlap and k are retrieval tuning, not memory types. D is incorrect because both roles participate in history; neither maps to the short vs long distinction.

---

## Question 3

**Type:** MCQ  
**Difficulty:** Easy

A developer keeps conversation history only in a Python list inside a Jupyter notebook. They close the notebook without saving to disk. The next day they open a fresh kernel and type `print(history)`.

What happens?

A. The list is gone — in-memory variables do not survive a closed runtime unless history was **persisted** to a file  
B. Python automatically reloads all lists from RAM across kernel restarts  
C. The Chroma `./Tesla_db` folder stores chat turns by default  
D. Groq's free tier permanently stores every chat thread for replay

**Correct Answer:** A

**Answer Explanation:**  
A is correct because lists live in RAM for the current runtime; persist means writing to durable storage such as JSON.

B is incorrect because kernel restarts clear in-memory state. C is incorrect because the vector index holds document chunks, not the analyst chat transcript. D is incorrect because API providers do not replace your application's local history file.

---

## Question 4

**Type:** MCQ  
**Difficulty:** Easy

A multi-turn RAG notebook builds `history` as a list of `{"role": ..., "content": ...}` dicts.

Which growth pattern is **correct**?

A. Start with a **system** message, then append **user** then **assistant** for each completed turn  
B. Append **assistant** before **user** every turn because the bot speaks first  
C. Store only the latest **user** message and discard older turns to save tokens  
D. Put all turns in one string with no role field

**Correct Answer:** A

**Answer Explanation:**  
A is correct because the lab pattern uses system rules once, then user-assistant pairs in order for each turn.

B is incorrect because user speaks first in each exchange. C is incorrect because dropping older turns breaks follow-ups like *"And in 2023?"* D is incorrect because LLM APIs expect structured role/content messages.

---

## Question 5

**Type:** MCQ  
**Difficulty:** Moderate

After turn 1, `tesla_chat_history.json` correctly holds the 2022 revenue exchange. Before turn 2, a teammate deletes the call to `load_history()` and passes only the new string *"And in 2023?"* into the RAG helper.

What is the **most likely** failure?

A. Turn 2 loses context that the topic is **revenue** and the prior year was **2022**  
B. `json.load` raises an error because 2023 is invalid JSON syntax  
C. `MAX_STEPS` fires immediately because the file has only one turn  
D. Chroma removes vectors when `load_history()` is skipped

**Correct Answer:** A

**Answer Explanation:**  
A is correct because without reloading or passing history, the model sees an isolated short question with no thread context.

B is incorrect because the year 2023 in a message string is unrelated to JSON parsing. C is incorrect because max steps limits loop iterations, not missing reload. D is incorrect because skipping load does not mutate the vector index.

---

## Question 6

**Type:** MCQ  
**Difficulty:** Moderate

A production chat loop uses `while True` with no `MAX_STEPS` and no stop-word check. Analysts can ask questions indefinitely and history grows every turn.

What is the **primary** risk?

A. Runaway iterations, rising API cost, and no safe exit when the user wants to stop  
B. JSON files cannot store more than five messages by specification  
C. Groq automatically terminates every chat after exactly three turns  
D. LangChain retrievers force k=0 after ten queries

**Correct Answer:** A

**Answer Explanation:**  
A is correct because loop termination (max steps and stop words) prevents infinite chat and unbounded cost.

B is incorrect because JSON has no five-message limit. C is incorrect because providers do not enforce a three-turn cap in your loop. D is incorrect because k is a retrieval setting, not a chat-loop guard.

---

## Question 7

**Type:** MSQ  
**Difficulty:** Moderate

A team implements `save_history`, `load_history`, and `append_turn` for a Tesla analyst bot.

Which statements are **correct**?

A. `json.dump` writes the history list to a text file such as `tesla_chat_history.json`  
B. `load_history` can return an empty list on first run when the file does not exist yet  
C. `append_turn` should append **user** then **assistant** and save after each pair  
D. Writing history to JSON for this lab is identical to enterprise long-term memory in a vector database  
E. Saving only at the very end of a demo risks losing all turns if the kernel crashes mid-session

**Correct Answers:** A, B, C, E

**Answer Explanation:**  
A, B, C, and E match the persist/reload pattern from the lab.

D is incorrect because JSON here is short-term session persistence; long-term cross-session memory uses different storage (for example vector DB summaries).

---

## Question 8

**Type:** MSQ  
**Difficulty:** Moderate

A `run_chat_turn` function uses a bounded `while` loop with `MAX_STEPS = 5` and `STOP_WORDS = {"quit", "exit", "stop"}`.

Which behaviours are **valid** stop mechanisms?

A. User types `exit` → return a farewell message and skip further RAG lookups  
B. `step` reaches `MAX_STEPS` without a reply → return a polite step-limit message  
C. After one successful `rag_answer`, `break` because the task is done in the beginner lab  
D. Remove the `while` check and trust the LLM to say it is finished with no step limit  
E. Use `while True` forever because each API call is always cheap

**Correct Answers:** A, B, C

**Answer Explanation:**  
A, B, and C are the taught stop rules: user stop words, max steps, and task-done break.

D is incorrect because models can loop without a hard ceiling. E is incorrect because unbounded loops are unsafe for cost and runtime.

---

## Question 9

**Type:** MSQ  
**Difficulty:** Hard

An engineer wraps `client.chat.completions.create` in `try/except` inside `run_chat_turn`. Groq returns a rate-limit error mid-demo.

Which responses follow **user-visible error handling** best practices?

A. Do not let an uncaught traceback crash the analyst-facing flow  
B. Return or print a short, friendly message (for example search unavailable, try again)  
C. Return `str(exception)` directly to the analyst for maximum transparency  
D. Catch failures at the API call site, not only in a distant outer notebook cell  
E. When using a `safe_rag_answer` pattern, reject blank input before any API call

**Correct Answers:** A, B, D, E

**Answer Explanation:**  
A, B, D, and E match the lab: catch at call site, friendly text, no raw tracebacks to users, guard blank input.

C is incorrect because exposing internal exception strings erodes trust in demos.

---

## Question 10

**Type:** MSQ  
**Difficulty:** Hard

A team adds multi-turn memory to an existing grounded Q&A helper on a Tesla index.

Which design choices are **sound**?

A. `build_question_with_memory` joins prior roles and the new message before calling `rag_answer`  
B. Call `load_history()` before turn 2 so the JSON file carries the turn 1 exchange  
C. Pass only the latest user bubble — high retriever k makes history unnecessary  
D. When token limits are hit in very long chats, **summarization** can compress older turns  
E. **Gradio** can wrap `run_chat_turn` for a quick POC chat UI but is not a production front-end replacement

**Correct Answers:** A, B, D, E

**Answer Explanation:**  
A, B, D, and E align with the memory + control-flow lab: full history for RAG, JSON reload, summarization as a production guardrail, Gradio for demos only.

C is incorrect because retrieval breadth does not replace conversation history for pronoun-style follow-ups like *"And in 2023?"*
