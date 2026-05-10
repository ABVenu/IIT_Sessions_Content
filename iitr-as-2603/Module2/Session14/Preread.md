# Pre-read: Data Prep — Handling Messy Data

Picture a bank branch that receives loan applications on paper and online. Some forms skip the income box. Two customers submit almost the same details twice. One clerk writes **Male**, another writes **male** with a space. A salary shows up as **minus five thousand** because of a typo. If someone tried to decide “approve or reject” using this pile as-is, honest applicants might get rejected and risky ones might slip through—not because the rules were wrong, but because **the inputs were messy**.

Now imagine that instead of dozens of forms, you have **thousands of rows** in a digital sheet: customer ages, cities, salaries, and “yes/no” outcomes. You want a computer to learn patterns from past cases so it can help score new applications. What if half the cells are blank? What if cities are spelled ten different ways? What if one salary column has numbers in lakhs and another looks fine until you notice a single entry big enough to buy a cricket team? Doing this cleanup **by hand for every row** is slow, tiring, and easy to get wrong. People who work with machine learning spend much of their project time here—not because they dislike models, but because **clean data is what makes learning trustworthy**.

This session is about that invisible but crucial work: **data preparation**—opening a dataset, spotting what is broken, fixing it in a repeatable way, and checking that your fixes actually helped. We use familiar tools (spreadsheet-style tables in Python, smart fill-ins for gaps, rules for duplicates and impossible values, turning category labels into numbers, and putting numbers on a fair scale) so the **computer can focus on real patterns**, not on garbage or accidental shortcuts.

---

Think of it like **cooking at home**. Before you stir-fry or simmer a curry, you wash vegetables, throw away what is rotten, chop evenly, and measure spices. Skip that step and even the best recipe gives you a disappointing plate. In the same way, **messy figures and labels in your training material often lead to weak or misleading predictions**, no matter how advanced the method sounds. Data prep is not a side chore—it is the foundation.

---

**In this pre-read, you'll discover:**

- **Why** teams guard their time for inspection and cleanup before trusting any automated learner.
- **How** missing answers can be handled fairly—using typical values for numbers and common labels for text—without throwing away half your rows when you do not have to.
- **Why** turning words like city names into numbers needs care (ordered grades versus plain categories), and why huge columns should not shout louder than small ones just because their digits are bigger.
- **How** to keep evaluations honest by avoiding **data leakage**—a fancy name for letting “exam answers” sneak into “study notes” before the test.

When people say they load data into a **DataFrame**, think of a **smart Excel sheet inside code**: rows are records, columns are fields, and you can ask for summaries and counts of blanks in seconds. **Encoding** simply means **giving the model number-friendly versions of text categories**—sometimes one number per label when order matters (low / medium / high), sometimes separate yes/no flags when order does not (city or payment mode). **Scaling** means **putting numeric columns on a comparable footing** so one column’s large range does not drown out another’s signal. **Imputation** is **filling a sensible value where something is missing**, instead of pretending the gap does not exist.

You will also meet ideas like **duplicates** (the same story saved twice), **outliers** (values that look like typos or rare extremes), and **train vs test splits**: we hold some rows aside to check performance, and we must learn our cleanup rules **only from the training portion** so the check stays fair—like measuring revision from old papers, not from tomorrow’s question paper.

---

### Interesting questions we’ll unpack in the live session

1. **If ten percent of salaries are blank**, is it wiser to delete those rows, fill with the average, or use the middle value (**median**) when a few salaries are wildly high—and **why** might your choice change the story?
2. **When a column lists cities with no natural ranking**, why might turning each city into its own **yes/no column** be safer than assigning Delhi = 1, Mumbai = 2 as if cities were marks on a scale?
3. **Why must scaling tools “learn” from training data only**, then apply the same rule to the held-out test rows—what goes wrong if averages from **all** rows sneak into the recipe?

---

### After the session, you’ll be able to

- Open a dataset, scan shape and summaries, and **name the main problems** (missing cells, wrong types, duplicates, odd extremes).
- Choose sensible strategies for **filling gaps**, **dropping or fixing bad rows**, and **making text categories model-ready**.
- Apply **scaling** so columns compete fairly, and describe **why splitting before fitting** keeps your evaluation trustworthy.
- **Compare before and after** cleaning so you can show whether preparation actually improved your starting point.

Bring your curiosity—you do not need to have memorised every command. The live class will connect these ideas to hands-on steps and short exercises so messy tables feel less scary and more like a **kitchen you know how to prep**.
