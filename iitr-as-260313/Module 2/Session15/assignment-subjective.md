# Assignment — Subjective (Session 15)

**Theme:** Read-only SQL reporting for a small “agent memory” style schema (sorting, pagination, pattern filters, and inner joins).

**Difficulty:** Medium

---

## Scenario

You support an internal tool that stores **device registrations** and **usage events** in two related tables.

- **`devices`**: one row per physical device.
- **`events`**: many rows per device (each event belongs to exactly one device).

The product team wants a **single SQL file** they can run in PostgreSQL / Supabase SQL editor to answer four reporting questions **without** changing the schema.

---

## Starter schema and seed data (use as-is)

Create a file named `session15_device_reports.sql`. **Keep** the following `CREATE TABLE` + `INSERT` section at the top **unchanged** (you may add comments, but do not rename columns/tables):

```sql
CREATE TABLE devices (
  device_id   INTEGER PRIMARY KEY,
  label       TEXT NOT NULL,
  owner_email TEXT NOT NULL,
  city        TEXT NOT NULL
);

CREATE TABLE events (
  event_id    INTEGER PRIMARY KEY,
  device_id   INTEGER NOT NULL REFERENCES devices(device_id),
  event_type  TEXT NOT NULL,
  payload     TEXT NOT NULL,
  created_at  TIMESTAMP NOT NULL
);

INSERT INTO devices VALUES
  (1, 'Edge-Node-A', 'a@example.com', 'Bengaluru'),
  (2, 'Edge-Node-B', 'b@example.com', 'Bengaluru'),
  (3, 'Gateway-01',  'c@example.com', 'Pune'),
  (4, 'Gateway-02',  'd@example.com', 'Mumbai');

INSERT INTO events VALUES
  (101, 1, 'boot',   'ok',  TIMESTAMP '2026-05-01 09:00:00'),
  (102, 1, 'error',  'e1',  TIMESTAMP '2026-05-02 10:05:00'),
  (103, 2, 'boot',   'ok',  TIMESTAMP '2026-05-03 08:10:00'),
  (104, 3, 'sync',   's1',  TIMESTAMP '2026-05-04 11:20:00'),
  (105, 3, 'error',  'e2',  TIMESTAMP '2026-05-05 12:30:00'),
  (106, 4, 'boot',   'ok',  TIMESTAMP '2026-05-06 07:40:00'),
  (107, 1, 'sync',   's2',  TIMESTAMP '2026-05-07 13:50:00'),
  (108, 2, 'error',  'e3',  TIMESTAMP '2026-05-08 14:55:00'),
  (109, 4, 'sync',   's3',  TIMESTAMP '2026-05-09 15:10:00'),
  (110, 3, 'boot',   'ok',  TIMESTAMP '2026-05-10 16:25:00');
```

---

## What you must implement (four queries)

Write **four separate `SELECT` statements** below the seed data. Each must run independently (you may repeat `ORDER BY` logic as needed).

1) **Newest errors first (cap + sort):**  
   Return `event_id`, `device_id`, `payload`, `created_at` for rows where `event_type = 'error'`, sorted by **`created_at` descending**, and return **at most 3** rows.

2) **Stable pagination (page 2):**  
   Return `event_id`, `device_id`, `event_type`, `created_at` for **all** events, ordered by **`event_id` ascending**. Return **page 2** with a page size of **4** (use `LIMIT` and `OFFSET`).

3) **Text pattern filter on devices:**  
   Return `device_id`, `label`, `owner_email` for devices whose `label` contains the substring **`way`** anywhere in the name (case-sensitive match is fine for this exercise).

4) **Inner join report + filter + sort:**  
   Return **`devices.label`**, **`events.event_type`**, **`events.created_at`** for events where **`devices.city = 'Bengaluru'`** and **`events.event_type <> 'error'`**, sorted by **`events.created_at` ascending**.

---

## Acceptance checks (self-verify before submission)

- Query (1) never returns more than **3** rows and never returns a non-error `event_type`.
- Query (2) returns **exactly 4** rows on the provided seed data and they correspond to **rows 5–8** when ordered by `event_id ASC` (verify by inspection).
- Query (3) returns **only** `Gateway-01` and `Gateway-02` for the provided seed data.
- Query (4) returns **only** Bengaluru devices and excludes `error` events, sorted oldest → newest.

---

## Submission instructions (**case c** — single file coding)

- Implement everything in **one** file: `session15_device_reports.sql` using **VS Code** (or your usual editor).
- Run the script end-to-end in **PostgreSQL** or the **Supabase SQL editor** and confirm all four queries execute without errors and match the acceptance checks.
- Submit the **full file contents** in the LMS code editor / answer box for this question.

---

## Answer explanation (for facilitators / LMS)

### Ideal approach

- **(1)** Filter with `WHERE event_type = 'error'`, sort with `ORDER BY created_at DESC`, cap with `LIMIT 3`.
- **(2)** `ORDER BY event_id ASC` then `LIMIT 4 OFFSET 4` implements page size 4, page 2 (0-based offset of 4).
- **(3)** `WHERE label LIKE '%way%'` matches `Gateway-01` and `Gateway-02`.
- **(4)** `FROM events INNER JOIN devices ON events.device_id = devices.device_id` (or equivalent qualified join keys), filter on `devices.city` and `events.event_type`, sort by `events.created_at ASC`.

### Example solution (reference)

```sql
-- 1)
SELECT event_id, device_id, payload, created_at
FROM events
WHERE event_type = 'error'
ORDER BY created_at DESC
LIMIT 3;

-- 2)
SELECT event_id, device_id, event_type, created_at
FROM events
ORDER BY event_id ASC
LIMIT 4 OFFSET 4;

-- 3)
SELECT device_id, label, owner_email
FROM devices
WHERE label LIKE '%way%';

-- 4)
SELECT d.label, e.event_type, e.created_at
FROM events e
INNER JOIN devices d
  ON e.device_id = d.device_id
WHERE d.city = 'Bengaluru'
  AND e.event_type <> 'error'
ORDER BY e.created_at ASC;
```

### Alternatives

- Using table names without aliases is acceptable if columns are qualified to avoid ambiguity.
- `!=` instead of `<>` is accepted on PostgreSQL for inequality.
