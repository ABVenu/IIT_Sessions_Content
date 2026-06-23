# Assignment — Objective (Ollama: Exploring Another World of LLMs)

**Instructions:** Choose the best answer for MCQs (single correct). For MSQs, **select all that apply** unless stated otherwise. Submit via the LMS objective assessment.

**Difficulty order:** Questions 1–4 (Easy, MCQ) → 5–6 (Moderate, MCQ) → 7–8 (Moderate, MSQ) → 9–10 (Hard, MSQ).

**Note:** After each question, this file lists the **correct option(s)** and **explanation** (for the Assess *Answer explanation* field and instructor use).

---

### Question 1 *(Easy — MCQ)*

Arjun is prototyping an **agent** that will read draft emails containing **student roll numbers** and internal notes. His team policy says inference must not leave the laptop for those drafts. Which setup best matches that requirement?

- A) Use the public ChatGPT website in a browser tab with no login  
- B) Pull a small **open-source** model with **Ollama** and run it **locally** on his machine  
- C) Forward every prompt by email to a teammate who has a paid GPT subscription  
- D) Store roll numbers in a spreadsheet and skip any LLM entirely  

**Correct option:** **B**

**Explanation:** **Local open-source inference** via Ollama keeps prompts on the machine for that step. **A** sends data to a third-party web service. **C** still exposes data externally. **D** avoids LLM use but does not meet the “run an LLM locally” design goal.

---

### Question 2 *(Easy — MCQ)*

You just finished installing Ollama on macOS. Before pulling any model, which command confirms the CLI is installed and on your **PATH**?

- A) `ollama chat --verify`  
- B) `ollama --version`  
- C) `pip install ollama`  
- D) `python -m ollama status`  

**Correct option:** **B**

**Explanation:** **`ollama --version`** prints the installed version — the standard verification step from setup docs. **A** and **D** are not the documented verify commands. **C** installs a Python package, not the Ollama runtime itself.

---

### Question 3 *(Easy — MCQ)*

Your Python script will call the **local** Ollama chat API on a default install. What is the **full URL** you should POST to?

- A) `https://api.openai.com/v1/chat/completions`  
- B) `http://localhost:11434/api/chat`  
- C) `http://127.0.0.1:5000/generate`  
- D) `https://ollama.com/run`  

**Correct option:** **B**

**Explanation:** Local Ollama serves chat at **`http://localhost:11434/api/chat`** (host + `/api/chat`). **A** is OpenAI’s cloud API. **C** is not Ollama’s default. **D** is not the local chat endpoint path.

---

### Question 4 *(Easy — MCQ)*

Which of the following **cannot** be downloaded as model **weights** for fully offline inference on your own laptop?

- A) A small **Qwen** tag from the Ollama library (for example `qwen2.5:0.5b`)  
- B) **OpenAI GPT** proprietary weights  
- C) An open **Llama** variant published for pull via Ollama  
- D) Any open model whose license allows redistribution through Ollama  

**Correct option:** **B**

**Explanation:** **GPT-family weights are proprietary** and run only on OpenAI’s infrastructure — you use an API, not local weights. **A**, **C**, and **D** describe open models you can pull and run locally (subject to each model’s license).

---

### Question 5 *(Moderate — MCQ)*

Meera’s laptop has **8 GB total system RAM**. On **ollama.com** she opens a model card that says it needs about **55 GB RAM**. She still wants to practise chat from Python this week. What should she do **before** `ollama run`?

- A) Run that model anyway — Ollama will automatically compress it to fit 8 GB  
- B) Pick a **smaller** model tag whose **size/RAM hints** fit her hardware (for example a sub‑2B listing)  
- C) Uninstall her operating system to free RAM  
- D) Set `"stream": true` in JSON so RAM usage becomes zero  

**Correct option:** **B**

**Explanation:** **Heavy models** can freeze or fail on typical student laptops; choosing a **light tag** is the taught rule of thumb. **A** and **C** are unsafe or unrealistic. **D** confuses streaming delivery with memory required to load weights.

---

### Question 6 *(Moderate — MCQ)*

You already have a working **local** Ollama script using `requests.post` with a `messages` payload. You now want **Ollama Cloud** with the same overall pattern. What **typically** changes compared with local?

- A) Switch from POST to GET and send the body as plain text instead of JSON  
- B) **Host URL** (for example `https://ollama.com/api/chat`), **`Authorization: Bearer <key>`** header, and often the **model tag**; the JSON payload shape stays similar  
- C) Remove the `messages` array — cloud only accepts a single field named `prompt_text`  
- D) Local requires `OLLAMA_API_KEY`; cloud never uses a key  

**Correct option:** **B**

**Explanation:** Cloud swaps **URL + Bearer token + model name** while keeping the same **chat JSON** idea. **A** misstates HTTP method and format. **C** is false — cloud still uses chat-style bodies. **D** reverses the real rule: **local** needs no API key; **cloud** does.

---

### Question 7 *(Moderate — MSQ)* — Select all that apply

Which statements describe **realistic benefits** of running a **small open model locally** through Ollama while you are learning agentic systems?

- A) You avoid **per-token cloud charges** for that local inference while experimenting  
- B) Prompts used in local inference need not be sent to a third-party cloud **for that generation step**  
- C) A **0.5B** local model will always outperform **GPT‑4** on complex medical diagnosis  
- D) You can re-run scripts and break things without worrying about a large proprietary API bill  

**Correct options:** **A, B, D**

**Explanation:** **A**, **B**, and **D** match the cost, privacy, and learning benefits from the notes. **C** is false — tiny local models are weaker on hard reasoning tasks, not universally superior.

---

### Question 8 *(Moderate — MSQ)* — Select all that apply

Your dorm study group uses **`qwen2.5:0.5b`** locally for quick Q&A. Which statements about **very small local models** are fair?

- A) They may **hallucinate** more often than large cloud models on obscure or time-sensitive facts  
- B) They are a good **learning sandbox**, not a sole authority for legal or medical decisions  
- C) They will always return **today’s live stock price** accurately without internet  
- D) Replies may be **shorter or less nuanced** than answers from large cloud models  

**Correct options:** **A, B, D**

**Explanation:** **A**, **B**, and **D** reflect documented trade-offs (quality, hallucination, trust). **C** is false — small offline models lack live market feeds and may invent numbers confidently.

---

### Question 9 *(Hard — MSQ)* — Select all that apply

You are wiring **`requests.post`** to Ollama’s **`/api/chat`** endpoint in Python. Which statements are **correct**?

- A) `requests.post(url, json=payload)` serialises the Python dict as a JSON request body  
- B) Setting `"stream": false` means you wait for the **full** reply in one JSON response  
- C) After `data = response.json()`, assistant text is commonly read from `data["message"]["content"]`  
- D) You **must** install the official **`openai`** Python package to talk to `localhost:11434`  

**Correct options:** **A, B, C**

**Explanation:** **A–C** match the local HTTP chat pattern behind the Ollama API. **D** is false — local Ollama can be called with plain **`requests`** or the **`ollama`** Python package.

---

### Question 10 *(Hard — MSQ)* — Select all that apply

Which statements about **Ollama CLI** commands and **runtime behaviour** are correct?

- A) `ollama list` shows models already **downloaded** on your machine  
- B) `ollama rm <model>` removes pulled weights and helps **free disk space**  
- C) Typical **local** HTTP calls to `localhost:11434` do **not** require `OLLAMA_API_KEY`  
- D) `ollama pull` requires a valid `OLLAMA_API_KEY` even for small local models  

**Correct options:** **A, B, C**

**Explanation:** **A**, **B**, and **C** are standard CLI and security behaviour from the session. **D** is false — **`ollama pull`** downloads weights locally and does **not** need a cloud API key.

---

**End of objective assignment.**
