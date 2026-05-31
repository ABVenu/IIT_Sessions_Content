# Assignment — Subjective (Session: LangChain Tools — Custom Tools and Tool Calling)

**Difficulty:** Easy–Medium  
**Type:** Coding implementation (complete the starter)

---

## Scenario

**Campus Crate** sells IIT club merchandise. You already have mock order data in memory. Your job is to finish a small script so a chat model can **request** an order lookup via a LangChain tool, your code **runs** the tool, and the model returns a short friendly answer.

You do **not** need to build refund tickets, policy lookup, or a large agent framework—only **one tool** and a **short two-step loop** (model → tool → model).

---

## Task

Create a single file named `campus_crate_orders.py`. Start from the skeleton below, fill every `# TODO` section, and make the file runnable.

### Mock data (already given — do not change keys)

```python
ORDERS_DB = {
    "CC2001": {
        "order_id": "CC2001",
        "item": "Hoodie — Batch 2026",
        "status": "shipped",
        "eta_days": 3,
    },
}
```

### What you must implement

1. **`OrderStatusInput`** — Pydantic model with one field: `order_id: str` and a short `Field(description=...)`.

2. **`get_order_status`** — function decorated with `@tool(args_schema=OrderStatusInput)` that:
   - Normalizes `order_id` with `.strip().upper()`
   - Returns `json.dumps({"ok": True, "order": order})` if found
   - Returns `json.dumps({"ok": False, "message": "Order not found"})` if missing  
   - Has a one-line docstring saying to use it when the user asks about order status or delivery

3. **Model setup** — `load_dotenv()`, `init_chat_model` with `temperature=0`, and `model_with_tools = model.bind_tools([get_order_status])`.

4. **`run_order_help(user_query: str) -> str`** — a **simple** loop (at most **3** model turns):
   - Start `messages` with one system line (“use the order tool when the user asks about an order”) and the user query
   - Call `model_with_tools.invoke(messages)` and append the reply
   - If there are **no** `tool_calls`, return the reply text
   - Otherwise, for each tool call: run `get_order_status.invoke(tool_call["args"])`, append a `ToolMessage` with that result and the same `tool_call_id`
   - Call the model **once more** and return its text (no need for a `max_steps` loop or `unknown_tool` handling)

5. **`if __name__ == "__main__"`** — print the final answer for these **two** queries (with a line of `=` between them):
   - `"Where is my order CC2001?"`
   - `"What is Python?"` (should answer without calling the tool)

### Starter skeleton (copy and complete)

```python
import json
import os

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.messages import ToolMessage
from langchain.tools import tool
from pydantic import BaseModel, Field

load_dotenv()

ORDERS_DB = {
    "CC2001": {
        "order_id": "CC2001",
        "item": "Hoodie — Batch 2026",
        "status": "shipped",
        "eta_days": 3,
    },
}


# TODO 1: Define OrderStatusInput (Pydantic)


# TODO 2: Define get_order_status with @tool


# TODO 3: Create model and model_with_tools = model.bind_tools(...)


def run_order_help(user_query: str) -> str:
  # TODO 4: Build messages, invoke, handle tool_calls or return early,
  #         then second invoke after ToolMessage(s)
  pass


if __name__ == "__main__":
    # TODO 5: Run the two test queries and print answers
    pass
```

---

## Submission instructions (Case C — single file)

- Complete all `# TODO` sections in **one** file: `campus_crate_orders.py`.
- Use a virtual environment; install `langchain`, `langchain-openai`, `pydantic`, `python-dotenv`.
- Put `OPENAI_API_KEY` in `.env` (do not submit the key).
- Run the file and check that the first query uses the tool and the second does not.
- Submit the full `.py` source in the LMS code editor / answer box.

---

## Answer Explanation (for Assess platform)

### Ideal solution walkthrough

Learners practice the smallest useful tool-calling path: register one function with `@tool` and Pydantic, bind it with `bind_tools`, read `tool_calls` from the first `AIMessage`, run `tool.invoke(args)`, send back `ToolMessage`, and invoke the model again for a natural-language answer.

The second query checks that when `tool_calls` is empty, the function returns immediately without forcing a tool run.

### Reference solution (complete code)

```python
import json
import os

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.messages import ToolMessage
from langchain.tools import tool
from pydantic import BaseModel, Field

load_dotenv()

ORDERS_DB = {
    "CC2001": {
        "order_id": "CC2001",
        "item": "Hoodie — Batch 2026",
        "status": "shipped",
        "eta_days": 3,
    },
}


class OrderStatusInput(BaseModel):
    order_id: str = Field(description="Campus Crate order ID, e.g. CC2001.")


@tool(args_schema=OrderStatusInput)
def get_order_status(order_id: str) -> str:
    """Look up order status and delivery ETA when the user asks about an order."""
    normalized_id = order_id.strip().upper()
    order = ORDERS_DB.get(normalized_id)
    if not order:
        return json.dumps({"ok": False, "message": "Order not found"})
    return json.dumps({"ok": True, "order": order})


model = init_chat_model(os.getenv("CHAT_MODEL", "gpt-4o-mini"), temperature=0)
model_with_tools = model.bind_tools([get_order_status])


def run_order_help(user_query: str) -> str:
    messages = [
        {
            "role": "system",
            "content": "You are a Campus Crate helper. Use get_order_status when the user asks about an order.",
        },
        {"role": "user", "content": user_query},
    ]

    ai_message = model_with_tools.invoke(messages)
    messages.append(ai_message)

    tool_calls = getattr(ai_message, "tool_calls", None) or []
    if not tool_calls:
        return ai_message.content

    for tool_call in tool_calls:
        result = get_order_status.invoke(tool_call["args"])
        messages.append(
            ToolMessage(content=str(result), tool_call_id=tool_call["id"])
        )

    final_message = model_with_tools.invoke(messages)
    return final_message.content


if __name__ == "__main__":
    for query in ["Where is my order CC2001?", "What is Python?"]:
        print("\n" + "=" * 50)
        print("Query:", query)
        print("Answer:", run_order_help(query))
```

### Alternative approaches

- Wrapping `tool.invoke` in `try/except` is optional bonus, not required.
- Learners may print `tool_calls` for debugging.
- A small `for` loop with `max_steps=3` is acceptable if behaviour matches the two-step pattern above.

---

**End of subjective assignment**
