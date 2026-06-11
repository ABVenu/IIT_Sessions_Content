"""Generate Session 43 lecture note diagrams — ReAct agents with LangChain."""
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
    "thought": "#E0F2FE",
    "action": "#FEF3C7",
    "obs": "#D1FAE5",
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
        "From Memory Loop to ReAct Agent",
        "Previous lab: remember chat + stop safely  |  Today: agent thinks, acts, observes",
    )
    rounded_box(ax, 0.4, 3.2, 5.3, 2.4,
                "PREVIOUS (memory lab)\n\ntesla_chat_history.json\nRAG on ./Tesla_db\nMAX_STEPS stop rule\nStill text-only answers",
                COLORS["chunk1"], edge=COLORS["primary"], fontsize=9.5)
    rounded_box(ax, 6.3, 3.2, 5.3, 2.4,
                "TODAY (first agent lab)\n\nLangChain ReAct agent\nThought → Action → Observation\nPython REPL + Serper search",
                COLORS["chunk3"], edge=COLORS["accent"], fontsize=9.5)
    ax.text(5.85, 4.4, "→", fontsize=16, weight="bold", ha="center", color=COLORS["accent"])
    rounded_box(ax, 0.4, 0.9, 11.2, 1.6,
                "Same Groq LLM and safe habits carry forward\nToday the model also runs tools — not only retrieves text",
                "#EEF2FF", edge=COLORS["secondary"], fontsize=10, weight="bold")
    save(fig, "session43-01-tesla-rag-vs-shopeasy-tools.png")


def image_02():
    fig, ax = setup_fig("Chatbot vs Agent", "Plain chat guesses · Agent uses tools and reads results")
    rounded_box(ax, 0.4, 3.5, 5.3, 2.2,
                "Plain chatbot\n\n'Nvidia stock is about $500'\n(may be outdated guess)",
                COLORS["chunk1"], edge=COLORS["danger"], fontsize=9.5)
    rounded_box(ax, 6.3, 3.5, 5.3, 2.2,
                "ReAct agent\n\nThought: need live price\nAction: serper_search\nObservation: real snippet",
                COLORS["obs"], edge=COLORS["success"], fontsize=9.5)
    rounded_box(ax, 0.4, 0.9, 11.2, 1.8,
                "Agent = LLM + Tools + Loop\nUser asks → agent plans → runs tool → reads observation → answers",
                COLORS["card"], edge=COLORS["secondary"], fontsize=10, weight="bold")
    save(fig, "session43-02-rag-vs-tools.png")


def image_03():
    fig, ax = setup_fig("The ReAct Paradigm", "Reasoning and Acting in repeated steps")
    stages = [
        ("Thought", "What should I\ndo next?", COLORS["thought"]),
        ("Action", "Run a tool\nwith input", COLORS["action"]),
        ("Observation", "Read tool\noutput", COLORS["obs"]),
    ]
    for i, (title, body, face) in enumerate(stages):
        x = 0.6 + i * 3.7
        rounded_box(ax, x, 4.2, 3.2, 0.7, title, face, fontsize=10, weight="bold")
        rounded_box(ax, x, 2.8, 3.2, 1.2, body, COLORS["card"], fontsize=9.5)
        if i < 2:
            arrow(ax, x + 3.2, 4.55, x + 3.7, 4.55, COLORS["accent"])
    arrow(ax, 11.0, 3.4, 1.2, 3.4, COLORS["secondary"])
    rounded_box(ax, 0.4, 0.9, 11.2, 1.5,
                "Scratchpad = running log of all Thoughts, Actions, Observations\nFinal Solution only after enough observations",
                "#EEF2FF", edge=COLORS["secondary"], fontsize=9.5)
    save(fig, "session43-03-tool-schema.png")


def image_04():
    fig, ax = setup_fig("LangChain Tool Wrapper", "name · description · func — the model reads this menu")
    rounded_box(ax, 0.4, 4.0, 11.2, 1.5,
                "Tool(name='serper_search', description='Serper search engine...', func=serper_search.run)",
                COLORS["chunk2"], edge=COLORS["secondary"], fontsize=10, weight="bold")
    rounded_box(ax, 0.4, 2.2, 3.5, 1.5,
                "PythonREPL\nruns code\nin sandbox", COLORS["chunk1"], fontsize=9)
    rounded_box(ax, 4.1, 2.2, 3.5, 1.5,
                "GoogleSerper\nAPIWrapper\nlive web search", COLORS["chunk3"], edge=COLORS["accent"], fontsize=9)
    rounded_box(ax, 7.8, 2.2, 3.8, 1.5,
                "repl_tool.invoke()\ntest without agent\nfirst", COLORS["success"], fontsize=9)
    arrow(ax, 3.9, 2.95, 4.1, 2.95, COLORS["accent"])
    arrow(ax, 7.6, 2.95, 7.8, 2.95, COLORS["accent"])
    rounded_box(ax, 0.4, 0.35, 11.2, 1.5,
                "Clear description tells the agent WHEN to pick each tool — vague text → wrong or no tool call",
                COLORS["card"], edge=COLORS["danger"], fontsize=9.5)
    save(fig, "session43-04-register-bind.png")


def image_05():
    fig, ax = setup_fig("Python ReAct Agent", "create_react_agent + AgentExecutor + python_repl")
    rounded_box(ax, 0.4, 4.5, 2.5, 1.2, "ChatGroq\nllama-3.3-70b", COLORS["chunk1"])
    rounded_box(ax, 3.1, 4.5, 2.8, 1.2, "hub.pull\nhwchase17/react", COLORS["chunk2"])
    rounded_box(ax, 6.1, 4.5, 2.5, 1.2, "create_react\n_agent", COLORS["chunk3"])
    rounded_box(ax, 8.8, 4.5, 2.8, 1.2, "AgentExecutor\nverbose=True", COLORS["success"])
    for i in range(3):
        arrow(ax, 2.9 + i * 3.0, 5.1, 3.1 + i * 3.0, 5.1, COLORS["accent"])
    rounded_box(ax, 0.4, 2.3, 5.5, 1.6,
                "Query: compound interest\nThought: use formula in Python\nAction: python_repl",
                COLORS["card"], edge=COLORS["primary"], fontsize=9)
    rounded_box(ax, 6.1, 2.3, 5.5, 1.6,
                "Observation: printed result\nFinal Answer: rupee amount",
                COLORS["card"], edge=COLORS["success"], fontsize=9)
    rounded_box(ax, 0.4, 0.35, 11.2, 1.5,
                "Math the LLM might get wrong → Python REPL gives exact number",
                "#FFFBEB", edge=COLORS["accent"], fontsize=9.5)
    save(fig, "session43-05-model-tool-loop.png")


def image_06():
    fig, ax = setup_fig("Search ReAct Agent — Two Tools", "serper_search + python_repl in one executor")
    rounded_box(ax, 0.4, 4.3, 3.5, 1.5, "User query\nNvidia price +\n$100 investment calc", COLORS["chunk1"])
    rounded_box(ax, 4.1, 4.3, 3.5, 1.5, "Thought 1\nneed live price\nAction: serper_search", COLORS["action"])
    rounded_box(ax, 7.8, 4.3, 3.8, 1.5, "Observation 1\nprice snippet\nfrom web", COLORS["obs"])
    arrow(ax, 3.9, 5.05, 4.1, 5.05, COLORS["accent"])
    arrow(ax, 7.6, 5.05, 7.8, 5.05, COLORS["accent"])
    rounded_box(ax, 0.4, 2.2, 5.5, 1.5,
                "Thought 2: compute return\nAction: python_repl\nwith price variable",
                COLORS["card"], edge=COLORS["secondary"], fontsize=9)
    rounded_box(ax, 6.1, 2.2, 5.5, 1.5,
                "handle_parsing_errors=True\nkeeps loop alive on format slips",
                COLORS["card"], edge=COLORS["success"], fontsize=9)
    rounded_box(ax, 0.4, 0.35, 11.2, 1.5,
                "Multi-step ReAct: search first, calculate second — observations feed the scratchpad",
                "#EEF2FF", edge=COLORS["secondary"], fontsize=9.5)
    save(fig, "session43-06-tool-message-roles.png")


def image_07():
    fig, ax = setup_fig("AgentExecutor Loop", "invoke({'input': question}) runs until Final Answer")
    rounded_box(ax, 0.4, 4.5, 2.8, 1.3, "Load prompt\n+ tools list", COLORS["chunk1"])
    rounded_box(ax, 3.4, 4.5, 3.0, 1.3, "LLM writes\nThought / Action", COLORS["chunk2"])
    rounded_box(ax, 6.6, 4.5, 2.5, 1.3, "Run matching\ntool func", COLORS["chunk3"])
    rounded_box(ax, 9.3, 4.5, 2.3, 1.3, "Append\nObservation", COLORS["success"])
    for i in range(3):
        arrow(ax, 3.2 + i * 3.2, 5.15, 3.4 + i * 3.2, 5.15, COLORS["accent"])
    arrow(ax, 10.45, 4.5, 4.9, 3.5, COLORS["secondary"])

    rounded_box(ax, 0.4, 2.0, 5.5, 1.5,
                "verbose=True prints\nevery Thought/Action/\nObservation in notebook",
                COLORS["card"], edge=COLORS["primary"], fontsize=9.5)
    rounded_box(ax, 6.1, 2.0, 5.5, 1.5,
                "MAX_STEPS safety from\nprevious lab still matters\nfor custom loops",
                COLORS["card"], edge=COLORS["success"], fontsize=9.5)

    rounded_box(ax, 0.4, 0.35, 11.2, 1.3,
                "response['output'] = final user-facing answer after the ReAct loop finishes",
                "#EEF2FF", edge=COLORS["secondary"], fontsize=9.5)
    save(fig, "session43-07-groq-executor.png")


def image_08():
    fig, ax = setup_fig("Notebook Lab Flow", "Setup → test tools → build agents → run sample queries")
    steps = [
        ("A", "pip install +\nimport libraries", COLORS["chunk1"]),
        ("B", "Test repl_tool\nand search_tool\nalone", COLORS["chunk2"]),
        ("C", "Python agent:\ninterest rate query", COLORS["chunk3"]),
        ("D", "Search agent:\nNvidia + $100 calc", COLORS["success"]),
    ]
    for i, (label, body, face) in enumerate(steps):
        x = 0.35 + i * 2.9
        rounded_box(ax, x, 4.0, 0.65, 0.65, label, face, fontsize=12, weight="bold")
        rounded_box(ax, x + 0.75, 3.5, 2.0, 1.5, body, COLORS["card"], edge=face, fontsize=8.5)
        if i < 3:
            arrow(ax, x + 2.75, 4.25, x + 2.9, 4.25, COLORS["accent"])

    rounded_box(ax, 0.4, 1.5, 5.5, 1.5,
                "GROQ_API_KEY +\nSERPER_API_KEY required",
                COLORS["card"], edge=COLORS["danger"], fontsize=9.5)
    rounded_box(ax, 6.0, 1.5, 5.6, 1.5,
                "Read verbose trace\nbefore trusting output",
                COLORS["card"], edge=COLORS["success"], fontsize=9.5)

    rounded_box(ax, 0.4, 0.2, 11.2, 1.0,
                "Deeper function-calling APIs come in a later session — today LangChain ReAct handles the loop",
                "#FFFBEB", edge=COLORS["accent"], fontsize=9)
    save(fig, "session43-08-notebook-demo-flow.png")


if __name__ == "__main__":
    image_01()
    image_02()
    image_03()
    image_04()
    image_05()
    image_06()
    image_07()
    image_08()
