"""Generate Session 48 lecture note diagrams — End-to-end n8n AI automation pipeline."""
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
    "gmail": "#FEE2E2",
    "llm": "#E9D5FF",
    "merge": "#DBEAFE",
    "delivery": "#D1FAE5",
    "oauth": "#FFEDD5",
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
        "End-to-End n8n AI Automation Pipeline",
        "Email in → parallel AI steps → merge → deliver summary and commented code back",
    )
    rounded_box(ax, 0.4, 3.8, 2.0, 1.4, "Gmail Trigger\nOn message\nreceived", COLORS["gmail"],
                edge=COLORS["danger"], fontsize=9, weight="bold")
    rounded_box(ax, 3.0, 4.6, 2.3, 1.0, "Code Summarizer\nBasic LLM Chain", COLORS["llm"],
                edge=COLORS["secondary"], fontsize=8.5)
    rounded_box(ax, 3.0, 3.2, 2.3, 1.0, "Code Commentator\nBasic LLM Chain", COLORS["llm"],
                edge=COLORS["secondary"], fontsize=8.5)
    rounded_box(ax, 5.8, 3.8, 1.8, 1.4, "Merge\nWait for both", COLORS["merge"],
                edge=COLORS["primary"], fontsize=9, weight="bold")
    rounded_box(ax, 8.0, 3.8, 1.8, 1.4, "Aggregate\nCombine text", COLORS["merge"],
                edge=COLORS["primary"], fontsize=9)
    rounded_box(ax, 10.0, 3.8, 1.6, 1.4, "Gmail Send\nMessage", COLORS["delivery"],
                edge=COLORS["success"], fontsize=9, weight="bold")

    arrow(ax, 2.4, 4.5, 3.0, 5.0, COLORS["accent"])
    arrow(ax, 2.4, 4.2, 3.0, 3.7, COLORS["accent"])
    arrow(ax, 5.3, 5.1, 5.8, 4.5, COLORS["primary"])
    arrow(ax, 5.3, 3.7, 5.8, 4.2, COLORS["primary"])
    arrow(ax, 7.6, 4.5, 8.0, 4.5, COLORS["primary"])
    arrow(ax, 9.8, 4.5, 10.0, 4.5, COLORS["success"])

    ax.text(2.7, 5.35, "parallel", fontsize=8, color=COLORS["accent"], ha="center", style="italic")

    stages = [
        ("Ingestion", "Read email body\nFilter by sender"),
        ("AI processing", "Summarize + comment\nin parallel"),
        ("Join & package", "Merge then aggregate\none send payload"),
        ("Delivery", "Email back to user\nText or HTML"),
    ]
    for i, (title, body) in enumerate(stages):
        x = 0.4 + i * 2.95
        rounded_box(ax, x, 1.5, 2.6, 0.45, title, COLORS["card"], edge=COLORS["accent"],
                    fontsize=8.5, weight="bold")
        rounded_box(ax, x, 0.55, 2.6, 0.85, body, COLORS["card"], fontsize=8)

    rounded_box(ax, 0.4, 0.05, 11.2, 0.4,
                "Bring content in → apply AI → route joined results → notify or store",
                "#EEF2FF", edge=COLORS["secondary"], fontsize=9.5)
    save(fig, "session48-01-end-to-end-pipeline-overview.png")


def image_02():
    fig, ax = setup_fig(
        "Gmail Automatic Trigger and Ingestion",
        "Polling inbox for trusted sender — no manual Execute button needed",
    )
    rounded_box(ax, 0.5, 4.0, 3.5, 2.0,
                "Incoming email\nSubject: Python code\nBody: script text\nFrom: trusted sender",
                COLORS["gmail"], edge=COLORS["danger"], fontsize=9)
    rounded_box(ax, 4.5, 4.3, 3.2, 1.4,
                "Gmail Trigger\nPoll every minute\nEvent: message received",
                COLORS["card"], edge=COLORS["primary"], fontsize=9, weight="bold")
    rounded_box(ax, 8.2, 4.3, 3.3, 1.4,
                "Sender filter\nOnly process mail\nfrom allowed address",
                COLORS["oauth"], edge=COLORS["accent"], fontsize=9, weight="bold")

    arrow(ax, 4.0, 5.0, 4.5, 5.0, COLORS["primary"])
    arrow(ax, 7.7, 5.0, 8.2, 5.0, COLORS["accent"])

    rounded_box(ax, 0.5, 1.8, 5.5, 1.6,
                "Manual trigger (previous build)\nHuman clicks Execute → form opens\nGood for demos, not live ops",
                COLORS["card"], edge=COLORS["danger"], fontsize=9)
    rounded_box(ax, 6.2, 1.8, 5.3, 1.6,
                "Automatic trigger (this build)\nMailbox watched continuously\nWorkflow starts on its own",
                COLORS["delivery"], edge=COLORS["success"], fontsize=9)

    rounded_box(ax, 0.5, 0.35, 11.0, 1.1,
                "Fetch test event pulls sample data before going live\nPin output while building LLM nodes — unpin for real end-to-end run",
                "#EEF2FF", edge=COLORS["secondary"], fontsize=10)
    save(fig, "session48-02-gmail-automatic-trigger.png")


def image_03():
    fig, ax = setup_fig(
        "Parallel LLM Branches, Merge, and Aggregate",
        "Independent AI tasks run together — merge waits until both finish",
    )
    rounded_box(ax, 0.5, 4.5, 2.4, 1.0, "Gmail email text\nPython script", COLORS["gmail"],
                edge=COLORS["danger"], fontsize=9, weight="bold")

    rounded_box(ax, 3.5, 5.2, 2.8, 0.9, "Code Summarizer\nPlain-English summary", COLORS["llm"],
                edge=COLORS["secondary"], fontsize=8.5)
    rounded_box(ax, 3.5, 3.8, 2.8, 0.9, "Code Commentator\nInline comments added", COLORS["llm"],
                edge=COLORS["secondary"], fontsize=8.5)

    arrow(ax, 2.9, 4.9, 3.5, 5.5, COLORS["accent"])
    arrow(ax, 2.9, 4.7, 3.5, 4.2, COLORS["accent"])
    ax.text(3.2, 4.95, "same input", fontsize=8, color=COLORS["muted"], rotation=90, va="center")

    rounded_box(ax, 6.8, 4.3, 2.0, 1.4, "Merge\nAppend both\noutputs", COLORS["merge"],
                edge=COLORS["primary"], fontsize=9, weight="bold")
    rounded_box(ax, 9.2, 4.3, 2.3, 1.4, "Aggregate\ntext0 + text1\none payload", COLORS["merge"],
                edge=COLORS["primary"], fontsize=9)

    arrow(ax, 6.3, 5.5, 6.8, 4.9, COLORS["primary"])
    arrow(ax, 6.3, 4.2, 6.8, 4.6, COLORS["primary"])
    arrow(ax, 8.8, 5.0, 9.2, 5.0, COLORS["primary"])

    rounded_box(ax, 0.5, 1.5, 5.3, 2.0,
                "Why parallel?\nSummarize and comment do not depend on each other\nFaster than running one after another",
                COLORS["card"], edge=COLORS["success"], fontsize=9)
    rounded_box(ax, 6.0, 1.5, 5.5, 2.0,
                "Why merge?\nParallel paths finish in random order\nEmail should wait for BOTH results",
                COLORS["card"], edge=COLORS["accent"], fontsize=9)

    rounded_box(ax, 0.5, 0.2, 11.0, 0.9,
                "Kitchen analogy: two cooks finish at different times — merge plates both dishes before serving",
                "#EEF2FF", edge=COLORS["secondary"], fontsize=10)
    save(fig, "session48-03-parallel-llm-merge-aggregate.png")


def image_04():
    fig, ax = setup_fig(
        "Gmail OAuth and OpenAI Credentials in n8n",
        "Two credential stores power the pipeline — never share keys in chat or screenshots",
    )
    rounded_box(ax, 0.4, 3.6, 4.8, 2.4,
                "Google Cloud Console\n1. Create project\n2. Enable Gmail API\n3. OAuth consent + test user\n4. Web client ID + secret",
                COLORS["oauth"], edge=COLORS["accent"], fontsize=9)
    rounded_box(ax, 6.0, 4.2, 2.2, 1.6, "n8n\nCredential\nvault", COLORS["card"],
                edge=COLORS["primary"], fontsize=10, weight="bold")
    rounded_box(ax, 8.6, 3.6, 2.8, 2.4,
                "OpenAI API key\nStored in n8n\nPowers Basic LLM Chain",
                COLORS["llm"], edge=COLORS["secondary"], fontsize=9)

    arrow(ax, 5.2, 4.8, 6.0, 5.0, COLORS["accent"])
    arrow(ax, 8.2, 4.8, 8.6, 4.8, COLORS["secondary"])
    ax.text(5.6, 5.25, "OAuth sign-in", fontsize=8, color=COLORS["accent"])
    ax.text(8.4, 5.25, "API key", fontsize=8, color=COLORS["secondary"])

    checks = [
        ("Gmail trigger", "Read inbox"),
        ("Gmail send", "Compose reply"),
        ("LLM nodes", "Summarize + comment"),
    ]
    for i, (node, scope) in enumerate(checks):
        y = 2.3 - i * 0.7
        rounded_box(ax, 0.5, y, 3.0, 0.55, node, COLORS["gmail"], fontsize=8.5, weight="bold")
        rounded_box(ax, 3.7, y, 4.5, 0.55, scope, COLORS["card"], fontsize=8.5)

    rounded_box(ax, 0.5, 0.25, 11.0, 0.85,
                "Revoke demo credentials after class — treat Client ID, Secret, and API keys like passwords",
                COLORS["card"], edge=COLORS["danger"], fontsize=10)
    save(fig, "session48-04-gmail-oauth-openai-credentials.png")


def image_05():
    fig, ax = setup_fig(
        "Delivery, HTML Formatting, and Workflow Handoff",
        "Readable email output plus JSON export for teammates",
    )
    rounded_box(ax, 0.4, 3.8, 5.0, 2.2,
                "Outgoing Gmail\nCommented code block\nBullet summary\nHTML message type",
                COLORS["delivery"], edge=COLORS["success"], fontsize=9, weight="bold")
    rounded_box(ax, 6.0, 4.2, 2.3, 1.5, "Plain text\nHard to read\ncode", COLORS["card"],
                edge=COLORS["danger"], fontsize=9)
    rounded_box(ax, 8.7, 4.2, 2.8, 1.5, "HTML format\nStyled blocks\nand bullets", COLORS["delivery"],
                edge=COLORS["success"], fontsize=9)
    arrow(ax, 5.4, 5.0, 6.0, 5.0, COLORS["danger"])
    arrow(ax, 8.3, 5.0, 8.7, 5.0, COLORS["success"])
    ax.text(6.15, 5.45, "before", fontsize=8, color=COLORS["danger"])
    ax.text(9.0, 5.45, "after", fontsize=8, color=COLORS["success"])

    rounded_box(ax, 0.4, 1.2, 5.5, 2.0,
                "Pipeline testing checklist\nHappy path: valid code email\nFailure: bad API key\nEdge: wrong sender ignored",
                COLORS["card"], edge=COLORS["accent"], fontsize=9)
    rounded_box(ax, 6.2, 1.2, 5.4, 2.0,
                "Workflow JSON export\nDownload from n8n\nImport on teammate server\nReconnect local credentials",
                COLORS["oauth"], edge=COLORS["primary"], fontsize=9)

    rounded_box(ax, 0.4, 0.15, 11.2, 0.75,
                "Sticky note on canvas documents assumptions — JSON shares wiring, not your private passwords",
                "#EEF2FF", edge=COLORS["secondary"], fontsize=10)
    save(fig, "session48-05-delivery-html-and-handoff.png")


if __name__ == "__main__":
    image_01()
    image_02()
    image_03()
    image_04()
    image_05()
    print("All Session 48 images generated.")
