"""Generate Session 43 lecture note diagrams — Debugging and iterating LangChain agents."""
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
    "warn": "#FEF3C7",
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
        "From Evaluation to Iteration — Closing the Debug Loop",
        "Previous harness finds failures; today you patch, tune, and measure",
    )
    steps = [
        ("Eval JSON\ntest cases", COLORS["ingest"]),
        ("Runner +\ntraces", COLORS["card"]),
        ("Failure\nclass", COLORS["warn"]),
        ("Prompt / tool /\nretrieval fix", COLORS["query"]),
        ("Quality metrics\n+ ship bar", COLORS["chroma"]),
    ]
    for i, (label, face) in enumerate(steps):
        x = 0.35 + i * 2.35
        rounded_box(ax, x, 3.8, 2.1, 1.35, label, face, fontsize=8.5, weight="bold")
        if i < len(steps) - 1:
            arrow(ax, x + 2.1, 4.45, x + 2.35, 4.45, COLORS["accent"])

    rounded_box(ax, 0.5, 1.6, 5.3, 1.7,
                "Yesterday: WHAT broke?\nresults.csv + failure traces\nWrong tool, weak retrieval",
                COLORS["card"], edge=COLORS["danger"], fontsize=9)
    rounded_box(ax, 6.2, 1.6, 5.3, 1.7,
                "Today: HOW to fix?\nTargeted patches, not guesswork\nOne knob at a time",
                COLORS["card"], edge=COLORS["success"], fontsize=9)
    rounded_box(ax, 0.5, 0.25, 11.0, 0.95,
                "Ship agents that improve with evidence — not random prompt rewrites every Friday",
                "#EEF2FF", edge=COLORS["secondary"], fontsize=10, weight="bold")
    save(fig, "session43-01-eval-to-iteration-loop.png")


def image_02():
    fig, ax = setup_fig(
        "Simple App vs Agent Workflow Debugging",
        "Input-output checks are not enough when tools and retrieval sit in the middle",
    )
    rounded_box(ax, 0.4, 3.5, 5.0, 2.4,
                "Traditional app\nOne input → one output\n2 + 2 must equal 4\nEasy pass / fail",
                COLORS["card"], edge=COLORS["success"], fontsize=9)
    rounded_box(ax, 6.5, 3.5, 5.1, 2.4,
                "Agentic workflow\nUser → LLM → tool → retrieval\n→ maybe another tool → answer\nMany failure points",
                COLORS["ingest"], edge=COLORS["danger"], fontsize=9)

    mid_steps = ["Prompt", "Tool pick", "Arguments", "Retrieval", "Final text"]
    for i, step in enumerate(mid_steps):
        x = 0.55 + i * 2.25
        rounded_box(ax, x, 1.5, 2.0, 0.85, step, COLORS["card"], fontsize=8.5)
        if i < len(mid_steps) - 1:
            arrow(ax, x + 2.0, 1.92, x + 2.25, 1.92, COLORS["accent"])

    rounded_box(ax, 0.5, 0.2, 11.0, 0.85,
                "Debug WHICH step failed — do not blame the model first",
                COLORS["warn"], edge=COLORS["accent"], fontsize=10, weight="bold")
    save(fig, "session43-02-simple-io-vs-agent-workflow.png")


def image_03():
    fig, ax = setup_fig(
        "Final Answer vs Trajectory Debugging",
        "Professional teams inspect the full path, not only the last sentence",
    )
    rounded_box(ax, 0.4, 3.6, 5.2, 2.3,
                "Final-answer debug\nCompare expected text\nvs actual reply only\nMisses wrong tool route",
                COLORS["card"], edge=COLORS["danger"], fontsize=9)
    rounded_box(ax, 6.4, 3.6, 5.2, 2.3,
                "Trajectory debug\nWhich tools fired?\nWhat was retrieved?\nShould it have refused?",
                COLORS["ingest"], edge=COLORS["success"], fontsize=9)

    rounded_box(ax, 0.5, 1.5, 11.0, 1.6,
                "Delivery analogy: reading 'not delivered' on the app\nvs tracking warehouse → hub → rider\n\n"
                "Eval harness traces = flight recorder for each test case",
                "#EEF2FF", edge=COLORS["secondary"], fontsize=9.5)

    rounded_box(ax, 0.5, 0.2, 11.0, 0.85,
                "GST question routed to policy search? Trajectory shows it before the polite wrong answer",
                COLORS["warn"], edge=COLORS["accent"], fontsize=10)
    save(fig, "session43-03-trajectory-vs-final-answer.png")


def image_04():
    fig, ax = setup_fig(
        "Failure Class → Remediation Map",
        "Name the defect category first, then apply the matching small fix",
    )
    pairs = [
        ("Wrong tool", "Tool patch +\nprompt examples", COLORS["danger"]),
        ("Missing tool call", "Prompt patch:\nmust call tool", COLORS["warn"]),
        ("Weak retrieval", "Tune K, search,\nchunk size", COLORS["ingest"]),
        ("Hallucination", "Grounding rule +\nbetter chunks", COLORS["query"]),
        ("Tool loop", "max_iterations\ncap", COLORS["llm"]),
        ("Slow / costly", "Cache, fewer\ncalls, smaller K", COLORS["chroma"]),
    ]
    for i, (failure, fix, edge) in enumerate(pairs):
        row, col = i // 2, i % 2
        x = 0.4 + col * 6.0
        y = 4.5 - row * 1.55
        rounded_box(ax, x, y, 2.6, 0.95, failure, COLORS["card"], edge=edge, fontsize=9, weight="bold")
        arrow(ax, x + 2.6, y + 0.48, x + 3.0, y + 0.48, COLORS["accent"])
        rounded_box(ax, x + 3.0, y, 2.5, 0.95, fix, COLORS["card"], edge=COLORS["success"], fontsize=8.5)

    rounded_box(ax, 0.5, 0.2, 11.0, 0.75,
                "One controlled change at a time — re-run full eval set to catch regressions",
                "#EEF2FF", edge=COLORS["primary"], fontsize=10, weight="bold")
    save(fig, "session43-04-failure-class-remediation.png")


def image_05():
    fig, ax = setup_fig(
        "Retrieval Tuning Demo — Same Query, Different Chunks",
        "Electronics return window: chunk_size 50 failed; chunk_size 150 succeeded",
    )
    rounded_box(ax, 0.4, 4.0, 5.3, 1.5,
                "chunk_size = 50, overlap = 10\n59 tiny chunks\nSearch hits 'electronics'\nin chunk 2 only",
                COLORS["card"], edge=COLORS["danger"], fontsize=9)
    rounded_box(ax, 6.3, 4.0, 5.3, 1.5,
                "chunk_size = 150, overlap = 20\n21 richer chunks\nCategory + 7-day rule\nin same context",
                COLORS["chroma"], edge=COLORS["success"], fontsize=9)

    rounded_box(ax, 0.5, 2.3, 5.5, 1.35,
                "Chunk 2: mentions electronics\nbut NOT return window",
                COLORS["warn"], edge=COLORS["danger"], fontsize=9)
    rounded_box(ax, 6.0, 2.3, 5.5, 1.35,
                "Chunk 4 had '7 days'\nbut was never retrieved\nwith tiny splits",
                COLORS["warn"], edge=COLORS["danger"], fontsize=9)

    arrow(ax, 2.75, 3.95, 2.75, 3.65, COLORS["danger"])
    ax.text(2.75, 3.75, "I don't know", ha="center", fontsize=9, color=COLORS["danger"], weight="bold")
    arrow(ax, 8.95, 3.95, 8.95, 3.65, COLORS["success"])
    ax.text(8.95, 3.75, "7 days ✓", ha="center", fontsize=9, color=COLORS["success"], weight="bold")

    rounded_box(ax, 0.5, 0.85, 11.0, 1.1,
                "Query: What is the return window for electronics items?\n"
                "Same files, same app — only ingest tuning changed the answer",
                COLORS["ingest"], edge=COLORS["primary"], fontsize=10, weight="bold")
    save(fig, "session43-05-chunk-tuning-electronics-demo.png")


def main():
    image_01()
    image_02()
    image_03()
    image_04()
    image_05()
    print("All Session 43 images generated.")


if __name__ == "__main__":
    main()
