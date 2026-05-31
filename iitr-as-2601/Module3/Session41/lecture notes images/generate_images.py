"""Generate Session 41 lecture note diagrams — RAG retrieve, augment, generate (same theme as Session 40)."""
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
        "RAG Flow — You Built Prepare; Now Finish Retrieve → Generate",
        "Session 40: chunk, embed, store in policy_chunks  |  Session 41: search, paste context, answer",
    )
    steps = [
        ("1 Ingest", "load policies", COLORS["muted"], False),
        ("2 Prepare", "chunk + embed\npolicy_chunks", COLORS["chunk1"], False),
        ("3 Retrieve", "top-k on Chroma\nall-MiniLM-L6-v2", COLORS["chunk2"], True),
        ("4 Augment", "delimiters +\nsource labels", COLORS["chunk3"], True),
        ("5 Generate", "Ollama or Groq\ngrounded answer", COLORS["success"], True),
    ]
    for i, (title, body, face, highlight) in enumerate(steps):
        x = 0.3 + i * 2.35
        edge = COLORS["accent"] if highlight else COLORS["primary"]
        lw = 2.5 if highlight else 1.5
        box = FancyBboxPatch(
            (x, 3.0), 2.1, 2.0,
            boxstyle="round,pad=0.02,rounding_size=0.15",
            linewidth=lw, edgecolor=edge, facecolor=face if highlight else COLORS["card"],
        )
        ax.add_patch(box)
        ax.text(x + 1.05, 4.35, title, ha="center", fontsize=10, weight="bold", color=COLORS["text"])
        ax.text(x + 1.05, 3.55, body, ha="center", fontsize=8.5, color=COLORS["text"])
        if i < len(steps) - 1:
            arrow(ax, x + 2.1, 4.0, x + 2.35, 4.0, COLORS["accent"] if highlight else COLORS["primary"])

    rounded_box(ax, 0.4, 1.0, 11.2, 1.5,
                "Grounded generation = open-book exam\nSearch first (retrieve) → paste allowed notes (augment) → then speak (generate)",
                "#EEF2FF", edge=COLORS["secondary"], fontsize=11, weight="bold")
    ax.text(0.4, 0.35, "Railway clerk reads the display board before telling you the platform — not from memory alone",
            fontsize=9, color=COLORS["muted"])
    save(fig, "session41-01-rag-five-steps-retrieve-generate.png")


def image_02():
    fig, ax = setup_fig("Top-k Retrieval — Bridge from Chroma to the LLM", "Query embedding must use the same model as index time")
    rounded_box(ax, 0.4, 4.2, 2.8, 1.2, "User question\n'How many days\nto return?'", COLORS["chunk1"], fontsize=9)
    rounded_box(ax, 3.6, 4.2, 2.6, 1.2, "Encode query\nall-MiniLM-L6-v2", COLORS["chunk2"], edge=COLORS["secondary"])
    rounded_box(ax, 6.4, 4.2, 2.8, 1.2, "Chroma query\npolicy_chunks\nn_results = k", COLORS["chunk3"], edge=COLORS["accent"])
    rounded_box(ax, 9.4, 4.2, 2.2, 1.2, "Top-k chunks\n+ metadata\n+ distance", COLORS["success"], edge=COLORS["success"])
    for x1, x2 in [(3.2, 3.6), (6.2, 6.4), (9.2, 9.4)]:
        arrow(ax, x1, 4.8, x2, 4.8)

    k_rows = [
        ("k = 1", "Fast — may miss\na second rule", COLORS["danger"], 0.5),
        ("k = 3", "Lab default\nbalanced", COLORS["success"], 4.2),
        ("k = 5+", "More context\nrisk of noise", COLORS["accent"], 7.9),
    ]
    for title, body, edge, x in k_rows:
        rounded_box(ax, x, 2.0, 3.0, 0.75, title, COLORS["card"], edge=edge, fontsize=10, weight="bold")
        rounded_box(ax, x, 0.9, 3.0, 0.95, body, COLORS["card"], edge=edge, fontsize=8.5)

    rounded_box(ax, 0.4, 0.15, 11.2, 0.6, "Librarian brings 3 relevant folders — not the entire stack",
                "#FFFBEB", edge=COLORS["accent"], fontsize=9)
    save(fig, "session41-02-top-k-retrieval.png")


def image_03():
    fig, ax = setup_fig("Context Assembly — Delimiters and Source Labels", "Build the exam paper: rules, evidence block, question")
    y = 5.5
    sections = [
        ("=== INSTRUCTIONS ===", "Answer ONLY from context\nRefuse if not found\nSources used: ...", COLORS["chunk1"]),
        ("=== CONTEXT START ===", "[Chunk 1 | source_id=returns_policy.txt | page=0]\n30 days return window...\n\n[Chunk 2 | shipping_policy.txt | page=0]\n...", COLORS["chunk2"]),
        ("=== CONTEXT END ===", "", COLORS["muted"]),
        ("=== QUESTION ===", "How many days do I have to return a product?", COLORS["chunk3"]),
    ]
    for header, body, face in sections:
        rounded_box(ax, 0.5, y - 1.15, 11.0, 1.0 if body else 0.45, f"{header}\n{body}" if body else header,
                    face, fontsize=8.5 if body else 9, weight="bold" if not body else "normal")
        y -= 1.25

    rounded_box(ax, 0.5, 0.2, 5.3, 0.85, "Court brief: Exhibit A, Exhibit B\n— judge knows the source", COLORS["card"], edge=COLORS["secondary"])
    rounded_box(ax, 6.0, 0.2, 5.5, 0.85, "Without delimiters → model treats\nchunks as optional background", COLORS["card"], edge=COLORS["danger"])
    save(fig, "session41-03-context-assembly-delimiters.png")


def image_04():
    fig, ax = setup_fig("RAG Pipeline in Code", "retrieve_chunks → build_rag_prompt → generate_answer")
    boxes = [
        (0.35, 3.9, "User query", COLORS["chunk1"]),
        (2.5, 3.9, "retrieve_chunks\nTOP_K = 3", COLORS["chunk2"]),
        (4.9, 3.9, "build_rag_prompt\ndelimiters + labels", COLORS["chunk3"]),
        (7.5, 3.9, "generate_answer\nOllama / Groq", COLORS["success"]),
        (10.0, 3.9, "Answer +\nSources used", COLORS["chunk1"]),
    ]
    for x, y, txt, face in boxes:
        rounded_box(ax, x, y, 2.0, 1.35, txt, face, fontsize=8.5, weight="bold")
    for x1, x2 in [(2.35, 2.5), (4.5, 4.9), (6.9, 7.5), (9.5, 10.0)]:
        arrow(ax, x1, 4.55, x2, 4.55, COLORS["accent"])

    rounded_box(ax, 0.4, 1.5, 5.5, 1.8,
                "Backend-neutral prompt\nSame retrieval for\nOllama and Groq",
                COLORS["card"], edge=COLORS["secondary"], fontsize=10)
    rounded_box(ax, 6.2, 1.5, 5.4, 1.8,
                "GENERATOR_BACKEND\n'ollama' | 'groq'\nOnly last call changes",
                COLORS["card"], edge=COLORS["accent"], fontsize=10)
    rounded_box(ax, 0.4, 0.2, 11.2, 0.9,
                "Common mistake: generate_answer before retrieve + build_rag_prompt = plain chatbot, not RAG",
                "#FEE2E2", edge=COLORS["danger"], fontsize=9.5)
    save(fig, "session41-04-rag-pipeline-code.png")


def image_05():
    fig, ax = setup_fig("Same RAG Path — Two Generator Backends", "Retrieval and prompt stay identical; swap GENERATOR_BACKEND only")
    rounded_box(ax, 0.5, 4.5, 11.0, 1.0, "build_rag_prompt output (identical for both)", COLORS["chunk2"], fontsize=11, weight="bold")
    arrow(ax, 6.0, 4.5, 6.0, 4.0, COLORS["accent"])
    arrow(ax, 3.0, 4.0, 3.0, 3.5)
    arrow(ax, 9.0, 4.0, 9.0, 3.5)

    rounded_box(ax, 0.8, 2.0, 4.5, 1.3, "Ollama (local)\nqwen2.5:0.5b\nollama pull + serve", COLORS["chunk1"], edge=COLORS["primary"])
    rounded_box(ax, 6.7, 2.0, 4.5, 1.3, "Groq (cloud)\nllama-3.3-70b\nGROQ_API_KEY", COLORS["chunk3"], edge=COLORS["secondary"])

    rounded_box(ax, 0.5, 0.25, 5.2, 1.2, "Best for: laptop,\nprivacy, offline", COLORS["card"], fontsize=9)
    rounded_box(ax, 6.3, 0.25, 5.2, 1.2, "Best for: Colab,\nweak laptop, speed", COLORS["card"], fontsize=9)
    save(fig, "session41-05-ollama-vs-groq-same-rag.png")


def image_06():
    fig, ax = setup_fig("Without RAG vs With RAG", "Same ShopEasy question — compare hallucination risk")
    rounded_box(ax, 0.5, 3.5, 5.2, 2.2,
                "WITHOUT RAG\ngenerate_without_rag(query only)\n\nMay invent generic\nreturn policy from\nmodel memory",
                COLORS["card"], edge=COLORS["danger"], fontsize=9.5)
    rounded_box(ax, 6.3, 3.5, 5.2, 2.2,
                "WITH RAG\nrag_answer(query)\nretrieve → prompt → generate\n\nCites YOUR stored chunks\n+ Sources used line",
                COLORS["card"], edge=COLORS["success"], fontsize=9.5)

    ax.text(5.85, 4.6, "vs", fontsize=14, weight="bold", ha="center", color=COLORS["accent"])
    rounded_box(ax, 1.0, 1.0, 10.0, 1.5,
                "Question: 'Is delivery free for a 600 rupee order?'\nWithout RAG: plausible guess  |  With RAG: shipping_policy.txt chunk evidence",
                "#EEF2FF", edge=COLORS["secondary"], fontsize=10, weight="bold")
    ax.text(0.5, 0.3, "Sounds confident either way — grounding rules + context block make the difference",
            fontsize=9, color=COLORS["muted"])
    save(fig, "session41-06-without-rag-vs-with-rag.png")


def image_07():
    fig, ax = setup_fig("Informal Grounding Check", "Manually map each claim in the answer to a retrieved chunk")
    rounded_box(ax, 0.4, 4.3, 5.5, 1.5, "Retrieval trace\nprint_retrieval_trace\nChunk 1, 2, 3 + source_id", COLORS["chunk1"])
    rounded_box(ax, 6.1, 4.3, 5.5, 1.5, "Generated answer\n'Sources used: ...'\nlist source_id / page", COLORS["chunk2"])
    arrow(ax, 5.9, 5.05, 6.1, 5.05, COLORS["accent"])

    checks = [
        ("Claim in context?", "Every number/rule\nin some chunk", COLORS["success"]),
        ("No-context case", "UPI question → refuse\nnot invent", COLORS["danger"]),
        ("Chunk ↔ claim", "30 days → Chunk 1\nreturns_policy.txt", COLORS["accent"]),
    ]
    for i, (title, body, edge) in enumerate(checks):
        x = 0.5 + i * 3.85
        rounded_box(ax, x, 1.5, 3.5, 0.7, title, COLORS["card"], edge=edge, fontsize=9, weight="bold")
        rounded_box(ax, x, 0.4, 3.5, 0.95, body, COLORS["card"], edge=edge, fontsize=8.5)

    rounded_box(ax, 0.4, 0.05, 11.2, 0.28, "News fact-check desk — match headline to quoted paragraph",
                "#FFFBEB", edge=COLORS["accent"], fontsize=8)
    save(fig, "session41-07-informal-grounding-check.png")


def image_08():
    fig, ax = setup_fig("Mini End-to-End RAG Script", "ingest (if empty) → retrieve → augment → generate → audit")
    stages = [
        ("ingest_sample_policies", "if count == 0\nchunk + upsert", COLORS["chunk1"]),
        ("retrieve_chunks", "top-k search\npolicy_chunks", COLORS["chunk2"]),
        ("build_rag_prompt", "CONTEXT START/END", COLORS["chunk3"]),
        ("generate_answer", "Ollama / Groq", COLORS["success"]),
        ("rag_answer", "answer + chunks\nfor audit", COLORS["chunk1"]),
    ]
    for i, (title, body, face) in enumerate(stages):
        x = 0.25 + i * 2.35
        rounded_box(ax, x, 3.6, 2.15, 0.65, title, face, fontsize=7.5, weight="bold")
        rounded_box(ax, x, 2.3, 2.15, 1.15, body, COLORS["card"], fontsize=8)
        if i < len(stages) - 1:
            arrow(ax, x + 2.15, 3.9, x + 2.35, 3.9, COLORS["accent"])

    symptoms = [
        ("Invented detail", "Strengthen grounding\n+ delimiters", COLORS["danger"]),
        ("Not found but exists", "Raise TOP_K\nfix chunking", COLORS["accent"]),
        ("Generic answer", "Use full rag_answer\nnot plain LLM", COLORS["secondary"]),
    ]
    for i, (sym, fix, edge) in enumerate(symptoms):
        rounded_box(ax, 0.4 + i * 3.9, 0.35, 3.6, 1.5, f"{sym}\n→ {fix}", COLORS["card"], edge=edge, fontsize=8.5)
    save(fig, "session41-08-end-to-end-mini-rag.png")


if __name__ == "__main__":
    image_01()
    image_02()
    image_03()
    image_04()
    image_05()
    image_06()
    image_07()
    image_08()
