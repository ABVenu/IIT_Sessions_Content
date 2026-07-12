# Agent Communication Patterns

## Introduction

In the **previous** session you built a **multimodal pipeline**: speech → text → summary → speech, plus a simple **vision** step.

This session keeps the theme of **how agents communicate**. First, a short refresh of **planner–executor** handoffs. Then you build **MasaiMato**: a mini Zomato-style **MCP** restaurant where **Groq** (Ollama Cloud optional) reads the menu and places orders through MCP tools.

**What you will learn:**

- Refresh planner–executor, JSON handoffs, and stop conditions
- Explain MCP: host, client, server, tools
- Build **MasaiMato** and run an **AI + MCP ordering loop** with one cloud key (`GROQ_API_KEY`)

---

## Quick Refresh: Agent Communication

You already practised stop conditions, tool executors, and JSON outputs earlier. Here is the short picture again.

- **Official Definition:** A **planner–executor** pattern splits work into a planner that creates an ordered plan and an executor that performs one step at a time.
- **In Simple Words:** One role makes the checklist; another ticks items off.
- **Real-Life Example:** “2 Masala Dosa for Asha” → check menu → place order → share order id.

| Idea | Meaning | Example |
|---|---|---|
| Task decomposition | Split one goal into ordered subtasks | Check menu → place order |
| JSON message contract | Agreed inputs, outputs, errors | `{"status":"ok","order_id":"MM1001"}` |
| Stop condition | End when complete or blocked | Dish missing → blocked; order placed → complete |

![Planner writing structured kitchen tickets and executor completing one ticket at a time, showing agent communication handoffs for a food order](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module4/session52/session52-01-agent-communication-handoff.png)

```text
User goal → Planner plan → Executor step (JSON) → Executor step (JSON) → Complete / Blocked
```

That answers *how steps talk inside a task*. Next: *how an AI talks to a restaurant system in a standard way*.

---

## Why We Need MCP

Agents need outside systems: menus, orders, status. Without a standard, every AI app invents its own plugin for the same restaurant tools. That is the **N × M problem**.

| AI app | Get menu | Place order |
|---|---|---|
| WhatsApp food bot | custom plugin | custom plugin |
| Hostel chatbot | rewrite again | rewrite again |
| Cursor agent | rewrite again | rewrite again |

| Without MCP | With MCP |
|---|---|
| Rewrite menu/order plugins for every AI host | Write MasaiMato server once |
| Field rename breaks many wrappers | Hosts keep one tool contract |
| Hard to reuse tools | `list_tools` + `call_tool` work the same way |

![Messy custom plugins from many AI apps versus one MCP hub connecting cleanly to a single MasaiMato restaurant service](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module4/session52/session52-02-why-mcp-standard.png)

- **Official Definition:** **Model Context Protocol (MCP)** is an open standard for how AI apps connect to external tools and context.
- **In Simple Words:** USB-C for AI tools — one server, many clients.
- **Real-Life Example:** One MasaiMato kitchen ticket system that WhatsApp bots, campus chatbots, and IDE agents can all use.

**Common doubt:** “I already have a restaurant REST API.” Good — MCP can wrap it. The API serves your app; MCP helps many AI hosts reuse the same capability.

---

## MCP Roles and vs Traditional API

| Role | Meaning | Analogy |
|---|---|---|
| Host | AI app the user sees | Cursor / chat demo |
| Client | Connector inside the host | Adapter cable |
| Server | Exposes tools/data | MasaiMato restaurant service |

![Hungry student talking to a Host AI, with an MCP Client cable connecting to the MasaiMato MCP Server offering Get Menu and Place Order tools](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module4/session52/session52-03-mcp-roles-masaimato.png)

```text
Hungry student → Host AI → MCP Client ←→ MasaiMato MCP Server (get_menu / place_order)
```

| Point | Traditional API | MCP |
|---|---|---|
| Start | You already know the URL | Client discovers tools |
| Style | Many REST shapes | Shared tool call style |
| AI reuse | Custom integration per app | One server, many hosts |

```text
API:   your code → POST /orders → backend
MCP:   AI → list_tools() → call_tool("place_order", {...}) → MasaiMato
```

**Clarity:** MCP may wrap a REST API. It does not always replace it. The win is the **agent-facing** discovery + tool contract.

### Activity — API or MCP?

| Situation | Traditional API / MCP / Both |
|---|---|
| Browser loads menu from `/api/menu` | |
| AI lists MasaiMato tools and calls `place_order` | |
| MCP tool internally calls restaurant REST API | |

**Suggested answers:** Traditional API; MCP; Both.

An MCP server can expose **tools** (actions), **resources** (read-only data), and **prompts** (templates). This lab focuses on **tools**.

---

## MasaiMato App Goal

Build a mini food-ordering MCP app:

1. **Server tools:** `get_menu()`, `place_order(item_name, quantity, customer_name)`
2. **AI loop:** Groq reads a natural-language order request, calls those MCP tools, confirms with a real order id

```text
"Order 2 Masala Dosa for Asha"
   → Groq (+ tool schemas from MCP)
   → MCP call_tool
   → MasaiMato server
   → JSON result back to Groq
   → Final confirmation
```

**Provider rule:** Main notes use **Groq** + `GROQ_API_KEY` only. Optional later: Ollama Cloud with only `OLLAMA_API_KEY`.

---

## Setup

```bash
pip install fastmcp groq python-dotenv openai
```

Create `.env` (do not commit):

```bash
GROQ_API_KEY=your_groq_key_here
```

Create folder `masaimato_mcp/` with:

- `server.py` — MasaiMato MCP tools
- `ai_mcp_chat.py` — Groq + MCP ordering demo

Keep both files in the same folder so `from server import mcp` works.

---

## MasaiMato MCP Server

- **Official Definition:** An MCP **tool** is a server function with name, description, and input schema.
- **In Simple Words:** A labelled kitchen action the AI is allowed to press.
- **Real-Life Example:** Zomato-like “View menu” and “Place order” buttons.

### Full code — `server.py`

```python
# server.py — MasaiMato MCP restaurant server
from fastmcp import FastMCP  # MCP server helper

mcp = FastMCP(name="MasaiMato")  # Server name

MENU = {  # Dish -> price in INR
    "masala dosa": 80,
    "paneer butter masala": 180,
    "butter naan": 40,
    "veg biryani": 150,
    "filter coffee": 30,
}

ORDERS = {}  # order_id -> order details
NEXT_ID = 1001  # next order number


@mcp.tool
def get_menu() -> dict:
    """Return MasaiMato menu with dish names and prices."""
    items = [{"item_name": n, "price_inr": p} for n, p in MENU.items()]
    return {"status": "ok", "restaurant": "MasaiMato", "items": items}


@mcp.tool
def place_order(item_name: str, quantity: int, customer_name: str) -> dict:
    """Place one MasaiMato order and return order id + total."""
    global NEXT_ID
    key = item_name.strip().lower()
    if key not in MENU:
        return {
            "status": "error",
            "message": f"'{item_name}' not on menu. Call get_menu first.",
        }
    if quantity < 1:
        return {"status": "error", "message": "Quantity must be at least 1."}

    order_id = f"MM{NEXT_ID}"
    NEXT_ID += 1
    total = MENU[key] * quantity
    order = {
        "order_id": order_id,
        "item_name": key,
        "quantity": quantity,
        "customer_name": customer_name.strip(),
        "total_inr": total,
        "status": "preparing",
    }
    ORDERS[order_id] = order
    return {"status": "ok", "message": "Order placed on MasaiMato.", "order": order}


if __name__ == "__main__":
    mcp.run()  # stdio server for host apps
```

**How the code works:**

- `get_menu` returns dishes and prices
- `place_order` rejects unknown dishes, creates `MM1001`-style ids, stores the bill
- Docstrings become tool descriptions for the AI

**Quick check:** Predict `place_order("Pizza", 1, "Asha")` → should return `status: error`.

### Tiny smoke test (optional, no LLM key)

In a Python shell or short script inside `masaimato_mcp/`:

```python
import asyncio
from fastmcp import Client
from server import mcp

async def smoke():
    async with Client(mcp) as client:
        print(await client.list_tools())
        print((await client.call_tool("get_menu", {})).data)
        print((await client.call_tool(
            "place_order",
            {"item_name": "masala dosa", "quantity": 2, "customer_name": "Asha"},
        )).data)

asyncio.run(smoke())
```

Use this only if you want to prove MCP before wiring Groq.

---

## AI Orders Through MCP (Groq)

The AI is the waiter. MCP is the official ticket system to the kitchen. Your script runs only `call_tool`.

- **Official Definition:** An **AI + MCP tool loop** lets the model choose discovered tools; your program executes them and returns results for the final answer.
- **In Simple Words:** Chat thinks; MCP executes; answer stays grounded.
- **Real-Life Example:** Do not invent Masala Dosa prices — read MasaiMato menu first.

![AI food assistant taking a student order, reading the MasaiMato menu through MCP, and returning a real order confirmation with id MM1001](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module4/session52/session52-04-ai-orders-through-mcp.png)

### Full code — `ai_mcp_chat.py`

```python
# ai_mcp_chat.py — Groq orders food through MasaiMato MCP tools
import asyncio
import json
import os

from dotenv import load_dotenv
from fastmcp import Client
from groq import Groq
from server import mcp


def to_llm_tools(mcp_tools):
    """Convert MCP tools into Groq function schemas."""
    out = []
    for t in mcp_tools:
        out.append(
            {
                "type": "function",
                "function": {
                    "name": t.name,
                    "description": t.description or "",
                    "parameters": t.inputSchema or {"type": "object", "properties": {}},
                },
            }
        )
    return out


def result_text(result):
    """Turn MCP result into text for the model."""
    if result.data is not None:
        return json.dumps(result.data)
    return str(result.content)


async def ask_masaimato(question):
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("Set GROQ_API_KEY in your .env file.")

    llm = Groq(api_key=api_key)
    model = "llama-3.1-8b-instant"

    async with Client(mcp) as client:
        mcp_tools = await client.list_tools()
        print("=== MCP TOOLS ===")
        for t in mcp_tools:
            print(f"- {t.name}: {t.description}")

        tools = to_llm_tools(mcp_tools)
        messages = [
            {
                "role": "system",
                "content": (
                    "You are MasaiMato, a food ordering assistant. "
                    "Use MCP tools for menu and orders. "
                    "Do not invent dishes, prices, or order ids."
                ),
            },
            {"role": "user", "content": question},
        ]

        while True:
            resp = llm.chat.completions.create(
                model=model,
                messages=messages,
                tools=tools,
                tool_choice="auto",
                temperature=0,
            )
            msg = resp.choices[0].message

            if not msg.tool_calls:
                print("\n=== AI FINAL ANSWER ===")
                print(msg.content)
                return msg.content

            print("\n=== AI REQUESTED MCP TOOLS ===")
            messages.append(
                {
                    "role": "assistant",
                    "content": msg.content or "",
                    "tool_calls": [
                        {
                            "id": tc.id,
                            "type": "function",
                            "function": {
                                "name": tc.function.name,
                                "arguments": tc.function.arguments,
                            },
                        }
                        for tc in msg.tool_calls
                    ],
                }
            )

            for tc in msg.tool_calls:
                args = json.loads(tc.function.arguments or "{}")
                print(f"MCP call_tool: {tc.function.name}({args})")
                result = await client.call_tool(tc.function.name, args)
                text = result_text(result)
                print(f"MCP result: {text}")
                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": tc.id,
                        "name": tc.function.name,
                        "content": text,
                    }
                )


if __name__ == "__main__":
    q = (
        "Check the MasaiMato menu and order 2 Masala Dosa for Asha. "
        "Tell me the order id and total bill."
    )
    asyncio.run(ask_masaimato(q))
```

**How the code works:**

- `list_tools()` discovers MasaiMato tools
- Groq receives those schemas and may request tool calls
- Your code runs MCP `call_tool` only
- Tool JSON goes back to Groq for a grounded confirmation

### Run

```bash
cd masaimato_mcp
python ai_mcp_chat.py
```

You should see: tools discovered → `get_menu` / `place_order` calls → final answer with order id and total.

Try a second prompt:

```python
q = "Order 1 Filter Coffee for Rohan and tell me the total."
```

### Demo walkthrough

1. Open `server.py` and read the MasaiMato menu dictionary
2. Run `python ai_mcp_chat.py`
3. Watch the printed `MCP call_tool` lines
4. Read the final AI confirmation with order id and total
5. Optional challenge: change the request to `"Order Pizza for Asha"` and observe the error path

### Activity — Trace One Order

| Check | Your note |
|---|---|
| Did AI call `get_menu`? | |
| Did AI call `place_order`? | |
| Order id shown? | |
| Invented a dish not on menu? (Yes/No) | |

---

## Optional: Ollama Cloud

Same MCP loop; change only the LLM client. Use **only** `OLLAMA_API_KEY`.

```python
from openai import OpenAI
load_dotenv()
api_key = os.getenv("OLLAMA_API_KEY")
if not api_key:
    raise ValueError("Set OLLAMA_API_KEY for the Ollama experiment.")
llm = OpenAI(base_url="https://ollama.com/v1", api_key=api_key)
model = "llama3.2"  # confirm current tag in your account
```

Keep MCP `list_tools` / `call_tool` unchanged.

---

## How This Ties Agent Communication Together

| Earlier idea | MasaiMato MCP version |
|---|---|
| Clear roles | Host / client / server |
| JSON contracts | Menu and order payloads |
| Stop when blocked | Unknown dish → error |
| AI invents facts | AI must call tools first |

Session story in four lines:

1. Talk clearly **inside** a task (plan → execute → stop)
2. Talk clearly **outside** to tools (MCP)
3. Build **MasaiMato** once
4. Let **Groq** order through MCP, not imagination

---

## Troubleshooting

| Symptom | Fix |
|---|---|
| Missing package | `pip install fastmcp groq python-dotenv openai` |
| `Set GROQ_API_KEY...` | Add key to `.env` in lab folder |
| `ModuleNotFoundError: server` | Run from `masaimato_mcp/` |
| AI invents a dish | Keep system prompt: use tools, do not invent |
| Empty terminal on `server.py` | Demo with `ai_mcp_chat.py`, not the raw server wait |

---

## Key Takeaways

- Agent communication needs clear roles, JSON handoffs, and stop conditions inside a task.
- Outside the app, **MCP** solves the N × M custom-plugin problem.
- MCP is not only REST: AI hosts **discover** tools, then call them in one shared style.
- **MasaiMato** is a mini Zomato MCP server: `get_menu` + `place_order`.
- Proper demo: **AI orders through MCP** with one key (`GROQ_API_KEY`; Ollama optional).

Next sessions move to workflow graphs that decide *when* steps run, while MCP-style tools decide *how* outside systems like MasaiMato are reached.

---

## Important Commands, Libraries, Terminologies Used

| Term / Item | Meaning |
|---|---|
| Planner–executor | Plan first, execute step by step |
| JSON message contract | Agreed inputs / outputs / errors |
| Stop condition | Complete or blocked ending |
| MCP | Model Context Protocol |
| Host / Client / Server | AI app / connector / capability program |
| Tool | Callable MCP action |
| N × M problem | Many apps × many tools without a standard |
| FastMCP | Python MCP helper |
| `list_tools` / `call_tool` | Discover and run MCP tools |
| Groq / `GROQ_API_KEY` | Main AI provider and key |
| Ollama Cloud / `OLLAMA_API_KEY` | Optional other provider |
| MasaiMato | Mini restaurant MCP app |
| `get_menu` / `place_order` | Menu + order tools |
