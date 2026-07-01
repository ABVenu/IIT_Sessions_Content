# Objective Assignment: LangChain Environment Setup and First LCEL Chain

## Multiple Choice Questions (Single Correct)

### Q1. Easy

Rahul is building a LangChain project on his laptop while also maintaining another Python project that needs different package versions. His classmate asks why he created a `venv` instead of installing everything into system Python. What is the best explanation?

A. A virtual environment isolates project-specific packages so different projects do not conflict on the same machine  
B. A virtual environment permanently removes global Python from the laptop  
C. A virtual environment is required only for JavaScript projects  
D. A virtual environment replaces the need for `pip`  

**Correct Answer:** A

**Answer Explanation:**  
A `venv` gives each project its own isolated Python and `site-packages` folder, which prevents version conflicts between projects. Option B is wrong because global Python is not removed. Option C is wrong because `venv` is a Python feature. Option D is wrong because `pip` is still used inside the venv to install packages.

---

### Q2. Easy

A team is preparing a LangChain worktree for GitHub. They want teammates to reproduce configuration without leaking private keys. Which file should **not** be committed to the repository?

A. `.env`  
B. `.env.example`  
C. `requirements.txt`  
D. `hello_chain.py`  

**Correct Answer:** A

**Answer Explanation:**  
The `.env` file may contain secrets such as API keys and machine-local settings, so it belongs in `.gitignore`. `.env.example` is a safe committed template with placeholders. `requirements.txt` and `hello_chain.py` are normal project files that should be shared with the team.

---

### Q3. Easy

In a LangChain script, the developer wants configuration values from a `.env` file to be available through `os.environ` before building the chain. Which package provides `load_dotenv()` for this purpose?

A. `python-dotenv`  
B. `langchain-core`  
C. `langchain-ollama`  
D. `venv`  

**Correct Answer:** A

**Answer Explanation:**  
`python-dotenv` loads key-value pairs from a `.env` file into the environment so they can be read with `os.environ.get(...)`. `langchain-core` provides prompts, parsers, and LCEL. `langchain-ollama` provides `ChatOllama`. `venv` creates isolated environments but does not load `.env` files.

---

### Q4. Easy

A developer runs `result = chain.invoke({...})` on a chain defined as `prompt | llm`. The printed value looks like an `AIMessage` object instead of readable text. What is the most appropriate fix?

A. Add `StrOutputParser()` at the end of the chain  
B. Remove `ChatOllama` from the chain  
C. Delete the `.env` file  
D. Change `temperature` to `0` only  

**Correct Answer:** A

**Answer Explanation:**  
Without an output parser, the chain returns the raw model response object. `StrOutputParser` extracts plain text so `invoke` returns a Python string. Removing `ChatOllama` would break the chain. Deleting `.env` or changing temperature alone does not convert the response type to a string.

---

### Q5. Moderate

Meera is building a chat-style prompt with a separate **system** instruction and a **human** question that uses placeholders `{topic}` and `{audience}`. Which approach is correct?

A. `ChatPromptTemplate.from_messages([("system", "..."), ("human", "...")])`  
B. `ChatPromptTemplate.from_template([("system", "..."), ("human", "...")])`  
C. `StrOutputParser.from_messages([("system", "..."), ("human", "...")])`  
D. `load_dotenv().from_messages([("system", "..."), ("human", "...")])`  

**Correct Answer:** A

**Answer Explanation:**  
Role-based chat prompts with system and human messages should be built using `from_messages()`. `from_template()` is for a single string template, not a list of role tuples. `StrOutputParser` parses output; it does not build prompts. `load_dotenv()` only loads environment variables.

---

### Q6. Moderate

A script defines:

```python
chain = prompt | llm | output_parser
```

and calls:

```python
chain.invoke({
    "topic": "virtual environments",
    "audience": "beginners",
    "analogy_domain": "hostel cupboards",
})
```

What is the correct order of operations inside this LCEL chain?

A. Placeholders are filled in the prompt, the LLM generates a response, and the output parser returns a plain string  
B. The output parser runs first, then the LLM, then the prompt  
C. The `.env` file is committed to GitHub automatically  
D. `invoke` only works when temperature is set to `1.0`  

**Correct Answer:** A

**Answer Explanation:**  
LCEL runs left to right: `ChatPromptTemplate` fills placeholders from the input dict, `ChatOllama` calls the model, and `StrOutputParser` extracts text. Option B reverses the pipe order incorrectly. Options C and D describe behaviour that does not happen during `invoke`.

---

## Multiple Select Questions (Multiple Correct)

### Q7. Moderate

A cohort is setting up a shared LangChain worktree named `langchain_worktree/`. Which practices support safe, reproducible collaboration?

A. Add `.env` to `.gitignore`  
B. Commit `.env.example` with the same keys as `.env` but without real secrets  
C. Hardcode the Ollama API key directly inside `hello_chain.py`  
D. List required packages in `requirements.txt` and install them with `pip install -r requirements.txt`  

**Correct Answers:** A, B, D

**Answer Explanation:**  
Ignoring `.env`, sharing `.env.example`, and pinning dependencies in `requirements.txt` are standard collaborative practices. Hardcoding secrets in Python files is unsafe and makes rotation difficult, so option C should not be selected.

---

### Q8. Moderate

A learner is building a minimal local chain that uses `ChatPromptTemplate`, `ChatOllama`, `StrOutputParser`, and configuration loaded from `.env`. Which packages are directly required?

A. `langchain-core`  
B. `langchain-ollama`  
C. `python-dotenv`  
D. `langchain-openai` — required even when the chain uses only local Ollama  

**Correct Answers:** A, B, C

**Answer Explanation:**  
`langchain-core` supplies prompts, parsers, and LCEL. `langchain-ollama` supplies `ChatOllama`. `python-dotenv` loads `.env` values. `langchain-openai` is only needed when using OpenAI models, not for a local Ollama-only chain, so option D is incorrect.

---

### Q9. Hard

When `chain.invoke(input_dict)` runs on `prompt | llm | output_parser`, which statements about data flow are correct?

A. `ChatPromptTemplate` uses keys from `input_dict` to fill placeholders such as `{topic}` and `{audience}`  
B. `ChatOllama` sends the prepared chat messages to the configured Ollama server  
C. `StrOutputParser` converts the model response into a plain Python string  
D. The pipe operator `|` executes the parser first, then the LLM, then the prompt  

**Correct Answers:** A, B, C

**Answer Explanation:**  
The chain flows prompt → LLM → parser. Placeholders are filled at invoke time, the model generates a response, and the parser extracts text. Option D is wrong because LCEL executes from left to right, not in reverse.

---

### Q10. Hard

A developer is tuning and validating a first LCEL chain that reads `OLLAMA_MODEL`, `OLLAMA_HOST`, and `OLLAMA_TEMPERATURE` from `.env`. Which statements are correct?

A. Running `load_dotenv()` before `os.environ.get(...)` ensures `.env` values are available at runtime  
B. A lower temperature such as `0.3` usually produces more focused wording than a higher temperature such as `0.9`  
C. A simple validation check can confirm the chain output is a non-empty string  
D. The standard way to share private API keys with teammates is to commit `.env` to GitHub  

**Correct Answers:** A, B, C

**Answer Explanation:**  
Configuration should be loaded before reading environment variables. Lower temperature reduces randomness; higher temperature increases creativity. Basic validation can check type and non-empty content. Option D is wrong because secrets should stay out of version control; share `.env.example` instead.
