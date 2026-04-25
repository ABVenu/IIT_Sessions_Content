# Lecture Script: Time Series — Data That Changes Over Time

**Session Duration:** 2 hours 15 minutes  
**Target Audience:** Learners from diverse backgrounds, including those without prior technical training (e.g. Indian students new to data/ML). Delivery should stay concrete, example-led, and jargon-light until terms are defined.

**How to use this document:** This file is for **timing and facilitation only**. It is not a transcript. Use the numbered blocks to pace the room, manage demos, and trigger participation; adapt wording to your style.

**Break rule:** After 60–75 minutes of instruction, take **one** pause of **5–8 minutes** (not a numbered block). Do not add extra formal breaks in the run-of-show.

---

## 1. Welcome, Bridge From Last Session, and Learning Outcomes (10 minutes)

- Welcome the group; briefly restate the arc: last time was **unsupervised learning** (K-Means, PCA) where **row order did not matter**.
- Contrast: today the **order of rows is the story** — one sentence each on **K-Means** vs **“data through time”** to anchor the shift.
- Share the four bullets from “What you will learn”: time-ordered data; trend and seasonality; **no random split**; rolling windows; evaluation.
- **Engagement — cold-call:** “Name one place you’ve seen a graph that goes up and down over months — stock, sales, temperature?” (2–3 quick answers.)
- **Room action:** Glance at chat or raised hands; if teaching hybrid, read one comment aloud.

**Bridge sentence:** “Once we agree that *when* a row happened matters, we’ll lock down what a time series actually is on your screen.”

---

## 2. What Is a Time Series? — Definition, Table, and “Shuffle” Thought Experiment (10 minutes)

- Screen-share the **date + temperature** table; read one row, then the next, to show **strict time order**.
- Walk the **official vs simple** definitions; use the **weather station** example (hourly readings, yearly total).
- Show the **time-order vs shuffle** figure; ask: “If we shuffle, what do we lose?”
- **Pair-share (2 min):** In pairs, one sentence: “What breaks if I shuffle this table?” Pairs report one insight.
- **Room action:** While they pair, walk the perimeter and nudge any quiet tables.

**Bridge sentence:** “Now we’ll name why this feels different from a normal customer or marks table.”

---

## 3. Why Time Series Is Different From “Regular” Data (5 minutes)

- Contrast **independent rows** (student marks) with **each row depending on what came before** (sales, weather, traffic).
- Use two bullets from the notes: yesterday → today, last week → this week.
- **Thumbs up / thumbs down:** “Could you shuffle a class attendance sheet and still predict pass/fail the same way? Thumbs for yes, side for no.” Clarify: attendance rows are closer to *independent* than price series.

**Bridge sentence:** “If dependency over time is the new rule, the first patterns to read on any chart are long-term direction and repeating cycles.”

---

## 4. Trend — Long-Term Direction and the Smartphone Table (14 minutes)

- Display the **trend vs seasonality** figure; say you’ll do **trend** first, then **seasonality** next.
- Define **trend** (official + simple + smartphone / newspaper examples).
- Hit the three key bullets: not every day up, **overall** direction, flat trend.
- Walk the **monthly smartphone** table: February dip vs **overall** climb from 42 to 78.
- **Engagement — cold-call:** “Where on this table do you *see* the dip, and where do you *still* see an upward story?”
- **Room action:** Zoom/pointer on the table cells you want them to read.

**Bridge sentence:** “Long-term slant is one pattern; the other is the wiggle that repeats on a schedule — that’s seasonality.”

---

## 5. Seasonality — Repeating Cycles and the Pizza Table (12 minutes)

- Define **seasonality** (official + simple); ice cream / Diwali + **pizza by day of week** examples.
- Three bullets: **fixed period**, not random, **multiple** cycles (weekly + yearly).
- Walk the **pizza delivery** table: stress **Friday/Saturday** spikes and **repetition** across weeks.
- **Check for understanding:** “If I only showed you Monday rows, would you know it’s a weekly pattern?” (Brief discussion.)

**Bridge sentence:** “We now have names for the slope and the repeating bump — let’s set them side by side and add the leftovers: noise and long waves.”

---

## 6. Trend vs Seasonality, Noise, Cyclical, Decomposition (11 minutes)

- Screen the **comparison table** (trend vs seasonality); read one row at a time quickly.
- One example: e-commerce **upward trend** + **October festive spike** — both at once.
- One line on **decomposition** as “naming the parts” before modeling.
- **Noise** and **cyclical** (non-fixed period): contrast **seasonal** “every Friday” with **economic** cycles.
- For beginners, reinforce: “Most starter work = trend + seasonality + noise.”
- **Pair-share (90 sec):** Give one real example that has *both* trend and seasonality (e.g. app downloads + festival sales).

**Bridge sentence:** “Patterns are useless if we train the model the wrong way — next we fix the most common time-series mistake: the random train-test split.”

---

**→ Take the single break (5–8 minutes) here if you have hit ~60–70 minutes of teaching. Optional:** quick stretch, water, return prompt on slide (“We split in *time order* after break”). **←**

---

## 7. Why Random Splits Fail — Leakage and Chronological Split (10 minutes)

- Set up: **house prices** = shuffle OK; **tomorrow’s price** = shuffle cheats.
- **Future leakage** in plain language: “peeking at the answer sheet”; stock exam-student analogy from notes.
- **Chronological split:** sort by time, **first 80% train**, **last 20% test**; rule: “learn from the past only.”
- Show **chronological vs random split** image; then the **10-month sales** table: Jan–Aug train, Sep–Oct test — no overlap.
- **Thumbs up:** “Is putting September in *training* for a *September forecast* a fair test?” (They should not thumb-up.)

**Bridge sentence:** “A single past→future cut is the minimum; next we add a pro technique that steps forward one period at a time.”

---

## 8. Walk-Forward Validation (6 minutes)

- Forecaster story: **expand the training window**, predict the **next** block only.
- Steps 1–4 from notes on the board; show **walk-forward** figure.
- **Why better:** multiple scores, stable vs degrading over time, matches deployment.
- Quick **table**: Random = bad; Chrono = good; Walk-forward = best for rigorous checks.
- **Engagement — cold-call:** “In step 2, can the model ever train on the month it is trying to predict?” (No.)

**Bridge sentence:** “Once the split is honest, we need features that summarize *recent* history — that’s where rolling windows come in.”

---

## 9. Rolling Windows — Idea, Why, and Common Statistics (7 minutes)

- Definition + **running** / **7-day average** intuition; **30-day stock** example.
- Show **rolling window** figure (window sliding one step).
- **Why:** smooth noise, **build features** (mean, std, etc.) for the model.
- Bulleted list: rolling mean, std, min/max, sum — one line each.
- **Room action:** Point at the axis on the figure: “The frame is fixed size, the world moves forward.”

**Bridge sentence:** “Definitions turn into code with pandas on the same small sales table you’ll use in assignments.”

---

## 10. Live Demo — Pandas `rolling` and the Sample Output Table (10 minutes)

- **Live-coding (or pre-recorded with pause points):** Build `date_range`, `sales`, `set_index('date')`, `rolling(3).mean/std/max`, `print(df)`.
- Explain **NaN** on the first two rows: “We need 3 days of history — expect gaps.”
- Walk **sample output** table: compute **211.67** for Jan 3 together on the whiteboard or calculator; verify **rolling_max** for one row.
- **Window size judgment:** small (3–7) vs large (30–90); “often multiple Ns as features.”
- **Room action:** If live, have learners open the same snippet in Colab/IDE; **circulate** and check `rolling_mean_3` first non-NaN row.

**Bridge sentence:** “Rolling is ‘many past days summarized’; lags are ‘this exact day last week’ — a simpler feature family.”

---

## 11. Lag Features — `shift(1)` and `shift(7)` (5 minutes)

- **Live or walk-through** the two lines: `lag_1`, `lag_7`.
- **Sample table:** connect Jan 8 row — lag_1 = prior day, lag_7 = Jan 1; **NaN** until history exists; `dropna()` before training.
- **Thumbs up:** “Is `lag_7` the same as a 7-day *average*?” (No — it’s a single past point.)

**Bridge sentence:** “With honest splits and rich features, we still need the right *numbers* to score forecasts — that means regression-style errors, not accuracy.”

---

## 12. MAE — Mean Absolute Error and sklearn (7 minutes)

- One line: time series = mostly **regression/forecasting**, not accuracy.
- **MAE** intuition + **rain 5mm vs 8mm**; formula on slide; work the 5-day **MAE = 12** table.
- **Live:** `mean_absolute_error(actual, predicted)` with the small arrays from notes.
- **Engagement — cold-call:** “What unit is MAE in?” (Same as target — rupees, degrees, etc.)

**Bridge sentence:** “MAE treats big and small mistakes in a straight average; sometimes one huge miss must hurt more — that’s RMSE.”

---

## 13. RMSE — When Large Errors Must Hurt More (6 minutes)

- **RMSE** definition; **penalize large errors** — medicine demand example.
- **Table** where one bad day inflates RMSE more than MAE; show **MAE vs RMSE** image.
- **Code path:** MSE then `np.sqrt` — or show sklearn pattern from notes.
- **Pair-share (60 sec):** “Would you report MAE or RMSE for hospital oxygen tanks?” (Bias toward RMSE; debrief briefly.)

**Bridge sentence:** “When you compare *different scales* — small shop vs big factory — MAPE turns errors into percent.”

---

## 14. MAPE, Metric Choice, and the Comparison Table (6 minutes)

- **MAPE** idea; two rupee examples with same **percentage**; walk **6.48%** table.
- **Code** snippet with `np`; **watch out:** **zero** actuals break MAPE — use MAE/RMSE.
- **Metric table** (MAE / RMSE / MAPE) — “often report more than one.”
- **Room action:** No deep math; keep focus on *when* each helps.

**Bridge sentence:** “Before you trust your model, you must beat the laziest possible predictor — a baseline.”

---

## 15. Baselines and End-to-End Workflow (7 minutes)

- **Naive, seasonal naive, rolling-mean** baselines — one line each; “if you can’t beat naive, something’s wrong.”
- **Screen-share** the long **RandomForest** workflow: create data → roll + lag → `dropna` → `iloc` split (no shuffle) → fit → `MAE` on test.
- **Narration only** one pass — do **not** line-by-line if short on time; highlight **chronological `iloc` split** and **feature list**.
- **Engagement — cold-call:** “Where in this script would a random `train_test_split` break the story?”

**Bridge sentence:** “That loop is the spine of today: order, features, honest split, then score.”

---

## 16. Key Takeaways, Glossary, and Next-Session Teaser (4 minutes)

- Rapid **five bullets** from “Key takeaways” (read or paraphrase).
- Optional: flash the **terms table** (Time Series, Leakage, Chronological, Walk-forward, Rolling, Lag, MAE, RMSE, MAPE, Naive) — no deep drill.
- Tease next session: **ARIMA**, **LSTMs**, long-range dependencies beyond rolling features.
- **Engagement — exit ticket (optional, 1 min in chat or paper):** “In one line: why can’t I shuffle a sales sheet before splitting?”
- **Room action:** Thank the group; point to where notes and code live in the course folder.

**Bridge sentence:** (Use only if you need a final line) “We started with *order*, we end with *honest evaluation* — that’s the foundation for every forecast you’ll build from here.”

---

## Timing Flex — If the Session Is Running Long

- **First trims (save ~8–12 minutes):** Shorten **Pair-shares** to 60 seconds; skip reading every cell in the **smartphone** and **pizza** tables (show, don’t read); cover **walk-forward** with the diagram + 3 steps only (omit extended table read).
- **Second trims (save ~10–15 minutes):** Run **rolling pandas demo** as a pre-recorded 3-minute clip *or* show output table only, no live typing; **merge MAE/RMSE/MAPE** into one block with formulas on one slide and **one** code cell for MAE only, assigning RMSE/MAPE as “read the notes.”
- **Last resort:** Defer the **full RandomForest** script to async reading; in class, only narrate 4 steps: features → `dropna` → chronological `iloc` split → `MAE`.
- **If ahead of time:** Add a **2-minute poll** (chat or hands): “Random split is OK for time series — True/False,” then debrief; or extra **Q&A** on **leakage** with one whiteboard calendar sketch.

**Never cut:** the idea of **chronological split and leakage**; the distinction between **trend and seasonality**; at least a **glimpse** of **rolling** and **lag** code.

---
