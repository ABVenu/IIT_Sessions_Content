"""Generate Session 20 (RAG Architecture and Pipeline) lecture note diagrams — ShopKart theme."""
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
        "ShopKart Support — Knowledge Boundary",
        "The assistant may only answer from official policy text, not general internet memory",
    )
    rounded_box(ax, 3.5, 5.0, 5.0, 0.7, "ShopKart Policy Rule Book", COLORS["card"],
                edge=COLORS["primary"], fontsize=11, weight="bold")
    stakeholders = [
        ("Customer", "Clear eligibility\n& timelines", COLORS["returns"], 0.4),
        ("Support team", "Fewer wrong\npromises", COLORS["shipping"], 3.3),
        ("Business", "Traceable to\nlive docs", COLORS["warranty"], 6.2),
        ("Outside boundary", "Refuse or\nescalate", COLORS["danger"], 9.1),
    ]
    for title, body, face, x in stakeholders:
        edge = COLORS["danger"] if "Outside" in title else COLORS["primary"]
        rounded_box(ax, x, 3.5, 2.5, 0.65, title, face, edge=edge, fontsize=9.5, weight="bold")
        rounded_box(ax, x, 1.8, 2.5, 1.4, body, face, edge=edge, fontsize=8.5)
        arrow(ax, 6.0, 5.0, x + 1.25, 3.15, COLORS["accent"])
    rounded_box(ax, 0.5, 0.2, 11.0, 0.85,
                "Knowledge boundary = allowed topics & documents  |  Like a bank agent quoting only the published brochure",
                "#EEF2FF", edge=COLORS["secondary"], fontsize=9.5)
    save(fig, "session20-01-knowledge-boundary.png")


def image_02():
    fig, ax = setup_fig(
        "Four Policy Areas → Chroma Chunks",
        "Each policy row becomes one searchable knowledge source in today's lab",
    )
    policies = [
        ("Returns", "7 days\nunopened", COLORS["returns"], 0.4),
        ("Shipping", "3–5 days\nexpress metros", COLORS["shipping"], 3.2),
        ("Warranty", "12 months\nno liquid", COLORS["warranty"], 6.0),
        ("Refunds", "5–7 days\nCOD → UPI", COLORS["refunds"], 8.8),
    ]
    for title, body, face, x in policies:
        rounded_box(ax, x, 3.8, 2.5, 0.7, title, face, fontsize=10, weight="bold")
        rounded_box(ax, x, 2.0, 2.5, 1.6, body, face, fontsize=8.5)
        arrow(ax, x + 1.25, 2.0, 6.0, 1.0, COLORS["primary"])
    rounded_box(ax, 3.8, 0.35, 4.4, 1.0,
                "Chroma collection\nshopkart_policy_kb (4 rows)",
                COLORS["card"], edge=COLORS["accent"], fontsize=10, weight="bold")
    rounded_box(ax, 0.5, 5.1, 11.0, 0.55,
                "Retriever must find Returns + Refunds for return questions — not Warranty alone",
                COLORS["warn"], edge=COLORS["accent"], fontsize=9.5)
    save(fig, "session20-02-policy-chunks-chroma.png")


def image_03():
    fig, ax = setup_fig(
        "Three Components — Minimal RAG Pipeline",
        "Knowledge sources + Retriever + Generator wired into one ShopKart loop",
    )
    rounded_box(ax, 0.4, 3.5, 3.5, 2.0,
                "Knowledge sources\nPOLICY_RECORDS\n→ Chroma upsert",
                COLORS["returns"], edge=COLORS["primary"], fontsize=9.5, weight="bold")
    rounded_box(ax, 4.2, 3.5, 3.5, 2.0,
                "Retriever\nSentenceTransformer\n+ collection.query top_k",
                COLORS["shipping"], edge=COLORS["secondary"], fontsize=9.5, weight="bold")
    rounded_box(ax, 8.0, 3.5, 3.5, 2.0,
                "Generator\nOpenAI chat API\nwrites from evidence",
                COLORS["refunds"], edge=COLORS["success"], fontsize=9.5, weight="bold")

    flow = [
        ("Customer\nquestion", 0.5),
        ("Retrieve\ntop-k", 2.8),
        ("Context", 5.1),
        ("Generate", 7.4),
        ("Grounded\nanswer", 9.7),
    ]
    for label, x in flow:
        rounded_box(ax, x, 0.6, 1.9, 0.85, label, COLORS["card"], fontsize=8.5, weight="bold")
    for x1, x2 in [(2.4, 2.8), (4.7, 5.1), (7.0, 7.4), (9.3, 9.7)]:
        arrow(ax, x1, 1.0, x2, 1.0, COLORS["accent"])
    arrow(ax, 3.9, 4.5, 4.2, 4.5, COLORS["primary"])
    arrow(ax, 7.7, 4.5, 8.0, 4.5, COLORS["primary"])
    rounded_box(ax, 0.5, 5.1, 11.0, 0.55,
                "Vector search alone ≠ RAG — generation with use-this-evidence rules completes the assistant",
                "#EEF2FF", edge=COLORS["secondary"], fontsize=9.5)
    save(fig, "session20-03-three-rag-components.png")


def image_04():
    fig, ax = setup_fig(
        "Lab Stack — Chroma + Embeddings + OpenAI",
        "Retriever runs locally; generator calls a hosted LLM with OPENAI_API_KEY",
    )
    rounded_box(ax, 0.5, 3.2, 3.4, 2.3,
                "chromadb\nPersistentClient\nupsert · query",
                COLORS["returns"], edge=COLORS["primary"], fontsize=9.5, weight="bold")
    rounded_box(ax, 4.3, 3.2, 3.4, 2.3,
                "sentence-transformers\nall-MiniLM-L6-v2\nsame model for index + query",
                COLORS["shipping"], edge=COLORS["secondary"], fontsize=9.5, weight="bold")
    rounded_box(ax, 8.1, 3.2, 3.4, 2.3,
                "openai\nchat.completions\nGENERATION_MODEL",
                COLORS["refunds"], edge=COLORS["success"], fontsize=9.5, weight="bold")
    rounded_box(ax, 0.5, 0.9, 5.5, 1.5,
                "API key in environment\nNever commit keys to Git",
                COLORS["warn"], edge=COLORS["accent"], fontsize=9.5, weight="bold")
    rounded_box(ax, 6.0, 0.9, 5.5, 1.5,
                "Folder: shopkart_rag_lab\n./chroma_store stays consistent",
                COLORS["card"], edge=COLORS["primary"], fontsize=9.5)
    save(fig, "session20-04-lab-stack.png")


def image_05():
    fig, ax = setup_fig(
        "Step 2 — Index Policy Records in Chroma",
        "Offline: embed POLICY_RECORDS → upsert ids, documents, metadata, embeddings",
    )
    steps = [
        ("POLICY_RECORDS\n4 dict rows", 0.4),
        ("model.encode\nbatch embed", 2.8),
        ("collection.upsert\nids + vectors", 5.2),
        ("count() = 4\nready to query", 7.6),
    ]
    for i, (txt, x) in enumerate(steps):
        face = [COLORS["returns"], COLORS["shipping"], COLORS["warranty"], COLORS["refunds"]][i]
        rounded_box(ax, x, 3.2, 2.2, 1.5, txt, face, fontsize=8.5, weight="bold")
        if i < 3:
            arrow(ax, x + 2.2, 3.95, steps[i + 1][1], 3.95, COLORS["primary"])
    rounded_box(ax, 0.5, 0.9, 11.0, 1.4,
                "embedding_function=None → you supply vectors manually\nSame teaching pattern as previous Chroma lab",
                COLORS["card"], edge=COLORS["secondary"], fontsize=9.5)
    save(fig, "session20-05-index-chroma.png")


def image_06():
    fig, ax = setup_fig(
        "Step 3 — Retriever: Semantic Top-k Search",
        "Embed question → query nearest policy vectors → return ranked excerpts",
    )
    rounded_box(ax, 0.4, 4.0, 2.8, 1.2, "Customer query\n'COD refund to UPI?'", COLORS["card"],
                edge=COLORS["accent"], fontsize=9)
    arrow(ax, 3.2, 4.6, 4.0, 4.6, COLORS["accent"])
    rounded_box(ax, 4.0, 3.8, 3.2, 1.4,
                "model.encode([query])\n→ query_embedding",
                COLORS["shipping"], edge=COLORS["secondary"], fontsize=9, weight="bold")
    arrow(ax, 7.2, 4.6, 8.0, 4.6, COLORS["primary"])
    rounded_box(ax, 8.0, 3.5, 3.6, 1.8,
                "collection.query\nn_results=top_k\nRank 1 · Rank 2\ndistance scores",
                COLORS["returns"], edge=COLORS["primary"], fontsize=9, weight="bold")

    rounded_box(ax, 0.5, 0.9, 5.3, 2.0,
                "Retriever does NOT call LLM\nOnly returns evidence dicts",
                COLORS["card"], edge=COLORS["success"], fontsize=9.5)
    rounded_box(ax, 6.0, 0.9, 5.5, 2.0,
                "Semantic = match by meaning\nnot exact keywords",
                COLORS["card"], edge=COLORS["accent"], fontsize=9.5)
    save(fig, "session20-06-retriever-topk.png")


def image_07():
    fig, ax = setup_fig(
        "Step 4 — Grounded Prompt + Generator",
        "Stitch excerpts + strict rules → LLM writes only from evidence",
    )
    rounded_box(ax, 0.4, 3.6, 3.0, 1.8,
                "Retrieved chunks\nExcerpt 1, 2\n+ metadata source",
                COLORS["returns"], edge=COLORS["primary"], fontsize=9, weight="bold")
    arrow(ax, 3.4, 4.5, 4.2, 4.5, COLORS["accent"])
    rounded_box(ax, 4.2, 3.4, 3.6, 2.0,
                "build_grounded_prompt\nRules 1–4\nuse ONLY excerpts",
                COLORS["warn"], edge=COLORS["accent"], fontsize=9, weight="bold")
    arrow(ax, 7.8, 4.5, 8.6, 4.5, COLORS["primary"])
    rounded_box(ax, 8.6, 3.6, 3.0, 1.8,
                "chat.completions\nsystem + user\nGrounded answer",
                COLORS["refunds"], edge=COLORS["success"], fontsize=9, weight="bold")
    rounded_box(ax, 0.5, 0.85, 11.0, 1.5,
                "Rule 2: admit insufficient policy info — better than fluent invention",
                COLORS["card"], edge=COLORS["danger"], fontsize=9.5)
    save(fig, "session20-07-grounded-generator.png")


def image_08():
    fig, ax = setup_fig(
        "LLM-Only Baseline vs Full RAG",
        "Same model — only context changes; RAG cites ShopKart's exact numbers",
    )
    rounded_box(ax, 0.4, 3.5, 5.4, 0.7, "LLM-only (no retrieval)", COLORS["card"],
                edge=COLORS["danger"], fontsize=10, weight="bold")
    rounded_box(ax, 0.4, 1.4, 5.4, 1.9,
                '"Usually 3–5 days"\nGeneric industry guess\n✗ No policy excerpt',
                "#FEE2E2", edge=COLORS["danger"], fontsize=9)

    rounded_box(ax, 6.2, 3.5, 5.4, 0.7, "RAG (retrieve + generate)", COLORS["card"],
                edge=COLORS["success"], fontsize=10, weight="bold")
    rounded_box(ax, 6.2, 1.4, 5.4, 1.9,
                '"5–7 business days after\nwarehouse verification; COD → UPI"\n✓ From refunds chunk',
                "#D1FAE5", edge=COLORS["success"], fontsize=9)

    rounded_box(ax, 0.5, 0.15, 11.0, 0.85,
                "COD kettle refund demo — reproduce ungrounded vs grounded gap from Session 19 in code",
                "#EEF2FF", edge=COLORS["secondary"], fontsize=9.5, weight="bold")
    save(fig, "session20-08-llm-only-vs-rag.png")


def image_09():
    fig, ax = setup_fig(
        "answer_with_rag — Full Minimal Loop",
        "Retrieve first → inspect ranks → generate second (order matters)",
    )
    steps = [
        ("A: retrieve_policy_chunks\ntop_k=2", COLORS["returns"], 0.4),
        ("B: print_retrieved_chunks\ncategory · distance", COLORS["shipping"], 3.2),
        ("C: generate_grounded_answer\npolicy-backed reply", COLORS["refunds"], 6.0),
    ]
    for i, (txt, face, x) in enumerate(steps):
        rounded_box(ax, x, 3.5, 2.6, 1.6, txt, face, fontsize=9, weight="bold")
        if i < 2:
            arrow(ax, x + 2.6, 4.3, steps[i + 1][2], 4.3, COLORS["accent"])
    rounded_box(ax, 8.8, 3.5, 2.8, 1.6, "Return to\ncustomer / UI", COLORS["success"],
                edge=COLORS["success"], fontsize=9, weight="bold")
    arrow(ax, 8.6, 4.3, 8.8, 4.3, COLORS["primary"])

    rounded_box(ax, 0.5, 0.85, 11.0, 1.6,
                "main() runs demo_queries: LLM-only print → then RAG with retrieval inspection\nSwap retrieve/generate order → breaks grounding",
                COLORS["card"], edge=COLORS["secondary"], fontsize=9.5)
    save(fig, "session20-09-answer-with-rag-loop.png")


def image_10():
    fig, ax = setup_fig(
        "End-to-End — Offline Index, Online RAG",
        "Policy indexed once; each customer question triggers retrieve → ground → generate",
    )
    rounded_box(ax, 0.4, 5.0, 3.0, 0.65, "OFFLINE", COLORS["warn"], edge=COLORS["accent"],
                fontsize=10, weight="bold")
    rounded_box(ax, 0.4, 3.5, 3.0, 1.3, "POLICY_RECORDS\nembed → upsert", COLORS["returns"],
                fontsize=9, weight="bold")
    arrow(ax, 3.4, 4.15, 4.2, 4.15, COLORS["primary"])
    rounded_box(ax, 4.2, 3.5, 2.8, 1.3, "Chroma\nshopkart_policy_kb", COLORS["shipping"],
                fontsize=9, weight="bold")

    rounded_box(ax, 7.2, 5.0, 4.4, 0.65, "ONLINE (per question)", COLORS["warn"], edge=COLORS["accent"],
                fontsize=10, weight="bold")
    online = [
        ("Embed\nquestion", 7.2),
        ("top-k\nquery", 8.6),
        ("Grounded\nprompt", 10.0),
    ]
    for txt, x in online:
        rounded_box(ax, x, 3.5, 1.2, 1.3, txt, COLORS["card"], fontsize=8, weight="bold")
    arrow(ax, 8.4, 4.15, 8.6, 4.15, COLORS["accent"])
    arrow(ax, 9.8, 4.15, 10.0, 4.15, COLORS["accent"])
    rounded_box(ax, 10.0, 2.0, 1.8, 1.2, "LLM\nreply", COLORS["refunds"], fontsize=8.5, weight="bold")
    arrow(ax, 10.6, 3.5, 10.9, 3.2, COLORS["success"])

    rounded_box(ax, 0.5, 0.2, 11.0, 1.2,
                "Two checks: retrieval intent match (Rank 1 category) + generation follows evidence (numbers in excerpt)",
                COLORS["card"], edge=COLORS["secondary"], fontsize=9.5)
    save(fig, "session20-10-end-to-end-pipeline.png")


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
    image_10()
