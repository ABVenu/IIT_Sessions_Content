"""Generate Session 23 (Working with APIs and JSON) lecture note diagrams — ShopKart theme."""
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
    "api": "#FECACA",
    "json": "#D1FAE5",
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
        "RAG vs API — Pick the Right Source",
        "ShopKart support: stored policy documents vs live external systems",
    )
    rounded_box(ax, 0.4, 3.0, 5.3, 2.4,
                "RAG — STORED DOCUMENTS\n\n"
                "• Return window for opened charger?\n"
                "• Express rules in metro cities?\n"
                "• 12-month warranty terms?\n\n"
                "Search Chroma policy chunks",
                COLORS["returns"], edge=COLORS["primary"], fontsize=9, weight="bold")
    rounded_box(ax, 6.3, 3.0, 5.3, 2.4,
                "API — LIVE DATA\n\n"
                "• Where is order ORD-88421?\n"
                "• Current temperature in Delhi?\n"
                "• Refund processed today?\n\n"
                "GET external service → JSON",
                COLORS["api"], edge=COLORS["danger"], fontsize=9, weight="bold")
    rounded_box(ax, 0.5, 0.45, 11.0, 1.8,
                "Wrong source = confident wrong answer\n"
                "Policy PDF cannot show live courier location · Live API cannot invent return windows",
                COLORS["warn"], edge=COLORS["accent"], fontsize=10, weight="bold")
    save(fig, "session23-01-rag-vs-api.png")


def image_02():
    fig, ax = setup_fig(
        "API Request — Four Parts",
        "Same pattern for weather GET and Groq POST — menu, order, credentials, payload",
    )
    parts = [
        ("1 · URL / ENDPOINT\nWhere to send\napi.open-meteo.com/forecast", COLORS["returns"], 0.35),
        ("2 · METHOD\nWhat action\nGET read · POST create", COLORS["shipping"], 3.05),
        ("3 · HEADERS\nMetadata\nAuth key · Content-Type", COLORS["warranty"], 5.75),
        ("4 · BODY\nData you send\nOften JSON (POST/PATCH)", COLORS["refunds"], 8.45),
    ]
    for txt, face, x in parts:
        rounded_box(ax, x, 3.0, 2.5, 2.2, txt, face, fontsize=8.5, weight="bold")
    rounded_box(ax, 0.5, 0.45, 11.0, 1.8,
                "Groq mapping: endpoint (library) · POST · Authorization header · messages body\n"
                "Always read status code before trusting the response body",
                COLORS["card"], edge=COLORS["secondary"], fontsize=9.5)
    save(fig, "session23-02-api-request-four-parts.png")


def image_03():
    fig, ax = setup_fig(
        "REST — Resource + HTTP Method",
        "Name the thing in the URL · express the action with GET POST PATCH PUT DELETE",
    )
    methods = [
        ("GET\nRead", COLORS["returns"], 0.4),
        ("POST\nCreate", COLORS["shipping"], 2.5),
        ("PATCH\nPartial update", COLORS["warranty"], 4.6),
        ("PUT\nFull replace", COLORS["refunds"], 6.7),
        ("DELETE\nRemove", COLORS["api"], 8.8),
    ]
    for txt, face, x in methods:
        rounded_box(ax, x, 3.5, 1.9, 1.5, txt, face, fontsize=8.5, weight="bold")
    rounded_box(ax, 0.5, 1.8, 11.0, 1.3,
                "REST style: GET /orders/88421   not   /get-order-by-id",
                COLORS["card"], edge=COLORS["primary"], fontsize=10, weight="bold")
    rounded_box(ax, 0.5, 0.4, 11.0, 1.2,
                "Today's lab: GET only — read live weather without changing server data",
                COLORS["warn"], edge=COLORS["accent"], fontsize=9.5, weight="bold")
    save(fig, "session23-03-rest-http-methods.png")


def image_04():
    fig, ax = setup_fig(
        "HTTP Status Codes — Check Before You Parse",
        "Three families · common ShopKart lab codes",
    )
    rounded_box(ax, 0.4, 3.2, 3.5, 2.0, "2xx SUCCESS\n\n200 OK — weather data\n201 Created",
                COLORS["refunds"], edge=COLORS["success"], fontsize=9, weight="bold")
    rounded_box(ax, 4.25, 3.2, 3.5, 2.0, "4xx CLIENT ERROR\n\n400 Bad request\n401 Unauthorized\n404 Not found\n429 Rate limit",
                COLORS["warn"], edge=COLORS["accent"], fontsize=8.5, weight="bold")
    rounded_box(ax, 8.1, 3.2, 3.5, 2.0, "5xx SERVER ERROR\n\n500 Internal error\nExternal API down",
                COLORS["api"], edge=COLORS["danger"], fontsize=9, weight="bold")
    rounded_box(ax, 0.5, 0.45, 11.0, 1.8,
                "429 on Groq free tier during heavy RAG testing — pause, not a retrieval bug\n"
                "Lab habit: if status != 200 → do not parse body as weather JSON",
                COLORS["card"], edge=COLORS["secondary"], fontsize=9.5)
    save(fig, "session23-04-http-status-codes.png")


def image_05():
    fig, ax = setup_fig(
        "JSON ↔ Python — Parse Before You Use",
        "API text string becomes a dict you can index",
    )
    rounded_box(ax, 0.4, 3.5, 3.2, 1.8,
                "JSON STRING\n(one big text blob\nfrom wire or file)",
                COLORS["card"], edge=COLORS["muted"], fontsize=9, weight="bold")
    arrow(ax, 3.6, 4.4, 4.5, 4.4, COLORS["accent"])
    rounded_box(ax, 4.5, 3.5, 3.0, 1.8,
                "json.loads()\nor\nresponse.json()",
                COLORS["warn"], edge=COLORS["accent"], fontsize=9, weight="bold")
    arrow(ax, 7.5, 4.4, 8.4, 4.4, COLORS["primary"])
    rounded_box(ax, 8.4, 3.5, 3.2, 1.8,
                "PYTHON DICT\nfields[\"temperature_c\"]",
                COLORS["json"], edge=COLORS["success"], fontsize=9, weight="bold")
    rounded_box(ax, 0.5, 0.45, 11.0, 2.0,
                "Weather lab output:\n"
                "  city · temperature_c · weather_code\n\n"
                "Extract only needed keys — same discipline as top-k policy chunks",
                COLORS["card"], edge=COLORS["primary"], fontsize=9.5)
    save(fig, "session23-05-json-python-roundtrip.png")


def image_06():
    fig, ax = setup_fig(
        "What Comes Next — LLM Calls Are APIs Too",
        "Groq POST → JSON response → read choices[0].message.content",
    )
    rounded_box(ax, 0.5, 3.8, 2.8, 1.5, "YOUR SCRIPT\nshopkart lab",
                COLORS["card"], edge=COLORS["primary"], fontsize=9, weight="bold")
    arrow(ax, 3.3, 4.55, 4.2, 4.55, COLORS["primary"])
    rounded_box(ax, 4.2, 3.5, 3.4, 1.9, "GROQ API\nPOST + messages\n+ API key header",
                COLORS["shipping"], edge=COLORS["secondary"], fontsize=9, weight="bold")
    arrow(ax, 7.6, 4.55, 8.5, 4.55, COLORS["accent"])
    rounded_box(ax, 8.5, 3.5, 3.0, 1.9, "JSON RESPONSE\nmodel reply text",
                COLORS["refunds"], edge=COLORS["success"], fontsize=9, weight="bold")
    rounded_box(ax, 0.5, 0.45, 11.0, 2.0,
                "Today: weather GET → parse → print in terminal\n"
                "Next session: register tools · model chooses · Groq synthesises final reply",
                COLORS["warn"], edge=COLORS["accent"], fontsize=9.5, weight="bold")
    save(fig, "session23-06-llm-as-api-preview.png")


if __name__ == "__main__":
    image_01()
    image_02()
    image_03()
    image_04()
    image_05()
    image_06()
