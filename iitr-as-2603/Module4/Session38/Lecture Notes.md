# Hands-On: Agentic RAG

## Exact Difference — Static RAG vs Agentic RAG

Before any code, lock this one idea:

| | **Static RAG** (what you built earlier) | **Agentic RAG** (today) |
|---|---|---|
| **One-line meaning** | Always **retrieve once**, then **generate** | Agent **decides** when/what to retrieve, then generate |
| **Who controls search?** | Your **fixed Python** path | The **agent loop** (may call a retrieve **tool**) |
| **How many searches?** | Usually **exactly one** per question | **Zero, one, or many** (multi-hop) |
| **Query used** | Mostly the **raw** user text | Often a **rewritten** search query |
| **Stop rule** | After that single retrieve | **Enough facts**, **max hops**, or empty hits |
| **Real-life picture** | Photocopier that **always** prints the same first pages | Cook who **tastes the dal** and opens the masala box only if needed |

**Same ShopEasy question:** *"Phone last week — can I return it, and is express free above 499?"*

- **Static:** one top-k search on the raw question → paste context → **Groq** answers — may miss shipping if returns ranked higher.
- **Agentic:** rewrite → retrieve returns → reason *"shipping still missing?"* → retrieve shipping → **stop** → **Groq** answers from both.

**In Simple Words:** Static RAG is a **fixed recipe**. Agentic RAG is a **smart assistant** who chooses shelves, may visit a second shelf, and knows when to stop.

![Static RAG always retrieves once on a fixed path versus Agentic RAG where the agent decides when to search, may multi-hop across policy folders, then generate with Groq](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module4/session38/session38-01-static-vs-agentic-rag.png)

**Setup for this lab (Groq):**

```bash
pip install groq
export GROQ_API_KEY="your_key_here"
```

Keep the key in the environment (or Colab Secrets) — never hard-code it in the file.

---

## Context of This Session

In **earlier RAG work** you built **static RAG**: chunk ShopEasy policies, **embed**, store in **Chroma**, **top-k** retrieve once, assemble context, generate with Ollama or **Groq**. In the **previous** session you added **guardrails** (injection, allow-lists, output checks). Retrieval still ran when **your code** said so.

Today you build **agentic RAG** on **Groq**: rewrite queries, treat retrieve as a **tool**, run **retrieve → reason → retrieve**, and compare answers to the static baseline.

**What you will learn:**

- State the **exact** static vs agentic difference (table above)
- **Rewrite** queries before search
- Call retrieval as a **tool** zero or more times
- Run a multi-hop loop with **stop conditions**
- Generate final answers with the **Groq API** and compare quality to one-shot RAG

---

## What You Already Built — Normal (Static) RAG

Straight road from earlier labs:

**ingest / chunk → embed → Chroma → always retrieve top-k → paste context → generate**

- **Official Definition:** **Static RAG** = fixed **retrieve-then-generate**; code always retrieves once, then the LLM answers.
- **Real-Life Example (library):** Always pull the **top three books** — even for *"Hi"* or when a **second shelf** is needed.
- **Real-Life Example (hospital):** Always open the **same FAQ binder** once — never walk to **billing** for a follow-up.

| Static RAG did well | It could not decide |
|---|---|
| Ground answers in ShopEasy docs | Skip search for greetings |
| Embeddings + Chroma semantic hit | Rewrite Hindi-English chat first |
| Clear top-k → context → generate | Two reasoned hops (returns then shipping) |

**Connecting idea:** Static RAG taught **how** to search. Agentic RAG teaches **when** to search, **what** next, and **when to stop** — then Groq writes the answer.

**More pictures:** ShopEasy sticky-note vs two folders · Passport pamphlets vs KYC-only rulebook · Zomato raw chat vs rewritten *"delivery delay refund"*.

### Activity — Label the pipeline

Write **Static** or **Agentic**: (1) always `retrieve` then `generate` · (2) model chooses `retrieve` then `final` · (3) "Hi" with **no** search.

---

## Groq Helper — Shared by Both Pipelines

Both static and agentic paths end with the **same** Groq call. Only the **context** they build is different.

```python
# groq_helper.py — one place to call Groq for grounded answers

import os  # Read secrets from environment
from groq import Groq  # Official Groq Python client

# Create the client once — key must be in GROQ_API_KEY
client = Groq(api_key=os.environ["GROQ_API_KEY"])

SYSTEM = (
    # Grounding rules — answer only from context
    "You are ShopEasy support. Use ONLY the context. "
    "If the answer is not in context, say you could not find it. "
    "Do not invent policy numbers."
)


def groq_answer(context, question):
    # Build user message with clear context delimiters
    user_msg = (
        "=== CONTEXT START ===\n"
        + context
        + "\n=== CONTEXT END ===\n\nQuestion: "
        + question
    )
    # Call Groq chat completions (same pattern as earlier labs)
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",  # Fast, strong model on Groq
        messages=[
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": user_msg},
        ],
        temperature=0,  # Stable support answers
    )
    # Return only the assistant text
    return response.choices[0].message.content
```

**How the code works:**

- **`GROQ_API_KEY`** in env only; both pipelines call the same **`groq_answer`** after building context.

---

## Recap — Static RAG Baseline (with Groq)

Tiny keyword corpus + **one** retrieve + **Groq** generate — your baseline.

```python
# static_rag_baseline.py — one retrieve, then Groq answer (no agent decisions)

from groq_helper import groq_answer  # Shared Groq generate step

CORPUS = {
    # Tiny ShopEasy knowledge base — filename maps to policy text
    "returns.txt": "ShopEasy returns: unused items within 30 days of delivery. Open box OK if tags attached. No returns on gift cards.",
    "shipping.txt": "ShopEasy shipping: Standard 5-7 days. Express 2 days in metro cities. Free shipping above Rs 499.",
    "warranty.txt": "ShopEasy warranty: Electronics 12 months from invoice. Physical damage not covered. Claim via My Orders.",
}


def keyword_retrieve(query, top_k=2):
    # Score each doc by how many query words appear in the text
    words = set(query.lower().split())
    scored = []
    for name, text in CORPUS.items():
        score = sum(1 for w in words if w in text.lower())
        scored.append((score, name, text))
    scored.sort(reverse=True)
    return [(n, t) for s, n, t in scored[:top_k] if s > 0]


def static_rag_answer(user_question):
    # Always retrieve once — even if the question needs two hops
    hits = keyword_retrieve(user_question, top_k=2)
    context = "\n".join([f"[{n}] {t}" for n, t in hits]) or "No docs found."
    # Generate with Groq using only that one-shot context
    answer = groq_answer(context, user_question)
    return {"answer": answer, "sources": [n for n, _ in hits], "hops": 1}


if __name__ == "__main__":
    q = "I got a phone last week. Can I return it and is express shipping free?"
    print(static_rag_answer(q))
```

**How the code works:**

- **`keyword_retrieve`** ranks docs by word overlap — enough to see pipeline behaviour.
- **`static_rag_answer`** always retrieves **once**, then calls **`groq_answer`** — classic static RAG.
- Multi-topic questions may still miss a file because there is **no second hop**.

---

## Query Rewrite — Improve Hit Quality Before Search

Bad search starts with a **messy question**. Agentic systems often **rewrite** the user text into a short, searchable query.

- **Official Definition:** **Query rewrite** (or query expansion) transforms a user utterance into one or more search strings optimised for retrieval.
- **In Simple Words:** Turn chai-stall chat into a **library catalogue** search phrase.
- **Real-Life Example:** User says *"Woh phone wapas kar sakte hain kya, kal aaya tha"* → rewrite to *"return window electronics delivery date"*.
- **Real-Life Example:** At a **medical store**, the customer says *"woh bukhar wali dawai"* — the pharmacist translates that into the **shelf label** before searching, instead of scanning every box for the casual phrase.

![Query rewrite turns casual Hindi-English chat into a short searchable policy phrase before retrieval, like a pharmacist matching shelf labels](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module4/session38/session38-02-query-rewrite.png)

| User question | Stronger rewritten query |
|---|---|
| *"Can I still send it back?"* | return policy unused items days |
| *"Kitne din mein aayega?"* | standard shipping delivery days |

- **Common doubt:** Rewrite does **not** invent facts — only changes **how you search**. Keep queries **short** (5–12 words).

### Simple rewrite helper

```python
# query_rewrite.py — turn casual questions into search-friendly phrases

REWRITE_HINTS = {
    # Map casual words to policy vocabulary used in CORPUS
    "send it back": "return unused items days",
    "wapas": "return policy",
    "kitne din": "shipping delivery days",
    "covered": "warranty electronics months",
    "free delivery": "free shipping above",
}


def rewrite_query(user_question):
    # Start from the original question in lowercase
    q = user_question.lower().strip()
    # Apply known phrase swaps when present
    for casual, formal in REWRITE_HINTS.items():
        if casual in q:
            q = q.replace(casual, formal)
    # Drop filler words that hurt keyword search
    fillers = {"please", "yaar", "can", "i", "still", "the", "a", "an", "kya"}
    tokens = [t for t in q.replace("?", " ").split() if t not in fillers]
    # Keep a short searchable string
    return " ".join(tokens[:12]) or user_question


if __name__ == "__main__":
    print(rewrite_query("Yaar can I still send it back please?"))
    # Expected idea: something like "return unused items days"
```

**How the code works:**

- **`REWRITE_HINTS`** maps casual Hindi/English phrases to corpus words.
- **`rewrite_query`** drops fillers and caps length; an LLM can do the same job later.

### Activity — Rewrite three questions

Rewrite each into a **short English search query** (max 10 words): *"Mera parcel late hai, express free milega kya?"* · *"Phone screen cracked — warranty?"* · *"Gift card return chahiye."*

---

## Retrieval as a Tool — The Agent Chooses When to Search

In **tool-calling** agents, retrieval is just another tool — like a calculator or policy lookup. The model can call it **zero times** (already knows), **once**, or **several times**.

- **Official Definition:** **Retrieval-as-a-tool** = search as a function the agent may call during reasoning (not a fixed pre-step).
- **In Simple Words:** A **"Search policies"** button — press only when needed (doorbell, not automatic door).
- **Real-Life Example:** Bank officer opens KYC rules for KYC — not for "Hello".

| Calls | When | Example |
|---|---|---|
| **0** | Greeting / thanks | *"Hi ShopEasy"* |
| **1** | Single topic | Standard shipping days |
| **2+** | Multi-hop | Return **and** warranty |

- **Common mistake:** Invented tool names — allow-list `retrieve_policies` only.

![Retrieval exposed as a tool the agent presses like a doorbell — zero calls for greetings, one for single topics, multiple for multi-hop policy search](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module4/session38/session38-03-retrieval-as-tool.png)

### Wiring retrieve as a callable tool

```python
# retrieve_tool.py — retrieval exposed like a function the agent can call

from static_rag_baseline import CORPUS, keyword_retrieve
from query_rewrite import rewrite_query

ALLOWED_TOOLS = {"retrieve_policies"}  # Guardrail habit: allow-list


def retrieve_policies(query, top_k=2):
    # Tool body — rewrite, then search the corpus
    search_q = rewrite_query(query)
    hits = keyword_retrieve(search_q, top_k=top_k)
    # Return structured data the agent can read
    return {
        "rewritten_query": search_q,
        "results": [{"source": n, "text": t} for n, t in hits],
    }


def run_tool(tool_name, **kwargs):
    # Only allow listed tools — blocks random or unsafe calls
    if tool_name not in ALLOWED_TOOLS:
        return {"error": "TOOL_BLOCKED"}
    if tool_name == "retrieve_policies":
        return retrieve_policies(**kwargs)
    return {"error": "TOOL_BLOCKED"}


if __name__ == "__main__":
    print(run_tool("retrieve_policies", query="return window unused items"))
    print(run_tool("delete_all_files"))  # Should be blocked
```

**How the code works:**

- **`retrieve_policies`** = rewrite + search; **`run_tool`** allow-lists calls (unknown → `TOOL_BLOCKED`).

---

## Iterative Retrieve → Reason → Retrieve

**Multi-hop** = look, think, look again with a **new** query until you can answer — or must stop.

- **Official Definition:** Each retrieve is guided by intermediate reasoning, not only the original question.
- **In Simple Words:** Find A, realise you need B, search B, then answer.
- **Real-Life Example:** **IRCTC** — confirm train date, then seat type. **CBSE** — Book 1 definition, then Book 2 example (not one blind top-k grab).

**Loop:** question → retrieve (rewritten) → reason *"enough?"* → maybe new retrieve → **stop** → **Groq** final answer.

![Multi-hop agentic RAG loop retrieve then reason then retrieve again with stop conditions before the final Groq grounded answer](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module4/session38/session38-04-multi-hop-stop-loop.png)

| Hop | Example query | Learn |
|---|---|---|
| 1 | `return unused items 30 days` | Return rules |
| 2 | `warranty electronics 12 months` | Warranty limits |

- **Common mistake:** Same query every hop, or one mega-query that confuses ranking.

### Activity — Plan two hops

*"Bought a mixer last month, motor failed, can I return or claim warranty?"* — write Hop-1 query, expected fact, Hop-2 query, expected fact.

---

## Stop Conditions — When the Agent Must Quit Searching

- **Official Definition:** A rule that ends the retrieve–reason loop (final answer or safe refusal).
- **In Simple Words:** School bell / **UPI** retry limit / **traffic signal** — without it, hops never end.

| Stop | Beginner setting |
|---|---|
| **Enough evidence** | Both needed topics found |
| **Max hops** | `MAX_HOPS = 3` |
| **Empty results** | Stop and say unknown |
| **Greeting** | Final reply, zero retrieve |

If hop 3 still lacks facts → grounded **"I could not find…"** (do not invent).

## Build the Agentic RAG Loop

This is the heart of the hands-on: a small controller that **rewrites**, **retrieves as a tool**, **reasons**, and **stops**.

```python
# agentic_rag.py — retrieve as a tool + multi-hop loop + Groq final answer

from retrieve_tool import run_tool  # Allow-listed retrieve tool
from groq_helper import groq_answer  # Shared Groq generate step

MAX_HOPS = 3  # Hard stop — never retrieve more than this many times


def needs_more_info(question, memory):
    # Very simple "reason" step: check if key topics appear in gathered text
    blob = " ".join(memory).lower()
    q = question.lower()
    needs_return = any(w in q for w in ["return", "wapas", "send it back"])
    needs_ship = any(w in q for w in ["shipping", "express", "delivery", "din"])
    needs_warranty = any(w in q for w in ["warranty", "guarantee", "covered"])
    if needs_return and "return" not in blob and "30 days" not in blob:
        return True, "return unused items days"
    if needs_ship and "shipping" not in blob and "5-7" not in blob:
        return True, "standard express shipping days free"
    if needs_warranty and "warranty" not in blob and "12 months" not in blob:
        return True, "warranty electronics months invoice"
    return False, ""


def agentic_rag(user_question):
    # Working memory stores texts returned by the retrieve tool
    memory = []
    sources = []
    hops = 0
    # First decision: greetings skip retrieval — no Groq policy call needed
    if user_question.strip().lower() in {"hi", "hello", "thanks", "thank you"}:
        return {"answer": "Hello! How can ShopEasy help?", "sources": [], "hops": 0}

    next_query = user_question
    while hops < MAX_HOPS:
        # Call retrieval as a tool (may be hop 1, 2, or 3)
        tool_out = run_tool("retrieve_policies", query=next_query, top_k=2)
        hops += 1
        for row in tool_out.get("results", []):
            memory.append(row["text"])
            sources.append(row["source"])
        # Reason: do we need another hop with a new query?
        more, follow_up = needs_more_info(user_question, memory)
        if not more:
            break  # Stop condition: enough evidence
        if not tool_out.get("results"):
            break  # Stop condition: empty retrieve — do not spin
        next_query = follow_up  # Different query for next hop

    context = "\n".join(memory) if memory else "No policy text found."
    # Final generate with Groq — same helper as static RAG
    answer = groq_answer(context, user_question)
    return {
        "answer": answer,
        "hops": hops,
        "sources": list(dict.fromkeys(sources)),
    }


if __name__ == "__main__":
    hard = "I got a phone last week. Can I return it and is express shipping free?"
    print(agentic_rag(hard))
    print(agentic_rag("Hi"))
```

**How the code works:**

- Loop may retrieve **0–MAX_HOPS** times; **`needs_more_info`** proposes the next query.
- Final step always uses **`groq_answer`** — fair comparison with static RAG on the **same Groq model**.

---

## Compare Quality — One-Shot Baseline vs Agentic Loop

Hands-on means you **measure**. Run the **same questions** on **static RAG + Groq** and **agentic RAG + Groq** — same model, different retrieve behaviour.

### Mini eval set (use these four)

| ID | Question | Why it is useful |
|---|---|---|
| Q1 | `"Hi"` | Agentic should **skip** retrieve; static still searches |
| Q2 | `"How long is standard shipping?"` | Both should find shipping — similar quality |
| Q3 | `"Can I return an unused phone after 10 days?"` | One clear topic — rewrite helps both |
| Q4 | `"Return window for phone and is express free above 499?"` | **Multi-hop** — agentic should pull returns + shipping |

### What to record

In your notebook, make columns: Question | Static sources | Agentic hops | Agentic sources | Winner | Why — fill one row each for Q1–Q4.

- **Scoring tip:** On Q4, prefer answers citing **both** policies without inventing numbers.

---

## Putting It Together — ShopEasy Decision Card

Use this card whenever you design a support bot:

| Situation | Prefer |
|---|---|
| Fixed FAQ, clear keywords (like your earlier Chroma mini-app) | **Normal / static RAG** |
| Casual / Hindi-mixed questions | **Query rewrite** then retrieve |
| Greetings and chit-chat | **No retrieve** (agent decides zero tools) |
| Two policies in one question | **Multi-hop** with max hops |
| Still missing facts after max hops | **Unknown-fact** style refusal |

### Live demo flow

1. **Exact difference** (static = one retrieve; agentic = decide + hops)  
2. Confirm `GROQ_API_KEY`; show `groq_helper.py`  
3. **Static** on Q4 — sources + Groq answer  
4. **Agentic** on Q4 — hops + both sources + Groq answer  
5. Both on `"Hi"` — static searches; agentic skips  

### When something breaks

| Symptom | Fix |
|---|---|
| Same docs every hop | Change follow-up query |
| Loop never ends | `MAX_HOPS` + break on empty |
| Greeting still retrieves | Early final path |
| Groq auth error | Check `GROQ_API_KEY` in env |
| Tool name hallucinated | `run_tool` + allow-list |

---

## Key Takeaways

- **Exact difference:** Static RAG **always retrieves once** then generates; Agentic RAG **decides** when/what to retrieve (0+ hops) then generates.
- Both labs finish with the **same Groq API** helper — compare **retrieve behaviour**, not model brand.
- **Query rewrite**, **retrieve-as-tool**, and **stop conditions** make RAG agentic.

These patterns extend your earlier RAG and tool work. **Next** topics deepen agent orchestration.

---

## Important Commands, Libraries, and Terminologies

| Term | Type | Meaning |
|---|---|---|
| **Static / normal RAG** | Concept | Fixed retrieve-once-then-generate (earlier Chroma labs) |
| **Agentic RAG** | Concept | Agent decides when/what to retrieve, with rewrite + hops |
| **Groq API** | Service | Cloud LLM used for grounded final answers in this lab |
| **`GROQ_API_KEY`** | Config | Environment secret for Groq — never hard-code |
| **`groq_answer`** | Function | Shared generate step for static and agentic paths |
| **`llama-3.3-70b-versatile`** | Model | Groq chat model used in demos |
| **Query rewrite** | Concept | Turn user chat into a better search string |
| **Retrieval-as-a-tool** | Concept | Search exposed as a callable function |
| **Multi-hop retrieve** | Concept | Multiple searches guided by intermediate reasoning |
| **Stop condition** | Concept | Rule that ends the retrieve–reason loop |
| **`CORPUS`** | Code | Mini ShopEasy policy dictionary |
| **`keyword_retrieve`** | Function | Rank docs by word overlap for the lab |
| **`rewrite_query`** | Function | Clean and map casual phrases to policy words |
| **`retrieve_policies`** | Tool | Allow-listed retrieval tool |
| **`run_tool`** | Function | Safe dispatcher — blocks unknown tools |
| **`MAX_HOPS`** | Constant | Hard cap on retrieve calls |
| **`needs_more_info`** | Function | Reason step proposing next query |
| **`agentic_rag`** | Function | Iterative loop with stops + Groq |
| **`static_rag_answer`** | Function | One-shot baseline + Groq |
