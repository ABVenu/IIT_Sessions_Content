# Pre-read: Loops & Iterations in Python

## Context of This Session in the Course

```mermaid
%%{init: {"diagramPadding": 24, "flowchart": {"htmlLabels": true, "nodeSpacing": 90, "rankSpacing": 110, "curve": "basis", "padding": 20}, "theme": "base", "themeVariables": {"fontFamily": "Arial", "fontSize": "15px", "lineColor": "#334155"}}}%%
flowchart TB
    subgraph FOUNDATION[" "]
        direction LR
        PREV[["&nbsp;&nbsp;<b>Current Module Until Previous Session</b>&nbsp;&nbsp;<br/><br/>Programming Foundations<br/>&amp; Developer Setup<br/><br/><i>Python basics · OneCompiler<br/>operators · conditionals</i><br/><br/><i>Programs that calculate,<br/>display, and choose paths</i>"]]
    end

    CURRENT{{"&nbsp;&nbsp;<b>Current Session</b>&nbsp;&nbsp;<br/><br/>Loops &amp; Iterations<br/>in Python<br/><br/><i>for · while · break · continue · range</i><br/><br/><b>Mental shift:</b><br/>from one-time steps<br/>to smart repetition"}}

    subgraph VALUE[" "]
        direction LR
        COURSE["&nbsp;&nbsp;<b>Course Connection</b>&nbsp;&nbsp;<br/><br/>Automation for data handling,<br/>functions, and repeated steps<br/>inside agentic systems<br/><br/><i>Programs that scale<br/>without copy-paste</i>"]
        REAL(["&nbsp;&nbsp;<b>Real-Life Connection</b>&nbsp;&nbsp;<br/><br/>UPI retries, exam result lists,<br/>seat scans, shopping bills,<br/>PIN validation, savings goals<br/><br/><i>Everyday apps that<br/>repeat until done</i>"])
    end

    subgraph FUTURE[" "]
        direction LR
        M2["&nbsp;&nbsp;<b>Upcoming Module</b>&nbsp;&nbsp;<br/><br/>Web Fundamentals + JavaScript<br/>(Frontend-101)<br/>(HTML + CSS + React)<br/><br/><i>Will use: pages, styling,<br/>DOM and Fetch API</i>"]
        M3["&nbsp;&nbsp;<b>Upcoming Module</b>&nbsp;&nbsp;<br/><br/>Backend Engineering<br/>with FastAPI<br/>(FastAPI + SQL + Auth)<br/><br/><i>Will use: APIs, databases,<br/>server-side logic</i>"]
        M4(["&nbsp;&nbsp;<b>Upcoming Module</b>&nbsp;&nbsp;<br/><br/>LLM Foundations + AI-First<br/>Development + Capstone<br/>(OpenAI + Agents + Deploy)<br/><br/><i>Will use: prompts, AI APIs,<br/>full-stack portfolio build</i>"])
    end

    PREV ==>|&nbsp;Foundation&nbsp;| CURRENT
    CURRENT ==>|&nbsp;Course Path&nbsp;| COURSE
    CURRENT ==>|&nbsp;Real-Life Use&nbsp;| REAL
    COURSE ==>|&nbsp;Next Module&nbsp;| M2
    M2 ==>|&nbsp;Next Module&nbsp;| M3
    M3 ==>|&nbsp;Next Module&nbsp;| M4

    classDef previous fill:#f8fafc,stroke:#475569,stroke-width:2px,color:#0f172a
    classDef current fill:#ecfeff,stroke:#0f766e,stroke-width:3px,color:#134e4a
    classDef value fill:#fff7ed,stroke:#c2410c,stroke-width:2px,color:#7c2d12
    classDef future fill:#f0fdf4,stroke:#15803d,stroke-width:2px,color:#14532d

    class PREV previous
    class CURRENT current
    class COURSE,REAL value
    class M2,M3,M4 future

    style FOUNDATION fill:transparent,stroke:transparent
    style VALUE fill:transparent,stroke:transparent
    style FUTURE fill:transparent,stroke:transparent
    linkStyle default stroke:#334155,stroke-width:3px
```

---

Picture yourself at a temple **prasad counter** on a busy Sunday. A long queue stretches behind you — fifty people, maybe a hundred. The volunteer at the counter does not serve everyone at once. They repeat the same small action again and again: take one laddu, hand it to the next person, move on. Same gesture, same smile, same rule — **one serving per person** — until the queue is empty.

That quiet repetition is something you see everywhere in daily life, and it is exactly the kind of work that computers are built to handle at massive scale. Your phone does not get tired. It does not lose count. It does not skip a name because it is bored. Once you teach it the pattern, it can repeat that pattern a hundred times or a thousand times with the same patience.

Your **UPI app** may check a failed payment two or three times before showing an error. A **train ticket app** scans every seat in a coach to show which ones are still free. An **exam result system** goes through every student's marks to decide pass or fail. A **shopping cart** adds every item's price to build your bill. None of these apps copy-paste the same instruction hundreds of times by hand. They use a single piece of logic and **run it again and again** — automatically, cleanly, without careless mistakes.

In the previous session, you taught your programs to **think and choose** — checking marks, applying discounts, validating input with **if**, **elif**, and **else**. That was a major upgrade. But every instruction still ran **once**, from top to bottom, like reading a recipe straight through without ever going back to step one. Now your programs are ready for their next skill: the ability to **repeat**.

---

## When doing it once is not enough

Imagine you are in charge of printing **multiplication tables** for an entire coaching class — tables of 7, 8, 9, and 10, each with ten rows. You could write every line by hand: 7 × 1 = 7, 7 × 2 = 14, and so on. For one table, that is annoying. For four tables, it is exhausting. For a hundred students who each need a personalised set of tables, it becomes impossible without help.

Now picture a **college results desk** again — but this time the challenge is different. You are not just deciding pass or fail for one student. You must process **every mark in a list of five hundred students**, add up a shopping bill with **twenty items**, **count** how many students are present, or **filter** out invalid scores before calculating a total. You might also keep asking for a **password** until the user finally types eight characters. You do not know in advance how many tries they will need. Sometimes they get it right on the first attempt; sometimes it takes four.

What if you had to do all of this by hand — sum every price, count every "present", skip every wrong score, and retry every weak password — for hundreds of people in one afternoon? Mistakes would pile up. Energy would run out. The work would not scale.

This is where **loops** come in. A **loop** — also called an **iteration** — is simply a way of telling a program: *"Do this block of steps again and again, until a condition changes or every item has been handled."* Instead of copying the same logic ten or hundred times, you write it **once** and let the computer run it for you.

---

## Two ways to repeat — and when to use each

Not every repetition works the same way, and choosing the right approach is half the battle.

A **`while` loop** is for situations where you keep going **until something changes**. Think of waiting at a traffic signal: you stay still **while** the light is red, and you only move when it turns green. You do not know exactly how long you will wait — the condition decides when to stop. This fits problems like **password validation** (keep asking until the input is long enough), **PIN entry** (retry until the code is correct), or **saving ₹500 every month** until your balance crosses ₹5,000.

A **`for` loop** is for situations where you already know **what to visit** — every fruit in a list, every student on an attendance sheet, every ball in a cricket over. A teacher calling roll does not guess how many names are on the list; they simply go through **each name, one by one**. When you need to count numbers in order — like printing 1 through 10 or building a multiplication table — Python offers a helper called **`range()`**, which hands you numbers one at a time without writing each number yourself.

Sometimes you need finer control inside a loop. **`break`** means *"stop the loop right now — we are done."* Like finding your Aadhaar card in the second drawer and closing the rest without checking. **`continue`** means *"skip this round only, but keep going."* Like packing tiffin boxes and skipping one spoiled roti while still filling the rest.

Together with the **conditionals** you already know, loops let your programs both **decide** and **repeat** — the combination real applications and **agentic systems** rely on every day. An AI agent often works the same way: try a step, check a rule, retry if needed, skip a bad input, stop when the goal is met.

---

## Think of it like a photocopy machine

Here is a simple way to hold the core idea in your head. A **photocopy machine** does not draw each page by hand. You place one original, press start, and the machine repeats the same print action fifty times. You wrote the logic once; the machine applied it everywhere.

That is the spirit of **automation through loops**. Three patterns show up again and again in real programs:

- **Summing** — start with zero, add each price or mark to a running total, and get the full bill or grand total at the end.
- **Counting** — start with zero, increase the count whenever a rule matches — how many students are present, how many items cost ₹150 or more.
- **Filtering** — keep or process only the items that pass a check — skip invalid scores, ignore negative prices, print only the values you care about.

An **accumulator** is just a friendly name for that running total — a variable that usually starts at zero and grows inside the loop, round by round. The **LOOP method** for problem-solving follows the same calm habit you used with conditionals: **list the goal**, **observe what repeats**, **outline which loop fits**, and **process one small step inside each round** — testing each part before combining them.

---

**In this pre-read, you'll discover:**

- How **`while` loops** and **`for` loops** let a program repeat actions automatically instead of copying the same steps many times.
- When to choose **`for`** (you know the items or count) versus **`while`** (you repeat until a condition changes).
- How **`break`** and **`continue`** give you control to stop early or skip one round without stopping the whole process.
- How **summing**, **counting**, and **filtering** turn one small rule into automation across bills, attendance lists, and large datasets.

---

A **loop** is any structure that runs the same block of steps more than once. An **iteration** is one single round of that loop — like serving one person in the prasad queue before moving to the next. An **infinite loop** happens when the stopping condition never becomes false — the program runs forever, like a counter that never increases. A **sentinel value** is a special input — such as typing `0` to finish adding prices — that signals the loop should stop. None of this needs advanced maths. It needs the same patience you use when checking a long list — one item at a time, without losing track.

---

## After this session, you'll be able to

- Print **number sequences and multiplication tables** using **`for` loops** and **`range()`** without writing every line separately.
- Build **input validation** that keeps asking until the user enters acceptable data — passwords, PINs, and savings goals.
- Process **lists of marks, prices, or attendance statuses** by combining loops with the conditionals you already know.
- **Sum**, **count**, and **filter** data in one pass — shopping bills, present students, valid scores only.
- Use **`break`** to stop a search as soon as you find what you need, and **`continue`** to skip unwanted items while keeping the loop running.
- Apply the **LOOP method** to plan and solve repetitive problems step by step — and spot common mistakes like off-by-one counts and loops that never end.

These automation skills prepare you for **functions** and richer **data structures** in upcoming lessons, and later for the repeated steps inside **agentic systems** you will design in this course.

---

## Questions we will solve together in the live class

1. **A student saves ₹500 every month starting from zero.** How does a program add the saving each round, print the balance after every month, and stop exactly when the total reaches at least ₹5,000 — without guessing the number of months in advance? Why is a **`while` loop** the natural fit here?

2. **You have a shopping list with prices ₹120, ₹85, ₹250, ₹40, and ₹199.** How do you calculate the **total bill**, **count** how many items cost ₹150 or more, and **filter** out anything under ₹100 for a discount list — all with loops instead of five separate additions?

3. **A coaching app must keep asking for a 4-digit PIN until the user types the correct one — or stop early after three wrong tries.** When should you use **`while`**, when does **`break`** help, and what happens if you forget to update the variable that controls when the loop stops?

Bring your curiosity. Every app that retries a payment, scans a seat list, grades a whole class, or totals a cart runs on the same repetition logic you are about to learn. The live session turns these everyday scenarios into programs you can write, test, and scale.
