"""Generate Session 43 lecture note diagrams — Agent Tool Use (ShopEasy + Tesla continuity)."""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT = Path(__file__).parent
COLORS = {
    "bg": "#F4F7FB",
    "primary": "#2563A8",
    "secondary": "#6B4FA0",
    "accent": "#E8913A",
    "success": "#2E9E6B",
    "danger": "#C94C4C",
    "card": "#FFFFFF",
    "text": "#1E293B",
    "muted": "#64748B",
    "chunk1": "#DBEAFE",
    "chunk2": "#E9D5FF",
    "chunk3": "#FFEDD5",
    "shop": "#FFF7ED",
}


def setup_fig(title: str, subtitle: str = ""):
    fig, ax = plt.subplots(figsize=(12, 6.75), dpi=150)
    fig.patch.set_facecolor(COLORS["bg"])
    ax.set_facecolor(COLORS["bg"])
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6.75)
    ax.axis("off")
    ax.text(0.35, 6.35, title, fontsize=16, fontweight="bold", color=COLORS["text"], va="top")
    if subtitle:
        ax.text(0.35, 5.95, subtitle, fontsize=10, color=COLORS["muted"], va="top")
    return fig, ax


def rounded_box(ax, x, y, w, h, text, face, edge=COLORS["primary"], fontsize=9, weight="normal"):
    box = FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.02,rounding_size=0.15",
        linewidth=1.5, edgecolor=edge, facecolor=face,
    )
    ax.add_patch(box)
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fontsize,
            color=COLORS["text"], weight=weight, wrap=True)


def arrow(ax, x1, y1, x2, y2, color=COLORS["primary"]):
    arr = FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>", mutation_scale=12,
                          linewidth=1.5, color=color, shrinkA=2, shrinkB=2)
    ax.add_patch(arr)


def save(fig, name):
    path = OUT / name
    fig.savefig(path, bbox_inches="tight", facecolor=COLORS["bg"])
    plt.close(fig)
    print(f"Saved {path}")


def image_01():
    fig, ax = setup_fig(
        "Previous Tesla RAG vs Today's ShopEasy Tool Lab",
        "Session 42: search ./Tesla_db  |  Session 43: lookup_order on live mock warehouse",
    )
    rounded_box(ax, 0.4, 3.2, 5.3, 2.4,
                "PREVIOUS (Tesla memory lab)\n\ntesla_chat_history.json\nrag_answer on ./Tesla_db\n'And in 2023?' works\nStill text search only",
                COLORS["chunk1"], edge=COLORS["primary"], fontsize=9.5)
    rounded_box(ax, 6.3, 3.2, 5.3, 2.4,
                "TODAY (ShopEasy tool lab)\n\nshopeasy_tool_history.json\nlookup_order(order_id)\n'Order #48291 out today?'\nNeeds a TOOL — not in PDF",
                COLORS["shop"], edge=COLORS["accent"], fontsize=9.5)
    ax.text(5.85, 4.4, "→", fontsize=16, weight="bold", ha="center", color=COLORS["accent"])
    rounded_box(ax, 0.4, 0.9, 11.2, 1.6,
                "Same patterns carry forward: Groq · MAX_STEPS · JSON history\nShopEasy is NEW today — order status cannot live in the Tesla annual report",
                "#EEF2FF", edge=COLORS["secondary"], fontsize=10, weight="bold")
    save(fig, "session43-01-tesla-rag-vs-shopeasy-tools.png")


def image_02():
    fig, ax = setup_fig("RAG vs Tools — When Each Is Enough", "Policy handbook vs warehouse phone call")
    rows = [
        ("Return policy: 30 days?", "Policy chunk in index", "Often RAG alone", COLORS["success"]),
        ("When was MY order delivered?", "No order dates in PDF", "lookup_order tool", COLORS["accent"]),
        ("Return fee for pincode?", "Rate not in policy text", "calculate_fee tool", COLORS["secondary"]),
    ]
    rounded_box(ax, 0.4, 5.0, 2.5, 0.55, "User question", COLORS["card"], fontsize=9, weight="bold")
    rounded_box(ax, 3.0, 5.0, 3.5, 0.55, "RAG alone", COLORS["card"], fontsize=9, weight="bold")
    rounded_box(ax, 6.6, 5.0, 2.5, 0.55, "Tool needed?", COLORS["card"], fontsize=9, weight="bold")
    for i, (q, rag, tool, edge) in enumerate(rows):
        y = 3.8 - i * 1.05
        rounded_box(ax, 0.4, y, 2.5, 0.85, q, COLORS["chunk1"], fontsize=8)
        rounded_box(ax, 3.0, y, 3.5, 0.85, rag, COLORS["card"], edge=COLORS["primary"], fontsize=8)
        rounded_box(ax, 6.6, y, 4.8, 0.85, tool, COLORS["card"], edge=edge, fontsize=8.5, weight="bold")

    rounded_box(ax, 0.4, 0.35, 11.0, 1.35,
                "Hallucinated action: bot GUESSES delivery date without running lookup_order\nMemory + RAG + Tools work together — not interchangeable",
                "#FEE2E2", edge=COLORS["danger"], fontsize=9.5)
    save(fig, "session43-02-rag-vs-tools.png")


def image_03():
    fig, ax = setup_fig("Tool Schema — Menu the Model Reads", "LOOKUP_ORDER_SCHEMA: name · description · required parameters")
    rounded_box(ax, 0.4, 4.0, 11.2, 1.5,
                "LOOKUP_ORDER_SCHEMA\nname: lookup_order  |  description: when user asks order number\nparameters: order_id (string, required)",
                COLORS["chunk2"], edge=COLORS["secondary"], fontsize=10, weight="bold")
    rounded_box(ax, 0.4, 2.3, 3.5, 1.4,
                "User asks:\n'When was order\n48291 delivered?'", COLORS["chunk1"], fontsize=9)
    rounded_box(ax, 4.1, 2.3, 3.5, 1.4,
                "Model fills form:\nlookup_order\norder_id: '48291'", COLORS["shop"], edge=COLORS["accent"], fontsize=9, weight="bold")
    rounded_box(ax, 7.8, 2.3, 3.8, 1.4,
                "Kitchen chit format:\nevery field labeled\nnot 'make something nice'", COLORS["success"], fontsize=9)
    arrow(ax, 3.9, 3.0, 4.1, 3.0, COLORS["accent"])
    arrow(ax, 7.6, 3.0, 7.8, 3.0, COLORS["accent"])
    rounded_box(ax, 0.4, 0.35, 11.2, 1.5,
                "Common mistakes: vague name 'helper' · omit required → empty order_id · name mismatch with Python function",
                COLORS["card"], edge=COLORS["danger"], fontsize=9.5)
    save(fig, "session43-03-tool-schema.png")


def image_04():
    fig, ax = setup_fig("Register and Bind a Tool", "TOOL_SCHEMAS → Groq API  |  TOOL_REGISTRY → Python functions")
    rounded_box(ax, 0.4, 4.2, 5.2, 1.6, "TOOL_SCHEMAS\n[sent to Groq tools=]\nModel sees the menu", COLORS["chunk2"], edge=COLORS["secondary"], fontsize=10)
    rounded_box(ax, 6.4, 4.2, 5.2, 1.6, "TOOL_REGISTRY\nlookup_order → lookup_order()\nYou control what runs", COLORS["success"], edge=COLORS["success"], fontsize=10)

    rounded_box(ax, 2.5, 2.4, 7.0, 1.3, "run_registered_tool(name, args)\nBind bridge: parse args → call Python → json.dumps(result)", COLORS["shop"], edge=COLORS["accent"], fontsize=10, weight="bold")
    arrow(ax, 2.8, 4.2, 4.0, 3.75, COLORS["primary"])
    arrow(ax, 9.2, 4.2, 8.0, 3.75, COLORS["primary"])

    rounded_box(ax, 0.4, 0.35, 5.5, 1.5,
                "Test without LLM:\nrun_registered_tool\n('lookup_order', {'order_id':'48291'})",
                COLORS["card"], edge=COLORS["primary"], fontsize=9)
    rounded_box(ax, 6.1, 0.35, 5.5, 1.5,
                "MOCK_ORDERS dict\n48291 → out_for_delivery\n51002 → delivered 12 May",
                COLORS["card"], edge=COLORS["accent"], fontsize=9)
    save(fig, "session43-04-register-bind.png")


def image_05():
    fig, ax = setup_fig("Model–Tool Loop", "propose → run → return → reason again (until final reply or MAX_STEPS)")
    stages = [
        ("1 Propose", "Model picks\ntool or text", COLORS["chunk1"]),
        ("2 Run", "TOOL_REGISTRY\nlookup_order()", COLORS["chunk2"]),
        ("3 Return", "append_tool_result\nrole: tool", COLORS["chunk3"]),
        ("4 Reason", "Model reads\nresult", COLORS["success"]),
    ]
    for i, (title, body, face) in enumerate(stages):
        x = 0.35 + i * 2.9
        rounded_box(ax, x, 3.8, 2.6, 0.65, title, face, fontsize=9, weight="bold")
        rounded_box(ax, x, 2.5, 2.6, 1.1, body, COLORS["card"], fontsize=8.5)
        if i < len(stages) - 1:
            arrow(ax, x + 2.6, 4.15, x + 2.9, 4.15, COLORS["accent"])
    arrow(ax, 11.0, 3.0, 1.5, 3.0, COLORS["secondary"])

    rounded_box(ax, 0.4, 0.9, 5.5, 1.3,
                "Fiction bug:\nmodel SAYS it checked\nbut code never ran tool",
                COLORS["card"], edge=COLORS["danger"], fontsize=9)
    rounded_box(ax, 6.0, 0.9, 5.6, 1.3,
                "Wiring bug:\ntool ran but result\nnever appended to messages",
                COLORS["card"], edge=COLORS["danger"], fontsize=9)
    save(fig, "session43-05-model-tool-loop.png")


def image_06():
    fig, ax = setup_fig("Tool Message Roles in the Loop", "tool_call_id must match — verify before next Groq call")
    roles = [
        ("user", "When was order 48291 delivered?", COLORS["chunk1"]),
        ("assistant", "tool_calls: lookup_order\norder_id: 48291", COLORS["chunk2"]),
        ("tool", '{"status":"out_for_delivery"\n"eta":"today by 6 PM"}', COLORS["chunk3"]),
        ("assistant", "Order 48291 is out for\ndelivery today by 6 PM.", COLORS["success"]),
    ]
    for i, (role, content, face) in enumerate(roles):
        y = 5.0 - i * 1.15
        rounded_box(ax, 0.5, y, 1.8, 0.85, role, face, edge=COLORS["primary"], fontsize=9, weight="bold")
        rounded_box(ax, 2.4, y, 9.1, 0.85, content, COLORS["card"], fontsize=8.5)
        if i < len(roles) - 1:
            arrow(ax, 1.4, y, 1.4, y - 0.3, COLORS["muted"])
    rounded_box(ax, 0.4, 0.25, 11.2, 0.85,
                "verify_tool_feedback() → False if tool result missing — do not trust final answer",
                "#FEE2E2", edge=COLORS["danger"], fontsize=9.5)
    save(fig, "session43-06-tool-message-roles.png")


def image_07():
    fig, ax = setup_fig("Groq Executor — run_tool_agent_turn", "tools=TOOL_SCHEMAS · while step < MAX_STEPS · shopeasy_tool_history.json")
    rounded_box(ax, 0.4, 4.5, 2.8, 1.3, "load_tool_history\nshopeasy_tool\n_history.json", COLORS["chunk1"])
    rounded_box(ax, 3.4, 4.5, 3.0, 1.3, "propose_tool_or_reply\nGroq + tools=\nauto", COLORS["chunk2"])
    rounded_box(ax, 6.6, 4.5, 2.5, 1.3, "run_registered_tool\n+ append_tool\n_result", COLORS["chunk3"])
    rounded_box(ax, 9.3, 4.5, 2.3, 1.3, "save_tool_history\nfull message list", COLORS["success"])
    for i in range(3):
        arrow(ax, 3.2 + i * 3.2, 5.15, 3.4 + i * 3.2, 5.15, COLORS["accent"])

    rounded_box(ax, 0.4, 2.5, 5.5, 1.5,
                "Do NOT overwrite\ntesla_chat_history.json\nSeparate lab files",
                COLORS["card"], edge=COLORS["danger"], fontsize=9.5)
    rounded_box(ax, 6.1, 2.5, 5.5, 1.5,
                "MAX_STEPS = 5\nSame safety rail\nfrom previous lab",
                COLORS["card"], edge=COLORS["success"], fontsize=9.5)

    rounded_box(ax, 0.4, 0.35, 11.2, 1.7,
                "chat_with_tools(msg) → load → run_tool_agent_turn → save → reply\nTool roles saved in JSON — turn 2 remembers order #48291 lookup",
                "#EEF2FF", edge=COLORS["secondary"], fontsize=9.5)
    save(fig, "session43-07-groq-executor.png")


def image_08():
    fig, ax = setup_fig("Notebook Demo — ShopEasy Tool Lab", "Step A: registry test  |  Step B: full loop  |  Step C: verify tool in JSON")
    steps = [
        ("A", "run_registered_tool\n48291 → JSON", COLORS["chunk1"]),
        ("B", "run_tool_agent_turn\n'Is 48291 out today?'", COLORS["chunk2"]),
        ("C", "any role=='tool'\nin saved history?", COLORS["success"]),
    ]
    for i, (label, body, face) in enumerate(steps):
        x = 0.5 + i * 3.85
        rounded_box(ax, x, 4.0, 0.7, 0.7, label, face, fontsize=12, weight="bold")
        rounded_box(ax, x + 0.85, 3.5, 2.85, 1.5, body, COLORS["card"], edge=face, fontsize=9)
        if i < 2:
            arrow(ax, x + 3.7, 4.25, x + 3.85, 4.25, COLORS["accent"])

    rounded_box(ax, 0.4, 1.5, 5.5, 1.5,
                "Turn 1: order 51002\ndelivered date",
                COLORS["card"], edge=COLORS["primary"], fontsize=9.5)
    rounded_box(ax, 6.0, 1.5, 5.6, 1.5,
                "Turn 2: ETA on same order\nmemory + tool entries",
                COLORS["card"], edge=COLORS["success"], fontsize=9.5)
    arrow(ax, 5.9, 2.25, 6.0, 2.25, COLORS["accent"])

    rounded_box(ax, 0.4, 0.2, 11.2, 1.0,
                "Optional: search_tesla_report wraps prior rag_answer on ./Tesla_db as second tool",
                "#FFFBEB", edge=COLORS["accent"], fontsize=9)
    save(fig, "session43-08-notebook-demo-flow.png")


if __name__ == "__main__":
    image_01()
    image_02()
    image_03()
    image_04()
    image_05()
    image_06()
    image_07()
    image_08()
