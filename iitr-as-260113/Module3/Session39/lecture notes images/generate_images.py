"""Generate Session 39 lecture note diagrams — LangChain memory on agents."""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

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
    "history": "#DBEAFE",
    "scratch": "#E9D5FF",
    "session_a": "#FFEDD5",
    "session_b": "#D1FAE5",
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
        "Why Agents Need Memory",
        "Stateless calls forget prior turns — conversational memory carries the dialogue forward",
    )
    rounded_box(ax, 0.4, 3.5, 5.2, 2.0,
                "Stateless LLM call\nEach invoke = blank slate\nTurn 2: 'status of it?'\nModel: Which order?",
                COLORS["card"], edge=COLORS["danger"], fontsize=9)
    rounded_box(ax, 6.4, 3.5, 5.2, 2.0,
                "Conversational memory\nchat_history in every invoke\nTurn 1: ORD102 stored\nTurn 2: tool uses ORD102",
                COLORS["history"], edge=COLORS["success"], fontsize=9)
    arrow(ax, 5.6, 4.5, 6.4, 4.5, COLORS["accent"])
    ax.text(5.85, 4.85, "add memory", fontsize=9, color=COLORS["accent"], ha="center", weight="bold")
    rounded_box(ax, 0.5, 1.0, 11.0, 1.8,
                "Tool calling still works each turn — wrong/missing context causes repeated questions\n"
                "Clinic file analogy: reception adds a line each visit; doctor reads the whole file",
                "#EEF2FF", edge=COLORS["secondary"], fontsize=10)
    save(fig, "session39-01-why-agents-need-memory.png")


def image_02():
    fig, ax = setup_fig(
        "MessagesPlaceholder + chat_history in the Prompt",
        "Placeholder reserves a seat — your code (or RunnableWithMessageHistory) fills it",
    )
    layers = [
        ("system", "Support agent rules\nRemember order IDs", COLORS["card"]),
        ("chat_history", "MessagesPlaceholder\noptional=True\nPast Human + AI turns", COLORS["history"]),
        ("human", "{input}\nCurrent user message", COLORS["session_a"]),
        ("agent_scratchpad", "MessagesPlaceholder\nTool steps THIS run only", COLORS["scratch"]),
    ]
    y = 5.0
    for label, body, face in layers:
        rounded_box(ax, 0.5, y - 1.05, 2.0, 0.55, label, face, fontsize=10, weight="bold", edge=COLORS["primary"])
        rounded_box(ax, 2.7, y - 1.05, 8.8, 0.55, body, face, fontsize=9)
        y -= 1.25
    rounded_box(ax, 0.5, 0.35, 11.0, 1.0,
                "First turn: chat_history=[] is valid with optional=True\n"
                "After invoke: append HumanMessage then AIMessage to the same list",
                COLORS["card"], edge=COLORS["success"], fontsize=10)
    save(fig, "session39-02-messages-placeholder-chat-history.png")


def image_03():
    fig, ax = setup_fig("chat_history vs agent_scratchpad", "Both placeholders — different jobs in a tool-calling agent")
    cols = [
        ("chat_history", [
            "Past user ↔ assistant turns",
            "YOU append (manual) or RunnableWithMessageHistory",
            "Needed for: 'status of it?'",
            "Lives across invocations (RAM / DB)",
        ], COLORS["history"], COLORS["primary"]),
        ("agent_scratchpad", [
            "Current run tool loop only",
            "AgentExecutor fills automatically",
            "Needed for: multi-step tools in one query",
            "Cleared when run ends",
        ], COLORS["scratch"], COLORS["secondary"]),
    ]
    for i, (title, lines, face, edge) in enumerate(cols):
        x = 0.5 + i * 6.0
        rounded_box(ax, x, 5.0, 5.5, 0.7, title, face, edge=edge, fontsize=12, weight="bold")
        for j, line in enumerate(lines):
            rounded_box(ax, x, 3.8 - j * 0.85, 5.5, 0.75, line, COLORS["card"], edge=edge, fontsize=9)
    rounded_box(ax, 0.5, 0.35, 11.0, 0.95,
                "Scratchpad does NOT remember ORD102 from turn 1 when turn 2 runs — that is chat_history's job",
                "#FFFBEB", edge=COLORS["accent"], fontsize=10, weight="bold")
    save(fig, "session39-03-chat-history-vs-scratchpad.png")


def image_04():
    fig, ax = setup_fig(
        "Classic Bug: Placeholder Without Append",
        "Turn 1 works — Turn 2 asks for order ID again",
    )
    rounded_box(ax, 0.4, 4.5, 3.5, 1.2, "Turn 1\nUser: ORD102\nAI: status OK", COLORS["success"], edge=COLORS["success"])
    rounded_box(ax, 4.2, 4.5, 3.5, 1.2, "Bug\nNever append to\nchat_history list", COLORS["danger"], edge=COLORS["danger"])
    rounded_box(ax, 8.0, 4.5, 3.5, 1.2, "Turn 2\nStill passes []\n'Share order ID?'", COLORS["card"], edge=COLORS["danger"])
    arrow(ax, 3.9, 5.1, 4.2, 5.1)
    arrow(ax, 7.7, 5.1, 8.0, 5.1)

    fixes = [
        "Match variable name in template and invoke",
        "Append HumanMessage then AIMessage after each run",
        "Human before AI per turn",
        "Per-session store — not one global list",
    ]
    for i, fix in enumerate(fixes):
        rounded_box(ax, 0.5 + (i % 2) * 6.0, 2.6 - (i // 2) * 1.1, 5.5, 0.9, f"✓ {fix}", COLORS["card"],
                    edge=COLORS["success"], fontsize=9)
    rounded_box(ax, 0.5, 0.3, 11.0, 0.85, "Fix: same list reference — append after invoke, pass again on turn 2",
                "#EEF2FF", edge=COLORS["primary"], fontsize=10, weight="bold")
    save(fig, "session39-04-bug-missing-append.png")


def image_05():
    fig, ax = setup_fig("Stateless vs With Memory — Same Wording, Turn 2", "Proves memory changes agent behavior")
    for col, title, t1, t2, edge in [
        (0.4, "Stateless\nchat_history=[] always", "Turn 1: learns ORD102", "Turn 2: 'status of it?'\nAsks for ID again", COLORS["danger"]),
        (6.4, "With memory\nappend after invoke", "Turn 1: ORD102 in history", "Turn 2: get_order_status(ORD102)", COLORS["success"]),
    ]:
        rounded_box(ax, col, 4.8, 5.2, 0.65, title, COLORS["card"], edge=edge, fontsize=10, weight="bold")
        rounded_box(ax, col, 3.2, 5.2, 1.3, t1, COLORS["card"], edge=edge, fontsize=9)
        arrow(ax, col + 2.6, 3.85, col + 2.6, 3.0, edge)
        rounded_box(ax, col, 1.5, 5.2, 1.3, t2, COLORS["history"] if col > 4 else COLORS["card"], edge=edge, fontsize=9)
    rounded_box(ax, 0.5, 0.25, 11.0, 0.9,
                "Memory helps: pronouns, IDs in turn 1 + action in turn 2  |  Stateless OK: one-shot complete questions",
                "#EEF2FF", edge=COLORS["secondary"], fontsize=10)
    save(fig, "session39-05-stateless-vs-with-memory.png")


def image_06():
    fig, ax = setup_fig(
        "RunnableWithMessageHistory — Automatic Session Memory",
        "You pass input + session_id — wrapper loads, injects, runs, appends",
    )
    steps = [
        ("invoke", "input + session_id\nin config", COLORS["session_a"]),
        ("load", "get_session_history\nInMemoryChatMessageHistory", COLORS["history"]),
        ("inject", "chat_history into\nMessagesPlaceholder", COLORS["scratch"]),
        ("run", "AgentExecutor +\ntools", COLORS["card"]),
        ("append", "Save new Human +\nAI to session store", COLORS["success"]),
    ]
    for i, (title, body, face) in enumerate(steps):
        x = 0.35 + i * 2.35
        rounded_box(ax, x, 4.0, 2.0, 0.6, title, face, fontsize=10, weight="bold")
        rounded_box(ax, x, 2.5, 2.0, 1.2, body, COLORS["card"], fontsize=8.5)
        if i < len(steps) - 1:
            arrow(ax, x + 2.0, 4.3, x + 2.35, 4.3, COLORS["accent"])
    rounded_box(ax, 0.5, 0.85, 5.3, 1.2, "store = {}\nsession_id → history object", COLORS["card"], edge=COLORS["primary"])
    rounded_box(ax, 6.0, 0.85, 5.5, 1.2, "No manual append\nhistory_messages_key='chat_history'",
                COLORS["card"], edge=COLORS["secondary"])
    save(fig, "session39-06-runnable-with-message-history.png")


def image_07():
    fig, ax = setup_fig("Session Isolation", "Session A and B do not share chat_history — like separate ChatGPT tabs")
    rounded_box(ax, 0.5, 3.8, 5.0, 2.0, "Session A (user-001)\nTurn 1: ORD101\nTurn 2: 'status of it?'\n→ knows ORD101",
                COLORS["session_a"], edge=COLORS["accent"])
    rounded_box(ax, 6.5, 3.8, 5.0, 2.0, "Session B (user-002)\n'What is my order ID?'\n→ should NOT see ORD101",
                COLORS["session_b"], edge=COLORS["success"])
    ax.text(6.0, 4.8, "≠", fontsize=28, ha="center", color=COLORS["danger"], weight="bold")
    rounded_box(ax, 0.5, 1.2, 11.0, 1.5,
                "store[session_id] = separate InMemoryChatMessageHistory\n"
                "Production: never one global chat_history for all customers",
                "#EEF2FF", edge=COLORS["primary"], fontsize=10)
    rounded_box(ax, 0.5, 0.25, 11.0, 0.75, "Rolling window: n_messages=10 on placeholder drops oldest when chat grows",
                COLORS["card"], edge=COLORS["secondary"], fontsize=9)
    save(fig, "session39-07-session-isolation-rolling.png")


if __name__ == "__main__":
    image_01()
    image_02()
    image_03()
    image_04()
    image_05()
    image_06()
    image_07()
