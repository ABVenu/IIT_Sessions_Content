"""Generate Session 40 lecture note diagrams — LangChain RAG pipeline."""
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
        "Why RAG Exists — Company Policies vs Plain LLM",
        "LLMs know public data; RAG connects your internal policy store at query time",
    )
    rounded_box(ax, 0.4, 3.4, 5.2, 2.2,
                "Plain LLM chatbot\nTrained on public internet\nNo return/refund rules\nMay guess wrong answers",
                COLORS["card"], edge=COLORS["danger"], fontsize=9)
    rounded_box(ax, 6.4, 3.4, 5.2, 2.2,
                "RAG support bot\nVector DB = your policies\nRetrieve relevant chunks\nAnswer from documents",
                COLORS["ingest"], edge=COLORS["success"], fontsize=9)
    arrow(ax, 5.6, 4.5, 6.4, 4.5, COLORS["accent"])
    ax.text(5.85, 4.9, "+ RAG", fontsize=9, color=COLORS["accent"], ha="center", weight="bold")
    rounded_box(ax, 0.5, 0.9, 11.0, 1.8,
                "Fine-tuning = small behaviour tweaks  |  RAG = large, changing document corpora\n"
                "E-commerce bot must quote return_policy.md — not generic web advice",
                "#EEF2FF", edge=COLORS["secondary"], fontsize=10)
    save(fig, "session40-01-why-rag-exists.png")


def image_02():
    fig, ax = setup_fig(
        "Typical RAG Flow — Prepare Once, Answer Many Times",
        "Offline ingest vs online retrieve-then-generate",
    )
    rounded_box(ax, 0.4, 4.6, 11.2, 0.65, "OFFLINE (one-time until docs change)", COLORS["ingest"],
                edge=COLORS["primary"], fontsize=10, weight="bold")
    offline = ["Create files", "Document loader", "Text splitter", "Embeddings", "Chroma persist"]
    for i, step in enumerate(offline):
        x = 0.4 + i * 2.25
        rounded_box(ax, x, 3.5, 2.0, 0.85, step, COLORS["card"], fontsize=8.5)
        if i < len(offline) - 1:
            arrow(ax, x + 2.0, 3.95, x + 2.25, 3.95, COLORS["accent"])

    rounded_box(ax, 0.4, 2.35, 11.2, 0.65, "ONLINE (every user question)", COLORS["query"],
                edge=COLORS["accent"], fontsize=10, weight="bold")
    online = ["User question", "Retriever", "Prompt + context", "LLM", "Final answer"]
    for i, step in enumerate(online):
        x = 0.4 + i * 2.25
        rounded_box(ax, x, 1.2, 2.0, 0.85, step, COLORS["card"], fontsize=8.5)
        if i < len(online) - 1:
            arrow(ax, x + 2.0, 1.65, x + 2.25, 1.65, COLORS["success"])

    rounded_box(ax, 0.5, 0.2, 11.0, 0.75, "Search first, speak second — retrieve top-k chunks before generation",
                COLORS["chroma"], edge=COLORS["success"], fontsize=10, weight="bold")
    save(fig, "session40-02-rag-flow-offline-online.png")


def image_03():
    fig, ax = setup_fig(
        "Chunkification — One Big Policy vs Searchable Chunks",
        "chunk_size=800, chunk_overlap=120 keeps context at boundaries",
    )
    rounded_box(ax, 0.4, 3.8, 4.5, 2.2,
                "Whole PDF → 1 vector\nTopics blend together\nRefund query may match\nshipping text",
                COLORS["card"], edge=COLORS["danger"], fontsize=9)
    rounded_box(ax, 5.2, 3.8, 6.4, 2.2,
                "Split into chunks\nEach chunk ≈ one idea\nOverlap repeats tail\nBetter similarity search",
                COLORS["ingest"], edge=COLORS["success"], fontsize=9)
    arrow(ax, 4.9, 4.9, 5.2, 4.9, COLORS["accent"])

    chunks = ["return_policy\nchunk 1", "return_policy\nchunk 2", "shipping\nchunk 1"]
    for i, label in enumerate(chunks):
        rounded_box(ax, 0.5 + i * 3.8, 1.5, 3.4, 1.5, label, COLORS["card"], edge=COLORS["primary"], fontsize=9)
        if i < 2:
            ax.plot([4.0 + i * 3.8, 4.3 + i * 3.8], [2.25, 2.25], color=COLORS["muted"], linestyle="--", lw=1)

    rounded_box(ax, 0.5, 0.25, 11.0, 0.85,
                "Netflix streams 1-min chunks — RAG stores policy chunks the same way",
                "#EEF2FF", edge=COLORS["secondary"], fontsize=10)
    save(fig, "session40-03-chunkification.png")


def image_04():
    fig, ax = setup_fig(
        "LangChain RAG Components",
        "Six building blocks implemented in this session",
    )
    components = [
        ("1. Document loader", "DirectoryLoader\nTextLoader\n**/*.md", COLORS["ingest"]),
        ("2. Text splitter", "RecursiveCharacter\nTextSplitter\n800 / 120", COLORS["card"]),
        ("3. Embeddings", "OpenAIEmbeddings\ntext-embedding-3-small\n1536 dims", COLORS["query"]),
        ("4. Chroma", "persist_directory\nchroma_db\ncollection", COLORS["chroma"]),
        ("5. Retriever", "as_retriever()\nsimilarity, k=3", COLORS["card"]),
        ("6. LCEL chain", "prompt | llm\nStrOutputParser", COLORS["llm"]),
    ]
    for i, (title, body, face) in enumerate(components):
        row, col = i // 3, i % 3
        x = 0.4 + col * 3.9
        y = 4.5 - row * 2.3
        rounded_box(ax, x, y, 3.5, 0.55, title, face, fontsize=9, weight="bold")
        rounded_box(ax, x, y - 1.35, 3.5, 1.2, body, COLORS["card"], fontsize=8.5)
        if col < 2:
            arrow(ax, x + 3.5, y - 0.55, x + 3.9, y - 0.55, COLORS["accent"])
        elif row == 0:
            arrow(ax, x + 1.75, y - 1.35, x + 1.75, y - 1.65, COLORS["accent"])

    rounded_box(ax, 0.5, 0.2, 11.0, 0.7, "Ingest once → RAG app reloads Chroma without re-embedding every query",
                "#EEF2FF", edge=COLORS["primary"], fontsize=10)
    save(fig, "session40-04-langchain-components.png")


def image_05():
    fig, ax = setup_fig(
        "Production File Layout — Four Python Scripts",
        "Run in order: create_corpus → ingest → (optional retriever) → rag_app",
    )
    files = [
        ("langchain_rag_create_corpus.py", "Dictionary → .md files\ndocuments/", COLORS["ingest"]),
        ("langchain_rag_ingest.py", "Load, split, embed\npersist chroma_db", COLORS["chroma"]),
        ("langchain_rag.py", "Optional retriever\ntest only", COLORS["card"]),
        ("langchain_rag_app.py", "LCEL RAG chain\nLLM + guardrails", COLORS["llm"]),
    ]
    for i, (fname, desc, face) in enumerate(files):
        y = 4.8 - i * 1.35
        rounded_box(ax, 0.5, y, 5.5, 0.55, f"Step {i + 1}", face, fontsize=10, weight="bold")
        rounded_box(ax, 0.5, y - 0.95, 5.5, 0.85, f"{fname}\n{desc}", COLORS["card"], fontsize=8.5)
        if i < len(files) - 1:
            arrow(ax, 3.25, y - 0.95, 3.25, y - 1.15, COLORS["accent"])

    rounded_box(ax, 6.2, 1.5, 5.3, 3.5,
                "E-commerce policy corpus:\n• return_policy.md\n• refund_policy.md\n• shipping_policy.md\n"
                "• warranty_policy.md\n• cancellation_policy.md",
                COLORS["query"], edge=COLORS["accent"], fontsize=9)
    save(fig, "session40-05-four-file-layout.png")


def image_06():
    fig, ax = setup_fig(
        "Ingest Pipeline — Load to Persisted Chroma",
        "DirectoryLoader → splitter → OpenAIEmbeddings → add_documents",
    )
    steps = [
        ("Load", "DirectoryLoader\nglob **/*.md\n5 policy files", COLORS["ingest"]),
        ("Split", "chunk_size 800\noverlap 120\nadd_start_index", COLORS["card"]),
        ("Embed", "text-embedding-3-small\nsame model at query", COLORS["query"]),
        ("Store", "Chroma persist\nchroma_db/\ne_commerce_policy_docs", COLORS["chroma"]),
    ]
    for i, (title, body, face) in enumerate(steps):
        x = 0.35 + i * 2.95
        rounded_box(ax, x, 4.2, 2.6, 0.55, title, face, fontsize=10, weight="bold")
        rounded_box(ax, x, 2.5, 2.6, 1.45, body, COLORS["card"], fontsize=8.5)
        if i < len(steps) - 1:
            arrow(ax, x + 2.6, 4.5, x + 2.95, 4.5, COLORS["accent"])

    rounded_box(ax, 0.5, 0.85, 5.3, 1.2, "Edit return_policy.md?\nRe-run ingest!\nVectors lag behind files",
                COLORS["card"], edge=COLORS["danger"], fontsize=9)
    rounded_box(ax, 6.0, 0.85, 5.5, 1.2, "Optional: shutil.rmtree\nbefore re-ingest\ncleans stale vectors",
                COLORS["card"], edge=COLORS["success"], fontsize=9)
    save(fig, "session40-06-ingest-pipeline.png")


def image_07():
    fig, ax = setup_fig(
        "LCEL RAG Chain",
        "RunnablePassthrough + retriever | format_docs → prompt → LLM → StrOutputParser()",
    )
    rounded_box(ax, 0.4, 4.5, 2.2, 1.0, "User\nquestion", COLORS["query"], edge=COLORS["accent"], fontsize=9)

    rounded_box(ax, 3.0, 5.0, 2.5, 0.8, "RunnablePassthrough", COLORS["card"], fontsize=8.5)
    rounded_box(ax, 3.0, 3.8, 2.5, 0.9, "retriever | format_docs\n→ {context}", COLORS["chroma"], fontsize=8.5)

    arrow(ax, 2.6, 4.8, 3.0, 5.4, COLORS["primary"])
    arrow(ax, 2.6, 4.3, 3.0, 4.2, COLORS["primary"])

    chain_steps = ["ChatPromptTemplate", "ChatOpenAI\ntemp=0", "StrOutputParser()"]
    for i, step in enumerate(chain_steps):
        x = 6.0 + i * 1.9
        rounded_box(ax, x, 4.2, 1.7, 1.0, step, COLORS["llm"] if i == 1 else COLORS["card"], fontsize=8.5)
        if i < len(chain_steps) - 1:
            arrow(ax, x + 1.7, 4.7, x + 1.9, 4.7, COLORS["accent"])

    arrow(ax, 5.5, 4.7, 6.0, 4.7, COLORS["success"])

    rounded_box(ax, 0.5, 1.0, 11.0, 2.0,
                "Prompt guardrails:\n• Use only retrieved context\n• Say 'I don't know based on the provided documents'\n"
                "• Mention source file (return_policy.md)\n• No outside knowledge",
                "#EEF2FF", edge=COLORS["secondary"], fontsize=10)
    save(fig, "session40-07-lcel-rag-chain.png")


def image_08():
    fig, ax = setup_fig(
        "Grounding — Cited Answer vs Honest Refusal",
        "Same RAG app: in-corpus query vs out-of-corpus query",
    )
    rounded_box(ax, 0.4, 3.5, 5.3, 2.5,
                "Q: Return window for\nelectronics?\n\nA: 7 days\nSource: return_policy.md\n✓ Grounded + cited",
                COLORS["success"], edge=COLORS["success"], fontsize=9)
    rounded_box(ax, 6.3, 3.5, 5.3, 2.5,
                "Q: Return window for\nbaby items?\n\nA: I don't know based on\nthe provided documents\n✓ No hallucination",
                COLORS["card"], edge=COLORS["accent"], fontsize=9)

    rounded_box(ax, 0.5, 0.9, 11.0, 1.8,
                "Prompt-level guardrail — like Amazon bot refusing random 'latest AI news' questions\n"
                "Re-ingest required when policy text changes; editing .md alone does not update vectors",
                "#EEF2FF", edge=COLORS["primary"], fontsize=10)
    save(fig, "session40-08-grounding-citations.png")


if __name__ == "__main__":
    image_01()
    image_02()
    image_03()
    image_04()
    image_05()
    image_06()
    image_07()
    image_08()
