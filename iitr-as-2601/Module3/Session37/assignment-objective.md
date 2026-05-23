# Assignment — Objective (Session: Open-Source LLMs)

**Instructions:** Answer all questions. **MCQ** = exactly one correct option. **MSQ** = select *all* options that apply; partial marking may apply per platform rules.

---

## Section A — Easy (MCQ)

### Q1 (MCQ — Easy)

A law college team is prototyping an assistant that reads **unpublished case summaries** stored only on lab laptops. Leadership wants **no student prompts or documents sent to a US cloud API** during this phase. Which setup best matches that goal?

- A) Call OpenAI’s public chat API from every student notebook  
- B) Run inference with **Ollama** on each laptop so weights and prompts stay on the machine  
- C) Paste case text into a public web chat with no login  
- D) Email case summaries to a shared Gmail account for manual review  

---

### Q2 (MCQ — Easy)

You have never downloaded a model on your PC. You want the **weights on disk** before you chat in the terminal. Which command should you run **first**?

- A) `ollama run qwen2.5:0.5b`  
- B) `ollama pull qwen2.5:0.5b`  
- C) `ollama rm qwen2.5:0.5b`  
- D) `ollama ps`  

---

### Q3 (MCQ — Easy)

A student on an **8 GB RAM** laptop runs `ollama pull llama3.1:70b` for a class demo. What is the **most likely** outcome on typical student hardware?

- A) Instant replies faster than any cloud API  
- B) The pull or run may fail, freeze, or make the machine unusable because the model needs far more memory than the laptop has  
- C) RAM usage stays under 500 MB because “70b” is only a label  
- D) Ollama automatically shrinks the model to 0.5B without telling the user  

---

### Q4 (MCQ — Easy)

Priya is practising **hundreds** of prompt variations for a personal project. She cares about **zero per-token bills** and keeping drafts on her device. Her friend Arjun needs **Llama 3.3 70B–class** answers in **under a second** on a weak laptop. What pairing is most reasonable?

- A) Priya: local Ollama with a small pulled model; Arjun: **Groq** (or similar cloud API) for large-model speed  
- B) Both must pull 70B locally to learn properly  
- C) Priya must use only paid OpenAI; Arjun must avoid all cloud APIs  
- D) Local Ollama always beats cloud on quality and speed for every task  

---

## Section B — Moderate (MCQ)

### Q5 (MCQ — Moderate)

In Google Colab you store your Groq key in **Secrets** as `GROQ_API_KEY` and read it with `os.environ.get("GROQ_API_KEY")`. The notebook cell fails with “API key not found” even though you pasted a valid key. Which cause is **most likely**?

- A) Groq only works on Windows, not in Colab  
- B) The secret **name** does not match what the code expects, or notebook access to that secret was not enabled  
- C) You must run `ollama pull` inside Colab before any Groq call  
- D) `client.chat.completions.create` is invalid on Groq’s API  

---

### Q6 (MCQ — Moderate)

You already have a working **Groq** script using `client.chat.completions.create(...)` with `system` and `user` messages. You want the **same message list** on **Anthropic**. What change is **required** at the API call layer (keys and model names aside)?

- A) Switch to `client.messages.create(...)` instead of `client.chat.completions.create(...)`  
- B) Remove all `role` fields because Anthropic does not use roles  
- C) Send prompts only as raw HTTP GET requests with no JSON body  
- D) Replace `messages` with SQL `JOIN` syntax  

---

## Section C — Moderate (MSQ)

### Q7 (MSQ — Moderate)

You are comparing **Qwen 2.5 0.5B** running locally through Ollama vs **Llama 3.3 70B** on Groq for the same homework task. Which statements about **very small local models** are correct?

- A) They can run on many student laptops without tens of gigabytes of RAM  
- B) They never hallucinate because smaller models are always factual  
- C) They are useful for learning APIs, privacy-sensitive drafts, and quick prototypes  
- D) They often trade away depth of reasoning and niche factual accuracy compared with large cloud models  

---

### Q8 (MSQ — Moderate)

Your team runs a **fair comparison** between two cloud models on the same hospital-notes prompt. Which practices match what you should hold constant?

- A) Keep the **same** system and user message text for both runs  
- B) Change the system prompt heavily for model B so it “gets a fair chance”  
- C) Change **only** the `model=` (or provider) identifier between runs  
- D) Raise temperature randomly between runs so results stay exciting  

---

## Section D — Hard (MSQ)

### Q9 (MSQ — Hard)

A product team might ship an open-weight **Qwen** or **DeepSeek** model for geopolitical Q&A. Which statements about **training-data bias** are correct?

- A) Answers can reflect geography, language, and viewpoints present in pre-training data—not a neutral encyclopedia  
- B) Open-source weights automatically remove all cultural or regional framing  
- C) The same user prompt can get different **framing** on models trained in different media ecosystems  
- D) Teams in regulated industries may choose models audited for their **jurisdiction** rather than assuming neutrality  

---

### Q10 (MSQ — Hard)

You are browsing [ollama.com/library](https://ollama.com/library) before pulling a model for a **text-only** FAQ bot. Which statements are correct?

- A) **Modality** describes input/output types such as text, vision, audio, or video  
- B) Pulling a **vision** model for a text-only FAQ wastes disk and RAM with no benefit  
- C) `ollama pull` downloads weights; `ollama run` starts an interactive chat with a pulled model  
- D) Embeddings and full RAG pipelines were the main hands-on focus of the introductory local setup segment  

---

## Answer Explanations (for Assess platform — paste per item)

### Q1 — Correct: **B**

**Reasoning:** A **local LLM** runs on your machine; Ollama keeps prompts and data on-device during local inference—matching the privacy requirement.

**Why others are wrong:** A/C/D) All send or expose content outside controlled local inference.

---

### Q2 — Correct: **B**

**Reasoning:** `ollama pull` downloads model weights once; `ollama run` loads and chats with an already-pulled model.

**Why others are wrong:** A) `run` before `pull` fails if the model is missing. C) `rm` deletes a model. D) `ps` shows what is loaded in memory, not first-time download.

---

### Q3 — Correct: **B**

**Reasoning:** 70B-class models often need **40+ GB** RAM; 8 GB laptops cannot host them reliably—matches class guidance to avoid heavy pulls.

**Why others are wrong:** A/C/D) Misstate memory needs or Ollama behaviour.

---

### Q4 — Correct: **A**

**Reasoning:** Local small models avoid per-token cost and keep data on-device; Groq-class cloud APIs deliver large-model speed without local 70B weights.

**Why others are wrong:** B) 70B local on weak laptops is discouraged. C/D) Overgeneralise cost, quality, and speed trade-offs taught in class.

---

### Q5 — Correct: **B**

**Reasoning:** Colab Secrets must match the exact name (`GROQ_API_KEY`) and grant notebook access—common live failure mode.

**Why others are wrong:** A) Groq works from Colab. C) Ollama pull is unrelated to Groq cloud calls. D) Groq uses OpenAI-style `chat.completions.create`.

---

### Q6 — Correct: **A**

**Reasoning:** Anthropic’s Python SDK uses `client.messages.create(...)` while Groq/OpenAI use `client.chat.completions.create(...)` for the same message-list idea.

**Why others are wrong:** B) Anthropic still uses role-based messages. C/D) Not how either SDK works.

---

### Q7 — Correct: **A, C, D**

**Reasoning:** Tiny models fit weak hardware and are great for learning/privacy; they trade accuracy/reasoning vs large models and can hallucinate more—not “never wrong.”

**Why others are wrong:** B) Small models **can** hallucinate; class explicitly warns about confident wrong answers.

---

### Q8 — Correct: **A, C**

**Reasoning:** Fair comparison fixes prompt and system rules; only the model (or provider) changes.

**Why others are wrong:** B) Changing system rules between models confounds the test. D) Random temperature breaks comparability.

---

### Q9 — Correct: **A, C, D**

**Reasoning:** Bias comes from training corpora; framing differs across ecosystems; enterprises may pick jurisdiction-appropriate models.

**Why others are wrong:** B) Open weights do not remove bias—open access ≠ neutral answers.

---

### Q10 — Correct: **A, B, C**

**Reasoning:** Modality is input/output type; vision pulls are wasteful for text-only; pull vs run is core CLI. Embeddings/RAG were **mentioned**, not the main hands-on local segment.

**Why others are wrong:** D) Overstates embeddings/RAG depth in the introductory Ollama setup covered in this session.

---

**End of objective assignment**
