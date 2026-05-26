# Assignment — Subjective (Session: LangChain Environment Setup and First LCEL Chain)

**Difficulty:** Medium  
**Type:** Coding implementation

---

## Scenario

You are helping a student support team build a tiny local AI helper called **Concept Coach**. The helper should explain programming concepts in simple language using an analogy chosen by the user. The team also wants a basic validation file so weak or unusable responses are noticed before they are shown in a demo.

## Task

Create a small LangChain + Ollama project that builds one reusable LCEL chain and validates its output across multiple inputs.

### Functional requirements

1. Create a project folder named `concept_coach_chain`.
2. Inside the folder, create these files:
   - `build_chain.py`
   - `validate_chain.py`
   - `.gitignore`
3. In `build_chain.py`, create a function named `build_chain()` that:
   - Uses `ChatPromptTemplate.from_messages()`.
   - Has one system message that makes the model act like a beginner-friendly programming instructor.
   - Has one human message that accepts two placeholders: `{topic}` and `{analogy_domain}`.
   - Uses `ChatOllama` with:
     - `model="qwen:1.8b"`
     - `base_url="http://localhost:11434"`
     - `temperature=1`
     - `num_predict=100`
   - Uses `StrOutputParser`.
   - Returns the chain composed as `prompt | llm | parser`.
4. In `validate_chain.py`, import `build_chain()` and create a function named `is_response_valid(response: str) -> tuple[bool, list[str]]` that checks:
   - Response must be a string.
   - Response must not be empty after trimming spaces.
   - Response must not be more than 100 words.
5. Test the chain using at least these three inputs:
   - Topic: `LangChain Expression Language`; analogy domain: `school assembly line`
   - Topic: `Prompt Templates`; analogy domain: `wedding invitation cards`
   - Topic: `Output Parsers`; analogy domain: `food delivery packaging`
6. For each test case, print:
   - Input dictionary
   - Generated response
   - Validation result
   - Validation errors, if any
7. In `.gitignore`, include at least:
   - `venv/`
   - `.env`
   - `__pycache__/`

### Expected run commands

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install langchain-core
pip3 install langchain-ollama
python3 validate_chain.py
```

If Ollama and the selected model are available locally, the program should generate responses and display whether each response passed validation.

---

## Submission instructions (Case D — multiple files/folder structure)

- Create a repo `agentic-systems` (if done use the same) and clone it (ignore if already done).
- In that repo, create a folder called `Module3` (ignore if already done).
- In that folder, create a folder called `Session36`.
- Inside `Session36`, create the `concept_coach_chain` project folder and code all files mentioned in the question.
- Do add all ignorable files like `.env`, generated cache folders, virtual environment folders, and configs to `.gitignore` wherever applicable.
- Run the code and verify it is working.
- Then add, commit, and push the code to GitHub.
- Submit the `Module3/Session36/concept_coach_chain` folder link as the submission link. Do not submit the entire repo link.

---

## Answer Explanation (for Assess platform)

### Ideal solution walkthrough

The solution should keep chain construction separate from validation. `build_chain.py` should only create and return the LCEL chain. `validate_chain.py` should import the chain builder, run multiple inputs, and check whether the returned output is usable according to basic success criteria.

The prompt should use `ChatPromptTemplate.from_messages()` because the chain has role-based chat messages. `ChatOllama` connects LangChain to the local Ollama server, and `StrOutputParser` converts the model response object into plain text. The validation function does not judge deep factual quality, but it catches basic failures such as wrong type, empty output, and overly long answers.

### Complete expected code

`build_chain.py`

```python
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama


def build_chain():
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a beginner-friendly programming instructor. "
                "Explain concepts clearly in simple language. "
                "Use short bullet points and avoid unnecessary introduction.",
            ),
            (
                "human",
                "Explain {topic} using a simple analogy from {analogy_domain}.",
            ),
        ]
    )

    llm = ChatOllama(
        model="qwen:1.8b",
        base_url="http://localhost:11434",
        temperature=1,
        num_predict=100,
    )

    parser = StrOutputParser()
    chain = prompt | llm | parser

    return chain


if __name__ == "__main__":
    chain = build_chain()
    response = chain.invoke(
        {
            "topic": "LangChain Expression Language",
            "analogy_domain": "school assembly line",
        }
    )
    print(response)
```

`validate_chain.py`

```python
from build_chain import build_chain


def is_response_valid(response: str) -> tuple[bool, list[str]]:
    errors = []

    if not isinstance(response, str):
        errors.append("Response is not a string.")
        return False, errors

    if not response.strip():
        errors.append("Response is empty.")

    if len(response.split()) > 100:
        errors.append("Response is too long: more than 100 words.")

    return len(errors) == 0, errors


chain = build_chain()

test_cases = [
    {
        "topic": "LangChain Expression Language",
        "analogy_domain": "school assembly line",
    },
    {
        "topic": "Prompt Templates",
        "analogy_domain": "wedding invitation cards",
    },
    {
        "topic": "Output Parsers",
        "analogy_domain": "food delivery packaging",
    },
]

for test_case in test_cases:
    response = chain.invoke(test_case)
    is_valid, errors = is_response_valid(response)

    print("Input:", test_case)
    print("Response:", response)
    print("Valid:", is_valid)
    print("Errors:", errors)
    print("-" * 40)
```

`.gitignore`

```gitignore
venv/
.env
__pycache__/
```

### Alternative approaches

Students may use another locally available Ollama model if `qwen:1.8b` is not installed, but they should clearly mention the model name they used. They may also add extra validation checks, such as requiring bullet points, as long as the required three checks are present and correct.

---

**End of subjective assignment**
