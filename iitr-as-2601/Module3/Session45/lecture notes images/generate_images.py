"""Generate Session 45 lecture note diagrams — Prompt Versioning & API Rate Limits."""
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
        "Prompt Versioning & API Rate Limits",
        "Manage prompts over time · call cloud APIs safely during development",
    )
    rounded_box(ax, 0.4, 3.5, 5.3, 2.4,
                "Prompt versioning\n\nNamed files · registry bundles\nCompare v1 vs v2 · roll back",
                COLORS["chunk1"], edge=COLORS["primary"], fontsize=10, weight="bold")
    rounded_box(ax, 6.3, 3.5, 5.3, 2.4,
                "API rate limits\n\n429 = slow down\nBackoff · jitter · retry logs",
                COLORS["chunk3"], edge=COLORS["accent"], fontsize=10, weight="bold")
    rounded_box(ax, 0.4, 0.9, 11.2, 2.0,
                "ShopEasy support bot: save every prompt revision · survive shared-key demos\n"
                "Shift from one request internals → traceable product logic + polite API habits",
                COLORS["card"], edge=COLORS["secondary"], fontsize=9.5, weight="bold")
    save(fig, "session45-01-prompt-versioning-overview.png")


def image_02():
    fig, ax = setup_fig("Why Prompts Need Versioning", "Living product logic — not a one-time sticky note")
    rounded_box(ax, 0.4, 3.6, 5.3, 2.5,
                "WITHOUT versioning\n\n'It worked yesterday' — no proof\nSilent Google Doc edits\nBug cannot be reproduced",
                COLORS["chunk5"], edge=COLORS["danger"], fontsize=9.5)
    rounded_box(ax, 6.3, 3.6, 5.3, 2.5,
                "WITH versioning\n\nv1_system.txt + v2_system.txt\nSame eval questions on both\nReload exact file from bug day",
                COLORS["chunk4"], edge=COLORS["success"], fontsize=9.5)
    rounded_box(ax, 0.4, 0.9, 5.5, 2.2,
                "Recipe notebook\nPaneer butter masala v1 (mild)\nv2 (extra spice)",
                COLORS["chunk2"], edge=COLORS["secondary"], fontsize=9)
    rounded_box(ax, 6.0, 0.9, 5.6, 2.2,
                "Zomato menu card\nKeep old card beside new\nCompare when complaints rise",
                COLORS["warn"], edge=COLORS["accent"], fontsize=9)
    save(fig, "session45-02-why-versioning.png")


def image_03():
    fig, ax = setup_fig("Versioned Folder Layout", "One file per version · config separate from prose")
    folders = [
        ("prompts/support_agent/\nv1_system.txt\nv2_system.txt\neval_questions.txt", 0.4, COLORS["chunk1"]),
        ("config/\nsupport_agent_v1.yaml\nsupport_agent_v2.yaml", 4.2, COLORS["chunk2"]),
        ("logs/\napi_retries.log", 8.0, COLORS["chunk3"]),
    ]
    for label, x, face in folders:
        rounded_box(ax, x, 3.2, 3.5, 2.5, label, face, fontsize=9, weight="bold")
    rounded_box(ax, 0.4, 1.5, 5.5, 1.4,
                "Prompt text = instructions the model reads",
                COLORS["card"], edge=COLORS["primary"], fontsize=9)
    rounded_box(ax, 6.0, 1.5, 5.6, 1.4,
                "Config = model name · temperature · max_tokens · tools",
                COLORS["card"], edge=COLORS["secondary"], fontsize=9)
    rounded_box(ax, 0.4, 0.25, 11.2, 1.0,
                "Like Diwali_2024.jpg and Diwali_2025.jpg — both visible, neither overwrites the other",
                "#EEF2FF", edge=COLORS["secondary"], fontsize=9)
    save(fig, "session45-03-versioned-folder-layout.png")


def image_04():
    fig, ax = setup_fig("Registry Pattern", "One lookup: agent name + version → prompt · config · tools")
    rounded_box(ax, 0.4, 4.5, 11.2, 1.2,
                "REGISTRY  —  support_agent/v2  →  prompt_path + config + tools + max_tool_steps",
                COLORS["secondary"], edge=COLORS["secondary"], fontsize=10, weight="bold")
    entries = [
        ("support_agent / v1", "v1_system.txt\ntemp=0 · lookup_order", COLORS["chunk1"]),
        ("support_agent / v2", "v2_system.txt\n+ closing line · same tools", COLORS["chunk2"]),
        ("summarizer / v1", "v1_system.txt\nno tools · temp=0.2", COLORS["chunk4"]),
    ]
    x = 0.4
    for title, body, face in entries:
        rounded_box(ax, x, 2.8, 3.6, 0.65, title, face, fontsize=9, weight="bold")
        rounded_box(ax, x, 1.5, 3.6, 1.15, body, COLORS["card"], edge=face, fontsize=8.5)
        x += 3.9
    rounded_box(ax, 0.4, 0.25, 11.2, 1.0,
                "Like Big Bazaar store directory — one chart, no wandering · bundle prompt + config + tools",
                "#FFFBEB", edge=COLORS["accent"], fontsize=9)
    save(fig, "session45-04-registry-pattern.png")


def image_05():
    fig, ax = setup_fig("Qualitative Eval — v1 vs v2", "Same questions · same context · human checklist")
    rounded_box(ax, 0.4, 4.8, 11.2, 0.75,
                "Eval Q: What is the electronics return window?  ·  Shared ShopEasy policy context",
                COLORS["warn"], edge=COLORS["accent"], fontsize=9, weight="bold")
    rounded_box(ax, 0.4, 2.5, 5.3, 2.0,
                "--- v1 ---\n7-day return if unopened.\nPolite · under 3 sentences.",
                COLORS["chunk1"], edge=COLORS["primary"], fontsize=9)
    rounded_box(ax, 6.3, 2.5, 5.3, 2.0,
                "--- v2 ---\nSame answer +\n'Need anything else? Reply order ID.'",
                COLORS["chunk2"], edge=COLORS["secondary"], fontsize=9)
    checks = "Grounded?  Refuses unknown?  ≤3 sentences?  v2 closing line?"
    rounded_box(ax, 0.4, 0.9, 11.2, 1.3,
                f"Checklist: {checks}\nShip v2 only if equal or better on every must-have row",
                COLORS["card"], edge=COLORS["success"], fontsize=9, weight="bold")
    save(fig, "session45-05-qualitative-eval.png")


def image_06():
    fig, ax = setup_fig("HTTP Rate Limits", "429 Too Many Requests — slow down, not broken phone")
    limits = [
        ("RPM\nRequests / minute", "ReAct loop\n8+ calls in 60s", COLORS["chunk5"]),
        ("TPM\nTokens / minute", "Fat RAG + long history\nin tight loop", COLORS["chunk3"]),
        ("Daily quota", "Class demos all day\non one org key", COLORS["chunk2"]),
    ]
    x = 0.4
    for title, body, face in limits:
        rounded_box(ax, x, 3.8, 3.6, 1.0, title, face, fontsize=9, weight="bold")
        rounded_box(ax, x, 2.3, 3.6, 1.3, body, COLORS["card"], edge=face, fontsize=8.5)
        x += 3.9
    rounded_box(ax, 0.4, 0.9, 5.5, 1.2,
                "RTO token counter\nOnly N people per hour",
                COLORS["chunk1"], edge=COLORS["primary"], fontsize=9)
    rounded_box(ax, 6.0, 0.9, 5.6, 1.2,
                "1 user message → 5–15 API calls\nin agent tool loop",
                COLORS["card"], edge=COLORS["danger"], fontsize=9, weight="bold")
    save(fig, "session45-06-http-rate-limits.png")


def image_07():
    fig, ax = setup_fig("Exponential Backoff", "Wait longer after each 429 — add jitter · cap max retries")
    attempts = [
        ("Attempt 1", "wait ~1s", 0.5, COLORS["chunk1"]),
        ("Attempt 2", "wait ~2s", 0.85, COLORS["chunk2"]),
        ("Attempt 3", "wait ~4s", 1.35, COLORS["chunk3"]),
        ("Attempt 4", "wait ~8s", 2.35, COLORS["chunk5"]),
    ]
    x = 0.5
    for label, wait, h, face in attempts:
        rounded_box(ax, x, 1.2, 2.4, h, f"{label}\n{wait}", face, fontsize=9, weight="bold")
        if x < 9:
            arrow(ax, x + 2.4, 1.2 + h / 2, x + 2.7, 1.2 + h / 2, COLORS["accent"])
        x += 2.7
    rounded_box(ax, 0.4, 4.2, 5.5, 1.5,
                "Knock patiently — not every second\nIRCTC Tatkal: wait, then retry",
                COLORS["card"], edge=COLORS["primary"], fontsize=9)
    rounded_box(ax, 6.0, 4.2, 5.6, 1.5,
                "Retry: 429 · 503 · timeout\nDo NOT retry: 401 · 400\nmax_retries = 4",
                COLORS["card"], edge=COLORS["success"], fontsize=9)
    rounded_box(ax, 0.4, 0.25, 11.2, 0.75,
                "Jitter spreads retries when many laptops share one classroom API key",
                "#EEF2FF", edge=COLORS["secondary"], fontsize=9)
    save(fig, "session45-07-exponential-backoff.png")


def image_08():
    fig, ax = setup_fig("Retry Logs & Resilient Pipeline", "Invisible waits become visible · version → eval → operate → promote")
    stages = [
        ("Design", "v2 diff from v1", COLORS["chunk1"]),
        ("Register", "agent bundle", COLORS["chunk2"]),
        ("Evaluate", "eval + checklist", COLORS["chunk3"]),
        ("Operate", "backoff + logs", COLORS["chunk4"]),
        ("Promote", "default = v2", COLORS["success"]),
    ]
    x = 0.35
    for i, (title, body, face) in enumerate(stages):
        rounded_box(ax, x, 4.0, 2.15, 0.6, title, face, fontsize=8.5, weight="bold")
        rounded_box(ax, x, 3.1, 2.15, 0.75, body, COLORS["card"], edge=face, fontsize=7.5)
        if i < 4:
            arrow(ax, x + 2.15, 4.3, x + 2.35, 4.3, COLORS["accent"])
        x += 2.35
    rounded_box(ax, 0.4, 1.0, 11.2, 1.8,
                "logs/api_retries.log\n"
                "2025-06-14 | WARNING | service=groq | version=support_agent/v2 | attempt=1/4 | wait_s=1.12\n"
                "2025-06-14 | INFO    | recovered_after_attempts=2",
                "#FFFBEB", edge=COLORS["accent"], fontsize=8.5)
    rounded_box(ax, 0.4, 0.15, 11.2, 0.7,
                "time.sleep(1) between eval questions = prevention · backoff = recovery",
                COLORS["card"], edge=COLORS["primary"], fontsize=9)
    save(fig, "session45-08-retry-logs-pipeline.png")


if __name__ == "__main__":
    image_01()
    image_02()
    image_03()
    image_04()
    image_05()
    image_06()
    image_07()
    image_08()
