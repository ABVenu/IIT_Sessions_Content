# The Developer Workflow

## What You’ll Learn

In this lesson, you’ll learn how AI engineers actually work on a daily basis. You’ll understand how to use the command line to navigate and run code, how Git tracks changes and protects your work, and why professionals carefully choose between notebooks and scripts. By the end, you’ll be able to follow a complete developer workflow confidently and independently.

![Image 1](https://coding-platform.s3.amazonaws.com/dev/lms/tickets/b44f1e23-ca86-4dcd-bc4c-cf2b5f0bb609/JurTpploVaUjMjIq.png)

---

## 1. Understanding the Developer Workflow

A developer workflow is the repeatable process used to write code, test ideas, save progress, and iterate safely. In AI development, workflows matter even more than in traditional software because experimentation is constant and results are rarely correct on the first attempt.

A typical AI developer workflow looks like this:

> Explore ideas → write code → run experiments → inspect results → save progress → iterate

The tools you will learn—CLI, Git, notebooks, and scripts—exist to support this loop while minimizing mistakes and lost work.

---

## 2. The Command Line (CLI)

### What Is the Command Line?

The Command Line Interface (CLI) is a text-based interface that allows you to communicate directly with your operating system. Instead of clicking buttons, you issue commands that tell the computer exactly what to do.

AI engineers rely heavily on the CLI because:

* Servers and cloud machines often have no graphical interface
* Automation requires command-based execution
* Development tools integrate tightly with the terminal

Think of the CLI as the **control panel beneath the graphical interface**.

---

### Core Concepts

#### Current Directory

When using the CLI, you are always inside a directory. All commands operate relative to that location.

To check where you are:

```bash
pwd
```

To see what files exist:

```bash
ls
```

To move into another folder:

```bash
cd project_folder
```

To move back up one level:

```bash
cd ..
```

These commands form the foundation of navigating any system, local or remote.

---

### Running Programs and Scripts

To run a Python script from the CLI:

```bash
python train_model.py
```

This is how most AI pipelines are executed in practice—especially in production or cloud environments.

---

### Recommended Reference

* Official Unix CLI primer:
  [https://ubuntu.com/tutorials/command-line-for-beginners](https://ubuntu.com/tutorials/command-line-for-beginners)
* VS Code terminal documentation:
  [https://code.visualstudio.com/docs/terminal/basics](https://code.visualstudio.com/docs/terminal/basics)

---

## 3. Git: Version Control from First Principles

### What Is Git?

Git is a distributed version control system that records changes to files over time. Instead of saving entire copies of a project, Git stores a history of changes, allowing you to move backward and forward safely.

A helpful way to think about Git:

> Git is a timeline of decisions, not just a backup system.

---

### Initializing a Repository

To start tracking a project with Git:

```bash
git init
```

This creates a hidden `.git` directory that stores the entire history of your project.

At this point, Git is watching—but not saving anything yet.

---

### Adding Files to the Staging Area

Before saving changes, you must select what you want Git to record.

To stage a specific file:

```bash
git add app.py
```

To stage everything:

```bash
git add .
```

The staging area exists so you can control what becomes part of your project’s history.

---

### Committing Changes

A commit is a permanent checkpoint.

```bash
git commit -m "Add initial data loading logic"
```

Each commit should represent:

* One clear idea
* One meaningful improvement
* A message explaining *why* the change was made

Good commits make debugging and collaboration dramatically easier.

---

### Why Git Is Essential for AI Projects

AI development involves trial and error. You may experiment with many approaches before settling on one. Git allows you to explore freely without fear of losing progress or breaking your project permanently.

---

### Recommended References

* Official Git documentation (beginner-friendly):
  [https://git-scm.com/docs/gittutorial](https://git-scm.com/docs/gittutorial)
* GitHub Git Handbook:
  [https://docs.github.com/en/get-started/using-git](https://docs.github.com/en/get-started/using-git)

---

## 4. Notebooks vs Scripts: A Professional Discipline

### What Is a Notebook?

A notebook (such as Jupyter or Colab) is an interactive environment where code is executed in cells. Cells can be run independently and out of order.

Example notebook cell:

```python
import pandas as pd

df = pd.read_csv("data.csv")
df.head()
```

Notebooks are excellent for:

* Learning
* Data exploration
* Visualizations
* Rapid prototyping

They encourage experimentation and curiosity.

---

### What Is a Script?

A script is a file that runs from top to bottom in a fixed order.

Example Python script:

```python
def load_data(path):
    return pd.read_csv(path)

def main():
    df = load_data("data.csv")
    print(df.head())

if __name__ == "__main__":
    main()
```

Scripts are ideal for:

* Reproducibility
* Automation
* Collaboration
* Production systems

---

### The Core Difference

Notebooks are **stateful**. Scripts are **deterministic**.

In notebooks:

* Hidden state can accumulate
* Results depend on execution order

In scripts:

* Execution always starts fresh
* Behavior is predictable and repeatable

---

### Industry Rule of Thumb

A widely followed professional guideline is:

> **Explore in notebooks.
> Build, test, and deploy in scripts.**

Many production failures come from ignoring this distinction.

---

### Recommended References

* Jupyter Notebook documentation:
  [https://docs.jupyter.org/en/latest/](https://docs.jupyter.org/en/latest/)
* Python scripting best practices:
  [https://realpython.com/python-main-function/](https://realpython.com/python-main-function/)

---

## 5. Putting It All Together: A Complete Workflow

A realistic AI workflow often looks like this:

1. Use a notebook to explore data and ideas
2. Identify a working approach
3. Convert that logic into a script
4. Run the script using the CLI
5. Track progress with Git
6. Commit meaningful milestones

Each tool has a clear role. Together, they form a system that supports experimentation without chaos.

---

## Key Takeaways

The command line gives you direct control over your system. Git protects your progress and enables collaboration. Commits represent deliberate progress, not just saved files. Notebooks are for thinking and exploration, while scripts are for reliability and scale. Mastering this workflow is a foundational skill for any AI engineer.

**Mental model:**
The CLI is how you act.
Git is how you remember.
Notebooks are how you explore.
Scripts are how you build.

---

### Optional Deep-Dive Resources

* Pro Git (free book):
  [https://git-scm.com/book/en/v2](https://git-scm.com/book/en/v2)
* Software Engineering for ML (Google):
  [https://developers.google.com/machine-learning/guides/rules-of-ml](https://developers.google.com/machine-learning/guides/rules-of-ml)
* Reproducible ML workflows:
  [https://mlops.community/](https://mlops.community/)
