# Pre-read: Pandas: Aggregation & Combining Data

## The hook

Imagine you are a team lead. Your boss does not want 10,000 rows of raw sales data. They want one clear answer: *How did each region perform last month?* In offices everywhere, people turn huge tables into short reports—totals, averages, and counts—so decisions can happen in a meeting, not in a spreadsheet maze. That skill is what we are building toward.

## The problem

**What if** you had employee data in one file, department names in another, and your manager asked for “average salary per department” and “total headcount per team”—all in one clean table?

Doing it by hand would mean sorting, copying, matching names, and recalculating every time the data changes. One small mistake breaks the whole report. The real challenge is not “math class” math; it is **organising** and **joining** information without drowning in rows.

## The solution preview

In this session, **pandas** is the hero tool. We will learn how to **summarise** big datasets into meaningful numbers (**aggregation**), how to group rows so we get answers “per team” or “per city” (**groupby**), how to fix messy column names and drop junk columns (**cleanup**), and how to **combine** two tables the right way (**merge**), like matching records that belong together.

## A simple analogy

Think of **grouping and summarising** like sorting laundry before washing: you **split** clothes into piles (whites, darks, colours), you **apply** the right wash to each pile, then you **combine** everything back in the cupboard. The lecture uses exactly this picture—many rows become neat piles, and each pile gets one clear summary. That is the core idea behind *split → apply → combine*.

## What you will be able to do after the session

- Turn a full column into one useful number (total, average, count, min, max, and more).
- Build **per-group** reports—for example, averages **per department**—without manual sorting.
- Create **rich reports in one go** (several calculations together), with clear column names managers can read.
- **Clean** tables by renaming ugly headers and removing useless columns.
- **Merge** two datasets using a shared key, and know when to use inner, left, right, or outer style joins—and what **join** on the index means, at a high level.

## Questions we will answer in the live session

1. How do you go from “one big salary column” to “average salary **for each department**” in a structured way—without losing track of which number belongs to which group?
2. When one table has employee IDs and another has department details, how do you **match** rows safely so nobody’s data ends up beside the wrong department?
3. How do you pack **many** summary numbers (total, average, headcount, and more) into **one** neat report—with names your boss will actually understand?

Come curious: we will connect cleanup, combining, and aggregation into a small **realistic workflow**—the kind analysts use every day.
