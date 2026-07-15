# In-Class Quiz — Session 32: Memory & Control Flow

**Instructions:** Each question has **one correct option**. Choose the best answer.

---

## LO 1 — Define an AI agent

### Question 1

Which of the following best describes an **AI agent**?

A. A system that only stores data in a database  
B. A system that perceives input, reasons, acts using tools, and can use memory  
C. A Python variable that holds a single number  
D. A CSV file used for logging

**Correct Answer:** B

**Answer Explanation:**  
B is correct — an AI agent perceives, reasons, acts (often with tools), and can remember.

A, C, and D describe storage or simple data — not an agent.

---

### Question 2

A one-shot tool call (ask once, get one answer, forget the turn) is mainly **tool use**. What is a beginner step toward **agent-like** behaviour?

A. Adding memory and a controlled loop  
B. Deleting all stop rules  
C. Never saving history  
D. Always showing raw error logs to the user

**Correct Answer:** A

**Answer Explanation:**  
A is correct — memory plus a controlled loop moves from one-shot tool use toward agent behaviour.

B, C, and D work against safe, coherent agent control.

---

## LO 2 — Distinguish short-term memory from long-term memory

### Question 3

Which of the following is an example of **long-term memory**?

A. Storing facts in a database across many sessions (days, weeks, months)  
B. Storing chat messages only in a Python list variable for the current run  
C. Printing a traceback to the console  
D. Setting `MAX_STEPS = 5`

**Correct Answer:** A

**Answer Explanation:**  
A is correct — long-term memory keeps information across sessions, typically in durable stores like a database or user profile.

B is short-term (current session / current run). C and D are error handling and loop control, not memory types.

---

### Question 4

If a **chat history** is kept for the current open chat / current session, which type of memory is that?

A. Long-term memory  
B. Short-term memory  
C. Both  
D. None

**Correct Answer:** B

**Answer Explanation:**  
B is correct — short-term memory is the running chat history for the current session.

A is for facts kept across sessions. It is specifically short-term, not both or none.

---

## LO 3 — Persist and reload conversation history

### Question 5

What does it mean to **persist** conversation history?

A. Keep messages only in a temporary Python list and never write a file  
B. Write the history to durable storage (for example a JSON file) so it can be loaded later  
C. Increase `MAX_STEPS` without any limit  
D. Delete history after every message

**Correct Answer:** B

**Answer Explanation:**  
B is correct — persist means save to durable storage so the history can be reloaded.

A is only in-memory. C is loop control. D removes history instead of saving it.

---

### Question 6

On first run, the history JSON file does not exist. What should a safe load function return?

A. An empty list `[]`  
B. A hard crash with no fallback  
C. The word `"error"` only  
D. A random assistant message

**Correct Answer:** A

**Answer Explanation:**  
A is correct — treat missing file as a fresh start and return an empty list.

B is unsafe for first run. C and D are not valid history structures.

---

## LO 4 — Implement loop termination

### Question 7

Without a **stop rule**, what can go wrong in an agent loop?

A. The loop may run forever and API cost can rise  
B. Short-term memory automatically becomes long-term memory  
C. The history file becomes permanently read-only  
D. Python lists can no longer append messages

**Correct Answer:** A

**Answer Explanation:**  
A is correct — missing termination can cause runaway iterations and higher API cost.

B, C, and D are not effects of missing stop rules.

---

### Question 8

Which option is a **hard ceiling** that stops a loop after a fixed number of steps?

A. Hoping the model says “I’m done”  
B. `MAX_STEPS`  
C. Saving history once a week  
D. Using a Python list for messages

**Correct Answer:** B

**Answer Explanation:**  
B is correct — `MAX_STEPS` is a non-negotiable max on loop iterations.

A alone is unsafe. C is about persist timing. D is about memory storage, not loop stop.

---

## LO 5 — Handle predictable errors with user-visible messages

### Question 9

When an API call fails, what should the **user** see?

A. A short friendly message (for example, try again in a minute)  
B. The full raw traceback with internal file paths  
C. The exact `str(exception)` text only  
D. No message at all

**Correct Answer:** A

**Answer Explanation:**  
A is correct — user-visible error handling shows a clear, friendly message.

B and C expose internal details. D leaves the user with no guidance.

---

### Question 10

The user typed only spaces (blank input). Which response is appropriate?

A. `"Please type a question."`  
B. A long stack trace  
C. `"Index is empty"` even when the index is fine  
D. Start an infinite loop

**Correct Answer:** A

**Answer Explanation:**  
A is correct — blank input should ask the user to type a question.

B is not user-friendly. C is the wrong error for this case. D is unsafe.

---

## Answer Key (quick)

| Q# | LO | Answer |
|---|---|---|
| 1 | Define an AI agent | B |
| 2 | Define an AI agent | A |
| 3 | Short-term vs long-term | A |
| 4 | Short-term vs long-term | B |
| 5 | Persist and reload | B |
| 6 | Persist and reload | A |
| 7 | Loop termination | A |
| 8 | Loop termination | B |
| 9 | User-visible errors | A |
| 10 | User-visible errors | A |
