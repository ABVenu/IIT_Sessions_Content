"""Generate Session 41 lecture note diagrams — Agentic RAG and integrated LangChain agent."""
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
    "ingest": "#DBEAFE",
    "query": "#FFEDD5",
    "chroma": "#D1FAE5",
    "llm": "#E9D5FF",
    "tool_a": "#BFDBFE",
    "tool_b": "#FDE68A",
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
        "Standalone RAG vs Agentic RAG",
        "Yesterday always retrieved; today the agent chooses when to search",
    )
    rounded_box(ax, 0.4, 3.6, 5.2, 2.3,
                "Standalone RAG chain\nUser → always retrieve\n→ prompt + chunks → LLM\nNo choice, no other tools",
                COLORS["card"], edge=COLORS["danger"], fontsize=9)
    rounded_box(ax, 6.4, 3.6, 5.2, 2.3,
                "Integrated agent (Agentic RAG)\nUser → Agent decides\n→ retriever | ticket tool | both | refuse\nSupervisor picks the button",
                COLORS["ingest"], edge=COLORS["success"], fontsize=9)
    arrow(ax, 5.6, 4.75, 6.4, 4.75, COLORS["accent"])
    ax.text(5.85, 5.2, "evolve", fontsize=9, color=COLORS["accent"], ha="center", weight="bold")

    rows = [
        ("Retrieval", "Always runs", "Only when agent picks tool"),
        ("Other actions", "Not supported", "Ticket lookup, future tools"),
        ("Memory", "Usually none", "chat_history across turns"),
    ]
    for i, (piece, old, new) in enumerate(rows):
        y = 2.5 - i * 0.75
        rounded_box(ax, 0.5, y, 2.2, 0.55, piece, COLORS["query"], fontsize=8.5, weight="bold")
        rounded_box(ax, 2.9, y, 4.0, 0.55, old, COLORS["card"], edge=COLORS["danger"], fontsize=8.5)
        rounded_box(ax, 7.1, y, 4.4, 0.55, new, COLORS["chroma"], edge=COLORS["success"], fontsize=8.5)

    rounded_box(ax, 0.5, 0.2, 11.0, 0.75,
                "create_retriever_tool exposes your existing retriever as a tool the agent can select",
                "#EEF2FF", edge=COLORS["secondary"], fontsize=10)
    save(fig, "session41-01-standalone-vs-agentic-rag.png")


def image_02():
    fig, ax = setup_fig(
        "Tool Arbitration — Pick the Right Tool",
        "Good tool descriptions answer what, when, and which user need",
    )
    rounded_box(ax, 4.2, 4.8, 3.6, 0.9, "Course Support Agent\n(front desk)", COLORS["llm"],
                edge=COLORS["secondary"], fontsize=10, weight="bold")

    rounded_box(ax, 0.5, 2.5, 4.8, 1.8,
                "course_policy_tool\n(retriever-backed)\nRefund, attendance,\nbatch change rules",
                COLORS["tool_a"], edge=COLORS["primary"], fontsize=9)
    rounded_box(ax, 6.7, 2.5, 4.8, 1.8,
                "get_ticket_status\n(auxiliary @tool)\nTKT-1001, TKT-1002\nlive ticket records",
                COLORS["tool_b"], edge=COLORS["accent"], fontsize=9)

    arrow(ax, 5.0, 4.8, 2.9, 4.3, COLORS["primary"])
    arrow(ax, 7.0, 4.8, 9.1, 4.3, COLORS["accent"])

    examples = [
        ("Refund policy?", "course_policy_tool", COLORS["tool_a"]),
        ("Status TKT-1002?", "get_ticket_status", COLORS["tool_b"]),
        ("Refund ticket status?", "both tools", COLORS["chroma"]),
        ("Who won IPL 2025?", "neither — refuse", COLORS["card"]),
    ]
    for i, (query, action, face) in enumerate(examples):
        x = 0.4 + i * 2.9
        rounded_box(ax, x, 0.35, 2.7, 1.6, f"{query}\n→ {action}", face,
                    edge=COLORS["primary"] if i < 3 else COLORS["danger"], fontsize=8)

    save(fig, "session41-02-tool-arbitration.png")


def image_03():
    fig, ax = setup_fig(
        "Course Support Agent — ragagent.py Architecture",
        "Two tools + memory + AgentExecutor in one file",
    )
    rounded_box(ax, 4.0, 5.0, 4.0, 0.85, "User query + chat_history", COLORS["query"],
                edge=COLORS["accent"], fontsize=10, weight="bold")
    arrow(ax, 6.0, 5.0, 6.0, 4.55, COLORS["primary"])

    rounded_box(ax, 3.2, 3.5, 5.6, 1.0, "AgentExecutor\nmax_iterations=3, verbose=True",
                COLORS["llm"], edge=COLORS["secondary"], fontsize=10, weight="bold")

    rounded_box(ax, 0.4, 1.5, 3.5, 1.6,
                "course_policy_tool\ncreate_retriever_tool\nChroma k=3 similarity",
                COLORS["tool_a"], fontsize=9)
    rounded_box(ax, 4.25, 1.5, 3.5, 1.6,
                "get_ticket_status\n@tool + docstring\nFAKE_TICKET_DATABASE",
                COLORS["tool_b"], fontsize=9)
    rounded_box(ax, 8.1, 1.5, 3.5, 1.6,
                "ChatOpenAI\ngpt-4o-mini\ntemp=0",
                COLORS["card"], fontsize=9)

    arrow(ax, 4.5, 3.5, 2.15, 3.1, COLORS["primary"])
    arrow(ax, 6.0, 3.5, 6.0, 3.1, COLORS["accent"])
    arrow(ax, 7.5, 3.5, 9.75, 3.1, COLORS["success"])

    rounded_box(ax, 0.5, 0.2, 11.0, 0.85,
                "Policy corpus: career, batch change, project, attendance, refund — inline Document objects",
                "#EEF2FF", edge=COLORS["primary"], fontsize=10)
    save(fig, "session41-03-course-support-agent.png")


def image_04():
    fig, ax = setup_fig(
        "Ingest Path Inside ragagent.py",
        "Same RAG prepare steps — now embedded before create_retriever_tool",
    )
    steps = [
        ("1. Documents", "5 inline policies\nmetadata source", COLORS["ingest"]),
        ("2. Split", "RecursiveCharacter\n500 / 80 overlap", COLORS["card"]),
        ("3. Embed", "text-embedding-3-small\nOpenAIEmbeddings", COLORS["query"]),
        ("4. Chroma", "course_policy_docs\ncollection", COLORS["chroma"]),
        ("5. Retriever", "similarity k=3\nas_retriever()", COLORS["card"]),
        ("6. Tool wrap", "create_retriever_tool\ncourse_policy_tool", COLORS["tool_a"]),
    ]
    for i, (title, body, face) in enumerate(steps):
        row, col = i // 3, i % 3
        x = 0.35 + col * 3.9
        y = 4.5 - row * 2.35
        rounded_box(ax, x, y, 3.5, 0.55, title, face, fontsize=9, weight="bold")
        rounded_box(ax, x, y - 1.35, 3.5, 1.2, body, COLORS["card"], fontsize=8.5)
        if col < 2:
            arrow(ax, x + 3.5, y - 0.55, x + 3.9, y - 0.55, COLORS["accent"])
        elif row == 0:
            arrow(ax, x + 1.75, y - 1.35, x + 1.75, y - 1.65, COLORS["accent"])

    rounded_box(ax, 0.5, 0.15, 11.0, 0.7,
                "Agent sees retriever tool like any @tool — arbitration uses name + description contract",
                "#EEF2FF", edge=COLORS["success"], fontsize=10)
    save(fig, "session41-04-ingest-to-retriever-tool.png")


def image_05():
    fig, ax = setup_fig(
        "chat_history vs agent_scratchpad",
        "Past turns vs current-run tool trace — different problems, different maintenance",
    )
    rounded_box(ax, 0.4, 3.2, 5.3, 2.8,
                "chat_history\n• Past user ↔ assistant messages\n• YOU append after each ask_agent\n"
                "• Turn 2: 'Status of it?' needs TKT from turn 1\n• MessagesPlaceholder optional=True",
                COLORS["query"], edge=COLORS["accent"], fontsize=9)
    rounded_box(ax, 6.3, 3.2, 5.3, 2.8,
                "agent_scratchpad\n• Tool inputs/outputs THIS run only\n• Executor fills automatically\n"
                "• Multi-step in ONE query\n• get_ticket_status then course_policy_tool\n• Required for tool-calling agents",
                COLORS["llm"], edge=COLORS["secondary"], fontsize=9)

    rounded_box(ax, 0.5, 1.0, 5.3, 1.5,
                "Bug: placeholder exists\nbut list never appended\n→ empty memory",
                COLORS["card"], edge=COLORS["danger"], fontsize=9)
    rounded_box(ax, 6.2, 1.0, 5.5, 1.5,
                "Fix: append HumanMessage +\nAIMessage after every invoke;\npass same list next turn",
                COLORS["chroma"], edge=COLORS["success"], fontsize=9)

    rounded_box(ax, 0.5, 0.15, 11.0, 0.65,
                "Desk remembers the notepad (history) and can still open the policy file on turn 3",
                "#EEF2FF", edge=COLORS["primary"], fontsize=10)
    save(fig, "session41-05-chat-history-vs-scratchpad.png")


def image_06():
    fig, ax = setup_fig(
        "Live Demo — Three Query Patterns",
        "verbose=True shows which tool fired in the terminal",
    )
    demos = [
        ("Query 1 — refund policy",
         "course_policy_tool\n7-day / 30-day rules\n'based on policy documents'",
         COLORS["tool_a"]),
        ("Query 2 — ticket status",
         "get_ticket_status\nTKT-51001\nreview + working days",
         COLORS["tool_b"]),
        ("Query 3 — multi-tool",
         "get_ticket_status first\nthen course_policy_tool\nbatch approved + refund rules",
         COLORS["chroma"]),
    ]
    for i, (title, body, face) in enumerate(demos):
        x = 0.4 + i * 3.9
        rounded_box(ax, x, 4.5, 3.5, 0.65, title, face, fontsize=9, weight="bold")
        rounded_box(ax, x, 2.3, 3.5, 2.0, body, COLORS["card"], fontsize=9)
        if i < 2:
            arrow(ax, x + 3.5, 3.3, x + 3.9, 3.3, COLORS["accent"])

    rounded_box(ax, 0.5, 0.5, 5.3, 1.4,
                "Multi-tool = two tools\nin ONE message",
                COLORS["query"], fontsize=10, weight="bold")
    rounded_box(ax, 6.2, 0.5, 5.5, 1.4,
                "Multi-turn = several messages;\nhistory supplies ticket ID",
                COLORS["llm"], fontsize=10, weight="bold")
    save(fig, "session41-06-live-demo-queries.png")


def image_07():
    fig, ax = setup_fig(
        "EvalPack — Bounded Agent Testing",
        "Small fixed test set with expected tools, keywords, and failure labels",
    )
    scenarios = [
        ("In-domain", "Refund policy?\n→ course_policy_tool\nkeywords: 7 days, refund", COLORS["tool_a"]),
        ("Tool-first", "Ticket TKT-51001?\n→ get_ticket_status\nkeywords: review", COLORS["tool_b"]),
        ("Out-of-domain", "Who won IPL?\n→ no tool\npolite refusal", COLORS["card"]),
        ("Multi-turn", "ID in turn 1\n'Status of it?' turn 2\n→ memory + tool", COLORS["query"]),
    ]
    for i, (title, body, face) in enumerate(scenarios):
        row, col = i // 2, i % 2
        x = 0.4 + col * 5.9
        y = 4.2 - row * 2.1
        rounded_box(ax, x, y, 5.5, 0.55, title, face, fontsize=10, weight="bold")
        rounded_box(ax, x, y - 1.5, 5.5, 1.35, body, COLORS["card"], fontsize=9)

    rounded_box(ax, 0.5, 0.15, 11.0, 0.75,
                "Each row: name, input, expected_tool, expected_keywords, failure_type — run after every code change",
                "#EEF2FF", edge=COLORS["secondary"], fontsize=10)
    save(fig, "session41-07-evalpack-scenarios.png")


def image_08():
    fig, ax = setup_fig(
        "Failure Signatures — What to Fix First",
        "EvalPack failure_type points to the right knob",
    )
    failures = [
        ("Wrong tool", "Policy → ticket tool\nFix: descriptions + prompt", COLORS["danger"]),
        ("Weak retrieval", "Right tool, wrong chunk\nFix: chunk k, overlap, MMR", COLORS["accent"]),
        ("Over-refusal", "Says can't help\nwhen policy covers it\nFix: loosen prompt", COLORS["card"]),
        ("Missing memory", "Turn 2 forgets ID\nFix: append chat_history", COLORS["query"]),
    ]
    for i, (title, fix, face) in enumerate(failures):
        x = 0.35 + i * 2.95
        rounded_box(ax, x, 3.8, 2.7, 0.6, title, face, fontsize=9, weight="bold")
        rounded_box(ax, x, 1.8, 2.7, 1.8, fix, COLORS["card"], fontsize=8.5)
        if i < 3:
            arrow(ax, x + 2.7, 2.7, x + 2.95, 2.7, COLORS["muted"])

    rounded_box(ax, 0.5, 0.25, 11.0, 1.2,
                "Debugging priority: wrong tool → tool contract | weak retrieval → chunk/search config\n"
                "over-refusal → prompt wording | missing memory → HumanMessage/AIMessage append",
                "#EEF2FF", edge=COLORS["primary"], fontsize=10)
    save(fig, "session41-08-failure-signatures.png")


if __name__ == "__main__":
    image_01()
    image_02()
    image_03()
    image_04()
    image_05()
    image_06()
    image_07()
    image_08()
