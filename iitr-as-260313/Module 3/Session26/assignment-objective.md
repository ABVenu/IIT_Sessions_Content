# Objective Assignment: Introduction to LangChain and First Chain

## Multiple Choice Questions (Single Correct)

### Q1. Easy

A college helpdesk chatbot starts with a simple LLM call. Later, the team wants it to use reusable prompts, read policy documents, remember some user context, and connect to tools. Which option best explains why a framework like LangChain becomes useful?

A. It replaces the LLM completely  
B. It gives reusable building blocks for connecting models, prompts, tools, memory, retrievers, and workflows  
C. It is only used for designing website buttons  
D. It removes the need to write any Python code  

**Correct Answer:** B

**Answer Explanation:**  
LangChain is useful because it provides reusable building blocks for LLM applications. It helps connect models, prompts, tools, memory, retrievers, and workflows in a structured way. Option A is wrong because LangChain does not replace the LLM. Option C is wrong because LangChain is not a website UI framework. Option D is wrong because LangChain is a code framework, so Python code is still written.

---

### Q2. Easy

In an AI product, the user interface sends a question to the backend. The backend then uses a framework to coordinate the prompt, LLM, output parser, and possible tools. Where does LangChain usually sit in this architecture?

A. Between the model provider and the application logic  
B. Inside the user's keyboard  
C. Only inside the frontend CSS file  
D. As a replacement for the operating system  

**Correct Answer:** A

**Answer Explanation:**  
LangChain usually sits between the model provider and the application logic. It coordinates prompts, LLMs, tools, retrievers, memory, and output parsing. Options B, C, and D are unrelated to LangChain's role in an AI application architecture.

---

### Q3. Easy

A learner writes the same prompt string in five different Python files. Later, they need to change the tone and word limit in all five places. Which LangChain component directly helps avoid this repeated prompt editing?

A. PromptTemplate  
B. Vector database  
C. Operating system scheduler  
D. HTML table  

**Correct Answer:** A

**Answer Explanation:**  
`PromptTemplate` allows developers to define a reusable prompt with placeholders like `{topic}`, `{audience}`, `{tone}`, and `{limit}`. This avoids copy-pasting and editing the same prompt across many files. A vector database is used for retrieval, and the other options are unrelated.

---

### Q4. Easy

Which statement best describes a Runnable in LangChain?

A. A component that takes input, performs work, and returns output  
B. A file that can only store images  
C. A command used only to delete Ollama models  
D. A frontend layout element  

**Correct Answer:** A

**Answer Explanation:**  
A Runnable is a unit of work that accepts input, performs an operation, and returns output. Prompt templates, LLM wrappers, and parsers can behave as runnable components. The other options do not describe the Runnable idea.

---

### Q5. Moderate

A developer creates this LangChain expression:

```python
chain = prompt | llm | output_parser
```

What does the pipe operator `|` represent here?

A. It connects the steps so the prompt output goes to the LLM, and the LLM output goes to the parser  
B. It deletes the prompt after every run  
C. It installs LangChain packages automatically  
D. It converts Python into JavaScript  

**Correct Answer:** A

**Answer Explanation:**  
In LCEL, the pipe operator connects runnables from left to right. The prompt prepares the input, the LLM generates a response, and the output parser cleans the response. It does not delete files, install packages, or convert programming languages.

---

### Q6. Moderate

A Python program calls a chat model using LangChain and gets a response object that contains text plus other metadata. The developer wants the final chain output to be a plain string ready for printing. Which component should be added at the end of the chain?

A. StrOutputParser  
B. Gmail tool  
C. N8N workflow button  
D. CSS parser  

**Correct Answer:** A

**Answer Explanation:**  
`StrOutputParser` extracts the model's text content and returns it as a plain Python string. This makes the final output easier to print, store, or send to a UI. Gmail tools, N8N, and CSS parsers are not used for this LangChain output-cleaning task.

---

## Multiple Select Questions (Multiple Correct)

### Q7. Moderate

A team is deciding whether to build a small AI assistant with raw LLM API calls or with LangChain. Which situations make LangChain more useful than a one-off raw API script?

A. The app needs reusable prompt templates  
B. The app needs a sequence like prompt -> LLM -> parser  
C. The app may later add retrieval, tools, or memory  
D. The app must avoid all Python code completely  

**Correct Answers:** A, B, C

**Answer Explanation:**  
LangChain is useful when prompts need to be reused, steps need to be connected into a chain, and future components like retrieval, tools, or memory may be added. Option D is wrong because LangChain is still used through code, commonly Python.

---

### Q8. Moderate

A learner is setting up a minimal LangChain + Ollama program using `PromptTemplate`, `ChatOllama`, and `StrOutputParser`. Which packages are directly relevant for this minimal flow?

A. `langchain-core`  
B. `langchain-ollama`  
C. `langchain-community` for every possible integration before writing any code  
D. A provider package that connects LangChain to the chosen model provider  

**Correct Answers:** A, B, D

**Answer Explanation:**  
`langchain-core` provides core building blocks such as `PromptTemplate`, LCEL, and output parsers. `langchain-ollama` is the provider package for Ollama. Option D is also correct because provider packages connect LangChain to specific model providers. Option C is wrong because installing every community integration is unnecessary for a minimal prompt -> model -> parser chain.

---

### Q9. Hard

A support chatbot is being designed for order issues. It may answer simple questions now, but later it may classify complaints, call APIs, remember previous user context, and retrieve policy documents. Which LangChain module-to-role mappings are correct?

A. Tools can represent external actions such as APIs or calculators  
B. Memory can store useful context across conversation turns  
C. Retrievers can fetch relevant document chunks for RAG-style answering  
D. PromptTemplate automatically stores long-term user memory by itself  

**Correct Answers:** A, B, C

**Answer Explanation:**  
Tools represent external actions such as APIs, calculators, Gmail, or Slack. Memory stores useful conversation context. Retrievers fetch relevant chunks from documents or vector stores. Option D is wrong because `PromptTemplate` formats prompts; it does not automatically store long-term user memory.

---

### Q10. Hard

A developer is comparing LangChain with building everything from scratch for a RAG-style AI app. Which statements are correct?

A. LangChain can be useful for generic or medium-complexity workflows where default components are enough  
B. Building from scratch may be better when the project needs deep control over chunking, embedding, retrieval ranking, and generation logic  
C. LangChain removes every need for developers to understand prompts, models, or parsers  
D. Raw API calls may be acceptable for a very small one-script demo  

**Correct Answers:** A, B, D

**Answer Explanation:**  
LangChain is useful for many generic or medium-complexity workflows because it provides reusable components. Building from scratch may be better when deeper customization is required. Raw API calls can be fine for a very small demo. Option C is wrong because developers still need to understand prompts, models, parsers, and workflow logic even when using LangChain.
