## HDFC Life Policy Desk API

Create a **Spring Boot REST API** that stores HDFC Life policies in memory, exposes CRUD endpoints, documents them with **Springdoc**, and owns the **PostgreSQL-ready schema** through **Flyway**.

This is a **new project**. You do not need last week's repo.

Use **Spring Boot 3** and **Java 17**. Bootstrap with Spring Initializr (or the equivalent Maven/Gradle setup).

Allowed starters / libraries:

- `spring-boot-starter-web`
- `spring-boot-starter-validation`
- `spring-boot-starter-data-jpa` (for datasource auto-configuration only)
- `flyway-core`
- `com.h2database:h2` (runtime, `dev` profile)
- `org.postgresql:postgresql` (runtime, `prod` profile)
- `org.springdoc:springdoc-openapi-starter-webmvc-ui` (OpenAPI 3 / Swagger UI)

Do **not** use `@Entity`, `JpaRepository`, or Hibernate `ddl-auto` to create tables. Flyway owns the schema. REST data lives in an **in-memory store**.

Do **not** use field `@Autowired`. Use **constructor injection** only.

Do **not** put store logic inside a controller. Controllers call a service. The service depends on a `PolicyStore` **interface**.

---

### Seed data

Create all 6 policies **only** through `PolicyStore.add(...)` from a `CommandLineRunner` (not by hard-coding them inside the controller).

```text
HDFC-LIFE-1001 | Anita Sharma  | TERM       | 18500 | Active
HDFC-LIFE-1002 | Rahul Mehta   | ULIP       | 42000 | Active
HDFC-LIFE-1003 | Priya Nair    | ENDOWMENT  | 27000 | Lapsed
HDFC-LIFE-1004 | Vikram Singh  | TERM       | 15200 | Active
HDFC-LIFE-1005 | Sneha Patel   | ULIP       | 36000 | Active
HDFC-LIFE-1006 | Anita Sharma  | ENDOWMENT  | 22000 | Pending
```

Active policies → **`4`** (`1001`, `1002`, `1004`, `1005`).  
TERM policies → **`2`** (`1001`, `1004`).  
Unique customer names → **`5`**.

---

### 1. Spring Boot project, IoC and profiles

- Group: `com.hdfclife`  
- Artifact / root package: `com.hdfclife.desk`  
- Packaging: jar  
- Default profile: **`dev`**

`application.yml` (shared):

```yaml
spring:
  profiles:
    active: dev
  jpa:
    hibernate:
      ddl-auto: none
    open-in-view: false
```

`application-dev.yml`:

- H2 in-memory URL `jdbc:h2:mem:hdfclife;MODE=PostgreSQL;DB_CLOSE_DELAY=-1`
- H2 console enabled
- Flyway enabled
- `hdfc.company-name` = `HDFC Life`
- `hdfc.max-claim-amount` = `500000`

`application-prod.yml`:

- PostgreSQL URL / username / password from environment variables (`DB_URL`, `DB_USER`, `DB_PASSWORD`)
- `hdfc.company-name` = `HDFC Life Production`
- Flyway enabled

`HdfcProperties` must be a `@ConfigurationProperties(prefix = "hdfc")` class. Bind `companyName` and `maxClaimAmount`. Validate with `@NotBlank` / `@Min(1)` and `@EnableConfigurationProperties` (or `@Validated` on the properties class).

Register beans with stereotype annotations:

| Type | Annotation |
| ---- | ---------- |
| `InMemoryPolicyStore` | `@Repository` |
| `PolicyService` | `@Service` |
| `ClaimService` | `@Service` |
| `PolicyController` | `@RestController` |
| `ClaimController` | `@RestController` |

`PolicyService` constructor takes `PolicyStore` (the interface), not `InMemoryPolicyStore`.

One `@Component` `StoreLifecycle` must implement:

- `@PostConstruct` → print `PolicyStore ready`
- `@PreDestroy` → print `PolicyStore shutdown`

Do not use `@Autowired` on fields.

---

### 2. CommandLineRunner seed and startup print

A `DataSeeder` `CommandLineRunner` (constructor-injected `PolicyStore` + `HdfcProperties` + `Environment`) must:

1. Insert the six seed policies  
2. Print the lines in the **Startup print** section below  

If you run the app twice in the same JVM, do not insert duplicates. Check `count()` before seeding.

---

### 3. Springdoc / Swagger

Integrate Springdoc OpenAPI 3.

- Swagger UI must load at `/swagger-ui/index.html` (or the Springdoc default that redirects there)
- OpenAPI JSON at `/v3/api-docs`
- `PolicyController` and `ClaimController` each have `@Tag`
- Every handler method has `@Operation` and at least one `@ApiResponse`
- List-by-query methods have `@Parameter` on the request param

README must include a screenshot **or** a short note with the exact Swagger UI URL you opened.

---

### 4. REST controllers and services

Base path: `/api`.

JSON field names are **exact**. Use `int` for money. Do not use `double`.

**Policy JSON**

```json
{
  "policyNo": "HDFC-LIFE-1004",
  "customer": "Vikram Singh",
  "type": "TERM",
  "basePremium": 15200,
  "status": "Active"
}
```

**Claim JSON**

```json
{
  "claimNo": "CLM-01",
  "policyNo": "HDFC-LIFE-1001",
  "claimAmount": 25000,
  "urgency": "HIGH",
  "status": "SUBMITTED"
}
```

| Method | Path | Behaviour | Status |
| ------ | ---- | --------- | ------ |
| `GET` | `/api/policies` | All policies in seed order | `200` |
| `GET` | `/api/policies/{policyNo}` | One policy | `200` / `404` |
| `GET` | `/api/policies?status=Active` | Filter by status (exact match) | `200` |
| `GET` | `/api/policies?type=TERM` | Filter by type (exact match) | `200` |
| `POST` | `/api/policies` | Create. Body is Policy JSON without extra fields | `201` / `409` |
| `PUT` | `/api/policies/{policyNo}` | Replace customer, type, basePremium, status. `policyNo` in the path wins | `200` / `404` |
| `DELETE` | `/api/policies/{policyNo}` | Remove | `204` / `404` |
| `GET` | `/api/policies/{policyNo}/claims` | Claims for that policy, oldest first | `200` / `404` |
| `POST` | `/api/claims` | File a claim. Body: `policyNo`, `claimAmount`, `urgency` | `201` / `400` / `404` |
| `GET` | `/api/claims/{claimNo}` | One claim | `200` / `404` |

Rules:

- Use `@GetMapping`, `@PostMapping`, `@PutMapping`, `@DeleteMapping`
- Use `@PathVariable`, `@RequestParam`, `@RequestBody`
- Return `ResponseEntity` so you control the status code
- `POST /api/policies` sets header `Location` to `/api/policies/{policyNo}`
- `POST /api/claims` sets header `Location` to `/api/claims/{claimNo}`
- Duplicate `policyNo` → `DuplicatePolicyException` → **`409`**
- Unknown `policyNo` or `claimNo` → `PolicyNotFoundException` / `ClaimNotFoundException` → **`404`**
- `claimAmount <= 0` or `claimAmount > hdfc.max-claim-amount` → `InvalidClaimException` → **`400`**
- Claim numbers are `CLM-01`, `CLM-02`, … zero-padded to 2 digits, issued in order
- New claims start as `SUBMITTED`
- `GET` collection endpoints return a **JSON array** (not a wrapper object)
- Unsupported method on `/api/policies` (for example `PATCH`) → **`405`** (Spring default is fine)

`status` and `type` query params are optional. If both are omitted, return all. If both are present, apply **both** filters (AND).

After `DELETE /api/policies/HDFC-LIFE-1006`, `GET /api/policies` must not include `1006`. Do this on a copy in your head — **do not delete seed policies in `DataSeeder`**. The delete demo is for you / the grader via HTTP, not at startup.

---

### 5. Flyway schema (3NF)

Commit Flyway scripts under `src/main/resources/db/migration/`.

`V1__hdfc_life_schema.sql` must create **exactly** these tables and constraints (column types may be `VARCHAR` / `INTEGER` / `BIGINT`; names are locked):

**`customers`**

| Column | Rules |
| ------ | ----- |
| `id` | primary key, identity |
| `full_name` | `NOT NULL`, `UNIQUE` |
| `email` | `NOT NULL`, `UNIQUE` |

**`policies`**

| Column | Rules |
| ------ | ----- |
| `id` | primary key, identity |
| `policy_no` | `NOT NULL`, `UNIQUE` |
| `customer_id` | `NOT NULL`, `FOREIGN KEY` → `customers(id)` |
| `product_type` | `NOT NULL`, `CHECK` in `('TERM','ULIP','ENDOWMENT')` |
| `base_premium` | `NOT NULL`, `CHECK` `> 0` |
| `status` | `NOT NULL`, `CHECK` in `('Active','Lapsed','Pending')` |

**`claims`**

| Column | Rules |
| ------ | ----- |
| `id` | primary key, identity |
| `claim_no` | `NOT NULL`, `UNIQUE` |
| `policy_id` | `NOT NULL`, `FOREIGN KEY` → `policies(id)` |
| `amount` | `NOT NULL`, `CHECK` `> 0` |
| `urgency` | `NOT NULL`, `CHECK` in `('HIGH','MEDIUM','LOW')` |
| `status` | `NOT NULL`, `CHECK` in `('SUBMITTED','APPROVED','REJECTED')` |

**`riders`**

| Column | Rules |
| ------ | ----- |
| `id` | primary key, identity |
| `code` | `NOT NULL`, `UNIQUE` |
| `name` | `NOT NULL` |

**`policy_riders`** (many-to-many junction)

| Column | Rules |
| ------ | ----- |
| `policy_id` | `FOREIGN KEY` → `policies(id)` |
| `rider_id` | `FOREIGN KEY` → `riders(id)` |
| composite **primary key** `(policy_id, rider_id)` | |

This is 3NF: customer name and email live on `customers` only. Policy rows reference `customer_id`. Riders are not copied onto `policies`.

Write standard SQL that runs on **H2 with `MODE=PostgreSQL`** and on PostgreSQL. Prefer `GENERATED BY DEFAULT AS IDENTITY` over `SERIAL`.

`V2__seed_reference_riders.sql` must insert exactly:

```text
ACCIDENT_COVER | Accident Cover
CRITICAL_ILLNESS | Critical Illness
WAIVER_OF_PREMIUM | Waiver of Premium
```

Do **not** seed policies in SQL. Java `DataSeeder` owns policy seed data.

On `dev`, the app must **start cleanly** with Flyway applying V1 and V2 (check the startup log for `Successfully applied` / `Migrated`).

---

### 6. Exception handling

All of these must extend **`RuntimeException`**:

```text
DeskException
  ├── PolicyNotFoundException
  ├── ClaimNotFoundException
  ├── DuplicatePolicyException
  └── InvalidClaimException
```

`RestExceptionHandler` annotated with `@RestControllerAdvice`:

| Exception | HTTP | JSON body |
| --------- | ---- | --------- |
| `PolicyNotFoundException` | `404` | `{ "error": "<message>" }` |
| `ClaimNotFoundException` | `404` | `{ "error": "<message>" }` |
| `DuplicatePolicyException` | `409` | `{ "error": "<message>" }` |
| `InvalidClaimException` | `400` | `{ "error": "<message>" }` |

Do not empty-catch. Messages must be non-blank.

`DataSeeder` / a `@PostConstruct` demo method is **not** required to throw. The HTTP contract below is the demo.

---

### 7. README

`README.md` must include:

1. How to run (`./mvnw spring-boot:run` or `mvn spring-boot:run`)  
2. Table of all 10 endpoints (method, path, status codes)  
3. Entity-relationship list: the five tables and their foreign keys  
4. One short paragraph (4–6 lines) answering:

> When would you keep the policy desk in an in-memory store, and when would you move it to PostgreSQL? What does Flyway give you that `ddl-auto=update` does not?

---

### Suggested layout

```text
hdfc-life-policy-desk/
  pom.xml
  src/main/java/com/hdfclife/desk/
    DeskApplication.java
    config/        HdfcProperties, StoreLifecycle, DataSeeder, RestExceptionHandler
    model/         Policy, Claim, Urgency
    store/         PolicyStore, InMemoryPolicyStore
    service/       PolicyService, ClaimService
    web/           PolicyController, ClaimController
    exception/     DeskException, PolicyNotFoundException, ClaimNotFoundException,
                   DuplicatePolicyException, InvalidClaimException
  src/main/resources/
    application.yml
    application-dev.yml
    application-prod.yml
    db/migration/  V1__hdfc_life_schema.sql, V2__seed_reference_riders.sql
  README.md
  .gitignore
```

You may merge small helpers, but do not put store, HTTP, and SQL in one class.

`.gitignore` must exclude `target/`, `.idea/`, `*.class`, `.env`, and `application-prod.yml` secrets. Commit the prod **file** with `${DB_URL}` placeholders, not real passwords.

---

### Startup print (CommandLineRunner, in this order)

1. Active profile → `dev`  
2. Company name from `HdfcProperties` → `HDFC Life`  
3. Max claim amount → `500000`  
4. Seeded policy count → `6`  
5. Lookup `HDFC-LIFE-1004` customer → `Vikram Singh`  
6. Active policy count via `PolicyService` → `4`  
7. TERM policy count via `PolicyService` → `2`  
8. Unique customer count → `5`  
9. Simple class name of the injected `PolicyStore` → `InMemoryPolicyStore`  
10. Lifecycle line (from `@PostConstruct`, may appear before the runner) → `PolicyStore ready`

---

### HTTP contract the grader will call (seed already loaded)

Use these exact requests. Bodies are JSON.

1. `GET /api/policies` → `200`, array length **`6`**, first `policyNo` → `HDFC-LIFE-1001`, last → `HDFC-LIFE-1006`  
2. `GET /api/policies/HDFC-LIFE-1004` → `200`, `customer` → `Vikram Singh`, `basePremium` → `15200`  
3. `GET /api/policies?status=Active` → `200`, array length **`4`**  
4. `GET /api/policies?type=TERM` → `200`, array length **`2`**, policy numbers `HDFC-LIFE-1001` and `HDFC-LIFE-1004`  
5. `GET /api/policies/HDFC-LIFE-9999` → `404`, body has `"error"`  
6. `POST /api/policies` with

```json
{
  "policyNo": "HDFC-LIFE-1007",
  "customer": "Kiran Rao",
  "type": "TERM",
  "basePremium": 20000,
  "status": "Active"
}
```

→ `201`, `Location` contains `/api/policies/HDFC-LIFE-1007`

7. `POST /api/policies` again with `HDFC-LIFE-1007` → `409`  
8. `PUT /api/policies/HDFC-LIFE-1007` with status `Lapsed` (other fields same as create) → `200`, `status` → `Lapsed`  
9. `DELETE /api/policies/HDFC-LIFE-1007` → `204`  
10. `GET /api/policies` → length **`6`** again  
11. `POST /api/claims` with

```json
{
  "policyNo": "HDFC-LIFE-1001",
  "claimAmount": 25000,
  "urgency": "HIGH"
}
```

→ `201`, `claimNo` → `CLM-01`, `status` → `SUBMITTED`

12. `POST /api/claims` with `claimAmount` `600000` and `policyNo` `HDFC-LIFE-1001` → `400`  
13. `POST /api/claims` with `policyNo` `HDFC-LIFE-9999` and `claimAmount` `1000` and `urgency` `LOW` → `404`  
14. `GET /api/policies/HDFC-LIFE-1001/claims` → `200`, array length **`1`**, `claimNo` → `CLM-01`  
15. `GET /swagger-ui/index.html` → `200` (HTML)  
16. `GET /v3/api-docs` → `200`, JSON contains `/api/policies`

---

### Submission Guidelines

Submit the **GitHub repository link**.

- Push the full Spring Boot project (`pom.xml` or `build.gradle`, `src`, `README.md`, `.gitignore`)
- Repo must be **public**
- Do **not** commit `target/`, `.class` files, or real database passwords
- Submit the GitHub repo URL as your answer

### Additional Solving

- <a href="https://leetcode.com/problems/combine-two-tables/" target="_blank" rel="noopener noreferrer">Combine Two Tables</a>
- <a href="https://leetcode.com/problems/customers-who-never-order/" target="_blank" rel="noopener noreferrer">Customers Who Never Order</a>
- <a href="https://leetcode.com/problems/duplicate-emails/" target="_blank" rel="noopener noreferrer">Duplicate Emails</a>
- <a href="https://leetcode.com/problems/employees-earning-more-than-their-managers/" target="_blank" rel="noopener noreferrer">Employees Earning More Than Their Managers</a>
- <a href="https://leetcode.com/problems/department-highest-salary/" target="_blank" rel="noopener noreferrer">Department Highest Salary</a>
- <a href="https://leetcode.com/problems/rising-temperature/" target="_blank" rel="noopener noreferrer">Rising Temperature</a>
- <a href="https://leetcode.com/problems/delete-duplicate-emails/" target="_blank" rel="noopener noreferrer">Delete Duplicate Emails</a>
- <a href="https://leetcode.com/problems/second-highest-salary/" target="_blank" rel="noopener noreferrer">Second Highest Salary</a>
