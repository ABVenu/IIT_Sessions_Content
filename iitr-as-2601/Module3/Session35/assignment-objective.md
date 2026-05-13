# Assignment — Objective (Session 35: GenAI Concepts for Beginners)

**Instructions:** Choose the best answer for MCQs (single correct). For MSQs, **select all that apply** unless stated otherwise. Submit via the LMS objective assessment.

**Difficulty order:** Questions 1–4 (Easy, MCQ) → 5–6 (Moderate, MCQ) → 7–8 (Moderate, MSQ) → 9–10 (Hard, MSQ).

**Note:** After each question, this file lists the **correct option(s)** and **explanation** (for the Assess *Answer explanation* field and instructor use).

---

### Question 1 *(Easy — MCQ)*

Riya is comparing traditional supervised ML pipelines (spreadsheet-style features, fixed columns) with a friend who wants an app that drafts polite customer emails from bullet points. Riya argues classical tabular models fail here mainly because:

- A) Email servers reject machine learning models  
- B) Open-ended language is hard to express as fixed numeric feature columns for every possible phrasing  
- C) Logistic regression cannot run on a laptop  
- D) Tabular data always contains more rows than text data  

**Correct option:** **B**

**Explanation:** Variable-length, meaning-rich text does not map cleanly to a fixed set of numeric columns—the usual **feature engineering bottleneck** for tabular ML. **A** is irrelevant to the modelling limitation. **C** misstates the issue as hardware. **D** confuses row counts with representational limits.

---

### Question 2 *(Easy — MCQ)*

Consider the sentence: *"I went to the bank."* For a naive model that encodes **"bank"** as a single categorical or numeric feature without surrounding context, the main difficulty is that:

- A) The token is always a spelling error  
- B) The surface form can correspond to different meanings depending on context (**word ambiguity**)  
- C) Financial institutions never appear in structured databases  
- D) The sentence always exceeds practical tokenizer limits  

**Correct option:** **B**

**Explanation:** **Word ambiguity** means the same string can label different meanings; context disambiguates—something a lone feature column cannot represent. **A**, **C**, and **D** are factually or logically weak distractors.

---

### Question 3 *(Easy — MCQ)*

A common teaching analogy compares one artificial **neuron** (or perceptron) to which classical building block?

- A) K-Means centroids  
- B) Linear regression (weighted inputs plus bias, predicting a continuous-style output before any nonlinearity)  
- C) A relational `JOIN` between tables  
- D) A UI theme configuration object  

**Correct option:** **B**

**Explanation:** A single neuron’s affine combination of inputs plus bias parallels **linear regression** intuition (weights as slopes, bias as intercept) before activation. **A**, **C**, and **D** do not fit that standard analogy.

---

### Question 4 *(Easy — MCQ)*

Compared with a classic **RNN** that consumes text strictly step by step, a **Transformer** encoder block is most accurately characterised by:

- A) Dropping all punctuation tokens  
- B) Processing all positions in the sequence in parallel and using **attention** to relate tokens  
- C) Removing hidden layers to guarantee faster training  
- D) Rasterising each token into an image tensor before prediction  

**Correct option:** **B**

**Explanation:** Transformers rely on **self-attention** over the full sequence rather than only a compressed left-to-right hidden state. **A**, **C**, and **D** are incorrect characterisations.

---

### Question 5 *(Moderate — MCQ)*

For **GPT-style generative pre-training** on large-scale web and book corpora, the dominant **self-supervised** objective is usually described as:

- A) Predicting house prices from square footage  
- B) Next-token (next-word) prediction without per-example human task labels for that phase  
- C) Sorting the vocabulary alphabetically to build an inverted index  
- D) Hand-labelling every sentence with a sentiment score before any language modelling loss  

**Correct option:** **B**

**Explanation:** Large-scale **causal language modelling** (predict the next token) drives pre-training; task labels come later if at all. **A**, **C**, and **D** misdescribe that pipeline.

---

### Question 6 *(Moderate — MCQ)*

You are budgeting tokens for an English body of text using the heuristic **≈ 0.75 words per token** (equivalently, tokens ≈ words ÷ 0.75). Roughly how many **tokens** should you plan for **90 words**?

- A) About 34 tokens  
- B) About 68 tokens  
- C) About 120 tokens  
- D) About 200 tokens  

**Correct option:** **C**

**Explanation:** 90 ÷ 0.75 = **120**. **A**, **B**, and **D** do not follow the stated rule.

---

### Question 7 *(Moderate — MSQ)* — Select all that apply

Which statements about an LLM **context window** are correct?

- A) It caps how many tokens the model can attend to in **one** forward pass, typically counting both user input and model output for that call  
- B) If a chat log exceeds the window, earlier turns that fall outside are not visible to the model on that call  
- C) A larger context window mathematically guarantees factually correct answers  
- D) **Gemini 1.5 Pro** has been publicly marketed with a context window on the order of **one million** tokens  

**Correct options:** **A, B, D**

**Explanation:** **A** and **B** state the standard definition and overflow behaviour. **D** matches widely published vendor specifications (order-of-magnitude). **C** is false: capacity ≠ correctness.

---

### Question 8 *(Moderate — MSQ)* — Select all that apply

Which statements are generally true about **tokens** and **commercial LLM billing**?

- A) Providers often meter **prompt** (input) tokens separately from **completion** (output) tokens  
- B) **Subword** tokenisers may split a rare or long technical string into multiple tokens  
- C) Setting `temperature = 2` halves the per-token price automatically  
- D) Allowing very long model answers increases completion-token usage and therefore cost or latency  

**Correct options:** **A, B, D**

**Explanation:** **A**, **B**, and **D** align with common API pricing and tokenisation practice. **C** is false: temperature controls sampling randomness, not list price.

---

### Question 9 *(Hard — MSQ)* — Select all that apply

Which statements best characterise **hallucinations** in large language models?

- A) Output can read fluent and authoritative yet be fabricated or factually incorrect  
- B) Training optimises plausible next-token continuation, not a verified lookup against a ground-truth database on every step  
- C) A model’s **knowledge cutoff** can contribute to confident mistakes about events after training data ends  
- D) Hallucinations become impossible if the user’s prompt is polite  

**Correct options:** **A, B, C**

**Explanation:** **A–C** capture standard definitions and mechanisms taught in LLM safety primers. **D** is false: tone does not remove structural hallucination risk.

---

### Question 10 *(Hard — MSQ)* — Select all that apply

Which statements align with the widely taught **historical / architectural** narrative for modern LLMs?

- A) **Word2Vec**-style dense vectors let vector arithmetic approximate semantic relations between words  
- B) Vanilla **RNNs** often struggle to carry information from very early tokens across very long sequences  
- C) Generative **pre-training** on raw text at scale required a human label for every token in Wikipedia before any next-token loss could be defined  
- D) **Self-attention** lets each position attend to every other position, easing long-range dependencies compared with strict left-to-right recurrence alone  

**Correct options:** **A, B, D**

**Explanation:** **A**, **B**, and **D** are textbook-accurate. **C** is false: next-token LM does not use per-token human labels for the main objective.

---

**End of objective assignment.**
