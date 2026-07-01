# Subjective Assignment: Build a Campus Study Buddy LCEL Chain

## Practical Task (Medium)

A campus learning app wants a small Python module that explains study topics to different student groups using one reusable LangChain pipeline. Your task is to build a single-file chain that loads Ollama settings from `.env`, uses a chat-style prompt, and returns clean text through LCEL.

### Scenario

The app should explain any study topic to a chosen audience using a real-life analogy domain — for example, explaining **"hash tables"** to **"first-year students"** using an analogy from **"library shelf numbers"**.

### Requirements

Write a Python program named `study_buddy_chain.py` that:

1. Imports `os`, `load_dotenv` from `dotenv`, `ChatPromptTemplate` from `langchain_core.prompts`, `StrOutputParser` from `langchain_core.output_parsers`, and `ChatOllama` from `langchain_ollama`.
2. Calls `load_dotenv()` before reading any configuration values.
3. Reads these values from the environment (with the same defaults shown below if a key is missing):
   - `OLLAMA_MODEL` default `"qwen2.5:0.5b"`
   - `OLLAMA_HOST` default `"http://localhost:11434"`
   - `OLLAMA_TEMPERATURE` default `"0.3"` converted to `float`
4. Creates a `ChatPromptTemplate` using `from_messages()` with:
   - a **system** message that sets the role as a friendly campus tutor and asks for simple language with short bullet points
   - a **human** message with placeholders `{topic}`, `{audience}`, and `{analogy_domain}`
5. Creates a `ChatOllama` instance using the model name, base URL, and temperature from step 3.
6. Creates a `StrOutputParser`.
7. Builds an LCEL chain in this exact order:

```python
chain = prompt | llm | output_parser
```

8. Defines **two** test input dictionaries inside the program (do not ask the user for input) and runs `chain.invoke(...)` for each one.
9. For each run, prints:
   - the input dictionary
   - the response string
   - whether the response is valid using a small helper that returns `False` if the response is not a `str` or is empty after `strip()`
10. After both runs, prints how many of the two validation checks passed.

### Test Inputs to Use

Use exactly these two input dictionaries:

```python
test_cases = [
    {
        "topic": "hash tables",
        "audience": "first-year students",
        "analogy_domain": "library shelf numbers",
    },
    {
        "topic": "Git branches",
        "audience": "beginners",
        "analogy_domain": "parallel notebook drafts",
    },
]
```

### Example Output Shape

Exact wording will vary because the LLM generates the answer, but your program output should look similar to this:

```text
Input: {'topic': 'hash tables', 'audience': 'first-year students', 'analogy_domain': 'library shelf numbers'}
Response: Hash tables help you store and find values quickly using keys. Think of library shelf numbers ...
Valid: True
----------------------------------------
Input: {'topic': 'Git branches', 'audience': 'beginners', 'analogy_domain': 'parallel notebook drafts'}
Response: Git branches let you work on separate versions of the same project ...
Valid: True
----------------------------------------
Passed 2 of 2 validation checks.
```

### Constraints

- Use a **single** Python file named `study_buddy_chain.py`.
- Use only the LangChain components listed in the requirements.
- Do not use agents, tools, memory, retrievers, or vector databases.
- Ollama must be installed and running locally.
- The model name in `.env` (or the default) must match a model available in `ollama list`.
- If `qwen2.5:0.5b` is not available, pull it using:

```bash
ollama pull qwen2.5:0.5b
```

- Create a local `.env` file in the same folder with at least:

```text
OLLAMA_MODEL=qwen2.5:0.5b
OLLAMA_HOST=http://localhost:11434
OLLAMA_TEMPERATURE=0.3
```

- Install required packages inside your activated virtual environment:

```bash
pip install langchain-core langchain-ollama python-dotenv
```

### Submission Instruction

1. Code all the points mentioned above in VS Code in a single `.py` file named `study_buddy_chain.py`.
2. Run the code and verify that it is working.
3. Submit the complete code in the code editor/answer box in the LMS.

---

## Answer Explanation

### Ideal Solution Walkthrough

The program should load configuration from `.env` first, then build a reusable LCEL chain. `ChatPromptTemplate.from_messages()` separates system behaviour from the human request. `ChatOllama` connects to the local Ollama server using values from the environment. `StrOutputParser` ensures each `invoke` result is a plain string suitable for printing or UI display.

The two fixed test dictionaries prove the same chain works across different inputs without rewriting the prompt. The small validation helper checks structural correctness (string type and non-empty content), which is enough for this assignment.

### Complete Code

```python
# Standard library — read configuration from the environment
import os  # Access environment variables after dotenv loads them

# Load .env file into os.environ before reading any settings
from dotenv import load_dotenv  # Reads key=value pairs from .env on disk

# LangChain Core — prompt template and output parser
from langchain_core.prompts import ChatPromptTemplate  # Chat messages with {placeholders}
from langchain_core.output_parsers import StrOutputParser  # Returns plain string from model reply

# Ollama integration — chat model wrapper
from langchain_ollama import ChatOllama  # Runnable that talks to your Ollama server

# Load .env from the same folder as this script
load_dotenv()  # Makes OLLAMA_MODEL, OLLAMA_HOST, etc. available via os.environ

# Read model settings from .env — defaults match local teaching setup
MODEL_NAME = os.environ.get("OLLAMA_MODEL", "qwen2.5:0.5b")  # Must match ollama list
BASE_URL = os.environ.get("OLLAMA_HOST", "http://localhost:11434")  # Local Ollama address
TEMPERATURE = float(os.environ.get("OLLAMA_TEMPERATURE", "0.3"))  # Lower = more stable demos


def is_response_valid(response: str) -> bool:
    # Return False if output is not a string or is empty after stripping whitespace
    if not isinstance(response, str):  # Parser should return str — guard anyway
        return False  # Non-string output fails validation
    if not response.strip():  # Whitespace-only counts as empty
        return False  # Empty output fails validation
    return True  # Passed basic structural checks


def build_chain():  # Factory function — returns a reusable LCEL chain
    # Chat-style prompt with separate system and human roles
    prompt = ChatPromptTemplate.from_messages([  # Use from_messages for role tuples
        ("system", (  # System instruction — how the model should behave
            "You are a friendly campus study tutor. "
            "Explain concepts in simple language with short bullet points. "
            "Keep answers practical for college learners."
        )),
        ("human", (  # User request with placeholders filled at invoke time
            "Explain {topic} to {audience} using one analogy from {analogy_domain}."
        )),
    ])

    # ChatOllama Runnable — model settings from .env block above
    llm = ChatOllama(
        model=MODEL_NAME,  # Tag from OLLAMA_MODEL — same as ollama list
        base_url=BASE_URL,  # Host from OLLAMA_HOST — usually localhost:11434
        temperature=TEMPERATURE,  # Creativity knob from OLLAMA_TEMPERATURE
    )

    output_parser = StrOutputParser()  # Last step — chain output becomes a str

    # LCEL composition: template → model → parser
    chain = prompt | llm | output_parser  # Pipe declares left-to-right order

    return chain  # Caller can invoke without rebuilding the pipeline


def main():  # Run chain and validation when executed directly
    chain = build_chain()  # Build once — reuse for every test input

    # Two distinct inputs — proves placeholders drive behaviour, not hard-coded prompts
    test_cases = [
        {
            "topic": "hash tables",
            "audience": "first-year students",
            "analogy_domain": "library shelf numbers",
        },
        {
            "topic": "Git branches",
            "audience": "beginners",
            "analogy_domain": "parallel notebook drafts",
        },
    ]

    passed = 0  # Count how many inputs meet success criteria

    for test_input in test_cases:  # Loop — one invoke per distinct input dict
        result = chain.invoke(test_input)  # Run full LCEL pipeline
        valid = is_response_valid(result)  # Check basic success criteria

        print("Input:", test_input)  # Show which placeholders were used
        print("Response:", result)  # Plain string thanks to StrOutputParser
        print("Valid:", valid)  # True or False
        print("-" * 40)  # Visual separator between test cases

        if valid:
            passed += 1  # Track pass rate across inputs

    print(f"Passed {passed} of {len(test_cases)} validation checks.")


if __name__ == "__main__":  # Standard Python entry point
    main()  # Only runs when you execute: python study_buddy_chain.py
```

### Alternative Approaches

- The validation helper can also check a maximum word count, similar to `hello_chain.py`, but the assignment only requires string type and non-empty checks.
- The same chain structure works for other topics by changing only the test input dictionaries.
- A different local Ollama model can be used if `OLLAMA_MODEL` in `.env` is updated to a tag available in `ollama list`.
