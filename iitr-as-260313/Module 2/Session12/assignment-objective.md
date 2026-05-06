# Objective Assignment — Introduction to Memory in AI Agents

---

## Multiple Choice Questions (Single Correct Answer)

---

### Question 1 — Easy

A food delivery chatbot helps a customer check the status of one order. The next day, the same customer opens the chatbot and asks, *"Can you update me on that order?"* The bot replies, *"Please share your order number and explain your issue."* According to the session, what is the main limitation shown here?

- A) The bot has too much long-term memory
- B) The bot is behaving like a stateless agent
- C) The bot is using semantic retrieval incorrectly
- D) The bot has exceeded its context window

**Correct Answer:** B

**Answer Explanation:**
The bot is behaving like a **stateless agent** because it does not retain information from the previous interaction. It treats the new message as a completely fresh request and asks the customer to repeat context that was already shared.

- **A is incorrect:** There is no evidence that the bot stored too much information. The problem is the opposite — it remembers nothing.
- **C is incorrect:** Semantic retrieval means finding conceptually relevant memories. The scenario does not show retrieval happening incorrectly; it shows no memory being used at all.
- **D is incorrect:** Context window overflow can cause older information to be dropped in long conversations, but this scenario simply shows the bot failing to remember a previous session.

---

### Question 2 — Easy

In the session, *state* was compared to a doctor's patient file. Why is this comparison useful?

- A) Because state stores every possible medical fact in the model's training data
- B) Because state helps a system retain past interaction information and use it later
- C) Because state means the agent always gives healthcare advice
- D) Because state removes the need for user identification

**Correct Answer:** B

**Answer Explanation:**
State is the ability of a system to retain and remember information from past interactions so it can use that information in future interactions. A doctor's patient file works the same way: it stores history so the doctor does not start from zero each time.

- **A is incorrect:** State is not about storing all global knowledge in the model's training data. It is about retaining relevant interaction information.
- **C is incorrect:** The doctor example is only an analogy. State applies to many agent domains, not only healthcare.
- **D is incorrect:** User identification is often needed before an agent can retrieve the correct user's memories.

---

### Question 3 — Easy

A learner asks an AI tutor, *"Can you continue from where we stopped yesterday?"* The tutor replies, *"I do not know what we studied earlier. Please tell me the topic again."* Which user experience problem does this best illustrate?

- A) Repetition problem
- B) Procedural memory
- C) Context assembly
- D) Memory write-back

**Correct Answer:** A

**Answer Explanation:**
This illustrates the **repetition problem**. When an agent has no memory, users must repeatedly explain information they already shared. The learner has to re-state the previous topic because the tutor cannot remember the earlier session.

- **B is incorrect:** Procedural memory is memory of how to perform tasks or workflows. The scenario is not about remembering a procedure.
- **C is incorrect:** Context assembly is the process of combining retrieved memories, conversation history, and the latest message before calling the model. The scenario shows that this did not happen effectively.
- **D is incorrect:** Memory write-back means saving important information after a response. The immediate user-facing problem here is forced repetition.

---

### Question 4 — Easy

Which of the following is the best example of **short-term memory** in an AI agent?

- A) A database record storing that a user prefers Hindi explanations
- B) A full transcript stored permanently in file storage
- C) The last few messages held inside the current context window during an active chat
- D) A vector database containing summaries from past sessions

**Correct Answer:** C

**Answer Explanation:**
Short-term memory, also called working memory or in-context memory, is the information currently held inside the model's context window during one active conversation. It is fast to access but temporary.

- **A is incorrect:** A stored user preference in a database is long-term memory.
- **B is incorrect:** A permanently stored transcript is long-term memory in file storage.
- **D is incorrect:** A vector database stores retrievable long-term memory, often for semantic search.

---

### Question 5 — Moderate

An AI travel assistant is helping a user plan a 5-day Goa trip with a ₹20,000 budget. In the same chat, the user later asks, *"Which hotel should I choose?"* The assistant recommends luxury hotels costing ₹15,000 per night because it ignored the earlier budget. What concept explains why the current question was misunderstood?

- A) The assistant failed to use the conversation context
- B) The assistant used too much procedural memory
- C) The assistant stored a permanent memory too early
- D) The assistant correctly acted as a stateless system

**Correct Answer:** A

**Answer Explanation:**
The user's latest question only makes sense when interpreted with the earlier context: Goa, 5 days, and ₹20,000 budget. The assistant gave a technically possible answer but failed to use the relevant background information, making the response practically useless.

- **B** mischaracterises the issue — procedural memory is about remembering how to perform tasks, but the failure here is ignoring relevant conversation context such as the budget.
- **C** introduces an unsupported claim — nothing suggests a permanent save happened too early; the assistant simply failed to use information already in the same chat.
- **D** is backwards — for multi-turn trip planning, the assistant should use prior context rather than behave as if each turn is isolated.

---

### Question 6 — Moderate

A product team is designing an AI career coach that users will interact with over several months. The agent should remember each user's skills, target roles, interview history, and preferred learning style. Which design choice best matches the session's guidance?

- A) Keep the agent stateless to reduce complexity, because career advice is mostly one-time
- B) Store all conversation text directly in every prompt forever so nothing is ever lost
- C) Use long-term memory to store durable user information and retrieve relevant parts into the context window
- D) Avoid user identification so that any stored memory can be shared across all users

**Correct Answer:** C

**Answer Explanation:**
This scenario requires continuity and personalisation across weeks or months, so the agent needs long-term memory. Durable facts such as skills, goals, and learning preferences should be stored externally and retrieved into the context window when relevant.

- **A** underestimates the product need — career coaching continues across weeks or months and depends on goals, history, and progress, not one-off advice.
- **B** is impractical at scale — dumping the full transcript into every prompt is costly, hits context limits, and is the opposite of selective retrieval.
- **D** violates basic memory design — without user identification, memories cannot be isolated per person and private storage breaks down.

---

## Multiple Select Questions (Multiple Correct Answers)

---

### Question 7 — Moderate

Meera is comparing stateless and stateful agents for different product features. Which of the following features are better suited for a **stateful** agent? **Select ALL that apply.**

- A) An AI tutor that remembers a student's weak areas and past lessons
- B) A one-time sentence translation tool
- C) A customer support bot that continues an unresolved complaint across multiple days
- D) A chatbot that validates whether an email address format is correct
- E) A shopping assistant that remembers size, fabric preferences, and budget

**Correct Answers:** A, C, E

**Answer Explanation:**
- **A is correct:** A tutor becomes more useful when it remembers learning history, weak areas, and progress.
- **B is incorrect:** One-time translation is a single-turn task where stateless design is usually sufficient.
- **C is correct:** Multi-day customer support requires continuity, past ticket details, and previous escalation history.
- **D is incorrect:** Email format validation is a simple one-off task that does not require memory of past interactions.
- **E is correct:** A shopping assistant benefits strongly from remembering user-specific preferences and constraints.

---

### Question 8 — Moderate

An agent receives a user message and needs to answer using memory. Which steps belong in the memory-powered interaction flow taught in the session? **Select ALL that apply.**

- A) Identify the user before retrieving personal memories
- B) Retrieve relevant long-term memories before generating the response
- C) Assemble context by combining retrieved memories, recent conversation, latest message, and system instructions
- D) Assume the AI model already remembers the user from its training data
- E) Write back important new information after the response when it is memory-worthy

**Correct Answers:** A, B, C, E

**Answer Explanation:**
- **A is correct:** The agent often needs to identify who is sending the message so it can access the correct memory store.
- **B is correct:** Memory retrieval happens before the model generates the response, so relevant past information can be used.
- **C is correct:** Context assembly combines retrieved memory, short-term conversation history, the latest user message, and system instructions.
- **D is incorrect:** The model does not personally remember the user from training data. Memory is an external architecture that loads information into context.
- **E is correct:** After the response, the agent may save useful new facts or decisions back to long-term memory.

---

### Question 9 — Hard

Riya is designing memory rules for an AI fitness coach. Which pieces of information are good candidates for **long-term memory**, based on the session's design considerations? **Select ALL that apply.**

- A) *"User has a right knee injury and cannot run or do squats"*
- B) *"User typed 'hello' at 9:01 AM today"*
- C) *"User prefers workouts under 30 minutes"*
- D) *"User asked one random trivia question about cricket during the session"*
- E) *"User's goal is to reduce weight from 85 kg to 75 kg"*
- F) *"User said they are tired today after sleeping late last night"*

**Correct Answers:** A, C, E

**Answer Explanation:**
- **A is correct:** A knee injury is important, safety-relevant, and should persist across sessions.
- **B is incorrect:** A greeting timestamp is low-value conversational noise and not worth storing.
- **C is correct:** Workout duration preference improves future recommendations and is durable enough to store.
- **D is incorrect:** A one-time unrelated trivia question is not useful for future fitness coaching.
- **E is correct:** A user's fitness goal is central to personalisation and progress tracking.
- **F is incorrect:** Being tired today is usually short-lived state. It may matter for the current session but does not necessarily need long-term storage unless it becomes a repeated pattern.

---

### Question 10 — Hard

A team is reviewing proposed memory architecture decisions for an AI agent. Which statements are consistent with the session's guidance? **Select ALL that apply.**

- A) Long-term memory should feed short-term memory by retrieving relevant facts into the context window
- B) Every user message should be stored permanently so retrieval has maximum data
- C) Retrieval quality matters because irrelevant memories can waste context window space and confuse the model
- D) Memory lifetimes can differ: some memories are short-lived, some medium-lived, and some permanent
- E) Privacy can be ignored for memory systems because the AI model only uses text
- F) Semantic retrieval can help find memories by meaning, not only exact keyword matches

**Correct Answers:** A, C, D, F

**Answer Explanation:**
- **A is correct:** The session explains that long-term memory feeds short-term memory by retrieving relevant memories and loading them into the context window.
- **B is incorrect:** Storing everything creates clutter, cost, privacy risk, and poor retrieval quality. Good memory systems are selective.
- **C is correct:** Bad retrieval can load irrelevant memories, waste limited context space, and reduce response quality.
- **D is correct:** The session describes short-lived, medium-lived, and permanent memory lifetimes.
- **E is incorrect:** Memory raises serious privacy and ethical responsibilities, including user awareness, deletion rights, and protection of sensitive data.
- **F is correct:** Semantic retrieval searches based on conceptual relevance rather than only exact words.
