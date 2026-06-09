"""Session 02 — Operators & Conditional Statements. Polished edu diagrams with full text."""
import textwrap
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch, Polygon, Rectangle

OUT = Path(__file__).parent
W, H = 16.0, 10.0

C = {
    "bg1": "#EDE9FE",
    "bg2": "#FEF3C7",
    "header": "#4F46E5",
    "indigo": "#4338CA",
    "violet": "#7C3AED",
    "cyan": "#0891B2",
    "emerald": "#059669",
    "emerald_bg": "#D1FAE5",
    "rose": "#E11D48",
    "rose_bg": "#FFE4E6",
    "amber": "#D97706",
    "amber_bg": "#FEF3C7",
    "sky_bg": "#E0F2FE",
    "violet_bg": "#EDE9FE",
    "white": "#FFFFFF",
    "slate": "#1E293B",
    "muted": "#64748B",
    "code_bg": "#0F172A",
    "code_kw": "#67E8F9",
    "code_str": "#86EFAC",
    "shadow": "#94A3B8",
}


def setup(title: str, subtitle: str = ""):
    fig, ax = plt.subplots(figsize=(16, 10), dpi=160)
    fig.patch.set_facecolor(C["bg1"])
    grad = np.linspace(0, 1, 512).reshape(-1, 1)
    grad = np.hstack([grad, grad])
    ax.imshow(
        grad, aspect="auto", extent=[0, W, 0, H], origin="lower", zorder=0,
        cmap=plt.matplotlib.colors.LinearSegmentedColormap.from_list("bg", [C["bg1"], C["bg2"]]),
    )
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.axis("off")

    header = FancyBboxPatch(
        (div := 0.45, 8.85), W - 2 * div, 1.05,
        boxstyle="round,pad=0.02,rounding_size=0.2",
        facecolor=C["header"], edgecolor=C["indigo"], linewidth=2, zorder=2,
    )
    ax.add_patch(header)
    ax.text(W / 2, 9.55, title, ha="center", va="center", fontsize=20, fontweight="bold",
            color="white", zorder=3)
    if subtitle:
        ax.text(W / 2, 9.05, subtitle, ha="center", va="center", fontsize=11,
                color="#E0E7FF", zorder=3, style="italic")
    return fig, ax


def wrap_lines(text: str, width: int = 32) -> list[str]:
    lines = []
    for paragraph in text.split("\n"):
        if not paragraph.strip():
            lines.append("")
        else:
            lines.extend(textwrap.wrap(paragraph, width=width) or [""])
    return lines


def _chars_per_line(w: float, fontsize: float) -> int:
    return max(12, int(w * 5.8 / (fontsize / 10)))


def draw_text_block(ax, x, y, w, h, lines, fontsize=10.5, color=C["slate"], weight="normal", family="sans-serif"):
    n = len([ln for ln in lines if ln.strip()])
    if n == 0:
        return
    pad = 0.22
    max_fs = fontsize
    while n * (max_fs / 72 * 1.45) > h - pad and max_fs > 7:
        max_fs -= 0.5
    line_h = (h - pad) / max(n, 1)
    start_y = y + h / 2 + (n - 1) * line_h / 2
    idx = 0
    for line in lines:
        if not line.strip():
            continue
        ax.text(
            x + w / 2, start_y - idx * line_h, line,
            ha="center", va="center", fontsize=max_fs, color=color,
            fontweight=weight, family=family, zorder=5, clip_on=True,
        )
        idx += 1


def card(ax, x, y, w, h, text, face=C["white"], edge=C["indigo"], fontsize=10.5,
         weight="normal", wrap=None, text_color=C["slate"], shadow=True, family="sans-serif"):
    if wrap is None:
        wrap = _chars_per_line(w, fontsize)
    if shadow:
        sh = FancyBboxPatch(
            (x + 0.08, y - 0.08), w, h,
            boxstyle="round,pad=0.03,rounding_size=0.18",
            facecolor=C["shadow"], edgecolor="none", alpha=0.28, zorder=2,
        )
        ax.add_patch(sh)
    box = FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.03,rounding_size=0.18",
        facecolor=face, edgecolor=edge, linewidth=2.2, zorder=3,
    )
    ax.add_patch(box)
    draw_text_block(ax, x, y, w, h, wrap_lines(text, wrap), fontsize, text_color, weight, family)
    return box


def code_card(ax, x, y, w, h, text, fontsize=9.5):
    lines = text.split("\n")
    fs = fontsize
    while len(lines) * (fs / 72 * 1.5) > h - 0.3 and fs > 7:
        fs -= 0.5
    card(ax, x, y, w, h, text, face=C["code_bg"], edge=C["cyan"], fontsize=fs,
         weight="bold", wrap=_chars_per_line(w, fs), text_color="#F8FAFC", family="monospace")


def arrow(ax, x1, y1, x2, y2, color=C["indigo"], lw=2.0, style="-|>", shrink_a=6, shrink_b=6, zorder=4):
    arr = FancyArrowPatch(
        (x1, y1), (x2, y2), arrowstyle=style, mutation_scale=16,
        linewidth=lw, color=color, shrinkA=shrink_a, shrinkB=shrink_b, zorder=zorder,
        connectionstyle="arc3,rad=0",
    )
    ax.add_patch(arr)


def arrow_elbow(ax, pts, color=C["indigo"], lw=2.0):
    """Draw orthogonal path through list of (x,y) points."""
    for i in range(len(pts) - 1):
        x1, y1 = pts[i]
        x2, y2 = pts[i + 1]
        is_last = i == len(pts) - 2
        arr = FancyArrowPatch(
            (x1, y1), (x2, y2),
            arrowstyle="-|>" if is_last else "-",
            mutation_scale=16 if is_last else 0,
            linewidth=lw, color=color, shrinkA=0, shrinkB=6 if is_last else 0, zorder=4,
        )
        ax.add_patch(arr)


def arrow_between_boxes(ax, left_x, left_w, right_x, y, color=C["indigo"]):
    """Horizontal arrow in the gap between two boxes."""
    arrow(ax, left_x + left_w + 0.12, y, right_x - 0.12, y, color=color, shrink_a=0, shrink_b=0)


def arrow_label(ax, x, y, text, color, face):
    ax.text(x, y, text, ha="center", va="center", fontsize=9.5, fontweight="bold", color=color, zorder=6,
            bbox=dict(boxstyle="round,pad=0.28", facecolor=face, edgecolor=color, linewidth=1.5))


def diamond(ax, cx, cy, rw, rh, text, face=C["amber_bg"], edge=C["amber"], wrap=None):
    if wrap is None:
        wrap = max(14, int(rw * 2.2))
    poly = Polygon(
        [(cx, cy + rh), (cx + rw, cy), (cx, cy - rh), (cx - rw, cy)],
        closed=True, facecolor=face, edgecolor=edge, linewidth=2.2, zorder=3,
    )
    ax.add_patch(poly)
    draw_text_block(ax, cx - rw + 0.15, cy - rh + 0.1, rw * 2 - 0.3, rh * 2 - 0.2,
                    wrap_lines(text, wrap), 9.5, weight="bold", color=C["slate"])


def save(fig, name):
    path = OUT / name
    fig.savefig(path, bbox_inches="tight", facecolor=C["bg1"], pad_inches=0.15)
    plt.close(fig)
    print(f"Saved {path}")


def image_01():
    fig, ax = setup(
        "Why Programs Need to Make Decisions",
        "Program flow control — the program changes direction based on a condition",
    )
    cx = 3.2
    card(ax, cx - 1.4, 7.15, 2.8, 0.9, "Start Program", C["amber_bg"], C["amber"], 12, "bold")
    arrow(ax, cx, 7.15, cx, 6.75, C["indigo"], shrink_a=0, shrink_b=0)
    diamond(ax, cx, 5.85, 1.75, 1.05, "Ticket for\nPlatform 3?", C["sky_bg"], C["cyan"], wrap=14)

    false_cx = 0.45 + 3.5 / 2
    true_cx = 4.85 + 3.5 / 2
    branch_y = 5.05
    action_top = 2.55 + 1.65

    card(ax, 0.45, 2.55, 3.5, 1.65, "Walk RIGHT\ntoward other platforms", C["rose_bg"], C["rose"], 10.5, "bold")
    card(ax, 4.85, 2.55, 3.5, 1.65, "Walk LEFT\ntoward Platform 3", C["emerald_bg"], C["emerald"], 10.5, "bold")

    arrow_elbow(ax, [(cx - 0.15, 4.95), (false_cx, 4.95), (false_cx, branch_y), (false_cx, action_top + 0.12)], C["rose"])
    arrow_label(ax, (cx + false_cx) / 2 - 0.3, branch_y + 0.22, "False", C["rose"], C["rose_bg"])
    arrow_elbow(ax, [(cx + 0.15, 4.95), (true_cx, 4.95), (true_cx, branch_y), (true_cx, action_top + 0.12)], C["emerald"])
    arrow_label(ax, (cx + true_cx) / 2 + 0.3, branch_y + 0.22, "True", C["emerald"], C["emerald_bg"])

    card(
        ax, 8.8, 6.35, 6.7, 1.95,
        "Key Terms:\n"
        "Condition = the check (platform, marks, PIN)\n"
        "Action = what runs when True or False\n"
        "Boolean = only True or False",
        C["sky_bg"], C["cyan"], 10,
    )
    card(
        ax, 8.8, 4.15, 6.7, 2.0,
        "Real-Life Examples in Apps:\n"
        "• UPI apps check balance before payment\n"
        "• Exam portals show Pass or Fail from marks\n"
        "• ATMs validate PIN before withdrawal",
        C["white"], C["violet"], 10,
    )
    card(
        ax, 8.8, 2.55, 6.7, 1.35,
        "Without conditionals, every program follows one fixed path like a recipe that never changes.",
        C["violet_bg"], C["violet"], 10,
    )

    card(
        ax, 0.45, 0.45, 15.1, 1.55,
        "Definition: Program flow control is the ability of a program to change the order of execution based on conditions, rather than running every line in a fixed sequence.",
        C["white"], C["indigo"], 10.5, "bold", wrap=88,
    )
    save(fig, "session02-01-program-decision-flow.png")


def image_02():
    fig, ax = setup(
        "Boolean Values and Comparison Operators",
        "Every condition evaluates to exactly True or False — never both",
    )
    # Scholarship flow — single clean row, arrows only in gaps
    bx = [0.55, 4.15, 7.75, 11.35]
    bw = 3.35
    by, bh = 6.85, 1.55
    labels = [
        ("marks >= 80\nResult: True or False", C["sky_bg"], C["cyan"]),
        ("attendance >= 75\nResult: True or False", C["sky_bg"], C["cyan"]),
        ("and\nboth must be True", C["violet_bg"], C["violet"]),
        ("qualifies = True\nScholarship granted!", C["emerald_bg"], C["emerald"]),
    ]
    for x, (txt, face, edge) in zip(bx, labels):
        card(ax, x, by, bw, bh, txt, face, edge, 10, "bold")
    for i in range(3):
        arrow_between_boxes(ax, bx[i], bw, bx[i + 1], by + bh / 2, C["indigo"])

    ax.text(8.0, 6.35, "Scholarship eligibility example", ha="center", fontsize=9.5,
            color=C["muted"], style="italic", zorder=5)

    ops = [
        ("==  Equal to", "50 == 50  →  True", C["emerald_bg"], C["emerald"]),
        ("!=  Not equal", "50 != 40  →  True", C["emerald_bg"], C["emerald"]),
        (">  Greater than", "85 > 40  →  True", C["sky_bg"], C["cyan"]),
        ("<  Less than", "30 < 40  →  True", C["sky_bg"], C["cyan"]),
        (">=  Greater or equal", "40 >= 40  →  True", C["violet_bg"], C["violet"]),
        ("<=  Less or equal", "35 <= 40  →  True", C["violet_bg"], C["violet"]),
    ]
    for i, (title, ex, face, edge) in enumerate(ops):
        col, row = i % 3, i // 3
        card(ax, 0.55 + col * 5.15, 4.55 - row * 2.05, 4.85, 1.75, f"{title}\n{ex}", face, edge, 10, "bold")

    card(ax, 0.55, 0.45, 7.55, 1.85,
         "Logical Operators:\n"
         "and — both True\n"
         "or — at least one True\n"
         "not — reverses the value\n"
         "True and False → False  |  True or False → True  |  not True → False",
         C["white"], C["indigo"], 9.5, wrap=42)

    card(ax, 8.35, 0.45, 7.15, 1.85,
         "Common Mistake:\n"
         "marks = 80  assigns a value (wrong in if)\n"
         "marks == 80  compares values (correct in if)",
         C["rose_bg"], C["rose"], 9.5, "bold", wrap=36)
    save(fig, "session02-02-boolean-conditions.png")


def image_03():
    fig, ax = setup(
        "The if Statement — Run Code Only When Condition Is True",
        "Start with if, then condition, then colon. Indent the block with 4 spaces.",
    )
    code_card(
        ax, 0.55, 5.35, 7.35, 3.15,
        "# Voting eligibility (age 18+ in India)\n"
        "age = int(input(\"Enter your age: \"))\n"
        "if age >= 18:\n"
        "    print(\"You are eligible to vote.\")",
    )
    card(
        ax, 8.2, 5.85, 7.25, 2.65,
        "Syntax Rules:\n"
        "1. Write if, then the condition, then a colon :\n"
        "2. Indent the block below (usually 4 spaces)\n"
        "3. If condition is False, Python skips the block\n"
        "4. Lines not indented always run after the block",
        C["violet_bg"], C["violet"], 10, wrap=36,
    )
    card(
        ax, 8.2, 3.55, 7.25, 1.85,
        "Common Mistakes:\n"
        "Forgetting int() causes TypeError.\n"
        "Wrong indentation causes IndentationError.",
        C["rose_bg"], C["rose"], 10, "bold", wrap=38,
    )

    card(ax, 0.55, 3.85, 7.35, 1.35,
         "age = 20  →  age >= 18 is True  →  message prints on screen",
         C["emerald_bg"], C["emerald"], 10, "bold", wrap=40)
    card(ax, 0.55, 2.35, 7.35, 1.35,
         "age = 15  →  age >= 18 is False  →  indented block is skipped",
         C["rose_bg"], C["rose"], 10, "bold", wrap=40)

    # Bottom flow — full width, evenly spaced (clear gap below outcome cards)
    steps = ["Get Input", "Evaluate\nCondition", "Condition\nTrue?", "Run if\nBlock", "Continue\nProgram"]
    sw, sh, sy, sx0 = 2.55, 1.25, 0.45, 0.55
    gap = (15.0 - len(steps) * sw) / (len(steps) - 1)
    for i, label in enumerate(steps):
        x = sx0 + i * (sw + gap)
        card(ax, x, sy, sw, sh, label,
             C["amber_bg"] if i == 0 else C["white"], C["indigo"], 9.5, "bold", wrap=16)
        if i < len(steps) - 1:
            arrow_between_boxes(ax, x, sw, x + sw + gap, sy + sh / 2, C["cyan"])

    save(fig, "session02-03-if-statement-flow.png")


def image_04():
    fig, ax = setup(
        "if and else — Exactly One Branch Runs",
        "When the if condition is False, the else block runs instead — never both, never neither",
    )
    cx, cy = 8.0, 7.45
    diamond(ax, cx, cy, 1.75, 0.9, "marks >= 40 ?", C["amber_bg"], C["amber"])

    lx, lw, ly, lh = 0.8, 5.8, 5.65, 1.45
    rx, rw, ry, rh = 9.4, 5.8, 5.65, 1.45
    left_cx = lx + lw / 2
    right_cx = rx + rw / 2
    bus_y = 6.55
    card_top = ly + lh

    card(ax, lx, ly, lw, lh,
         "if marks >= 40:\n    print(\"Result: PASS\")", C["emerald_bg"], C["emerald"], 10.5, "bold", wrap=28)
    card(ax, rx, ry, rw, rh,
         "else:\n    print(\"Result: FAIL\")", C["rose_bg"], C["rose"], 10.5, "bold", wrap=28)

    arrow_elbow(ax, [(cx - 1.75, cy), (left_cx, cy), (left_cx, bus_y), (left_cx, card_top + 0.12)], C["emerald"])
    arrow_label(ax, (cx + left_cx) / 2 - 0.4, cy + 0.15, "True", C["emerald"], C["emerald_bg"])
    arrow_elbow(ax, [(cx + 1.75, cy), (right_cx, cy), (right_cx, bus_y), (right_cx, card_top + 0.12)], C["rose"])
    arrow_label(ax, (cx + right_cx) / 2 + 0.4, cy + 0.15, "False", C["rose"], C["rose_bg"])

    ax.text(8.0, 5.35, "Exactly one branch runs — never both, never neither", ha="center",
            fontsize=10, color=C["muted"], style="italic", zorder=5)

    code_card(
        ax, 0.55, 0.45, 7.55, 3.75,
        "# Even or odd using modulus operator\n"
        "number = int(input(\"Enter a whole number: \"))\n"
        "if number % 2 == 0:\n"
        "    print(f\"{number} is an even number.\")\n"
        "else:\n"
        "    print(f\"{number} is an odd number.\")",
    )
    card(
        ax, 8.35, 0.45, 7.15, 3.75,
        "How modulus % works:\n\n"
        "number % 2 gives the remainder when divided by 2.\n\n"
        "Remainder 0 → even number\n"
        "Remainder 1 → odd number\n\n"
        "Example: 7 % 2 = 1 (odd)\n"
        "Example: 8 % 2 = 0 (even)",
        C["sky_bg"], C["cyan"], 10, wrap=34,
    )
    save(fig, "session02-04-if-else-branches.png")


def image_05():
    fig, ax = setup(
        "if, elif, and else — Multiple Conditions in Order",
        "Python checks from top to bottom and stops at the first True condition",
    )
    rows = [
        ("if marks >= 90:", "Grade: A — Outstanding!", C["emerald_bg"], C["emerald"]),
        ("elif marks >= 75:", "Grade: B — Very Good!", C["sky_bg"], C["cyan"]),
        ("elif marks >= 60:", "Grade: C — Good", C["violet_bg"], C["violet"]),
        ("elif marks >= 40:", "Grade: D — Needs improvement", C["amber_bg"], C["amber"]),
        ("else:", "Grade: F — Failed", C["rose_bg"], C["rose"]),
    ]
    y = 7.0
    for cond, result, face, edge in rows:
        card(ax, 0.6, y, 5.2, 0.95, cond, face, edge, 10.5, "bold", 28)
        arrow(ax, 5.8, y + 0.48, 6.3, y + 0.48, C["indigo"])
        card(ax, 6.3, y, 5.5, 0.95, result, face, edge, 10.5, "bold", 30)
        y -= 1.15

    card(
        ax, 12.2, 2.5, 3.2, 5.45,
        "Example: marks = 95\nOnly Grade A prints.\nAll other conditions\nare skipped.\n\n"
        "Wrong Order Mistake:\nPutting marks >= 40\nbefore marks >= 90\nmeans almost everyone\ngets Grade D!",
        C["rose_bg"], C["rose"], 10.5, "bold", wrap=26,
    )
    card(
        ax, 0.6, 0.55, 11.2, 1.35,
        "Same elif pattern used for: electricity billing slabs (100 / 200 units), train ticket categories by age, and any problem with more than two outcomes.",
        C["white"], C["indigo"], 11, wrap=72,
    )
    save(fig, "session02-05-elif-chain.png")


def image_06():
    fig, ax = setup(
        "Logical Operators Inside if Conditions",
        "Use and, or, and not when a single comparison is not enough",
    )
    card(
        ax, 0.6, 5.0, 4.8, 3.35,
        "Scholarship — and\n\n"
        "if (marks >= 80) and (attendance >= 75):\n"
        "    print(\"Eligible for scholarship!\")\n\n"
        "Both conditions must be True.",
        C["emerald_bg"], C["emerald"], 10.5, wrap=30,
    )
    card(
        ax, 5.6, 5.0, 4.8, 3.35,
        "Shop Discount — or\n\n"
        "if (amount > 1000) or (has_membership == \"yes\"):\n"
        "    apply 20% discount\n\n"
        "At least one condition must be True.",
        C["amber_bg"], C["amber"], 10.5, wrap=30,
    )
    card(
        ax, 10.6, 5.0, 4.8, 3.35,
        "Account Login — not\n\n"
        "if not is_locked:\n"
        "    print(\"Login successful!\")\n\n"
        "not False becomes True.\n"
        "Account must NOT be locked.",
        C["sky_bg"], C["cyan"], 10.5, wrap=30,
    )
    card(
        ax, 0.6, 2.35, 7.5, 2.15,
        "Truth Table Quick Reference:\n"
        "True and True → True       |    True or False → True       |    not True → False\n"
        "True and False → False     |    False or False → False     |    not False → True",
        C["white"], C["indigo"], 10.5, "bold", wrap=52,
    )
    card(
        ax, 8.4, 2.35, 7.0, 2.15,
        "Readability Tip:\n"
        "Use parentheses in complex conditions:\n"
        "(marks >= 80) and (attendance >= 75)",
        C["violet_bg"], C["violet"], 10.5, wrap=38,
    )
    card(
        ax, 0.6, 0.55, 14.8, 1.35,
        "and requires BOTH sides to be True. or requires AT LEAST ONE side to be True. not flips True to False and False to True.",
        C["white"], C["violet"], 11, "bold", wrap=90,
    )
    save(fig, "session02-06-logical-operators.png")


def image_07():
    fig, ax = setup(
        "Nested Conditionals — Decisions Inside Decisions",
        "Check a second condition only after the first condition passes",
    )
    diamond(ax, 8.0, 7.6, 1.7, 0.75, "username ==\ncorrect_username ?", C["amber_bg"], C["amber"])

    card(ax, 0.5, 5.5, 4.5, 1.35, "else:\nprint(\"Username not found.\")", C["rose_bg"], C["rose"], 11, "bold", wrap=28)
    arrow(ax, 6.5, 7.6, 2.75, 6.85, C["rose"])
    badge(ax, 1.5, 6.95, "False", C["rose_bg"], C["rose"])

    diamond(ax, 10.5, 5.5, 1.6, 0.7, "password ==\ncorrect_password ?", C["sky_bg"], C["cyan"])
    arrow(ax, 9.0, 7.2, 10.5, 6.2, C["emerald"])
    badge(ax, 9.5, 6.55, "True", C["emerald_bg"], C["emerald"])

    card(ax, 7.0, 3.2, 4.5, 1.35, "else:\nprint(\"Wrong password. Please try again.\")", C["rose_bg"], C["rose"], 10.5, "bold", wrap=30)
    card(ax, 12.2, 3.2, 3.3, 1.35, "print(\"Login successful! Welcome.\")", C["emerald_bg"], C["emerald"], 10.5, "bold", wrap=24)
    arrow(ax, 9.5, 5.15, 9.25, 4.55, C["rose"])
    arrow(ax, 11.5, 5.15, 13.0, 4.55, C["emerald"])

    code_card(
        ax, 0.5, 0.55, 15.0, 2.35,
        "if username == correct_username:\n"
        "    if password == correct_password:\n"
        "        print(\"Login successful! Welcome.\")\n"
        "    else:\n"
        "        print(\"Wrong password. Please try again.\")\n"
        "else:\n"
        "    print(\"Username not found.\")",
        10,
    )
    card(
        ax, 0.5, 3.2, 6.0, 1.35,
        "Real-Life: If you have a ticket, enter the stadium. If you also have a VIP pass, go to the premium stand.",
        C["violet_bg"], C["violet"], 10.5, wrap=38,
    )
    save(fig, "session02-07-nested-conditionals.png")


def image_08():
    fig, ax = setup(
        "The STEP Method — Think Before You Code",
        "State the problem → identify inputs → list conditions → write Python",
    )
    steps = [
        ("S", "State the Problem", "Cinema charges ₹150 for adults and ₹80 for children (age 12 or below).", C["amber_bg"], C["amber"]),
        ("T", "Identify Inputs", "The program needs the passenger age from the user.", C["sky_bg"], C["cyan"]),
        ("E", "List Conditions and Outcomes", "If age <= 12 → child ticket ₹80\nElse → adult ticket ₹150", C["violet_bg"], C["violet"]),
        ("P", "Write Python Code", "Map each outcome from step E to an if or else block in Python.", C["emerald_bg"], C["emerald"]),
    ]
    for i, (letter, heading, detail, face, edge) in enumerate(steps):
        x = 0.6 + i * 3.85
        circ = Circle((x + 0.55, 7.35), 0.45, facecolor=edge, edgecolor="white", linewidth=2, zorder=4)
        ax.add_patch(circ)
        ax.text(x + 0.55, 7.35, letter, ha="center", va="center", fontsize=18, fontweight="bold", color="white", zorder=5)
        card(ax, x, 5.85, 3.55, 1.2, heading, face, edge, 12, "bold", wrap=22)
        card(ax, x, 3.5, 3.55, 2.1, detail, C["white"], edge, 10.5, wrap=28)
        if i < 3:
            arrow(ax, x + 3.55, 6.45, x + 3.85, 6.45, C["indigo"])

    code_card(
        ax, 0.6, 0.55, 15.0, 2.55,
        "# STEP: input = age; if age <= 12 → ₹80, else → ₹150\n"
        "age = int(input(\"Enter your age: \"))\n"
        "if age <= 12:\n"
        "    print(f\"Child ticket: ₹80\")\n"
        "else:\n"
        "    print(f\"Adult ticket: ₹150\")",
        10,
    )
    save(fig, "session02-08-step-method.png")


def image_09():
    fig, ax = setup(
        "Common Mistakes with Conditionals",
        "Most beginner errors come from syntax, data types, or wrong elif order",
    )
    mistakes = [
        ("Using = instead of ==", "if marks = 50:", "if marks == 50:", "= assigns, == compares"),
        ("Forgetting the colon", "if marks >= 40", "if marks >= 40:", "Python expects : at end of if line"),
        ("Wrong indentation", "print not indented under if", "Indent block with 4 spaces", "Python cannot find the if block"),
        ("String vs number", "age == 18 when age is \"18\"", "int(age) == 18", "Different types cannot compare"),
        ("Wrong elif order", ">= 40 checked before >= 90", "Put >= 90 first (strictest)", "Almost everyone gets wrong grade"),
        ("Empty if block", "Nothing below if statement", "Use pass or real code", "Python disallows empty blocks"),
    ]
    y = 7.15
    for title, wrong, right, why in mistakes:
        card(ax, 0.5, y, 3.0, 0.95, title, C["amber_bg"], C["amber"], 9.5, "bold", wrap=22)
        card(ax, 3.65, y, 4.2, 0.95, f"Wrong: {wrong}", C["rose_bg"], C["rose"], 9, wrap=28)
        card(ax, 8.0, y, 4.2, 0.95, f"Correct: {right}", C["emerald_bg"], C["emerald"], 9, wrap=28)
        card(ax, 12.35, y, 3.15, 0.95, why, C["white"], C["muted"], 8.5, wrap=22)
        y -= 1.12

    card(
        ax, 0.5, 0.55, 15.0, 1.15,
        "Debugging Tips: Print the condition before the if to see True or False. Use print(type(variable)) to check data types. Test boundary values like 39, 40, and 90 for pass and grade programs.",
        C["sky_bg"], C["cyan"], 10.5, "bold", wrap=88,
    )
    save(fig, "session02-09-common-mistakes.png")


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
