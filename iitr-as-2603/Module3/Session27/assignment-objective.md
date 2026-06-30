# Assignment — Objective (Session: Open-Source LLMs)

**Instructions:** Answer all questions. **MCQ** = exactly one correct option. **MSQ** = select *all* options that apply; partial marking may apply per platform rules.

---

## Section A — Easy (MCQ)

### Q1 (MCQ — Easy)

A college hackathon team wants to **download model weights once** and run demos **without internet** in a basement lab with no Wi-Fi. Which option best fits that requirement?

- A) Use GPT-4 through a paid API that streams answers from OpenAI’s servers  
- B) Pull an open-source model with **Ollama** and run inference on the laptop  
- C) Paste prompts into a browser chat tab that requires a live connection  
- D) Wait for Azure to email the model weights as a PDF attachment  

---

### Q2 (MCQ — Easy)

You installed Ollama but have **never** downloaded `qwen2.5:0.5b`. You want the weights on disk before chatting in the terminal. Which command should you run **first**?

- A) `ollama run qwen2.5:0.5b`  
- B) `ollama pull qwen2.5:0.5b`  
- C) `ollama rm qwen2.5:0.5b`  
- D) `ollama ps`  

---

### Q3 (MCQ — Easy)

On a laptop with **8 GB RAM**, a student runs `ollama pull llama3.1:70b` for a quick test. What is the **most likely** outcome?

- A) The machine runs faster than any cloud API because local is always optimal  
- B) The pull or run may fail, freeze, or make the laptop unusable because the model needs far more memory than the laptop has  
- C) Ollama silently converts the 70B tag into a 0.5B model with no warning  
- D) RAM usage stays under 500 MB because parameter count is only a marketing label  

---

### Q4 (MCQ — Easy)

Your manager asks which benchmark best shows **broad factual knowledge and reasoning across many subjects** when comparing two chatbot candidates. Which name should you cite?

- A) **MMLU**  
- B) **HellaSwag** only, because it covers every academic domain  
- C) **SWE-bench**, because it measures general encyclopedia trivia  
- D) **TruthfulQA**, because it is the only benchmark that tests coding ability  

---

## Section B — Moderate (MCQ)

### Q5 (MCQ — Moderate)

You have a working Groq script:

```python
client = Groq(api_key=...)
response = client.chat.completions.create(model="...", messages=[...])
```

You want the **same `messages` list** on **local Ollama** using the OpenAI-compatible style taught in class. What is the **minimum** change at the client layer?

- A) Replace Python with SQL and store prompts in a database table  
- B) Use `OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")` and keep `client.chat.completions.create(...)`  
- C) Delete all `role` fields because Ollama does not support chat roles  
- D) Send prompts only as raw HTTP GET requests with no JSON body  

---

### Q6 (MCQ — Moderate)

A health-tech intern types **patient appointment notes** into a VS Code script during a privacy review. Leadership requires that **prompt text must not leave the laptop** during inference. Which setup best matches that rule?

- A) Call a public cloud chat API from the script on every keystroke  
- B) Run a **small pulled model through local Ollama** so inference stays on the machine  
- C) Post the notes to a public forum and copy the top reply  
- D) Email the notes to a shared inbox for manual summarisation  

---

## Section C — Moderate (MSQ)

### Q7 (MSQ — Moderate)

You are comparing **Qwen 2.5 0.5B** on local Ollama with a **much larger cloud model** for the same homework helper. Which statements about **very small local models** are correct?

- A) They can run on many student laptops without tens of gigabytes of RAM  
- B) They never hallucinate because smaller parameter counts guarantee factual answers  
- C) They are useful for learning the API pattern, privacy-sensitive drafts, and quick prototypes  
- D) They often trade away depth of reasoning and niche factual accuracy compared with large cloud models  

---

### Q8 (MSQ — Moderate)

Your team runs a **fair comparison** between a **local Ollama model** and **Ollama Cloud** on the same FAQ prompt. Which practices should you follow?

- A) Keep the **same** system and user message text for both runs  
- B) Change the system prompt heavily for the cloud run so it “gets a fair chance”  
- C) Change **only** the host, API key handling, and `model=` identifier between runs  
- D) Raise temperature randomly between runs so answers stay unpredictable  

---

## Section D — Hard (MSQ)

### Q9 (MSQ — Hard)

A product lead is choosing between a **paid API-only model** (e.g. GPT-class) and an **open-weight model** self-hosted with Ollama. Which statements are correct?

- A) Paid API models typically cannot be downloaded as public weights for local self-hosting  
- B) Open-source weights can be pulled and run locally, though quality and RAM needs vary by size  
- C) Self-hosting eliminates all inference cost because electricity and hardware are free in every organisation  
- D) The same Python **messages** shape can often be reused across hosted APIs and local Ollama with different clients or base URLs  

---

### Q10 (MSQ — Hard)

You are wiring **Ollama Cloud** alongside **local Ollama** in one Python project. Which statements are correct?

- A) Local OpenAI-compatible calls typically use `base_url="http://localhost:11434/v1"`  
- B) Ollama Cloud OpenAI-compatible calls use `base_url="https://ollama.com/v1"` and a valid **API key**  
- C) Every local model tag is guaranteed to exist on Ollama Cloud without checking the library page  
- D) For local calls, the OpenAI library still expects a non-empty `api_key` string even though Ollama does not validate it on localhost  

---

## Answer Explanations (for Assess platform — paste per item)

### Q1 — Correct: **B**

**Reasoning:** Open-source models have **downloadable weights**; Ollama lets you pull and run them locally, including offline after the pull completes.

**Why others are wrong:** A/C/D) All depend on live remote services or are not realistic ways to obtain runnable weights.

---

### Q2 — Correct: **B**

**Reasoning:** `ollama pull` downloads model weights; `ollama run` loads and chats with an already-pulled model.

**Why others are wrong:** A) `run` before `pull` fails if the model is missing. C) `rm` deletes a model. D) `ps` shows what is loaded in memory, not first-time download.

---

### Q3 — Correct: **B**

**Reasoning:** 70B-class models often need **40+ GB** RAM; 8 GB laptops cannot host them reliably — class guidance is to avoid heavy pulls on student machines.

**Why others are wrong:** A/C/D) Misstate memory needs or Ollama behaviour.

---

### Q4 — Correct: **A**

**Reasoning:** **MMLU** measures broad knowledge and reasoning across many subjects — the standard choice for general factual comparison in the notes.

**Why others are wrong:** B) HellaSwag tests common-sense completion, not full academic breadth. C) SWE-bench targets software engineering tasks. D) TruthfulQA focuses on truthfulness, not general multi-subject exams or coding.

---

### Q5 — Correct: **B**

**Reasoning:** Local Ollama exposes an **OpenAI-compatible** endpoint at `localhost:11434/v1`; swap the client/base URL and keep `chat.completions.create` with the same messages.

**Why others are wrong:** A/C/D) Not how Ollama chat or the taught Python pattern works. Ollama supports role-based messages.

---

### Q6 — Correct: **B**

**Reasoning:** **Local inference** keeps prompts on the device — matching the privacy requirement for sensitive notes.

**Why others are wrong:** A/C/D) All expose or transmit content outside controlled local inference.

---

### Q7 — Correct: **A, C, D**

**Reasoning:** Tiny models fit weak hardware and suit learning/privacy prototypes; they trade accuracy and reasoning depth vs large models and **can** hallucinate.

**Why others are wrong:** B) Small models **can** hallucinate; class explicitly warns about confident wrong answers.

---

### Q8 — Correct: **A, C**

**Reasoning:** Fair comparison fixes prompt text and system rules; only host, auth, and model identifier change between local and cloud runs.

**Why others are wrong:** B) Changing system rules between runs confounds the test. D) Random temperature breaks comparability.

---

### Q9 — Correct: **A, B, D**

**Reasoning:** Paid APIs are usage-based without public weight download; open weights are self-hostable with hardware costs; the same messages pattern transfers across providers with client/base URL changes.

**Why others are wrong:** C) Self-hosting still costs RAM, electricity, and ops time — not “free” in every sense.

---

### Q10 — Correct: **A, B, D**

**Reasoning:** Local vs cloud differ by **base URL** and cloud **API key**; local still passes a dummy key for the OpenAI library. Cloud model names must be verified on the library — not every local tag exists remotely.

**Why others are wrong:** C) Cloud availability is not automatic for every local tag — always confirm on ollama.com/library.

---

**End of objective assignment**
