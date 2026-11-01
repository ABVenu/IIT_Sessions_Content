# Masterclass: Database Transactions & ACID

A UPI transfer, a railway seat booking, and a college fee payment all change **more than one fact** in storage. Money must leave one account and enter another; a seat must become reserved while a booking row appears; fee paid must match the receipt.

In the previous lesson you saw that the **backend** holds shared data, rules, and secrets, while the browser only draws what it is allowed to show. This lesson answers a sharper question: what happens when the backend must change **several related rows**, and something fails halfway?

If those steps are not protected together, the system can look successful on one phone and wrong on another. This lesson teaches **database transactions**, **ACID**, when plain **CRUD** is enough, and the **security habits** that keep databases and backends safe in real products.

## What You Will Learn in This Lesson

In this lesson, you will learn:

- The **demerit** of updating related data in **multiple steps** without protection
- Why databases need **transactions** for reliable business operations
- The difference between simple **CRUD** queries and a **transaction**
- When an app can rely on typical CRUD, and when it must use transactions
- **Commit** and **rollback** as success and failure handling
- The **ACID** properties and why each one matters
- Edge cases: crash mid-way, two users racing, timeout after success, retry duplicates
- Why **backend APIs** and **ORMs** wrap multi-step writes inside transactions
- **Security practices** for databases and backend apps (API-only access, roles, replicas, backups, and more)
- Lessons from real incidents where data leaked or servers were compromised
- An **optional** practice of `BEGIN` / `COMMIT` / `ROLLBACK` in the **Supabase SQL Editor**

By the end, you will be able to spot an unsafe multi-step update, choose CRUD vs transaction wisely, name which ACID property is at risk, and list the security habits that protect production data.

---

## Why Related Updates Are Dangerous Without Protection

A **database** stores lasting facts in tables. Many business actions need **two or more** writes that must stay true together.

- **Official Definition:** A **multi-step update** is a business action that changes more than one row, table, or value before the action is complete.
- **In Simple Words:** One user click may need several “save” steps inside the database.
- **Real-Life Example:** Transferring ₹500 from Account A to Account B needs “reduce A” and “increase B.” Both must succeed, or neither should stick.

**Need:** Products promise correctness. “Payment done” must mean money moved completely. “Seat booked” must mean a seat is blocked and a booking exists.

**Logic:** If step 1 saves and step 2 fails, the database still has step 1. The product now lies: money left A but never reached B.

![Unsafe multi-step update — debit on Account A succeeds, credit on Account B fails, leaving partial broken data in the database](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/masterclasses/sdai2606/session04/session04-01-half-update-problem.png?v=20261101)

| Unsafe sequence | What went wrong | What the user sees |
|---|---|---|
| Debit A, then credit B fails | A lost money; B unchanged | App may show error, but money is missing |
| Mark seat reserved, then booking insert fails | Seat blocked; no ticket row | Empty seat for everyone; no PNR for the passenger |
| Reduce stock, then create order fails | Stock down; no order | Inventory wrong; customer has no order |
| Mark fee paid, then receipt insert fails | Paid flag true; no receipt | Accounts and student disagree |

**Common doubt:** “The API returned an error, so nothing changed.”  
Not always. An error after the **first** write can leave a **partial** change unless the steps were one protected unit. Manual “fix later” APIs are slow and unsafe under load.

**Activity — Spot the half-update:**  
On paper, write three steps for “pay ₹200 from wallet to merchant.” Circle which stored facts would be wrong if step 2 fails after step 1 succeeds. Expected risk: wallet reduced, merchant not credited.

Once you see that risk, you need a database idea that treats many steps as **all or nothing**. That idea is a **transaction**.

---

## What Is a Database Transaction?

A **transaction** is the database’s way of grouping related changes into one protected unit of work.

- **Official Definition:** A **database transaction** is a sequence of one or more operations treated as a **single logical unit** that either fully succeeds or fully fails.
- **In Simple Words:** The database opens a temporary “draft” of changes. Only when everything is correct does it make the draft permanent.
- **Real-Life Example:** Filling a bank transfer form is not the transfer. Pressing Confirm is like asking the bank to apply the full change. Cancel is like throwing the form away before it is final.

**Need:** Business operations are rarely one cell change. Transactions match the business meaning of “one complete action.”

**Logic:** Inside a transaction, intermediate states are not final for other users in the way that matters for correctness. Outside a transaction, every successful write is already final — even if your later steps fail.

Keep this short mental picture:

- **BEGIN** opens the draft.
- Related writes happen inside the draft.
- **COMMIT** stamps the draft as final.
- **ROLLBACK** throws the draft away.

![Database transaction lifecycle — BEGIN opens draft changes, then COMMIT makes them permanent or ROLLBACK discards the draft](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/masterclasses/sdai2606/session04/session04-02-transaction-lifecycle.png?v=20261101)

| Without a transaction | With a transaction |
|---|---|
| Each successful write is final immediately | Writes stay temporary until success is declared |
| Failure after step 1 can leave partial data | Failure can undo all steps in the unit |
| Hard to keep related rows consistent | Related rows stay together by design |

**Common doubt:** “Is a transaction only for money?”  
No. Booking + seat, order + stock, attendance + total, and checkout + inventory all need the same protection. A single `UPDATE` is often atomic alone; danger starts when **several statements** must succeed together.

**Activity — Name the unit:**  
For “book one IRCTC berth,” list the facts that must change together (seat status, booking row, payment status). Write: “These must be one transaction because ___.”

Now compare this protected unit with everyday **CRUD**, so you know when each tool is enough.

---

## Simple CRUD vs a Transaction

Most beginner database work starts with **CRUD**. Transactions are a different layer of protection on top of writes.

- **Official Definition:** **CRUD** stands for **Create**, **Read**, **Update**, and **Delete** — the four basic operations on stored data.
- **In Simple Words:** Add a row, fetch a row, change a row, or remove a row.
- **Real-Life Example:** Adding a student name to a register (Create), looking up a roll number (Read), correcting a phone number (Update), and removing a withdrawn student (Delete) are CRUD actions.

![CRUD vs Transaction — left side shows independent Create Read Update Delete operations; right side shows related writes grouped as one all-or-nothing unit](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/masterclasses/sdai2606/session04/session04-03-crud-vs-transaction.png?v=20261101)

| Point | Simple CRUD query | Transaction |
|---|---|---|
| **Typical size** | Often one statement: one insert, one select, one update, or one delete | One or many statements grouped as one business unit |
| **Success meaning** | “This one statement ran” | “The whole business action finished correctly” |
| **Failure meaning** | That one statement failed | All related changes in the unit are discarded (**rollback**) |
| **Best for** | Independent facts: save profile name, read a product list | Related facts: debit + credit, order + stock, booking + seat |
| **User mental model** | “Change this one thing” | “Complete this one job end to end” |
| **Risk if misused** | Wrong single row; usually limited blast radius | Half-finished multi-step business state if you skip the transaction |

**Need:** Students often think “I already know SQL insert/update, so I know safe systems.” CRUD teaches the verbs. Transactions teach **when several verbs must succeed together**.

**Logic:** A single `UPDATE students SET phone = ... WHERE id = 12` is usually enough as plain CRUD. A payment that needs two balance updates is not “two separate CRUD calls” in the business sense — it is one **transaction**.

**Common doubt:** “Is every CRUD operation also a transaction?”  
A single statement is often atomic by itself inside the database engine. The product danger appears when **your business action needs several statements** that must succeed together. That is when you must open an explicit transaction boundary.

**Common doubt:** “If I wrap every tiny read in a long transaction, is that safer?”  
Not automatically. Over-long transactions hold locks, slow other users, and can create new failures. Use transactions where **related writes** define one business action.

**Activity — Label CRUD or Transaction:**  
For each, write C or T: (1) read a menu of snacks, (2) update only your profile email, (3) place an order and reduce stock together, (4) delete one expired OTP row, (5) transfer wallet money between two accounts. Expected: C, C, T, C, T.

CRUD and transactions are both used in real apps. The next question is whether every application needs only one of them.

---

## Does Every App Need Only Transactions, or Only CRUD?

No serious product is “CRUD only forever” or “transaction for every click.” Most applications use **both**, for different kinds of work.

- **Official Definition:** An application’s **write pattern** is how it changes data: independent single-row changes versus multi-step business operations that must stay consistent.
- **In Simple Words:** Some clicks change one fact. Some clicks change a set of facts that must stay together.
- **Real-Life Example:** Editing your display name on a campus app is usually simple CRUD. Paying fees that update wallet, fee status, and receipt together needs a transaction.

| App style | Mostly enough | Where transactions still appear |
|---|---|---|
| Simple notes / personal todo on one device | Typical CRUD | Rare, unless syncing multiple stores |
| College club member list | CRUD for add/edit/remove members | Transaction if “add member + create welcome dues invoice” must be atomic |
| Catalogue / brochure site with admin edits | CRUD for content | Transaction if publish updates many related pages/rows together |
| Ecommerce / food delivery / tickets / UPI | CRUD for reads and simple profile edits | Transactions for checkout, payment, inventory, booking |
| Banking / wallets / ledgers | CRUD for statements and profile reads | Transactions for almost every money movement |

**Decision guide**

- Use **typical CRUD** when the business meaning is one independent fact, and a failed write does not leave another table lying.
- Use a **transaction** when two or more changes must stay true together, or when concurrent users can corrupt the same stock, seat, or balance.
- Do **not** force a heavy multi-statement transaction around every harmless `SELECT` of a public menu.
- Do **not** split a money or booking flow into unprotected CRUD calls just because each call “looks simple.”

**Need:** Teams waste time either over-engineering every read as a giant transaction, or under-protecting checkout as “just two updates.”

**Logic:** Ask one question for each feature: “If step 1 succeeds and step 2 fails, is the product still honest?” If no, you need a transaction. If yes, plain CRUD may be enough.

**Common doubt:** “My app is small, so I can skip transactions.”  
Small apps become real products when money, seats, marks, or stock appear. Size does not remove the rule. The **data relationship** decides.

**Common doubt:** “If the framework auto-saves models, I am safe.”  
Auto-save of one object is still one CRUD write. Related objects saved in separate auto-commits can still leave half-updates.

**Activity — Feature triage:**  
List five features of a campus food app (view menu, edit profile phone, place order, admin change price, refund after cancel). Mark each CRUD or Transaction. Expected lean: view menu = CRUD, edit phone = CRUD, place order = Transaction, change price = CRUD (unless price + audit log must be atomic), refund after cancel = Transaction.

Knowing when to use a transaction is step one. Next come the two endings of every transaction: **commit** and **rollback**.

---

## Commit and Rollback

Every transaction ends in one of two decisions: **commit** or **rollback**.

- **Official Definition:** **Commit** makes all changes in the current transaction **permanent** in the database.
- **In Simple Words:** “Stamp the draft as final.”
- **Real-Life Example:** The bank officer stamps the transfer slip. The new balances are now the official record.

- **Official Definition:** **Rollback** **cancels** all changes made in the current transaction and restores the previous consistent state.
- **In Simple Words:** “Throw the draft away. Pretend those half-edits never happened.”
- **Real-Life Example:** The officer finds a wrong account number and tears up the slip before stamping. Both accounts stay as they were.

**Need:** Success must be final. Failure must leave no scars. Commit and rollback are those two doors.

**Logic:** Code that changes data should decide: if every rule passed, commit; if any rule failed, rollback. Do not leave a transaction open forever.

| Outcome | Database action | After-effect |
|---|---|---|
| All steps valid | **COMMIT** | New values are visible and durable |
| Any step invalid or crash before success | **ROLLBACK** | Old values remain; no half-update |
| Long idle open transaction | Risk of locks and blocked users | Other requests may wait |

**Common doubt:** “Rollback deletes the whole table.”  
No. It undoes only **uncommitted** changes of **that** transaction. After **commit**, you cannot rollback; a bad commit needs a new compensating action such as a refund.

**Edge case — timeout after commit:**  
The network drops after commit. The phone shows an error, but money already moved. Blind retry can double-charge unless the system uses a unique payment or request id.

**Edge case — crash before commit:**  
Power fails mid-transaction. On recovery, uncommitted work is rolled back. That is safer than keeping half-written balances.

**Edge case — success screen before commit:**  
If the app shows “Paid” before commit, a later rollback makes the screen lie. Confirm only after commit, and let a status check by id reveal the truth after refresh.

**Activity — Commit or rollback?**  
Write C or R: (1) debit and credit both succeeded, (2) credit failed a rule check, (3) seat reserved then booking insert errored, (4) all steps stamped. Expected: C, R, R, C.

Commit and rollback answer success and failure. **ACID** names the four promises that make transactions trustworthy.

---

## ACID Properties Overview

**ACID** is the classic checklist for reliable transaction behaviour in databases.

- **Official Definition:** **ACID** stands for **Atomicity**, **Consistency**, **Isolation**, and **Durability** — four properties that define a reliable transaction.
- **In Simple Words:** All-or-nothing, rules respected, concurrent users do not corrupt each other, and saved work survives a crash.
- **Real-Life Example:** A sealed exam answer booklet: either the full booklet is submitted, rules of the exam hold, two students do not overwrite each other’s sheets, and once submitted the copy is kept safely.

![ACID properties as four pillars — Atomicity, Consistency, Isolation, and Durability supporting a reliable database transaction](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/masterclasses/sdai2606/session04/session04-04-acid-four-pillars.png?v=20261101)

| Letter | Property | One-line promise |
|---|---|---|
| **A** | Atomicity | All steps succeed, or none remain |
| **C** | Consistency | Rules and valid state are preserved |
| **I** | Isolation | Concurrent work does not create dirty mixed results |
| **D** | Durability | After commit, data survives restart |

**Need:** Without these promises, “transaction” is only a word. Products that move money, seats, and grades need all four.

**Logic:** Learn each property separately, then connect them. Real bugs often break one property while the others look fine.

The next four headings unpack each letter with edge cases and product examples.

---

## Atomicity: All or Nothing

**Atomicity** is the “all or nothing” promise.

- **Official Definition:** **Atomicity** means a transaction’s operations are indivisible: either every change is committed, or every change is rolled back.
- **In Simple Words:** No permanent half-work.
- **Real-Life Example:** Either the full UPI transfer completes, or both wallets stay as before — not “money left your wallet and vanished.”

**Why it matters:** Business actions are multi-step. Atomicity matches the user’s idea of one action.

| Edge case | What can go wrong without atomicity | Safe behaviour |
|---|---|---|
| Second write fails | First write stays | Full rollback |
| App process dies mid-way | Partial rows remain | Uncommitted work discarded |
| Developer catches error but forgets rollback | Draft may linger or later commit wrongly | Explicit rollback on failure path |
| Retry after unknown failure | Duplicate second attempt | Design with unique keys / idempotent payment ids |

**Real-life application:** Wallet debit + merchant credit; order create + stock reduce; booking create + seat lock.

**Common doubt:** “If atomicity fails, is the database broken?”  
Often the **application** failed to use a transaction. The database can only protect what you put inside one transaction boundary.

**Activity — Atomic checklist:**  
Write two writes for “return a product and refund wallet.” Mark them as one atomic unit. Add one line: “If refund insert fails, stock restore must also undo.”

Atomicity stops half-saves. **Consistency** stops saves that break the rules of the data.

---

## Consistency: Rules Must Still Hold

**Consistency** means the database moves from one **valid** state to another **valid** state.

- **Official Definition:** **Consistency** means a transaction brings the database from one state that satisfies defined rules to another state that still satisfies those rules.
- **In Simple Words:** After the transaction, constraints and business rules still hold.
- **Real-Life Example:** A classroom attendance total cannot exceed the number of enrolled students. A transfer cannot leave a “no overdraft” account negative if that rule exists.

**Why it matters:** Atomicity can still commit nonsense if your rules are wrong or missing. Consistency asks: “Is the result allowed?”

Rules come from:

- **Database constraints:** primary keys, foreign keys, `NOT NULL`, `CHECK`, unique indexes
- **Application rules:** “balance must stay ≥ 0,” “order total must equal sum of line items”

| Edge case | Broken consistency looks like | Guard |
|---|---|---|
| Negative wallet after transfer | Rule not checked | Constraint or app check inside transaction |
| Orphan booking with no user id | Foreign key missing | Foreign key + transaction |
| Stock count −1 | Oversell under load | Check stock before commit; proper isolation |
| Two primary keys same id | Duplicate identity | Unique / primary key constraint |

**Real-life application:** Fee payment must keep `amount_paid = fee_due` for that challan, or create a clear partial-payment state that the schema allows — not a silent mismatch.

**Common doubt:** “Does the database invent business rules for me?”  
No. You define constraints and code checks. Consistency means the transaction respects the rules you declared.

**Activity — Name one rule:**  
For a food-delivery cart checkout, write one consistency rule (example: “paid amount must equal cart total”). Write what the system should do if the rule fails: rollback.

Even with good rules, two users can interfere. That is **Isolation**.

---

## Isolation: Concurrent Users Must Not Corrupt Each Other

**Isolation** controls what one transaction can see of another transaction’s uncommitted or in-progress work.

- **Official Definition:** **Isolation** means concurrent transactions do not interfere in ways that produce incorrect intermediate reads or lost updates, according to the chosen isolation level.
- **In Simple Words:** Two people editing related data should not create a mixed, wrong result.
- **Real-Life Example:** Two passengers trying to book the last seat. Only one booking should win. The other should see “sold out,” not both getting the same berth.

**Why it matters:** Real systems have many requests at once. Without isolation, race conditions appear.

Important race ideas:

- **Dirty read:** Reading another transaction’s uncommitted draft
- **Lost update:** Two transactions read the same value, both write, last write silently overwrites the other
- **Non-repeatable read:** Reading the same row twice in one transaction and getting different committed values
- **Phantom read:** A second query sees new rows that appeared from another commit

| Edge case | Example | What you want |
|---|---|---|
| Last seat double book | Two commits both see seat free | One succeeds; one fails or waits |
| Stock oversell | Two orders read stock = 1 | Only one order commits |
| Wallet race | Two spends read same balance | Serialised updates or locked row |
| Report mid-transfer | Report reads after debit before credit | Isolation so reports do not trust dirty drafts |

**Real-life application:** IRCTC last seat, flash-sale stock on Flipkart, UPI balance under two rapid spends, exam marksheet update while a result PDF is generated.

**Common doubt:** “Can isolation mean nobody else can use the database?”  
No. Databases use locks and isolation levels so many transactions run, but conflicting ones wait or fail safely.

**Common doubt:** “Do I need to memorise every isolation level now?”  
For this lesson, remember the goal: concurrent work must not create wrong business results. Exact level names deepen later when you tune performance.

**Activity — Last seat race:**  
Student A and Student B both try to book seat S1 at the same millisecond. Write the safe outcomes (one booked, one rejected). Write the unsafe outcome (both booked). Circle Isolation as the property that prevents the unsafe outcome.

After commit, the result must survive a restart. That is **Durability**.

---

## Durability: Committed Data Survives Failure

**Durability** means a successful commit is not forgotten when the machine restarts.

- **Official Definition:** **Durability** means once a transaction has committed, its changes remain permanent even after power loss, crash, or restart.
- **In Simple Words:** “Saved” really means saved to durable storage, not only RAM.
- **Real-Life Example:** After a bank SMS says “₹500 debited,” a branch power cut should not erase that debit from the official ledger.

**Why it matters:** Users trust confirmation messages. If committed data vanishes on reboot, trust collapses.

| Edge case | Risk | Durable behaviour |
|---|---|---|
| Server restarts after commit | In-memory only data lost | Commit flushed to disk / durable store |
| Confirm shown before commit | User thinks success; data rolled back | Confirm only after commit |
| Disk full at commit | Commit may fail | Fail loudly; do not pretend success |
| Backup restore to old time | Recent commits missing | Recovery plans and backups are operations topics; durability is about the commit itself surviving normal crash recovery |

**Real-life application:** After fee payment success, the paid status must remain after server maintenance. After ticket booking success, the PNR must still exist tomorrow.

**Common doubt:** “Is durability the same as backup?”  
Related but not identical. Durability is about surviving normal crash recovery after commit. Backups protect against wider disasters and human mistakes. You will see backup practice again in the security section.

**Activity — Trust the SMS?**  
Write yes/no: Should a payment SMS be sent before commit? Expected: no. Send after successful commit (or based on a status that is already committed).

Atomicity, Consistency, Isolation, and Durability together explain why backends wrap dangerous writes carefully.

---

## Why Backend APIs and ORMs Rely on Transactions

A **backend API** receives a request, applies rules, and writes to the database. An **ORM** (Object-Relational Mapper) is a library that lets application code work with tables through objects while still talking SQL underneath.

- **Official Definition:** An **ORM** maps programming objects to database tables and rows, and often provides helpers to begin, commit, and rollback transactions.
- **In Simple Words:** The ORM is a translator between app code and SQL, including “start transaction / finish transaction” helpers.
- **Real-Life Example:** Instead of writing raw SQL for every student row, the app says “save this Student object,” and the ORM generates SQL — ideally inside a safe transaction when many objects change together.

**Need:** APIs often do several writes per request. Frameworks and ORMs therefore expose transaction helpers so developers do not forget the boundary.

**Logic:** Safe pattern for a write API:

1. Begin transaction
2. Validate rules
3. Perform all related writes
4. If anything fails → rollback and return error
5. If all succeed → commit and return success

| Layer | Transaction role |
|---|---|
| **Frontend** | Sends one user intent (pay, book, place order) |
| **Backend API** | Starts the transaction, checks rules, decides commit/rollback |
| **ORM / DB client** | Issues `BEGIN`, statements, `COMMIT` / `ROLLBACK` |
| **Database** | Enforces ACID for that unit of work |

**Common doubt:** “If I use an ORM, am I automatically safe?”  
No. You must still group related writes in one transaction. An ORM that auto-commits each `save()` separately can still create half-updates.

**Common doubt:** “Can the frontend start a database transaction?”  
The browser must not hold database credentials or open DB transactions. The **backend** owns that boundary. That rule is also a **security** rule, not only an architecture preference.

**Edge cases backends must plan for:**

- Request timeout while transaction is open → rollback and release locks
- Duplicate submit (double click Pay) → idempotency keys so one business payment commits once
- Partial external side effect (SMS sent, DB rolled back) → send notifications after commit
- Long transaction holding locks → keep transactions short; do heavy non-DB work outside

**Real-life application:** A checkout API that creates order rows, reduces stock, and records payment intent must wrap those DB writes together. A marks API that updates subject marks and total must not leave totals stale.

**Activity — API boundary sketch:**  
On paper, draw four boxes: Frontend, API, ORM/DB client, Database. Put a star only on API + Database for “who owns commit/rollback.” Write one sentence: “The Pay button asks; the backend decides; the database stamps.”

Correct transactions keep data honest. Security practices keep data **out of the wrong hands** and recoverable after disaster.

---

## Security Practices for Databases and Backend Apps

A correct transaction still fails the product if anyone on the internet can open the database and run free SQL. Reliability and security must travel together.

- **Official Definition:** **Database and backend security** is the set of controls that limit who can see or change data, how they may access it, and how the organisation recovers when something goes wrong.
- **In Simple Words:** Lock the ledger room, give each staff only the keys they need, never let customers walk into the vault, and keep photocopies of the ledger on a schedule.
- **Real-Life Example:** A bank customer uses the app or counter. The customer does not get the branch database password. Staff roles differ: teller, auditor, admin.

### No direct client queries — everything goes through the API

- Browsers, mobile apps, and outside scripts must **not** receive the main database username and password.
- The client sends an **API request** (“place order”, “update phone”). The **backend** checks identity and permission, then talks to the database.
- Direct SQL from the client bypasses business rules, role checks, and audit trails.

![Clients talk to the API not the database — frontend reaches Backend API safely, while a direct SQL path from the app to the private database is blocked](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/masterclasses/sdai2606/session04/session04-05-api-owns-database.png?v=20261101)

**Need:** If the database port and password are in the app, a curious or hostile user can read or wipe tables.

**Logic:** The API is the only public door. The database stays on a private network path that only the backend can use.

| Bad pattern | Safer pattern |
|---|---|
| Mobile app embeds DB password | App calls HTTPS API with user login token |
| Student project opens DB to `0.0.0.0` on the internet | DB accepts connections only from backend servers |
| “Temporary” SQL admin page on production | Admin tools behind strong auth, VPN, or private access |

### Role-based CRUD — not everyone needs full Create, Read, Update, Delete

- **Official Definition:** **RBAC** (Role-Based Access Control) gives each user or service only the actions their role requires.
- **In Simple Words:** A reader is not an editor. An editor is not a billing admin. An intern is not a production root user.
- **Real-Life Example:** In a campus portal, students read their own marks; teachers update marks for their courses; only exam cell staff can publish finals; nobody casual gets `DELETE` on the whole marks table.

Apply RBAC at **two layers**:

1. **Application roles:** student, teacher, admin, support agent — checked in the API before any write.
2. **Database roles:** the backend’s DB user itself should have least privilege (for example, no permission to drop schemas in production).

| Role example | Allowed | Not allowed |
|---|---|---|
| End user | Read own profile; create own order through API | Read other users’ rows; raw SQL; delete catalogue |
| Support agent | Read selected customer fields; limited status updates | Export whole database; change prices globally |
| Analytics reader | Read from **replica** views | Write to primary; delete; change passwords |
| DB admin (break-glass) | Migrations and emergency repair with audit | Daily app traffic; shared laptop login |

**Common doubt:** “Our team is small, so one shared admin DB user is fine.”  
Shared god-mode users make accidents and breaches worse. Prefer named access, least privilege, and short-lived admin elevation.

### Primary database vs replica — where work should run

- **Official Definition:** The **primary** (main) database accepts authoritative **writes**. A **replica** is a copy kept in sync mainly for **reads**, reporting, and safety workloads.
- **In Simple Words:** The main ledger takes the official stamps. The photocopy machine’s copies are for reading and analysis, not for inventing new official stamps.
- **Real-Life Example:** Checkout writes go to the primary. Heavy “sales dashboard for last year” queries run on a replica so they do not slow payments.

![Primary replica and backups — Backend API writes to Primary, syncs to Replica for reads and reports, and keeps encrypted backups on a frequent schedule](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/masterclasses/sdai2606/session04/session04-06-primary-replica-backup.png?v=20261101)

Practical rules:

- **Business writes** (Create/Update/Delete that change truth) go to the **primary** through the backend API — never from random laptops as free SQL on production.
- **Heavy reads, reports, data science exploration, and practice queries** should use a **replica** or a non-production copy — not the live primary under customer load.
- Do **not** treat a replica as a second place to “quickly fix” production money rows. Fixes still go through controlled primary write paths.
- Never point student experiments, BI tools with broad access, or one-off scripts at the production primary if a replica or staging DB exists.

**Need:** One expensive report on the primary can lock or slow the same database that is taking UPI traffic.

**Logic:** Separate “change the truth” from “study the truth.”

### Frequent backup and sync discipline

- **Official Definition:** A **backup** is a recoverable copy of data taken on a schedule so the organisation can restore after deletion, corruption, ransomware, or cloud failure.
- **In Simple Words:** Photocopy the ledger on a timetable, store copies safely, and practise opening a photocopy before you need it in a fire.
- **Real-Life Example:** Nightly full backups plus more frequent incremental backups; some teams also keep continuous WAL/point-in-time recovery for databases.

Good backup habits:

- Schedule **frequent** backups appropriate to how painful data loss is (money systems need tighter recovery points than a static brochure).
- Store backups in a **separate** account/region when possible so one breach or one bill lapse does not delete both live data and backups.
- **Encrypt** backups and restrict who can download them.
- **Test restore** on a schedule. An untested backup is a hope, not a plan.
- Keep retention (how many days/weeks of copies you keep) written down for the team.

**Common doubt:** “The cloud already replicates disks, so I do not need backups.”  
Replication copies damage too (bad delete, ransomware encrypt). Backups are for recovery to an earlier good time.

### Other essential security practices

| Practice | What it means | Why it matters |
|---|---|---|
| **Least privilege** | Every user and service gets the minimum rights needed | Limits blast radius of a stolen password |
| **Secrets management** | DB URLs, API keys, and admin tokens stay in env/secrets stores — not in Git, screenshots, or frontend code | Leaked repos are a common breach start |
| **TLS / HTTPS** | Encrypt data in transit between client, API, and DB connections | Stops casual network sniffing |
| **Encryption at rest** | Disks and backups encrypted | Harder to use stolen disk images |
| **Parameterized queries / ORM binds** | User input never concatenated into raw SQL strings | Blocks classic **SQL injection** |
| **Input validation** | API rejects impossible or oversized payloads early | Reduces junk writes and some attack paths |
| **Authentication + session/token expiry** | Prove who the caller is; expire tokens | Stolen old tokens should die |
| **Audit logs** | Record who changed sensitive rows and when | Needed after incidents and for compliance |
| **Rate limiting** | Cap repeated failed logins and heavy APIs | Slows password guessing and abuse |
| **Private networking** | DB not publicly open; security groups / firewall allow only backend | Shrinks internet attack surface |
| **Environment separation** | Dev, staging, production are different projects/credentials | Experiments do not erase live customers |
| **Dependency and patch hygiene** | Update frameworks and DB engines | Old unpatched software is a favourite entry door |
| **Safe error messages** | Clients see “payment failed,” not full SQL/stack traces | Error detail helps attackers map your system |

**Activity — Security checklist for one feature:**  
Pick “student updates phone number.” Write five controls you expect: login required, can update only own row, API only (no direct SQL), validate phone format, audit log of the change. Star any control your mental design was missing.

Security rules are easier to remember when you see what happens when teams skip them.

---

## Real Incidents: Data Leaks and Compromised Systems

These summaries are for learning. They are not attack recipes. The pattern to notice is always the same: weak access control, exposed credentials, unpatched software, or missing recovery discipline.

### Equifax (2017) — unpatched software, massive personal data exposure

- **What happened (public reporting):** Attackers exploited a known vulnerability in a web application component that had not been patched in time. Personal data of a very large number of people was exposed.
- **Lesson for builders:** Patching and inventory of internet-facing apps are security work, not optional chores. A database behind a weak edge app is still at risk.

### Capital One (2019) — cloud misconfiguration

- **What happened (public reporting):** A misconfigured web application firewall / cloud access path allowed an outsider to obtain data from cloud storage connected to the company’s systems.
- **Lesson for builders:** Cloud defaults and overly broad IAM roles can open the vault without “hacking the database password” in the old sense. Least privilege applies to cloud roles too.

### Uber (2016 breach and response failures) — stolen credentials, poor disclosure

- **What happened (public reporting):** Attackers used stolen cloud credentials (reportedly found via a private code repo pattern) to access user data. The company’s handling and disclosure later drew heavy criticism and legal consequences.
- **Lesson for builders:** Secrets in code repositories are gold for attackers. Incident honesty and containment matter as much as the first intrusion.

### LinkedIn (password dumps over years) — credential stuffing forever

- **What happened (public reporting):** Large sets of LinkedIn account credentials appeared in dumps after breaches; attackers reuse those emails/passwords on other sites.
- **Lesson for builders:** Hash passwords properly, support multi-factor authentication, and never assume users have unique passwords. Your API login is part of database security because it gates data access.

### Air India / SITA (2021) — airline passenger data through a vendor platform

- **What happened (public reporting):** Passenger data linked to Air India was affected through a breach at SITA, a widely used aviation IT provider. Data such as contact and passport-related fields were reported at risk depending on records.
- **Lesson for builders:** Vendors and integrations expand your trust boundary. Third-party access to data must be contractual, logged, and least-privilege — the same mental model as RBAC inside your own API.

### Domino’s Pizza India (2021 reporting) — large customer dataset allegedly exposed

- **What happened (public reporting):** Security researchers and news outlets reported that a very large set of customer records related to Domino’s India appeared exposed / circulating, raising questions about how customer databases were protected.
- **Lesson for builders:** Customer phone numbers and order history are valuable. API-only access, role limits, and monitoring for bulk export matter for “ordinary” commerce apps, not only banks.

### Common thread across incidents

| Weakness seen again and again | Safer habit from this lesson |
|---|---|
| Public or weakly protected data stores | No direct client DB access; private networking |
| Shared or leaked credentials | Secrets management; rotate keys; no secrets in Git |
| Too much privilege for one role | RBAC at API and DB layers |
| Unpatched edge software | Patch hygiene and dependency updates |
| No reliable restore story | Frequent backups, separate storage, tested restore |
| Heavy tools aimed at live primary | Replicas / staging for analytics and experiments |

**Activity — Map an incident to a control:**  
Choose one incident above. Write one sentence: “This risk shrinks if we enforce ___.” Fill with a control from the security section (for example, least privilege, no secrets in Git, patching, API-only access).

Correctness (ACID) and safety (security) now sit side by side. Use the product map below before the optional practice.

---

## Putting It Together for Real Products

| Product moment | Without transactions | With ACID transactions | Security companion |
|---|---|---|---|
| UPI transfer | Money can vanish mid-way | Atomic debit+credit; durable after commit | API-only; strong auth; audit |
| Last seat book | Double booking possible | Isolation + constraints; one winner | Role checks; rate limits |
| Checkout + stock | Oversell or orphan order | One unit; rollback on rule fail | No direct SQL from app |
| Fee paid + receipt | Paid without proof row | Both rows commit together | Least privilege staff roles |
| Marks + total | Total stale after subject save | Update both in one transaction | Teachers update only own courses |
| Sales dashboard | Slows checkout if on primary | Reads can stay simple CRUD selects | Run on **replica**, not primary writes |
| Profile email edit | Usually fine as one UPDATE | Transaction optional unless paired logs required | User can edit only own row |

**Common doubt:** “Should every `SELECT` be a transaction?”  
Reads can use transactions for consistent reports. The urgent need is **multi-step writes**. Major relational databases share the ACID idea even when command defaults differ.

**Decision postcard to keep**

1. Independent single fact → typical **CRUD** through API  
2. Related facts / money / stock / seats → **transaction** through API  
3. Who may do which CRUD → **RBAC**  
4. Where heavy reads run → **replica**  
5. How we survive wipe/ransomware → **frequent tested backups**

---

## Optional Implementation: Supabase SQL Editor

This practice is **optional**. Use it only if you want to feel `BEGIN` / `COMMIT` / `ROLLBACK` once in a browser. You will not build an app here.

- **Official Definition:** **Supabase** is a backend platform that provides a hosted **PostgreSQL** database and tools such as a browser **SQL Editor**.
- **In Simple Words:** An online database project with a page where you type SQL and run it.
- **Real-Life Example:** Like using a training ledger screen to try a draft transfer, then stamp it or tear it up — without building a mobile app.

- **Official Definition:** **PostgreSQL** is a relational database that supports standard transaction commands such as `BEGIN`, `COMMIT`, and `ROLLBACK`.
- **In Simple Words:** The engine behind many serious apps; Supabase hosts it for you.
- **Real-Life Example:** The same family of SQL ideas used for wallets, bookings, and orders in production systems.

**Safety note for the optional practice:** Use a **learning / demo project**, not a live production customer database. Optional classroom SQL still follows the spirit of “do not experiment on the main production vault.”

### Setup once

1. Open your Supabase project in the browser.
2. Go to **SQL Editor**.
3. Run the setup script below to create a tiny wallet table and two rows.

```sql
-- Create a simple wallet table for the demo
CREATE TABLE IF NOT EXISTS wallet_demo (
  account_name TEXT PRIMARY KEY, -- unique name for each wallet
  balance INTEGER NOT NULL CHECK (balance >= 0) -- money cannot go negative
);

-- Remove old demo rows if you re-run setup
DELETE FROM wallet_demo;

-- Seed two wallets with clear starting balances
INSERT INTO wallet_demo (account_name, balance) VALUES
  ('Riya', 1000), -- sender starts with 1000
  ('Aman', 200);  -- receiver starts with 200
```

**How the code works**

- `CREATE TABLE` makes a tiny ledger with a name and a balance.
- `CHECK (balance >= 0)` supports **consistency**: negative money is rejected.
- `DELETE` then `INSERT` gives a clean starting point for the demos.
- After setup, Riya has 1000 and Aman has 200.

**Activity — Confirm seed:**  
In SQL Editor run `SELECT * FROM wallet_demo ORDER BY account_name;` and confirm two rows.

### Demo A — Commit a full transfer

Transfer ₹100 from Riya to Aman inside one transaction, then commit.

```sql
-- Start one protected unit of work
BEGIN;

-- Step 1: take 100 from Riya
UPDATE wallet_demo
SET balance = balance - 100
WHERE account_name = 'Riya';

-- Step 2: give 100 to Aman
UPDATE wallet_demo
SET balance = balance + 100
WHERE account_name = 'Aman';

-- Make both steps permanent together
COMMIT;
```

**How the code works**

- `BEGIN` opens the transaction draft.
- Both `UPDATE` statements belong to the same unit.
- `COMMIT` stamps both changes. Expected balances: Riya 900, Aman 300.

### Demo B — Rollback after a failed rule

First reset balances (run alone):

```sql
-- Reset demo balances before the failure demo
UPDATE wallet_demo SET balance = 1000 WHERE account_name = 'Riya';
UPDATE wallet_demo SET balance = 200 WHERE account_name = 'Aman';
```

Then run this block. The illegal debit should error:

```sql
-- Start a new protected unit
BEGIN;

-- Attempt an unsafe debit that would make balance negative
UPDATE wallet_demo
SET balance = balance - 5000
WHERE account_name = 'Riya';
```

If the SQL Editor stops on the error, run this next:

```sql
-- Clear the aborted transaction before any new work
ROLLBACK;
```

**How the code works**

- The debit would make Riya’s balance negative, so `CHECK (balance >= 0)` rejects it.
- PostgreSQL marks the open transaction aborted until you roll back.
- After `ROLLBACK;`, select again: Riya 1000, Aman 200. No half-transfer remains.

### Demo C — See half-work avoided

```sql
-- Prove final state after demos
SELECT account_name, balance
FROM wallet_demo
ORDER BY account_name;
```

**How the code works**

- A plain `SELECT` shows the committed truth.
- You should not see a world where Riya lost money and Aman gained nothing from Demo B.

**Activity — Narrate one run:**  
In your notebook write: “BEGIN → two updates → COMMIT means ___.” Then: “Error or bad rule → ROLLBACK means ___.” Fill with “both saved” and “both discarded.”

If you skip this optional practice, you can still master the lesson through the definitions, tables, and notebook activities above.

---

## Key Takeaways

- Multi-step business updates without protection can leave **partial**, incorrect data even when the user sees an error.
- **CRUD** is the basic create/read/update/delete toolbox. A **transaction** groups related changes into one unit that ends with **commit** or **rollback**.
- Not every feature needs a heavy transaction, and not every app can survive on unprotected CRUD alone — choose by whether related facts must stay honest together.
- **ACID** means **Atomicity**, **Consistency**, **Isolation**, and **Durability**.
- **Backend APIs** and **ORMs** own multi-step writes; the frontend only sends intent.
- Security essentials: **no direct client SQL**, **API-only access**, **RBAC**, **primary vs replica** discipline, **frequent tested backups**, secrets hygiene, TLS, parameterized queries, and least privilege.
- Real breaches often start with exposed credentials, over-broad access, unpatched edges, or missing recovery — not with “ACID theory forgotten” alone.
- The Supabase SQL Editor walkthrough is an **optional** way to feel commit and rollback on a demo wallet table.

These ideas prepare you for backend lessons where APIs create orders, payments, and bookings against a shared database. Whenever a feature changes data, ask both: which ACID promise protects correctness, and which security control protects access and recovery?

---

## Important Commands, Libraries, Terminologies Used

| Term / Idea | Meaning (quick revision) |
|---|---|
| **CRUD** | Create, Read, Update, Delete — basic data operations |
| **Multi-step update** | One business action that needs several related writes |
| **Transaction** | All-or-nothing unit of database work |
| **BEGIN** | Start a transaction draft |
| **COMMIT** | Make the draft permanent |
| **ROLLBACK** | Discard the draft; restore prior state |
| **ACID** | Atomicity, Consistency, Isolation, Durability |
| **Atomicity** | All steps succeed, or none remain |
| **Consistency** | Rules and valid state still hold after the transaction |
| **Isolation** | Concurrent transactions do not create corrupted results |
| **Durability** | After commit, data survives restart |
| **Dirty read / lost update** | Reading uncommitted data / silent overwrite races |
| **Constraint / CHECK** | Database rule that rejects invalid values |
| **Backend API** | Server program that owns rules, commit/rollback, and access checks |
| **ORM** | Object-to-table helper; still needs explicit transaction grouping |
| **Idempotency** | Retrying the same request does not double-apply the business action |
| **RBAC** | Role-based access — only needed CRUD per role |
| **Primary DB** | Authoritative database for writes |
| **Replica** | Synced copy used mainly for reads, reports, safer exploration |
| **Backup / restore test** | Scheduled recoverable copies; restore must be practised |
| **Least privilege** | Minimum rights for each user or service |
| **SQL injection defence** | Parameterized queries / bound ORM values — no string-glued SQL |
| **Secrets management** | Keep DB passwords and keys out of Git and frontend |
| **Supabase SQL Editor** | Optional browser tool to run SQL on hosted PostgreSQL |
| **PostgreSQL** | Relational database used by Supabase for the optional demo |
| **wallet_demo** | Tiny practice table for commit/rollback demos |
