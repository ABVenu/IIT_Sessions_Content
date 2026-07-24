# Pre-read: Operators & Conditional Statements

You are standing at a railway station with a ticket in your hand. The display board says **Platform 3**. You do not wander randomly — you turn left, because that is where your train leaves from. If the board had shown a different number, you would have walked the other way. One piece of information, two possible paths, and you picked the right one without thinking twice.

That is exactly what the apps on your phone do millions of times every day. When you try to pay through **UPI**, the app checks your balance first — if the money is not enough, it stops and shows an error instead of completing the payment. When you open your **exam result portal**, it looks at your marks and shows either **Pass** or **Fail**. When you enter your **PIN at an ATM**, a wrong number blocks you; the correct one opens the menu. None of these apps follow a single fixed path. They **look at a situation, decide, and act accordingly**.

In the previous session, you learned to write Python programs in **OneCompiler** using **variables**, **data types**, **operators**, and basic **input/output**. Your programs could calculate marks, split bills, and show results — but every program ran the same way from top to bottom, like a fixed recipe that never changes. That was a strong start. Now your programs are ready for their next upgrade: the ability to **think and choose**.

---

## Context of This Session in the Course

```mermaid
%%{init: {"diagramPadding": 24, "flowchart": {"htmlLabels": true, "nodeSpacing": 90, "rankSpacing": 110, "curve": "basis", "padding": 20}, "theme": "base", "themeVariables": {"fontFamily": "Arial", "fontSize": "15px", "lineColor": "#334155"}}}%%
flowchart TB
    subgraph FOUNDATION[" "]
        direction LR
        PREV[["&nbsp;&nbsp;<b>Current Module Until Previous Session</b>&nbsp;&nbsp;<br/><br/>Introduction to Programming<br/>&amp; Python Basics<br/><br/><i>OneCompiler · variables · operators<br/>input and output</i><br/><br/><i>Straight-line programs<br/>that calculate and display</i>"]]
    end

    CURRENT{{"&nbsp;&nbsp;<b>Current Session</b>&nbsp;&nbsp;<br/><br/>Operators &amp; Conditional<br/>Statements<br/><br/><i>if · elif · else · boolean logic</i><br/><br/><b>Mental shift:</b><br/>from fixed steps<br/>to smart choices"}}

    subgraph VALUE[" "]
        direction LR
        COURSE["&nbsp;&nbsp;<b>Course Connection</b>&nbsp;&nbsp;<br/><br/>Decision logic for loops,<br/>data handling, and the<br/>rule-based choices inside<br/>agentic systems<br/><br/><i>Programs that choose<br/>different paths</i>"]
        REAL(["&nbsp;&nbsp;<b>Real-Life Connection</b>&nbsp;&nbsp;<br/><br/>UPI balance checks, exam<br/>results, ATM PIN, train fares,<br/>and agent routing rules<br/><br/><i>Everyday apps that<br/>decide before they act</i>"])
    end

    subgraph FUTURE[" "]
        direction LR
        M2["&nbsp;&nbsp;<b>Upcoming Module</b>&nbsp;&nbsp;<br/><br/>Fundamentals of ML<br/>(Regression + Classification)<br/><br/><i>Will use: model training,<br/>evaluation, data prep</i>"]
        M3["&nbsp;&nbsp;<b>Upcoming Module</b>&nbsp;&nbsp;<br/><br/>GenAI &amp; Agents<br/>(LLMs + RAG + Tools)<br/><br/><i>Will use: prompts, retrieval,<br/>function calling</i>"]
        M4(["&nbsp;&nbsp;<b>Upcoming Module</b>&nbsp;&nbsp;<br/><br/>Agentic Systems &amp; Design<br/>(LangGraph + Deployment)<br/><br/><i>Will use: agent workflows,<br/>observability, capstone</i>"])
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

## When one answer is not enough

Imagine you are the clerk at a college results desk. A long queue of students waits with their mark sheets. For each student, you must decide: **Pass or Fail?** If they passed, which **grade** do they get — A, B, C, or D? If they failed, do you tell them it was because of low marks, low attendance, or both?

You *could* handle one student manually. But what if you had to process **five hundred students** in an afternoon, each with different marks, attendance records, and subject-wise scores? Doing every check by hand would be slow, tiring, and full of mistakes — especially when rules overlap, like needing at least 40 in every subject **and** 75% attendance to pass.

This is the kind of challenge that **conditional statements** solve. They let a program check a situation — a **condition** that is either true or false — and run different actions depending on the answer. A **boolean** value is simply a yes-or-no answer stored in code: either **True** or **False**, like answering whether you have a membership card at a shop.

You already met the building blocks in the previous session. **Comparison operators** let you ask questions like "Are the marks at least 40?" or "Is the age 18 or above?" **Logical operators** let you combine questions — **and** means both must be true (scholarship needs good marks *and* good attendance), **or** means at least one must be true (discount applies if the bill is above ₹1,000 *or* you have a membership card), and **not** flips the answer (login allowed only when the account is *not* locked).

---

## The fork in the road — and the menu with many options

Think of **conditional statements** like the signpost at that railway fork. The platform number is the **condition**. Your direction is the **action**. In Python, the word **if** means "only do this when the check passes" — like saying, *"If it is raining, take an umbrella."* The action happens only when the condition is true.

But life rarely stops at two choices. Sometimes you need an **otherwise** path. **else** covers everything the first check did not catch — like a pass/fail result where marks below 40 mean Fail and everything else means Pass. Exactly one path runs; never both, never neither.

Many real problems have **more than two** outcomes. At a restaurant, you might order thali — or if that is not available, dosa — or if neither works, a default combo. The kitchen checks options **in order** and stops at the first match. In Python, **elif** does the same thing: if the first check fails, try the next one, and keep going until something matches or the default **else** runs.

This pattern shows up everywhere around you:

- **Electricity billing slabs** — different rates for the first 100 units, the next 100, and anything above 200.
- **Train ticket categories** — free for very young children, half fare for kids, full fare for adults, senior discount for those above 60.
- **Grade ladders** — A for 90 and above, B for 75–89, and so on, checked from the highest threshold downward so nobody accidentally lands in the wrong grade.

The order of checks matters. Putting a lower threshold before a higher one is like putting "anyone above 40" before "anyone above 90" in a grade program — almost everyone would get the wrong grade. Getting the sequence right is part of **breaking word problems into logical, testable steps** before you write a single line of code.

---

## Decisions inside decisions — and following the path

Some problems need a second check only after the first one passes. Picture entering a stadium: first, the guard checks whether you have a ticket. Only if that passes does a second guard check whether you have a VIP pass for the premium stand. This is a **nested conditional** — one decision sitting inside another.

Login screens work the same way. If the username is wrong, the program says so immediately. If the username is right, it then checks the password — and gives a different error message for each kind of mistake. That is far more helpful than a single vague "login failed" for every case.

When several conditions must be checked together, you can combine them with **and**, **or**, and **not** inside a single decision — scholarship eligibility, shop discounts, and account-lock checks all work this way.

Before you trust any program, you should be able to **trace** it — walk through the logic with a sample input and mark which branch runs. If marks are 78, does the grade program print B or D? If age is exactly 12, does the child ticket rule apply? **Tracing execution paths** for sample inputs — especially **boundary values** like 40 for pass/fail or 90 for Grade A — catches most beginner mistakes before they become confusing bugs.

The **STEP method** gives you a reliable habit before you code: **State** the word problem in plain English, identify the **inputs** you need, list every **condition and outcome**, and only then write the Python. It is like making chai — boil water, add tea, add milk, add sugar. The order matters, and each step can be tested on its own.

These decision skills matter beyond exam portals and ticket counters. The **agentic systems** you will design later also need clear rules — if a user request is incomplete, ask for more details; if a tool call fails, retry or stop; if a condition is not met, take a different path. Every intelligent agent starts with the same kind of structured if-this-then-that thinking you are about to practise.

---

**In this pre-read, you'll discover:**

- How programs use **if**, **elif**, and **else** to choose different actions instead of running the same steps every time.
- Why **boolean logic** and **comparison operators** are the questions your program asks before it acts.
- How to break real **word problems** — exam results, bill slabs, discounts, login checks — into clear, testable steps using structured thinking.
- Why the **order of conditions** can make or break a program, and how **tracing sample inputs** helps you debug confidently.

---

A **condition** is any check that results in True or False — like asking whether marks are at least 40. **Program flow control** simply means the program can change which steps it runs based on those answers, rather than marching line by line from start to finish. **Indentation** — the spaces at the start of a line in Python — tells the computer which lines belong to which decision block; get it wrong and the wrong code runs. None of this requires advanced maths. It requires the same clarity you use when explaining rules to a friend: *"If this, then that; otherwise, something else."*

---

## After this session, you'll be able to

- Write programs that check user input and respond differently — voting eligibility, pass/fail results, even-or-odd numbers, and temperature warnings.
- Handle **multiple outcomes** with **elif** chains — grade calculators, electricity billing slabs, and train ticket categories by age.
- Combine **and**, **or**, and **not** inside conditions for scholarship rules, shop discounts, and login validation.
- Use **nested conditionals** when one decision depends on another, with clear error messages for each failure case.
- Apply the **STEP method** to plan any conditional word problem before writing code — and **trace execution paths** to debug when something does not behave as expected.

These decision-making skills prepare you for **loops** in upcoming lessons, where programs repeat actions and combine repetition with conditions — another building block for the **agentic systems** you will design later in this course.

---

## Questions we will solve together in the live class

1. **A student has marks in three subjects and an attendance percentage.** The college says you must pass every subject with at least 40 marks **and** maintain 75% attendance to get an overall Pass — and only then assign First, Second, or Third division based on average marks. How do you break this word problem into conditions, trace the path for different sample inputs, and explain **why** a student failed when more than one rule is broken?

2. **An electricity board charges ₹5 per unit for the first 100 units, ₹7 for units 101–200, and ₹10 beyond 200.** A customer enters their total units consumed. How does the program figure out which slab applies — and why does checking the slabs in the wrong order give wrong answers for almost everyone?

3. **You are building a simple ATM withdrawal check.** The account has ₹5,000. A user tries to withdraw an amount. How should the program handle three different situations — not enough balance, an invalid amount like zero or negative, and a successful withdrawal that updates the remaining balance — and how do you trace each path before running the program?

Bring your curiosity. Every app you use daily — from payments to results to ticket booking — runs on the same decision logic you are about to learn. The live session turns these everyday scenarios into programs you can write, test, trace, and trust.
