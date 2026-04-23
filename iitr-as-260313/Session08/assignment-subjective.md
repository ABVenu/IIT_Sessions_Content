# Subjective assignment — LLM-aware agent design

## Brief

You are designing an **Observe → Think → Act** assistant that calls an LLM and can use **web search** and **Python code execution**. You do **not** need to write API code.

---

## Scenario

A user uploads a **CSV** (employee ID, hours worked, hourly rate) with **80 rows** and asks:

*“Calculate **gross pay per row**, **company total gross pay**, and **flag rows where hours > 48**.”*

---

## Submit (one short document)

**1. Design note (about ½ page, max ~120 words)**  
Answer in prose: Why is it a bad idea to do all of this in the LLM’s head? Name the **relevant LLM limitations**, say **which tool** should produce the numbers, and what the LLM should do **after** those numbers exist.

**2. One Think-stage prompt**  
Write **one** prompt the agent sends to the LLM during **Think** so it can produce the next step (e.g. draft code, or interpret tool output). It must clearly include **role**, **context** (use placeholders like `[CSV_SAMPLE]` if needed), **task**, and **format** of the answer you want. Target **about 100–160 words**.

**3. What can still go wrong?**  
In **2–4 sentences**: name **one** failure mode even when using tools, and **one** mitigation.

---

## Submission

Markdown, plain text, PDF, or Google Doc — your cohort’s usual channel.

---

## Answer Explanation (for Assess)

**1.** Strong answers cite **unreliable precise arithmetic at scale** (and optionally **inconsistency**). Numbers should come from **code execution** on the real CSV; the LLM **writes or refines** code and/or **formats** results from **executed** output — not mental math in chat.

**2.** The Think prompt should ground the model: placeholders for data, explicit task (e.g. generate Python that reads CSV and computes totals/flags), and format (e.g. return only code, or return a short plan then code).

**3.** Valid risks: **buggy generated code**, **wrong file assumed**, **two runs differ slightly**; mitigations: **run/validate** outputs, **fixed randomness** where needed, **human check** on totals for payroll.

---

*End of subjective assignment.*
