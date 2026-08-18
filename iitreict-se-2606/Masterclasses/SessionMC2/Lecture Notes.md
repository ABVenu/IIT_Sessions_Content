# Masterclass: Algorithms & Complexity Analysis

## What You Will Learn in This Session

In the previous masterclass you opened the lid of the computer. You learned that the **CPU**, **RAM**, and **storage** work as a team, and that a program can feel slow because the machine is waiting for disk, running out of memory, or sharing the CPU with many other processes.

That knowledge explains *machine* delays. This session explains *method* delays. Two programs can run on the same laptop, yet one finishes in a blink and the other takes minutes — because they follow different **algorithms**.

You have already written Python programs that loop through lists, store data, sort values, and search for items. Today the question is: which method should you choose, and how do you compare methods before you commit to one?

You will learn:

- Why we need **algorithms** instead of solving every problem with one-off, ad-hoc steps.
- Why an approach that works for 10 items can become unusable for 10,000 items.
- What **time complexity** and **space complexity** mean at a conceptual level.
- How **Big-O** helps you compare two approaches to the same problem without running both on huge data.
- Why **searching** and **sorting** strategies should be compared *before* you pick one.

By the end, you will look at a problem and ask: "What is my plan, how does the work grow, and is there a better plan?" — not just "Does this code run on a tiny example?"

---

## Why We Need Algorithms

Before we talk about speed, we need a clear idea of what an algorithm is, and why "I will just figure it out as I go" is not enough for software.

### Ad-Hoc Steps vs a Repeatable Plan

- **Official Definition:** An **ad-hoc approach** is a one-time, improvised sequence of steps made for a single situation, without a reusable method that others can follow or measure.
- **In Simple Words:** Ad-hoc means you solve today's problem by guessing, trying, and adjusting — and tomorrow you may not remember what you did.
- **Real-Life Example:** You need to reach a cousin's house in a new city. You take random turns, ask three people, and somehow arrive. Next week you cannot repeat the same journey, and you cannot teach a friend the route.

Now contrast that with a proper plan.

- **Official Definition:** An **algorithm** is a finite, step-by-step procedure that takes an input, follows well-defined rules, and produces a correct output in a finite amount of time.
- **In Simple Words:** An algorithm is a clear recipe. Anyone who follows the same steps, with the same ingredients, should get the same dish.
- **Real-Life Example:** A chai recipe — boil water, add tea leaves, add milk, add sugar, simmer, strain. The steps are ordered, they end, and the result is predictable. That is an algorithm in daily life.

Software is full of recipes: find a student in an attendance list, sort marks high to low, check if a UPI transaction ID already exists, decide who gets the last railway seat. If each developer invents a new private method every time, the program becomes hard to test, hard to debug, and hard to improve.

### Why a Recipe Beats Guessing

An algorithm gives you four practical benefits that ad-hoc steps do not:

- **Repeatable:** The same input should give the same output every time. If you search for roll number `104` today and tomorrow, the answer should not change because you "felt lucky."
- **Shareable:** A teammate can follow the same steps. You do not need to sit next to them and say "click here, then try that."
- **Checkable:** You can test the plan on small examples and know whether it is correct.
- **Comparable:** Once two plans are written clearly, you can ask which one does less work as the data grows.

Without a named method, you cannot compare methods. You can only say "it worked on my laptop."

### Common Doubt: "If My Code Works, Why Do I Need an Algorithm?"

Working on 8 names is not the same as working on 80,000 names. Ad-hoc code often hides nested loops and repeated scanning that you never notice on a tiny list. A correct algorithm is not only "gives the right answer" — it is a method you can reason about: how many checks, how much extra memory, and what happens when n becomes 10 times larger.

![Ad-hoc guessing versus a clear algorithm — a person taking random turns in a city on one side, and a numbered tea recipe card with ordered English steps on the other, showing why a repeatable plan beats improvising](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitreict-se-2606/masterclasses/sessionmc2/sessionmc2-01-adhoc-vs-algorithm.png)

### Activity: Write the Recipe, Not the Guess

Pick one everyday task: making instant noodles, finding a contact in your phone, or packing a school bag.

1. Write **ad-hoc steps** (messy, incomplete, "I will see as I go") in 3–4 lines.
2. Rewrite the same task as an **algorithm**: numbered steps, a clear start, a clear end, and a clear result.
3. Circle one step that another person might do differently. That circled step is where software also needs a decision — and later, a complexity comparison.

---

## When an Inefficient Approach Meets Growing Input

Once you have a plan, the next question is not "Does it work on 5 items?" The real question is "What happens when the input grows?" An approach that feels instant in class can become unusable in a real app.

### What Input Size Means

- **Official Definition:** **Input size** (often written as **n**) is the amount of data the algorithm must process — for example, the number of items in a list, the number of characters in a string, or the number of records in a file.
- **In Simple Words:** **n** is "how much stuff" you gave the program. Ten students is a small **n**. Ten lakh IRCTC users is a huge **n**.
- **Real-Life Example:** Checking attendance for a tutorial group of 12 students is easy. Checking attendance for a university with 40,000 students is the same *kind* of task — but the volume changes everything.

The algorithm did not become "wrong." The amount of work exploded.

### Why Slow Methods Hide on Small Data

Your laptop can do millions of simple checks per second. For `n = 10`, even a clumsy nested loop finishes before you blink, so you conclude "this is fine." Then the same method is used for a result portal with 50,000 students, a shopping app with 2 lakh products, or a UPI log with a full day of transactions.

The program suddenly takes seconds or minutes and users close the tab. The logic can still be "correct" — the method simply does too much work per extra item.

### A Concrete Picture: Nested Checks vs One Pass

Suppose you want to know whether any **roll number is repeated** in a list.

One natural but costly idea: for every roll number, scan the rest of the list to see if it appears again. That is a nested scan. If there are `n` roll numbers, you do work that grows like `n × n`.

A cheaper idea: keep a notebook of roll numbers you have already seen. For each new roll number, ask "Have I seen this?" If yes, you found a duplicate. If no, add it to the notebook. That is one pass through the list.

| n (roll numbers) | Nested scan (about n × n checks) | One pass (about n checks) |
|---|---|---|
| 10 | about 100 | about 10 |
| 100 | about 10,000 | about 100 |
| 1,000 | about 1,000,000 | about 1,000 |
| 10,000 | about 100,000,000 | about 10,000 |

The nested method is not 10 times slower when data becomes 10 times bigger. It is closer to **100 times** slower, because both loops grew.

That is the demerit of an inefficient approach: **the pain does not grow in a straight line.** It can grow in a curve that quickly becomes impossible.

![Input size growth — a small classroom register staying manageable, then a huge exam hall and a crowded railway booking screen where the same nested-checking method explodes in work as n grows](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitreict-se-2606/masterclasses/sessionmc2/sessionmc2-02-input-size-growth.png)

### Full Code: Count the Work, Not Just the Answer

Run this program (One Compiler or your editor). Notice that both methods can find the same duplicate — but they do very different amounts of work.

```python
# Store a list of roll numbers; 104 is repeated on purpose
rolls = [101, 102, 103, 104, 105, 104, 106]

# Start a counter for the nested-scan method
nested_checks = 0
# Remember whether the nested method found a duplicate
nested_found = False

# Walk through every position i in the list
for i in range(len(rolls)):
    # Walk through every later position j after i
    for j in range(i + 1, len(rolls)):
        # Count one comparison between two roll numbers
        nested_checks = nested_checks + 1
        # If the two positions hold the same roll number, we found a duplicate
        if rolls[i] == rolls[j]:
            # Record that a duplicate exists
            nested_found = True

# Start a counter for the one-pass notebook method
pass_checks = 0
# Create an empty set to remember roll numbers already seen
seen = set()
# Remember whether the one-pass method found a duplicate
pass_found = False

# Walk through each roll number exactly once
for roll in rolls:
    # Count one "have I seen this?" check
    pass_checks = pass_checks + 1
    # If this roll number is already in the notebook, it is a duplicate
    if roll in seen:
        # Record that a duplicate exists
        pass_found = True
    # If it is new, add it to the notebook for later checks
    else:
        # Store this roll number as already seen
        seen.add(roll)

# Print whether both methods agree on the answer
print("Nested method found a duplicate:", nested_found)
# Print how many pair-checks the nested method needed
print("Nested method checks:", nested_checks)
# Print whether the one-pass method found a duplicate
print("One-pass method found a duplicate:", pass_found)
# Print how many checks the one-pass method needed
print("One-pass method checks:", pass_checks)
```

**How the code works**

- The nested method compares pairs of positions. For 7 items, pair-checks are `6 + 5 + 4 + 3 + 2 + 1 = 21`.
- The one-pass method looks at each item once and asks a set "have I seen this?" — about 7 checks, using extra memory for `seen`.
- Both can report that `104` is repeated. If `rolls` later has 1,000 items, nested work grows like n² and one-pass work grows like n.

### Activity: Feel the Curve Yourself

Use the table pattern above and rough mental maths. Treat nested work as `n × n` and one-pass work as `n`. Fill values for `n = 20`, `n = 200`, and `n = 2,000`. Then complete: "When n became 10 times bigger, nested work became ____ times bigger, and one-pass work became ____ times bigger."

Expected direction: nested work grows by about **100 times** when n grows by 10 times. One-pass work grows by about **10 times**.

---

## Time Complexity and Space Complexity

You have seen that two correct methods can do very different amounts of work. Complexity is the language we use to describe that difference without depending on one laptop's speed.

### Time Complexity: How Work Grows

- **Official Definition:** **Time complexity** describes how the number of basic operations an algorithm performs grows as the input size **n** grows.
- **In Simple Words:** Time complexity is not "how many seconds on my phone." It is "if the list becomes 10 times longer, does the work become 10 times bigger, or 100 times bigger?"
- **Real-Life Example:** Serving one extra customer in a small kirana shop is one extra bill. If your "method" is to recount every item in the entire shop for each customer, one extra customer is a disaster. The second method has a much worse time complexity.

We do not measure only in seconds, because laptops differ, languages differ, and the OS may be sharing the CPU with Zoom or Chrome. Seconds mix **algorithm quality** with **machine luck**. Counting how work grows with **n** compares methods, not laptops.

### Space Complexity: How Extra Memory Grows

- **Official Definition:** **Space complexity** describes how the extra memory an algorithm needs grows as the input size **n** grows. Extra memory means storage beyond the input itself.
- **In Simple Words:** Does the method rearrange items on the same desk, or does it photocopy the whole register onto a second desk?
- **Real-Life Example:** Sorting students by height in a single queue needs almost no extra room — people swap places. Making a full photocopy of the attendance sheet needs extra paper. That extra paper is extra space.

A few useful distinctions:

- **Input space** is the original list. Almost every program needs that. We usually focus on **extra space**.
- **O(1) extra space** means a few variables, no matter how large n becomes — like keeping one sticky note.
- **O(n) extra space** means extra memory that grows with the list — like a second notebook with one line per student.

### The Time–Space Trade-Off

Faster methods often spend memory to save time. The duplicate finder above did exactly that: a `seen` set uses extra RAM so you do not scan the list again and again. That is not automatically bad — RAM exists to be used.

The professional question is: **Is the extra memory worth the time you save, on the data sizes you actually have?** A college tool on 2,000 names can afford extra memory. Copying a 10-lakh-row table just to make a lookup nicer can exhaust RAM.

![Time versus space complexity — a clock showing growing work on one side, and a study desk versus a second photocopied register on the other, showing the trade-off between extra time and extra memory](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitreict-se-2606/masterclasses/sessionmc2/sessionmc2-03-time-space-complexity.png)

### Activity: Packing for a Trip

You are packing for a two-day trip. **Strategy A** packs only what you will wear (tiny bag, extra re-planning if weather changes). **Strategy B** packs a backup of every outfit (heavy bag, almost no deciding later).

Write one line for each: is it better on **time** or **space**, and why? There is no single winner — this is the same judgement you will use for algorithms.

---

## Big-O Intuition: Comparing Two Approaches

Time and space complexity become useful when we can *name the growth pattern*. That name is **Big-O**.

### What Big-O Actually Tells You

- **Official Definition:** **Big-O notation** describes an upper bound on how an algorithm's time or extra space grows as input size **n** becomes large. It ignores constant details and focuses on the dominant growth pattern.
- **In Simple Words:** Big-O answers, "When the data gets huge, what kind of growth should I expect?" It is a label for the shape of the work, not the exact number of comparisons.
- **Real-Life Example:** Saying a journey is "highway driving" vs "visiting every gali" does not tell you the exact minutes. It tells you which plan will still make sense if the city becomes 10 times larger.

Common beginner mistake: thinking **O(n²)** means "exactly n² comparisons." It does not. It means the work grows like a square. Constants, such as `n × (n-1) / 2` pair checks, still sit in the **O(n²)** family.

### The Growth Family You Need for This Course

You do not need heavy mathematics here. You need four families that appear again and again in searching and sorting.

| Big-O | Growth in simple words | Everyday picture | Typical coding pattern |
|---|---|---|---|
| **O(1)** | Work stays almost the same even if n grows | Picking the top book from a labelled pile | Direct index access, `list[0]` |
| **O(log n)** | Work grows very slowly; data can double and you add only a few extra steps | Finding a name in a sorted phone directory by opening the middle | Binary search on sorted data |
| **O(n)** | Work grows in a straight line with n | Checking every student in a register once | A single loop over the list |
| **O(n²)** | Work grows like n times n | Every student compared with every other student | Nested loops over the same list |

**O(n log n)** also matters for good sorting methods (including Python's built-in sort). Read it as: "more than a single pass, much less than nested n × n work."

### Same Problem, Two Labels

Big-O is most powerful when both methods solve **the same problem**.

Problem: "Does this roll number exist in the list?"

- Walk from start to end until you find it or finish. That is **linear search**, **O(n)** time.
- If the list is already sorted, jump to the middle, throw away half, repeat. That is **binary search**, **O(log n)** time.

Both can be correct. Big-O tells you which plan stays kind as n grows.

For 16 items, binary search needs about 4–5 checks in the worst case (`16 → 8 → 4 → 2 → 1`), while linear search may need 16. For 1,000,000 items, binary search needs about 20 checks, while linear search may need 1,000,000. That gap is the difference between "instant" and "the app feels stuck."

### What Big-O Ignores (On Purpose)

Big-O hides laptop speed and tiny extra steps such as `print`, so you can compare growth shapes. It focuses on **large n**. For `n = 5`, a simple O(n²) method can beat a fancy method because fancy methods have extra setup.

Use Big-O to choose among serious options for real data sizes — not to brag that a complicated method is "better" for 6 names.

![Big-O growth families — four lanes labelled O(1), O(log n), O(n), and O(n squared), with queues staying flat, growing slowly, growing steadily, and exploding, so students can see shape rather than exact seconds](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitreict-se-2606/masterclasses/sessionmc2/sessionmc2-04-big-o-intuition.png)

### Full Code: Count Steps in Linear vs Binary Search

This program searches for the same target with two strategies and prints the step count. Binary search is used only because the list is sorted.

```python
# Create a sorted list of roll numbers so binary search is allowed
rolls = [101, 104, 109, 112, 118, 121, 125, 130]
# Choose the roll number we want to find
target = 125

# Start a step counter for linear search
linear_steps = 0
# Remember the index if linear search finds the target
linear_index = -1
# Check items from left to right
for i in range(len(rolls)):
    # Count one comparison against the target
    linear_steps = linear_steps + 1
    # If this position holds the target, record the index and stop
    if rolls[i] == target:
        # Store the found position
        linear_index = i
        # Leave the loop because the search is over
        break

# Start a step counter for binary search
binary_steps = 0
# Left boundary is the first index
left = 0
# Right boundary is the last index
right = len(rolls) - 1
# Remember the index if binary search finds the target
binary_index = -1
# Repeat while the search window still has items
while left <= right:
    # Count one middle-item comparison
    binary_steps = binary_steps + 1
    # Find the middle index of the current window
    mid = (left + right) // 2
    # If the middle item is the target, record it and stop
    if rolls[mid] == target:
        # Store the found position
        binary_index = mid
        # Leave the loop because the search is over
        break
    # If the middle item is smaller than the target, search the right half
    elif rolls[mid] < target:
        # Move the left boundary just after mid
        left = mid + 1
    # Otherwise the middle item is larger, so search the left half
    else:
        # Move the right boundary just before mid
        right = mid - 1

# Print linear search result and how many steps it took
print("Linear search index:", linear_index, "steps:", linear_steps)
# Print binary search result and how many steps it took
print("Binary search index:", binary_index, "steps:", binary_steps)
```

**How the code works**

- Linear search may stop early if the target is near the front. In the worst case it checks every item — **O(n)**.
- Binary search halves the window each time, but **only because the list is sorted**. Extra space is **O(1)** for both methods here.
- The step gap looks small on 8 items and becomes huge when n is large. Same problem, two growth labels — now you can choose.

### Activity: Match the Label

For each situation, pick **O(1)**, **O(log n)**, **O(n)**, or **O(n²)**.

| Situation | Your Big-O guess |
|---|---|
| Reading the first item of a list by index. | |
| Checking every product price once to find the minimum. | |
| Comparing every student with every other student to find duplicate marks the slow way. | |
| Finding a word in a dictionary by repeatedly opening the middle of a sorted page range. | |

Answers: O(1), O(n), O(n²), O(log n).

---

## Compare Searching Strategies Before You Choose

You now have Big-O as a comparison tool. Let us apply it to searching — a task you have already practised with lists.

### Linear Search: The Honest Full Scan

- **Official Definition:** **Linear search** checks items one by one from the start of a collection until the target is found or the collection ends.
- **In Simple Words:** Start at the first desk in a classroom and ask each student "Are you roll 125?" until you find them or you run out of desks.
- **Real-Life Example:** Finding a guest in an unmarked wedding hall. There is no seating chart. You walk row by row.

Linear search is a good choice when the list is **unsorted**, **small**, or you will search **only once** (or a few times). It hurts when you search again and again on a huge unsorted list, because each search restarts from zero.

### Binary Search: Fast, With a Ticket Price

- **Official Definition:** **Binary search** finds a target in a **sorted** collection by repeatedly comparing the middle element and discarding half of the remaining range.
- **In Simple Words:** Open a sorted telephone directory in the middle. If the name you want comes after that page, throw away the left half. Repeat.
- **Real-Life Example:** Finding a word in an English dictionary. You would never start at page 1 for every word.

The ticket price is **sorted data**. If the list is unsorted, binary search is not "a bit wrong." It is the wrong tool.

### The Hidden Cost: Sort Then Search vs Just Scan

Suppose you have an unsorted list and you need **one** lookup.

- Linear search: about **O(n)**.
- Sort first (good sort is about **O(n log n)**), then binary search **O(log n)**. Total is dominated by sorting: **O(n log n)**.

For **one** search, sorting first is usually extra work. Linear search wins.

Now suppose you will look up 10,000 different roll numbers in the same list.

- 10,000 linear searches: about **10,000 × n** checks.
- Sort once **O(n log n)**, then 10,000 binary searches: about **10,000 × log n** extra checks.

The second plan wins because you **paid the sorting cost once** and reused the sorted order many times.

This is why "binary search is faster" is incomplete. The professional question is: **How many times will I search? Is the data already sorted? Can I afford to sort?**

### Activity: Choose the Search Plan

For each case, write **linear**, **binary**, or **sort once then binary**.

1. A list of 12 lab partners, unsorted. Find one name.
2. A sorted college merit list of 8,000 names. Find one name.
3. An unsorted dump of 50,000 order IDs. You must answer 20,000 "does this ID exist?" questions.

Suggested answers: (1) linear, (2) binary, (3) sort once then binary.

---

## Compare Sorting Strategies Before You Choose

Searching often depends on order. Sorting is the other everyday decision, and the same rule applies: **do not pick the first sort you remember. Compare.**

### What "Better Sort" Means

- **Official Definition:** A **sorting algorithm** arranges items into a defined order (for example, ascending marks or alphabetical names) using comparisons and moves.
- **In Simple Words:** Sorting is putting things in line — prices low to high, ranks high to low, names A to Z.
- **Real-Life Example:** Arranging answer scripts by roll number before data entry. The office can use a slow pile-by-pile method or a faster systematic method. Both produce a sorted pile. They do not cost the same time.

You have already seen elementary sorts such as **Bubble Sort** and **Selection Sort**. Both typically take **O(n²)** time. They are excellent for learning, because you can trace every swap. They are rarely the best choice for large data.

Python's built-in **`sorted()`** and **`list.sort()`** use a highly tuned method (Timsort) that is about **O(n log n)** in typical cases, and they are implemented in fast underlying code. For real programs, that is usually the default professional choice.

### A Comparison Checklist (Use This Before Coding)

Ask these questions *before* you write a sort:

- **How large is n?** For 8 items, almost any correct sort is fine. For 8 lakh items, O(n²) can become painful.
- **Do I need a new list or can I sort in place?** `sorted(list)` builds a new list (extra memory). `list.sort()` changes the same list.
- **Is this for learning or for a live app?** Tracing Bubble Sort teaches swaps. Shipping it in a result portal is usually the wrong strategy.
- **Will I sort once or many times?** Sorting on every keystroke is different from sorting once when the file is loaded.

| Strategy | Typical time | Extra space (simple view) | Best used when |
|---|---|---|---|
| Bubble / Selection style nested sort | O(n²) | O(1) extra | Learning, tiny lists, tracing |
| Python `list.sort()` | about O(n log n) | sorts in place | You own the list and can change it |
| Python `sorted()` | about O(n log n) | new list, extra O(n) | You must keep the original order too |
| Sort once, then many binary searches | O(n log n) setup, then cheap lookups | depends on the sort | Many searches on the same data |

### Common Doubt: "Then Why Did I Learn Slow Sorts?"

Because a built-in function is a black box unless you understand what "sort" is doing. You already know the danger of treating the machine as a black box, and the same idea applies to algorithms. Learning a slow, traceable sort trains your eye for nested loops, swaps, and O(n²) growth.

You do not throw away elementary sorts. You put them in the right drawer: **teaching tools and tiny cases**, not default tools for huge data.

![Comparing search and sort strategies — unmarked wedding hall row-by-row search versus a sorted directory opened in the middle, plus a small classroom pile sort versus a huge result-portal sort choosing a faster built-in method](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitreict-se-2606/masterclasses/sessionmc2/sessionmc2-05-search-sort-compare.png)

### Activity: Pick a Strategy, Then Defend It

For each scenario, write the strategy and one reason.

1. Sort 6 grocery prices for a class demo, and explain each swap to yourself.
2. Sort 2 lakh product prices on a shopping website, then show "low to high."
3. Keep the original unsorted list of applicants, but also display a sorted-by-marks copy.
4. Unsorted log of 1 lakh ticket PNR numbers; operators will search thousands of PNRs during the day.

Suggested direction: (1) elementary sort for learning, (2) in-place built-in sort, (3) `sorted()` so the original remains, (4) sort once, then binary search.

---

## Choose Before You Code

Algorithm choice is a habit. State the problem, reject pure ad-hoc steps, estimate **n**, name two strategies, compare them with Big-O and extra space, and only then write code. If you skip to coding, you often lock yourself into the first idea that runs on 10 rows.

### Activity: One Problem, Two Plans

A list of student names. You must answer whether a name exists.

Write **Plan A** for 10 unsorted names, searched once. Write **Plan B** for 1,00,000 unsorted names, searched 5,000 times. For each plan, mention time complexity in Big-O and whether you sort first.

---

## Key Takeaways

- An **algorithm** is a finite, repeatable recipe. Ad-hoc guessing can "work" once, but it cannot be tested, shared, or compared as data grows.
- An inefficient method often looks fine on small **n** because computers are fast. The demerit appears when input grows: nested work can explode toward **n × n**, while a one-pass plan grows far more gently.
- **Time complexity** describes how work grows. **Space complexity** describes how extra memory grows. Faster plans sometimes spend RAM to save time — that trade-off is a design choice, not an accident.
- **Big-O** is a growth label for comparing two approaches to the *same* problem. O(1), O(log n), O(n), O(n²), and O(n log n) are the families you will use most.
- **Search** and **sort** are not one-size tools. Linear search, binary search, elementary sorts, and built-in sorts each win in different situations. Compare strategies — including "how many times will I search?" — before you choose.

This way of thinking continues into later programming work. Whenever you write a loop inside a loop, store an extra copy of data, or pick a search method, you are making a complexity decision. The machine you studied earlier has limits, and algorithms decide how hard you push those limits.

---

## Important Commands, Libraries, and Terminologies

| Term | What It Means | Analogy |
|---|---|---|
| **Ad-hoc approach** | Improvised one-off steps, not a reusable method | Random turns in a new city |
| **Algorithm** | Finite, ordered steps from input to correct output | Chai recipe |
| **Input size (n)** | How much data the algorithm must process | 12 students vs 40,000 students |
| **Time complexity** | How work (operations) grows as n grows | Extra customers vs recounting the whole shop |
| **Space complexity** | How extra memory grows as n grows | Sorting in one queue vs photocopying the register |
| **Extra space** | Memory beyond the original input | A second notebook |
| **Time–space trade-off** | Using more memory to reduce work, or the reverse | Tiny bag vs packing every backup outfit |
| **Big-O notation** | Label for the growth shape, not exact seconds | Highway vs visiting every gali |
| **O(1)** | Work stays roughly constant as n grows | Picking the top labelled book |
| **O(log n)** | Work grows slowly; doubling n adds few steps | Opening a dictionary in the middle |
| **O(n)** | Work grows in a straight line with n | Checking every row once |
| **O(n log n)** | More than one pass, much less than n × n | A good general-purpose sort |
| **O(n²)** | Work grows like n times n | Every student compared with every other |
| **Linear search** | Scan items one by one; O(n) | Walking an unmarked wedding hall |
| **Binary search** | Halve a **sorted** range each time; O(log n) | Dictionary lookup |
| **Sorting algorithm** | Arrange items into order | Arranging scripts by roll number |
| **`sorted()`** | Returns a new sorted list | Photocopy, then arrange the copy |
| **`list.sort()`** | Sorts the same list in place | Rearranging people in the same queue |
| **`set`** | Collection for fast "have I seen this?" checks | Attendance notebook of unique rolls |
| **Worst case** | The most work the method might need for size n | Target is last, or not present at all |
