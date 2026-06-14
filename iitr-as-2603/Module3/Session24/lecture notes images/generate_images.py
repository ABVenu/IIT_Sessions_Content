"""Generate Session 24 lecture note diagrams — Prompt Engineering."""
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
    "system": "#DBEAFE",
    "user": "#FFEDD5",
    "zero": "#E0F2FE",
    "few": "#E9D5FF",
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


def image_01_system_vs_user():
    fig, ax = setup_fig(
        "System Prompt vs User Prompt",
        "System = backstage rules set once  |  User = live message each turn",
    )
    rounded_box(ax, 0.4, 3.8, 5.3, 2.0,
                "SYSTEM PROMPT (set once)\n\nPersona: library assistant Meera\nScope: timings, fines only\nTone: short sentences",
                COLORS["system"], edge=COLORS["primary"], fontsize=9.5, weight="bold")
    rounded_box(ax, 6.3, 3.8, 5.3, 2.0,
                "USER PROMPT (each turn)\n\n\"What is the fine for\na late book return?\"",
                COLORS["user"], edge=COLORS["accent"], fontsize=9.5, weight="bold")
    arrow(ax, 5.7, 4.8, 6.3, 4.8, COLORS["accent"])
    rounded_box(ax, 2.0, 1.8, 8.0, 1.5,
                "LLM reads BOTH → reply stays on scope,\nuses library tone, answers the live question",
                COLORS["success"], edge=COLORS["success"], fontsize=10, weight="bold")
    rounded_box(ax, 0.4, 0.35, 11.2, 1.2,
                "Common mistake: long rules only in first user message — they get buried in chat history",
                COLORS["card"], edge=COLORS["danger"], fontsize=9)
    save(fig, "session24-01-system-vs-user-prompt.png")


def image_02_zero_vs_few_shot():
    fig, ax = setup_fig(
        "Zero-Shot vs Few-Shot Prompting",
        "Zero-shot = instruction only  |  Few-shot = show examples first, then the real task",
    )
    rounded_box(ax, 0.4, 3.5, 5.3, 2.3,
                "ZERO-SHOT\n\n\"Write a product tagline\nfor noise-cancelling headphones\"\n\nNo examples given",
                COLORS["zero"], edge=COLORS["primary"], fontsize=9.5)
    rounded_box(ax, 6.3, 3.5, 5.3, 2.3,
                "FEW-SHOT\n\nExample 1: Water bottle → tagline\nExample 2: Desk lamp → tagline\nNow: Headphones → ?",
                COLORS["few"], edge=COLORS["secondary"], fontsize=9.5)
    rounded_box(ax, 0.4, 1.5, 5.3, 1.5,
                "Best for: translation,\nsimple Q&A\nLower token cost",
                COLORS["card"], edge=COLORS["primary"], fontsize=9)
    rounded_box(ax, 6.3, 1.5, 5.3, 1.5,
                "Best for: custom format,\nbrand tone, labels\nMore consistent output",
                COLORS["card"], edge=COLORS["secondary"], fontsize=9)
    rounded_box(ax, 0.4, 0.2, 11.2, 1.0,
                "Tip: start zero-shot — add 2 strong examples only when format drifts",
                "#FFFBEB", edge=COLORS["accent"], fontsize=9.5, weight="bold")
    save(fig, "session24-02-zero-shot-vs-few-shot.png")


if __name__ == "__main__":
    image_01_system_vs_user()
    image_02_zero_vs_few_shot()
