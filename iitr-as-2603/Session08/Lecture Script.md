# Lecture Script: Pandas — Indexing & Filtering (Session 08 bundle)

**Duration:** 2 hours 15 minutes (135 minutes)  
**Audience:** Beginners comfortable with basic Python; Indian students / mixed cohorts.

Have **`Lecture Notes.md`** (this bundle) open for code to copy, **figures** to project, and the **Quick Reference** at the end.

---

## 1. Welcome and roadmap (5 minutes)

- Greet; confirm **Python 3**, **Jupyter / Colab / VS Code notebook**, and `import pandas as pd` works (or allow 2 minutes to `pip install pandas`).
- One-sentence hook from the notes: lists are too plain, Excel is too manual — **Pandas** gives labelled, fast tables.
- Roadmap: **Series** → **indexing & vectorization** → **DataFrame** building → **select / `loc` / `iloc`** → **mutate & filter** → **group & sort** → **missing data**; skip reading “Under the Hood” aloud unless someone asks.

**Bridge sentence:** *“We start with one column — the Series — before we glue columns into a DataFrame.”*

---

## 2. Series: why, anatomy, creating (12 minutes)

- Notes § *Install Pandas and Create Series*: **Why Pandas?** + **Locker room** analogy — under 90 seconds.
- Project **Figure** (Series anatomy) from the notes; learners match **index / values / dtype** on screen.
- Live: `pd.Series` from a **list**, then **custom index** (monthly sales), then **scalar broadcast** — follow the first code cells; **circulate** for import errors.
- One pitfall line: mixed types → `object` dtype.

**Bridge sentence:** *“Real data arrives as dicts and APIs — the Series constructor has to eat those too.”*

---

## 3. Series from dict, scalar, index override (10 minutes)

- Notes § *Create Series from Different Data Structures*: **Cookie cutter** + **chocolate box** analogies — quick.
- Project figure *Series from structures*; run **dict → Series**, **scalar + index**, **dict + index** (SF → **NaN**) — emphasize **silent NaN** from the notes.
- **Thumbs:** “If a label is in `index` but not in the dict, what appears?” (NaN)
- Mention **zero-copy / broadcasting** in one sentence only.

**Bridge sentence:** *“Once data is in a Series, we need precise ways to read rows — by label or by position.”*

---

## 4. Access by index, `loc`, `iloc`, vectorization (14 minutes)

- Notes § *Access Series Elements by Index*: **Library** analogy; show **Series access** figure.
- Contrast **`[]`**, **`.loc`**, **`.iloc`**, **`.get`** with the stock example; **integer index trap** on board — cold-call: position 0 vs label `10`.
- Notes § *Perform Vectorized Operations*: **Payroll** analogy + vectorization figure; one demo: math on Series + **index alignment** (mention NaN when labels don’t match).
- **Pair-share (60 sec):** when would you use `iloc` vs `loc`?

**Bridge sentence:** *“One Series is a column; a DataFrame is many columns sharing one index.”*

---

## 5. DataFrame: dict, lists, arrays, CSV, structure (16 minutes)

- Notes § *Create DataFrame from Dictionary* through *Understand DataFrame Structure*: **Spreadsheet** analogy + DataFrame anatomy figure.
- Run **dict of lists**, **list of dicts**, then **list of lists / array** with explicit `columns` — notes examples.
- **`read_csv`** demo: default headers vs `sep` / `header=None` / `index_col` — use paths your cohort can reach or a tiny inline CSV string.
- **`df.shape`**, **`df.info()`**, **`values` vs losing names** — 3 minutes max.
- **Circulate** during CSV read.

**→ Break (8 minutes).** Announce return time.

**Bridge sentence:** *“When we’re back, we slice tables like a jukebox — pick songs (columns), then rows by name or seat number.”*

---

## 6. Selecting columns; `loc` on DataFrame (13 minutes)

- Notes § *Select Columns from DataFrame*: **Jukebox** analogy; **sample `df`** from notes (Name, Age, Department, Salary, Email).
- **`df['Age']`** vs **`df[['Age']]`** — type difference; **dot notation** caveat.
- Notes § *Select Rows using `loc`*: employee ID examples — single label, slice (inclusive), row + column subset.
- Project **select columns** figure if bandwidth allows.

**Bridge sentence:** *“Labels use `loc`; integer seats use `iloc` — we’ll compare them on one slide.”*

---

## 7. `iloc`, `loc` vs `iloc` comparison (12 minutes)

- Notes § *Select Rows using `iloc`*: slices, negatives, **`::10`**, block of **first 3 rows × 2 cols**.
- Show **comparison table** from the notes (**label vs position**, inclusive vs exclusive).
- **Cold-call:** “First two rows by position — `iloc` slice?” (`0:2`)

**Bridge sentence:** *“Selection is read-only; next we add columns and filter rows with Boolean logic.”*

---

## 8. New columns, Boolean filters, drop (13 minutes)

- Notes § *Add New Columns*: constant column, arithmetic, Boolean flag, **`df.copy()`** before mutate.
- Notes § *Filter with Multiple Conditions*: **`&` / `|`**, parentheses, **`query`** optional if in notes.
- Notes § *Delete Columns and Rows*: **`drop`**, **`axis`**, **`inplace`** vs copy; mention **`del`** briefly.
- **Circulate** on a two-condition filter bug (missing parentheses).

**Bridge sentence:** *“Renaming and grouping turn messy exports into report-ready tables.”*

---

## 9. Rename columns; `groupby` (11 minutes)

- Notes § *Rename Columns and Index*: **`rename`**, **`columns=`** dict, danger of assigning full list.
- Notes § *Group Data with groupby*: **Laundry** analogy; **`groupby` → aggregate** — show **lazy** idea: chain `.sum()` / `.mean()` / multiple columns.
- One **groupby** example live; avoid deep **transform** unless time.

**Bridge sentence:** *“Grouping answers ‘by category’; sorting answers ‘who is first in line?’”*

---

## 10. Sort by values; sort by index (9 minutes)

- Notes § *Sort DataFrame by Values*: **`sort_values`**, **`ascending`**, multiple keys, **`na_position`**.
- Notes § *Sort DataFrame by Index*: **`sort_index`**, **`axis=1`** for column order.
- Quick demo each; no long **Timsort** theory — one sentence from “Under the Hood” if asked.

**Bridge sentence:** *“Sorted tables still have holes — missing data is the last boss fight.”*

---

## 11. Missing data: detect, fill, drop + close (9 minutes)

- Notes § *isna / notna*: masks, **`isnull().sum()`**, **`info`**.
- Notes § *fillna*: constant, **`ffill`**, deprecations note if present.
- Notes § *dropna*: **`how`**, **`subset`**, dropping sparse columns.
- **Exit ticket (chat or paper):** one case where you’d **`fillna`** vs **`dropna`**.
- Point to **Quick Reference** in notes; homework: rerun key cells on the **sample `df`**; next-session pointer per your syllabus.

---


