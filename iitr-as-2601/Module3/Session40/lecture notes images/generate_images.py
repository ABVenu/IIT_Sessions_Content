"""Generate Session 40 lecture note diagrams with a consistent theme."""
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
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
    "chunk1": "#DBEAFE",
    "chunk2": "#E9D5FF",
    "chunk3": "#FFEDD5",
    "overlap": "#FDE68A",
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
        "From One FAQ Line to Many Searchable Chunks",
        "Previous lab: one sentence = one Chroma row  |  This session: split long policies into labelled chunks",
    )
    rounded_box(ax, 0.4, 3.6, 5.2, 1.6, "Previous lab\nOne FAQ sentence\n= one Chroma row\nmetadata: category",
                COLORS["chunk1"], edge=COLORS["primary"])
    rounded_box(ax, 6.4, 3.6, 5.2, 1.6, "This session\nOne chunk = one Chroma row\nmetadata: source_id, page, chunk_index",
                COLORS["chunk2"], edge=COLORS["secondary"])
    arrow(ax, 5.6, 4.4, 6.4, 4.4, COLORS["accent"])
    ax.text(5.85, 4.65, "split", fontsize=9, color=COLORS["accent"], ha="center", weight="bold")

    rounded_box(ax, 0.8, 1.0, 10.4, 2.0,
                "ShopEasy 40-page policy PDF  -->  many small search cards  -->  each card embedded & stored in Chroma",
                "#EEF2FF", edge=COLORS["secondary"], fontsize=11, weight="bold")
    ax.text(0.8, 0.45, "Real-life: pull one highlighted section with page number — not the whole module photocopy",
            fontsize=9, color=COLORS["muted"])
    save(fig, "session40-01-faq-to-chunks.png")


def image_02():
    fig, ax = setup_fig("Why Chunking Matters", "Each search card should hold roughly one idea")
    cards = [
        ("Whole file -> one vector", "Meaning gets averaged\nShipping Q matches returns text", COLORS["danger"]),
        ("Chunk too large", "Rank 1 returns a wall of text\nHard to use in a prompt", COLORS["accent"]),
        ("Chunk too small", "Fragment: 'within 30 days'\nLoses returns context", COLORS["secondary"]),
    ]
    xs = [0.5, 4.2, 7.9]
    for i, (title, body, edge) in enumerate(cards):
        rounded_box(ax, xs[i], 3.2, 3.2, 1.0, title, COLORS["card"], edge=edge, fontsize=10, weight="bold")
        rounded_box(ax, xs[i], 1.5, 3.2, 1.5, body, COLORS["card"], edge=edge, fontsize=9)
    rounded_box(ax, 1.5, 0.35, 9.0, 0.85,
                "Chunking sits BEFORE embedding and BEFORE Chroma upsert",
                COLORS["success"], edge=COLORS["success"], fontsize=11, weight="bold")
    save(fig, "session40-02-why-chunking-matters.png")


def image_03():
    fig, ax = setup_fig(
        "Fixed Size + Overlap Strategy",
        "Slide a window of chunk_size characters; step forward by chunk_size - overlap",
    )
    text = (
        "ShopEasy Return Policy. Customers may return unused products within 30 days of delivery. "
        "Items must be in original packaging. To start a return, open Orders and tap Request Return."
    )
    ax.text(0.4, 5.2, text, fontsize=8.5, color=COLORS["text"], wrap=True)

    # chunk windows
    starts = [0.4, 2.6, 4.8, 7.0]
    widths = [2.0, 2.0, 2.0, 2.0]
    labels = ["Chunk 0", "Chunk 1", "Chunk 2", "Chunk 3"]
    faces = [COLORS["chunk1"], COLORS["chunk2"], COLORS["chunk3"], COLORS["chunk1"]]
    for x, w, label, face in zip(starts, widths, labels, faces):
        rect = FancyBboxPatch((x, 3.5), w, 1.1, boxstyle="round,pad=0.02,rounding_size=0.1",
                              linewidth=1.5, edgecolor=COLORS["primary"], facecolor=face, alpha=0.95)
        ax.add_patch(rect)
        ax.text(x + w / 2, 4.05, label, ha="center", va="center", fontsize=9, weight="bold")

    overlap = FancyBboxPatch((2.3, 3.5), 0.5, 1.1, boxstyle="round,pad=0.02,rounding_size=0.05",
                             linewidth=1.2, edgecolor=COLORS["accent"], facecolor=COLORS["overlap"], alpha=0.9)
    ax.add_patch(overlap)
    ax.text(2.55, 2.95, "overlap\n75 chars", ha="center", fontsize=8, color=COLORS["accent"], weight="bold")

    rounded_box(ax, 0.4, 1.2, 5.5, 1.2, "chunk_size = 500\n~2-4 policy sentences", COLORS["card"])
    rounded_box(ax, 6.2, 1.2, 5.4, 1.2, "overlap = 75 (~15%)\nshared margin at boundaries", COLORS["card"], edge=COLORS["accent"])
    rounded_box(ax, 0.4, 0.2, 11.2, 0.75, "Step size = chunk_size - overlap  |  Rule: overlap must be < chunk_size",
                "#EEF2FF", edge=COLORS["secondary"], fontsize=10)
    save(fig, "session40-03-sliding-window-overlap.png")


def image_04():
    fig, ax = setup_fig("Chunk Size Trade-offs", "Justify your number — one idea per chunk")
    items = [
        ("Too small\n~80 chars", "Loses context\n'within 30 days' alone", COLORS["danger"], 0.5),
        ("Lab default\n500 chars", "Balanced\n2-4 policy sentences", COLORS["success"], 4.2),
        ("Too large\n~4000 chars", "Few chunks\nBlurry embeddings", COLORS["accent"], 7.9),
    ]
    for title, body, edge, x in items:
        rounded_box(ax, x, 3.4, 3.0, 1.0, title, COLORS["card"], edge=edge, fontsize=10, weight="bold")
        rounded_box(ax, x, 1.8, 3.0, 1.4, body, COLORS["card"], edge=edge, fontsize=9)
    ax.annotate("", xy=(4.0, 2.2), xytext=(3.5, 2.2),
                arrowprops=dict(arrowstyle="<->", color=COLORS["primary"], lw=2))
    ax.annotate("", xy=(7.7, 2.2), xytext=(7.2, 2.2),
                arrowprops=dict(arrowstyle="<->", color=COLORS["primary"], lw=2))
    ax.text(6.0, 2.2, "sweet spot", ha="center", fontsize=10, color=COLORS["success"], weight="bold")
    rounded_box(ax, 1.0, 0.25, 10.0, 0.9,
                "Samosa analogy: too small loses filling; too large is not bite-sized",
                "#FFFBEB", edge=COLORS["accent"], fontsize=10)
    save(fig, "session40-04-chunk-size-tradeoffs.png")


def image_05():
    fig, ax = setup_fig("Metadata for Traceability", "Labels on the folder — not the paragraph itself")
    rounded_box(ax, 0.5, 4.0, 3.0, 1.5, "Parent record\nreturns_policy.txt\npage: 0", COLORS["chunk1"])
    steps = [
        (4.0, 4.5, "chunk_text()\nsplit into pieces"),
        (7.0, 4.5, "copy source_id\n+ page to each chunk"),
        (10.0, 4.5, "add chunk_index\n+ stable id"),
    ]
    for x, y, txt in steps:
        rounded_box(ax, x, y, 2.5, 1.0, txt, COLORS["card"], fontsize=8.5)
    arrow(ax, 3.5, 4.75, 4.0, 4.75)
    arrow(ax, 6.5, 4.75, 7.0, 4.75)
    arrow(ax, 9.5, 4.75, 10.0, 4.75)

    chunks = [
        ("returns_policy.txt__p0__c0", "source_id, page, chunk_index: 0", COLORS["chunk1"]),
        ("returns_policy.txt__p0__c1", "source_id, page, chunk_index: 1", COLORS["chunk2"]),
        ("returns_policy.txt__p0__c2", "source_id, page, chunk_index: 2", COLORS["chunk3"]),
    ]
    for i, (cid, meta, face) in enumerate(chunks):
        rounded_box(ax, 0.8 + i * 3.7, 1.5, 3.2, 1.8, f"{cid}\n{meta}", face, fontsize=8)

    rounded_box(ax, 0.5, 0.2, 11.0, 0.85, "Only text is embedded — metadata stored for citation & filters",
                "#EEF2FF", edge=COLORS["secondary"], fontsize=10, weight="bold")
    save(fig, "session40-05-metadata-traceability.png")


def image_06():
    fig, ax = setup_fig("Persist Chunked Documents in Chroma", "Same pipeline as FAQ lab — more rows, richer metadata")
    boxes = [
        (0.4, 3.8, "sample_corpus\n+ chunking", COLORS["chunk1"]),
        (2.8, 3.8, "chunks list\nid, text, metadata", COLORS["chunk2"]),
        (5.2, 3.8, "SentenceTransformer\nall-MiniLM-L6-v2", COLORS["chunk3"]),
        (7.8, 3.8, "collection.upsert\npolicy_chunks", COLORS["chunk1"]),
        (10.2, 3.8, "query top-k\nread metadata", COLORS["chunk2"]),
    ]
    for x, y, txt, face in boxes:
        rounded_box(ax, x, y, 2.1, 1.3, txt, face, fontsize=8.5, weight="bold")
    for x1, x2 in [(2.5, 2.8), (4.9, 5.2), (7.3, 7.8), (9.9, 10.2)]:
        arrow(ax, x1, 4.45, x2, 4.45)

    rounded_box(ax, 0.5, 1.6, 5.3, 1.6,
                "Index-aligned lists\nids[i], documents[i],\nmetadatas[i], embeddings[i]\n= same chunk",
                COLORS["card"], edge=COLORS["success"])
    rounded_box(ax, 6.2, 1.6, 5.3, 1.6,
                "Same model rule\nOne encoder for all chunks\nand every query",
                COLORS["card"], edge=COLORS["secondary"])
    rounded_box(ax, 0.5, 0.25, 11.0, 0.9,
                "FAQ rows stay in support_knowledge_base  |  policy chunks go to policy_chunks",
                "#EEF2FF", edge=COLORS["primary"], fontsize=10)
    save(fig, "session40-06-chroma-chunk-pipeline.png")


def image_07():
    fig, ax = setup_fig("Document Preparation — RAG Prepare Stage", "Load, chunk, tag, embed, store")
    stages = [
        ("Load", ".txt / PDF\n-> corpus list", COLORS["chunk1"]),
        ("Chunk", "fixed size\n+ overlap", COLORS["chunk2"]),
        ("Tag", "source_id\npage, chunk_index", COLORS["chunk3"]),
        ("Embed", "all-MiniLM-L6-v2\nvectors", COLORS["chunk1"]),
        ("Store", "Chroma upsert\npolicy_chunks", COLORS["chunk2"]),
    ]
    for i, (title, body, face) in enumerate(stages):
        x = 0.35 + i * 2.35
        rounded_box(ax, x, 3.5, 2.0, 0.7, title, face, fontsize=11, weight="bold")
        rounded_box(ax, x, 2.2, 2.0, 1.1, body, COLORS["card"], fontsize=8.5)
        if i < len(stages) - 1:
            arrow(ax, x + 2.0, 3.85, x + 2.35, 3.85, COLORS["accent"])

    rounded_box(ax, 0.5, 0.85, 5.5, 1.0, "Weak retrieval? Tune chunk size / overlap first",
                COLORS["card"], edge=COLORS["danger"], fontsize=10)
    rounded_box(ax, 6.3, 0.85, 5.2, 1.0, "Next: prompt assembly & full RAG chatbot",
                COLORS["card"], edge=COLORS["success"], fontsize=10)
    save(fig, "session40-07-document-prep-pipeline.png")


if __name__ == "__main__":
    image_01()
    image_02()
    image_03()
    image_04()
    image_05()
    image_06()
    image_07()
