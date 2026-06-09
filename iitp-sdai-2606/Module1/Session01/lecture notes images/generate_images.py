"""Session 01 lecture diagrams — polished layout, complete text, no overflow."""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Circle, Rectangle

OUT = Path(__file__).parent
W, H = 16.0, 10.0
DPI = 150
LH = 0.36
PAD = 0.30
HEADER_H = 1.45
GAP = 0.2
TOP = H - HEADER_H - 0.3
FOOTER_Y = 0.35
FOOTER_RESERVE = 1.15
MIN_Y = FOOTER_Y + FOOTER_RESERVE + GAP

C = {
    "bg": "#F0F4FF",
    "header": "#312E81",
    "header_accent": "#6366F1",
    "card": "#FFFFFF",
    "text": "#0F172A",
    "indigo": "#4F46E5",
    "violet": "#7C3AED",
    "teal": "#0D9488",
    "teal_bg": "#CCFBF1",
    "amber": "#B45309",
    "amber_bg": "#FEF3C7",
    "rose": "#BE123C",
    "rose_bg": "#FFE4E6",
    "emerald": "#047857",
    "emerald_bg": "#D1FAE5",
    "sky": "#0369A1",
    "sky_bg": "#E0F2FE",
    "code_bg": "#1E293B",
    "code_text": "#E2E8F0",
    "py_blue": "#306998",
    "py_yellow": "#FFD43B",
    "lavender": "#EDE9FE",
    "peach": "#FFEDD5",
}


def new_fig():
    fig, ax = plt.subplots(figsize=(W / 1.5, H / 1.5), dpi=DPI)
    fig.patch.set_facecolor(C["bg"])
    ax.set_facecolor(C["bg"])
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.axis("off")
    return fig, ax


def header(ax, title, subtitle=""):
    ax.add_patch(Rectangle((0, H - HEADER_H), W, HEADER_H, facecolor=C["header"], edgecolor="none", zorder=1))
    ax.add_patch(Rectangle((0, H - HEADER_H), 0.5, HEADER_H, facecolor=C["py_yellow"], edgecolor="none", zorder=2))
    ax.text(0.7, H - 0.55, title, fontsize=16.5, fontweight="bold", color="white", va="center", zorder=3)
    if subtitle:
        ax.text(0.7, H - 1.05, subtitle, fontsize=10, color="#C7D2FE", va="center", zorder=3)
    ax.add_patch(Circle((15.4, H - HEADER_H / 2), 0.34, facecolor=C["header_accent"], edgecolor="white", lw=2, zorder=3))
    ax.text(15.4, H - HEADER_H / 2, "01", fontsize=10, fontweight="bold", color="white", ha="center", va="center", zorder=4)


def card_h(n_lines, has_title=False):
    return n_lines * LH + 2 * PAD + (0.48 if has_title else 0)


def draw_card(ax, x, bottom_y, w, lines, bg, border, *, title=None, fontsize=10.0,
              mono=False, accent=None, text_color=None, align="center"):
    h = card_h(len(lines), bool(title))
    y = bottom_y
    if accent:
        ax.add_patch(Rectangle((x + 0.06, y + 0.1), 0.12, h - 0.2, facecolor=accent, edgecolor="none", zorder=3))
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.16",
        linewidth=2.0, edgecolor=border, facecolor=bg, zorder=4,
    ))
    tc = text_color or C["text"]
    family = "monospace" if mono else "sans-serif"
    tx = x + w / 2 if align == "center" else x + PAD + 0.2
    ha = "center" if align == "center" else "left"
    cy = y + h - PAD
    if title:
        ax.text(tx, cy, title, ha=ha, va="top", fontsize=fontsize + 1.6,
                fontweight="bold", color=border, family=family, zorder=5)
        cy -= 0.46
    for i, line in enumerate(lines):
        ax.text(tx, cy - i * LH, line, ha=ha, va="top", fontsize=fontsize,
                color=tc, family=family, zorder=5)
    return h


class Col:
    def __init__(self, top=TOP):
        self.cursor = top

    def add(self, ax, x, w, lines, bg, border, **kw):
        h = card_h(len(lines), bool(kw.get("title")))
        self.cursor -= h
        draw_card(ax, x, self.cursor, w, lines, bg, border, **kw)
        self.cursor -= GAP
        return self.cursor


def arrow(ax, x1, y1, x2, y2, color=C["indigo"]):
    ax.add_patch(FancyArrowPatch(
        (x1, y1), (x2, y2), arrowstyle="-|>", mutation_scale=13,
        linewidth=1.8, color=color, shrinkA=3, shrinkB=3, zorder=6,
    ))


def footer(ax, text):
    if len(text) > 82:
        mid = text.rfind(" ", 0, len(text) // 2 + 15)
        lines = [text[:mid].strip(), text[mid:].strip()] if mid > 20 else [text]
    else:
        lines = [text]
    draw_card(ax, 0.5, FOOTER_Y, 15.0, lines, C["card"], C["indigo"], fontsize=9.6, accent=C["indigo"])


def save(fig, name):
    path = OUT / name
    fig.savefig(path, bbox_inches="tight", facecolor=C["bg"], pad_inches=0.12)
    plt.close(fig)
    print(f"Saved {path}")


def image_01():
    fig, ax = new_fig()
    header(ax, "What Is Programming?",
           "Writing step-by-step instructions that a computer understands and executes")
    left, right = Col(), Col()
    left.add(ax, 0.5, 7.2, [
        "Step 1: Turn on the gas",
        "Step 2: Heat the pan and add oil",
        "Step 3: Add chopped onions",
        "Step 4: Add salt and spices",
        "Step 5: Serve the food on a plate",
    ], C["py_yellow"], C["py_blue"], title="Recipe = Program", fontsize=10.0, accent=C["py_blue"])
    left.add(ax, 0.5, 7.2, [
        "UPI payments",
        "Train ticket booking",
        "WhatsApp messaging",
        "Netflix recommendations",
        "AI tools you will build later",
    ], C["lavender"], C["violet"], title="Digital World Runs on Code", fontsize=10.0, accent=C["violet"])
    right.add(ax, 8.1, 7.35, [
        "Program  =  the recipe (your code)",
        "Computer =  the cook (runs each line)",
        "Every step must be written clearly.",
        "Forget to turn on the gas?",
        "Nothing gets cooked — same with code!",
    ], C["amber_bg"], C["amber"], title="The Analogy", fontsize=10.0, accent=C["amber"])
    right.add(ax, 8.1, 7.35, [
        "Programming teaches you to break",
        "big problems into small, clear steps.",
        "Useful in tech careers and in",
        "everyday life.",
    ], C["emerald_bg"], C["emerald"], title="Why It Matters", fontsize=10.0, accent=C["emerald"])
    footer(ax, "In simple words: programming is like giving very clear directions to a machine that never guesses — it only does exactly what you tell it.")
    save(fig, "session01-01-programming-recipe-analogy.png")


def image_02():
    fig, ax = new_fig()
    header(ax, "Why Python?", "Simple, readable syntax — reads almost like plain English")
    left, right = Col(), Col()
    left.add(ax, 0.5, 7.3, [
        "print('Hello, World!')", "age = 22", "name = 'Priya'", "print(name)",
    ], C["code_bg"], C["py_blue"], title="Sample Python Code", fontsize=10.2, mono=True, text_color=C["code_text"])
    right.add(ax, 8.15, 7.35, [
        "Software development", "Data science", "Artificial intelligence",
        "Browser coding on day one", "No complicated installation",
    ], C["sky_bg"], C["sky"], title="Used Everywhere", fontsize=10.0, accent=C["sky"])
    left.add(ax, 0.5, 7.3, [
        "Simple, readable syntax", "Focus on thinking logically",
        "Not fighting complex rules", "Most popular language worldwide",
    ], C["py_yellow"], C["py_blue"], title="Why Start with Python?", fontsize=10.0, accent=C["py_blue"])
    right.add(ax, 8.15, 7.35, [
        "If programming languages were spoken languages,",
        "Python is like Hindi or English — easy to start",
        "with and widely used everywhere.",
    ], C["card"], C["violet"], title="In Simple Words", fontsize=10.0, accent=C["violet"])
    footer(ax, "Official definition: Python is a high-level, general-purpose programming language known for its simple, readable syntax.")
    save(fig, "session01-02-python-beginner-language.png")


def image_03():
    fig, ax = new_fig()
    header(ax, "OneCompiler — Your Online Coding Workspace",
           "Free browser compiler at onecompiler.com — write, run, save, and share Python code")
    steps = [
        ("Step 1", ["Open", "onecompiler.com", "in your browser"], C["py_yellow"], C["py_blue"]),
        ("Step 2", ["Click Python", "from the", "language list"], C["sky_bg"], C["sky"]),
        ("Step 3", ["Sign up or", "sign in to", "save your work"], C["lavender"], C["violet"]),
        ("Step 4", ["Type Python", "code in the", "editor area"], C["card"], C["indigo"]),
        ("Step 5", ["Click Run", "to see output", "below the editor"], C["emerald_bg"], C["emerald"]),
    ]
    sx = 0.35
    sw = 3.05
    mids = []
    for title, lines, bg, border in steps:
        h = card_h(len(lines), True)
        bottom = TOP - h
        draw_card(ax, sx, bottom, sw, lines, bg, border, title=title, fontsize=9.0, accent=border)
        mids.append((sx + sw, bottom + h / 2))
        sx += sw + 0.08
    for i in range(4):
        arrow(ax, mids[i][0], mids[i][1], mids[i][0] + 0.4, mids[i][1])
    row2 = TOP - card_h(3, True) - GAP - 0.15
    left, right = Col(row2), Col(row2)
    left.add(ax, 0.5, 7.4, [
        "Code Editor (top area)", "  print('Hello, World!')",
        "Output (bottom area)", "  Hello, World!",
    ], C["code_bg"], C["py_blue"], title="What You See on Screen", fontsize=9.5, mono=True, text_color=C["code_text"], align="left")
    right.add(ax, 8.2, 7.3, [
        "Forgetting to click Run — code alone does nothing",
        "Not saving your work — use Save to keep progress",
        "Spelling: Print vs print (case-sensitive)",
        "Curly quotes from Word or WhatsApp",
        'Use straight " quotes from keyboard',
        "Share a link with your instructor for review",
    ], C["rose_bg"], C["rose"], title="Common Beginner Mistakes", fontsize=9.1, accent=C["rose"], align="left")
    footer(ax, "An online compiler is like a digital notebook with a Run button — type code, press Run, and the result appears instantly.")
    save(fig, "session01-03-onecompiler-workspace.png")


def image_04():
    fig, ax = new_fig()
    header(ax, "Your First Python Program — Hello, World!",
           "Comments are for humans; print() shows output; Python runs every line from top to bottom")
    left, right = Col(), Col()
    left.add(ax, 0.5, 6.9, [
        "# This is my very first Python program",
        "# The print() function displays text",
        "print('Hello, World!')",
    ], C["code_bg"], C["py_blue"], title="Type This in OneCompiler", fontsize=9.5, mono=True, text_color=C["code_text"])
    right.add(ax, 7.85, 7.65, [
        "Lines starting with # are comments —",
        "notes for humans that Python ignores.",
        "print() shows output on the screen.",
        "Text in quotes is a string (text data).",
        "Click Run to execute top to bottom.",
    ], C["sky_bg"], C["sky"], title="How the Code Works", fontsize=9.5, accent=C["sky"], align="left")
    flow_y = min(left.cursor, right.cursor) - GAP - card_h(1, False)
    labels = [("Type code in editor", C["card"], C["indigo"]),
              ("Click the Run button", C["amber_bg"], C["amber"]),
              ("Python runs each line", C["py_yellow"], C["py_blue"]),
              ("Output on the screen", C["emerald_bg"], C["emerald"])]
    fx = 0.5
    for i, (label, bg, border) in enumerate(labels):
        h = card_h(1, False)
        draw_card(ax, fx, flow_y, 3.55, [label], bg, border, fontsize=9.5, accent=border)
        if i < 3:
            arrow(ax, fx + 3.65, flow_y + h / 2, fx + 4.0, flow_y + h / 2)
        fx += 3.82
    footer(ax, "Quick activity: Print your name on line 1 and your city on line 2 using two separate print() calls.")
    save(fig, "session01-04-hello-world-flow.png")


def image_05():
    fig, ax = new_fig()
    header(ax, "Variables — Storing Information in Your Program",
           "A named reference that holds a value — like a labelled dabba at a kirana store")
    jx = 0.5
    jar_h = card_h(2, True)
    for label, value in [("age", "22"), ("name", '"Priya"'), ("balance", "500")]:
        draw_card(ax, jx, TOP - jar_h, 4.85, [f"Variable: {label}", f"Value: {value}"],
                  C["py_yellow"], C["py_blue"], title="Labelled Box", fontsize=10.0, accent=C["py_blue"])
        jx += 5.1
    row2 = TOP - jar_h - GAP
    left, right = Col(row2), Col(row2)
    left.add(ax, 0.5, 7.5, [
        "age = 22", "name = 'Priya'", "print(age)    # shows 22", "print(name)   # shows Priya",
        "The = sign means assignment,",
        "not maths equality.",
    ], C["code_bg"], C["py_blue"], title="Creating Variables", fontsize=9.3, mono=True, text_color=C["code_text"], align="left")
    right.add(ax, 8.4, 7.1, [
        "Letters, numbers, underscore allowed", "Cannot start with a number",
        "Case-sensitive: Age ≠ age", "Use descriptive names: student_marks",
        "balance = 500", "balance = balance - 120", "print(balance)  →  380",
    ], C["card"], C["violet"], title="Naming Rules & Reassignment", fontsize=9.1, accent=C["violet"], align="left")
    footer(ax, "Real-life example: Shopkeeper writes 'Rice — 2 kg' on a bag. The label is the variable name; '2 kg' is the value.")
    save(fig, "session01-05-variables-labeled-boxes.png")


def image_06():
    fig, ax = new_fig()
    header(ax, "Data Types — What Kind of Information Are You Storing?",
           "Python detects the type from how you write the value — use type() when debugging")
    tx = 0.4
    row_h = 0
    for title, lines, bg, border in [
        ("INT", ["Whole numbers", "(no decimals)", "25, 0, -10"], C["emerald_bg"], C["emerald"]),
        ("FLOAT", ["Numbers with", "decimals", "3.14, 99.5"], C["amber_bg"], C["amber"]),
        ("STR", ["Text in quotes", '(strings)', '"Hello", \'India\''], C["sky_bg"], C["sky"]),
        ("BOOL", ["True or False", "(capital T & F)", "True, False"], C["rose_bg"], C["rose"]),
    ]:
        h = card_h(len(lines), True)
        row_h = max(row_h, h)
        draw_card(ax, tx, TOP - h, 3.8, lines, bg, border, title=title, fontsize=9.3, accent=border)
        tx += 3.92
    row2 = TOP - row_h - GAP
    left, right = Col(row2), Col(row2)
    left.add(ax, 0.5, 7.5, [
        "students = 40          # int", "temperature = 36.6     # float",
        'city = "Bengaluru"     # str', "is_passed = True       # bool",
        "print(type(students))  # <class 'int'>",
    ], C["code_bg"], C["py_blue"], title="Examples in Python", fontsize=9.3, mono=True, text_color=C["code_text"], align="left")
    right.add(ax, 8.4, 7.1, [
        "Form analogy:", "Age field expects a number (int)", "Name field expects text (str)",
        "Mixing them up causes errors.", "", "Common mistake:",
        'Storing "85" as text instead of 85', "— maths operations will not work!",
    ], C["card"], C["rose"], title="Think Before You Store", fontsize=9.1, accent=C["rose"], align="left")
    footer(ax, "Data type is like labelling a dabba — this one holds numbers, that one holds words.")
    save(fig, "session01-06-data-types-overview.png")


def image_07():
    fig, ax = new_fig()
    header(ax, "Arithmetic Operators — Making Your Program Calculate",
           "Symbols that perform maths on values — store results in variables for readable code")
    row1_h = max(card_h(2, True) for _ in range(4))
    ox = 0.45
    for sym, meaning, example in [
        ("+", "Addition", "10 + 3 = 13"), ("-", "Subtraction", "10 - 3 = 7"),
        ("*", "Multiplication", "10 * 3 = 30"), ("/", "Division (float)", "10 / 3 = 3.333..."),
    ]:
        draw_card(ax, ox, TOP - row1_h, 3.75, [meaning, example], C["card"], C["indigo"], title=sym, fontsize=9.1, accent=C["indigo"])
        ox += 3.88
    row2_top = TOP - row1_h - GAP
    row2_h = max(card_h(2, True) for _ in range(3))
    ox = 0.45
    for sym, meaning, example in [
        ("//", "Floor division", "10 // 3 = 3"), ("%", "Modulus (remainder)", "10 % 3 = 1"), ("**", "Exponent (power)", "2 ** 3 = 8"),
    ]:
        draw_card(ax, ox, row2_top - row2_h, 3.75, [meaning, example], C["sky_bg"], C["sky"], title=sym, fontsize=9.1, accent=C["sky"])
        ox += 3.88
    row3 = row2_top - row2_h - GAP
    left, right = Col(row3), Col(row3)
    left.add(ax, 0.5, 7.6, [
        "a = 20", "b = 6", "print(a + b)   # 26", "print(a // b)  # 3", "print(a % b)   # 2", "print(a ** 2)  # 400",
    ], C["code_bg"], C["py_blue"], title="Python Example", fontsize=9.3, mono=True, text_color=C["code_text"], align="left")
    right.add(ax, 8.45, 7.05, [
        "Real-life: splitting a dinner bill", "total_bill = 1500   # rupees", "num_friends = 3",
        "share = total_bill / num_friends", "print(share)  →  500.0", "Each friend pays ₹500",
    ], C["emerald_bg"], C["emerald"], title="Splitting a ₹1500 Bill", fontsize=9.1, accent=C["emerald"], align="left")
    save(fig, "session01-07-arithmetic-operators.png")


def image_08():
    fig, ax = new_fig()
    header(ax, "Comparison & Logical Operators — True or False",
           "Comparisons check conditions; logical operators combine multiple conditions")
    top = Col()
    top.add(ax, 0.5, 7.5, [
        "==  Equal to          5 == 5   →  True",
        "!=  Not equal to      5 != 3   →  True",
        ">   Greater than      10 > 3   →  True",
        "<   Less than         10 < 3   →  False",
        ">=  Greater or equal  10 >= 10 →  True",
        "<=  Less or equal     5 <= 3   →  False",
    ], C["sky_bg"], C["sky"], title="Comparison Operators", fontsize=9.0, mono=True, accent=C["sky"], align="left")
    mid_top = top.cursor
    lh = card_h(2, True)
    draw_card(ax, 0.5, mid_top - lh, 4.9, [
        "Both must be True", "marks >= 80 and attendance >= 75",
    ], C["emerald_bg"], C["emerald"], title="and", fontsize=9.2, accent=C["emerald"])
    draw_card(ax, 5.55, mid_top - lh, 4.9, [
        "At least one True", "number < 1 or number > 100",
    ], C["amber_bg"], C["amber"], title="or", fontsize=9.2, accent=C["amber"])
    draw_card(ax, 10.6, mid_top - lh, 4.9, [
        "Reverses value", "not True → False", "not False → True",
    ], C["rose_bg"], C["rose"], title="not", fontsize=9.2, accent=C["rose"])
    row3 = mid_top - lh - GAP
    left, right = Col(row3), Col(row3)
    left.add(ax, 0.5, 7.5, [
        "marks = 50   assigns a value", "marks == 50  compares values",
        "score = 0; score += 10; score += 5; score -= 3 → 12",
    ], C["card"], C["violet"], title="Watch Out!", fontsize=9.0, accent=C["violet"], align="left")
    right.add(ax, 8.4, 7.1, [
        "eligible = (marks >= 80)", "         and (attendance >= 75)",
        "print(eligible)  →  True", "Use parentheses () to group conditions.",
    ], C["code_bg"], C["py_blue"], title="Real Example", fontsize=8.8, mono=True, text_color=C["code_text"], align="left")
    save(fig, "session01-08-comparison-logical-operators.png")


def image_09():
    fig, ax = new_fig()
    header(ax, "Input & Output — Talking to the User",
           "input() collects data from the user; print() displays results on the screen")
    ih = card_h(2, True)
    draw_card(ax, 0.45, TOP - ih, 3.1, ["User types name", "and presses Enter"], C["py_yellow"], C["py_blue"],
              title="INPUT", fontsize=9.5, accent=C["py_blue"])
    mid_y = TOP - ih / 2
    arrow(ax, 3.65, mid_y, 4.15, mid_y)
    ch = card_h(4, True)
    draw_card(ax, 4.25, TOP - ch, 4.6, [
        'name = input("Enter name: ")', "# always returns a string",
        "age = int(input('Enter age: '))", "# convert before maths",
    ], C["code_bg"], C["py_blue"], title="input() Function", fontsize=8.8, mono=True, text_color=C["code_text"], align="left")
    arrow(ax, 8.95, mid_y, 9.45, mid_y)
    draw_card(ax, 9.55, TOP - ih, 2.9, ["Program", "processes data"], C["card"], C["teal"], title="PROCESS", fontsize=9.5, accent=C["teal"])
    arrow(ax, 12.55, mid_y, 13.05, mid_y)
    draw_card(ax, 13.15, TOP - ih, 2.4, ["print() shows", "result on screen"], C["emerald_bg"], C["emerald"],
              title="OUTPUT", fontsize=9.5, accent=C["emerald"])
    row_top = TOP - max(ih, ch) - GAP
    left, right = Col(row_top), Col(row_top)
    left.add(ax, 0.5, 7.4, [
        "name = input('Enter your name: ')", "print('Hello,', name)", "",
        "age_text = input('Enter your age: ')", "age_number = int(age_text)", "",
        'print(f"Sneha scored {marks} marks")',
    ], C["code_bg"], C["py_blue"], title="Complete Code Examples", fontsize=8.8, mono=True, text_color=C["code_text"], align="left")
    right.add(ax, 8.3, 7.2, [
        "Railway counter analogy:", "You tell clerk destination → input",
        "Clerk prints your ticket → output", "", "input() always returns a string.",
        "Use int() or float() before maths.", "", "Mistake: '22' + 5  →  ERROR", "Correct:  22 + 5   →  27",
    ], C["card"], C["amber"], title="Key Rules to Remember", fontsize=9.0, accent=C["amber"], align="left")
    footer(ax, "Mini report card: use input() for name and marks, int() to convert, arithmetic for total/average, and print() with f-strings.")
    save(fig, "session01-09-input-output-flow.png")


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
