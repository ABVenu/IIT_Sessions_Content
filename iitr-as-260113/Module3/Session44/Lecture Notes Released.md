# Hands-On Real-World Use Cases

## Context of This Session

In the **previous** class you learned how to **debug** LangChain agents systematically. You grouped failures into **failure classes**, applied **prompt patches**, **tool patches**, and **retrieval tuning**, and used an **evaluation harness** to see what broke before you shipped.

That was the *quality loop*. Today's class applies the same LangChain stack to a **real enterprise pattern** — and builds one full application end to end: an **HR onboarding assistant**.

You will first see how agents look in **finance** and **content** domains, then design and **implement** the HR agent with **policy search**, **employee lookup**, and **training recommendations**. You will run a **live demo**, learn how to read **tool and AI messages** in the trace, and connect the HR agent to the **evaluation harness** you already know.

**In this session, you will:**

- Recognise the **enterprise agent pattern** shared across finance, HR, and content workflows
- **Contrast** how data sources, tools, memory, retrieval, and guardrails differ by domain
- **Design** an HR onboarding architecture with corpus, tools, escalation, and evidence
- **Implement** `hr_onboarding_agent.py` using **InMemoryVectorStore** and three **@tool** functions
- **Demonstrate** the agent on in-domain queries and plan **out-of-corpus** refusal behaviour
- **Extend** the agent with **eval JSON test cases** and **human-in-the-loop** feedback

---

## Why Real-World Use Cases Matter

- **Official Definition:** A **use-case pattern** is a repeatable blueprint for building an agent around a business problem — what data it reads, what tools it calls, and what rules it must never break.
- **In Simple Words:** You are not learning "agents in theory" — you are learning **templates** you can copy for HR, finance, or marketing teams.
- **Real-Life Example:** When you join a new company, an HR coordinator walks you through **documents**, **benefits**, **leave rules**, and **mandatory trainings**. An **HR onboarding assistant** automates that guided tour — with policy proof, not guesswork.

This module ends with a **revision-style capstone**: most building blocks (RAG, tools, agents, memory, evaluation) were introduced earlier. Today you **recombine** them on a fresh, practical example so you are ready for **multi-agent frameworks** and **no-code automation** in the upcoming module.

---

## The Enterprise Agent Pattern

Before writing code, every production-grade company agent follows a similar journey:

```
User business question
    → Agent understands intent
    → Retrieves policies / business context (RAG)
    → Calls tools (email, leave apply, laptop allocate, payment, etc.)
    → Validates answer against rules
    → Replies with final answer + evidence (citations) + next steps
```

- **Official Definition:** An **enterprise agent** is an AI workflow deployed inside a company (not just a demo) that must follow **business rules**, use **approved data sources**, and leave an **audit trail**.
- **In Simple Words:** The agent is a **trained office assistant** — it cannot invent company policy any more than a new intern can.
- **Real-Life Example:** At **TCS** or **Infosys**, approving **travel reimbursement** without reading the policy document would be a **compliance disaster**. The agent must **retrieve the policy first**, then act.

| Step | What happens | Why it matters |
|---|---|---|
| **Intent** | Agent figures out what the employee is asking | Wrong intent → wrong tool |
| **RAG retrieval** | Policy chunks pulled from vector database | Grounded answers, fewer hallucinations |
| **Tool calls** | External actions — assign training, fetch profile | Agents *do* things, not only chat |
| **Rule validation** | Answer must match policy boundaries | Prevents random approvals |
| **Evidence + next steps** | Cite document ID; suggest what to do next | Trust and usability |

- **Common mistake:** Returning the **entire policy PDF text** to the user. The tool may fetch ten pages; the **AI message** should summarise in plain language and attach **source IDs**.
- **Citation habit:** Phrases like *"As per HR Policy 002 (Leave Policy)…"* mirror how legal and HR teams expect answers in email.

---

## Finance Use Case Pattern

Finance is a high-stakes domain for agents because **money** and **tax compliance** are involved.

- **Official Definition:** A **finance agent** automates policy-bound workflows such as reimbursement approval, GST filing support, invoice generation, or vendor payment validation.
- **In Simple Words:** The agent is a **strict accounts officer** — it checks the rulebook before signing anything.
- **Real-Life Example:** You claim **Wi-Fi reimbursement** after a **personal vacation**. A careless agent that approves without checking travel dates creates a **fraud risk**.

**Typical finance agent capabilities discussed in class:**

| Capability | Example tool / step |
|---|---|
| **Policy-bound approve/reject** | Read reimbursement policy before yes/no |
| **GST / tax automation** | Monthly GST payment reminders and calculations |
| **Invoice generation** | Create vendor invoices from structured data |
| **Vendor payment validation** | Match PO, invoice, and bank details |
| **Employee grade lookup** | Fresher vs senior may have different limits |
| **Amount calculation** | Compute reimbursement after grade + policy rules |

**Operational guardrails in finance:**

- Never approve or reject **randomly** — every decision must trace to **policy text**.
- **Employee grade** and **employment status** often change the limit (fresher vs senior).
- Wrong approval on personal travel is called out in class as a **blunder** — design refusal and audit logs accordingly.

- **Common doubt:** *"Can one agent handle all finance tasks?"* In practice you start with **one workflow** (e.g. reimbursement) and expand tools later — same pattern as HR onboarding today.

---

## Content Creation Use Case Pattern

- **Official Definition:** A **content-creation agent** schedules and drafts posts (LinkedIn, YouTube, Twitter, Facebook) from prompts or topic lists.
- **In Simple Words:** You give a **topic list** and posting schedule; the agent drafts and uploads so your **consistency** does not depend on your mood that day.
- **Real-Life Example:** A creator wants a LinkedIn post every morning at 9 AM on **Agentic AI** topics. The agent reads the prompt, drafts the post, and publishes — like a **social media intern with a calendar**.

**Typical content workflow:**

| Piece | Role |
|---|---|
| **Prompt / topic list** | What to write about |
| **Scheduler** | When to publish |
| **Platform API tools** | Upload to LinkedIn, YouTube, etc. |
| **Brand guardrails** | Tone, length, forbidden words |

- **Reason it is simpler than HR/finance:** Content agents rarely need **personal employee data** or **legal policy citations** — but they still need **brand rules** so posts do not go off-message.
- **Common mistake:** Fully automated posting **without human review** on sensitive topics — many teams add an **approval step** before publish.

---

## Contrasting Finance, HR, and Content Workflows

The three examples share the **same enterprise skeleton** (intent → retrieve → tool → validate → respond) but differ in **data**, **risk**, and **guardrails**.

| Dimension | Finance (reimbursement / tax) | HR onboarding | Content creation |
|---|---|---|---|
| **Primary data sources** | Reimbursement policy, tax rules, employee grade DB, invoices | HR policy PDFs, employee profile, training catalog | Topic list, brand guidelines, past posts |
| **Retrieval needs** | High — every approval must cite policy | High — leave, benefits, relocation limits | Low–medium — style examples, not legal corpus |
| **Typical tools** | `get_employee_grade`, `calculate_reimbursement`, `approve_payment` | `search_hr_policy`, `get_employee_profile`, `get_mandatory_trainings` | `draft_post`, `schedule_upload`, `fetch_analytics` |
| **Memory** | Session context for claim under review; audit log persisted | Multi-turn onboarding Q&A; optional chat history | Editorial calendar state; draft versions |
| **Operational guardrails** | No random approve/reject; amount caps by grade | Never invent policy; escalate if evidence missing | Brand tone; no plagiarised or offensive content |
| **Evidence style** | Policy clause + calculation steps | Policy ID + section + citation | Source links / draft diff (optional) |
| **Failure cost** | Financial loss, compliance breach | Wrong benefits info, legal exposure | Reputation damage |

- **Connecting idea:** HR onboarding sits in the **middle** — more structured than content, less legally intense than tax automation, but still needs **grounded policy answers** and **personalization** via employee profile tools.
- **Activity — Match the domain:** For each need, write **Finance**, **HR**, or **Content**.

  1. Verify relocation bonus up to ₹50,000 against policy  
  2. Auto-post a Twitter thread every Friday at 6 PM  
  3. Reject a mobile bill reimbursement if amount exceeds fresher cap  

  **Suggested answers:** 1 → HR, 2 → Content, 3 → Finance

---

## HR Onboarding Assistant — Problem Statement

When you join a new company, you face many questions:

- What **documents** do I submit before day one? (Aadhaar, PAN, bank details, NDA)
- What is the **leave policy**?
- What **benefits and insurance** apply?
- Which **mandatory trainings** must I complete?
- How do I get my **laptop** and set it up?

An **HR onboarding assistant** is an agent that answers these questions using **company policy documents** and can **trigger actions** (assign trainings, send calendar invites) through tools.

- **Official Definition:** **HR onboarding** is the process of integrating a new employee — paperwork, orientation, systems access, and policy awareness.
- **In Simple Words:** Everything HR explains in your **first week**, packaged into a chat assistant.
- **Real-Life Example:** Instead of emailing HR for *"How many paid leaves do full-time employees get?"*, you ask the agent — it searches **Leave Policy**, cites **HR Policy 002**, and answers **24 paid leaves** with portal instructions.

**Why vector database here:** Policies live in documents (PDFs, Word files, or text). The agent cannot memorize all pages. **RAG** stores embeddings so the right policy chunk surfaces per question — same pattern you used for course support agents.

---

## HR Onboarding Architecture

Design before code. The class architecture has five pillars:

| Pillar | Implementation in this project |
|---|---|
| **Corpus** | Sample HR policy `Document` objects (pre-joining, leave, trainings, benefits) |
| **Vector store** | `InMemoryVectorStore` + `text-embedding-3-small` |
| **Retriever** | `as_retriever(search_kwargs={"k": 3})` — top 3 similar chunks |
| **Tools** | Policy search, employee profile, mandatory trainings |
| **Agent + system prompt** | `create_agent` with role, tool rules, evidence format, escalation |

### Escalation When Evidence Is Missing

The system prompt includes a critical guardrail:

- **Never invent a policy.**
- If **evidence is not found**, say **HR confirmation is required** (human assistance).
- Always include **evidence** (source IDs), **actions taken** (which tool ran), and **escalation / next steps** when needed.

- **Official Definition:** **Escalation** is handing a question to a human expert when the automated system lacks grounded information.
- **In Simple Words:** The agent says *"I don't have this in our policy documents — please check with HR"* instead of making up an answer.
- **Real-Life Example:** At a **hospital help desk**, if your test report is not in the system, the receptionist does not guess your diagnosis — they call the lab.

### Answer Format Taught in Class

Each final response should be structured as:

1. **Answer** — concise, professional  
2. **Evidence** — policy document name / ID  
3. **Actions taken** — e.g. *"Searched HR policy document for full-time employees"*  
4. **Escalation / next steps** — only when the query needs human follow-up  

- **Common mistake:** Returning the raw **tool message** (full policy paragraph) to the end user. Extract the polished **AI message** content instead.

---

## Project Setup — Extending the LangChain App Folder

The instructor continues in the existing **LangChain apps** repository rather than creating a new repo — same pattern as earlier RAG and agent exercises.

**Folder mental map from class:**

| Folder / file area | Purpose |
|---|---|
| LangChain RAG files | Ingest and retrieve documents |
| Memory files | Chat history patterns |
| Automation / stateless agent files | Prior agent examples |
| **`hr_onboarding_agent.py`** | Today's full HR agent |

**Install dependencies (if not already present):**

```bash
pip install langchain langchain-core langchain-openai openai
```

Set your API key before running:

```bash
export OPENAI_API_KEY="your-key-here"
```

---

## InMemoryVectorStore vs Chroma

Earlier classes used **Chroma** as the vector database. Today introduces **InMemoryVectorStore** from LangChain.

- **Official Definition:** **InMemoryVectorStore** keeps embeddings in **RAM** for the running Python process — no separate database server.
- **In Simple Words:** Policies sit in your laptop's **short-term memory** while the script runs — fast for labs, not for huge production corpora.
- **Real-Life Example:** A **pop-up stall menu** written on a whiteboard (in-memory) vs a **library catalog** (Chroma) that supports advanced filters and persists after closing.

| Feature | InMemoryVectorStore | Chroma |
|---|---|---|
| **Persistence** | Lost when process ends | Saved to disk |
| **Setup** | ~2 lines of code | Collection + path config |
| **Metadata filters** | More limited | Richer filter queries |
| **Best for** | Demos, small policy sets | Production RAG |

- **Common doubt:** *"Do I still need to embed the query manually?"* **No** — `retriever.invoke(query)` embeds the query internally, then runs similarity search.
- **Production note:** Large companies switch to Chroma, Pinecone, or similar when policy count and filter needs grow.

---

## Full Code — `hr_onboarding_agent.py`

Save this file in your LangChain apps folder. Every line has a comment so you can map it to the live walkthrough.

```python
# hr_onboarding_agent.py — HR onboarding assistant with RAG + tools
# Requires: pip install langchain langchain-core langchain-openai openai
# Set: export OPENAI_API_KEY="your-key"

import os  # Read environment variables (API key)

from langchain_core.documents import Document  # Wrap policy text + metadata
from langchain_core.tools import tool  # Decorator to expose functions as agent tools
from langchain_core.vectorstores import InMemoryVectorStore  # In-RAM vector database
from langchain_openai import OpenAIEmbeddings, ChatOpenAI  # Embeddings + chat model
from langchain.agents import create_agent  # High-level agent builder used in class


# ── Step 1: HR policy corpus (sample documents) ──────────────────────────────

HR_DOCUMENTS = [
    Document(
        page_content=(
            "Before day one, every new employee must complete identity verification, "
            "submit bank account details, sign the non-disclosure agreement (NDA), "
            "and provide emergency contact details."
        ),
        metadata={"source": "HR_POLICY_001", "section": "pre_joining_formalities"},
    ),
    Document(
        page_content=(
            "Full-time employees receive 24 paid leaves per calendar year. "
            "Leave requests must be submitted via the HR portal at least 3 working days in advance. "
            "Unused leaves may be carried forward up to 5 days subject to manager approval."
        ),
        metadata={"source": "HR_POLICY_002", "section": "leave_policy"},
    ),
    Document(
        page_content=(
            "All new joiners must complete security awareness, code of conduct, "
            "data privacy, and anti-harassment training within the first 14 days."
        ),
        metadata={"source": "HR_POLICY_003", "section": "mandatory_trainings"},
    ),
    Document(
        page_content=(
            "Employees are eligible for health insurance from day one. "
            "Relocation bonus up to INR 50,000 is available for eligible relocations "
            "with valid invoices submitted within 30 days of joining."
        ),
        metadata={"source": "HR_POLICY_004", "section": "benefits_and_insurance"},
    ),
    Document(
        page_content=(
            "Laptop allocation happens on joining day. IT setup guide is shared by email. "
            "Remote employees receive equipment via courier within 5 business days."
        ),
        metadata={"source": "HR_POLICY_005", "section": "equipment_setup"},
    ),
]


# ── Step 2: Sample employee database ───────────────────────────────────────

EMPLOYEES = {
    "E101": {
        "employee_id": "E101",
        "name": "Anita Sharma",
        "role": "backend_engineer",
        "location": "Bangalore",
        "work_mode": "hybrid",
    },
    "E102": {
        "employee_id": "E102",
        "name": "Rohit Mehta",
        "role": "product_manager",
        "location": "Mumbai",
        "work_mode": "remote",
    },
}


# ── Step 3: Embedding model + vector store + retriever ───────────────────────

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")  # OpenAI embedding model from class

vector_store = InMemoryVectorStore(embedding=embeddings)  # Create in-memory store with embeddings
vector_store.add_documents(HR_DOCUMENTS)  # Embed and store all HR policy chunks

retriever = vector_store.as_retriever(
    search_type="similarity",  # Standard cosine-style similarity search
    search_kwargs={"k": 3},  # Return top 3 matching policy chunks per query
)


# ── Step 4: Tool 1 — search HR policies ────────────────────────────────────

@tool
def search_hr_policy(query: str) -> str:
    """Search HR policy documents and return relevant chunks for the user query.

    Use this tool when the user asks about onboarding, leave policy, reimbursement,
    benefits, insurance, mandatory trainings, pre-joining formalities, or equipment setup.
    """
    docs = retriever.invoke(query)  # Embed query internally + similarity search

    if not docs:  # No matching policy found
        return f"No relevant policy document found for query: {query}"

    results = []  # Collect formatted strings — one per retrieved document
    for doc in docs:
        source = doc.metadata.get("source", "unknown")  # Default if metadata missing
        section = doc.metadata.get("section", "unknown")
        content = doc.page_content  # Actual policy text chunk
        block = f"Source: {source} | Section: {section} | Content: {content}"
        results.append(block)

    return "\n---\n".join(results)  # Join all hits with a visible separator


# ── Step 5: Tool 2 — get employee profile ────────────────────────────────────

@tool
def get_employee_profile(employee_id: str) -> dict:
    """Fetch employee information from the database for the given employee ID.

    Use this tool when the answer needs personalization (role, location, work mode).
    Returns a JSON-friendly dict with found=True/False and message or employee fields.
    """
    employee = EMPLOYEES.get(employee_id)  # Lookup in sample dict

    if not employee:
        return {
            "found": False,
            "message": f"Employee with ID {employee_id} not found in the database.",
        }

    return {
        "found": True,
        "message": "Employee record found.",
        **employee,  # Unpack employee fields into the response dict
    }


# ── Step 6: Tool 3 — mandatory training recommendations ──────────────────────

COMMON_TRAININGS = [
    "security_awareness",
    "code_of_conduct",
    "data_privacy",
    "anti_harassment",
]

ROLE_SPECIFIC_TRAININGS = {
    "backend_engineer": ["python_fundamentals", "fastapi", "agentic_ai"],
    "product_manager": ["client_interaction", "client_data_handling"],
}


@tool
def get_mandatory_trainings(role: str) -> dict:
    """Return mandatory training recommendations for a new employee based on their role.

    Common trainings apply to every employee. Role-specific trainings depend on job family.
    """
    role_key = role.strip().lower().replace(" ", "_")  # Normalize role string
    role_trainings = ROLE_SPECIFIC_TRAININGS.get(role_key, [])  # Empty list if role unknown

    return {
        "common_trainings": COMMON_TRAININGS,
        "role_specific_trainings": role_trainings,
        "all_mandatory": COMMON_TRAININGS + role_trainings,
    }


# ── Step 7: System prompt — role, guardrails, answer format ──────────────────

SYSTEM_PROMPT = """
You are an HR onboarding assistant for a company.

Help new employees understand onboarding steps, leave policy, benefits, equipment, and trainings.

Rules:
- Use search_hr_policy whenever the answer depends on company policy.
- Use get_employee_profile when the answer needs personalization.
- Use get_mandatory_trainings when the user asks about required trainings for a role.
- Never invent a policy. If evidence is not found, say that HR confirmation is required.
- Always include evidence (source IDs), actions taken, and escalation/next steps when needed.
- Keep answers clear, professional, and concise.
"""


# ── Step 8: LLM model + agent creation ───────────────────────────────────────

model = ChatOpenAI(model="gpt-4o-mini", temperature=0)  # Low temperature for policy answers

tools = [
    search_hr_policy,
    get_employee_profile,
    get_mandatory_trainings,
]

agent = create_agent(
    model=model,  # Chat model the agent reasons with
    tools=tools,  # List of @tool functions exposed to the agent
    system_prompt=SYSTEM_PROMPT,  # Fixed instructions sent with every query
)


# ── Step 9: Invoke helper — run agent and return final text ───────────────────

def ask_agent(user_query: str) -> str:
    """Invoke the agent for a user query and return the final assistant message content."""
    result = agent.invoke(
        {"messages": [{"role": "user", "content": user_query}]}  # Message list format from class
    )
    last_message = result["messages"][-1]  # Final AI message in the trace
    return last_message.content  # String shown to the end user


# ── Step 10: Demo execution ───────────────────────────────────────────────────

if __name__ == "__main__":
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("Set OPENAI_API_KEY in your environment before running.")

    # In-domain query demonstrated live in class
    query = "How many paid leaves does a full-time employee receive?"
    answer = ask_agent(query)
    print("User:", query)
    print("Assistant:", answer)
```

**How the code works:**

- **`HR_DOCUMENTS`** — five policy chunks with `source` and `section` metadata for citations.
- **`InMemoryVectorStore.add_documents`** — embeds and stores all chunks in one call.
- **`retriever` with `k=3`** — returns the three most semantically similar policies per question.
- **`search_hr_policy`** — formats each hit as `Source | Section | Content` instead of raw objects.
- **`get_employee_profile`** — returns structured **`found`** status so the agent can branch cleanly.
- **`get_mandatory_trainings`** — merges **common** trainings with **role-specific** lists.
- **`SYSTEM_PROMPT`** — encodes escalation (*HR confirmation required*) and evidence rules.
- **`ask_agent`** — reads `result["messages"][-1].content` to avoid dumping the full trace.

- **Common mistake:** Forgetting `export OPENAI_API_KEY` — the live demo failed first run for this reason.
- **Optional upgrade:** Swap `InMemoryVectorStore` for **Chroma** when you need persistence and metadata filters (`where` clauses).

---

## Reading the Agent Trace — Human, Tool, and AI Messages

When you print the raw `agent.invoke` result, you see multiple **message types**:

| Message type | Who created it | What it contains |
|---|---|---|
| **HumanMessage** | User / your test query | The employee's question |
| **ToolMessage** | Tool execution | Raw policy chunk from `search_hr_policy` |
| **AIMessage** | LLM | Polished answer for the user |

**Live demo walkthrough (leave query):**

1. User asks: *"How many paid leaves does a full-time employee get?"*
2. Agent calls **`search_hr_policy`** → **ToolMessage** shows **HR_POLICY_002** leave text (*24 paid leaves*).
3. **AIMessage** summarises: *"As per company leave policy, full-time employees receive 24 paid leaves…"* plus evidence and action lines.

- **Official Definition:** A **trajectory** is the ordered list of messages and tool calls from input to final output.
- **In Simple Words:** The **receipt** showing every step the agent took — not only the final bill amount.
- **Real-Life Example:** **Swiggy** order tracking shows *restaurant accepted → rider picked up → delivered* — not only *"food arrived."*

### Extracting Only the Final Answer

Two options taught in class:

1. **`result["messages"][-1].content`** — take the last message's text (used in `ask_agent` above).
2. **String output parser** — LangChain helper to parse LLM output when chains grow longer.

- **Common doubt:** *"Does the system prompt waste context window?"* **Yes, it uses tokens every turn** — but it is **mandatory** so every answer follows HR rules. You cannot skip it to save tokens.

---

## Live Demo — In-Domain Query

The instructor executed:

```bash
python3 hr_onboarding_agent.py
```

**Expected behaviour for the leave question:**

| Check | Expected |
|---|---|
| Tool called | `search_hr_policy` |
| Evidence | **HR_POLICY_002** / leave section |
| Answer fact | **24 paid leaves** for full-time employees |
| Extra detail | Submit via **HR portal** |

- **In-domain** means the question is answerable from the **HR corpus** you loaded.
- The first run failed without **`OPENAI_API_KEY`** — always export the key in the same terminal session.

### Activity — Predict the Tool

Without running code, predict which tool(s) the agent should call:

1. *"What trainings must a backend engineer complete?"*  
2. *"What is employee E101's work mode?"*  
3. *"What is the CEO's personal email?"*

**Suggested answers:**

1. `get_mandatory_trainings` (and possibly `search_hr_policy` for policy backup)  
2. `get_employee_profile` with `E101`  
3. No HR policy covers this → **refuse** or **escalate to HR** — do not invent an email

---

## Out-of-Corpus Queries and Refusal Paths

An **out-of-corpus** question cannot be answered from loaded HR policies — e.g. *"What is the weather in Delhi?"* or *"Book me a flight to Goa."*

- **Official Definition:** **Out-of-corpus** (out-of-domain) means the query falls outside the knowledge and tools the agent was designed for.
- **In Simple Words:** The employee asked HR about something HR's filing cabinet does not contain.
- **Real-Life Example:** Asking the **passport office** for restaurant recommendations — wrong desk, polite refusal.

**Expected agent behaviour:**

| Query type | Should refuse? | Should invent facts? |
|---|---|---|
| Valid leave policy question | No | No |
| Random unrelated question | Yes | No |
| Partially related but no evidence | Escalate to HR | No |

The evaluation harness checks **`should_refuse`** flags — if the agent answers a forbidden question confidently, the test **fails**.

### Activity — Write Two Test Queries

Create one **in-domain** and one **out-of-corpus** query for your HR agent. For each, note:

- Expected tool(s)  
- Whether `should_refuse` is `true` or `false`  
- One keyword the answer must contain (if not refusing)

---

## Evaluation Harness for the HR Agent

You already built an **eval JSON + runner** pattern for a course support agent. The same harness extends to HR — add new rows, keep the same field names.

- **Official Definition:** An **evaluation harness** runs scripted test cases against an agent and compares **tools used**, **documents cited**, **keywords**, and **refusal behaviour** to an answer key.
- **In Simple Words:** A **question paper with marking scheme** for your bot — graded automatically.
- **Real-Life Example:** **NEET** mock tests — same format every week so you can see if scores improved after revision.

**Each eval case includes:**

| Field | Purpose |
|---|---|
| **`id`** | Short name (`leave_policy_fulltime`) |
| **`input`** | User question string |
| **`must_use_tools`** | Tools the agent should call |
| **`forbidden_tools`** | Tools that must NOT run |
| **`must_cite_doc_ids`** | Policy sources that should appear |
| **`must_contain`** | Keywords in final answer (e.g. `"24"`) |
| **`should_refuse`** | `true` if agent must decline |

### Full Code — `hr_evaluation_cases.json`

```json
[
  {
    "id": "leave_policy_fulltime",
    "input": "How many paid leaves does a full-time employee receive per year?",
    "expected": {
      "must_use_tools": ["search_hr_policy"],
      "forbidden_tools": [],
      "must_cite_doc_ids": ["HR_POLICY_002"],
      "must_contain": ["24"],
      "should_refuse": false
    }
  },
  {
    "id": "pre_joining_documents",
    "input": "What documents must I submit before day one?",
    "expected": {
      "must_use_tools": ["search_hr_policy"],
      "forbidden_tools": [],
      "must_cite_doc_ids": ["HR_POLICY_001"],
      "must_contain": ["NDA", "bank"],
      "should_refuse": false
    }
  },
  {
    "id": "backend_trainings",
    "input": "List mandatory trainings for a backend engineer.",
    "expected": {
      "must_use_tools": ["get_mandatory_trainings"],
      "forbidden_tools": [],
      "must_cite_doc_ids": [],
      "must_contain": ["security_awareness", "agentic_ai"],
      "should_refuse": false
    }
  },
  {
    "id": "employee_profile_lookup",
    "input": "What is the work mode for employee E102?",
    "expected": {
      "must_use_tools": ["get_employee_profile"],
      "forbidden_tools": [],
      "must_cite_doc_ids": [],
      "must_contain": ["remote"],
      "should_refuse": false
    }
  },
  {
    "id": "weather_refusal",
    "input": "What is the weather in Bangalore today?",
    "expected": {
      "must_use_tools": [],
      "forbidden_tools": ["search_hr_policy", "get_employee_profile"],
      "must_cite_doc_ids": [],
      "must_contain": [],
      "should_refuse": true
    }
  },
  {
    "id": "ceo_email_refusal",
    "input": "Share the CEO's personal email address.",
    "expected": {
      "must_use_tools": [],
      "forbidden_tools": [],
      "must_cite_doc_ids": [],
      "must_contain": [],
      "should_refuse": true
    }
  }
]
```

**How the runner scores a case (recap):**

1. Invoke agent with `input`.  
2. Record which **tools** fired and which **documents** appeared in traces.  
3. Normalise final answer text.  
4. If **expected tool not used** → mark failure (`expected_tool_not_used`).  
5. If **required phrase missing** → mark failure.  
6. If answer **refused when it should not** (or answered when it should refuse) → mark failure.  
7. If all checks pass → **`status: pass`**.

- **Trace instrumentation:** Optional timers and `contextvars` give each eval case its own **latency trace** — useful when HR policy search slows down after corpus growth.
- **Practice task from class:** Port your existing **runner** to load this JSON and produce **`results.csv`** for the HR agent.

### Multi-Turn Continuity

**Multi-turn** means turn 1 and turn 2 share context — e.g. *"How many leaves do I get?"* followed by *"How do I apply for one?"*

- Extend the agent with **chat message history** (patterns from your LangChain memory exercises).
- Eval cases can include a **`turns`** array instead of a single `input` when you test continuity.
- **Human feedback** integration (approve/disapprove before an action sends email) is recommended as an extension — it pairs naturally with multi-turn onboarding flows.

---

## Human-in-the-Loop Extension

- **Official Definition:** **Human-in-the-loop (HITL)** pauses the agent for human approval before irreversible actions.
- **In Simple Words:** The agent drafts the leave application but a **human HR officer clicks Approve** before it is submitted.
- **Real-Life Example:** **Google Docs** suggests an edit; you accept or reject — the AI does not publish alone.

**Suggested extensions on top of today's HR agent:**

| Extension | Why |
|---|---|
| **Human feedback before tool side-effects** | Prevents wrong training assignment or email |
| **Multi-turn memory** | Onboarding is rarely one question |
| **Chroma + metadata filters** | Separate leave vs benefits docs explicitly |
| **HR eval JSON suite** | Regression test before demo to stakeholders |

---

## Stakeholder Demo and Residual Risks

A **stakeholder demo** shows business value in five minutes: one **in-domain** win, one **polite refusal**, and honest **risks**.

**Suggested demo script:**

| Step | What to show |
|---|---|
| 1 | Ask leave policy question → grounded answer with **HR_POLICY_002** citation |
| 2 | Ask weather / CEO email → **refusal** or **HR escalation** — no hallucination |
| 3 | Show **eval CSV** with pass rate after your test suite |

**Residual risks to articulate (professional honesty):**

| Risk | Mitigation |
|---|---|
| **Hallucinated policy** if retrieval misses | Strong system prompt + `must_cite_doc_ids` in eval |
| **Verbose answers** with too much trace data | Return only `messages[-1].content` to users |
| **In-memory store** lost on restart | Move to Chroma for production |
| **No human approval** on actions | Add HITL before emails or HRIS writes |
| **Answer noise** even when facts are right | Tune prompts; model evaluation techniques in advanced modules |

- **Common mistake:** Demoing only the happy path. Stakeholders trust you more when you show a **clean refusal** on an invalid question.

---

## Module Checklist — What You Should Revise

This class is a **capstone revision** before module evaluation. Connect the dots:

| Building block | HR onboarding connection |
|---|---|
| **RAG / vector store** | `search_hr_policy` retrieves leave and benefits chunks |
| **Tools** | Employee profile + training lookup |
| **Agent + system prompt** | Role, evidence, escalation rules |
| **Evaluation harness** | JSON cases for tools, citations, refusal |
| **Debugging** | Read tool vs AI messages when answers look wrong |

- Revise **LangChain agent patterns**, **memory**, **RAG ingest**, and **eval runner** files in your repo.
- The upcoming module introduces **N8N**, **CrewAI**, **AutoGen**, and **multi-agent** workflows — less raw Python, more orchestration platforms.

---

## Key Takeaways

- **Enterprise agents** follow intent → **RAG** → **tools** → **rule validation** → **answer + evidence** — whether the domain is finance, HR, or content.
- **HR onboarding** combines **policy retrieval**, **personalized employee tools**, and **training recommendations** with strict **no-invention** and **HR escalation** guardrails.
- **`InMemoryVectorStore`** is ideal for labs; **Chroma** wins when you need persistence and richer metadata filters.
- **`@tool` descriptions** matter — they steer the LLM toward the right function, same as debugging **wrong tool selection** failures.
- Always extract the final **`AIMessage`** for users; use the full **message trace** for debugging and **eval harness** scoring.
- **Eval JSON** for HR should test **grounded answers**, **tool use**, **refusal paths**, and eventually **multi-turn** continuity before you demo to stakeholders.

---

## Important Commands, Libraries, and Terminologies

| Term / Command | Type | Meaning |
|---|---|---|
| **Enterprise agent** | Concept | Production company agent with rules, RAG, tools, evidence |
| **HR onboarding assistant** | Use case | Agent helping new employees with policies and setup |
| **Use-case pattern** | Concept | Repeatable blueprint for domain-specific agents |
| **RAG** | Concept | Retrieve relevant policy chunks before answering |
| **InMemoryVectorStore** | Class | LangChain vector DB stored in RAM for the process |
| **Chroma** | Database | Persistent vector store with richer filters |
| **`text-embedding-3-small`** | Model | OpenAI embedding model used in class |
| **`as_retriever(search_kwargs={"k": 3})`** | Method | Top-3 similarity search retriever |
| **`@tool`** | Decorator | Exposes a Python function as an agent tool |
| **`create_agent`** | Function | Builds LangChain agent with model, tools, system prompt |
| **`Document`** | Class | LangChain wrapper for `page_content` + `metadata` |
| **HumanMessage** | Object | User query in agent trace |
| **ToolMessage** | Object | Raw output from a tool call |
| **AIMessage** | Object | Final polished LLM reply |
| **Escalation** | Concept | Hand off to human HR when evidence is missing |
| **Evidence / citation** | Concept | Policy source ID supporting the answer |
| **In-domain query** | Concept | Question answerable from loaded HR corpus |
| **Out-of-corpus query** | Concept | Question outside agent scope — should refuse |
| **`should_refuse`** | Eval field | Whether test expects a decline response |
| **Evaluation harness** | System | JSON cases + runner + traces + results.csv |
| **Human-in-the-loop** | Concept | Human approval before irreversible actions |
| **`export OPENAI_API_KEY=...`** | Command | Set API key in terminal session |
| **`python3 hr_onboarding_agent.py`** | Command | Run HR onboarding demo |
| **`result["messages"][-1].content`** | Pattern | Extract final assistant text from trace |
| **Operational guardrail** | Concept | Business rule the agent must never break |
| **Trajectory** | Concept | Full message and tool path for one query |
