# Objective Assignment — GenAI Concepts for Beginners

## Instructions
- Total questions: 10
- Question types: 6 MCQs (single correct), 4 MSQs (multiple correct)
- Difficulty progression: Easy → Moderate → Hard

---

## MCQs (Single Correct)

### Q1 (Easy)
**FreshBite** runs a food-delivery app. Their team built a **spam filter** that labels incoming emails as *Inbox* or *Junk*, and separately they use **ChatGPT** to draft polite apology emails to customers. What best describes ChatGPT's role compared to the spam filter?

A. It classifies existing emails into fixed categories only.  
B. It **creates new text** (apology drafts) rather than only scoring or labelling data.  
C. It stores every customer email in a lookup table and returns exact matches.  
D. It follows a fixed IVR menu with keyword routing.  

**Correct Answer:** B  
**Explanation:** Generative AI creates new content — here, apology drafts. The spam filter (A) only classifies. LLMs are not simple lookup tables (C). IVR keyword routing (D) describes rule-based systems, not generative drafting.

---

### Q2 (Easy)
**PaySafe** needs a login flow: send a one-time password (OTP) to the user's phone, accept the typed code, and grant access — with **no creativity** and the **same steps every time**. Which approach is the better fit?

A. **Rule-based software** with a fixed OTP verification flow  
B. A general-purpose **LLM chatbot** that improvises replies  
C. A **Random Forest** classifier trained on 500 OTP rows  
D. A **time-series forecasting** model trained on past login timestamps  

**Correct Answer:** A  
**Explanation:** OTP verification is narrow, predictable, and deterministic — ideal for rule-based logic. LLMs (B) add unnecessary variability. Time-series forecasting (D) predicts future values from past data; it does not implement a fixed OTP verification flow. Random Forest on OTP rows (C) is not how OTP systems are built.

---

### Q3 (Easy)
**TokenTrack** bills API usage by how LLMs read text internally. What is a **token** in this context?

A. A security key used to authenticate API calls  
B. The **smallest unit of text** an LLM processes (word piece, punctuation, or whitespace chunk)  
C. The maximum number of pages a model can read in one year  
D. A labelled row in a classical ML training table  

**Correct Answer:** B  
**Explanation:** Tokens are subword text chunks the model encodes to numbers. API keys (A) are unrelated. Page limits (C) confuse tokens with context windows. Labelled rows (D) describe classical ML features, not LLM tokenisation.

---

### Q4 (Easy)
A support lead tests the same customer question — *"What is my account balance?"* — twice on two systems. System **A** returns the **identical** answer both times. System **B** returns slightly different wording each time. Which pairing is most likely?

A. A = LLM, B = rule-based chatbot  
B. A = rule-based chatbot, B = LLM  
C. Both are rule-based chatbots  
D. Both are LLMs that always return word-for-word identical answers  

**Correct Answer:** B  
**Explanation:** Rule-based systems follow fixed paths → same input, same output. LLMs use probabilistic next-token prediction → answers may vary in wording. (A) reverses the roles. (C) would not explain variation on B. (D) is false — LLM outputs can vary between runs.

---

### Q5 (Moderate)
**DocuMind** uses a model with a **4,096-token context window**. The team pastes a 200-page policy PDF, 40 messages of chat history, and a system prompt into **one API call**, then asks for a summary. The combined input plus expected reply exceeds the window. What is the **most likely** result?

A. The model automatically opens a second hidden window at no cost  
B. **Earlier content is truncated or dropped** — the model may miss instructions or early document sections  
C. The API refuses to tokenise non-English text  
D. The model fetches missing pages from the internet  

**Correct Answer:** B  
**Explanation:** Context windows are hard ceilings; overflow causes truncation or loss of early context. There is no free extra window (A). Tokenisation works across languages (C is wrong). Models do not browse by default (D).

---

### Q6 (Moderate)
An engineer configures a context checker for a **4,096-token** model:

- `MODEL_CONTEXT_LIMIT = 4096`  
- `RESERVED_FOR_REPLY = 600`  
- `SAFETY_BUFFER = 200`  

What is the **safe maximum input token budget** (`usable_limit`) for the prompt alone?

A. 4,096 tokens  
B. 3,496 tokens  
C. 3,296 tokens  
D. 600 tokens  

**Correct Answer:** C  
**Explanation:** `usable_limit = 4096 − 600 − 200 = 3296`. (A) ignores reply and buffer reserves. (B) subtracts only one reserve. (D) is only the reply reserve, not the input budget.

---

## MSQs (Multiple Correct)

### Q7 (Moderate)
**LinguaPay** compares billing for three customer-message drafts before sending them to an LLM API. Which statements about **token count** are **correct**?

A. A long **URL with query parameters** usually consumes **more tokens** than a short plain-English sentence of similar meaning.  
B. A **Hindi–English mix** often has a **higher token count than word count**.  
C. Token count always equals **exact word count** for every English sentence.  
D. **Native-script Indian language** text often uses **more tokens** than equivalent English for the same meaning.  

**Correct Answers:** A, B, D  
**Explanation:** URLs and symbols split heavily (A). Hinglish and Indian scripts often tokenise into more pieces (B, D). Word count ≠ token count (C is false — e.g. *"unhappiness"* can be multiple tokens).

---

### Q8 (Moderate)
**RouteBot** is choosing between a **keyword rule router** and an **LLM** for customer intent handling. Which statements are **valid**?

A. A rule *"if message contains `refund`, route to billing"* will reliably catch *"Please return my money for the damaged item."*  
B. An LLM generates output **one token at a time** using probabilistic next-token prediction.  
C. An LLM behaves like a **database lookup** — it fetches a stored answer row for each question.  
D. **OTP verification** is a good fit for **rule-based** logic.  
E. A rule-based router typically gives the **same output for the same input** every time.  

**Correct Answers:** B, D, E  
**Explanation:** Paraphrases without the keyword break rules (A is false). LLMs predict tokens probabilistically (B). They generate text; they do not look up rows (C is false). OTP flows are deterministic (D). Rule engines are repeatable (E).

---

### Q9 (Hard)
**TrustCart** reviews four production incidents. Which **failure-mode labels** are **correctly matched**?

A. The model states a product launched in **2024**, but the company launched it in **2025** → **Knowledge cutoff / no live data**  
B. The model gives a **different word count** every time for the same paragraph → **Inconsistency** (probabilistic generation)  
C. After a **40-message** chat, the bot ignores *"respond only in Hindi"* from message 1 → **Context loss**  
D. The model invents a **refund clause** not present in the pasted policy PDF → **Hallucination**  
E. The model routes *"Press 1 for billing"* in an IVR menu → **Hallucination**  

**Correct Answers:** A, B, C, D  
**Explanation:** Stale or missing live facts (A), varying outputs (B), forgotten early instructions when the window fills (C), and fabricated policy text (D) match the failure-mode table. IVR menu routing (E) is **rule-based design**, not hallucination.

---

### Q10 (Hard)
**SafeDraft** is designing a customer-support assistant that must stay within model limits and reduce false claims. Which design choices are **sound**?

A. Measure prompt size with **`tiktoken`** (or equivalent) instead of guessing from word count alone.  
B. Reserve tokens for the **model's reply** and a **safety/system buffer**, not use 100% of the window for input.  
C. Paste a **500-page PDF** in one shot because a large context window makes retrieval unnecessary.  
D. Treat **fluent, confident** answers as automatically **fact-checked**.  
E. Split large documents into **smaller sections** and ask **targeted questions** when near the context ceiling.  
F. Expect an LLM to **verify facts** through an internal database lookup on every answer by default.  

**Correct Answers:** A, B, E  
**Explanation:** Measure tokens (A), reserve reply/buffer space (B), and split/chunk large inputs (E) align with context-window practice. Huge single uploads (C) still overflow or dilute attention. Fluency ≠ truth (D). LLMs generate; they do not auto-lookup facts (F).

---
