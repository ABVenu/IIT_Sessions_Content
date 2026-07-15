# In-Class Quiz — Session 32: Memory & Control Flow

**Instructions:** Each question has **one correct option**. Choose the best answer.

---

## LO 1 — Define an AI agent

### Question 1

Which definition best matches an **AI agent**?

A. A one-shot answer machine that ignores tools and prior messages  
B. A system that perceives input, reasons about the next step, acts with tools, and can remember prior steps  
C. A database that only stores static records  
D. A spreadsheet that only performs calculations

**Correct Answer:** B

**Answer Explanation:**  
B is correct — an AI agent perceives, reasons, acts (often with tools), and can remember so later turns stay coherent.

A is incorrect because that describes a one-shot call without agent behaviour. C is incorrect because storing records alone is not perceiving/reasoning/acting. D is incorrect because calculation alone is not agent behaviour.

---

### Question 2

Which of the following is the clearest **beginner step** from a single tool call toward agent-like behaviour?

A. Adding memory and a controlled loop on top of tool use  
B. Turning off the model entirely  
C. Deleting the chat history after every word  
D. Showing only raw error codes to the user

**Correct Answer:** A

**Answer Explanation:**  
A is correct — a single tool call is tool use; adding memory plus a controlled loop is the beginner step toward agent behaviour.

B is incorrect because the model is still needed to reply. C is incorrect because deleting history removes memory. D is incorrect because raw errors are poor UX, not agent design.

---

## LO 2 — Distinguish short-term memory from long-term memory

### Question 3

What is **short-term memory** in a chat-based system?

A. Facts stored about a user for weeks or months across many chats  
B. Hardware RAM of the user’s phone only, with no message list  
C. The running chat history for the **current session**  
D. Only images uploaded in a future session

**Correct Answer:** C

**Answer Explanation:**  
C is correct — short-term memory is the running chat history for the current session.

A describes long-term memory. B confuses the concept with device hardware. D is unrelated to the current session’s message history.

---

### Question 4

Which statement correctly contrasts short-term and long-term memory?

A. Short-term lasts days/weeks; long-term lasts only one message  
B. Both are identical and must always use a vector database  
C. Long-term memory is required for a short multi-message demo  
D. Short-term is this session’s chat history; long-term stores facts across sessions (days, weeks, months)

**Correct Answer:** D

**Answer Explanation:**  
D is correct — short-term is this chat/session; long-term persists across sessions.

A reverses the durations. B is incorrect because short-term memory can be a simple list or JSON file. C is incorrect — a short demo can rely on short-term (session) memory alone.

---

## LO 3 — Persist and reload conversation history

### Question 5

An in-memory `history` list is lost when a notebook kernel restarts.

What does **persist** mean in this context?

A. Delete all messages after every reply  
B. Write the history to durable storage (for example a JSON file) so it can be loaded later  
C. Print the traceback of every API call  
D. Raise `MAX_STEPS` with no upper bound

**Correct Answer:** B

**Answer Explanation:**  
B is correct — persist writes history to durable storage; reload reads it back.

A is the opposite of saving. C is logging, not persistence of chat history. D relates to loop limits, not saving history.

---

### Question 6

A `load_history` function is called, but the history file does not exist yet (first run).

What should a safe `load_history` return?

A. An empty list `[]`  
B. A crash with no fallback  
C. The word `"error"` as a string only  
D. A random assistant reply

**Correct Answer:** A

**Answer Explanation:**  
A is correct — on `FileNotFoundError` (first run), return an empty list so the chat can start fresh.

B is incorrect because first run should be handled safely. C and D do not restore a message list.

---

## LO 4 — Implement loop termination

### Question 7

An agent loop may repeat internal steps (search, draft, check). Without a stop rule, what is a likely risk?

A. The history file becomes permanently read-only  
B. Short-term memory turns into long-term memory automatically  
C. The loop might run forever and API cost can rise  
D. The user’s keyboard locks forever

**Correct Answer:** C

**Answer Explanation:**  
C is correct — without loop termination, iterations can continue endlessly and increase API usage.

A, B, and D are not consequences described for missing stop rules.

---

### Question 8

Which stop rule is a **non-negotiable hard ceiling** on how many times a loop may iterate?

A. Hoping the model always says “I’m done” with no step limit  
B. Never checking for user words like `quit`, `exit`, or `stop`  
C. Saving history only at the end of the week  
D. `MAX_STEPS` — stop when the step count reaches the maximum

**Correct Answer:** D

**Answer Explanation:**  
D is correct — max steps (`MAX_STEPS`) is a hard ceiling even if the model wants to keep trying.

A is a common mistake (trusting the model with no step limit). B removes a useful user-stop rule; it is not the hard ceiling. C is about persistence timing, not loop termination.

---

## LO 5 — Handle predictable errors with user-visible messages

### Question 9

An API or tool call fails. What should the **end user** see?

A. A full red traceback with internal file paths  
B. A short friendly message such as “Search is unavailable. Please try again in a minute.”  
C. The exact raw `str(exception)` text from the library  
D. An empty string with no reply at all

**Correct Answer:** B

**Answer Explanation:**  
B is correct — user-visible error handling returns a clear, friendly message.

A and C expose messy internals. D leaves the user with silence instead of guidance.

---

### Question 10

Before calling a helper function, the code finds that the user typed only spaces.

Which user-visible response is appropriate?

A. `"Please type a question."`  
B. A long stack trace  
C. `"Document index is empty. Please run setup first."` even though the index is fine  
D. Starting a new infinite loop with no max steps

**Correct Answer:** A

**Answer Explanation:**  
A is correct — blank input should get a simple prompt like “Please type a question.”

B is not user-friendly. C mismatches the blank-input case (that message is for an empty index). D is unsafe and unrelated to blank input.

---

## Answer Key (quick)

| Q# | LO | Answer |
|---|---|---|
| 1 | Define an AI agent | B |
| 2 | Define an AI agent | A |
| 3 | Short-term vs long-term | C |
| 4 | Short-term vs long-term | D |
| 5 | Persist and reload | B |
| 6 | Persist and reload | A |
| 7 | Loop termination | C |
| 8 | Loop termination | D |
| 9 | User-visible errors | B |
| 10 | User-visible errors | A |
