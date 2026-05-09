# Subjective Assignment — Short-Term vs Long-Term Memory in AI Agents

**Total Questions:** 1 | **Type:** Practical Coding Task | **Difficulty:** Medium

---

## Q1 — Build a Window Memory Study Assistant

Kavya is building a study assistant chatbot for her university's AI club. The assistant helps students work through AI concepts in long sessions (30–40 messages). She wants it to use **Window Memory** so token costs stay predictable — but with a twist: a **pinned system message** that always stays in the context so the agent never forgets who the student is, even as old messages slide out of the window.

Implement this study assistant in Python with the following three tasks:

---

**Task 1 — Set up the memory structure**

Define a pinned `system_message` with the format:
```python
{"role": "system", "content": "You are a helpful AI study assistant. The student's name is [your name] and they are studying AI Agents and Memory Systems."}
```
Replace `[your name]` with your actual name. Then define `full_history = []` (stores all messages) and `WINDOW_SIZE = 6`.

---

**Task 2 — Implement Window Memory with pinned context**

Write two functions:

- `call_llm(messages)` — a simulated LLM that returns:
  `"[Study Assistant]: Got your question about '{last user message}'. I can see {len(messages)} messages in my context window."`

- `chat_with_agent(user_message)` — appends the user message to `full_history`, builds the context as `[system_message] + full_history[-WINDOW_SIZE:]`, calls `call_llm`, appends the response to `full_history`, and returns the response.

---

**Task 3 — Simulate a session and print a memory report**

Run 8 turns of conversation using `chat_with_agent()` with questions covering different topics from the session (STM vs LTM, Buffer/Window/Summary strategies, Episodic/Semantic/Procedural memory, context window limits).

After all turns, print:

```
--- Final Memory Report ---
Total messages in full_history: [X]
Messages sent to LLM in the last call: [Y]  (1 system + up to 6 history)
Window Memory bounded context to [Y] messages while full history holds [X] messages.
```

Verify that `Y` is always ≤ 7.

---

### Submission Instructions

- Code all three tasks in VS Code in a **single `.py` file** (e.g., `window_memory_agent.py`)
- Run the code and verify the final report shows the LLM received ≤ 7 messages per call
- Then **submit the code in the code editor / answer box in the LMS**

---

**Answer Explanation (Ideal Solution Walkthrough):**

The core insight: *Window Memory bounds what the model sees per call, but the full history is maintained separately. Pinning the system message outside the sliding window ensures critical context (student name, study topic) is never dropped.*

```python
system_message = {
    "role": "system",
    "content": "You are a helpful AI study assistant. The student's name is Kavya and they are studying AI Agents and Memory Systems."
}

full_history = []
WINDOW_SIZE = 6

def call_llm(messages):
    last_user_msg = next(
        (m["content"] for m in reversed(messages) if m["role"] == "user"), ""
    )
    return f"[Study Assistant]: Got your question about '{last_user_msg}'. I can see {len(messages)} messages in my context window."

def chat_with_agent(user_message):
    full_history.append({"role": "user", "content": user_message})
    context = [system_message] + full_history[-WINDOW_SIZE:]
    response = call_llm(messages=context)
    full_history.append({"role": "assistant", "content": response})
    return response

questions = [
    "What is Short-Term Memory in an AI agent?",
    "How is it different from Long-Term Memory?",
    "What is a context window and why does it have limits?",
    "What is Buffer Memory and when should it be used?",
    "How does Window Memory differ from Buffer Memory?",
    "What is Summary Memory and what problem does it solve?",
    "What is Episodic Memory — give an example.",
    "How do agents decide what information is worth remembering?"
]

for i, question in enumerate(questions, start=1):
    response = chat_with_agent(question)
    print(f"Turn {i}:\nUser: {question}\nAssistant: {response}\n")

last_context_size = 1 + min(len(full_history), WINDOW_SIZE)
print("--- Final Memory Report ---")
print(f"Total messages in full_history: {len(full_history)}")
print(f"Messages sent to LLM in the last call: {last_context_size}  (1 system + up to {WINDOW_SIZE} history)")
print(f"Window Memory bounded context to {last_context_size} messages while full history holds {len(full_history)} messages.")
```

**Alternative Approaches:**
- `WINDOW_SIZE` could be dynamically tuned based on estimated token count rather than message count
- In a real system, `call_llm` is replaced with an actual API call to an LLM provider (OpenAI, Anthropic, etc.)
- Multiple pinned messages (e.g., user profile + system instructions) can be stored in a separate `pinned_messages` list prepended before the window
