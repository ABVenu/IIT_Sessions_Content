# Introduction to LangChain: Concepts Architecture and First Demo

## Context of This Session

In the **previous** session, you worked with **Ollama**, pulled a local model, called it from **Python**, and understood that a model can run either locally or through a cloud provider.

That solved one important question: **how do we call an LLM from code?**

This session answers the next question: **how do we build a proper AI application without writing too much repeated glue code?**

In this session, you will learn:

- What **LangChain** is and why teams use it.
- Why raw LLM API calls are not enough for bigger applications.
- Where LangChain sits in an AI product architecture.
- What **Runnables**, **chains**, **tools**, **memory**, and **retrievers** mean.
- How **LangChain Core**, **Community**, and provider packages are different.
- How to create reusable prompts with **PromptTemplate**.
- How to connect **PromptTemplate -> LLM -> output parser** using **LCEL** and the pipe operator.
- How a minimal LangChain chain works end-to-end with **Ollama**.

---

## Why Just Calling the LLM Is Not Enough

Many beginners think an AI app is only:

```text
send prompt -> get answer -> show answer
```

This is fine for a small demo, but a real product needs more parts.

- **Official Definition:** A modern LLM application combines the model with **tools**, **memory**, **retrieval**, **prompting**, and **post-processing**.
- **In Simple Words:** The LLM is the **brain**, but the app also needs hands, notes, files, and a proper workflow.
- **Real-Life Example:** A college helpdesk chatbot may first answer normal questions. Later it may need to read PDF rules, remember the student's hostel block, call an API for mess timings, and format the answer cleanly.

![A real LLM app combines the model brain with tools, memory, documents, and pre/post-processing - not a single chat call](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session35/session35-01-modern-llm-app.png)

If you build everything manually, you repeatedly write code for:

- Calling the model.
- Formatting prompts.
- Connecting tools.
- Reading documents.
- Managing memory.
- Parsing the model output.
- Switching from one model provider to another.

This repeated code becomes difficult to maintain as the project grows.

---

## What Is LangChain?

- **Official Definition:** **LangChain** is an open-source framework for building LLM-powered applications by connecting models, prompts, tools, memory, retrievers, and workflows in a structured way.
- **In Simple Words:** LangChain gives ready-made blocks so you do not write every integration from scratch.
- **Real-Life Example:** Think of a railway booking platform. You do not separately visit different counters for train search, payment, ticket generation, and messages. One system coordinates everything for you.

LangChain does a similar job for AI applications.

It helps connect:

- **LLMs** such as Ollama, Groq, OpenAI, or Gemini.
- **Prompts** that can be reused.
- **Tools** such as Gmail, Slack, calculators, or APIs.
- **Memory** so the app can remember conversation context.
- **Retrievers** for RAG over PDFs, websites, or internal documents.
- **Chains** so multiple steps can run in a fixed order.

![LangChain orchestrates your app with LLM providers, vector DBs, tools, and more - like one coordination layer for many AI parts](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session35/session35-02-langchain-orchestration.png)

---

## Why Use a Framework Instead of Raw API Calls?

- **Official Definition:** A **framework** provides reusable code for common tasks so developers can focus on business logic.
- **In Simple Words:** Many developers need the same repeated code. A framework writes that code once and lets everyone reuse it.
- **Real-Life Example:** You can build a website using only HTML, CSS, and JavaScript. But frameworks like React or Next.js save time by giving reusable components and structure.

LangChain works in a similar way for AI applications.

If you directly connect every LLM, tool, memory system, and retriever yourself, you may write a lot of repeated code.

With LangChain, many of those operations become function calls or reusable components.

| Without LangChain | With LangChain |
| --- | --- |
| Write custom API calls repeatedly | Use model wrappers like `ChatOllama` |
| Copy-paste prompt strings | Use `PromptTemplate` |
| Manually connect steps | Use chains and LCEL |
| Manually extract output | Use output parsers |
| Harder provider switching | Change the model/provider binding in fewer places |

### Composability and Maintainability

- **Composability** means small components can be connected together.
- **Maintainability** means the code remains easier to update later.

For example, if a prompt is written in five files, changing the wording becomes painful. If the prompt is written once as a template, you change it in one place.

This is why LangChain becomes useful when an app grows beyond a single script.

---

## Where LangChain Sits in the Agentic Stack

LangChain does not replace the LLM.

LangChain also does not replace your business logic.

It usually sits **between the model provider and your application logic**.

```text
User -> UI / App -> Backend API -> LangChain layer
                                      |
                                      v
                LLMs, tools, memory, retrievers, vector DBs, APIs
```

- **Model provider layer:** Ollama, Groq, OpenAI, Gemini, or another LLM provider.
- **LangChain layer:** Prompt templates, chains, tools, retrievers, memory, and output parsers.
- **Application layer:** Your product logic, backend APIs, and UI.

![User request flows through your backend into LangChain, which coordinates LLMs, databases, tools, and embeddings like a conductor](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session35/session35-03-agentic-stack.png)

- **Official Definition:** **Orchestration** means coordinating multiple components so they work together as one workflow.
- **In Simple Words:** LangChain acts like a coordinator between your LLM and the other parts of your app.
- **Real-Life Example:** In a company app, the user may ask a question. The backend sends it to the AI layer. LangChain can coordinate the prompt, LLM, tool call, retriever, and final output.

---

## N8N vs LangChain

The session also clarified that **N8N** and **LangChain** are not the same thing.

| Tool | What it is | Main idea |
| --- | --- | --- |
| **N8N** | No-code / low-code automation platform | Build workflows visually |
| **LangChain** | Code framework for LLM apps | Build AI workflows using Python code |

- **N8N** is useful when you want to create automation workflows without writing much code.
- **LangChain** is useful when you are building coded AI applications and want reusable LLM components.

In simple words, **N8N is more like a visual automation tool**, while **LangChain is a programming framework**.

---

## When to Use LangChain and When to Build From Scratch

LangChain is helpful, but it is not always the answer for every project.

- Use **LangChain** when your project is generic or medium-complexity.
- Build from scratch when your project needs deep customization.

For example, in a simple RAG project, LangChain's default retriever and chain patterns may be enough.

But in a complex production RAG system, you may want to fully control:

- Chunking strategy.
- Embedding model.
- Retrieval ranking.
- Generation logic.
- Prompt formatting.
- Evaluation and logging.

- **Real-Life Example:** Buying ready-made clothes is fast and works for many people. Getting clothes stitched by a tailor takes more effort but gives deeper customization.

LangChain is like a ready-made framework. Building from scratch is like tailoring every component yourself.

---

## Runnable Mental Model

LangChain uses a common idea called a **Runnable**.

- **Official Definition:** A **Runnable** is a unit of work that takes input, performs an operation, and returns output.
- **In Simple Words:** It is one small component that can run.
- **Real-Life Example:** In a document pipeline, one component may scrape data, another may clean it, another may chunk it, and another may store it.

Each of these can be understood as a runnable-style component:

```text
input -> component does work -> output
```

![Runnables snap together like LEGO blocks; a chain passes each step's output to the next - like an assembly line](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session35/session35-04-runnables-chain.png)

In a basic LangChain flow, the runnable components may be:

```text
PromptTemplate -> LLM -> OutputParser
```

Each component receives something and sends something to the next component.

---

## What Is a Chain?

- **Official Definition:** A **chain** is an ordered sequence of connected steps where the output of one step becomes input to the next.
- **In Simple Words:** A chain is a pipeline.
- **Real-Life Example:** Making chai has a sequence: boil water -> add tea -> add milk -> strain.

In LangChain, a simple chain can look like this:

```text
prompt -> llm -> output parser
```

The chain helps maintain the order.

It says:

1. First create the prompt.
2. Then send the prompt to the LLM.
3. Then parse the output.

---

## LangChain Modules in a Single-Agent Workflow

LangChain has many modules. In this session, most modules were introduced conceptually, while the practical demo focused mainly on prompts, LLM calls, LCEL, and output parsing.

| LangChain module | Role in an AI agent |
| --- | --- |
| **Chains** | Connect fixed steps in order |
| **Agents** | Let the LLM decide which action or tool to use |
| **Tools** | External actions such as Gmail, Slack, calculator, APIs |
| **Memory** | Stores useful conversation context |
| **Retrievers** | Fetch relevant data from documents or vector DBs |
| **Prompts** | Give structured instructions to the LLM |
| **Output Parsers** | Convert raw model output into useful format |

![Six LangChain building blocks - models, prompts, chains, memory, indexes for RAG, and agents that pick tools](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session35/session35-06-six-components.png)

A possible single-agent workflow can be:

1. User asks a question.
2. Retriever fetches relevant data if needed.
3. PromptTemplate prepares the final instruction.
4. LLM generates an answer.
5. Output parser cleans the result.
6. Memory can store context for later turns.
7. Agent logic can choose tools when needed.

The session introduced these modules, but detailed hands-on work for agents, memory, tools, and retrievers will come later.

---

## Agents and Tools Overview

- **Official Definition:** An **agent** is an LLM-driven component that decides what action to take next, often by selecting a tool.
- **In Simple Words:** The model does not only answer. It can decide which helper to call.
- **Real-Life Example:** If the user asks, "What is the weather in Delhi in Fahrenheit?", the agent may call a weather API and then use a calculator to convert Celsius to Fahrenheit.

![An agent uses the LLM to choose tools - for example weather API then a calculator before replying in Fahrenheit](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session35/session35-05-agent-tools.png)

Tools can include:

- Gmail.
- Slack.
- Google Drive.
- Google Sheets.
- Calculator.
- Database.
- Company APIs.

LangChain reduces the code needed to connect these tools into an AI workflow.

---

## LangChain Core vs Community vs Provider Packages

LangChain has different packages. Knowing the package names helps when reading imports and debugging errors.

| Package | What it contains | Simple meaning |
| --- | --- | --- |
| **`langchain-core`** | Runnables, LCEL, PromptTemplate, output parsers | Main building blocks |
| **`langchain-community`** | Community integrations such as vector stores and loaders | Optional integrations |
| **Provider packages** | Model-specific connectors like `langchain-ollama`, `langchain-groq`, `langchain-openai` | LLM provider connectors |

For this session's minimal demo, the important packages are:

```bash
pip install langchain-core langchain-ollama
```

You do not need to install every LangChain package at the beginning.

Install only what your project needs.

---

## PromptTemplate

Prompts should not be scattered as hard-coded strings in many files.

LangChain provides **PromptTemplate** to make prompts reusable.

- **Official Definition:** A **PromptTemplate** is a prompt blueprint with placeholders that are filled at runtime.
- **In Simple Words:** It is like a sentence with blanks.
- **Real-Life Example:** A school form has fixed labels, but each student's name, class, and roll number are different.

![Hard-coded prompts fix one string in code; PromptTemplate fills variables at runtime like a reusable blueprint](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session35/session35-07-prompt-template.png)

### Hard-Coded Prompt

```text
Explain REST APIs to beginner students in simple words.
```

This prompt is fixed.

If you want to explain another topic or change the audience, you must edit the full string.

### Templated Prompt

```text
Explain {topic} to {audience} with these requirements:
- Use {tone} tone
- Give one real-life analogy
- Keep the answer within {limit} words
```

Here, only the variables change:

- `{topic}`
- `{audience}`
- `{tone}`
- `{limit}`

The same template can explain REST APIs, SQL indexes, vector databases, or any other topic.

This is useful because values can come from user input, a web form, or backend API data.

---

## LCEL and the Pipe Operator

- **Official Definition:** **LCEL** means **LangChain Expression Language**. It lets you connect runnables using the pipe operator `|`.
- **In Simple Words:** The pipe operator connects steps from left to right.
- **Real-Life Example:** In a food counter, order slip -> cook -> server. Each person receives output from the previous step.

In LangChain, a simple LCEL chain looks like this:

```python
chain = prompt | llm | output_parser
```

This means:

1. `prompt` prepares the final prompt.
2. `llm` sends it to the model.
3. `output_parser` cleans the model output.

![LCEL chain flow with LangChain and Ollama - input dictionary through prompt template, ChatOllama at localhost:11434, StrOutputParser to plain string](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session36/session36-02-lcel-chain-flow.png)

You do not manually write separate glue logic for every step.

The pipe declares the order clearly.

---

## Output Parsers

Models may return rich response objects.

Your application usually needs only clean text.

- **Official Definition:** An **output parser** converts raw model output into a clean and predictable format.
- **In Simple Words:** It extracts the useful answer from the full response.
- **Real-Life Example:** When a food delivery arrives, you eat the food, not the bag, bill, and packaging.

### StrOutputParser

- **Official Definition:** **StrOutputParser** returns the model's text content as a Python string.
- **In Simple Words:** It makes the final output easier to print, store, or send to a UI.

| Without parser | With `StrOutputParser` |
| --- | --- |
| You may receive a response object with metadata | You receive a plain string |
| You manually read `.content` | The chain returns final text directly |
| More glue code | Cleaner chain output |

![Without StrOutputParser, invoke returns a full response object with metadata; with StrOutputParser, the chain returns a plain answer string ready for your UI](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module3/session35/session35-10-app1-vs-app2.png)

---

## Ollama Setup and Common Commands

The demo used a local Ollama model.

Before running the LangChain program, Ollama must be installed and the required model should be available locally.

Important commands:

```bash
ollama list
```

This shows the models already available on your system.

```bash
ollama pull qwen2.5:0.5b
```

This downloads the model if it is not already present.

```bash
ollama run qwen2.5:0.5b
```

This starts the model for local interaction.

```bash
ollama rm qwen2.5:0.5b
```

This removes a local model if needed.

### Python Packages Used

```bash
pip install langchain-core
pip install langchain-ollama
```

If your system uses `pip3`, use:

```bash
pip3 install langchain-core
pip3 install langchain-ollama
```

Common setup issues:

- Ollama is not running.
- The model name in code does not match `ollama list`.
- Required Python package is not installed.
- VS Code interpreter is not refreshed after package installation.
- The local model output may behave differently depending on model settings and environment.

---

## Step 1 - Raw Ollama Call

This is the baseline approach.

It calls Ollama directly without LangChain.

**File: `raw_ollama.py`**

```python
from ollama import chat  # Import the local Ollama chat helper

user_question = "Explain REST APIs to beginner students in simple words."  # Store one fixed prompt

response = chat(  # Send the prompt to the local Ollama model
    model="qwen2.5:0.5b",  # Use the model name available in ollama list
    messages=[{"role": "user", "content": user_question}],  # Send one user message
)  # End the Ollama chat call

answer = response["message"]["content"]  # Extract only the assistant answer text
print(answer)  # Print the answer in the terminal
```

### How the code works

- `chat()` sends the prompt to Ollama.
- `model` must match the model installed locally.
- `messages` follows chat format.
- The prompt is hard-coded.
- You manually extract the answer from the response.

---

## Step 2 - PromptTemplate With ChatOllama

Now the prompt becomes reusable.

The model is called through LangChain's Ollama integration.

**File: `template_only.py`**

```python
from langchain_core.prompts import PromptTemplate  # Import PromptTemplate from LangChain Core
from langchain_ollama import ChatOllama  # Import the Ollama chat model wrapper

llm = ChatOllama(  # Create a LangChain runnable for the local Ollama model
    model="qwen2.5:0.5b",  # Use the local model tag
    base_url="http://localhost:11434",  # Use the default Ollama local server URL
    temperature=0.3,  # Keep the answer focused for learning
)  # End model configuration

prompt_template = PromptTemplate.from_template(  # Create a reusable prompt template
    """Explain {topic} to {audience} with these requirements:
- Use {tone} tone
- Give one real-life analogy
- Keep the answer within {limit} words"""
)  # End template creation

final_prompt = prompt_template.format(  # Fill the template variables
    topic="REST APIs",  # Fill the topic placeholder
    audience="beginners",  # Fill the audience placeholder
    tone="simple",  # Fill the tone placeholder
    limit="150",  # Fill the word-limit placeholder
)  # End prompt formatting

response = llm.invoke(final_prompt)  # Send the final prompt to the model
print(response.content)  # Print only the text content from the response object
```

### How the code works

- `PromptTemplate.from_template()` creates the reusable template.
- `.format()` fills `{topic}`, `{audience}`, `{tone}`, and `{limit}`.
- `ChatOllama` connects LangChain to the local Ollama server.
- `invoke()` runs the model once.
- `.content` gives the answer text from the model response.

---

## Step 3 - First LCEL Chain

This is the main chain pattern demonstrated in the session.

It connects prompt, model, and parser in one flow.

**File: `first_chain.py`**

```python
from langchain_ollama import ChatOllama  # Import the Ollama model wrapper for LangChain
from langchain_core.prompts import PromptTemplate  # Import reusable prompt template support
from langchain_core.output_parsers import StrOutputParser  # Import parser for plain string output

llm = ChatOllama(  # Create the LLM runnable
    model="qwen2.5:0.5b",  # Use the local Ollama model tag
    base_url="http://localhost:11434",  # Connect to local Ollama server
    temperature=0.3,  # Keep output stable for classroom demo
)  # End LLM setup

prompt = PromptTemplate.from_template(  # Create the reusable prompt template
    """Explain {topic} to {audience} with these requirements:
- Use {tone} tone
- Give one real-life analogy
- Keep the answer within {limit} words"""
)  # End prompt template setup

output_parser = StrOutputParser()  # Create the parser that returns a plain string

chain = prompt | llm | output_parser  # Connect prompt, model, and parser using LCEL pipe

result = chain.invoke({  # Run the full chain with input values
    "topic": "REST APIs",  # Fill the topic variable
    "audience": "beginners",  # Fill the audience variable
    "tone": "simple",  # Fill the tone variable
    "limit": "150",  # Fill the limit variable
})  # End chain input

print(result)  # Print the final plain string output
```

### How the code works

- `prompt | llm | output_parser` declares the order.
- The input dictionary keys must match the template placeholders.
- The prompt step fills the variables.
- The LLM step generates the answer.
- The parser step returns clean string output.
- The final `result` is directly printable.

---

## Raw Ollama vs LangChain Chain

The output may look similar in a small example.

The difference becomes important when the app grows.

| Situation | Raw Ollama | LangChain |
| --- | --- | --- |
| One static prompt | Simple enough | Also simple |
| Reusable prompts | Manual string handling | `PromptTemplate` |
| Multi-step workflow | Manual glue code | Chain with pipe operator |
| Output formatting | Manual extraction | `StrOutputParser` |
| Provider switching | More code changes | Change provider wrapper/config |
| Future memory/tools/RAG | Build manually | Add LangChain components |

LangChain is not valuable only because it reduces a few lines today.

It is valuable because it gives a structure that can grow when you add retrieval, tools, memory, or agents.

---

## Real-World Example: Support Chatbot

The session also discussed a support-chatbot style example similar to what food-delivery apps use.

Such a chatbot may handle:

- Refund status.
- Wrong payment.
- Missing item.
- Order issue.
- User complaint classification.

In this type of application, LangChain can help connect:

- The user question.
- Prompt templates.
- LLM reasoning.
- Tool calls.
- Output formatting.
- Future memory or retrieval.

The main idea is that developers do not need to memorize every internal LangChain function.

They should understand the building blocks and use documentation or AI-assisted coding tools to apply the right function when needed.

---

## Key Takeaways

- **LangChain** is a framework for building structured LLM applications using reusable components.
- Raw LLM calls are fine for small demos, but bigger apps need prompts, chains, tools, memory, retrievers, and output parsing.
- LangChain sits between the model provider and your application logic as an orchestration layer.
- A **Runnable** takes input and returns output; a **chain** connects multiple runnables in order.
- This session's main practical flow was **PromptTemplate -> ChatOllama -> StrOutputParser** using LCEL pipe syntax.

In the next hands-on work, the same chain idea can be expanded with tools, memory, retrieval, and agents.

---

## Important Commands, Libraries, and Terminologies Used

| Term / command | Meaning |
| --- | --- |
| **LangChain** | Framework for composing LLM applications from reusable parts |
| **Framework** | Reusable structure that reduces repeated code |
| **Runnable** | Component that takes input, performs work, and returns output |
| **Chain** | Ordered sequence where one step feeds the next |
| **LCEL** | LangChain Expression Language for connecting runnables |
| **Pipe operator `|`** | Connects steps from left to right |
| **PromptTemplate** | Reusable prompt with placeholders |
| **ChatOllama** | LangChain wrapper for Ollama chat models |
| **StrOutputParser** | Converts model response into plain string output |
| **Agent** | LLM-driven component that can choose actions or tools |
| **Tool** | External action such as API, calculator, Gmail, or Slack |
| **Memory** | Stores useful conversation context |
| **Retriever** | Fetches relevant document chunks for RAG |
| **LangChain Core** | Package with PromptTemplate, LCEL, runnables, output parsers |
| **LangChain Community** | Package with community integrations like vector stores and loaders |
| **Provider package** | Package for a model provider, such as `langchain-ollama` |
| `pip install langchain-core` | Install LangChain core building blocks |
| `pip install langchain-ollama` | Install Ollama integration for LangChain |
| `ollama list` | See locally available Ollama models |
| `ollama pull qwen2.5:0.5b` | Download the model locally |
| `ollama run qwen2.5:0.5b` | Run the model through Ollama |
| `PromptTemplate.from_template()` | Create a reusable prompt template |
| `chain.invoke({...})` | Run a chain once with input values |
