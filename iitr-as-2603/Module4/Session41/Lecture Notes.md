# Agent Communication Patterns

## Introduction

In the **previous** session you built a **recipe mini-app**: a food photo, spoken ingredients, an **alignment guardrail**, then a recipe plus spoken audio — or a polite **refusal** when the photo and speech did not match.

This session is about **how agents talk**. First you design a **planner–executor** flow with **JSON messages** and **stop conditions** for one food-order task. Then you build **MasaiMato**: a mini Zomato-style **MCP** restaurant where **Groq** reads the menu and places orders through MCP tools instead of inventing dishes.

**What you will learn:**

- Decompose one user goal into planner and executor subtasks, with JSON inputs, outputs, and errors
- Run a **sequential** planner–executor script and **stop** when the task is complete or blocked
- Explain MCP: host, client, server, tools
- Build **MasaiMato** and run an **AI + MCP ordering loop** with one cloud key (`GROQ_API_KEY`)

---

## Planner–Executor for One Business Task

A recipe app already made a **decision** (cook or refuse). A planner–executor makes a **checklist**, then ticks items **one by one**.

- **Official Definition:** A **planner–executor** pattern splits work into a planner that creates an ordered plan and an executor that performs one step at a time.
- **In Simple Words:** One role writes the kitchen tickets; another completes one ticket at a time.
- **Real-Life Example:** Goal: “2 Masala Dosa for Asha” → check menu → place order → share order id. Nobody argues about who speaks next.

| Idea | Meaning | Example |
|---|---|---|
| Task decomposition | Split one goal into ordered subtasks | Check menu → place order |
| JSON input | Planner → executor | `{"action":"place_order","item_name":"masala dosa","quantity":2,"customer_name":"Asha"}` |
| JSON output (ok) | Executor → next step | `{"status":"ok","order_id":"MM1001","total_inr":160}` |
| JSON error | Executor → stop | `{"status":"error","message":"Dish not on menu"}` |
| Sequential flow | Execute step 1, then 2 — no extra agents | Planner plans once; executor runs the list |
| Stop condition | End when complete or blocked | Dish missing → blocked; order placed → complete |

![Planner writing structured kitchen tickets and executor completing one ticket at a time, showing agent communication handoffs for a food order](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module4/session41/session41-01-agent-communication-handoff.png)

```text
User goal → Planner plan → Executor step (JSON) → Executor step (JSON) → Complete / Blocked
```

**Common doubt:** “Can two planners debate the next step?” Not here. This is **sequential** only — one plan, then one executor, until a stop condition fires.

### Sequential script (no multi-agent arbitration)

```python
# planner_executor.py — one food-order task, sequential handoffs
MENU = {"masala dosa": 80, "filter coffee": 30}  # dish -> price in INR


def planner(goal: str) -> list:
    """Turn one user goal into ordered subtasks for the executor."""
    # Lab uses a fixed Asha/Dosa checklist so the JSON shape stays clear.
    return [  # checklist, not a group chat
        {"step": 1, "action": "get_menu", "input": {}},
        {"step": 2, "action": "place_order",
         "input": {"item_name": "masala dosa", "quantity": 2, "customer_name": "Asha"}},
    ]


def executor(task: dict) -> dict:
    """Run one subtask and return JSON (ok or error)."""
    action = task["action"]
    if action == "get_menu":
        items = [{"item_name": n, "price_inr": p} for n, p in MENU.items()]
        return {"status": "ok", "items": items}
    if action == "place_order":
        key = task["input"]["item_name"].strip().lower()
        qty = task["input"]["quantity"]
        if key not in MENU:
            return {"status": "error", "message": f"'{key}' not on menu."}
        if qty < 1:
            return {"status": "error", "message": "Quantity must be at least 1."}
        return {"status": "ok", "order_id": "MM1001", "total_inr": MENU[key] * qty}
    return {"status": "error", "message": f"Unknown action: {action}"}


def run(goal: str) -> dict:
    """Execute the plan in order. Stop when complete or blocked."""
    last = None
    for task in planner(goal):
        last = executor(task)
        print(f"Step {task['step']} {task['action']} -> {last}")
        if last.get("status") == "error":
            return {"stop": "blocked", "reason": last["message"]}
    return {"stop": "complete", "result": last}


if __name__ == "__main__":
    print(run("Order 2 Masala Dosa for Asha"))
```

**How the code works:**

- `planner` decomposes the goal into two executor subtasks.
- `executor` returns a **JSON contract**: `status: ok` or `status: error`.
- `run` is sequential: any error **stops as blocked**; all successes **stop as complete**.

**Quick check:** Change `item_name` to `"pizza"` and predict the stop reason → `blocked`, dish not on menu.

### Activity — Name the stop

For each result, write `complete` or `blocked`:

| Result JSON | Your stop |
|---|---|
| `{"status":"ok","order_id":"MM1001","total_inr":160}` | |
| `{"status":"error","message":"pizza not on menu"}` | |
| `{"status":"error","message":"Quantity must be at least 1."}` | |

**Suggested answers:** complete; blocked; blocked.

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

![Messy custom plugins from many AI apps versus one MCP hub connecting cleanly to a single MasaiMato restaurant service](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module4/session41/session41-02-why-mcp-standard.png)

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

![Hungry student talking to a Host AI, with an MCP Client cable connecting to the MasaiMato MCP Server offering Get Menu and Place Order tools](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module4/session41/session41-03-mcp-roles-masaimato.png)

```text
Hungry student → Host AI → MCP Client ←→ MasaiMato MCP Server (get_menu / place_order)
API:   your code → POST /orders → backend
MCP:   AI → list_tools() → call_tool("place_order", {...}) → MasaiMato
```

| Point | Traditional API | MCP |
|---|---|---|
| Start | You already know the URL | Client discovers tools |
| Style | Many REST shapes | Shared tool call style |
| AI reuse | Custom integration per app | One server, many hosts |

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

Build a mini food-ordering MCP app: `get_menu()` and `place_order(item_name, quantity, customer_name)`, then a Groq loop that confirms with a real order id.

```text
"Order 2 Masala Dosa for Asha" → Groq (+ MCP tool schemas) → call_tool → MasaiMato JSON → confirmation
```

This is the same sequential idea as `planner_executor.py`: discover → act → stop. The planner is now the **model**; the executor is **MCP `call_tool`**.

**Provider rule:** Main notes use **Groq** + `GROQ_API_KEY` only. You may later try Ollama Cloud with only `OLLAMA_API_KEY`.

---

## Setup

```bash
pip install fastmcp groq python-dotenv openai
```

Create `.env` (do not commit):

```bash
GROQ_API_KEY=your_groq_key_here
```

Create folder `masaimato_mcp/` with `server.py` (MasaiMato MCP tools) and `ai_mcp_chat.py` (Groq + MCP ordering demo). Keep both files in the same folder so `from server import mcp` works.

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
        return {"status": "error", "message": f"'{item_name}' not on menu. Call get_menu first."}
    if quantity < 1:
        return {"status": "error", "message": "Quantity must be at least 1."}
    order_id = f"MM{NEXT_ID}"
    NEXT_ID += 1
    order = {
        "order_id": order_id, "item_name": key, "quantity": quantity,
        "customer_name": customer_name.strip(), "total_inr": MENU[key] * quantity, "status": "preparing",
    }
    ORDERS[order_id] = order
    return {"status": "ok", "message": "Order placed on MasaiMato.", "order": order}


if __name__ == "__main__":
    mcp.run()  # stdio server for host apps
```

**How the code works:**

- `get_menu` returns dishes and prices.
- `place_order` rejects unknown dishes, creates `MM1001`-style ids, and stores the bill.
- Docstrings become tool descriptions for the AI.

**Quick check:** Predict `place_order("Pizza", 1, "Asha")` → should return `status: error`.

---

## AI Orders Through MCP (Groq)

The AI is the waiter. MCP is the official ticket system to the kitchen. Your script runs only `call_tool`.

- **Official Definition:** An **AI + MCP tool loop** lets the model choose discovered tools; your program executes them and returns results for the final answer.
- **In Simple Words:** Chat thinks; MCP executes; answer stays grounded.
- **Real-Life Example:** Do not invent Masala Dosa prices — read MasaiMato menu first.

![AI food assistant taking a student order, reading the MasaiMato menu through MCP, and returning a real order confirmation with id MM1001](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module4/session41/session41-04-ai-orders-through-mcp.png)

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
                model=model, messages=messages, tools=tools, tool_choice="auto", temperature=0,
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
                            "id": tc.id, "type": "function",
                            "function": {"name": tc.function.name, "arguments": tc.function.arguments},
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
                    {"role": "tool", "tool_call_id": tc.id, "name": tc.function.name, "content": text}
                )


if __name__ == "__main__":
    q = "Check the MasaiMato menu and order 2 Masala Dosa for Asha. Tell me the order id and total bill."
    asyncio.run(ask_masaimato(q))
```

**How the code works:**

- `list_tools()` discovers MasaiMato tools; Groq receives those schemas and may request tool calls.
- Your code runs MCP `call_tool` only; ok **and** error JSON both go back to Groq.
- The `while` loop **stops** only when Groq returns a final answer with no further tool calls.

### Run

```bash
cd masaimato_mcp
python ai_mcp_chat.py
```

You should see: tools discovered → `get_menu` / `place_order` calls → final answer with order id and total. Then try `q = "Order 1 Filter Coffee for Rohan and tell me the total."` and `"Order Pizza for Asha"` to watch the error path.

### Activity — Trace One Order

| Check | Your note |
|---|---|
| Did AI call `get_menu`? | |
| Did AI call `place_order`? | |
| Order id shown? | |
| Invented a dish not on menu? (Yes/No) | |

---

## Ollama Cloud (same MCP loop)

Change only the LLM client. Use **only** `OLLAMA_API_KEY`. Keep MCP `list_tools` / `call_tool` unchanged.

```python
from openai import OpenAI
load_dotenv()
api_key = os.getenv("OLLAMA_API_KEY")
if not api_key:
    raise ValueError("Set OLLAMA_API_KEY for the Ollama experiment.")
llm = OpenAI(base_url="https://ollama.com/v1", api_key=api_key)
model = "llama3.2"  # confirm current tag in your account
```

---

## How This Ties Agent Communication Together

| Earlier idea | MasaiMato MCP version |
|---|---|
| Clear roles | Host / client / server |
| JSON contracts | Menu and order payloads |
| Sequential executor | `call_tool` one step at a time |
| Stop when blocked | Unknown dish → error |
| AI invents facts | AI must call tools first |

Talk clearly **inside** a task (plan → execute → stop), then **outside** to tools (MCP). Build **MasaiMato** once, and let **Groq** order through MCP, not imagination.

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

- Agent communication needs clear roles, **JSON handoffs**, and **stop conditions** inside a sequential planner–executor flow.
- Outside the app, **MCP** solves the N × M custom-plugin problem.
- MCP is not only REST: AI hosts **discover** tools, then call them in one shared style.
- **MasaiMato** is a mini Zomato MCP server: `get_menu` + `place_order`.
- Proper demo: **AI orders through MCP** with one key (`GROQ_API_KEY`; Ollama is another provider you can try).

Upcoming sessions move to workflow graphs that decide *when* steps run, while MCP-style tools decide *how* outside systems like MasaiMato are reached.

---

## Important Commands, Libraries, Terminologies Used

| Term / Item | Meaning |
|---|---|
| Planner–executor | Plan first, execute step by step |
| Task decomposition | Split one goal into ordered subtasks |
| JSON message contract | Agreed inputs / outputs / errors |
| Stop condition | Complete or blocked ending |
| Sequential flow | No multi-agent debate; one plan, then execute |
| MCP | Model Context Protocol |
| Host / Client / Server | AI app / connector / capability program |
| Tool | Callable MCP action |
| N × M problem | Many apps × many tools without a standard |
| FastMCP | Python MCP helper |
| `list_tools` / `call_tool` | Discover and run MCP tools |
| Groq / `GROQ_API_KEY` | Main AI provider and key |
| Ollama Cloud / `OLLAMA_API_KEY` | Another provider you can try |
| MasaiMato | Mini restaurant MCP app |
| `get_menu` / `place_order` | Menu + order tools |
