
##  HDFC Life Policy Claims Console

Create a **Java console application** that stores policies, calculates premium, files claims, and notifies channels when a claim status changes.

Use this seed data (create all 6 policies **only** through `PolicyFactory`):

```text
HDFC-LIFE-1001 | Anita Sharma  | TERM       | 18500 | Active
HDFC-LIFE-1002 | Rahul Mehta   | ULIP       | 42000 | Active
HDFC-LIFE-1003 | Priya Nair    | ENDOWMENT  | 27000 | Lapsed
HDFC-LIFE-1004 | Vikram Singh  | TERM       | 15200 | Active
HDFC-LIFE-1005 | Sneha Patel   | ULIP       | 36000 | Active
HDFC-LIFE-1006 | Anita Sharma  | ENDOWMENT  | 22000 | Pending
```

Plain Java only. No Spring. Compile and run with `javac` / `java`, or Maven/Gradle if you already use it. Do not use Java Streams.

---

### 1. Collections

Keep data in a store class and use **all** of these:

| Collection | Use |
|---|---|
| `ArrayList` | All policies |
| `HashSet` | Unique customer names |
| `HashMap` | Lookup policy by policy number |
| `TreeMap` | Policies sorted by policy number |
| `PriorityQueue` | Claims ordered by urgency (`HIGH` before `MEDIUM` before `LOW`) |

Print all policies using an **Iterator** (not only for-each).

---

### 2. SOLID

Split work across focused classes. Do not put store, premium math, claim filing, and notifications in one class.

- **SRP:** `PolicyStore`, `PremiumCalculator`, `ClaimService`, `AuditLogger` each do one job  
- **OCP:** a new premium type can be added without editing `PremiumCalculator`  
- **LSP:** any `PremiumStrategy` can be swapped in and still work  
- **ISP:** observers implement a small `ClaimObserver` interface with **one** method  
- **DIP:** `ClaimService` depends on abstractions (`PremiumStrategy`, `ClaimObserver`), not concrete classes  

---

### 3. Singleton

`AppConfig` must be a **thread-safe enum singleton** with:

- `companyName = "HDFC Life"`
- `maxClaimAmount = 500000`

Use `AppConfig.INSTANCE` everywhere. Do not write `new AppConfig()`.

---

### 4. Factory

`PolicyFactory.create(type, policyNo, customer, premium, status)` returns:

- `"TERM"` → `TermLifePolicy`
- `"ULIP"` → `UlipPolicy`
- `"ENDOWMENT"` → `EndowmentPolicy`

Unknown type → throw `UnknownPolicyTypeException`.

---

### 5. Builder

Build a claim with a fluent **inner static Builder**.

**Required:** `policyNo`, `claimAmount`, `urgency`  
**Optional:** `hospitalName`, `remarks`  
**Initial status:** `SUBMITTED`

```java
Claim claim = new Claim.Builder("HDFC-LIFE-1001", 25000, Urgency.HIGH)
    .hospitalName("Apollo Hospital")
    .remarks("Hospitalisation")
    .build();
```

After build, the **only** allowed change is `updateStatus(...)`. Do not add setters for the other fields.

---

### 6. Strategy

Use integer percent (no `double`):

| Type | Rule |
|---|---|
| TERM | `basePremium * 100 / 100` |
| ULIP | `basePremium * 112 / 100` |
| ENDOWMENT | `basePremium * 108 / 100` |

`PremiumCalculator` holds a `PremiumStrategy` and can change it at runtime.

ULIP premium for `HDFC-LIFE-1002` must print **`47040`**.

---

### 7. Observer

When claim status changes, notify all registered observers.

- Subject: `ClaimEventPublisher`
- Interface: `ClaimObserver` with `onClaimUpdate(Claim claim)`
- Observers: `InAppNotifier` and `BranchLetterNotifier`

`main` must:

1. Register both observers  
2. File **three** claims: HIGH on `1001`, MEDIUM on `1002`, LOW on `1004`  
3. Call `updateStatus(APPROVED)` on the HIGH claim  
4. Show that **both** observers printed a notification  

---

### 8. Exception handling

All of these must extend **`RuntimeException`**:

```text
PolicyServiceException
  ├── PolicyNotFoundException
  ├── InvalidClaimException
  └── UnknownPolicyTypeException
```

- Missing policy number → `PolicyNotFoundException`  
- Claim amount `<= 0` or `> AppConfig.maxClaimAmount` → `InvalidClaimException`  
- Unknown factory type → `UnknownPolicyTypeException`  
- `AuditLogger` implements `AutoCloseable` and writes one line to `audit.log` using **try-with-resources**  
- If file write fails, wrap the IO exception in `PolicyServiceException` and **keep the cause**  
- Do not empty-catch. Print the exception message in `main`

`main` must also demonstrate all three failures:

- lookup `"HDFC-LIFE-9999"`  
- build/file a claim with amount `600000`  
- `PolicyFactory.create("INVALID", ...)`

---

### Suggested layout

```text
hdfc-life-policy-system/
  src/com/hdfclife/
    Main.java
    model/          Policy, TermLifePolicy, UlipPolicy, EndowmentPolicy, Claim, Urgency
    store/          PolicyStore
    config/         AppConfig
    factory/        PolicyFactory
    strategy/       PremiumStrategy, TermPremiumStrategy, UlipPremiumStrategy,
                    EndowmentPremiumStrategy, PremiumCalculator
    observer/       ClaimObserver, ClaimEventPublisher, InAppNotifier, BranchLetterNotifier
    service/        ClaimService, AuditLogger
    exception/      PolicyServiceException, PolicyNotFoundException,
                    InvalidClaimException, UnknownPolicyTypeException
  README.md
  .gitignore
```

---

### `main` must print (in this order)

1. Company name from `AppConfig` → `HDFC Life`  
2. All 6 policies (Iterator)  
3. Unique customer count → **`5`**  
4. Lookup `HDFC-LIFE-1004` → Vikram Singh  
5. `TreeMap` keys in sorted order  
6. ULIP premium for `HDFC-LIFE-1002` → **`47040`**  
7. Both observer messages after HIGH claim status → `APPROVED`  
8. PriorityQueue poll order → **HIGH, then MEDIUM, then LOW**  
9. Caught message for `"HDFC-LIFE-9999"`  
10. Caught message for claim amount `600000`  
11. Caught message for factory type `"INVALID"`  
12. A line in `audit.log` for a filed claim  

---

### Submission Guidelines

Submit the **GitHub repository link**.

- Push the full Java project (`src`, README, `.gitignore`)
- Repo must be **public**
- Do **not** commit `audit.log`, `.class` files, or `out/` / `bin/` / `target/`
- Submit the GitHub repo URL as your answer