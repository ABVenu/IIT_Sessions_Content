"""Generate Session 19 (Introduction to RAG) lecture note diagrams — ShopKart theme."""
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
        "ShopKart Knowledge Base — The Rule Book",
        "Curated policy documents the support bot is allowed to cite",
    )
    rounded_box(ax, 4.0, 5.0, 4.0, 0.75, "ShopKart Support Assistant", COLORS["card"],
                edge=COLORS["primary"], fontsize=11, weight="bold")
    policies = [
        ("Returns", "7 calendar days\nunopened only", COLORS["returns"], 0.5),
        ("Shipping", "3–5 business days\nexpress in metros", COLORS["shipping"], 3.3),
        ("Warranty", "12-month electronics\nno liquid damage", COLORS["warranty"], 6.1),
        ("Refunds", "5–7 business days\nafter verification", COLORS["refunds"], 8.9),
    ]
    for title, body, face, x in policies:
        rounded_box(ax, x, 2.8, 2.4, 0.65, title, face, fontsize=10, weight="bold")
        rounded_box(ax, x, 1.2, 2.4, 1.4, body, face, fontsize=8.5)
        arrow(ax, 6.0, 5.0, x + 1.2, 2.45, COLORS["accent"])
    rounded_box(ax, 0.5, 0.25, 11.0, 0.75,
                "Knowledge base = trusted docs  |  Not whatever the LLM remembers from training",
                "#EEF2FF", edge=COLORS["secondary"], fontsize=10)
    save(fig, "session19-01-shopkart-knowledge-base.png")


def image_02():
    fig, ax = setup_fig(
        "When LLM-Only Knowledge Falls Short",
        "Three gaps that appear in real customer-support products",
    )
    gaps = [
        ("Static knowledge gap", "Training cutoff\nPolicy changed to 7 days\nModel still says 30 days", COLORS["danger"], 0.4),
        ("Domain context gap", "Never saw ShopKart docs\nInvents 'lifetime warranty'\nShopKart never offered it", COLORS["accent"], 4.2),
        ("Hallucination risk", "Fluent but false\n'Refund in 24 hours'\nPolicy says 5–7 days", COLORS["secondary"], 8.0),
    ]
    for title, body, edge, x in gaps:
        rounded_box(ax, x, 3.6, 3.4, 0.85, title, COLORS["card"], edge=edge, fontsize=9.5, weight="bold")
        rounded_box(ax, x, 1.3, 3.4, 2.1, body, COLORS["card"], edge=edge, fontsize=8.5)
    rounded_box(ax, 0.5, 0.25, 11.0, 0.85,
                "Good English ≠ good knowledge  |  Separate writing quality from organizational correctness",
                COLORS["warn"], edge=COLORS["accent"], fontsize=10, weight="bold")
    save(fig, "session19-02-llm-knowledge-gaps.png")


def image_03():
    fig, ax = setup_fig(
        "Confidence vs Correctness",
        "Polite tone impresses users — product teams must verify facts separately",
    )
    rounded_box(ax, 0.5, 3.8, 5.2, 1.8,
                "What the customer sees\n• Polite, complete sentences\n• Specific numbers ('7 days')\n• Empathy lines",
                COLORS["card"], edge=COLORS["primary"], fontsize=9.5)
    rounded_box(ax, 6.3, 3.8, 5.2, 1.8,
                "What the team must verify\n• Matches live policy PDF?\n• Numbers in retrieved evidence?\n• Empathy ≠ eligibility",
                COLORS["card"], edge=COLORS["success"], fontsize=9.5)
    arrow(ax, 5.7, 4.7, 6.3, 4.7, COLORS["accent"])
    ax.text(6.0, 5.05, "audit", fontsize=9, color=COLORS["accent"], ha="center", weight="bold")

    rounded_box(ax, 1.0, 1.5, 4.5, 1.5, "Ungrounded\nSounds confident\nMay be wrong", COLORS["danger"],
                edge=COLORS["danger"], fontsize=10, weight="bold")
    rounded_box(ax, 6.5, 1.5, 4.5, 1.5, "Grounded\nMay feel stricter\nMore correct", COLORS["success"],
                edge=COLORS["success"], fontsize=10, weight="bold")
    rounded_box(ax, 0.5, 0.2, 11.0, 0.75,
                "Calibration = align stated confidence with how often answers are actually correct",
                "#EEF2FF", edge=COLORS["secondary"], fontsize=10)
    save(fig, "session19-03-confidence-vs-correctness.png")


def image_04():
    fig, ax = setup_fig(
        "Grounding — Show Your Work",
        "Tie the final answer to evidence from trusted documents",
    )
    steps = [
        (0.4, "Customer\nquestion", COLORS["returns"]),
        (2.6, "Retrieve\npolicy chunks", COLORS["shipping"]),
        (4.8, "Evidence in\nprompt", COLORS["warranty"]),
        (7.0, "LLM explains\nin plain language", COLORS["refunds"]),
        (9.2, "Grounded\nreply", COLORS["success"]),
    ]
    for x, txt, face in steps:
        rounded_box(ax, x, 3.5, 1.9, 1.4, txt, face, fontsize=8.5, weight="bold")
    for x1, x2 in [(2.3, 2.6), (4.5, 4.8), (6.7, 7.0), (8.9, 9.2)]:
        arrow(ax, x1, 4.2, x2, 4.2, COLORS["primary"])

    rounded_box(ax, 0.5, 1.2, 5.3, 1.6,
                "Without grounding\nCreative writing from memory\nRisky for policy Q&A",
                COLORS["card"], edge=COLORS["danger"], fontsize=9.5)
    rounded_box(ax, 6.2, 1.2, 5.3, 1.6,
                "With grounding\nReading comprehension +\nexplanation — safer for customers",
                COLORS["card"], edge=COLORS["success"], fontsize=9.5)
    rounded_box(ax, 0.5, 0.15, 11.0, 0.75,
                "Real-life: CA files taxes from your Form 16 — not from guessing your salary",
                "#FFFBEB", edge=COLORS["accent"], fontsize=9.5)
    save(fig, "session19-04-grounding-show-your-work.png")


def image_05():
    fig, ax = setup_fig(
        "RAG — Search First, Answer Second",
        "Retrieval-Augmented Generation combines two weak-alone skills into one strong pipeline",
    )
    rounded_box(ax, 0.5, 3.2, 5.0, 2.2,
                "RETRIEVAL\nEmbed question → vector search\nTop-k policy chunks\n(Librarian pulls the page)",
                COLORS["returns"], edge=COLORS["primary"], fontsize=9.5, weight="bold")
    rounded_box(ax, 6.5, 3.2, 5.0, 2.2,
                "GENERATION\nLLM reads evidence + question\nWrites clear, polite reply\n(Agent explains the rule)",
                COLORS["refunds"], edge=COLORS["secondary"], fontsize=9.5, weight="bold")
    arrow(ax, 5.5, 4.3, 6.5, 4.3, COLORS["accent"])
    ax.text(6.0, 4.65, "context", fontsize=9, color=COLORS["accent"], ha="center", weight="bold")

    flow = [
        ("Query", 0.6),
        ("Retrieve", 2.5),
        ("Context", 4.4),
        ("Generate", 6.3),
        ("Grounded reply", 8.2),
    ]
    for label, x in flow:
        rounded_box(ax, x, 0.85, 1.7, 0.7, label, COLORS["card"], fontsize=8.5, weight="bold")
    for x1, x2 in [(2.3, 2.5), (4.2, 4.4), (6.1, 6.3), (8.0, 8.2)]:
        arrow(ax, x1, 1.2, x2, 1.2, COLORS["primary"])
    rounded_box(ax, 10.2, 0.85, 1.3, 0.7, "User", COLORS["warn"], edge=COLORS["accent"], fontsize=8.5)
    arrow(ax, 10.2, 1.2, 9.9, 1.2, COLORS["accent"])
    save(fig, "session19-05-rag-search-first-answer-second.png")


def image_06():
    fig, ax = setup_fig(
        "Ungrounded vs Grounded — Same Question, Different Trust",
        "ShopKart: 'How many days to return an unopened phone case?'",
    )
    rounded_box(ax, 0.4, 3.5, 5.4, 0.7, "Ungrounded (LLM-only)", COLORS["card"],
                edge=COLORS["danger"], fontsize=10, weight="bold")
    rounded_box(ax, 0.4, 1.5, 5.4, 1.8,
                '"Most stores offer 15–30 days;\nyou should be fine within two weeks."\n\n✗ Wrong window  ✗ No source',
                "#FEE2E2", edge=COLORS["danger"], fontsize=9)

    rounded_box(ax, 6.2, 3.5, 5.4, 0.7, "Grounded (RAG-style)", COLORS["card"],
                edge=COLORS["success"], fontsize=10, weight="bold")
    rounded_box(ax, 6.2, 1.5, 5.4, 1.8,
                '"Unopened items within\n7 calendar days from delivery."\n\n✓ ShopKart policy  ✓ Traceable chunk',
                "#D1FAE5", edge=COLORS["success"], fontsize=9)

    rounded_box(ax, 0.5, 0.2, 11.0, 0.85,
                "Same polite tone — very different trustworthiness when numbers and eligibility rules matter",
                "#EEF2FF", edge=COLORS["secondary"], fontsize=10, weight="bold")
    save(fig, "session19-06-ungrounded-vs-grounded.png")


def image_07():
    fig, ax = setup_fig(
        "Retrieve Step = Your Vector Search Pipeline",
        "RAG does not replace embedding search — it uses the Chroma top-k you already built",
    )
    offline = [
        ("Index building\n(offline)", "Load policies\nChunk + embed\nChroma upsert", COLORS["returns"], 0.4),
        ("Retrieve\n(online)", "Embed question\nquery top_k\nRead ranked chunks", COLORS["shipping"], 4.2),
        ("Generate\n(online)", "LLM + evidence\nWrite answer\nNext session", COLORS["warranty"], 8.0),
    ]
    for title, body, face, x in offline:
        rounded_box(ax, x, 3.8, 3.4, 0.75, title, face, fontsize=9.5, weight="bold")
        rounded_box(ax, x, 1.8, 3.4, 1.8, body, face, fontsize=8.5)
    arrow(ax, 3.8, 4.15, 4.2, 4.15, COLORS["accent"])
    arrow(ax, 7.6, 4.15, 8.0, 4.15, COLORS["accent"])

    rounded_box(ax, 0.5, 0.25, 5.5, 1.2,
                "Previous lab skills\nupsert · count · peek\nquery · top_k · distance",
                COLORS["card"], edge=COLORS["primary"], fontsize=9)
    rounded_box(ax, 6.0, 0.25, 5.5, 1.2,
                "Same model rule\nOne encoder for\nindex + query",
                COLORS["card"], edge=COLORS["secondary"], fontsize=9)
    save(fig, "session19-07-retrieve-equals-vector-search.png")


def image_08():
    fig, ax = setup_fig(
        "When Retrieval Misses — RAG Quality Depends on Both Steps",
        "RAG quality = retrieval quality × generation discipline",
    )
    failures = [
        ("Wrong chunk", "Refund Q pulls\nshipping text\nPolished but irrelevant", COLORS["danger"], 0.4),
        ("No relevant chunk", "Empty top-k\nLLM may guess\nunless prompt forbids", COLORS["accent"], 4.2),
        ("Right chunk, ignored", "Evidence in prompt\nAnswer adds extra facts\nGeneration failure", COLORS["secondary"], 8.0),
    ]
    for title, body, edge, x in failures:
        rounded_box(ax, x, 3.2, 3.4, 0.75, title, COLORS["card"], edge=edge, fontsize=9.5, weight="bold")
        rounded_box(ax, x, 1.3, 3.4, 1.7, body, COLORS["card"], edge=edge, fontsize=8.5)
    rounded_box(ax, 0.5, 0.2, 11.0, 0.85,
                "Fixing only the LLM prompt cannot fix search that never finds the refund paragraph",
                COLORS["warn"], edge=COLORS["accent"], fontsize=10, weight="bold")
    save(fig, "session19-08-retrieval-failure-modes.png")


def image_09():
    fig, ax = setup_fig(
        "RAG Beyond ShopKart — Common Application Patterns",
        "Same search-first pattern wherever answers must come from documents you control",
    )
    patterns = [
        ("Support bot", "Policies, FAQs", COLORS["returns"]),
        ("Document Q&A", "HR, SOPs, wikis", COLORS["shipping"]),
        ("Education", "Course notes, labs", COLORS["warranty"]),
        ("Agentic workflows", "API docs, runbooks", COLORS["refunds"]),
    ]
    for i, (title, docs, face) in enumerate(patterns):
        x = 0.4 + i * 2.9
        rounded_box(ax, x, 3.4, 2.6, 0.75, title, face, fontsize=9.5, weight="bold")
        rounded_box(ax, x, 2.0, 2.6, 1.2, f"Retrieve:\n{docs}", COLORS["card"], fontsize=8.5)
        arrow(ax, x + 1.3, 2.0, x + 1.3, 1.2, COLORS["primary"])
        rounded_box(ax, x, 0.45, 2.6, 0.65, "Grounded answer", COLORS["card"],
                    edge=COLORS["success"], fontsize=8.5, weight="bold")
    rounded_box(ax, 0.4, 5.15, 11.2, 0.55,
                "Search alone returns chunks  |  RAG turns chunks into a complete, evidence-backed reply",
                "#EEF2FF", edge=COLORS["secondary"], fontsize=9.5)
    save(fig, "session19-09-rag-application-patterns.png")


if __name__ == "__main__":
    image_01()
    image_02()
    image_03()
    image_04()
    image_05()
    image_06()
    image_07()
    image_08()
    image_09()
