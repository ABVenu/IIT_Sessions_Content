"""Generate Session 22 (Evaluating and Improving RAG Systems) lecture note diagrams — ShopKart theme."""
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
    "retrieval": "#DBEAFE",
    "generation": "#FFEDD5",
    "hallucination": "#FECACA",
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
        "Three RAG Failure Modes — ShopKart",
        "Classify the bug before you change code — each mode needs a different fix",
    )
    modes = [
        ("RETRIEVAL\nWrong / missing chunks\nRank 1 category or text wrong",
         COLORS["retrieval"], COLORS["primary"], 0.4),
        ("GENERATION\nGood chunks retrieved\nAnswer misreads excerpts",
         COLORS["generation"], COLORS["accent"], 4.1),
        ("HALLUCINATION\nFacts not in excerpts\nInvented UPI steps, instant refund",
         COLORS["hallucination"], COLORS["danger"], 7.8),
    ]
    for txt, face, edge, x in modes:
        rounded_box(ax, x, 3.0, 3.5, 2.2, txt, face, edge=edge, fontsize=9, weight="bold")

    rounded_box(ax, 0.5, 0.5, 11.0, 1.8,
                "Fix mapping:\n• Retrieval → top-k · metadata filter · chunk overlap\n"
                "• Generation → stricter grounding prompt\n"
                "• Hallucination → refusal sentence + do not invent rules",
                COLORS["card"], edge=COLORS["secondary"], fontsize=9.5)
    save(fig, "session22-01-three-failure-modes.png")


def image_02():
    fig, ax = setup_fig(
        "The Clinic Test — Diagnose Before You Prescribe",
        "Same three failure modes — wrong test, misread report, or invented treatment",
    )
    cases = [
        ("Wrong test ordered", "RETRIEVAL\nPolicy in library\nbut search missed it", 0.4),
        ("Report on desk,\nmisread", "GENERATION\nEvidence present\nanswer wrong", 4.1),
        ("No report,\nconfident anyway", "HALLUCINATION\nNot supported\nby evidence", 7.8),
    ]
    for title, body, x in cases:
        rounded_box(ax, x, 4.5, 3.5, 0.9, title, COLORS["warn"], edge=COLORS["accent"],
                    fontsize=9, weight="bold")
        rounded_box(ax, x, 2.5, 3.5, 1.7, body, COLORS["card"], edge=COLORS["primary"],
                    fontsize=9, weight="bold")

    rounded_box(ax, 0.5, 0.45, 11.0, 1.5,
                "Do not rebuild the whole pipeline after one mistake.\nAsk which stage failed → apply a targeted fix.",
                COLORS["card"], edge=COLORS["success"], fontsize=10, weight="bold")
    save(fig, "session22-02-clinic-test-analogy.png")


def image_03():
    fig, ax = setup_fig(
        "Evaluate Retrieval and Generation Separately",
        "Two independent stages — judge each before changing code",
    )
    rounded_box(ax, 0.4, 3.2, 5.2, 2.3,
                "STAGE 1 — RETRIEVAL\nDid we fetch the right policy chunk?\n\n"
                "Inspect: Rank 1 category · source · distance · text",
                COLORS["retrieval"], edge=COLORS["primary"], fontsize=9.5, weight="bold")
    rounded_box(ax, 6.4, 3.2, 5.2, 2.3,
                "STAGE 2 — GENERATION\nDoes the answer match the excerpts?\n\n"
                "Compare: numbers · rules · no invented steps",
                COLORS["generation"], edge=COLORS["accent"], fontsize=9.5, weight="bold")
    arrow(ax, 5.6, 4.35, 6.4, 4.35, COLORS["accent"])

    rounded_box(ax, 0.5, 0.5, 11.0, 1.8,
                "Lab workflow: print_retrieved_chunks → read Rank 1 → read Answer\n"
                "If Stage 1 fails, fix retrieval first — not the LLM prompt",
                COLORS["warn"], edge=COLORS["danger"], fontsize=9.5, weight="bold")
    save(fig, "session22-03-two-stage-evaluation.png")


def image_04():
    fig, ax = setup_fig(
        "Four-Step Evaluation Checklist",
        "Run in order for every query in TEST_QUERIES",
    )
    steps = [
        ("1\nRight policy\narea?", COLORS["returns"], 0.4),
        ("2\nRight chunk\nwithin policy?", COLORS["shipping"], 2.8),
        ("3\nAnswer\nfactually correct?", COLORS["warranty"], 5.2),
        ("4\nAnswer\ngrounded?", COLORS["refunds"], 7.6),
    ]
    for i, (txt, face, x) in enumerate(steps):
        rounded_box(ax, x, 3.0, 2.2, 1.8, txt, face, fontsize=9, weight="bold")
        if i < 3:
            arrow(ax, x + 2.2, 3.9, steps[i + 1][2], 3.9, COLORS["primary"])

    rounded_box(ax, 0.5, 0.5, 11.0, 1.8,
                "Example: returns question → Rank 1 category must be returns, not shipping\n"
                "Example: prepaid UPI → no UPI section in corpus → answer must refuse, not invent",
                COLORS["card"], edge=COLORS["secondary"], fontsize=9.5)
    save(fig, "session22-04-four-step-checklist.png")


def image_05():
    fig, ax = setup_fig(
        "Four Improvement Levers — Pick by Failure Mode",
        "Change one or two levers per run — re-test the same TEST_QUERIES",
    )
    levers = [
        ("top-k\n3 baseline → 5 improved\nMore chunks per query", COLORS["returns"], 0.3),
        ("Metadata filter\nguess_category + where\nOne policy shelf only", COLORS["shipping"], 3.1),
        ("Stricter prompt\ngenerate_strict_answer\nREFUSAL sentence", COLORS["warranty"], 5.9),
        ("Chunk overlap\n120 words / 30 overlap\nOptional 2nd iteration", COLORS["refunds"], 8.7),
    ]
    for txt, face, x in levers:
        rounded_box(ax, x, 3.0, 2.5, 2.0, txt, face, fontsize=8.5, weight="bold")

    rounded_box(ax, 0.5, 0.45, 11.0, 1.8,
                "Improved run in lab: strict prompt + category filter + top_k=5\n"
                "Opened charger fail? → try chunk overlap after improved run",
                COLORS["warn"], edge=COLORS["accent"], fontsize=9.5, weight="bold")
    save(fig, "session22-05-four-improvement-levers.png")


def image_06():
    fig, ax = setup_fig(
        "Metadata Filter — Search One Policy Shelf",
        "guess_category routes query → retrieve_filtered uses where={category: ...}",
    )
    rounded_box(ax, 0.4, 4.2, 11.2, 0.65,
                "All chunks in shopkart_policy_kb_v2 tagged: returns · shipping · warranty · refunds",
                COLORS["card"], edge=COLORS["muted"], fontsize=9.5)

    shelves = [
        ("returns", COLORS["returns"], 0.4),
        ("shipping", COLORS["shipping"], 3.1),
        ("warranty", COLORS["warranty"], 5.8),
        ("refunds", COLORS["refunds"], 8.5),
    ]
    for name, face, x in shelves:
        rounded_box(ax, x, 2.5, 2.5, 1.4, name, face, fontsize=10, weight="bold")

    rounded_box(ax, 0.4, 0.5, 4.5, 1.5,
                'Query: "water damage warranty?"\nguess_category → warranty',
                COLORS["warn"], edge=COLORS["accent"], fontsize=9, weight="bold")
    arrow(ax, 2.65, 2.0, 6.95, 2.5, COLORS["accent"])
    rounded_box(ax, 5.2, 0.5, 6.3, 1.5,
                "Chroma query with\nwhere={category: warranty}\n→ no shipping noise",
                COLORS["card"], edge=COLORS["success"], fontsize=9.5, weight="bold")
    save(fig, "session22-06-metadata-filter.png")


def image_07():
    fig, ax = setup_fig(
        "Baseline vs Improved Run",
        "Same TEST_QUERIES — compare terminal output side by side",
    )
    rounded_box(ax, 0.4, 3.5, 5.2, 2.0,
                "BASELINE\noriginal prompt\nno filter · top_k=3\n\ngenerate_grounded_answer",
                COLORS["card"], edge=COLORS["muted"], fontsize=9.5, weight="bold")
    rounded_box(ax, 6.4, 3.5, 5.2, 2.0,
                "IMPROVED\nstrict prompt + filter\n top_k=5\n\ngenerate_strict_answer",
                COLORS["success"], edge=COLORS["success"], fontsize=9.5, weight="bold")
    arrow(ax, 5.6, 4.5, 6.4, 4.5, COLORS["accent"])

    rounded_box(ax, 0.5, 0.5, 11.0, 2.2,
                "run_queries() loops TEST_QUERIES:\n"
                "  retrieve_filtered → print_retrieved_chunks → Answer\n\n"
                "Watch: Rank 1 category · refusal on prepaid UPI · no instant refund on COD",
                COLORS["warn"], edge=COLORS["primary"], fontsize=9.5)
    save(fig, "session22-07-baseline-vs-improved.png")


def image_08():
    fig, ax = setup_fig(
        "Iterative Evaluation Cycle",
        "Building RAG is step one — production teams repeat this loop",
    )
    steps = [
        ("TEST\nTEST_QUERIES", COLORS["returns"], 0.4),
        ("DIAGNOSE\nRank 1 + failure mode", COLORS["shipping"], 2.8),
        ("IMPROVE\n1–2 levers", COLORS["warranty"], 5.2),
        ("RE-TEST\nsame queries", COLORS["refunds"], 7.6),
    ]
    for i, (txt, face, x) in enumerate(steps):
        rounded_box(ax, x, 3.2, 2.2, 1.6, txt, face, fontsize=9, weight="bold")
        if i < 3:
            arrow(ax, x + 2.2, 4.0, steps[i + 1][2], 4.0, COLORS["primary"])
    arrow(ax, 9.8, 3.2, 0.4, 3.2, COLORS["accent"])

    rounded_box(ax, 0.5, 0.45, 11.0, 1.8,
                "Repeat when: new refund PDF · wrong warranty answers · model swap · user feedback\n"
                "Re-run build_knowledge_base after policy or chunk changes",
                COLORS["card"], edge=COLORS["secondary"], fontsize=9.5)
    save(fig, "session22-08-iterative-cycle.png")


if __name__ == "__main__":
    image_01()
    image_02()
    image_03()
    image_04()
    image_05()
    image_06()
    image_07()
    image_08()
