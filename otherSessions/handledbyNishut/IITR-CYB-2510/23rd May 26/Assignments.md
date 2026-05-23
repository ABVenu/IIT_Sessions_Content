# Applied Cryptography: Hashing, Encryption, Salting, and Secure Coding Practices

---

**Question 1 (Easy MCQ - 1 correct option):**

A backend engineer is onboarding a new team member and explaining the two broad categories of cryptography. The new hire asks: "In symmetric key cryptography, how many keys are used between two communicating parties?" Which answer is correct?

- A) Two keys — one public key and one private key are generated per communicating party
- B) One key for encryption and a separate key derived from the first for decryption only
- C) Four keys in total — each party holds both an encryption key and a decryption key
- D) One shared secret key used by both parties for encryption and decryption operations

**Correct Answer:** D

**Answer Explanation:**
D) Correct. Symmetric key cryptography uses a single shared secret key for both encryption and decryption, and both communicating parties must possess that same key.
A) Incorrect. This describes asymmetric (public key) cryptography, where each party holds a public/private key pair — not symmetric.
B) Incorrect. Symmetric encryption does not derive a separate decryption key; the same key performs both operations.
C) Incorrect. Four keys in total describes no standard cryptographic model and confuses symmetric with other schemes.

---

**Question 2 (Easy MCQ - 1 correct option):**

A security analyst is reviewing a code audit report that flags a legacy system's password storage mechanism. The report notes that two completely different input values produce the same hash output for the algorithm in use. Which hashing problem does this describe?

- A) Avalanche effect causing different outputs from the same input
- B) Rainbow table vulnerability from pre-computed hash lookups
- C) Hash collision producing identical outputs from different inputs
- D) Salt reuse weakness across multiple stored passwords

**Correct Answer:** C

**Answer Explanation:**
C) Correct. A hash collision occurs when two completely different inputs produce the same hash output — exactly the scenario described. This is why MD5 is considered cryptographically broken.
A) Incorrect. The avalanche effect is a desirable property where a tiny change in input causes a completely different hash output — the opposite of a collision.
B) Incorrect. A rainbow table vulnerability refers to pre-computed lookup attacks against unsalted hashes, not same-output different-input scenarios.
D) Incorrect. Salt reuse means multiple passwords share the same salt value, weakening protection, but does not describe two inputs producing the same hash output.

---

**Question 3 (Easy MCQ - 1 correct option):**

A junior developer is writing a password-storage module for a new web application. The team lead says: "Never use plain SHA-256 for passwords — use a purpose-built algorithm instead." The developer asks why Argon2id is the top recommendation. Which property best explains this?

- A) It is FIPS-compliant, required for US government systems, and auto-salts passwords
- B) It is memory-hard and auto-salts, resisting GPU and ASIC brute-force attacks
- C) It produces a fixed-length output, making it the fastest for high-load systems
- D) It is faster than bcrypt and scrypt, ideal for high-throughput authentication

**Correct Answer:** B

**Answer Explanation:**
B) Correct. Argon2id is the OWASP first-choice recommendation because it is memory-hard (attacks require large amounts of memory) and automatically handles salting, making GPU and ASIC brute-force attacks significantly harder.
A) Incorrect. FIPS compliance is a feature of PBKDF2 and bcrypt, not Argon2id; Argon2id is explicitly not FIPS-compliant.
C) Incorrect. Fixed-length output is a property of all hash functions including SHA-256 — it is not unique to Argon2id, and Argon2id is not optimized for speed.
D) Incorrect. Argon2id is intentionally slower than bcrypt — its slowness raises the cost of brute-force attacks and is a deliberate security feature, not a drawback.

---

**Question 4 (Easy MCQ - 1 correct option):**

A DevOps engineer is reviewing a Python microservice. The error handler currently reads: `except Exception as e: return str(e)`. What will be the concrete security consequence of this pattern in a production environment?

- A) The application will log passwords to the internal monitoring system
- B) The full stack trace and internal details will be exposed to the API caller
- C) The exception will be silently swallowed and the user will receive no response
- D) The application will retry the failed operation automatically

**Correct Answer:** B

**Answer Explanation:**
B) Correct. Returning `str(e)` directly sends the full exception message — including file paths, variable names, and internal architecture details — to the API caller, exposing internal application structure to potential attackers.
A) Incorrect. This pattern returns the exception to the caller; it does not involve logging passwords to a monitoring system. Logging sensitive data is a separate bad practice.
C) Incorrect. This is the opposite of what happens — the error is explicitly returned to the caller, not silently swallowed.
D) Incorrect. `return str(e)` performs no retry logic whatsoever; automatic retries require explicit retry code.

---

**Question 5 (Moderate MCQ - 1 correct option):**

A security engineer at a financial services firm is designing a new user authentication system. The firm must comply with FIPS (Federal Information Processing Standards) requirements mandated by its government contracts. The engineer cannot use Argon2id. Which password-hashing algorithm should be selected, and what iteration count aligns with FIPS standards?

- A) bcrypt with 12 rounds; bcrypt is FIPS-compliant, memory-hard, and auto-salting
- B) SHA-256 with a random 16-byte salt; SHA-256 is purpose-built for password storage
- C) PBKDF2 at ~600,000 iterations; mandated for FIPS-compliant password hashing
- D) scrypt with high memory cost; scrypt is FIPS-compliant and memory-hard by design

**Correct Answer:** C

**Answer Explanation:**
C) Correct. PBKDF2 (Password-Based Key Derivation Function 2) is specifically required when FIPS compliance is mandated, with a FIPS-standard iteration count of approximately 600,000.
A) Incorrect. bcrypt is not FIPS-compliant — it uses the Blowfish cipher, which is not an approved FIPS algorithm. It also uses a rounds work factor, not a 600,000-iteration count. The question specifies the firm needs FIPS compliance without Argon2id, which uniquely identifies PBKDF2.
B) Incorrect. SHA-256 is a cryptographic hash function, not a purpose-built password-hashing algorithm, and is not recommended for direct password storage.
D) Incorrect. scrypt is memory-hard and strong, but it is not FIPS-compliant, making it unsuitable for a government-mandated compliance requirement.

---

**Question 6 (Moderate MCQ - 1 correct option):**

A penetration tester recovers a database dump containing password hashes. The hashes were stored with SHA-256 but no salting was applied. The tester pastes several hashes into CrackStation. Which outcome best describes what will happen and why?

- A) CrackStation will fail because SHA-256 has no known collisions and is not yet broken
- B) CrackStation will crack the passwords via real-time SHA-256 computation and brute force
- C) CrackStation will look up the hashes in its pre-computed table and return plaintexts
- D) CrackStation only succeeds when passwords are shorter than 8 characters in length

**Correct Answer:** C

**Answer Explanation:**
C) Correct. CrackStation maintains terabytes of pre-computed hash data. Without salting, it simply looks up the SHA-256 hash and immediately retrieves the original plaintext — this is a lookup, not computation.
A) Incorrect. SHA-256 having no known collisions does not protect against pre-computed lookups; rainbow tables work against any deterministic, unsalted hash regardless of collision resistance.
B) Incorrect. CrackStation's mechanism is a pre-built table lookup, not real-time brute-force computation; real-time brute force would be far slower.
D) Incorrect. Password length is not the determining factor — CrackStation has pre-computed hashes for billions of common passwords regardless of their length.

---

**Question 7 (Moderate MSQ - Multiple correct options):**

A data engineer is evaluating password-hashing algorithms for a new SaaS platform. The team wants algorithms that handle salt generation automatically — removing that responsibility from application developers. Which of the following algorithms automatically generate a salt without requiring the developer to do it manually?

- A) scrypt
- B) Argon2id
- C) PBKDF2
- D) bcrypt

**Correct Answers:** B, D

**Answer Explanation:**
B) Correct. Argon2id automatically handles salting — no manual salt generation is needed, making it the first-choice recommendation per OWASP.
D) Correct. bcrypt automatically generates a 128-bit salt, removing the developer's burden of manual salt management.
A) Incorrect. scrypt is memory-hard and strong, but it does NOT auto-salt; the developer must generate and manage the salt manually.
C) Incorrect. PBKDF2 similarly requires the developer to supply the salt at call time; it does not auto-generate one.

---

**Question 8 (Moderate MSQ - Multiple correct options):**

A senior developer is reviewing a Python authentication module and spots several patterns. Which of the following are correct, secure practices for handling passwords and authentication in production code?

- A) Using MD5 to hash passwords because it is fast and always produces a fixed-length output
- B) Using the `secrets` library to generate cryptographically random tokens for password resets
- C) Hard-coding API keys directly in source code to eliminate the need to manage `.env` files
- D) Returning "Invalid credentials" on login failure rather than exposing the stored hash

**Correct Answers:** B, D

**Answer Explanation:**
B) Correct. Using the `secrets` library for cryptographically secure random token generation is a recommended practice — the lab's `generate_reset_token` function demonstrates exactly this approach.
D) Correct. Returning "Invalid credentials" on login failure is the secure pattern — the `verify_password` function returns this generic message rather than internal data, preventing information leakage.
A) Incorrect. MD5 is cryptographically broken, must not be used for security purposes, and is one of the intentionally bad patterns flagged by both Bandit and Semgrep in the lab.
C) Incorrect. Hard-coding API keys in source code is a critical security flaw — secrets must be stored in `.env` files (excluded from version control) or in a vault like HashiCorp Vault or AWS Secrets Manager.

---

**Question 9 (Hard MSQ - Multiple correct options):**

A security architect is reviewing a startup's backend infrastructure after a near-miss data breach. The startup stored user passwords using SHA-256 without salting, committed API keys to their GitHub repository, and returned raw exception objects to API clients. Which of the following independent remediation steps would directly address the vulnerabilities identified?

- A) Replace SHA-256 password hashing with bcrypt via `bcrypt.hashpw` and `bcrypt.gensalt(rounds=12)`
- B) Add a unique, random 16-byte salt per password before hashing, per OWASP minimum requirements
- C) Switch from AES-256 to SHA-256 for data in transit to reduce ciphertext output size
- D) Move secrets to a `.env` file excluded from Git, or use HashiCorp Vault or AWS Secrets Manager
- E) Update the error handler to log exceptions internally and return only a generic message

**Correct Answers:** A, B, D, E

**Answer Explanation:**
A) Correct. Replacing SHA-256 with bcrypt via `bcrypt.hashpw` and `bcrypt.gensalt(rounds=12)` directly fixes the unsalted SHA-256 password storage — the lab's `hash_password` function shows this exact pattern.
B) Correct. Adding a unique random 16-byte salt per password (OWASP's minimum) defeats rainbow table attacks even without changing the algorithm.
D) Correct. Moving secrets to a `.env` file excluded from Git, or a centralized vault like HashiCorp Vault or AWS Secrets Manager, directly remediates the hard-coded API key exposure.
E) Correct. Updating the error handler to log exceptions internally and return only a generic message prevents architecture leakage to attackers.
C) Incorrect. AES-256 is a symmetric encryption algorithm for confidentiality; SHA-256 is a one-way hash function, not an encryption algorithm. Mixing up encryption and hashing is a fundamental cryptography mistake — switching to SHA-256 for data in transit would eliminate decryptability entirely, introducing a new critical vulnerability.

---

**Question 10 (Hard MSQ - Multiple correct options):**

A platform engineering team is deploying a Python web application with a full CI/CD pipeline on GitHub Actions. They want automated detection of weak cryptographic practices in every pull request. Which of the following statements about Bandit and Semgrep are accurate based on how these tools operate?

- A) Bandit is Python-specific and can detect hard-coded passwords, MD5 usage, and SHA-1 usage, reporting file name, line number, and severity level
- B) Semgrep is a multi-language SAST tool that runs a rule set — the lab run executed 187 rules and produced 3 findings, all overlapping with Bandit's output
- C) Bandit and Semgrep findings from the lab confirmed that using MD5 for hashing is a high-severity issue, and that SHA-1 also triggered a weak-hash finding
- D) Running `bandit -r lab/ --severity-level medium` on the lab file produces zero findings because MD5 is acceptable for non-authentication use cases

**Correct Answers:** A, B, C

**Answer Explanation:**
A) Correct. Bandit is Python-specific and detected MD5 usage (high severity, high confidence), SHA-1 usage (high severity), and an additional lower-severity finding, each with exact file name, line number, and column number.
B) Correct. Semgrep is a multi-language SAST tool; the lab run executed 187 rules and produced 3 findings that all overlapped with Bandit's output, confirming consistency across tools.
C) Correct. Both tools independently confirmed MD5 usage as a high-severity security issue and flagged weak hash algorithms in the lab code.
D) Incorrect. `bandit -r lab/ --severity-level medium` produces 2 high-severity issues and 1 low-severity issue, not zero findings. MD5 is flagged as a security problem regardless of use-case labeling, and the lab was designed explicitly to trigger these findings.

---

**Question 11 (Hard Subjective - Practical Task):**

**Problem Statement:**
A backend engineer is building a user authentication service in Python. The current codebase stores passwords with MD5 (no salting), hard-codes the application secret in the source file, and returns raw exception messages to API callers. The engineer needs to refactor three functions — `store_password`, `verify_login`, and `handle_error` — to follow secure coding practices using the `bcrypt` and `secrets` libraries.

**Constraints & Requirements:**
- Use `bcrypt` for password hashing with `bcrypt.gensalt(rounds=12)` and `bcrypt.hashpw`.
- Use `bcrypt.checkpw` for password verification.
- The `verify_login` function must return `"Login success"` on a correct password and `"Invalid credentials"` on a wrong password — never expose the stored hash or exception details.
- The `handle_error` function must log the exception internally using `print` (simulating an internal logger) and return the string `"An error occurred"` to the caller.
- Use only `bcrypt` and `secrets` from external libraries; `hashlib` is available in stdlib but must not be used for password storage.
- Do not hard-code any secrets in the source code.
- The solution must run cleanly against the sample input below.

**Inlined Sample Data & Inputs (required):**

```python
# Sample inputs the student's solution will be tested against:
sample_password = "SecurePass@99"
wrong_password  = "WrongPass123"

# Expected behavior:
# store_password(sample_password)  -> returns a bytes object (the bcrypt hash)
# verify_login(sample_password, stored_hash) -> "Login success"
# verify_login(wrong_password, stored_hash)  -> "Invalid credentials"
# handle_error(ValueError("DB timeout: host=db01"))  -> "An error occurred"
#   AND must print the exception internally (not return it)
```

**Expected output for the sample above:**
```
Login success
Invalid credentials
An error occurred
```
(Internal log line printed to stdout before "An error occurred" is acceptable and expected.)

**Submission Format:**
Paste your complete answer (including code, if applicable) into the text box on the platform, following the structure shown in the Submission Format Example below.

## Submission Format Example

```python
import bcrypt
import secrets

def store_password(password: str) -> bytes:
    # Your implementation here
    pass

def verify_login(password: str, stored_hash: bytes) -> str:
    # Your implementation here
    pass

def handle_error(e: Exception) -> str:
    # Your implementation here
    pass

if __name__ == "__main__":
    sample_password = "SecurePass@99"
    wrong_password  = "WrongPass123"

    stored_hash = store_password(sample_password)
    print(verify_login(sample_password, stored_hash))
    print(verify_login(wrong_password, stored_hash))
    print(handle_error(ValueError("DB timeout: host=db01")))
```

**Answer Explanation (Model Answer):**

- **Ideal Approach Walkthrough:**
  1. **`store_password`:** Generate a bcrypt salt using `bcrypt.gensalt(rounds=12)` — the `rounds` parameter sets the work factor, making brute-force expensive. Encode the plaintext password to bytes and pass both to `bcrypt.hashpw`, which hashes the password with the embedded salt. Return the resulting bytes object. Never use MD5 or SHA-256 here.
  2. **`verify_login`:** Use `bcrypt.checkpw(password.encode(), stored_hash)` to compare the submitted password against the stored bcrypt hash. bcrypt re-extracts the salt from the stored hash and recomputes internally. Return `"Login success"` on `True`, `"Invalid credentials"` on `False`. Do not expose the stored hash, the exception, or any internal state.
  3. **`handle_error`:** Wrap the call in a try/except if needed, but the handler itself should `print` the full exception details to a simulated internal log (e.g., `print(f"[INTERNAL LOG] Exception: {e}")`) and return only `"An error occurred"` to the caller. Never return `str(e)`.

- **Expected Code / Solution Files:**

```python
import bcrypt
import secrets

def store_password(password: str) -> bytes:
    salt = bcrypt.gensalt(rounds=12)
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed

def verify_login(password: str, stored_hash: bytes) -> str:
    try:
        if bcrypt.checkpw(password.encode(), stored_hash):
            return "Login success"
        else:
            return "Invalid credentials"
    except Exception as e:
        print(f"[INTERNAL LOG] Exception during login check: {e}")
        return "Invalid credentials"

def handle_error(e: Exception) -> str:
    print(f"[INTERNAL LOG] Exception occurred: {e}")
    return "An error occurred"

if __name__ == "__main__":
    sample_password = "SecurePass@99"
    wrong_password  = "WrongPass123"

    stored_hash = store_password(sample_password)
    print(verify_login(sample_password, stored_hash))
    print(verify_login(wrong_password, stored_hash))
    print(handle_error(ValueError("DB timeout: host=db01")))
```

- **Alternative Approaches:**
  - Argon2id could be used instead of bcrypt via the `argon2-cffi` library — it is the OWASP first-choice recommendation and is memory-hard, making it stronger against GPU brute force. The tradeoff is that `argon2-cffi` is not in stdlib and is less universally pre-installed.
  - For the `handle_error` function, a production system would use Python's `logging` module (`logger.error("Exception occurred", exc_info=True)`) rather than `print`, providing structured log levels and integration with centralized log aggregators. The `print` approach is used here to keep the solution self-contained.
  - A `generate_reset_token` function using `secrets.token_urlsafe(32)` is the secure way to generate password-reset tokens, replacing any approach that uses `random` or `hashlib` for token generation.