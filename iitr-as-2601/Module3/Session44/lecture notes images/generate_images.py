"""Generate Session 44 lecture note diagrams — LLM Internals for Designers."""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle

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
    "chunk4": "#D1FAE5",
    "chunk5": "#FEE2E2",
    "thought": "#E0F2FE",
    "action": "#FEF3C7",
    "obs": "#D1FAE5",
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
        "LLM Internals for Designers",
        "RAG · memory · tools — all compete for one fixed context window",
    )
    rounded_box(ax, 0.4, 4.0, 3.5, 1.6, "RAG chunks\nretrieved text", COLORS["chunk1"])
    rounded_box(ax, 4.1, 4.0, 3.5, 1.6, "Chat history\nsaved turns", COLORS["chunk2"])
    rounded_box(ax, 7.8, 4.0, 3.8, 1.6, "Tool observations\nThought / Action logs", COLORS["chunk3"])
    rounded_box(ax, 0.4, 1.8, 11.2, 1.8,
                "CONTEXT WINDOW = shared tiffin box\n"
                "Tokens · billing · latency · truncation — designer knobs, not model engineering",
                "#EEF2FF", edge=COLORS["secondary"], fontsize=10, weight="bold")
    for x in [2.15, 5.85, 9.7]:
        arrow(ax, x, 4.0, 6.0, 3.6, COLORS["accent"])
    save(fig, "session44-01-designer-llm-internals.png")


def image_02():
    fig, ax = setup_fig("Tokens vs Words", "What you type ≠ what the API bills and limits")
    rounded_box(ax, 0.4, 3.8, 5.3, 2.2,
                "On your screen\n\n'Namaste, how are you?'\n= 4 words (looks small)",
                COLORS["chunk1"], edge=COLORS["primary"], fontsize=9.5)
    rounded_box(ax, 6.3, 3.8, 5.3, 2.2,
                "What API measures\n\n~6–8 tokens after tokenisation\n+ ₹ per 1,000 tokens",
                COLORS["chunk3"], edge=COLORS["accent"], fontsize=9.5)
    ax.text(5.85, 4.9, "≠", fontsize=20, weight="bold", ha="center", color=COLORS["danger"])
    rounded_box(ax, 0.4, 0.9, 3.5, 2.2, "Short English\n~1 token/word", COLORS["obs"], fontsize=9)
    rounded_box(ax, 4.1, 0.9, 3.5, 2.2, "Long URL / JSON\nmany tokens", COLORS["chunk5"], edge=COLORS["danger"], fontsize=9)
    rounded_box(ax, 7.8, 0.9, 3.8, 2.2, "Hindi + English mix\ntokens > words", COLORS["chunk2"], fontsize=9)
    save(fig, "session44-02-tokens-vs-words.png")


def image_03():
    fig, ax = setup_fig("Context Window Budget", "Input + output share one ceiling — measure before you ship")
    blocks = [
        ("System rules\n~200 tok", 0.55, COLORS["chunk1"]),
        ("RAG chunks\n~900 tok", 0.45, COLORS["chunk2"]),
        ("Chat history\n~1,400 tok", 0.65, COLORS["chunk3"]),
        ("Tool logs\n~2,000 tok", 0.85, COLORS["action"]),
        ("User question\n~30 tok", 0.25, COLORS["obs"]),
        ("Output slot\n~1,000 tok", 0.50, COLORS["success"]),
    ]
    y = 1.2
    for label, h, face in blocks:
        rounded_box(ax, 2.0, y, 8.0, h, label, face, fontsize=9.5, weight="bold")
        y += h + 0.08
    rounded_box(ax, 0.4, 1.0, 1.4, y - 1.0, "8k\nwindow", COLORS["card"], edge=COLORS["danger"], fontsize=10, weight="bold")
    ax.add_patch(Rectangle((0.4, 1.0), 1.4, y - 1.0, linewidth=2, edgecolor=COLORS["danger"], facecolor="none", linestyle="--"))
    rounded_box(ax, 0.4, 0.2, 11.2, 0.65,
                "Overflow → silent truncation or cut-off answers · budget with tiktoken",
                "#FFFBEB", edge=COLORS["accent"], fontsize=9)
    save(fig, "session44-03-context-window-budget.png")


def image_04():
    fig, ax = setup_fig("RAG Token Budget", "top_k and chunk size compete — hard-cap retrieval block")
    rounded_box(ax, 0.4, 4.3, 2.8, 1.4, "Vector DB\n4 chunks retrieved", COLORS["chunk1"])
    rounded_box(ax, 3.4, 4.3, 3.2, 1.4, "Chunk 1 + 2\nfit in 600 tok", COLORS["success"])
    rounded_box(ax, 6.8, 4.3, 2.5, 1.4, "Chunk 3\nDROPPED", COLORS["chunk5"], edge=COLORS["danger"])
    rounded_box(ax, 9.5, 4.3, 2.1, 1.4, "Chunk 4\nDROPPED", COLORS["chunk5"], edge=COLORS["danger"])
    arrow(ax, 3.2, 5.0, 3.4, 5.0, COLORS["accent"])
    arrow(ax, 6.6, 5.0, 6.8, 5.0, COLORS["danger"])
    rounded_box(ax, 0.4, 2.0, 5.5, 1.8,
                "MAX_CONTEXT_TOKENS = 600\nShort source_id labels save tokens",
                COLORS["card"], edge=COLORS["primary"], fontsize=9.5)
    rounded_box(ax, 6.0, 2.0, 5.6, 1.8,
                "More chunks ≠ better answers\nIrrelevant hits add noise + eat history space",
                COLORS["card"], edge=COLORS["secondary"], fontsize=9.5)
    rounded_box(ax, 0.4, 0.35, 11.2, 1.3,
                "Progressive disclosure: start low top_k · expand only if answer is thin",
                "#EEF2FF", edge=COLORS["secondary"], fontsize=9.5)
    save(fig, "session44-04-rag-token-budget.png")


def image_05():
    fig, ax = setup_fig("Memory Truncation", "File on disk remembers everything · model sees only the tail")
    rounded_box(ax, 0.4, 3.8, 5.3, 2.3,
                "chat_history.json on disk\n\nTurn 1: grounding rule\nTurn 2–7: full debate\n(hundreds possible)",
                COLORS["chunk1"], edge=COLORS["primary"], fontsize=9)
    rounded_box(ax, 6.3, 3.8, 5.3, 2.3,
                "Sent to model (MAX_MESSAGES=4)\n\nOnly last 4 messages\nRule in Turn 1 = DROPPED",
                COLORS["chunk5"], edge=COLORS["danger"], fontsize=9)
    arrow(ax, 5.7, 4.9, 6.3, 4.9, COLORS["accent"])
    ax.text(5.85, 5.2, "window", fontsize=8, ha="center", color=COLORS["muted"])
    rounded_box(ax, 0.4, 0.9, 11.2, 2.2,
                "User-visible: bot 'forgets' answer-only-from-report rule\n"
                "Fix: re-inject rules · summary memory · user banner when truncated",
                COLORS["card"], edge=COLORS["success"], fontsize=9.5, weight="bold")
    save(fig, "session44-05-truncation-memory.png")


def image_06():
    fig, ax = setup_fig("Temperature & Determinism", "Low = stable facts · High = creative variation")
    rounded_box(ax, 0.4, 3.6, 5.3, 2.5,
                "temperature = 0\n\nSame prompt → same answer\n(3 runs match)\n\nRAG · policy · tool planning",
                COLORS["obs"], edge=COLORS["success"], fontsize=9.5)
    rounded_box(ax, 6.3, 3.6, 5.3, 2.5,
                "temperature = 0.8\n\nSame prompt → different wording\n(3 runs vary)\n\nSMS banners · brainstorm",
                COLORS["chunk3"], edge=COLORS["accent"], fontsize=9.5)
    rounded_box(ax, 0.4, 1.0, 3.5, 2.0,
                "seed = 42\n(reproducible QA tests)",
                COLORS["chunk2"], edge=COLORS["secondary"], fontsize=9)
    rounded_box(ax, 4.1, 1.0, 7.5, 2.0,
                "Per-feature settings beat one global dial\nRefund bot = 0 · Festive SMS = higher",
                COLORS["card"], edge=COLORS["primary"], fontsize=9.5, weight="bold")
    save(fig, "session44-06-temperature-determinism.png")


def image_07():
    fig, ax = setup_fig("Multi-Turn Agent Token Growth", "Each ReAct lap adds tokens — randomness multiplies too")
    laps = [
        ("Lap 1", "Thought + search\nobservation", COLORS["thought"]),
        ("Lap 2", "Thought + python\nobservation", COLORS["action"]),
        ("Lap 3", "Thought only", COLORS["chunk2"]),
        ("Lap 4", "Final answer", COLORS["success"]),
    ]
    x = 0.4
    for i, (title, body, face) in enumerate(laps):
        rounded_box(ax, x, 4.5, 2.6, 0.7, title, face, fontsize=9, weight="bold")
        rounded_box(ax, x, 3.0, 2.6, 1.3, body, COLORS["card"], edge=face, fontsize=8.5)
        backpack_h = 0.5 + i * 0.35
        rounded_box(ax, x + 0.3, 1.5, 2.0, backpack_h, f"tokens\n+{ (i+1)*400 }", face, fontsize=8)
        if i < 3:
            arrow(ax, x + 2.6, 4.85, x + 2.9, 4.85, COLORS["accent"])
        x += 2.9
    rounded_box(ax, 0.4, 0.25, 11.2, 1.0,
                "Cap observations · max_iterations · temperature=0 for tool chains · re-inject rules after turn 20",
                "#FFFBEB", edge=COLORS["accent"], fontsize=9)
    save(fig, "session44-07-agent-loop-token-growth.png")


def image_08():
    fig, ax = setup_fig("End-to-End Request Anatomy", "Typical RAG + memory + agent call ≈ 5,530 tokens")
    rows = [
        ("System + grounding", 200, COLORS["chunk1"]),
        ("RAG top_k=3", 900, COLORS["chunk2"]),
        ("Last 6 chat turns", 1400, COLORS["chunk3"]),
        ("ReAct scratchpad", 2000, COLORS["action"]),
        ("User question", 30, COLORS["obs"]),
        ("Reserved output", 1000, COLORS["success"]),
    ]
    y = 4.8
    for label, tok, face in rows:
        w = tok / 5530 * 9.5 + 1.5
        tok_label = f"{tok:,}" if tok >= 1000 else str(tok)
        rounded_box(ax, 0.4, y, w, 0.55, f"{label}  ~{tok_label} tok", face, fontsize=8.5)
        y -= 0.62
    rounded_box(ax, 0.4, 0.35, 11.2, 1.2,
                "Designer job: sum < provider window with 10–15% safety margin · update table before adding tools",
                "#EEF2FF", edge=COLORS["secondary"], fontsize=9.5, weight="bold")
    ax.text(10.5, 5.5, "TOTAL\n~5,530", fontsize=10, weight="bold", ha="right", color=COLORS["primary"])
    save(fig, "session44-08-end-to-end-anatomy.png")


if __name__ == "__main__":
    image_01()
    image_02()
    image_03()
    image_04()
    image_05()
    image_06()
    image_07()
    image_08()
