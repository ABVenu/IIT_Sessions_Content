# Lecture Script: Integrating Applications with Python Data Tools — RetailPulse Analytics

**Session Duration:** 2 hours  
**Target Audience:** Learners from diverse backgrounds, including those without prior technical training. Keep delivery concrete and example-led.

**How to use this document:** Timing and facilitation only — not a transcript. Adapt wording to your style.

**Break rule:** After **60–70 minutes**, take **one** pause of **5–8 minutes** (not a numbered block).

---

## 1. Welcome, Capstone Frame, and VS Code Setup (10 minutes)

- Frame today as **Module 1 capstone**: **NumPy + pandas + SQL** in one **RetailPulse** app — not three separate exercises.
- Read five outcomes from Lecture Notes “What You Will Learn.”
- **Room action:** Folder `retailpulse_dashboard`, `venv`, `pip install pandas numpy`, interpreter from `venv`.
- Paste both **S3 URLs** (CSV + JSON) into chat.
- **Engagement — thumbs up:** `python -c "import pandas, numpy, sqlite3; print('ok')"` works.

**Bridge sentence:** “Once VS Code is ready, we’ll see why RetailPulse needs one integrated pipeline instead of three disconnected scripts.”

---

## 2. RetailPulse Story and Module 1 Revision Sprint (10 minutes)

- Narrate: superstore orders CSV + region targets JSON → KPIs → SQL reports → pandas executive summary.
- Screen-share **why databases** image from Notes (session10).
- Hit revision only: pandas = tables; NumPy = fast columns; SQL = persistent queries; `to_sql` / `read_sql` = bridges.
- **Cold-call:** “Which tool is best for `GROUP BY region` on 50,000 rows stored permanently?” (SQL / database.)
- **Activity (1 min):** Students write the one-sentence integration note from Notes revision section.

**Bridge sentence:** “Story set — next we pull both data files from S3 onto every laptop.”

---

## 3. Notes Step 1 — Download from S3 (10 minutes)

- **Live-coding:** `download_data_files()` and `DATA_URLS`.
- Confirm `data/superstore_orders.csv` and `data/region_targets.json` exist.
- Open CSV in VS Code — point at columns (Order ID, Region, Sales, Profit).
- Open JSON — show `regions` list with targets.
- **Cold-call:** “Which file is the large fact export vs the small config?” (CSV vs JSON.)

**Bridge sentence:** “Data is local — we load and clean with pandas before touching NumPy or SQL.”

---

## 4. Notes Step 2 (Phase 2) — pandas Load and Dimension Tables (20 minutes)

- **Live-coding:** `load_and_prepare_orders()` — shape, `head`, `isnull`, filter `sales >= 50`.
- **Live-coding:** `build_dimension_tables()` — explain `factorize` for `customer_id`, `customers` vs `order_lines`.
- **Engagement — thumbs up:** `customers` has fewer rows than `order_lines`.
- Mention snake_case rename — same names in SQL later.

**Bridge sentence:** “Tables are clean — NumPy will crunch the numeric columns in one shot.”

---

## 5. Notes Step 2 (Phase 3) — NumPy KPIs (15 minutes)

- **Live-coding:** `numpy_kpi_summary()` — `to_numpy`, `np.sum`, `np.mean`, `np.percentile`.
- Contrast: doing `sum()` in a Python loop vs one NumPy call.
- **Cold-call:** “Why convert to NumPy if pandas already has `.sum()`?” (Speed, percentiles, masks on large data.)
- **Activity (2 min):** Students note `total_profit` from output.

**Bridge sentence:** “KPIs are computed — now we persist tables to SQLite so SQL can answer multi-table questions.”

---

## 6. Notes Step 2 (Phases 4–5) — SQLite + SQL Analytics (35 minutes)

- **Longest block.** Live-coding: `setup_sqlite_database()` with `to_sql` — show `retailpulse.db` file appear.
- Run SQL Q1 (`WHERE` + `JOIN`) and Q2 (`GROUP BY` region) — screen-share printed rows.
- Screen-share **GROUP BY** and **INNER JOIN** images from Notes.
- SQL Q3 (`HAVING`) and Q4 (JOIN `region_targets` — target vs actual).
- SQL Q5 top customers — tie to business question.
- **Room action:** Circulate during SQL section; common error = wrong column name after rename.
- **Common doubt:** delete `.db` and re-run if tables missing.

**Bridge sentence:** “SQL answered the business questions — we pull results back into pandas for the final report.”

---

## 7. Notes Step 2 (Phase 6) + Step 3 — Executive Report and pandas↔SQL Map (15 minutes)

- **Live-coding:** `print_executive_report()` and `pd.read_sql` outputs.
- Walk **pandas vs SQL mapping table** in Notes Step 4.
- **Pair-share (2 min):** “When would you use `groupby` in pandas vs `GROUP BY` in SQL?” (Exploration in notebook vs persisted shared DB / large data.)
- **Activity:** Change Q1 threshold `1000` → `500`, re-run, compare row count.

**Bridge sentence:** “You’ve shipped a mini integrated app — we’ll close with what transfers to production.”

---

## 8. Wrap-Up and Key Takeaways (5 minutes)

- Three takeaways: chain tools; `to_sql` / `read_sql`; dimension + fact split enables JOINs.
- Point to Quick Reference table.
- Optional stretch: matplotlib bar chart from `region_vs_target` DataFrame.
- **Exit ticket:** “Name one step that only SQL did well today.”

---

## Timing Flex

| Behind | Cut |
|--------|-----|
| 10+ min | Shorten Block 2 to 5 min |
| 15+ min | Run SQL Q1, Q2, Q4 only; demo Q3/Q5 verbally |
| 20+ min | Pre-build `retailpulse.db` on instructor machine; students run report half only |

| Ahead | Add |
|-------|-----|
| 10 min | Students write one extra SQL question from practice list |
| 15 min | Optional LEFT JOIN region with a dummy region in targets |

**Hard stop:** Everyone runs `main()` once and sees executive report + `retailpulse.db`.

---

## Lecture Notes Alignment Map

| Script block | Time | Lecture Notes section |
|--------------|------|------------------------|
| 1 | 10 min | What You Will Learn + **Step 0** VS Code |
| 2 | 10 min | RetailPulse Problem + **Module 1 revision** |
| 3 | 10 min | **Step 1** S3 download |
| 4 | 20 min | **Step 2** Phase 2 — pandas load + dimensions |
| 5 | 15 min | **Step 2** Phase 3 — NumPy KPIs |
| 6 | 35 min | **Step 2** Phases 4–5 — SQLite + SQL |
| 7 | 15 min | **Step 2** Phase 6 + **Step 3–4** report + mapping table |
| 8 | 5 min | Key Takeaways + Quick Reference |

**Data URLs (chat):**

- `https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module1/Masterclass/001/data/superstore_orders.csv`
- `https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module1/Masterclass/001/data/region_targets.json`
