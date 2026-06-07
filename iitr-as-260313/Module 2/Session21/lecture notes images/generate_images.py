"""Generate Session 21 (Building a RAG Pipeline) lecture note diagrams — ShopKart theme."""
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
        "ShopKart — From Four Strings to Four Files",
        "Session 20: one string per policy in code  →  Today: real files in policy_documents/",
    )
    rounded_box(ax, 0.4, 4.8, 5.0, 0.65, "Previous lab — POLICY_RECORDS", COLORS["warn"],
                edge=COLORS["accent"], fontsize=10, weight="bold")
    rounded_box(ax, 0.4, 2.8, 5.0, 1.8,
                "4 Python strings\n1 chunk each\nshopkart_policy_kb",
                COLORS["card"], edge=COLORS["muted"], fontsize=9)

    arrow(ax, 5.4, 3.8, 6.6, 3.8, COLORS["accent"])

    rounded_box(ax, 6.6, 4.8, 5.0, 0.65, "Today — policy_documents/", COLORS["success"],
                edge=COLORS["success"], fontsize=10, weight="bold")
    files = [
        ("returns_policy.txt", COLORS["returns"], 6.6),
        ("shipping_policy.txt", COLORS["shipping"], 8.0),
        ("warranty_policy.txt", COLORS["warranty"], 9.4),
        ("refunds_policy.txt", COLORS["refunds"], 10.8),
    ]
    for name, face, x in files:
        rounded_box(ax, x, 2.0, 1.2, 1.5, name.replace("_", "\n"), face, fontsize=7, weight="bold")
    rounded_box(ax, 6.6, 0.9, 5.2, 0.85,
                "Many chunks per file → shopkart_policy_kb_v2",
                COLORS["card"], edge=COLORS["primary"], fontsize=9.5, weight="bold")
    rounded_box(ax, 0.4, 0.9, 5.0, 0.85,
                "Online loop unchanged:\nBGE + Chroma + Groq",
                COLORS["card"], edge=COLORS["secondary"], fontsize=9.5)
    save(fig, "session21-01-four-strings-to-files.png")


def image_02():
    fig, ax = setup_fig(
        "Offline Ingestion Pipeline",
        "Load → clean → chunk → embed → store runs once; customer questions use the online loop",
    )
    steps = [
        ("Policy files\n.txt / .pdf", COLORS["returns"], 0.4),
        ("Load +\nclean", COLORS["shipping"], 2.5),
        ("Chunk\n100w / 20 overlap", COLORS["warranty"], 4.6),
        ("BGE\nembed", COLORS["refunds"], 6.7),
        ("Chroma\nvector store", COLORS["card"], 8.8),
    ]
    for i, (txt, face, x) in enumerate(steps):
        rounded_box(ax, x, 3.5, 1.9, 1.5, txt, face, fontsize=8.5, weight="bold")
        if i < 4:
            arrow(ax, x + 1.9, 4.25, steps[i + 1][2], 4.25, COLORS["primary"])

    rounded_box(ax, 0.4, 0.9, 4.5, 1.8,
                "OFFLINE (once)\nbuild_knowledge_base()",
                COLORS["warn"], edge=COLORS["accent"], fontsize=9.5, weight="bold")
    rounded_box(ax, 5.2, 0.9, 6.4, 1.8,
                "ONLINE (per question)\nQuestion → Retrieve → Groq → Answer",
                COLORS["card"], edge=COLORS["success"], fontsize=9.5, weight="bold")
    arrow(ax, 9.7, 4.25, 10.5, 1.8, COLORS["accent"])
    rounded_box(ax, 10.5, 3.2, 1.1, 1.5, "Q", COLORS["accent"], edge=COLORS["accent"],
                fontsize=11, weight="bold")
    save(fig, "session21-02-ingestion-pipeline.png")


def image_03():
    fig, ax = setup_fig(
        "Document Loaders — TXT and PDF",
        "Each loader returns cleaned text + metadata (source, category, file_type)",
    )
    rounded_box(ax, 0.4, 4.5, 5.2, 0.65, "policy_documents/ folder", COLORS["card"],
                edge=COLORS["primary"], fontsize=10, weight="bold")

    rounded_box(ax, 0.4, 2.2, 2.4, 2.0,
                "load_txt_file\nopen() + read\n1 doc per file",
                COLORS["returns"], edge=COLORS["primary"], fontsize=9, weight="bold")
    rounded_box(ax, 3.2, 2.2, 2.4, 2.0,
                "load_pdf_file\npypdf PdfReader\n1 doc per page",
                COLORS["shipping"], edge=COLORS["secondary"], fontsize=9, weight="bold")

    arrow(ax, 1.6, 4.5, 1.6, 4.2, COLORS["primary"])
    arrow(ax, 4.4, 4.5, 4.4, 4.2, COLORS["secondary"])

    rounded_box(ax, 6.2, 2.5, 5.4, 2.2,
                "Metadata inferred from filename\nreturns_policy.txt → category: returns\nshipping_policy.txt → shipping\nwarranty / refunds likewise",
                COLORS["warn"], edge=COLORS["accent"], fontsize=9)

    rounded_box(ax, 0.5, 0.5, 11.0, 1.0,
                "load_all_policy_documents() scans folder, skips unknown extensions, prints load counts",
                COLORS["card"], edge=COLORS["secondary"], fontsize=9.5)
    save(fig, "session21-03-document-loaders.png")


def image_04():
    fig, ax = setup_fig(
        "Overlap Chunking — 100 Words, 20-Word Tail",
        "Overlap keeps split rules from losing context across chunk boundaries",
    )
    words = ["ShopKart", "Returns", "Policy.", "Unopened", "items", "in", "original",
             "packaging", "may", "be", "returned", "within", "7", "calendar", "days",
             "of", "delivery.", "Opened", "or", "used", "items", "are", "not", "eligible",
             "unless", "defective", "or", "damaged", "on", "arrival."]
    chunk1_end = 20
    chunk2_start = 15
    chunk2_end = 35

    rounded_box(ax, 0.4, 4.8, 11.2, 0.55, "Full cleaned policy text (word stream)", COLORS["card"],
                edge=COLORS["muted"], fontsize=9.5)

    rounded_box(ax, 0.4, 3.2, 7.5, 1.2,
                "Chunk 1 — words 1–20\n" + " ".join(words[:chunk1_end]),
                COLORS["returns"], edge=COLORS["primary"], fontsize=7.5, weight="bold")
    rounded_box(ax, 3.8, 1.6, 7.8, 1.2,
                "Chunk 2 — words 16–35 (20-word overlap)\n" + " ".join(words[chunk2_start:chunk2_end]),
                COLORS["shipping"], edge=COLORS["secondary"], fontsize=7.5, weight="bold")

    rounded_box(ax, 0.4, 1.6, 3.0, 1.2,
                "Overlap zone\nwords 16–20\nshared context",
                COLORS["warn"], edge=COLORS["accent"], fontsize=8.5, weight="bold")
    arrow(ax, 3.4, 2.2, 3.8, 2.2, COLORS["accent"])

    rounded_box(ax, 0.5, 0.35, 11.0, 0.9,
                "DEFAULT_CHUNK_SIZE=100 · DEFAULT_CHUNK_OVERLAP=20 · start += chunk_size - overlap",
                COLORS["card"], edge=COLORS["success"], fontsize=9.5, weight="bold")
    save(fig, "session21-04-overlap-chunking.png")


def image_05():
    fig, ax = setup_fig(
        "Project Structure — shopkart_rag_pipeline",
        "One script, four policy files, local Chroma store, API key in .env",
    )
    tree = """shopkart_rag_pipeline/
├── policy_documents/
│   ├── returns_policy.txt
│   ├── shipping_policy.txt
│   ├── warranty_policy.txt
│   └── refunds_policy.txt
├── .env                  GROQ_API_KEY
├── rag_pipeline.py
└── chroma_store/         auto-created"""
    rounded_box(ax, 0.5, 1.0, 6.5, 4.8, tree, COLORS["card"], edge=COLORS["primary"],
                fontsize=10, weight="bold")

    rounded_box(ax, 7.3, 3.5, 4.2, 2.3,
                "pip install\nchromadb\nsentence-transformers\ngroq · pypdf\ndotenv",
                COLORS["returns"], edge=COLORS["secondary"], fontsize=9, weight="bold")
    rounded_box(ax, 7.3, 1.0, 4.2, 2.2,
                "Never commit .env\nto Git — keys stay\nin environment only",
                COLORS["warn"], edge=COLORS["danger"], fontsize=9.5, weight="bold")
    save(fig, "session21-05-project-structure.png")


def image_06():
    fig, ax = setup_fig(
        "build_knowledge_base — Offline Index",
        "load_all_policy_documents → create_chunks_from_documents → index_policy_chunks",
    )
    steps = [
        ("load_all_policy_documents\n4 files loaded", COLORS["returns"], 0.4),
        ("create_chunks_from_documents\nN chunks > 4", COLORS["shipping"], 3.0),
        ("model.encode\nBGE embeddings", COLORS["warranty"], 5.6),
        ("collection.upsert\nshopkart_policy_kb_v2", COLORS["refunds"], 8.2),
    ]
    for i, (txt, face, x) in enumerate(steps):
        rounded_box(ax, x, 3.4, 2.4, 1.6, txt, face, fontsize=8.5, weight="bold")
        if i < 3:
            arrow(ax, x + 2.4, 4.2, steps[i + 1][2], 4.2, COLORS["primary"])

    rounded_box(ax, 0.5, 0.85, 5.3, 1.8,
                "Chunk id format:\n{category}_{doc_index}_{chunk_index}",
                COLORS["card"], edge=COLORS["accent"], fontsize=9.5)
    rounded_box(ax, 6.0, 0.85, 5.5, 1.8,
                "embedding_function=None\nyou supply vectors manually\n(same pattern as Session 20)",
                COLORS["card"], edge=COLORS["secondary"], fontsize=9.5)
    save(fig, "session21-06-build-knowledge-base.png")


def image_07():
    fig, ax = setup_fig(
        "Many Chunks in Chroma — shopkart_policy_kb_v2",
        "Four policy files produce many searchable rows; top_k=3 retrieves best excerpts",
    )
    files = [
        ("returns\n3 chunks", COLORS["returns"], 0.4),
        ("shipping\n2 chunks", COLORS["shipping"], 2.2),
        ("warranty\n2 chunks", COLORS["warranty"], 4.0),
        ("refunds\n2 chunks", COLORS["refunds"], 5.8),
    ]
    for title, face, x in files:
        rounded_box(ax, x, 4.5, 1.6, 1.0, title, face, fontsize=8.5, weight="bold")
        arrow(ax, x + 0.8, 4.5, 4.0, 2.8, COLORS["primary"])

    rounded_box(ax, 2.8, 1.5, 6.4, 1.5,
                "Chroma collection: shopkart_policy_kb_v2\n~9+ chunks with category + source metadata",
                COLORS["card"], edge=COLORS["accent"], fontsize=10, weight="bold")

    rounded_box(ax, 7.8, 3.8, 3.8, 2.0,
                "Query: phone case return?\nRank 1 → returns\nRank 2 → returns\nRank 3 → refunds",
                COLORS["warn"], edge=COLORS["success"], fontsize=9, weight="bold")

    rounded_box(ax, 0.5, 0.2, 11.0, 0.85,
                "Wrong Rank 1 category? Debug ingestion/chunking — not the generator",
                COLORS["card"], edge=COLORS["danger"], fontsize=9.5, weight="bold")
    save(fig, "session21-07-many-chunks-chroma.png")


def image_08():
    fig, ax = setup_fig(
        "answer_with_rag — Same Loop, Richer Index",
        "Retrieve top_k=3 → print_retrieved_chunks → generate_grounded_answer",
    )
    steps = [
        ("retrieve_policy_chunks\ntop_k = 3", COLORS["returns"], 0.4),
        ("print_retrieved_chunks\nRank · category · distance", COLORS["shipping"], 3.2),
        ("generate_grounded_answer\nGroq + grounded prompt", COLORS["refunds"], 6.0),
    ]
    for i, (txt, face, x) in enumerate(steps):
        rounded_box(ax, x, 3.5, 2.6, 1.6, txt, face, fontsize=9, weight="bold")
        if i < 2:
            arrow(ax, x + 2.6, 4.3, steps[i + 1][2], 4.3, COLORS["accent"])
    rounded_box(ax, 8.8, 3.5, 2.8, 1.6, "Grounded\nShopKart answer", COLORS["success"],
                edge=COLORS["success"], fontsize=9, weight="bold")
    arrow(ax, 8.6, 4.3, 8.8, 4.3, COLORS["primary"])

    rounded_box(ax, 0.5, 0.85, 11.0, 1.6,
                "demo_queries: phone case return · express metro · earphones warranty · COD kettle refund\nVerify numbers: 7 days · 3–5 days · 12 months · 5–7 days · metro express · COD → UPI",
                COLORS["card"], edge=COLORS["secondary"], fontsize=9)
    save(fig, "session21-08-answer-with-rag.png")


def image_09():
    fig, ax = setup_fig(
        "Terminal Verification Checklist",
        "Inspect load counts, chunk totals, Rank 1 category, and grounded numbers every run",
    )
    checks = [
        ("Load\n4 files × 1 doc", COLORS["returns"], 0.4),
        ("Chunk\nTotal > 4", COLORS["shipping"], 2.5),
        ("Index\nN in v2 collection", COLORS["warranty"], 4.6),
        ("Retrieve\nRank 1 category", COLORS["refunds"], 6.7),
        ("Answer\npolicy numbers", COLORS["success"], 8.8),
    ]
    for i, (txt, face, x) in enumerate(checks):
        rounded_box(ax, x, 3.2, 1.9, 1.5, txt, face, fontsize=8.5, weight="bold")
        ax.text(x + 0.95, 2.6, "✓", ha="center", fontsize=18, color=COLORS["success"], weight="bold")
        if i < 4:
            arrow(ax, x + 1.9, 3.95, checks[i + 1][2], 3.95, COLORS["primary"])

    rounded_box(ax, 0.5, 0.5, 11.0, 1.5,
                "If Rank 1 category mismatches the question area → fix loaders, clean_text, or chunk settings\nGeneration tuning and policy refresh workflows come in a later session",
                COLORS["warn"], edge=COLORS["accent"], fontsize=9.5)
    save(fig, "session21-09-verification-checklist.png")


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
