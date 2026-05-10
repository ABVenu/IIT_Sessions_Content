# Lecture Script: Data Prep — Handling Messy Data

**Session Duration:** 2 Hours 15 Minutes  
**Audience:** Absolute beginners (Indian students, little or no prior tech background)

---

## How to use this document

This file is for **timing and facilitation only**. It is not a substitute for the lecture notes. Keep the detailed explanations, definitions, and code snippets in *Lecture Notes.md*; use this script to run the room, share screens, and check that learners are following on their machines.

---

## Break rule

After roughly **60–75 minutes** of session time, take **one** break of **5–8 minutes**. Do **not** treat the break as a numbered teaching block—announce it, pause the recording if applicable, and resume with the bridge into the next block.

---

## 1. Opening, recap, and why data prep matters (12 minutes)

**Facilitator**

- Welcome the group; confirm everyone can open Google Colab (or your chosen environment) and has a stable connection.
- **Cold-call** one or two students: “In one sentence, what is the difference between a **feature** and a **label**?” Praise partial answers; correct gently using last session’s language.
- Project the cooking analogy from the notes: prep before cooking → data prep before modelling. State plainly: **most practitioners spend a large share of time cleaning data**, not only tuning models.
- Show the session roadmap on screen (bullets from the notes: inspect, missing data, duplicates/consistency, encoding, scaling, leakage, measuring impact).

**Students**

- Mentally connect today’s topics to train/validation/test and baselines from the previous session.

**Engagement**

- **Thumbs up:** “Thumbs up if you’ve ever seen a spreadsheet with blank cells or the same row twice.”

**Bridge sentence:** “Now we open a real table in Python and learn to *see* what’s wrong before we touch anything.”

---

## 2. Load the dataset and inspect like a doctor’s check-up (15 minutes)

**Facilitator**

- **Screen-share** a Colab notebook. Live-code: `import pandas as pd`, `pd.read_csv(...)`, `df.head()`.
- Narrate each line in plain language (`read_csv` = spreadsheet in memory; `head` = quick peek).
- Run `df.shape`, `df.info()`, `df.describe()`. Pause after each output.
- **Circulate** (or ask in chat): “Does anyone’s `info()` show a column that should be numbers but says `object`?”
- Optionally flash the inspection diagram from the notes (missing cells, types, outliers, duplicates).

**Students**

- Run the same three inspection commands on your copy of the notebook (or provided starter file).

**Engagement**

- **Pair-share (2 minutes):** Partner A reads `shape` aloud; Partner B says one thing they would *look for next* in `info()` or `describe()`.

**Bridge sentence:** “Once we’ve listed what’s broken, we fix the easiest big problem first: **missing values**.”

---

## 3. Missing data — detect and impute (18 minutes)

**Facilitator**

- Define **missing data** in everyday terms (blank form field; attendance register).
- Live-code: `df.isnull().sum()` and percentage with `df.isnull().mean() * 100`.
- Display the **mean / median / mode** table from the notes. **Cold-call:** “Salary with crazy outliers — median or mean?” “City column — what do we use?”
- Live-code median fill for `Age`, mean for `Salary`, mode for `City`; end with `df.isnull().sum()` to verify.
- Address the common doubt: delete vs impute — emphasize **small data** and **keeping rows** when sensible.

**Students**

- Run detection cells, then imputation cells; confirm missing counts drop to zero for the practiced columns.

**Engagement**

- **Thumbs up:** “Thumbs up if seeing `NaN` in your own project would make you nervous — that’s normal.”

**Bridge sentence:** “Missing values are only one kind of mess; next we remove **double copies** and fix values that don’t make sense.”

---

## 4. Duplicates, outliers, and text consistency (14 minutes)

**Facilitator**

- Story: duplicate customer feedback → inflated counts. Live-code `df.duplicated().sum()` and `drop_duplicates()`.
- Define **outliers** with a relatable money/age example; show `describe()` then filter with `between` and non-negative salary.
- Live-code `.str.lower().str.strip()` on `Gender` (or a sample column).
- **Check screens:** quick walk—two volunteers share whether duplicate count went to zero.

**Students**

- Execute duplicate check/removal and at least one filter + one text-standardisation cell.

**Bridge sentence:** “The table is cleaner, but models still can’t multiply words — we turn **categories into numbers**.”

---

## 5. Categorical data, label encoding, and one-hot encoding (18 minutes)

**Facilitator**

- Define **categorical** data with payment-method examples. Stress: **models need numbers**.
- Live-code `select_dtypes(include='object')` and `value_counts()` for one column.
- **Label encoding:** ordered example (**Low / Medium / High**). `LabelEncoder`, `fit_transform`, new column `Education_encoded`.
- **One-hot encoding:** unordered cities. `pd.get_dummies(..., drop_first=True)` — briefly name **multicollinearity** without a statistics lecture; “we drop one column on purpose.”
- Side-by-side **which encoding when** from the notes.

**Students**

- Run encoding cells; inspect `head()` to see new columns.

**Engagement**

- **Pair-share:** “Name one column in a real business that should be label-encoded vs one-hot-encoded.”

**Bridge sentence:** “Even after encoding, **big numbers can bully small numbers** — so we **scale**.”

---

## 6. Feature scaling — normalisation vs standardisation (14 minutes)

**Facilitator**

- Use the Age vs Salary contrast: different **magnitudes** can skew learning. Define **feature scaling** in one line.
- Live-code `MinMaxScaler` on two numeric columns; show `describe()` min/max near 0–1.
- Live-code `StandardScaler`; point at mean ≈ 0, std ≈ 1 in output. Use the comparison table (when to use which).
- Warn: in a full pipeline, scaling order matters—we set up the next block.

**Students**

- Run both scalers on the same practice columns (separate cells or copies) and compare outputs.

**Bridge sentence:** “Here’s the rule that separates beginners from careful practitioners: **split first, then fit only on train**.”

---

## 7. Data leakage — split, fit, transform (16 minutes)

**Facilitator**

- Analogy: seeing the exam paper early. Define **leakage** with the “mean salary from whole dataset” example.
- Live-code `train_test_split` **before** scaling.
- Emphasize: `fit_transform(X_train)` vs **`transform(X_test)` only** — never `fit` again on test.
- **Cold-call:** “What goes wrong if we `fit` the scaler on the full dataset including test?”

**Students**

- Run split + scaler pattern exactly as in the notes; verify shapes of `X_train_scaled` and `X_test_scaled`.

**Engagement**

- **Thumbs up:** “Thumbs up if ‘fit on train, transform on test’ is a phrase you’ll write on a sticky note.”

**Bridge sentence:** “We end by proving the cleanup **moved the needle** — shape, missing counts, and sanity stats.”

---

## 8. Measure impact, recap, and close (18 minutes)

**Facilitator**

- Walk through “before/after”: row counts, `isnull().sum().sum()`, `describe()`.
- Rapid-fire **key takeaways** from the notes (messy is normal; impute smartly; encoding choice; scaling; split-before-fit).
- Point learners to the **Important Commands** table for revision.
- Preview: next sessions move from clean tables to **training models**.

**Students**

- Skim the glossary table and star two commands they’ll use in this week’s practice.

**Engagement**

- Final **cold-call:** “Name one mistake that causes **data leakage** in preprocessing.”

**Bridge sentence:** “Carry today’s pipeline mindset forward: **see the data, fix it honestly, and evaluate without cheating**.”

---

## Timing flex — if you are running late

- **Cut first (save demos):** Shorten pair-shares from 2 minutes to 1; trim extended Q&A in blocks 2 and 4; show scaling outputs once (either MinMax **or** StandardScaler live, summarize the other from slides).
- **Cut second:** Combine blocks 5 and 6 slightly: teach one-hot + label encoding with less `value_counts` exploration; assign `describe()` comparisons after class.
- **Never skip:** Block 7 (leakage + `fit`/`transform` on train vs test)—this is safety and credibility for everything that follows.
- **If ahead of schedule:** Add a **mini-poll** (hands or chat): “Which imputation for `Age` if histogram is skewed?” Add 5 minutes for learners to write **three bullet notes** on what they will do before training any model on a new CSV.
