| Detailed Sub-topic | Status | Remarks |
|---|---|---|
| Create and use dictionaries with key-value pairs | Covered | Explained 3 ways to create a dictionary (literal/initialization, empty dict then add values via input, and `dict()` keyword). Covered accessing & modifying values, key uniqueness, and duplicate-key overwrite behavior. |
| Apply get(), keys(), values(), and items() methods | Covered | All four methods demonstrated with code. `get()` shown with default value (e.g. `get(key, 0)`) and `None` handling to avoid program crashes; `items()` used for iterating key-value pairs in a loop. |
| Explain dictionary/hashmap intuition for fast lookups | Covered | Strong intuition built via phone-book (10k contacts) and car-valet analogies. Explained O(1) vs O(n) time complexity, internal hash function generating a hash, memory slot mapping, and that dictionary == hashmap (with naming across Java/C++/JS). |
| Use built-in functions to work with dictionary data | Covered | `len()` and `sorted()` covered (sorted on keys and on `.values()`). |
| Hashable / valid key data types (Extra) | Covered (Extra) | Beyond syllabus: explained valid key types — string, integer, boolean, tuple — and that a list cannot be used as a key (unhashable), causing an error. |
| Internal hashing mechanism (Extra) | Covered (Extra) | Beyond syllabus: explained how Python compresses a key into a hash value and maps it to a memory slot, with the car-valet analogy. |
| Character frequency counter mini-problem (Extra) | Covered (Extra) | Beyond syllabus: live-coded counting character occurrences in a string (e.g. "banana") using a dictionary with `get(char, 0)` pattern — practical application. |
| Additional built-in functions: max(), min(), sum() (Extra) | Covered (Extra) | Beyond the listed `len()`/`sorted()`: also demonstrated `max()`, `min()`, and `sum()` on dictionary values. |
| Tuples (Extra - assigned as reading) | Not Covered (in live) | Mentioned as a key type and shared as post-class reading material with interview questions; not taught live. |
