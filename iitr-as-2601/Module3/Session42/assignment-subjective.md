# Subjective Assignment: Save & Reload Chat History

## Practical Task

**Difficulty:** Easy  
**Type:** Coding implementation

---

## Scenario

**EcoDrive Motors** analysts use a simple earnings Q&A bot. You do **not** need a real database or API key for this task.

Your job is to build a tiny **memory layer**:

1. Save chat turns to a JSON file after each message.  
2. Reload that file before the next message.  
3. Pass the **full chat so far** into a stub answer function so a short follow-up like *"And in 2023?"* still works.

---

## Provided stub

Copy this function into your file — do not change it:

```python
def mock_rag_answer(full_question):
    """Looks at the full text (old turns + new message) and returns a fake answer."""
    text = full_question.lower()
    if "2022" in text and "revenue" in text:
        return "EcoDrive revenue in 2022 was 12.4 billion dollars."
    if "2023" in text and ("revenue" in text or "2022" in text):
        return "EcoDrive revenue in 2023 was 14.1 billion dollars."
    return "I need more context about which metric and year you mean."
```

---

## Task

Create one file: `ecodrive_memory_chat.py`

### Part A — Save and load JSON

1. Set `HISTORY_FILE = "ecodrive_chat_history.json"`.  
2. Write `save_history(history)` — use `json.dump(history, f, indent=2)`.  
3. Write `load_history()` — if the file is missing, return `[]`.  
4. Write `append_turn(history, user_text, bot_text)`:
   - Append `{"role": "user", "content": user_text}`  
   - Append `{"role": "assistant", "content": bot_text}`  
   - Call `save_history(history)`  
   - Return `history`

### Part B — One chat turn with memory

Write `chat_once(user_message, history)`:

1. Build one string called `full_question`:
   - For each item in `history`, add a line: `role: content`  
   - Add a last line: `user: <user_message>`  
2. Call `mock_rag_answer(full_question)` inside `try/except`.  
   - On success, store the returned string as `bot_reply`.  
   - On any error, set `bot_reply = "Search is unavailable right now. Please try again in a minute."`  
3. Call `append_turn(history, user_message, bot_reply)`.  
4. Return `bot_reply`.

### Part C — Run a two-turn demo in `main()`

```python
def main():
    # Start fresh
    if os.path.exists(HISTORY_FILE):
        os.remove(HISTORY_FILE)

    history = load_history()

    # Turn 1
    reply1 = chat_once("What was EcoDrive revenue in 2022?", history)
    print("Turn 1:", reply1)

    # Reload from file (proves persist works)
    history = load_history()

    # Turn 2 — short follow-up, no "revenue" repeated
    reply2 = chat_once("And in 2023?", history)
    print("Turn 2:", reply2)
```

---

## Expected output (example)

```
Turn 1: EcoDrive revenue in 2022 was 12.4 billion dollars.
Turn 2: EcoDrive revenue in 2023 was 14.1 billion dollars.
```

Turn 2 works only because turn 1 was saved to JSON and passed back into `full_question`.

---

## Submission Instructions

- Code all parts in VS Code in a single `.py` file.
- Run the code and verify both turns print the expected revenue figures.
- Submit the complete code in the LMS code editor/answer box.

---

## Answer Explanation

### Walkthrough

1. `append_turn` + `save_history` write each exchange to disk.  
2. `load_history` before turn 2 reloads turn 1 so the stub still sees **2022** and **revenue**.  
3. `chat_once` joins old messages + new message into one string for `mock_rag_answer`.  
4. `try/except` returns a friendly line if anything fails.

### Complete Code

```python
import json
import os

HISTORY_FILE = "ecodrive_chat_history.json"


def mock_rag_answer(full_question):
    text = full_question.lower()
    if "2022" in text and "revenue" in text:
        return "EcoDrive revenue in 2022 was 12.4 billion dollars."
    if "2023" in text and ("revenue" in text or "2022" in text):
        return "EcoDrive revenue in 2023 was 14.1 billion dollars."
    return "I need more context about which metric and year you mean."


def save_history(history):
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)


def load_history():
    try:
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def append_turn(history, user_text, bot_text):
    history.append({"role": "user", "content": user_text})
    history.append({"role": "assistant", "content": bot_text})
    save_history(history)
    return history


def chat_once(user_message, history):
    lines = []
    for msg in history:
        lines.append(f"{msg['role']}: {msg['content']}")
    lines.append(f"user: {user_message}")
    full_question = "\n".join(lines)

    try:
        bot_reply = mock_rag_answer(full_question)
    except Exception:
        bot_reply = "Search is unavailable right now. Please try again in a minute."

    append_turn(history, user_message, bot_reply)
    return bot_reply


def main():
    if os.path.exists(HISTORY_FILE):
        os.remove(HISTORY_FILE)

    history = load_history()

    reply1 = chat_once("What was EcoDrive revenue in 2022?", history)
    print("Turn 1:", reply1)

    history = load_history()

    reply2 = chat_once("And in 2023?", history)
    print("Turn 2:", reply2)


if __name__ == "__main__":
    main()
```

### Notes for evaluation

- Turn 2 must mention **14.1 billion** — if it prints *"I need more context"*, history was not saved or reloaded correctly.  
- Accept small wording differences if the dollar amounts are correct.  
- No Groq, Chroma, loop termination, or Gradio required for this task.
