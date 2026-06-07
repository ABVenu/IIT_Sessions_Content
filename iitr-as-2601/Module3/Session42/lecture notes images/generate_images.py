"""Generate Session 42 lecture note diagrams — Memory & Control Flow (Tesla RAG continuity)."""
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
    "overlap": "#FDE68A",
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
        "One-Shot RAG vs Multi-Turn Chat With Memory",
        "Previous session: each Tesla question alone  |  Today: follow-ups like 'And in 2023?'",
    )
    rounded_box(ax, 0.4, 3.2, 5.3, 2.4,
                "WITHOUT MEMORY (Session 41 Gradio)\n\nQ1: Revenue in 2022? → answer\nQ2: And in 2023? → forgets context\nMay search wrong passages",
                COLORS["card"], edge=COLORS["danger"], fontsize=9.5)
    rounded_box(ax, 6.3, 3.2, 5.3, 2.4,
                "WITH MEMORY (Session 42)\n\nhistory holds 2022 revenue turn\nQ2: And in 2023? → full thread to RAG\nFollow-up understood in context",
                COLORS["card"], edge=COLORS["success"], fontsize=9.5)
    ax.text(5.85, 4.4, "vs", fontsize=14, weight="bold", ha="center", color=COLORS["accent"])
    rounded_box(ax, 0.4, 0.9, 11.2, 1.6,
                "Tesla analyst chat\nTurn 1: 'What is annual revenue in 2022?'  →  $96.77B\nTurn 2: 'And in 2023?'  →  needs history, not a fresh one-shot query",
                "#EEF2FF", edge=COLORS["secondary"], fontsize=10, weight="bold")
    save(fig, "session42-01-one-shot-vs-multi-turn.png")


def image_02():
    fig, ax = setup_fig("Short-Term vs Long-Term Memory", "Today's lab = JSON history for this session only")
    rounded_box(ax, 0.5, 3.5, 5.2, 2.3,
                "SHORT-TERM\n\nRunning chat list\nPython list + tesla_chat_history.json\nThis notebook session\nWaiter's notepad",
                COLORS["chunk1"], edge=COLORS["primary"], fontsize=10, weight="bold")
    rounded_box(ax, 6.3, 3.5, 5.2, 2.3,
                "LONG-TERM\n\nAcross weeks / sessions\nDatabase, user profile\nAnalyst returns next week\nLoyalty card file",
                COLORS["chunk3"], edge=COLORS["secondary"], fontsize=10, weight="bold")

    rows = [
        ("Duration", "This chat only", "Days to months"),
        ("Storage", "list + JSON", "DB / profile"),
        ("Today", "YES — main lab", "Later work"),
    ]
    for i, (label, st, lt) in enumerate(rows):
        y = 2.5 - i * 0.75
        rounded_box(ax, 0.5, y, 2.0, 0.55, label, COLORS["card"], fontsize=8, weight="bold")
        rounded_box(ax, 2.6, y, 3.1, 0.55, st, COLORS["chunk1"], fontsize=8)
        rounded_box(ax, 6.3, y, 5.2, 0.55, lt, COLORS["chunk3"], fontsize=8)
    save(fig, "session42-02-short-vs-long-term-memory.png")


def image_03():
    fig, ax = setup_fig("Conversation History — List of Messages", "Always append user first, then assistant")
    roles = [
        ("user", "What is annual revenue in 2022?", COLORS["chunk1"]),
        ("assistant", "2022 revenue: $96.77B (from chunks)", COLORS["success"]),
        ("user", "And in 2023?", COLORS["chunk1"]),
        ("assistant", "[2023 figure from RAG]", COLORS["success"]),
    ]
    for i, (role, content, face) in enumerate(roles):
        y = 5.0 - i * 1.15
        rounded_box(ax, 0.5, y, 1.6, 0.85, role, face, edge=COLORS["primary"], fontsize=9, weight="bold")
        rounded_box(ax, 2.2, y, 9.3, 0.85, content, COLORS["card"], fontsize=9)
        if i < len(roles) - 1:
            arrow(ax, 1.3, y, 1.3, y - 0.3, COLORS["muted"])

    rounded_box(ax, 0.5, 0.25, 11.0, 0.85,
                "Common mistake: send only latest message → Turn 2 loses 'revenue' and '2022' context",
                "#FEE2E2", edge=COLORS["danger"], fontsize=9.5)
    save(fig, "session42-03-conversation-history-list.png")


def image_04():
    fig, ax = setup_fig("Persist and Reload — tesla_chat_history.json", "Survives notebook restart and next cell")
    items = [
        (0.35, 2.1, "history list\n(in RAM)", COLORS["chunk1"]),
        (2.55, 2.2, "save_history()\njson.dump", COLORS["chunk2"]),
        (4.85, 2.3, "tesla_chat_history.json\non disk", COLORS["chunk3"]),
        (7.25, 2.2, "load_history()\njson.load", COLORS["chunk2"]),
        (9.55, 2.1, "history list\n(reloaded)", COLORS["success"]),
    ]
    y = 4.0
    for x, w, txt, face in items:
        rounded_box(ax, x, y, w, 1.3, txt, face, fontsize=8.5, weight="bold")

    for i in range(len(items) - 1):
        x1, w1, _, _ = items[i]
        x2, _, _, _ = items[i + 1]
        arrow(ax, x1 + w1, y + 0.65, x2, y + 0.65, COLORS["accent"])

    rounded_box(ax, 0.4, 2.0, 5.5, 1.5, "append_turn()\nuser → assistant → save_history()\nafter EVERY turn", COLORS["card"], edge=COLORS["accent"], fontsize=10)
    rounded_box(ax, 6.2, 2.0, 5.4, 1.5, "FileNotFoundError?\n→ return []\nfirst run safe default", COLORS["card"], edge=COLORS["secondary"], fontsize=10)
    rounded_box(ax, 0.4, 0.2, 11.2, 1.4,
                "Clinic desk writes visit notes in a folder — tomorrow's staff reads before calling",
                "#FFFBEB", edge=COLORS["accent"], fontsize=9)
    save(fig, "session42-04-persist-reload-json.png")


def image_05():
    fig, ax = setup_fig("Pass Memory Into rag_answer", "build_question_with_memory → rag_answer(query, retriever)")
    rounded_box(ax, 0.4, 4.5, 3.0, 1.4, "history list\nprior turns", COLORS["chunk1"])
    rounded_box(ax, 3.6, 4.5, 3.0, 1.4, "new_message\n'And in 2023?'", COLORS["chunk3"])
    rounded_box(ax, 6.8, 4.5, 4.8, 1.4, "build_question_with_memory\nfull thread as one query", COLORS["chunk2"], edge=COLORS["secondary"])
    arrow(ax, 3.4, 5.2, 3.6, 5.2)
    arrow(ax, 6.6, 5.2, 6.8, 5.2)

    rounded_box(ax, 2.0, 2.5, 4.0, 1.3, "rag_answer(full_question, retriever)\nTesla_db — reuse from prior lab", COLORS["success"], edge=COLORS["success"], fontsize=10, weight="bold")
    arrow(ax, 9.2, 4.5, 4.0, 3.85, COLORS["accent"])

    rounded_box(ax, 6.5, 2.5, 5.1, 1.3, "append_turn + save\nupdate tesla_chat_history.json", COLORS["card"], edge=COLORS["accent"], fontsize=10)
    arrow(ax, 4.0, 2.5, 6.5, 3.15, COLORS["primary"])

    rounded_box(ax, 0.4, 0.25, 11.2, 1.5,
                "Analyst re-reads entire email thread — not just the last sentence\nTurn 2 works because 2022 revenue context is in the query block",
                "#EEF2FF", edge=COLORS["secondary"], fontsize=9.5)
    save(fig, "session42-05-memory-into-rag.png")


def image_06():
    fig, ax = setup_fig("Loop Termination — Stop Rules", "MAX_STEPS + task done + quit / exit / stop")
    rounded_box(ax, 0.4, 4.2, 3.4, 1.5, "run_chat_turn()\nwhile step < MAX_STEPS", COLORS["chunk2"], edge=COLORS["primary"], fontsize=10, weight="bold")
    arrow(ax, 3.8, 4.95, 4.2, 4.95)

    rules = [
        ("MAX_STEPS = 5", "Hard ceiling\nnon-negotiable", COLORS["danger"]),
        ("Task done", "break after\nrag_answer OK", COLORS["success"]),
        ("STOP_WORDS", "quit / exit / stop\npolite goodbye", COLORS["accent"]),
    ]
    for i, (title, body, edge) in enumerate(rules):
        x = 4.2 + i * 2.55
        rounded_box(ax, x, 4.5, 2.3, 0.7, title, COLORS["card"], edge=edge, fontsize=9, weight="bold")
        rounded_box(ax, x, 3.5, 2.3, 0.85, body, COLORS["card"], edge=edge, fontsize=8.5)

    rounded_box(ax, 0.4, 1.0, 5.5, 2.0,
                "WITHOUT stop rule\n\nLoop searches report\nforever → API bill rises\nUser abandons chat",
                COLORS["card"], edge=COLORS["danger"], fontsize=9.5)
    rounded_box(ax, 6.0, 1.0, 5.6, 2.0,
                "WITH stop rule\n\nstep 1: RAG → break\nor hit MAX_STEPS → polite msg\nATM: 3 PIN tries then stop",
                COLORS["card"], edge=COLORS["success"], fontsize=9.5)
    save(fig, "session42-06-loop-termination.png")


def image_07():
    fig, ax = setup_fig("User-Visible Error Handling", "try/except around rag_answer — friendly text, not traceback")
    rounded_box(ax, 0.5, 3.8, 5.2, 2.3,
                "BAD\n\nexcept Exception:\n  return str(e)\n\nUser sees:\nConnectionRefusedError: ...",
                COLORS["card"], edge=COLORS["danger"], fontsize=9)
    rounded_box(ax, 6.3, 3.8, 5.2, 2.3,
                "GOOD\n\nexcept Exception:\n  return friendly msg\n\nUser sees:\n'Search unavailable.\nTry again in a minute.'",
                COLORS["card"], edge=COLORS["success"], fontsize=9)

    errors = [
        ("API down", "Search unavailable...", COLORS["danger"]),
        ("Empty index", "Run setup first", COLORS["accent"]),
        ("Blank input", "Please type a question", COLORS["secondary"]),
    ]
    for i, (etype, msg, edge) in enumerate(errors):
        x = 0.5 + i * 3.85
        rounded_box(ax, x, 0.9, 3.5, 1.8, f"{etype}\n→ {msg}", COLORS["card"], edge=edge, fontsize=8.5)
    save(fig, "session42-07-error-handling.png")


def image_08():
    fig, ax = setup_fig("Notebook Demo — Memory + Control Flow on Tesla RAG", "Reuse retriever + rag_answer; add today's cells only")
    stages = [
        ("load_history", "tesla_chat_history.json", COLORS["chunk1"]),
        ("run_chat_turn", "MAX_STEPS + STOP_WORDS", COLORS["chunk2"]),
        ("build_question", "history + new msg", COLORS["chunk3"]),
        ("rag_answer", "Tesla_db retriever", COLORS["success"]),
        ("append_turn", "save JSON", COLORS["chunk1"]),
    ]
    for i, (title, body, face) in enumerate(stages):
        x = 0.25 + i * 2.35
        rounded_box(ax, x, 3.8, 2.15, 0.65, title, face, fontsize=7.5, weight="bold")
        rounded_box(ax, x, 2.5, 2.15, 1.1, body, COLORS["card"], fontsize=8)
        if i < len(stages) - 1:
            arrow(ax, x + 2.15, 4.15, x + 2.35, 4.15, COLORS["accent"])

    rounded_box(ax, 0.4, 0.9, 5.5, 1.3,
                "Turn 1: Revenue in 2022?\n→ answer + save",
                COLORS["card"], edge=COLORS["primary"], fontsize=9.5)
    rounded_box(ax, 6.0, 0.9, 5.6, 1.3,
                "Turn 2: And in 2023?\nload_history → context intact",
                COLORS["card"], edge=COLORS["success"], fontsize=9.5)
    arrow(ax, 5.9, 1.55, 6.0, 1.55, COLORS["accent"])
    save(fig, "session42-08-notebook-demo-flow.png")


if __name__ == "__main__":
    image_01()
    image_02()
    image_03()
    image_04()
    image_05()
    image_06()
    image_07()
    image_08()
