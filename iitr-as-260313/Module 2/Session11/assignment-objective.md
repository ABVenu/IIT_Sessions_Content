# Objective Assignment — Self-Reflection and Feedback Loops

---

## Multiple Choice Questions (Single Correct Answer)

---

### Question 1 — Easy

After a long day of testing, an e-commerce company's AI chatbot is found to respond with *"Please contact support for assistance"* to almost every customer complaint — not because it lacks knowledge, but because it stops at the very first answer it generates without ever reviewing it. According to the concepts covered in this session, which mechanism is the chatbot missing?

- A) Chain-of-thought reasoning
- B) One-shot prompting
- C) Self-reflection
- D) User feedback loop

**Correct Answer:** C

**Answer Explanation:**
Self-reflection is the mechanism by which an AI reviews, evaluates, and revises its own output before presenting it to the user. The chatbot in this scenario generates the first possible response and stops — it has no built-in habit of asking itself: *"Is this actually useful? Is this the best I can do?"* That deliberate second-check is exactly what self-reflection provides.

- **A is incorrect:** Chain-of-thought is a reasoning technique that helps the AI think step by step before answering — it does not address whether the AI re-evaluates the quality of its output after generating it.
- **B is incorrect:** One-shot prompting is a prompting strategy (send one prompt, accept the first response) — it is not a quality-check mechanism and is actually the root of the problem described.
- **D is incorrect:** A user feedback loop requires a human to read the response and send corrections. The chatbot's problem is that it is not self-checking; whether or not users are correcting it is a separate issue.

---

### Question 2 — Easy

Nadia is designing a self-correction prompt for an AI research assistant. She wants the AI to first produce a draft answer, then carefully analyse its own weaknesses, and finally produce a better version using those insights. Which of the following sequences correctly represents the three stages of a self-correction prompt?

- A) Critique → Rewrite → Generate
- B) Generate → Rewrite → Critique
- C) Critique → Generate → Rewrite
- D) Generate → Critique → Rewrite

**Correct Answer:** D

**Answer Explanation:**
The three stages of a self-correction prompt are defined as: **Stage 1 — Generate** (produce the initial response), **Stage 2 — Critique** (the AI reviews what it just wrote and identifies what is missing, incorrect, or weak), and **Stage 3 — Rewrite** (the AI produces an improved version based on its own critique). The critique must come before the rewrite — that is what makes self-correction different from simply asking the AI to "write a good answer." Without the critique step, the AI has no map of what to fix.

- **A** places Critique first before anything has been generated — nothing to critique yet.
- **B** places Rewrite before Critique — the AI is rewriting without knowing what needs fixing.
- **C** starts with Critique before a draft exists, then generates, then rewrites — logically impossible.

---

### Question 3 — Easy

Rohan uses the EVAL framework to review an AI-generated response. The AI was asked: *"What are the advantages and disadvantages of remote work for small businesses?"* The response lists only advantages — nothing about disadvantages. Using the EVAL framework, which criterion has most clearly failed?

- A) Validity
- B) Layout
- C) Adequacy
- D) Exactness

**Correct Answer:** D

**Answer Explanation:**
**Exactness** (the "E" in EVAL) asks: *"Did the AI answer exactly what was asked — not a related topic, not a simplified version, but the actual question?"* The original question explicitly asked for both advantages AND disadvantages. The AI answered only one dimension, which means it did not answer exactly what was asked. That is an Exactness failure.

- **Validity (V)** checks whether the specific facts, names, and claims can be verified — not the concern here; the listed advantages may be perfectly accurate.
- **Adequacy (A)** checks whether the depth of the response is sufficient — the issue is not depth within what was answered, but that half of the question was entirely skipped.
- **Layout (L)** checks whether the format matches what was requested — no specific format was prescribed here.

---

### Question 4 — Easy

A learner asks an AI: *"Who founded Microsoft?"* The AI responds: *"Microsoft was founded by Steve Jobs and Steve Wozniak in 1975 as a personal computing company."* What type of AI response quality failure does this represent?

- A) Vagueness
- B) Wrong format
- C) Incomplete coverage
- D) Hallucination

**Correct Answer:** D

**Answer Explanation:**
**Hallucination** occurs when an AI confidently states something false with the full markers of a real fact — a specific name, a year, and a description. Microsoft was actually founded by Bill Gates and Paul Allen, not Steve Jobs and Steve Wozniak (who co-founded Apple). The AI has produced a completely wrong answer but delivered it with the same confidence and detail as if it were true. That is the hallucination pattern — and it is dangerous precisely because it sounds convincing.

- **Vagueness (A)** would mean the answer is technically true but too general to be useful — the opposite of what happened here (the answer is specific, just wrong).
- **Wrong format (B)** would mean the structure of the response does not match what was requested.
- **Incomplete coverage (C)** would mean part of the question was skipped — here, the question was fully answered, just incorrectly.

---

### Question 5 — Moderate

Karan is on Round 2 of iterative prompting to improve a business email. The current version has a strong, confident opening and a clear call to action — both of which work well. However, the second paragraph contains technical jargon that the intended reader (a non-technical small business owner) would not understand. What is the MOST effective Round 3 follow-up prompt?

- A) "This email is still not right. Rewrite it completely."
- B) "The opening and call to action are strong — keep them exactly as they are. Rewrite only the second paragraph: remove all technical jargon and use plain business language a non-technical reader can follow."
- C) "Make this email clearer, simpler, and more professional overall."
- D) "Can you improve this email and make it easier to read?"

**Correct Answer:** B

**Answer Explanation:**
Best practice for iterative prompting has two rules working together: **acknowledge what is already working** (so the AI does not discard the good parts) and **target exactly one specific problem** (so the improvement is controlled and precise). Option B does both — it explicitly tells the AI to keep the opening and call to action, then directs it to fix only the second paragraph with a clear, specific instruction (remove jargon, use plain language).

- **A** asks for a full rewrite — this risks losing the strong opening and call to action that were already working. Throwing away good work is the common mistake iterative prompting is designed to avoid.
- **C** targets multiple vague things simultaneously ("clearer, simpler, more professional"). Without specificity, the AI has no precise target, and the result will be another generic improvement.
- **D** is vague and gives the AI no indication of what specifically is wrong — it will likely produce a different version of the same quality.

---

### Question 6 — Moderate

A logistics company wants to deploy an AI agent that generates shipping delay notifications to customers — processing 5,000 notifications per day automatically, with no human reading each individual notification. Every notification must always include: (1) the specific reason for the delay, (2) an estimated new delivery date, and (3) an apology. Which prompting strategy is MOST appropriate for this agent?

- A) One-shot prompting — because delay notifications are simple and do not need complex prompts
- B) Iterative prompting — because a human reviewer can check each notification and send corrections
- C) Reflection-based prompting — because the agent must autonomously verify quality criteria without human oversight at scale
- D) User feedback loops — because customers can report bad notifications and the agent will improve over time

**Correct Answer:** C

**Answer Explanation:**
**Reflection-based prompting** is the right choice when an agent must maintain consistent quality autonomously — without a human present for each interaction. The three required elements (reason, estimated date, apology) are clear, measurable criteria that can be embedded directly in an internal feedback loop. The agent checks its own output against those criteria and revises automatically, every time, at any volume.

- **One-shot prompting (A)** provides no mechanism to verify that all three elements appear in every notification — a notification missing the estimated date would go out uncorrected.
- **Iterative prompting (B)** requires a human to review each round — completely impractical at 5,000 notifications per day.
- **User feedback loops (D)** are reactive — customers receive a bad notification first, then report it. The quality failure has already reached the customer. That is too late.

---

## Multiple Select Questions (Multiple Correct Answers)

---

### Question 7 — Moderate

Ananya is building an internal feedback loop for an AI agent that generates social media captions for a fashion brand. She wants the loop to run efficiently and produce consistent results. Which of the following represent well-designed feedback loop practices? **Select ALL that apply.**

- A) Setting a maximum of 3 revision cycles; if criteria are still not met after 3 cycles, flagging the issue instead of looping further
- B) Using the criterion: *"Does the caption include at least one relevant hashtag and a call to action? (Yes/No)"*
- C) Using the criterion: *"Is the caption engaging and on-brand? (Yes/No)"*
- D) Saving the tested prompt flow as a reusable template where only the product details change for each new caption
- E) Running as many revision cycles as needed until the output "feels right" before delivering

**Correct Answers:** A, B, D

**Answer Explanation:**
- **A is correct:** Limiting the loop to a maximum of 2–3 cycles is a core efficiency principle. If the agent cannot meet criteria in that many cycles, the problem is in the prompt design — not something more loops will fix. A maximum cycle limit also prevents production agents from running indefinitely.
- **B is correct:** "Does it include a hashtag and a call to action?" is a specific, binary, and fully checkable criterion. The AI can verify this exactly — it either included them or it did not.
- **C is incorrect:** "Engaging and on-brand" is subjective — the AI has no concrete definition to check against. Subjective criteria break the self-evaluation mechanism because "somewhat" becomes a valid answer. Strong criteria must be measurable.
- **D is correct:** Saving working prompt flows as reusable templates (changing only the TASK) is Principle 3 of optimising feedback loops. It makes the quality system scalable and ensures consistency across hundreds of captions without redesigning the loop each time.
- **E is incorrect:** "Until it feels right" is not a measurable stopping condition and represents exactly the kind of infinite loop that well-designed feedback loops must prevent. Production agents need hard stopping points.

---

### Question 8 — Moderate

Preethi is reviewing a colleague's AI agent that produces customer onboarding summaries. The agent works correctly sometimes, but the outputs are inconsistent — some summaries are formal, some are casual, some are structured bullet lists, and others are long unbroken paragraphs. Which MISSING components from the agent prompt flow are MOST LIKELY causing this inconsistency? **Select ALL that apply.**

- A) Role (System Instruction) — defining who the agent is, its expertise, and its default tone and behaviour
- B) Task — the specific assignment with details about the customer being onboarded
- C) Reflection + Feedback Criteria — measurable quality checks the agent runs on its own output before delivering
- D) Output Format — specifying exactly how the summary should be structured, the length, and the presentation
- E) Chain-of-thought reasoning steps embedded within the task description

**Correct Answers:** A, C, D

**Answer Explanation:**
- **A is correct:** Without a Role, the agent defaults to a random tone — sometimes formal, sometimes casual — depending on how the task happens to be phrased. The Role locks in the agent's default behaviour, expertise, and communication style across every run. Removing the Role removes the consistency anchor.
- **B is incorrect:** The Task defines what to do for a specific customer — varying this is expected and intentional. The inconsistency is in tone and format, not in what is being summarised.
- **C is correct:** Without Reflection Criteria, the agent does not self-check whether its output meets a quality standard before delivering. Inconsistent quality (some good, some poor) is exactly what reflection criteria are designed to catch and correct.
- **D is correct:** Without an Output Format instruction, the agent freely chooses its own structure — bullet points one time, paragraph the next. Specifying the exact format is what enforces structural consistency across all runs.
- **E is incorrect:** Chain-of-thought reasoning helps improve reasoning quality within a single response — it does not control tone or format consistency across different runs of the agent.

---

### Question 9 — Hard

Faisal is designing an internal feedback loop for an autonomous agent that writes brief property reviews for a travel booking platform. The reviews will be published without human review. Which of the following criteria are well-suited for a reliable internal feedback loop? **Select ALL that apply.**

- A) *"Does the review mention at least one specific property feature (e.g., location, check-in experience, room quality)? (Yes/No)"*
- B) *"Is the review under 80 words? (Yes/No)"*
- C) *"Is this a good review? (Yes/No)"*
- D) *"Does the review avoid making audience-specific claims (e.g., 'ideal for families' or 'perfect for business travellers') that were not part of the verified information? (Yes/No)"*
- E) *"Does the review end with a clear overall recommendation sentence? (Yes/No)"*
- F) *"Is the tone positive and enthusiastic? (Yes/No)"*

**Correct Answers:** A, B, D, E

**Answer Explanation:**
- **A is correct:** Specific and binary — the AI can check whether it mentioned a named feature. This is an inclusion check.
- **B is correct:** Word count is perfectly measurable. The AI can verify this exactly with no ambiguity.
- **C is incorrect:** "Is this a good review?" is entirely subjective. The AI cannot self-evaluate against this criterion because "good" has no definition it can check — this is the textbook example of a weak feedback loop criterion.
- **D is correct:** This is a clear rule — did the review make a claim about a specific audience type without verified data? The AI can check whether sentences like "ideal for families" appear in the output. This is measurable.
- **E is correct:** Specific and binary — the agent can check whether a concluding recommendation sentence exists before marking the review as accepted.
- **F is incorrect:** "Positive and enthusiastic" is vague and subjective. A strong version of this criterion would be: *"Does the review avoid negative language and use at least one positive adjective? (Yes/No)"* — that version is checkable. As stated, F gives the AI no concrete definition to evaluate against.

---

### Question 10 — Hard

A quality assurance team is reviewing five AI-generated responses using the five types of bad AI responses covered in the session. Which of the following statements correctly identify the type of quality failure in each described response? **Select ALL that apply.**

- A) An AI asked for *"a numbered list of 5 budget travel tips"* returns a continuous paragraph of travel advice — this is a **Wrong Format** failure.
- B) An AI states: *"The Bharat Ratna was first awarded in 1950 to C. V. Raman"* (the actual year was 1954 and the first recipient was C. Rajagopalachari) — this is a **Vagueness** failure.
- C) An AI responds to *"What are the pros and cons of online learning?"* with only a list of pros, completely skipping cons — this is an **Incomplete Coverage** failure.
- D) An AI opens with *"Social media is clearly harmful for teenagers,"* then lists five mental health benefits of social media in the body, and concludes *"Therefore, social media is harmful and teenagers should avoid it"* — this is a **Logical Contradiction** failure.
- E) An AI answers *"How do I build a website?"* with: *"You can use web development tools to build websites. Programming knowledge is important."* — this is a **Hallucination** failure.

**Correct Answers:** A, C, D

**Answer Explanation:**
- **A is correct:** The user specified both the format (numbered list) and quantity (5 tips). The AI ignored both and returned a paragraph. This is a Wrong Format failure — the output structure does not match the explicit instruction.
- **B is incorrect:** Stating specific wrong facts (wrong year, wrong person) with full confidence is **Hallucination**, not Vagueness. Hallucination produces false details that sound like real facts. Vagueness is when the answer is too general to be useful — the opposite of what happened here.
- **C is correct:** The question explicitly asked for both pros and cons. The AI covered only one dimension and silently skipped the other. That is Incomplete Coverage — part of the question was never answered.
- **D is correct:** The AI's body presents evidence directly contradicting its opening claim and conclusion. Stating "social media is harmful" while listing mental health benefits, then concluding "therefore it is harmful," is a Logical Contradiction — two claims that cannot both be true, with a conclusion that ignores the evidence in its own response.
- **E is incorrect:** This is **Vagueness**, not Hallucination. The response is technically true but so general that it gives the user nothing actionable — no specific tools, no steps, no starting point. A person trying to build a website is no better off after reading it. That is the Vagueness failure pattern.
