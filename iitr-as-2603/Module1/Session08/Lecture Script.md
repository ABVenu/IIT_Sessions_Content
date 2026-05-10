# Lecture Script: Pandas — Indexing & Filtering

**Session Duration:** 2 hours 15 minutes  
**Audience:** Beginners (Indian students); minimal prior programming assumed; comfort with basic Python lists helps.

---

## How to use this document

This file is for **timing and facilitation only**. It is not a substitute for the Lecture Notes. Use it to manage pacing, screen-sharing, room circulation, and quick engagement checks. Keep the Lecture Notes open for definitions, code, and analogies.

---

## Break rule

After **60–75 minutes** of instruction and live coding, take **one** pause of **5–8 minutes**. Do not schedule the break as a numbered teaching block; resume with the next block’s bridge sentence.

---

## 1. Opening — Why Pandas, install, and import (8 minutes)

- **Screen-share:** Session objective (from metadata): load tabular data, understand structure, select rows/columns with `loc`/`iloc`, filter, sort, handle missing values.
- **Say in one line:** Pandas bridges lists and spreadsheets — you load, clean, and analyze **tables** in Python with structure and speed (NumPy under the hood).
- **Live-demo (terminal or notebook):** `pip install pandas` once per environment; then `import pandas as pd`.
- **Students do:** Run the import; confirm no `ModuleNotFoundError`. Circulate for environment issues (venv, Jupyter kernel).
- **Check:** **Thumbs up** — “Does `import pandas as pd` run clean?”
- **Cold-call:** One student — “What will you use `pd` for in today’s session?” (tie to notes: read files, select rows/columns, missing values.)

**Bridge sentence:** “Before we load anything, we need to agree on what a CSV file actually is — because `read_csv` is just parsing text into a table.”

---

## 2. What is CSV? — format, why it matters, create a tiny file (12 minutes)

- **Screen-share:** CSV = comma-separated values; one line ≈ one row; commas separate columns; first line often = headers; quoted fields when text has commas; TSV/tabs and pipes as alternatives (`sep=` later).
- **Why CSV:** portable, lightweight, universal exports, **text diffs in Git** vs binary `.xlsx` — one sentence each from the notes.
- **Live-code:** Build `csv_text` for `people.csv` exactly as in the notes; `open(..., "w", encoding="utf-8")` and write; open the file in a text editor or `print` contents so students *see* raw text.
- **Students do:** Create the same small file in their folder; verify it on disk.
- **Pair-share (2 min):** “What would change if a city name contained a comma?” (lead to quotes in CSV — conceptual.)

**Bridge sentence:** “We have honest text on disk; now we hand that file to Pandas and turn it into a DataFrame.”

---

## 3. `pd.read_csv()` + DataFrame structure (15 minutes)

- **Screen-share:** `read_csv` **parses** text into a DataFrame — headers, rows, inferred dtypes.
- **Analogy (30 seconds):** Universal translator — `sep`, `header`, `names`, `index_col`.
- **Live-code:** `df = pd.read_csv('people.csv')` (their file from block 2); standard load; then intermediate example (`sep='|'`, `header=None`, `names=[...]`); advanced `index_col='EmployeeID'` if using a sample `employees.csv` you provide.
- **Structure (city map):** `.index`, `.columns`, `.values`, `.shape`, `.dtypes` — quick inspection prints from notes.
- **Under the hood:** C-engine — one sentence.
- **Pitfalls:** `encoding='cp1252'`; wrong `sep` → parser errors — show **diagnosis** (peek at file, try `\t` or `|`).
- **Students do:** Load `people.csv`; print `shape` and `columns`; optionally load your second file with `index_col`.
- **Check:** **Thumbs up** — “Does your column count match the header row?”

**Bridge sentence:** “We trust structure only after we’ve *looked* at real rows — that’s exploratory inspection.”

---

## 4. Inspect data quickly — EDA first step (12 minutes)

- **Screen-share:** `head()`, `tail(10)`, `sample(5, random_state=42)` — why random rows matter (edges can mislead).
- **Live-code:** `.shape` in an f-string; `df.info()` — non-null counts vs dtypes; optional `memory_usage='deep'`.
- **Students do:** On their `df`, run `head`, `tail`, `sample`, `info`; name one column that might have missing values from non-null counts.
- **Cold-call:** “Why use `random_state=42` on `sample`?”

**Bridge sentence:** “Inspection tells us what’s there; next we choose *which columns* we work with.”

---

## 5. Selecting columns — Series vs DataFrame (8 minutes)

- **Screen-share:** `df['Col']` → Series; `df[['Col']]` → DataFrame; dot shorthand + limits.
- **Live-code:** Sample employee `DataFrame` from notes — mean of `Age`; subset `Name` + `Email`.
- **Pitfalls:** Dot vs methods, spaces in names, assignment only `df['NewCol'] = ...`.
- **Students do:** One statistic on a column; a two-column sub-table.
- **Pair-share (90 sec):** “When is double bracket *required*?”

**Bridge sentence:** “Columns are names; rows can be labels too — that’s `loc`.”

---

## 6. Selecting rows with `loc` — labels & inclusive slices (12 minutes)

- **Screen-share:** DataFrame with `EMP_001`… index; `df.loc[row]`, `df.loc[[rows]]`, slice with column list — stress **inclusive** slice.
- **Pitfalls:** `KeyError`, type mismatch; unsorted index + slice → `sort_index()`.
- **Students do:** One row, two rows, one slice; neighbor check — is the end label **in** the slice?
- **Check:** **Thumbs up** — “Inclusive for `loc` — yes or no?”

**Bridge sentence:** “Labels are human-friendly; integer **position** is `iloc`.”

---

## 7. Selecting rows with `iloc` & compare to `loc` (12 minutes)

- **Screen-share:** `iloc[0]`, `iloc[-1]`, `iloc[0:5]` (**exclusive** stop), `iloc[::10]`, 2D `iloc[0:3, 0:2]`.
- **Contrast table:** **loc vs iloc** on screen — 2 minutes max.
- **Pitfalls:** Integer index → use `iloc` for position.
- **Students do:** Same rows via `loc` and `iloc` where possible; compare.
- **Cold-call:** “`iloc[0:3]` — how many rows?”

**Bridge sentence:** “Sometimes we promote a column to the index or flatten it back — `set_index` and `reset_index`.”

---

## 8. `set_index` & `reset_index` (10 minutes)

- **Screen-share:** `set_index('Employee_ID')` — column leaves `columns`; `loc` on IDs; `reset_index()` vs `reset_index(drop=True)`.
- **Students do:** Promote an ID, query with `loc`, then `reset_index(drop=True)` on a filtered subset.
- **Check:** **Thumbs up** — “After `set_index`, is that ID still a normal column?”

**Bridge sentence:** “Indexes organize rows; filtering uses Boolean logic — the bouncer at the door.”

---

## 9. Boolean filtering — masks & one-liners (10 minutes)

- **Screen-share:** `mask = df['Score'] > 90`; `df[mask]`; one-liner; strings; `df[df['Col'].isna()]` for missing.
- **Under the hood (optional):** Bitmaps — one line.
- **Students do:** One numeric and one string filter.
- **Cold-call:** “Empty result but you ‘know’ the city exists — what do you check?” (case, whitespace.)

**Bridge sentence:** “One condition is easy; business questions combine conditions with care.”

---

## 10. Multiple conditions — `&`, `|`, `~`, `isin` (8 minutes)

- **Screen-share:** `(A) & (B)`, `(A) | (B)`, `~`; never `and`/`or` on Series; `isin([...])`.
- **Note:** Pandas does not short-circuit — brief mention if time.
- **Students do:** English rule → code; report row count.
- **Check:** **Thumbs up** — “Parentheses around *each* condition?”

**Bridge sentence:** “We can subset a cohort; next we *order* it for ranking and reporting.”

---

## 11. Sorting with `sort_values` (8 minutes)

- **Screen-share:** Single column descending; multi-column `ascending=[True, False]`; `na_position`; **re-assign**; `reset_index(drop=True)` after sort if needed.
- **Pitfalls:** Forgetting assignment; numeric strings sorted as text.
- **Students do:** Sort by one column, then by two with different directions.

**Bridge sentence:** “Sorted tables still have gaps — we detect, fill, or drop missing values.”

---

## 12. Missing data — `isna` / `notna`, `fillna`, `dropna` (15 minutes)

- **Part A — Detect (5 min):** `isna()`, `notna()`, `isna().sum()`; never `x == np.nan`; string `"NaN"` vs real `NaN`.
- **Part B — Fill (5 min):** constant, `ffill()`/`bfill()`, mean for numeric; salary ≠ 0 default; `"Unknown"` for strings.
- **Part C — Drop (5 min):** `dropna`, `subset`, `thresh`, `axis`; `shape` before/after; `reset_index(drop=True)`.
- **Students do:** On messy sample data: count nulls, fill one column sensibly, drop using `subset` on a critical column.
- **Pair-share (2 min):** “Drop vs fill — when is each ethical for analysis?”

**Bridge sentence:** “That closes the loop: from text file to loaded, inspected, selected, filtered, sorted, cleaned tables.”

---

## 13. Consolidation & exit (5 minutes)

- **Screen-share:** One-slide recap: **install / CSV text → `read_csv` → structure + `info` → `[]` vs `[[]]` → `loc` / `iloc` → `set_index` / `reset_index` → Boolean + `&` / `|` → `sort_values` → `isna` / `fillna` / `dropna`.
- **Students do:** Write one command they will reuse this week.
- **Q&A:** 2–3 minutes; point to Lecture Notes for CSV layout and pitfall lists.

**Bridge sentence (into next session / async work):** “Keep today’s notebook — the next session builds on the same load–inspect–transform habits.”

---

## Timing flex — if you are running late

- **Cut first:** Shorten CSV “why Git vs xlsx” and all “under the hood” asides to one line; demo file creation **or** student file creation, not both.
- **Merge:** Blocks 5–6 (columns + `loc`) if brackets are easy; or blocks 9–10 (single + multiple filters) with one combined demo.
- **Demo-only:** Block 12 — live-demo detect/fill/drop once; assign three small exercises as homework with solutions in LMS.
- **Minimum viable:** `import` + **what a CSV is** (30 seconds) + `read_csv` + `info`/`head`; column vs DataFrame selection; **`loc` and `iloc`** with inclusive vs exclusive; one Boolean filter with `&` and parentheses; **`isna().sum()`** at minimum.
- **If ahead of schedule:** 10 minutes **live debugging** — wrong `sep` or encoding; students propose fixes from notes; optional: show `read_csv` on a **URL** if your policy allows.
