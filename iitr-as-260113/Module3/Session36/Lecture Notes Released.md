# LangChain Environment Setup and First LCEL Chain

## What You Already Know and What We Build Now

In the previous class, you learned the basic idea of **LangChain** and why we use it instead of writing only raw LLM API calls. You also saw reusable **prompt templates**, the **LCEL pipe operator**, and the role of **StrOutputParser** in getting clean text output.

Now we will connect those ideas with **Ollama**. The goal is simple: set up a clean Python project, bind LangChain to an Ollama model, build a small LCEL chain, run it, and then validate whether the output is usable before showing it to a user.

**In this lesson, you will learn:**

- How to keep a clean Python environment for LangChain work.
- How to install the required LangChain and Ollama packages.
- How to use project folders and environment variables safely.
- How to connect **ChatOllama** to a local Ollama model.
- How to build a first chain using **ChatPromptTemplate**, **ChatOllama**, and **StrOutputParser**.
- How to test and validate LLM output using simple success criteria.

---

## Why We Need a Proper Environment

Before writing LangChain code, we need a clean place where all project packages live separately.

- **Official Definition:** A **virtual environment** is an isolated Python environment that stores packages for one project without disturbing other projects.
- **In Simple Words:** It is like keeping separate notebooks for separate subjects. Your maths notes should not mix with your chemistry notes.
- **Real-Life Example:** If one college project needs an old library version and another project needs a new one, a virtual environment prevents both from fighting with each other.

For LangChain work, this matters because packages like `langchain-core`, `langchain-ollama`, and provider libraries keep changing quickly. A separate environment keeps your project predictable.

![Virtual environment isolation for LangChain projects -- global Python can have package conflicts, while each project venv keeps its own dependency versions separate](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session36/session36-01-environment-isolation.png)

### Create and activate a virtual environment

Use these commands from your project folder:

```bash
python3 -m venv venv
source venv/bin/activate
```

On Windows, activation usually looks like this:

```bash
venv\Scripts\activate
```

After activation, your terminal prompt usually shows `(venv)`. That means Python will use packages from this project environment.

---

## Required Packages

For today’s chain, we need LangChain’s core package and the Ollama integration package.

- **Official Definition:** A **package** is reusable code written by other developers and installed into your project.
- **In Simple Words:** Instead of building everything yourself, you install ready-made tools.
- **Real-Life Example:** When you cook Maggi, you do not prepare noodles and masala from scratch. You use a ready packet and focus on cooking.

Install the packages:

```bash
pip3 install langchain-core
pip3 install langchain-ollama
```

### What each package does

- **`langchain-core`** gives the basic LangChain building blocks such as prompts, output parsers, and runnables.
- **`langchain-ollama`** gives the wrapper needed to talk to Ollama models from LangChain.

If you already installed these packages, the terminal may say **requirement already satisfied**. That is fine.

---

## Safe Project Layout and Environment Variables

In real projects, code should be organised so that files are reusable and secrets are not accidentally pushed to GitHub.

- **Official Definition:** An **environment variable** is a value stored outside the code and read by the program at runtime.
- **In Simple Words:** It is a private setting kept outside your Python file.
- **Real-Life Example:** Your ATM PIN is needed to use your card, but you do not write the PIN on the card itself.

For local Ollama usage, you usually do **not** need an API key. But if you use a cloud model or paid provider later, you should store keys in environment variables or `.env` files, not directly inside Python files.

Recommended folder style:

```text
langchain_application/
├── venv/
├── .env
├── .gitignore
├── build_chain.py
└── validate_chain.py
```

### Important safety rules

- Do not hardcode API keys in Python files.
- Add `.env` to `.gitignore`.
- Keep reusable chain-building code in one file, such as `build_chain.py`.
- Keep testing or validation code in a separate file, such as `validate_chain.py`.

This is useful in collaborative work because one teammate can improve the chain and another can improve validation without editing the same long file.

---

## Ollama Local vs Ollama Cloud

Ollama helps us run open-source LLMs locally or through cloud infrastructure.

- **Official Definition:** **Ollama** is a tool for running and serving open-source large language models.
- **In Simple Words:** It lets your laptop or server behave like an LLM API provider.
- **Real-Life Example:** Instead of ordering food from outside every time, you keep basic ingredients at home and cook small meals yourself.

### Local Ollama

When Ollama runs locally, your model runs on your own machine.

- The base URL is usually `http://localhost:11434`.
- No API key is usually required.
- Model speed and quality depend on your laptop configuration.
- Small models are better for learning and demos.

### Cloud Ollama or other cloud providers

When you use cloud, the model runs on someone else’s server.

- You usually need an API key or credentials.
- You may get stronger hardware.
- You may need to pay for usage.
- The code pattern is similar, but base URL and credentials change.

For learning, local Ollama is good enough because the main goal is to understand the LangChain flow. A bigger model may give a better answer, but the code structure stays almost the same.

---

## ChatOllama: Binding LangChain to an Ollama Model

Now we connect LangChain to an Ollama model.

- **Official Definition:** **ChatOllama** is a LangChain chat model wrapper that lets your LangChain code call models served by Ollama.
- **In Simple Words:** It is the adapter between LangChain and your Ollama model.
- **Real-Life Example:** If LangChain speaks Hindi and Ollama speaks Tamil, `ChatOllama` acts like the translator who helps both talk.

To create a ChatOllama object, we mainly provide:

- **`model`**: the model name available in Ollama, such as a small Qwen model.
- **`base_url`**: where Ollama is running, usually `http://localhost:11434`.
- **`temperature`**: how creative or strict the answer should be.
- **`num_predict`**: approximate output token limit.

### Temperature

- **Official Definition:** **Temperature** controls randomness in model output.
- **In Simple Words:** Low temperature gives safer and more predictable answers. High temperature gives more creative answers.
- **Real-Life Example:** A strict school exam answer is low temperature. A creative story-writing competition is high temperature.

For beginner explanations, a middle value like `1` is acceptable. For production, you may reduce it when you need more controlled output.

---

## ChatPromptTemplate

A prompt template lets us reuse the same prompt with different inputs.

- **Official Definition:** **ChatPromptTemplate** is a LangChain prompt object designed for chat-style messages such as system and human messages.
- **In Simple Words:** It is a reusable message format where only a few values change each time.
- **Real-Life Example:** A wedding invitation has the same structure, but names, venue, and date change for every family.

### System and human messages

In a chat application, there are usually two sides:

- **System message:** tells the model how to behave.
- **Human message:** contains the user’s actual request.

Example idea:

- System: “You are a beginner-friendly programming instructor.”
- Human: “Explain `{topic}` using a simple analogy from `{analogy_domain}`.”

### Common mistake: `from_template` vs `from_messages`

If you are passing one simple string, `from_template()` is fine.

If you are passing a list of chat messages like `("system", "...")` and `("human", "...")`, use `from_messages()`.

This was an important syntax correction in the class:

- `from_template()` expects one string template.
- `from_messages()` expects a list of chat messages.

---

## LCEL: LangChain Expression Language

LCEL is the main way we compose the chain.

- **Official Definition:** **LCEL**, or **LangChain Expression Language**, is LangChain’s syntax for composing runnable components into a pipeline.
- **In Simple Words:** It lets us connect prompt, model, and parser using the pipe symbol.
- **Real-Life Example:** Think of a dosa counter: batter goes to tawa, cooked dosa goes to plate, plate goes to customer. Each step passes output to the next step.

The basic chain is:

```text
Prompt Template → Chat Model → Output Parser
```

In LCEL, we write it like this:

```python
chain = prompt | llm | parser
```

The `|` symbol is called the **pipe operator**. On most keyboards, it is available near the Enter key.

### How data moves inside the chain

- The input dictionary goes into the prompt template.
- The prompt template creates the final messages.
- The chat model receives those messages and generates a response object.
- The output parser converts that response object into a plain string.

![LCEL chain flow with LangChain and Ollama -- input dictionary goes into ChatPromptTemplate, then ChatOllama at localhost, then StrOutputParser returns a plain string response](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session36/session36-02-lcel-chain-flow.png)

---

## StrOutputParser

LLM responses are not always plain strings.

- **Official Definition:** **StrOutputParser** is a LangChain output parser that extracts text from model response objects and returns a plain Python string.
- **In Simple Words:** It removes the extra packaging and gives only the answer text.
- **Real-Life Example:** When you order from Swiggy, the food comes with bag, bill, tissue, and boxes. You finally eat only the food. `StrOutputParser` gives only the useful food part.

Without a string parser, the model may return an object such as an AI message with extra metadata. That can be useful sometimes, but for beginner apps we often want clean text.

---

## Full Code: Build the First LCEL Chain

Create a file named `build_chain.py`.

This file only builds and returns the chain. Keeping this code separate makes it reusable in other files.

```python
from langchain_ollama import ChatOllama  # Import the LangChain wrapper used to talk to Ollama chat models.
from langchain_core.prompts import ChatPromptTemplate  # Import the chat prompt template builder from LangChain Core.
from langchain_core.output_parsers import StrOutputParser  # Import the parser that converts model output into plain text.


def build_chain():  # Define a reusable function that will create and return the LCEL chain.
    prompt = ChatPromptTemplate.from_messages(  # Create a chat-style prompt using system and human messages.
        [  # Start the list of chat messages.
            (  # Start the first message tuple.
                "system",  # Mark this message as the system instruction for the model.
                "You are a beginner-friendly programming instructor. "  # Tell the model its teaching role.
                "Explain concepts clearly in simple language. "  # Ask the model to explain in simple language.
                "Use short bullet points and avoid unnecessary introduction.",  # Ask for concise output.
            ),  # End the first message tuple.
            (  # Start the second message tuple.
                "human",  # Mark this message as the user request.
                "Explain {topic} using a simple analogy from {analogy_domain}.",  # Use placeholders for dynamic inputs.
            ),  # End the second message tuple.
        ]  # End the list of chat messages.
    )  # Finish creating the chat prompt template.

    llm = ChatOllama(  # Create the Ollama chat model object.
        model="qwen:1.8b",  # Choose the Ollama model name available on your machine.
        base_url="http://localhost:11434",  # Tell LangChain where the local Ollama server is running.
        temperature=1,  # Set a balanced creativity level for the model output.
        num_predict=100,  # Ask the model to keep the generated output around a small size.
    )  # Finish creating the ChatOllama object.

    parser = StrOutputParser()  # Create a parser that converts the model response object into a plain string.

    chain = prompt | llm | parser  # Compose prompt, model, and parser into one LCEL pipeline.

    return chain  # Return the complete chain so another file can reuse it.


if __name__ == "__main__":  # Run this block only when this file is executed directly.
    chain = build_chain()  # Build the chain by calling the reusable function.
    response = chain.invoke(  # Invoke the chain with the required input values.
        {  # Start the input dictionary.
            "topic": "LangChain Expression Language",  # Provide the topic placeholder value.
            "analogy_domain": "software engineering",  # Provide the analogy domain placeholder value.
        }  # End the input dictionary.
    )  # Finish invoking the chain.
    print(response)  # Print the final string response returned by the parser.
```

### How the code works

- The imports bring the three main LangChain components into the file.
- `build_chain()` creates the full pipeline and returns it.
- `ChatPromptTemplate.from_messages()` is used because we have system and human messages.
- `ChatOllama()` connects to the local Ollama server.
- `StrOutputParser()` converts the model response into plain text.
- `prompt | llm | parser` is the LCEL chain.
- The `if __name__ == "__main__"` block lets you test the file directly.

### Running the file

Make sure Ollama is running locally and the model is available. Then run:

```bash
python3 build_chain.py
```

If you get a response, the chain is working end to end.

---

## Understanding the Output Quality

In class, the small local model generated an analogy that was not very clear. That is normal with small models.

The important point is:

- The **code worked**.
- The **chain was correctly composed**.
- The **model quality** depends on which Ollama model you use.

If you use a stronger local model or a cloud model, the response quality may improve. But the LangChain structure remains almost the same.

This is similar to using a small calculator versus a scientific calculator. The calculation process may be similar, but the bigger tool can handle more complex work.

---

## Why Validate LLM Output

LLM output should not always be sent directly to the user.

- **Official Definition:** **Output validation** is the process of checking whether generated output follows expected rules before using it.
- **In Simple Words:** We check the answer before showing it to the user.
- **Real-Life Example:** A teacher checks answer sheets before declaring final marks. Even if the student wrote something, it must be verified.

LLMs can:

- Give empty output.
- Return output in the wrong type.
- Ignore word limits.
- Hallucinate or answer unclearly.
- Break formatting instructions even when the prompt is good.

So production applications often validate responses in the background.

![LLM output validation gate -- model response is checked for string type, non-empty content, and word limit before showing it to a user or retrying](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session36/session36-03-output-validation-gate.png)

---

## Success Criteria for the First Chain

For this beginner validation, we use simple rules:

- Response should be a **string**.
- Response should **not be empty**.
- Response should **not be too long**.
- Optionally, response should follow a required bullet-point format.

These checks are not perfect, but they teach the habit of testing LLM output.

---

## Full Code: Validate the Chain

Create a second file named `validate_chain.py`.

This file imports the reusable chain and checks the response.

```python
from build_chain import build_chain  # Import the reusable chain-building function from build_chain.py.


def is_response_valid(response: str) -> tuple[bool, list[str]]:  # Define a function that returns validity and error messages.
    errors = []  # Create an empty list to store validation errors.

    if not isinstance(response, str):  # Check whether the response is not a Python string.
        errors.append("Response is not a string.")  # Add an error message when response type is wrong.
        return False, errors  # Stop further checks because non-string output cannot be stripped or split safely.

    if not response.strip():  # Remove extra spaces and check whether anything meaningful is left.
        errors.append("Response is empty.")  # Add an error message when the response has no real content.

    word_count = len(response.split())  # Split the response by spaces and count the number of words.

    if word_count > 100:  # Check whether the response is longer than the allowed limit.
        errors.append("Response is too long: more than 100 words.")  # Add an error message when output is too long.

    return len(errors) == 0, errors  # Return True if there are no errors, otherwise return False with errors.


chain = build_chain()  # Build the LCEL chain once so it can be tested.

test_case = {  # Create one test input for the chain.
    "topic": "LangChain Expression Language",  # Provide the topic that the model should explain.
    "analogy_domain": "software engineering",  # Provide the analogy domain for the explanation.
}  # End the test input dictionary.

response = chain.invoke(test_case)  # Run the chain with the test input and collect the response.

print("Generated Response:")  # Print a heading before the model response.
print(response)  # Print the actual response returned by the chain.

is_valid, errors = is_response_valid(response)  # Validate the response using the success criteria.

if is_valid:  # Check whether the validation result is successful.
    print("Valid response.")  # Print success message when all checks pass.
else:  # Run this block when validation fails.
    print("Invalid response.")  # Print failure message.
    print(errors)  # Print the list of validation errors.
```

### How the code works

- `build_chain` is imported from the first file, so we do not copy-paste the chain logic.
- `is_response_valid()` checks whether the model output follows basic rules.
- `isinstance(response, str)` confirms that the output is a string.
- `response.strip()` catches empty output even if it contains only spaces.
- `response.split()` helps count words.
- `len(errors) == 0` becomes `True` only if no validation problem was found.
- The final `if` block prints whether the response passed validation.

### Running the validation file

```bash
python3 validate_chain.py
```

If the response passes all checks, you will see:

```text
Valid response.
```

If the response fails, you will see:

```text
Invalid response.
['Response is too long: more than 100 words.']
```

---

## Testing Across Multiple Inputs

In class, the validation was shown with one test input. In real work, you should test across multiple inputs.

- **Official Definition:** A **test case** is one input scenario used to check whether code behaves correctly.
- **In Simple Words:** It is one sample question you ask your app to see whether it works.
- **Real-Life Example:** Before opening a food stall, you ask friends to try dosa, idli, and vada. Testing only one item is not enough.

You can extend the validation like this:

```python
from build_chain import build_chain  # Import the reusable chain builder.


def is_response_valid(response: str) -> tuple[bool, list[str]]:  # Define the validation function.
    errors = []  # Store all validation errors here.

    if not isinstance(response, str):  # Check whether the response is not a string.
        errors.append("Response is not a string.")  # Add an error for wrong response type.
        return False, errors  # Return early because other string checks are not safe.

    if not response.strip():  # Check whether the response is empty after removing spaces.
        errors.append("Response is empty.")  # Add an error for empty output.

    if len(response.split()) > 100:  # Check whether the response has more than 100 words.
        errors.append("Response is too long: more than 100 words.")  # Add an error for long output.

    return len(errors) == 0, errors  # Return whether the response passed all checks.


chain = build_chain()  # Build the LCEL chain.

test_cases = [  # Create multiple inputs to test the same chain.
    {  # Start the first test case.
        "topic": "LangChain Expression Language",  # Set the first topic.
        "analogy_domain": "software engineering",  # Set the first analogy domain.
    },  # End the first test case.
    {  # Start the second test case.
        "topic": "Prompt Templates",  # Set the second topic.
        "analogy_domain": "wedding invitation cards",  # Set the second analogy domain.
    },  # End the second test case.
    {  # Start the third test case.
        "topic": "Output Parsers",  # Set the third topic.
        "analogy_domain": "food delivery packaging",  # Set the third analogy domain.
    },  # End the third test case.
]  # End the list of test cases.

for test_case in test_cases:  # Loop through every test case one by one.
    response = chain.invoke(test_case)  # Run the chain for the current test case.
    is_valid, errors = is_response_valid(response)  # Validate the generated response.
    print("Input:", test_case)  # Print the input that was tested.
    print("Response:", response)  # Print the generated response.
    print("Valid:", is_valid)  # Print whether the response passed validation.
    print("Errors:", errors)  # Print validation errors if any exist.
    print("-" * 40)  # Print a separator line between test cases.
```

### Why multiple inputs matter

- One input passing does not prove the chain always works.
- Different topics may produce longer or weaker responses.
- Validation helps you notice patterns before users face issues.
- In real apps, this becomes part of **monitoring** and **observability**.

---

## Basic Observability for LLM Applications

Validation is the first step toward observability.

- **Official Definition:** **Observability** means tracking what your application is doing so you can understand failures and performance.
- **In Simple Words:** It is like CCTV for your software behaviour.
- **Real-Life Example:** A restaurant owner checks which dishes are delayed, which orders are returned, and which customers complain. Without that, improvement is guesswork.

For an LLM application, you may track:

- How many responses passed validation.
- How many responses were empty.
- How many responses were too long.
- Which topics created poor answers.
- Which model produced better results.

This becomes very important because LLMs are not guaranteed to follow instructions every time.

---

## Regeneration Loops and Human-in-the-Loop

If validation fails, the application can take action.

- **Official Definition:** A **regeneration loop** retries or corrects model output when validation fails.
- **In Simple Words:** If the answer is bad, ask the model to fix it and try again.
- **Real-Life Example:** If a student’s assignment is not acceptable, the teacher gives feedback and asks for a corrected submission.

But loops should always have a limit.

- Do not retry forever.
- Set a maximum retry count.
- If the answer is still poor, involve a human or show a safe fallback.

This connects to **human-in-the-loop**, where a person reviews, approves, or corrects the model’s output before final use.

![Observability and bounded regeneration loop -- prompt, LLM, validation, retry with feedback up to max retries, plus dashboard metrics for pass rate and failures](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session36/session36-04-observability-retry-loop.png)

---

## Where Pydantic Fits

Pydantic was briefly discussed for structured validation.

- **Official Definition:** **Pydantic** is a Python library used to validate data structures and data types.
- **In Simple Words:** It checks whether an object has the right fields and right value types.
- **Real-Life Example:** A college admission form must have name, age, phone number, and marks in the correct format. Pydantic checks that structure.

For today’s plain string response, simple Python checks are enough. If the model returns JSON or a structured object, Pydantic becomes more useful.

Example use cases:

- Check whether `name` is present.
- Check whether `age` is an integer.
- Check whether `items` is a list.
- Check whether an object follows the expected schema.

---

## Common Doubts and Fixes

### “Do I need an API key for local Ollama?”

Usually no. If your model runs on `localhost`, you normally only need the local base URL and model name.

### “Why is my model answer weak?”

Small local models may generate weak analogies or unclear explanations. The chain may be correct even when output quality is average.

### “Can I use a better model?”

Yes. You can download a larger local model if your laptop supports it, or use a cloud model. The main code structure will remain similar.

### “Why use `from_messages()`?”

Use it when you are passing system and human messages as a list. Use `from_template()` for one simple string prompt.

### “Why return the chain from a function?”

Returning the chain makes the code reusable. Another file can import `build_chain()` instead of copying the prompt, model, and parser code again.

---

## Student Practice Activity

Try this small activity after reading the notes.

1. Run `build_chain.py` with the topic `Prompt Templates` and analogy domain `school timetable`.
2. Change `temperature` from `1` to `0`.
3. Run the same input again and observe whether the output becomes stricter.
4. Change `num_predict` from `100` to `50`.
5. Run again and observe whether the answer becomes shorter.
6. Add one more test case in `validate_chain.py`.
7. Check whether validation still passes.

This activity helps you see that the chain structure is stable, while model behaviour changes based on parameters and inputs.

---

## Key Takeaways

- A clean virtual environment and safe project layout make LangChain work easier to maintain.
- `ChatOllama` connects LangChain to models running through Ollama, usually with `model` and `base_url`.
- `ChatPromptTemplate`, `ChatOllama`, and `StrOutputParser` can be composed as `prompt | llm | parser`.
- `StrOutputParser` is useful because it returns plain string output instead of complex model response objects.
- LLM output should be validated before sending it to users because models can hallucinate, ignore limits, or produce unusable output.

In the next stage of learning, this same chain-building habit will become the base for more advanced workflows with stronger validation, retries, tools, and agent-style behaviour.

---

## Important Commands, Libraries, Terminologies Used

| Item | Meaning / Use |
|---|---|
| `python3 -m venv venv` | Creates an isolated Python environment. |
| `source venv/bin/activate` | Activates the virtual environment on macOS/Linux. |
| `pip3 install langchain-core` | Installs LangChain core building blocks. |
| `pip3 install langchain-ollama` | Installs the Ollama integration for LangChain. |
| `python3 build_chain.py` | Runs the first LCEL chain file. |
| `python3 validate_chain.py` | Runs the validation file. |
| `ChatOllama` | LangChain wrapper for Ollama chat models. |
| `ChatPromptTemplate` | Reusable chat prompt structure with system/human messages. |
| `from_messages()` | Correct method when creating a prompt from multiple chat messages. |
| `from_template()` | Method for creating a prompt from one string template. |
| `StrOutputParser` | Converts model response objects into plain strings. |
| `LCEL` | LangChain Expression Language for composing chains. |
| Pipe operator `|` | Connects prompt, model, and parser into one pipeline. |
| `chain.invoke()` | Executes a LangChain chain with input values. |
| `temperature` | Controls creativity/randomness of output. |
| `num_predict` | Approximate limit for generated output length in Ollama. |
| `base_url` | Endpoint where the Ollama server is running. |
| `localhost:11434` | Common local Ollama server address. |
| Validation | Checking output before using it. |
| Observability | Monitoring how the application behaves over time. |
| Pydantic | Python library for validating structured data. |
