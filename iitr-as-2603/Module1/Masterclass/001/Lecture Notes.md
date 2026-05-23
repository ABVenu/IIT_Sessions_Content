# Integrating Applications with Python Data Tools: RetailPulse Analytics Dashboard

## What You Will Learn in This Session

In the previous part of the course, you worked with **Python basics**, **NumPy** arrays, **pandas** for tables, and **SQL** for querying persistent data. You practised filtering rows, aggregating with `groupby`, writing `SELECT` and `WHERE` queries, and combining tables with **JOINs**.

This masterclass connects those tools in **one integrated application** — the way real analyst and backend teams ship small internal dashboards. You will build **RetailPulse Analytics**: a script that loads retail order data from the course **S3** bucket, analyses numbers with **NumPy**, stores structured tables in **SQLite**, runs **SQL** reports, and brings results back into **pandas** for a final summary.

By the end of this session, you will be able to:

- Download a **CSV** and **JSON** dataset from S3 into a **VS Code** project on your laptop.
- **Clean and filter** order data with pandas before sending it to other tools.
- Use **NumPy** for fast numeric summaries on sales and profit columns.
- **Load pandas tables into SQLite** and query them with SQL (`SELECT`, `WHERE`, `GROUP BY`, `HAVING`, `JOIN`).
- Use **`pd.read_sql`** to pull SQL results back into pandas and print an executive report.

---

## The RetailPulse Problem

**RetailPulse** is a retail analytics team supporting a superstore chain. Every week, leadership asks:

- *"What is our total profit and average order value this quarter?"*
- *"Which region beat its monthly sales target?"*
- *"Who are the top customers by revenue?"*

The raw data lives in a **CSV export** (hundreds of order lines). The **targets** live in a small **JSON** file (region goals). The team wants **one Python application** that:

1. Loads both files (pandas).
2. Computes quick numeric KPIs (NumPy).
3. Persists data in a **local database** (SQLite) for reusable SQL.
4. Answers business questions with **JOIN** and **aggregation** queries.
5. Returns a clean **pandas report** for the ops meeting.

**Your job today:** Build that integrated script in **VS Code** — not in Colab, not in a separate MySQL install for this exercise (SQLite runs inside Python).

![Why databases: pandas and CSV live in temporary workspace memory while a database persists on disk and serves many users at once — persistence, concurrency, scale](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/session10/session10-why-databases.png)

---

## Module 1 Skills — Quick Revision

This section is a **checklist**, not a full re-teach. Skim it, then start coding.

**pandas**
- **Official Definition:** A library for tabular data (`DataFrame`) with loading, filtering, grouping, and merging.
- **In Simple Words:** Excel-like tables in Python with powerful filters and summaries.
- **Real-Life Example:** Sorting 500 food-delivery orders by city and totalling revenue per restaurant.

**NumPy**
- **Official Definition:** A library for fast numeric **arrays** and vectorised math.
- **In Simple Words:** A calculator that works on whole columns at once instead of row-by-row loops.
- **Real-Life Example:** Finding mean and standard deviation of 10,000 exam marks in one line.

**SQL (SQLite in Python)**
- **Official Definition:** A language to **read and summarise** data stored in relational tables.
- **In Simple Words:** Asking precise questions to a filing cabinet that remembers data after you close the program.
- **Real-Life Example:** *"Show regions where total profit is above ₹1,00,000."*

**Integration idea**
- **pandas** = prepare and present tables.
- **NumPy** = fast numeric core on columns.
- **SQL** = persistent storage + complex multi-table questions.
- **`pd.read_sql`** = bridge from SQL answers back to pandas.

**Activity:** Write one sentence in a comment: *"pandas prepares data, SQL stores and queries it, NumPy speeds up the math in between."*

---

## Data on S3 — Download Links

| File | Purpose | S3 URL |
|------|---------|--------|
| `superstore_orders.csv` | ~500 order line items (sales, profit, region, customer, product) | `https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module1/Masterclass/001/data/superstore_orders.csv` |
| `region_targets.json` | Monthly sales target per region for target-vs-actual analysis | `https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module1/Masterclass/001/data/region_targets.json` |

**Common doubt:** Why both CSV and JSON? **Answer:** CSV is the large operational export; JSON is a small config file many apps use for targets, rules, or feature flags — a realistic split.

---

## Step 0 — Set Up VS Code and Your Project

### Project structure

```text
retailpulse_dashboard/
├── data/                      ← downloaded from S3
│   ├── superstore_orders.csv
│   └── region_targets.json
├── retailpulse.db             ← created by SQLite (auto)
├── requirements.txt
└── retailpulse_integration.py
```

### Virtual environment

Open **Terminal** in VS Code:

```bash
cd retailpulse_dashboard
python3 -m venv venv
source venv/bin/activate          # Mac/Linux
# venv\Scripts\activate           # Windows
pip install pandas numpy
```

**`requirements.txt`:**

```text
pandas
numpy
```

**Setup check:** Run `python -c "import pandas, numpy, sqlite3; print('RetailPulse ready')"` — `sqlite3` is built into Python; no extra install.

---

## Step 1 — Download Data from S3

```python
# =============================================================================
# STEP 1 — INGESTION: Download CSV + JSON from course S3 into data/
# =============================================================================

import os
import json
import urllib.request

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

DATA_URLS = {
    "superstore_orders.csv": (
        "https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/"
        "iitr-as-2603/module1/Masterclass/001/data/superstore_orders.csv"
    ),
    "region_targets.json": (
        "https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/"
        "iitr-as-2603/module1/Masterclass/001/data/region_targets.json"
    ),
}


def download_data_files():
    """Pull both datasets from S3 so the app works offline after one download."""
    for filename, url in DATA_URLS.items():
        local_path = os.path.join(DATA_DIR, filename)
        urllib.request.urlretrieve(url, local_path)
        print(f"Downloaded: {local_path}")
```

**How the code works:**

- Files land in `data/` next to your script — same pattern as loading from a company file server once per day.
- If download fails, open the URL in a browser and save manually into `data/`.

---

## Step 2 — Full Integration Script (`retailpulse_integration.py`)

Copy the **entire** script below into `retailpulse_integration.py`. Comments mark each **major phase** of the integrated application.

```python
# =============================================================================
# RetailPulse Analytics — Integrated NumPy + pandas + SQL (SQLite)
#
# FLOW:
#   1. Download data (S3)
#   2. pandas — load, clean, filter, build dimension tables
#   3. NumPy — vectorised KPIs on sales / profit
#   4. SQLite — persist tables, run SQL (aggregation + JOIN)
#   5. pandas — read_sql executive report
# =============================================================================

import os
import json
import sqlite3
import urllib.request

import numpy as np
import pandas as pd

# =============================================================================
# CONFIGURATION
# =============================================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
DB_PATH = os.path.join(BASE_DIR, "retailpulse.db")

DATA_URLS = {
    "superstore_orders.csv": (
        "https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/"
        "iitr-as-2603/module1/Masterclass/001/data/superstore_orders.csv"
    ),
    "region_targets.json": (
        "https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/"
        "iitr-as-2603/module1/Masterclass/001/data/region_targets.json"
    ),
}


# =============================================================================
# PHASE 1 — DOWNLOAD (S3 → local data/)
# =============================================================================
def download_data_files():
    os.makedirs(DATA_DIR, exist_ok=True)
    for filename, url in DATA_URLS.items():
        local_path = os.path.join(DATA_DIR, filename)
        urllib.request.urlretrieve(url, local_path)
        print(f"Downloaded: {local_path}")


# =============================================================================
# PHASE 2 — PANDAS: Load, inspect, clean, filter
# =============================================================================
def load_and_prepare_orders() -> pd.DataFrame:
    """
    Read CSV into a DataFrame, standardise column names, basic EDA, filter bad rows.
    Returns a cleaned line-level orders table ready for NumPy and SQL.
    """
    csv_path = os.path.join(DATA_DIR, "superstore_orders.csv")
    df = pd.read_csv(csv_path)

    # Snake_case column names — easier in Python and SQL
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )

    print("\n=== PANDAS: Shape and preview ===")
    print("Shape:", df.shape)
    print(df.head(3))

    print("\n=== PANDAS: Missing values ===")
    print(df.isnull().sum())

    # Drop rows with missing sales or negative sales (data quality gate)
    df = df.dropna(subset=["sales", "profit"])
    df = df[df["sales"] > 0]

    # Keep only rows with meaningful line revenue (example business filter)
    df = df[df["sales"] >= 50]

    print(f"\nRows after cleaning filter: {len(df)}")
    return df


def build_dimension_tables(df: pd.DataFrame):
    """
    Split flat CSV into:
      - customers (one row per customer)
      - order_lines (every product line, linked by customer_id)
    This mirrors real apps: dimensions + facts.
    """
    # Assign stable integer customer_id (like a warehouse surrogate key)
    df = df.copy()
    df["customer_id"] = pd.factorize(df["customer_name"])[0] + 1
    df["line_id"] = range(1, len(df) + 1)

    customers = (
        df[["customer_id", "customer_name", "segment", "region"]]
        .drop_duplicates(subset=["customer_id"])
        .sort_values("customer_id")
    )

    order_lines = df[
        [
            "line_id",
            "order_id",
            "customer_id",
            "order_date",
            "category",
            "sub_category",
            "product_name",
            "sales",
            "quantity",
            "discount",
            "profit",
        ]
    ].copy()

    return customers, order_lines


def load_region_targets() -> pd.DataFrame:
    """Load JSON targets into a small DataFrame for SQL JOIN."""
    json_path = os.path.join(DATA_DIR, "region_targets.json")
    with open(json_path, "r", encoding="utf-8") as f:
        payload = json.load(f)
    return pd.DataFrame(payload["regions"])


# =============================================================================
# PHASE 3 — NUMPY: Fast numeric KPIs on array columns
# =============================================================================
def numpy_kpi_summary(order_lines: pd.DataFrame) -> dict:
    """
    Convert sales/profit columns to NumPy arrays and compute vectorised stats.
    Shows why NumPy sits between raw pandas and SQL reporting.
    """
    sales = order_lines["sales"].to_numpy(dtype=float)
    profit = order_lines["profit"].to_numpy(dtype=float)
    quantity = order_lines["quantity"].to_numpy(dtype=float)

    summary = {
        "total_sales": float(np.sum(sales)),
        "total_profit": float(np.sum(profit)),
        "avg_sales_per_line": float(np.mean(sales)),
        "std_sales": float(np.std(sales)),
        "max_profit_line": float(np.max(profit)),
        "total_units": int(np.sum(quantity)),
    }

    print("\n=== NUMPY: KPI summary ===")
    for key, value in summary.items():
        print(f"  {key}: {value:,.2f}" if isinstance(value, float) else f"  {key}: {value}")

    # Example: lines with profit in top 10% (boolean mask — NumPy strength)
    threshold = np.percentile(profit, 90)
    high_profit_count = int(np.sum(profit >= threshold))
    print(f"  lines_in_top_10pct_profit: {high_profit_count}")

    return summary


# =============================================================================
# PHASE 4 — SQLITE: Create DB, load tables from pandas
# =============================================================================
def setup_sqlite_database(customers, order_lines, region_targets):
    """
    Write pandas DataFrames into SQLite tables.
    Integration point: pandas (memory) → SQL (persistent disk).
    """
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)  # Fresh DB each run for repeatable class demos

    conn = sqlite3.connect(DB_PATH)

    customers.to_sql("customers", conn, index=False, if_exists="replace")
    order_lines.to_sql("order_lines", conn, index=False, if_exists="replace")
    region_targets.to_sql("region_targets", conn, index=False, if_exists="replace")

    print("\n=== SQLITE: Tables created ===")
    print("  customers, order_lines, region_targets")

    return conn


# =============================================================================
# PHASE 5 — SQL: Analytical queries (SELECT, WHERE, GROUP BY, HAVING, JOIN)
# =============================================================================
def run_sql_analytics(conn) -> dict:
    """
    Run four business SQL queries via cursor + fetchall.
    Returns dict of DataFrames via read_sql for the final report.
    """
    cursor = conn.cursor()

    # --- Query 1: SELECT + WHERE — high-value lines ---
    print("\n=== SQL Q1: Lines with sales > 1000 ===")
    cursor.execute(
        """
        SELECT order_id, product_name, sales, profit, region
        FROM order_lines ol
        JOIN customers c ON ol.customer_id = c.customer_id
        WHERE sales > 1000
        ORDER BY sales DESC
        LIMIT 5;
        """
    )
    q1_rows = cursor.fetchall()
    for row in q1_rows:
        print(row)

    # --- Query 2: GROUP BY + aggregates — profit by region ---
    print("\n=== SQL Q2: Total profit by region ===")
    cursor.execute(
        """
        SELECT c.region,
               COUNT(*) AS line_count,
               ROUND(SUM(ol.profit), 2) AS total_profit,
               ROUND(AVG(ol.sales), 2) AS avg_sale
        FROM order_lines ol
        JOIN customers c ON ol.customer_id = c.customer_id
        GROUP BY c.region
        ORDER BY total_profit DESC;
        """
    )
    for row in cursor.fetchall():
        print(row)

    # --- Query 3: GROUP BY + HAVING — categories with strong profit ---
    print("\n=== SQL Q3: Categories with total profit > 5000 ===")
    cursor.execute(
        """
        SELECT category,
               COUNT(*) AS lines,
               ROUND(SUM(profit), 2) AS category_profit
        FROM order_lines
        GROUP BY category
        HAVING SUM(profit) > 5000
        ORDER BY category_profit DESC;
        """
    )
    for row in cursor.fetchall():
        print(row)

    # --- Query 4: JOIN region actuals to targets ---
    print("\n=== SQL Q4: Region sales vs monthly target ===")
    cursor.execute(
        """
        SELECT c.region,
               ROUND(SUM(ol.sales), 2) AS actual_sales,
               rt.monthly_target_sales AS target_sales,
               ROUND(SUM(ol.sales) - rt.monthly_target_sales, 2) AS gap
        FROM order_lines ol
        JOIN customers c ON ol.customer_id = c.customer_id
        JOIN region_targets rt ON c.region = rt.region
        GROUP BY c.region, rt.monthly_target_sales
        ORDER BY gap DESC;
        """
    )
    for row in cursor.fetchall():
        print(row)

    # --- Query 5: Top customers by revenue (JOIN + GROUP BY + ORDER BY) ---
    print("\n=== SQL Q5: Top 5 customers by revenue ===")
    top_customers_sql = """
        SELECT c.customer_name,
               c.region,
               COUNT(*) AS order_lines,
               ROUND(SUM(ol.sales), 2) AS total_revenue
        FROM order_lines ol
        INNER JOIN customers c ON ol.customer_id = c.customer_id
        GROUP BY c.customer_id, c.customer_name, c.region
        ORDER BY total_revenue DESC
        LIMIT 5;
    """
    cursor.execute(top_customers_sql)
    for row in cursor.fetchall():
        print(row)

    # Return key reports as pandas DataFrames (application integration closure)
    reports = {
        "region_vs_target": pd.read_sql(
            """
            SELECT c.region,
                   ROUND(SUM(ol.sales), 2) AS actual_sales,
                   rt.monthly_target_sales AS target_sales
            FROM order_lines ol
            JOIN customers c ON ol.customer_id = c.customer_id
            JOIN region_targets rt ON c.region = rt.region
            GROUP BY c.region, rt.monthly_target_sales
            ORDER BY actual_sales DESC;
            """,
            conn,
        ),
        "top_customers": pd.read_sql(top_customers_sql, conn),
    }
    return reports


# =============================================================================
# PHASE 6 — PANDAS: Executive report from SQL results
# =============================================================================
def print_executive_report(kpi: dict, reports: dict):
    """Combine NumPy KPIs and SQL-driven DataFrames into one readable summary."""
    print("\n" + "=" * 72)
    print("RETAILPULSE EXECUTIVE REPORT")
    print("=" * 72)
    print(f"\nTotal sales (NumPy):    ₹{kpi['total_sales']:,.2f}")
    print(f"Total profit (NumPy):   ₹{kpi['total_profit']:,.2f}")
    print(f"Avg sale per line:      ₹{kpi['avg_sales_per_line']:,.2f}")

    print("\n--- Region vs target (from SQL → pandas) ---")
    print(reports["region_vs_target"].to_string(index=False))

    print("\n--- Top customers (from SQL → pandas) ---")
    print(reports["top_customers"].to_string(index=False))

    best_region = reports["region_vs_target"].iloc[0]["region"]
    print(f"\nInsight: Highest actual sales region this run: {best_region}")
    print("Next step: Feed these DataFrames into charts (matplotlib) in a future session.")


# =============================================================================
# MAIN — Wire all phases in order
# =============================================================================
def main():
    print("=== RetailPulse Integrated Dashboard ===\n")

    download_data_files()

    orders_df = load_and_prepare_orders()
    customers, order_lines = build_dimension_tables(orders_df)
    region_targets = load_region_targets()

    kpi = numpy_kpi_summary(order_lines)

    conn = setup_sqlite_database(customers, order_lines, region_targets)
    reports = run_sql_analytics(conn)
    conn.close()

    print_executive_report(kpi, reports)
    print(f"\nDatabase saved at: {DB_PATH}")


if __name__ == "__main__":
    main()
```

**How the code works:**

- **Phase 2 (pandas):** Loads CSV, cleans bad rows, builds `customers` and `order_lines` — same idea as normalising a flat export into tables before SQL.
- **Phase 3 (NumPy):** `to_numpy()` then `np.sum`, `np.mean`, `np.percentile` — no slow Python loops.
- **Phase 4 (SQLite):** `to_sql()` writes tables; `retailpulse.db` persists on disk.
- **Phase 5 (SQL):** Five queries map to Module 1 skills — `WHERE`, `GROUP BY`, `HAVING`, `INNER JOIN`.
- **Phase 6 (pandas):** `pd.read_sql()` closes the loop — SQL answers land back in DataFrames for reporting.

![GROUP BY splits rows into separate groups (for example by city or customer), then each aggregate runs inside its own group](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/session11/session11-group-by-buckets.png)

![INNER JOIN keeps only rows that match in both tables; LEFT JOIN keeps every row from the left table and uses NULL when there is no match on the right](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/session11/session11-inner-vs-left-join.png)

**Common doubt:** Why SQLite instead of MySQL Workbench here? **Answer:** SQLite needs no server install — perfect for a **single Python app** integrating all three tools. MySQL Workbench skills transfer directly; only the connection string changes.

**Activity:** After `main()` runs, open `retailpulse.db` with the **DB Browser for SQLite** (optional) or run `SELECT COUNT(*) FROM order_lines` in a small test script to prove data persisted.

---

## Step 3 — Run the Integrated App

```bash
python retailpulse_integration.py
```

**Expected terminal flow:**

1. Two files downloaded to `data/`.
2. pandas shape (~500 rows before filter, fewer after cleaning).
3. NumPy KPI block printed.
4. Five SQL query result blocks.
5. Executive report with region vs target and top customers.

**Activity:** Change the `WHERE sales > 1000` filter to `> 500` in SQL Q1. Re-run only that query (or the whole script). Note how many more rows appear — precision vs breadth, similar to tuning `top_k` in RAG.

---

## Step 4 — Map pandas Operations to SQL (Revision Table)

| pandas (you practised earlier) | SQL (today in SQLite) |
|-------------------------------|------------------------|
| `df[df["sales"] > 1000]` | `WHERE sales > 1000` |
| `df.groupby("region")["profit"].sum()` | `GROUP BY region` + `SUM(profit)` |
| Filter groups after aggregating | `HAVING SUM(profit) > 5000` |
| `pd.merge(customers, orders, on="customer_id")` | `INNER JOIN ... ON customer_id` |
| `df.sort_values("sales", ascending=False).head(5)` | `ORDER BY sales DESC LIMIT 5` |
| Result in a new DataFrame | `pd.read_sql(query, conn)` |

![A JOIN uses matching key columns — a primary key in one table and a foreign key in the other — to link related rows](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/session11/session11-joins-keys-bridge.png)

---

## Step 5 — Troubleshooting Checklist

| Issue | What to try |
|-------|-------------|
| `FileNotFoundError` for CSV | Re-run download; check `data/` folder path |
| Empty SQL results | Print `len(order_lines)` before `to_sql` — filter may be too strict |
| `no such table` | Delete `retailpulse.db` and re-run `main()` |
| Wrong column names in SQL | Print `order_lines.columns` — must match snake_case names |
| NumPy `nan` in KPIs | Check `dropna` ran on sales/profit |

---

## Sample Business Questions (Practice)

Use these to extend the SQL section on your own:

1. Which **segment** (`Consumer`, `Corporate`, `Home Office`) has the highest average profit per line?
2. Which **sub_category** has more than 20 order lines and average discount above 0.15?
3. Which **regions** missed their target (`gap < 0` in Q4)?
4. Which customer in the **East** region has the most order lines?

---

## Key Takeaways

- Real **data applications** rarely use only one library — they **chain** pandas, NumPy, and SQL in one workflow.
- **pandas** is strongest for loading, cleaning, and presenting tables; **NumPy** for fast numeric cores; **SQL** for persistent storage and multi-table logic.
- **`DataFrame.to_sql`** and **`pd.read_sql`** are the standard bridges between pandas and a database in Python.
- Splitting a flat CSV into **`customers`** + **`order_lines`** mirrors how companies model data before JOINs.
- The same integration pattern scales to larger databases (PostgreSQL, MySQL) when you move from class projects to production.

---

## Important Commands, Libraries, and Terminologies

| Item | Meaning |
|------|---------|
| `python3 -m venv venv` | Create isolated Python environment |
| `pip install pandas numpy` | Install table and array libraries |
| `pd.read_csv(path)` | Load CSV into a DataFrame |
| `df.to_numpy()` | Convert a column to a NumPy array |
| `np.sum`, `np.mean`, `np.percentile` | Vectorised numeric operations |
| `sqlite3.connect("file.db")` | Open/create a local SQLite database |
| `df.to_sql("table", conn, if_exists="replace")` | Write a DataFrame into SQL |
| `pd.read_sql(query, conn)` | Run SQL and return a DataFrame |
| `pd.factorize(column)` | Create integer IDs from text labels |
| `SELECT` / `WHERE` / `GROUP BY` / `HAVING` | Core SQL clauses for filtering and summarising |
| `INNER JOIN` | Keep rows that match in both tables |
| **Integration** | Connecting multiple tools in one application flow |
| **Surrogate key** | Simple integer ID (`customer_id`) replacing long text names in joins |
