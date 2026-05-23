# Assignment — Subjective (Applied Cryptography: Secure Coding in Python)

**Type:** One practical coding task (medium difficulty)

---

## Problem Statement

A backend engineer is building a user authentication service in Python. The current codebase stores passwords with MD5 (no salting), hard-codes the application secret in the source file, and returns raw exception messages to API callers. Refactor the service by implementing four functions — `store_password`, `verify_login`, `generate_reset_token`, and `handle_error` — using secure coding practices with the `bcrypt` and `secrets` libraries.

---

## Constraints & Requirements

- Use `bcrypt` for password hashing with `bcrypt.gensalt(rounds=12)` and `bcrypt.hashpw`.
- Use `bcrypt.checkpw` for password verification.
- Implement `generate_reset_token()` using `secrets.token_urlsafe(32)` and return the token string.
- The `verify_login` function must return `"Login success"` on a correct password and `"Invalid credentials"` on a wrong password — never expose the stored hash or exception details.
- The `handle_error` function must log the exception internally using `print` (simulating an internal logger) and return the string `"An error occurred"` to the caller.
- Use only `bcrypt` and `secrets` from external libraries; `hashlib` is available in stdlib but must not be used for password storage.
- Do not hard-code any secrets in the source code.

---

## Sample Input & Expected Behavior

```python
sample_password = "SecurePass@99"
wrong_password  = "WrongPass123"

# Expected behavior:
# store_password(sample_password)  -> returns a bytes object (the bcrypt hash)
# verify_login(sample_password, stored_hash) -> "Login success"
# verify_login(wrong_password, stored_hash)  -> "Invalid credentials"
# handle_error(ValueError("DB timeout: host=db01"))  -> "An error occurred"
#   AND must print the exception internally (not return it)
# generate_reset_token() -> URL-safe string of sufficient length (32 bytes entropy)
```

**Expected printed output from `__main__`:**

```
Login success
Invalid credentials
An error occurred
```

(An internal log line printed to stdout before `"An error occurred"` is acceptable and expected.)

---

## Starter Template

```python
import bcrypt
import secrets

def store_password(password: str) -> bytes:
    pass

def verify_login(password: str, stored_hash: bytes) -> str:
    pass

def generate_reset_token() -> str:
    pass

def handle_error(e: Exception) -> str:
    pass

if __name__ == "__main__":
    sample_password = "SecurePass@99"
    wrong_password  = "WrongPass123"

    stored_hash = store_password(sample_password)
    print(verify_login(sample_password, stored_hash))
    print(verify_login(wrong_password, stored_hash))
    print(handle_error(ValueError("DB timeout: host=db01")))
    reset = generate_reset_token()
    print(f"Reset token length: {len(reset)}")
```

---

## Submission Instructions (Case C)

- Code all requirements in **VS Code** in a **single `.py` file**.
- Run the code and verify it produces the expected output above.
- Submit the complete file in the **code editor / answer box** on the LMS.

---

## Answer Explanation (Model Answer)

**Ideal approach:**

1. **`store_password`:** Generate a bcrypt salt with `bcrypt.gensalt(rounds=12)`, encode the password to bytes, and return `bcrypt.hashpw(password.encode(), salt)`.
2. **`verify_login`:** Use `bcrypt.checkpw(password.encode(), stored_hash)`; return `"Login success"` or `"Invalid credentials"` only. On unexpected errors, log internally and still return `"Invalid credentials"`.
3. **`generate_reset_token`:** Return `secrets.token_urlsafe(32)` for cryptographically secure reset tokens.
4. **`handle_error`:** `print` full exception details internally; return only `"An error occurred"`.

**Complete solution:**

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
        return "Invalid credentials"
    except Exception as e:
        print(f"[INTERNAL LOG] Exception during login check: {e}")
        return "Invalid credentials"

def generate_reset_token() -> str:
    return secrets.token_urlsafe(32)

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
    reset = generate_reset_token()
    print(f"Reset token length: {len(reset)}")
```

**Alternative approaches:**

- **Argon2id** via `argon2-cffi` is the OWASP first choice and is memory-hard; trade-off is an extra dependency versus widely available `bcrypt`.
- Production code would use Python's `logging` module instead of `print` for internal exception logging.

---

**End of subjective assignment**
