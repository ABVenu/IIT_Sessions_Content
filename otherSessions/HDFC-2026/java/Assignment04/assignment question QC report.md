# Assignment Question QC Report

**File:** `Q.md`  
**Track:** HDFC Life 2026 — Java Backend  
**Week:** 31 August – 4 September 2026 (4 Sep has no Java session on the live calendar)  
**Format:** Single subjective GitHub project (same pattern as Assignment03)

---

## Iteration 1 — design notes (baked into `Q.md`)

| Issue | Severity | Fix |
|---|---|---|
| First Spring week cannot lock stdout the same way as a console `main` | Presentation | CommandLineRunner startup print **plus** a numbered HTTP contract |
| JPA entities are next week's live-calendar topic, not this week's | Scope leak | JPA starter allowed for datasource only; `@Entity` / `JpaRepository` banned; Flyway owns DDL |
| Requiring a local PostgreSQL would block graders without Docker | Logic risk | `dev` uses H2 `MODE=PostgreSQL`; `prod` uses `DB_*` env placeholders |
| `@ControllerAdvice` is taught later on the detailed sheet | Scope | Kept a thin `@RestControllerAdvice` so 404/400/409 are deterministic without a validation lecture |
| Friday 4 Sep is blank on the live calendar | Scope | No extra Friday topic (no Security, no advanced SQL, no Kafka) |
| Field `@Autowired` is the anti-pattern of this week's IoC session | Ambiguity | Constructor injection required; field injection banned |
| Duplicate seed on restart | Logic risk | Seeder must check `count()` before insert |
| Claim numbers could drift | Ambiguity | Locked to `CLM-01` incrementing, zero-padded to 2 digits |
| Additional Solving as LeetCode algorithms would be off-syllabus | Out of syllabus | SQL join / constraint problems only |

Locked HTTP lengths independently counted from the six-row seed: Active `4`, TERM `2`, unique names `5`. Create `1007` then delete restores length `6`. First claim is `CLM-01`.

---

## Section-level QC

| Section | Type | Remarks |
|---|---|---|
| Seed | Data | Same six policies as Assignment01. Counts verified. |
| 1. Project / IoC / profiles | Practical | Initializr, stereotypes, constructor injection, `dev`/`prod`, `@PostConstruct` / `@PreDestroy` |
| 2. CommandLineRunner + `@ConfigurationProperties` | Practical | Seed + locked startup lines; JSR-303 on properties |
| 3. Springdoc | Practical | `/swagger-ui/index.html` and `/v3/api-docs` in the HTTP contract |
| 4. REST + service | Practical | Full CRUD, query params, `ResponseEntity`, `Location` headers, 405 default |
| 5. Flyway 3NF | Practical | Five tables, FKs, junction PK, CHECKs; V2 riders only; policies stay in Java |
| 6. Exceptions | Practical | Hierarchy extends `RuntimeException`; four mapped statuses |
| 7. README | Written | Endpoint table, ER list, in-memory vs PostgreSQL vs `ddl-auto` paragraph |
| Additional Solving | Optional | SQL LeetCode only; `target="_blank"` |

---

## Curriculum coverage (live calendar, not detailed-curriculum row dates)

| Calendar session | Covered in `Q.md`? |
|---|---|
| 31 Aug — Spring Boot Introduction I / II | Initializr, stereotypes, constructor injection, profiles, bean lifecycle |
| 1 Sep — Spring Boot Project Setup & Swagger I / II | `@ConfigurationProperties`, `CommandLineRunner`, Springdoc annotations, Swagger UI |
| 2 Sep — REST Controllers & Services I / II | CRUD mappings, path/query/body, `ResponseEntity`, service layer |
| 3 Sep — PostgreSQL Schema & Relationships I / II | 3NF, PK/FK, many-to-many junction, CHECK/NOT NULL/UNIQUE, Flyway, JPA starter + driver without entities |
| 4 Sep — (no Java session) | Not included |

Not required (later calendar / later detailed rows): Advanced SQL, Spring Data JPA mappings, `@Valid` DTO lecture, Spring Security / JWT, microservices.

---

## Assignment-level QC

| Criteria | Rating / Status |
|---|---|
| Content Coverage | 5 |
| Creativity | 5 |
| Structural Adherence | 5 (seed, numbered sections, locked outputs, exception tree, layout, GitHub submit, Additional Solving) |
| No Logical Mistakes | True |
| No Presentation Mistakes | True |
| No Previous Session Number References | True |
| No Metadata / internal author notes in the student brief | True |

---

## Final QC Decision

**Passed** after Iteration 1 design locks.

- Content Coverage, Creativity, Structural Adherence are all 5.
- Locked counts recomputed from the seed and match `Q.md`.
- Live-calendar Friday gap is respected.
