# GenAI Coding Lab I

## What You Will Learn in This Lesson

In the previous session, you learned **Git branching**, **merging**, **conflict resolution**, and **team collaboration** on GitHub. You can now work on separate feature branches, merge safely, and share code through pull requests without breaking the stable `main` copy.

Before that, you also practised **DSA problem solving** on your local machine — breaking problems into **input**, **output**, **conditions**, and **steps**, and solving questions with **lists**, **strings**, **dictionaries**, **nested loops**, and **sorting**.

In this lesson, you will learn how to use **AI coding tools** (such as **ChatGPT** and **Claude**) as a learning partner — not a shortcut that replaces your thinking. You will:

- Use AI to **explain and clarify DSA concepts** in plain language
- **Generate pseudocode** for algorithms before writing Python code
- **Visualize step-by-step execution** of an algorithm with AI assistance
- **Debug solutions** and build **problem-solving intuition** you can reuse on your own

By the end, you will have a repeatable lab workflow: **understand → clarify → plan → trace → implement → verify → reflect**.

---

## Introduction to AI-Assisted Problem Solving

- **Official Definition:** **AI-assisted problem solving** is the practice of using **large language model (LLM)** tools — such as **ChatGPT** or **Claude** — to clarify concepts, draft plans, trace logic, and debug code while you remain responsible for understanding and verifying every result.
- **In Simple Words:** AI is like a patient tutor who explains ideas in many ways — but you still solve practice sums and check your own answers.
- **Real-Life Example:** Google Maps suggests a route; you still ride, watch traffic, and decide when to turn. AI suggests problem-solving routes; you still drive the code on your laptop.

| Tool | Simple picture |
|---|---|
| **ChatGPT** / **Claude** | Chat assistant that explains and plans in plain English |
| **GitHub Copilot** | Auto-suggest while you type in VS Code |
| **VS Code + AI extensions** | Your editor with a helper nearby |

**What AI helps with:** explain DSA ideas, draft **pseudocode**, produce **trace tables**, suggest debug fixes, and compare approaches.

**What AI cannot replace:** reading **constraints**, testing **edge cases**, understanding every line you run, and judging when an answer is wrong.

**Safe habits:** never paste private data into public chats; use a **feature branch** (`git switch -c ai-dsa-practice`) for experiments; read every generated line before running; commit useful prompts and corrected code.

**Logic to remember:** Treat AI output as a **first draft**. Interviews and real projects still need **your brain** — AI speeds learning; it does not remove thinking.

![AI suggests the route like GPS navigation, but you still ride the scooter and verify every turn — the same way AI drafts plans while you implement and test code on your laptop](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session13/session13-02-ai-learning-partner.png?v=20260721)

---

## The GenAI DSA Lab Workflow

Before jumping into tools, lock one reusable loop. Every problem in this lab follows the same rhythm.

| Step | What you do | Why it matters |
|---|---|---|
| **1. Understand** | Read the problem; list input, output, constraints | Stops you from coding the wrong question |
| **2. Clarify** | Ask AI to explain unfamiliar words or patterns | Fills gaps without skipping thinking |
| **3. Plan** | Generate or write **pseudocode** | Separates logic from syntax errors |
| **4. Trace** | Dry-run on paper or with AI step tables | Catches wrong logic before Python |
| **5. Implement** | Write Python on your local machine | Builds real skill in VS Code |
| **6. Verify** | Test normal + edge cases; compare with trace | Proves the solution is trustworthy |
| **7. Reflect** | Note what confused you and what pattern appeared | Turns one problem into long-term intuition |

**Connecting idea:** Steps 2–4 are where AI helps most. Steps 5–7 are where **you** become the programmer.

**Common mistake:** Skipping straight from problem statement to "Write full Python code for me." You may get runnable code you do not understand — and you will freeze when the question changes slightly in an assignment.

![GenAI DSA lab workflow — understand the problem, clarify with AI, plan pseudocode, trace step by step, implement in Python, verify with tests, then reflect and build intuition for the next question](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session13/session13-01-genai-lab-workflow.png?v=20260721)

---

## Using AI to Explain and Clarify DSA Concepts

- **Official Definition:** **Concept clarification** is the act of restating a technical idea in simpler language, often with examples, until the learner can predict how it behaves on new input.
- **In Simple Words:** You ask "What does nested loop really mean?" until you can explain it to a friend without reading notes.
- **Real-Life Example:** A new cricket fan asks what "strike rate" means. A good commentator explains with runs and balls faced — not only the formula. AI can be that commentator for DSA terms.

### How to write a strong "explain this concept" prompt

A weak prompt: `Explain nested loops.`  
A strong prompt:

```text
I am a beginner learning Python DSA.
Explain nested loops in simple English with:
1) a one-line official definition
2) a daily-life analogy from India
3) one small list example traced step by step
4) one common beginner mistake
Keep each paragraph under 3 sentences.
```

**Why this works:**

- You state your **level** (beginner).
- You ask for a **fixed structure** (definition, analogy, trace, mistake).
- You set a **length limit** so the answer stays scannable.

### Example: Asking AI to explain Bubble Sort

Expect a reply with definition (swap adjacent wrong-order pairs until sorted), simple words (values "bubble" to the end like soda bubbles), and a real-life analogy (students lining up by height, swapping neighbors each pass).

After reading, **close the chat** and rewrite definition, simple words, and example in your notebook without looking. If you cannot, ask AI to rephrase with a smaller numeric example.

### Practice Activity: Clarify One Concept in Your Own Words

Pick one topic that still feels fuzzy — for example **time complexity**, **two-pointer technique**, or **dictionary `.get()`**.

1. Open your AI assistant and use the strong prompt pattern above.
2. Read the reply once slowly; highlight words you still do not know.
3. Ask one follow-up: `Explain only the highlighted part with a numeric example.`
4. In your notes, write **In Simple Words** and **Real-Life Example** without copying the AI reply word for word.
5. Create one tiny Python example (3–5 lines) that demonstrates the idea on your machine.

**Self-check:** Can you predict the output before pressing Run? If yes, clarification worked.

---

## Generating Pseudocode Before Implementation

- **Official Definition:** **Pseudocode** is a human-readable step list for an algorithm without strict programming syntax; **pseudocode generation** is producing those steps from a problem statement — often with AI help — before writing executable code.
- **In Simple Words:** Pseudocode is the recipe on paper before you open the masala dabba; AI drafts steps, you cross out wrong ones like a friend reviewing your exam plan.
- **Real-Life Example:** A caterer writes "Soak rice → boil → dum 20 min" before entering the kitchen. Programmers write pseudocode before VS Code.

**Why plan first:** syntax errors hide logic mistakes; pseudocode is easy to edit; interviewers care about **clear thinking**; AI lets you **reject bad plans** cheaply before Python.

**Course pseudocode style:**

```
INPUT: list nums, target sum k
OUTPUT: True if any two numbers add up to k, else False
SET seen TO empty dictionary
FOR each number n in nums:
    IF (k - n) is already in seen: RETURN True
    STORE n in seen
RETURN False
```

![Plan before you code — write pseudocode steps on paper like a caterer planning a recipe, then translate the approved steps into Python on your laptop](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session13/session13-03-pseudocode-before-python.png?v=20260721)

### Strong prompt template for pseudocode

```text
Problem: Given a list of integers, return True if any two distinct
elements have the same value (duplicate exists), else False.

Constraints:
- List can be empty or have one element
- Values can be negative

Task:
Write pseudocode only (no Python).
Use INPUT, OUTPUT, and numbered steps.
Mention edge cases explicitly.
After pseudocode, list 3 test cases including one edge case.
```

### Review checklist before you accept AI pseudocode

| Check | Question to ask |
|---|---|
| **Correct problem** | Did AI solve the question you asked, not a similar one? |
| **Edge cases** | Empty input, single element, all same values — covered? |
| **Efficiency hint** | For large lists, is nested loop acceptable or is a dictionary better? |
| **Your understanding** | Can you execute the steps manually on `[1, 2, 1]`? |

**Common mistake:** Accepting pseudocode that says "compare every pair" for a duplicate check when the problem also asks for **indexes** — the plan may be incomplete. Always map steps back to the exact output format.

### Practice Activity: From Problem Statement to Pseudocode

**Problem:** Given a list of exam scores, return the **second largest unique** score. If no second unique score exists, return `None`.

1. Write input, output, and constraints in a table (same style as earlier DSA lessons).
2. Prompt your AI tool with the strong pseudocode template; paste your table into the prompt.
3. Read the pseudocode and mark any step you disagree with in `[brackets]`.
4. Rewrite the marked steps yourself — one sentence per step.
5. Run three manual traces: normal list, all equal values, list with duplicates of the maximum only.

Do **not** open Python until all three traces match your expected answers.

---

## From Pseudocode to Python — Full Worked Example

Now connect planning to code. We will solve the **duplicate detection** problem using AI-generated pseudocode that you verify first.

**Problem statement:** Given a list of integers, return `True` if any value appears more than once, else `False`.

**Constraints:** List may be empty; length can be up to a few thousand (nested loop is acceptable for learning size).

**Pseudocode (reviewed and approved):**

```
INPUT: nums (list of integers)
OUTPUT: Boolean

IF length of nums < 2:
    RETURN False

FOR i from 0 to length(nums) - 1:
    FOR j from i + 1 to length(nums) - 1:
        IF nums[i] == nums[j]:
            RETURN True

RETURN False
```

**Python implementation:**

```python
def has_duplicate(nums):  # Define a function that checks for duplicates
    if len(nums) < 2:  # If fewer than 2 items, duplicate is impossible
        return False  # Return False early for empty or single-item lists

    for i in range(len(nums)):  # Outer loop picks the first index of a pair
        for j in range(i + 1, len(nums)):  # Inner loop picks a later index only
            if nums[i] == nums[j]:  # If two different positions share a value
                return True  # Duplicate found — stop and return True

    return False  # No duplicate pair found after all comparisons


# --- Test block ---
print(has_duplicate([101, 204, 101]))  # Expected: True
print(has_duplicate([5, 6, 7]))  # Expected: False
print(has_duplicate([]))  # Expected: False
print(has_duplicate([42]))  # Expected: False
```

**How the code works:**

- Early return for lists with fewer than two elements avoids useless nested loops.
- The outer index `i` and inner index `j` compare each **unique pair** once.
- Returning `True` immediately inside the loop is correct — no need to keep searching.
- The test block at the bottom runs four cases: duplicate present, no duplicate, empty, single item.

**Building intuition:** Nested loops feel slow for huge lists — that is honest. Later you will meet **set** and **dictionary** patterns for faster duplicate checks. For learning, nested loops make the logic visible.

---

## Visualizing Step-by-Step Algorithm Execution

- **Official Definition:** **Algorithm visualization** (or **tracing**) is the manual or assisted recording of variable values and control flow at each step of an algorithm for a given input.
- **In Simple Words:** You pretend you are the computer and write what changes after every line.
- **Real-Life Example:** Tracking a T20 over ball by ball on Cricinfo — each ball updates the scoreboard. Tracing updates variable values the same way.

You already met **dry runs** in earlier DSA practice. AI makes tracing faster by producing tables — but **you** must confirm each row.

### Prompt for AI-assisted trace table

```text
Trace this pseudocode manually for input nums = [4, 7, 4, 9].

Show a table with columns:
Step | i | j | nums[i] | nums[j] | Match? | Return value so far

Stop early if the function returns.
After the table, state the final output in one sentence.
```

**Sample trace (partial):**

| Step | i | j | nums[i] | nums[j] | Match? | Return so far |
|---|---|---|---|---|---|---|
| 1 | 0 | 1 | 4 | 7 | No | — |
| 2 | 0 | 2 | 4 | 4 | Yes | True |

When the table shows **Match? = Yes**, the function returns `True` immediately — remaining rows are not executed.

![Trace an algorithm step by step like a ball-by-ball scoreboard — track i, j, compared values, and stop as soon as a duplicate match returns True](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session13/session13-04-trace-table-dry-run.png?v=20260721)

### When visualization catches bugs planning missed

- You assumed the inner loop starts at `0` — trace shows you double-count pairs.
- You forgot empty list handling — trace never enters loops but output should be `False`.
- You return `False` inside the loop by mistake — trace shows you quit too early on `[1, 2, 3]`.

**Common doubt:** "My code runs; do I still need a trace?"  
Yes — for assignments and interviews, **correct on one sample** is not enough. Traces prove you understand **all** paths.

### Practice Activity: Trace Before Run

Use this pseudocode for **find maximum in a list** (no built-in `max()`):

```
INPUT: nums
IF nums is empty: RETURN None
SET current_max TO nums[0]
FOR each n in nums:
    IF n > current_max: SET current_max TO n
RETURN current_max
```

1. Ask AI for a full trace table on input `[3, 9, 2, 9]`.
2. Cover one column with your hand and predict the next row before revealing it.
3. Write the Python function yourself and run the same input.
4. If Python output and trace disagree, find the first row where they split — that is your bug location.

---

## Debugging and Building Problem-Solving Intuition

- **Official Definition:** **Debugging** is the systematic process of finding and fixing errors in code — logic mistakes, runtime crashes, or wrong output — using evidence such as error messages, print statements, and traces.
- **In Simple Words:** Debugging is detective work: collect clues, form a guess, test one small change, repeat.
- **Real-Life Example:** Your scooter will not start. You check petrol, then spark plug, then battery — one test at a time. You do not replace the entire engine on the first guess.

**Problem-solving intuition** means recognizing **patterns** — "this smells like a duplicate problem," "this needs sorting first" — so the next question feels familiar even if numbers change.

### Three types of issues you will meet

| Type | What you see | First move |
|---|---|---|
| **Syntax error** | Red underline; `SyntaxError`, `IndentationError` | Read the line number; fix spelling, colons, indentation |
| **Runtime error** | Program crashes; `IndexError`, `TypeError` | Check empty input, wrong index, wrong data type |
| **Logic error** | Program runs but wrong answer | Trace small input; compare with expected table |

### How to prompt AI for debugging (without cheating your learning)

**Weak prompt:** `Fix my code.`  
**Strong prompt:** paste the problem goal, your code, the exact error or wrong output, what you already tried, and ask for (1) cause in simple English, (2) unsafe line, (3) **minimal fix** — not a full rewrite, (4) one edge-case test.

**Why this works:** You share **context**, **evidence**, and **your attempt**. AI teaches the **reason**, not only a pasted replacement.

### Intuition builders to note after each debug session

- **Pattern name:** duplicate scan, two-pointer merge, sort-then-pick, frequency count.
- **Trigger phrase in question:** "second largest," "pair with sum," "without built-in max."
- **Data structure chosen:** list only, dictionary for counts, sorted copy for ranking.
- **Edge case that broke you:** empty list, all equal, negative numbers.

Keep a one-page **"Bug Diary"** in your repo: date, problem, wrong line, lesson. After ten entries, you will spot mistakes faster than AI suggests fixes.

### Practice Activity: Debug a Broken Snippet

The function below should return how many pairs in a list add up to `target`, counting unique index pairs once.

```python
def count_pairs_with_sum(nums, target):  # Count pairs that sum to target
    count = 0  # Initialize pair counter
    for i in range(len(nums)):  # Outer loop index
        for j in range(len(nums)):  # Inner loop index — BUG is here
            if nums[i] + nums[j] == target:  # Check pair sum
                count = count + 1  # Increase count when sum matches
    return count  # Return final count


print(count_pairs_with_sum([1, 2, 3, 4, 5], 6))  # Expected: 2, got 4
```

**Your steps:**

1. Run the file and record expected vs actual output.
2. Ask AI for the **cause** using the strong debugging prompt — paste the code and wrong output.
3. Predict the fix before applying it (likely inner loop should start at `i + 1`).
4. Apply the fix, rerun, and add tests: `[1, 1, 2, 3]` with target `4`, empty list, no valid pair.
5. Write one sentence in your Bug Diary: what pattern caused double counting.

**Corrected inner loop line:**

```python
        for j in range(i + 1, len(nums)):  # Compare each unique pair only once
```

---

## End-to-End Lab: Two Sum with AI at Each Stage

Pull every skill into one problem — given a list and a **target**, return `True` if any two **distinct positions** add up to the target.

**Understand:** input `nums = [2, 7, 11, 15]`, `target = 9` → output `True` (`2 + 7`); edge cases — empty list or one element → `False`.

**Clarify with AI:** `Explain the dictionary approach for Two Sum to a beginner with a shopping-list analogy.` Idea — store each seen number; for current `n`, check if `target - n` was seen earlier.

**Pseudocode (you edit AI draft):**

```
INPUT: nums, target | OUTPUT: Boolean
CREATE empty dictionary seen
FOR each index i, value n in nums:
    need = target - n
    IF need in seen: RETURN True
    STORE seen[n] = i
RETURN False
```

**Trace:** on `[2, 7, 11, 15]`, when `n = 7`, `need = 2`, and `2` is already in `seen` → return `True`.

![Two Sum with a dictionary seen map — store each visited number, check complement target minus n, and return True when the needed pair was seen earlier in one pass](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session13/session13-05-two-sum-dictionary-intuition.png?v=20260721)

**Python:**

```python
def two_sum_exists(nums, target):  # True if two distinct indexes sum to target
    seen = {}  # value -> index for visited numbers
    for i in range(len(nums)):  # walk each index
        n = nums[i]  # current value
        need = target - n  # complement that completes the pair
        if need in seen:  # pair found at an earlier index
            return True
        seen[n] = i  # record value for future checks
    return False  # no pair after full scan

print(two_sum_exists([2, 7, 11, 15], 9))  # True
print(two_sum_exists([1, 2, 3], 7))  # False
print(two_sum_exists([], 0))  # False
```

**How the code works:** `seen` stores visited values; each step checks complement `need`; one pass — no nested loops. Nested loops would also work but scale worse — that comparison builds **intuition**.

**Verify and save:** run edge cases; commit on your feature branch. AI chats are temporary; **Git commits** are your permanent learning record.

### Prompt patterns to save in `prompts.md`

| Goal | Skeleton |
|---|---|
| **Explain** | definition + Indian analogy + tiny example + common mistake |
| **Pseudocode** | problem + constraints + INPUT/OUTPUT steps + 3 test cases |
| **Trace** | table with Step, variables, condition, output; stop at return |
| **Debug** | goal + code + error + what you tried + minimal fix + one test |

### Responsible use and mini lab checklist

- Read assignment rules before using AI; always be able to **explain your code line by line** in a viva.
- Rewrite clever one-liners you do not understand into simpler steps you own.
- **Mini lab (solo):** pick a known problem → constraints table → AI pseudocode with your `[edits]` → two traces → Python in VS Code → four tests → one Bug Diary entry → commit on a feature branch.

---

## Common Errors When Using AI for DSA

| Situation | What usually went wrong | What to do |
|---|---|---|
| Code runs on AI site but not locally | Different Python version or missing file setup | Run only in your VS Code environment |
| AI used `max()` when question forbids it | Prompt did not state constraints | Repeat prompt with "Do not use built-in max/sort" |
| Trace table looks perfect but code fails | Table was for different input size or wrong loop start | Re-trace on the exact input your code uses |
| AI says `O(1)` for every solution | Oversimplified complexity | Ask: "Explain time in simple words for input size n" |
| You cannot explain your own code | Copy-paste without stages 3–4 | Delete code; rebuild from pseudocode only |
| Infinite chat, no file saved | Treating chat as notebook | Move final artifacts to `.py` files and Git |

Mistakes are normal. The lab workflow exists so you catch them **before** submission, not after feedback.

### Quick Self-Check Before You Leave Practice

- Can I write a strong **explain-concept** prompt with level, structure, and length limit?
- Can I generate **pseudocode** with AI, edit wrong steps, and trace it by hand before Python?
- Can I read an AI **trace table** and spot when a loop starts at the wrong index?
- Can I debug with AI using **minimal fix** language instead of "rewrite everything"?
- Did I save final `.py` files and at least one commit on a **feature branch**?

If any answer is "not yet," repeat one practice activity from this lesson before moving on.

---

## How This Fits Your Journey Ahead

You can now combine **local Python DSA skills**, **Git collaboration habits**, and **AI-assisted planning and debugging** into one disciplined practice loop.

In upcoming lessons, you will tackle harder algorithm patterns and larger projects where fast planning and clean traces save hours. The intuition you build here — reading constraints, rejecting bad pseudocode, tracing before running — stays useful even when the AI model changes or is unavailable.

Keep your **Bug Diary** and **prompt templates** updated. They become personal documentation no generic chat can replace.

---

## Key Takeaways

- **AI coding assistants** explain concepts, draft pseudocode, produce trace tables, and help debug — but **you** verify every step on your machine.
- The reusable lab loop is **understand → clarify → plan → trace → implement → verify → reflect**; skipping planning produces code you cannot defend in a viva.
- **Strong prompts** include your level, constraints, desired format, and what you already tried — especially for debugging.
- **Visualization (dry runs)** catches logic errors early; compare AI-generated tables with your hand trace before trusting them.
- **Git feature branches** keep AI experiments safe while `main` stays stable — commit corrected work so learning is recorded.

These habits turn AI from a shortcut into a **learning accelerator** for every DSA topic ahead.

---

## Important Commands, Libraries, Terminologies Used

| Term / Command | Meaning in Simple Words |
|---|---|
| **AI coding assistant** | Chat tool that explains, plans, and suggests code from natural language |
| **LLM** | Large Language Model — the engine behind tools like ChatGPT and Claude |
| **Prompt** | The instruction you type to guide AI's reply |
| **Pseudocode** | Plain-language step list before real Python syntax |
| **Dry run / trace** | Manual step-by-step record of variable values |
| **Algorithm visualization** | Table or diagram showing execution over time |
| **Debugging** | Finding and fixing syntax, runtime, or logic errors |
| **Problem-solving intuition** | Recognizing familiar patterns in new questions |
| **Edge case** | Unusual but valid input — empty list, one item, all duplicates |
| **Nested loop** | Loop inside another loop — compares pairs of items |
| **Two Sum pattern** | Check if two elements satisfy a sum using complements |
| **Hash map / dictionary `seen`** | Stores values already visited for fast lookup |
| **Syntax error** | Invalid Python grammar — colons, indentation, spelling |
| **Runtime error** | Crash while program runs — bad index, wrong type |
| **Logic error** | Program runs but answer is wrong |
| **Feature branch** | Separate Git line for one experiment or feature |
| **`git switch -c branch-name`** | Create and move to a new branch |
| **`python file.py`** | Run your Python file in Terminal |
| **Bug Diary** | Personal log of mistakes and lessons learned |
| **Responsible AI use** | Learn with AI while following rules and owning your work |
