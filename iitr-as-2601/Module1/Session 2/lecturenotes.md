# Setting Up Your Lab

## What You’ll Learn

In this lesson, you’ll learn how to set up a professional development environment used by modern AI practitioners. You’ll install and configure a local code editor, use a cloud-based notebook environment, manage sensitive credentials securely, and create a GitHub account to collaborate and version your work. By the end, you will have a working “lab” that mirrors how AI systems are developed in real-world teams.

---

## 1. Why a “Lab” Matters in AI Development

Before writing any AI code, it is important to establish a reliable working environment. In professional settings, an AI lab is not a physical space—it is a **combination of tools, services, and practices** that allow you to experiment, build, and deploy systems safely and reproducibly.

Unlike traditional software, AI development often involves:

* Experimentation with models and data
* Frequent iteration and testing
* Use of external APIs and cloud services
* Collaboration across teams

A properly set up lab ensures that your work is organized, reproducible, and secure. It also helps you transition smoothly from learning environments to real production workflows.

---

## 2. Visual Studio Code: Your Local Development Environment

Visual Studio Code (VS Code) is a lightweight but powerful code editor developed by Microsoft. It is widely used in the AI and software engineering community because it balances simplicity with professional-grade features.

At its core, VS Code provides:

* A code editor with syntax highlighting and intelligent suggestions
* Integrated terminal access
* Debugging tools
* Extension support for languages, frameworks, and cloud services

In AI workflows, VS Code acts as your **local control center**. You write scripts, inspect files, manage environments, and interact with version control—all from one interface.

After installation, VS Code can be extended with plugins such as:

* Python support for writing and debugging ML code
* GitHub integration for version control
* Jupyter support for running notebooks locally

The key idea is that VS Code represents how engineers work on real projects: code lives on your machine, changes are tracked, and experiments are deliberate rather than disposable.

---

## 3. Google Colab: Cloud-Based Experimentation

While local development is essential, AI work often requires more compute power than a personal laptop can provide. This is where **Google Colab** becomes useful.

Google Colab is a cloud-hosted Jupyter notebook environment that runs entirely in the browser. It allows you to:

* Write and execute Python code without local setup
* Access GPUs and TPUs for free (with usage limits)
* Share notebooks easily with others

Colab is particularly valuable for:

* Learning and experimentation
* Running compute-intensive models
* Rapid prototyping

Unlike VS Code, Colab is **ephemeral**. Sessions can disconnect, and files may not persist unless explicitly saved. This makes it ideal for exploration, but not a replacement for a structured local environment.

A healthy AI workflow often uses both:

* VS Code for structured development and versioned code
* Colab for experiments, demos, and heavy computation

Understanding when to use each tool is part of developing professional intuition.

---

## 4. Managing Secrets and API Keys Safely

Modern AI development frequently relies on external services—language models, cloud platforms, databases, and APIs. Access to these services is typically controlled through **API keys or secrets**.

A secret is any piece of sensitive information that grants access to a system. Examples include:

* API keys
* Access tokens
* Passwords
* Service credentials

One of the most important professional habits you can build early is **never hard-coding secrets into your code**.

Why this matters:

* Code is often shared, committed to GitHub, or deployed publicly
* Exposed secrets can be misused, leading to security breaches or unexpected costs
* Once leaked, secrets must be rotated or revoked

Best practice is to store secrets in environment variables or secure secret managers. Both Google Colab and local environments support this pattern. The code reads the secret at runtime, but the value itself never appears in the source code.

This separation between **code** and **configuration** is a foundational principle in modern system design and is especially critical when working with AI APIs.

---

## 5. GitHub: Version Control and Collaboration

GitHub is a platform built on top of Git, a distributed version control system. It allows developers to track changes, collaborate with others, and maintain a history of their work.

In AI projects, GitHub plays several key roles:

* Tracking changes to code and experiments
* Collaborating with teammates
* Sharing reproducible examples
* Building a public portfolio

Creating a GitHub account is often the first step toward working like a professional engineer. Every meaningful change to a project can be committed, documented, and reviewed.

Version control is especially important in AI because experimentation is non-linear. You may try many approaches before finding what works. Git allows you to move forward without fear, knowing you can always return to a previous state.

Over time, your GitHub profile becomes a record of your learning and growth—not just what you built, but how you think.

---

## 6. How These Tools Work Together

Think of your lab as an ecosystem rather than a collection of disconnected tools.

VS Code is where structured development happens. Google Colab is where rapid experimentation and heavy computation occur. Secrets management ensures that your systems remain secure. GitHub ties everything together by tracking progress and enabling collaboration.

This mirrors how AI systems are built in industry: local development, cloud execution, secure credentials, and shared repositories.

Learning these tools early helps you focus less on setup friction and more on understanding AI systems themselves.

---

## Key Takeaways

A professional AI lab combines local tools, cloud resources, security practices, and collaboration platforms. Visual Studio Code provides a powerful local development environment, while Google Colab enables cloud-based experimentation. Managing secrets securely is essential for safe and scalable AI development. GitHub allows you to version, share, and grow your work over time.

**Mental model:**
VS Code is your workshop.
Colab is your test lab.
Secrets protect your access.
GitHub is your memory and collaboration layer.
