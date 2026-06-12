# Assignment Subjective

Total Questions: 1  
Difficulty: Medium  
Type: Practical Implementation

---

## Q1 (Practical, Medium)

A coding institute's **student helpdesk** wants one assistant that can (1) search **official course rules** and (2) check **support ticket status** — and remember a ticket ID across turns. Your task is to build a small **integrated LangChain agent** in a **single Python file**.

### Policy and ticket data to use

Embed these three policies as inline `Document` objects (include `metadata={"source": "<filename>"}`):

| `source` metadata | `page_content` (use exactly) |
|---|---|
| `refund_policy.md` | `Refund policy: Full refund within 7 days of enrollment if no live class attended. Partial refund within 30 days per program rules.` |
| `attendance_policy.md` | `Attendance policy: Minimum 75% attendance is required for certification and placement support.` |
| `batch_change_policy.md` | `Batch change policy: Students may request one batch change per cohort. Missing more than three classes without approved leave may delay batch change.` |

Use this **fake ticket database** inside your `@tool` function:

```python
FAKE_TICKET_DATABASE = {
    "TKT-2001": "Refund request under review. Expected response in 2 working days.",
    "TKT-2002": "Batch change request approved. New batch starts next Monday.",
}
```

### Problem Statement

Create **`course_support_agent.py`** that:

1. **Ingests** the three policies into Chroma:
   - `RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=60)`
   - `OpenAIEmbeddings(model="text-embedding-3-small")`
   - Collection name: `helpdesk_policy_docs`
2. Builds **`course_policy_tool`** with `create_retriever_tool` (`similarity`, `k=2`) and a clear description mentioning **refund, attendance, and batch change** rules.
3. Defines **`get_ticket_status(ticket_id: str)`** with `@tool` and a docstring that says when to use it for ticket / refund-request status.
4. Creates a **tool-calling agent** with:
   - `MessagesPlaceholder` for **`chat_history`** (`optional=True`) and **`agent_scratchpad`**
   - System rules: use policy tool for policy questions; ticket tool for ticket IDs; refuse politely on out-of-domain topics
   - `AgentExecutor(..., verbose=True, max_iterations=3)`
5. Implements **`ask_agent(user_query: str) -> str`** that invokes the executor, then **appends** `HumanMessage` and `AIMessage` to `chat_history`.
6. In `main()`, run these **four** labelled prints (same `chat_history` list across turns 3 and 4):

| Label | User message | Expected behaviour |
|---|---|---|
| **Demo A** | `What is the refund policy in the first week?` | Calls `course_policy_tool`; answer mentions **7 days** / refund |
| **Demo B** | `What is the status of ticket TKT-2001?` | Calls `get_ticket_status`; mentions **review** or **working days** |
| **Demo C (turn 1)** | `My support ticket is TKT-2002.` | Acknowledges or records context |
| **Demo C (turn 2)** | `What is the status of it?` | Uses memory + calls `get_ticket_status`; mentions **batch change** or **Monday** |
| **Demo D** | `Who won IPL 2025?` | Polite refusal — no invented sports answer |

Set `OPENAI_API_KEY` in your environment before running:

```bash
python3 course_support_agent.py
```

### Expected Outcome

- **Demo A:** Policy retrieval path; grounded refund wording.  
- **Demo B:** Ticket tool path; no policy search required.  
- **Demo C:** Two-turn memory — turn 2 resolves **TKT-2002** without the user repeating the ID.  
- **Demo D:** Out-of-domain refusal within course-support scope.  
- Terminal `verbose=True` output should show which tools fired.

### Submission Instruction

- code all the points mentioned in VS Code in a single `.py` file (`course_support_agent.py`)
- run the code and verify it is working
- then submit the code in the code editor / answer box in the LMS

---

## Answer Explanation (Complete Ideal Solution)

### Step-by-step Walkthrough

1. Define three `Document` objects with the given `page_content` and `metadata["source"]`.  
2. Split → embed → `Chroma.from_documents(..., collection_name="helpdesk_policy_docs")`.  
3. `retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 2})`.  
4. `course_policy_tool = create_retriever_tool(retriever, name="course_policy_tool", description=...)`.  
5. `@tool get_ticket_status` reads from `FAKE_TICKET_DATABASE`.  
6. Build prompt with `chat_history` + `agent_scratchpad` placeholders and routing system message.  
7. `create_tool_calling_agent` + `AgentExecutor` with `max_iterations=3`.  
8. `ask_agent` invokes, appends messages, returns `response["output"]`.  
9. Run Demo A → B → C (two turns) → D in `main()`.

### Reference — `course_support_agent.py`

```python
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.tools import tool
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain.tools.retriever import create_retriever_tool
from langchain_classic.agents import AgentExecutor, create_tool_calling_agent

RAW_DOCUMENTS = [
    Document(
        page_content=(
            "Refund policy: Full refund within 7 days of enrollment if no live class attended. "
            "Partial refund within 30 days per program rules."
        ),
        metadata={"source": "refund_policy.md"},
    ),
    Document(
        page_content=(
            "Attendance policy: Minimum 75% attendance is required for certification and placement support."
        ),
        metadata={"source": "attendance_policy.md"},
    ),
    Document(
        page_content=(
            "Batch change policy: Students may request one batch change per cohort. "
            "Missing more than three classes without approved leave may delay batch change."
        ),
        metadata={"source": "batch_change_policy.md"},
    ),
]

splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=60)
split_docs = splitter.split_documents(RAW_DOCUMENTS)

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
vectorstore = Chroma.from_documents(
    documents=split_docs,
    embedding=embeddings,
    collection_name="helpdesk_policy_docs",
)

retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 2},
)

course_policy_tool = create_retriever_tool(
    retriever=retriever,
    name="course_policy_tool",
    description=(
        "Searches official course policy documents for refund rules, attendance requirements, "
        "and batch change policy. Use when the user asks about program rules or policies."
    ),
)

FAKE_TICKET_DATABASE = {
    "TKT-2001": "Refund request under review. Expected response in 2 working days.",
    "TKT-2002": "Batch change request approved. New batch starts next Monday.",
}

@tool
def get_ticket_status(ticket_id: str) -> str:
    """Returns support ticket status for the given ticket ID.

    Use when the user asks about ticket status, refund request status,
    or support ticket progress for a specific ticket ID.
    """
    status = FAKE_TICKET_DATABASE.get(ticket_id)
    if not status:
        return f"Ticket status not found for ticket ID {ticket_id}."
    return status

tools = [course_policy_tool, get_ticket_status]

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        (
            "You are a helpful course support assistant. "
            "Use course_policy_tool for official policy questions. "
            "Use get_ticket_status when a ticket ID or ticket status is needed. "
            "Use chat history to resolve follow-ups like 'status of it'. "
            "If the question is outside course policies and support tickets, refuse politely. "
            "When answering from documents, mention available policy documents."
        ),
    ),
    MessagesPlaceholder(variable_name="chat_history", optional=True),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

agent = create_tool_calling_agent(llm=llm, tools=tools, prompt=prompt)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    max_iterations=3,
)

chat_history = []

def ask_agent(user_query: str) -> str:
    response = agent_executor.invoke({
        "input": user_query,
        "chat_history": chat_history,
    })
    answer = response["output"]
    chat_history.append(HumanMessage(content=user_query))
    chat_history.append(AIMessage(content=answer))
    return answer

def main():
    print("Demo A")
    print("User:", "What is the refund policy in the first week?")
    print("AI:", ask_agent("What is the refund policy in the first week?"))
    print()

    print("Demo B")
    print("User:", "What is the status of ticket TKT-2001?")
    print("AI:", ask_agent("What is the status of ticket TKT-2001?"))
    print()

    print("Demo C (turn 1)")
    print("User:", "My support ticket is TKT-2002.")
    print("AI:", ask_agent("My support ticket is TKT-2002."))
    print()

    print("Demo C (turn 2)")
    print("User:", "What is the status of it?")
    print("AI:", ask_agent("What is the status of it?"))
    print()

    print("Demo D")
    print("User:", "Who won IPL 2025?")
    print("AI:", ask_agent("Who won IPL 2025?"))

if __name__ == "__main__":
    main()
```

### Alternative Valid Approaches

- Add a minimal `EVAL_CASES` list and loop (bonus — not required for full credit if demos pass).  
- Use `persist_directory` for Chroma if you want reuse across runs (optional).  
- Strengthen the system prompt with explicit *"do not use outside knowledge for IPL questions"* if refusal is inconsistent.

### Common Mistakes to Avoid

- Forgetting to append `chat_history` → Demo C turn 2 fails.  
- Vague `course_policy_tool` description → ticket questions trigger retrieval.  
- Missing `agent_scratchpad` placeholder → unreliable tool loop.  
- Running Demo D before clearing history is fine; refusal should still work, but memory from prior turns may add noise — acceptable for this assignment.
