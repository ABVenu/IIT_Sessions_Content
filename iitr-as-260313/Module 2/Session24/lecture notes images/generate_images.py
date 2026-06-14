"""Generate Session 24 (Tool Integration in AI Agents) lecture note diagrams — ShopKart theme."""
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
    "returns": "#DBEAFE",
    "shipping": "#E9D5FF",
    "warranty": "#FFEDD5",
    "refunds": "#D1FAE5",
    "warn": "#FDE68A",
    "brain": "#E9D5FF",
    "runtime": "#DBEAFE",
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
        "Function Calling — Brain Chooses, Runtime Executes",
        "The model never calls HTTP directly · your Python runs the tool",
    )
    rounded_box(ax, 0.5, 3.2, 4.5, 2.3,
                "LLM (GROQ)\n\nReads tool descriptions\nEmits tool_calls\n+ JSON arguments",
                COLORS["brain"], edge=COLORS["secondary"], fontsize=9.5, weight="bold")
    arrow(ax, 5.0, 4.35, 6.5, 4.35, COLORS["accent"])
    rounded_box(ax, 6.5, 3.2, 5.0, 2.3,
                "PYTHON RUNTIME\n\nRuns search_shopkart_policy\nRuns get_city_weather\nReturns JSON to model",
                COLORS["runtime"], edge=COLORS["primary"], fontsize=9.5, weight="bold")
    rounded_box(ax, 0.5, 0.45, 11.0, 1.8,
                "Contrast previous lab: you hard-coded weather GET every time\n"
                "Today: model picks policy vs weather (or both) from the question",
                COLORS["warn"], edge=COLORS["accent"], fontsize=9.5)
    save(fig, "session24-01-function-calling.png")


def image_02():
    fig, ax = setup_fig(
        "Tool Execution Loop — ShopKart Agent",
        "Repeat until the model stops requesting tools",
    )
    steps = [
        ("USER\nquestion", COLORS["card"], 0.35),
        ("MODEL\npick tools", COLORS["brain"], 2.55),
        ("RUN\nPython fn", COLORS["runtime"], 4.75),
        ("JSON\nresult", COLORS["refunds"], 6.95),
        ("REPLY\ngrounded", COLORS["success"], 9.15),
    ]
    for i, (txt, face, x) in enumerate(steps):
        rounded_box(ax, x, 3.4, 1.95, 1.6, txt, face, fontsize=8.5, weight="bold")
        if i < 4:
            arrow(ax, x + 1.95, 4.2, steps[i + 1][2], 4.2, COLORS["primary"])
    arrow(ax, 9.15, 3.4, 2.55, 3.4, COLORS["accent"])
    rounded_box(ax, 0.5, 0.45, 11.0, 2.0,
                "while tool_calls: append results → call Groq again\n"
                "Safe errors: {error: Weather API failed} → no invented rain in final answer",
                COLORS["warn"], edge=COLORS["danger"], fontsize=9.5, weight="bold")
    save(fig, "session24-02-tool-execution-loop.png")


def image_03():
    fig, ax = setup_fig(
        "ShopKart Agent — Two Registered Tools",
        "Clear names and descriptions help the model route correctly",
    )
    rounded_box(ax, 3.8, 4.5, 4.4, 1.2,
                "SHOPKART TOOL AGENT  (Groq + tools=)",
                COLORS["card"], edge=COLORS["secondary"], fontsize=10, weight="bold")
    rounded_box(ax, 0.5, 2.3, 5.0, 1.8,
                "search_shopkart_policy\n\nReturns · Shipping ·\nWarranty · Refunds excerpts",
                COLORS["returns"], edge=COLORS["primary"], fontsize=9, weight="bold")
    rounded_box(ax, 6.5, 2.3, 5.0, 1.8,
                "get_city_weather\n\nOpen-Meteo GET\n temperature_c · weather_code",
                COLORS["shipping"], edge=COLORS["accent"], fontsize=9, weight="bold")
    arrow(ax, 5.5, 4.5, 3.0, 4.1, COLORS["primary"])
    arrow(ax, 6.5, 4.5, 9.0, 4.1, COLORS["primary"])
    rounded_box(ax, 0.5, 0.4, 11.0, 1.5,
                "Combined query: express Delhi + rain → both tools → one Groq reply\n"
                "Swap inline policy map for Chroma retriever when extending the project",
                COLORS["warn"], edge=COLORS["success"], fontsize=9.5)
    save(fig, "session24-03-shopkart-two-tools.png")


def image_04():
    fig, ax = setup_fig(
        "API Wrapped as a Tool",
        "Session 23 GET helper lives inside get_city_weather",
    )
    rounded_box(ax, 0.4, 3.5, 3.0, 1.8,
                "MODEL\nrequests\nget_city_weather",
                COLORS["brain"], edge=COLORS["secondary"], fontsize=9, weight="bold")
    arrow(ax, 3.4, 4.4, 4.3, 4.4, COLORS["accent"])
    rounded_box(ax, 4.3, 3.3, 3.2, 2.0,
                "PYTHON WRAPPER\n\nrequests.get\nstatus == 200?\nextract JSON fields",
                COLORS["runtime"], edge=COLORS["primary"], fontsize=9, weight="bold")
    arrow(ax, 7.5, 4.4, 8.4, 4.4, COLORS["primary"])
    rounded_box(ax, 8.4, 3.5, 3.2, 1.8,
                "JSON TO MODEL\n{city, temperature_c}",
                COLORS["refunds"], edge=COLORS["success"], fontsize=9, weight="bold")
    rounded_box(ax, 0.5, 0.45, 11.0, 2.0,
                "Closes Module 2: RAG evaluation → API/JSON foundation → tool integration\n"
                "Upcoming: LangChain AgentExecutor automates this same loop",
                COLORS["card"], edge=COLORS["secondary"], fontsize=9.5)
    save(fig, "session24-04-api-as-tool-wrapper.png")


if __name__ == "__main__":
    image_01()
    image_02()
    image_03()
    image_04()
