# Assignment: Setting Up Your AI Lab

**Lecture:** Setting Up Your Lab
**Objective:** Establish a professional local and cloud development environment
**Scope:** Strictly limited to lecture content

---

## Section 1: Objective Type Questions

**Total Questions:** 15
**Format:** 15 MCQs
**Difficulty Distribution:**

* **Easy:** 7
* **Intermediate:** 4
* **Hard:** 4

---

## 1.1 Easy Questions (7)

---

### Q1

What is the primary role of Visual Studio Code in an AI workflow?

A. Training models in the cloud
B. Local code editing and development
C. Hosting datasets
D. Managing API billing

**Correct Answer:** B

**Why B is correct:**
VS Code is a local development environment used to write, debug, and manage code.

**Why others are wrong:**

* **A:** Training happens in runtime environments, not editors.
* **C:** VS Code does not host data; it only accesses files.
* **D:** Billing is handled by cloud providers, not editors.

---

### Q2

Which statement best describes Google Colab?

A. A desktop IDE
B. A browser-based Jupyter notebook environment
C. A version control system
D. A secret management service

**Correct Answer:** B

**Why B is correct:**
Colab runs Jupyter notebooks in the browser with cloud-backed execution.

**Why others are wrong:**

* **A:** Colab is not installed locally.
* **C:** Git handles version control.
* **D:** Colab is not a dedicated secret manager.

---

### Q3

Which item should never be hard-coded into source code?

A. Variable names
B. Function definitions
C. API keys
D. Comments

**Correct Answer:** C

**Why C is correct:**
API keys provide access to services and must remain secret.

**Why others are wrong:**

* **A, B, D:** These do not grant system access.

---

### Q4

GitHub is built on top of which system?

A. Docker
B. SVN
C. Git
D. Jupyter

**Correct Answer:** C

**Why C is correct:**
GitHub hosts Git repositories.

**Why others are wrong:**

* **A:** Docker is for containers.
* **B:** SVN is a different VCS.
* **D:** Jupyter is a notebook interface.

---

### Q5

Which environment is considered ephemeral?

A. VS Code
B. Local Python files
C. Google Colab
D. GitHub repositories

**Correct Answer:** C

**Why C is correct:**
Colab sessions can reset or disconnect unless work is saved.

**Why others are wrong:**

* **A, B:** Persist on disk.
* **D:** Commits persist permanently.

---

### Q6

Why are environment variables used for secrets?

A. They improve performance
B. They allow secrets to be shared publicly
C. They separate sensitive data from code
D. They replace version control

**Correct Answer:** C

**Why C is correct:**
Secrets are injected at runtime without appearing in source code.

**Why others are wrong:**

* **A:** No performance impact.
* **B:** Secrets should never be public.
* **D:** They serve different purposes.

---

### Q7

Which of the following qualify as secrets?

A. Dataset filenames
B. API keys
C. Access tokens
D. Passwords

**Correct Answer:** B, C, D

**Why correct options are correct:**
All grant authenticated access to systems or services.

**Why A is wrong:**
Filenames are not sensitive credentials.

---

## 1.2 Intermediate Questions (4)

---

### Q8

Why is GitHub particularly important for AI projects?

A. AI models require GitHub to run
B. Experiments follow a linear path
C. It allows safe tracking of non-linear experimentation
D. It provides GPUs for training

**Correct Answer:** C

**Why C is correct:**
AI development involves branching, retries, and rollbacks.

**Why others are wrong:**

* **A:** Models run independently of GitHub.
* **B:** AI experimentation is non-linear.
* **D:** GitHub does not provide compute.

---

### Q9

What is the immediate risk of committing an API key to a public repository?

A. Slower code execution
B. Repository corruption
C. Unauthorized usage and financial loss
D. Syntax errors

**Correct Answer:** C

**Why C is correct:**
Anyone can misuse the exposed key.

**Why others are wrong:**

* **A:** Security does not affect speed.
* **B:** Git integrity is unaffected.
* **D:** Keys do not affect syntax.

---

### Q10

Which statements about Google Colab are true?

A. Sessions are always persistent
B. It supports GPU/TPU access
C. It is ideal for rapid experimentation
D. It replaces local development entirely

**Correct Answer:** B, C

**Why correct options are correct:**
Colab provides cloud compute and is designed for experimentation.

**Why others are wrong:**

* **A:** Sessions may disconnect.
* **D:** It complements, not replaces, local tools.

---

### Q11

Separating secrets from code follows which principle?

A. Functional programming
B. Separation of code and configuration
C. Object-oriented design
D. Test-driven development

**Correct Answer:** B

**Why B is correct:**
Configuration changes without modifying source code.

**Why others are wrong:**
They address unrelated design concerns.

---

## 1.3 Hard Questions (4)

---

### Q12

Which risks result from hard-coding secrets?

A. Security breaches
B. Increased model accuracy
C. Unexpected financial costs
D. Mandatory key rotation

**Correct Answer:** A, C, D

**Why correct options are correct:**
Exposed secrets lead to misuse and forced remediation.

**Why B is wrong:**
Security practices do not affect accuracy.

---

### Q13

Why are VS Code and Google Colab best used together?

A. They perform identical roles
B. Both are cloud-only tools
C. One supports structured development, the other experimentation
D. They store secrets automatically

**Correct Answer:** C

**Why C is correct:**
VS Code is persistent and structured; Colab is experimental and cloud-based.

**Why others are wrong:**

* **A:** Their roles differ.
* **B:** VS Code is local.
* **D:** Secrets require explicit handling.

---

### Q14

Which workflow reflects professional AI development practice?

A. Colab only, no version control
B. Local scripts without cloud usage
C. VS Code + Colab + GitHub + secure secrets
D. Writing directly on production servers

**Correct Answer:** C

**Why C is correct:**
This mirrors industry-standard workflows.

**Why others are wrong:**
They omit critical components.

---

### Q15

In the lecture’s mental model, GitHub primarily represents:

A. Compute infrastructure
B. A temporary workspace
C. Memory and collaboration layer
D. A secret manager

**Correct Answer:** C

**Why C is correct:**
GitHub preserves history and enables teamwork.

**Why others are wrong:**
They misrepresent GitHub’s role.
