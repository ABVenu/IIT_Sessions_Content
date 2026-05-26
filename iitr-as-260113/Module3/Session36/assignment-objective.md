# Assignment — Objective (Session: LangChain Environment Setup and First LCEL Chain)

**Instructions:** Answer all questions. **MCQ** = exactly one correct option. **MSQ** = select *all* options that apply; partial marking may apply per platform rules.

---

## Section A — Easy (MCQ)

### Q1 (MCQ — Easy)

Priya is starting a LangChain mini-project for a college demo. She already has other Python projects on the same laptop, and each project uses different package versions. What should she do first to keep this new project predictable?

- A) Install all packages globally with administrator permissions
- B) Create and activate a separate Python virtual environment for the project
- C) Store the project files directly inside the system Python folder
- D) Copy packages manually from another project folder

---

### Q2 (MCQ — Easy)

A learner wants to build a LangChain chain that talks to a local Ollama model. Which package provides the LangChain wrapper used to connect to Ollama chat models?

- A) `langchain-ollama`
- B) `python-dotenv`
- C) `pandas`
- D) `flask`

---

### Q3 (MCQ — Easy)

An app developer keeps a future cloud API key inside a `.env` file and adds `.env` to `.gitignore`. What is the main reason for this practice?

- A) It makes the model respond faster
- B) It prevents private credentials from being hardcoded or pushed to GitHub
- C) It automatically downloads all Ollama models
- D) It replaces the need for a virtual environment

---

### Q4 (MCQ — Easy)

A local Ollama service is running on a learner's laptop. Which base URL is commonly used when creating a `ChatOllama` object for this local setup?

- A) `https://api.openai.com/v1`
- B) `http://localhost:11434`
- C) `ftp://localhost/models`
- D) `https://github.com/langchain-ai`

---

## Section B — Moderate (MCQ)

### Q5 (MCQ — Moderate)

A learner creates this prompt:

```python
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a beginner-friendly programming instructor."),
    ("human", "Explain {topic} using an analogy from {analogy_domain}.")
])
```

Why is `from_messages()` the correct choice here?

- A) Because the prompt contains a list of chat messages with roles
- B) Because it automatically validates model output length
- C) Because it downloads the selected Ollama model
- D) Because it converts the final response into a plain string

---

### Q6 (MCQ — Moderate)

A chain is written as:

```python
chain = prompt | llm | parser
```

What best describes the data flow in this LCEL chain?

- A) Parser creates the prompt, prompt stores the model, model validates the code
- B) Prompt formats the input, model generates a response, parser converts it into plain text
- C) Model installs packages, parser activates the virtual environment, prompt prints output
- D) Input skips the prompt and goes directly to the parser

---

## Section C — Moderate (MSQ)

### Q7 (MSQ — Moderate)

Which statements about `StrOutputParser` are correct?

- A) It converts a LangChain model response object into a plain string
- B) It is useful when the app needs clean text instead of extra response metadata
- C) It creates and activates a Python virtual environment
- D) It guarantees that the model answer is factually correct

---

### Q8 (MSQ — Moderate)

A team wants to validate the output of a first LangChain chain before showing it to users. Which checks match simple beginner-level success criteria?

- A) Confirm that the response is a Python string
- B) Confirm that the response is not empty after removing extra spaces
- C) Confirm that the response stays within a reasonable word limit
- D) Confirm that the laptop's battery percentage is above 80%

---

## Section D — Hard (MSQ)

### Q9 (MSQ — Hard)

A student separates a LangChain project into `build_chain.py` and `validate_chain.py`. Which design choices are technically sound?

- A) Keep reusable chain construction inside a function such as `build_chain()`
- B) Import the reusable chain builder into the validation file instead of copy-pasting chain code
- C) Hardcode all future cloud API keys inside `build_chain.py` to simplify sharing
- D) Use multiple test cases to see whether validation behaves consistently across different inputs

---

### Q10 (MSQ — Hard)

A small local model returns a weak analogy, but the app still prints a response and validation reports that the response is a non-empty string under the word limit. Which conclusions are reasonable?

- A) The LCEL pipeline may be technically composed correctly even if the generated explanation is not very strong
- B) Model quality can depend on the selected model and available hardware
- C) Basic validation checks are helpful, but they do not prove that the answer is semantically excellent
- D) `StrOutputParser` always improves the intelligence of the selected model

---

## Answer Explanations (for Assess platform — paste per item)

### Q1 — Correct: **B**

**Reasoning:** A virtual environment isolates packages for one project, which prevents version conflicts with other projects on the same system.

**Why others are wrong:** A) Global installs can create conflicts across projects. C) System Python folders should not be used as project folders. D) Manually copying packages is unreliable and not a standard workflow.

---

### Q2 — Correct: **A**

**Reasoning:** `langchain-ollama` provides the integration/wrapper needed to call Ollama models through LangChain.

**Why others are wrong:** B) `python-dotenv` is commonly used for environment variables, not the Ollama wrapper shown here. C) `pandas` is for data analysis. D) `flask` is for building web apps, not for binding LangChain to Ollama.

---

### Q3 — Correct: **B**

**Reasoning:** Environment variables and `.env` files keep sensitive values outside source code; `.gitignore` helps prevent accidental commits of those private files.

**Why others are wrong:** A) Credential storage does not speed up model generation. C) `.env` does not download models. D) Environment variables and virtual environments solve different problems.

---

### Q4 — Correct: **B**

**Reasoning:** Local Ollama commonly serves models at `http://localhost:11434`, which is why this value is used as the local `base_url`.

**Why others are wrong:** A) This is an OpenAI-style endpoint, not local Ollama. C) FTP is not used for the LangChain chat model call. D) GitHub is a code hosting site, not the local model server.

---

### Q5 — Correct: **A**

**Reasoning:** `from_messages()` is designed for chat-style prompts represented as a list of role-message tuples, such as system and human messages.

**Why others are wrong:** B) Output validation is separate code. C) Model downloading is handled by Ollama commands, not this prompt method. D) `StrOutputParser` handles plain-string conversion, not `from_messages()`.

---

### Q6 — Correct: **B**

**Reasoning:** LCEL's pipe operator passes data through the pipeline: the prompt creates messages, the LLM produces a response object, and the parser returns clean text.

**Why others are wrong:** A) The order is reversed and conceptually incorrect. C) Package installation and environment activation are terminal setup tasks. D) The prompt is not skipped in this chain.

---

### Q7 — Correct: **A, B**

**Reasoning:** `StrOutputParser` extracts the text from a model response object and returns it as a plain string, which is useful for beginner apps that need clean text.

**Why others are wrong:** C) Virtual environments are created with Python commands, not output parsers. D) A parser changes output format; it does not guarantee factual accuracy.

---

### Q8 — Correct: **A, B, C**

**Reasoning:** Beginner validation can check whether the response is the expected type, contains meaningful content, and does not exceed the chosen length limit.

**Why others are wrong:** D) Battery level is unrelated to whether the generated response satisfies application output criteria.

---

### Q9 — Correct: **A, B, D**

**Reasoning:** Reusable chain construction belongs in a function, validation can import that function, and multiple test cases reveal behaviour across different inputs.

**Why others are wrong:** C) Hardcoding API keys in source files is unsafe and can expose secrets when code is shared.

---

### Q10 — Correct: **A, B, C**

**Reasoning:** A chain can be structurally correct while a small model gives a weak answer. Model quality depends on the selected model and environment, and basic validation only checks simple conditions such as type, emptiness, and length.

**Why others are wrong:** D) `StrOutputParser` converts response format; it does not make the model smarter.

---

**End of objective assignment**
