### **Why Version Control Matters — Pre-Read**

Software projects constantly evolve. Version Control Systems (VCS) are critical for tracking and managing these changes, allowing you to restore older versions, avoid conflicts, and collaborate effectively with teammates.

---

### **Real-World Problems Without Version Control**

*   Manual file backups (`final_v3_fixed_reallyfinal.cpp`) are unreliable and prone to failure.
*   Multiple people editing the same file often overwrite each other's work.
*   Accidental deletion or system crashes can lead to permanent code loss.

**Reflective question:** How would you recover your project if a new change breaks everything?

---

### **What Version Control Does**

VCS acts like a timeline for your project, recording every change.
```bash
v1 → v2 → v3 → v4
(works) (bug) (fix) (new feature)
```
It:
*   Stores every version safely.
*   Compares and restores previous versions.
*   Records authorship and reasoning for changes.
*   Enables smooth teamwork.
![Version Control](https://coding-platform.s3.amazonaws.com/dev/lms/tickets/8791fbc9-33ca-421b-ad68-a07d204fca84/qDCpbqCh13XUa0wH.png)

---

### **Simple Analogy**

Think of writing a report and saving multiple drafts (`draft1`, `draft2`). Older drafts are kept because they might be useful. VCS does this automatically for code, providing:
*   Permanent history.
*   Offline support.
*   Safe collaboration.

---

### **Types of Version Control Systems**

| Type               | Where history lives       | Best suited for           | Example        |
| ------------------ | ------------------------- | ------------------------- | -------------- |
| Local              | One machine               | Solo development          | RCS            |
| Centralized (CVCS) | One server                | Team collaboration        | SVN            |
| Distributed (DVCS) | Every developer’s machine | Modern, scalable projects | Git, Mercurial |

---

### **The Industry Standard: Git**

**Git** is the most widely used DVCS today because it is:
*   Fast and flexible.
*   Fully offline compatible.
*   Excellent at branching and merging.
*   Secure and reliable.

**GitHub** is a popular cloud service for hosting Git repositories online, facilitating team collaboration.
<image src="https://coding-platform.s3.amazonaws.com/dev/lms/tickets/6000a753-18b7-4a8b-bb7c-efd1aa3535dc/OkTPYUmUaszfEXKe.png" width="320px">

---

### **How VCS Supports Development**

| Situation                   | Without VCS              | With VCS                        |
| --------------------------- | ------------------------ | ------------------------------- |
| Machine failure             | Code lost permanently    | Restore from repository         |
| Trying new features         | Risky                    | Use branches to isolate changes |
| Debugging issues            | Hard to trace            | Check commit history            |
| Multiple edits on same file | Conflicts and overwrites | Safe merging workflow           |

---

### **Quick Self-Check**

*   Do you keep older versions of your project files?
*   Can you revert code confidently if a mistake happens?
*   Can you work on the same files with teammates safely?

These challenges highlight why Version Control is essential.

---

### **Useful Resources**

Videos:

*   Why Version Control? — [https://youtu.be/zbKdDsNNOhg](https://youtu.be/zbKdDsNNOhg)
*   What is Git & GitHub? — [https://youtu.be/RGOj5yH7evk](https://youtu.be/RGOj5yH7evk)

Blog:

*   Atlassian: Introduction to Version Control
    [https://www.atlassian.com/git/tutorials/what-is-version-control](https://www.atlassian.com/git/tutorials/what-is-version-control)

---

Software teams use Source Code Management (SCM) tools to track changes, prevent data loss, and coordinate collaboration efficiently.

## SCM Tools Overview

SCM tools come in centralized or distributed architectures.

| Tool Name          | Nature            | Primary Usage                                    |
| ------------------ | ----------------- | ------------------------------------------------ |
| SVN, Perforce      | Centralized       | Managed access via a shared server               |
| Git, Mercurial     | Distributed       | Full history on every developer’s machine        |
| Azure DevOps / TFS | Centralized/Cloud | Repository, project planning, and automation     |

Distributed systems like Git are now the industry standard.

## Why Git is the Standard

Git's key advantages include:
*   Offline development capability
*   Full version history locally
*   Fast operations
*   Safe branching and merging
*   Secure change tracking
*   Broad community adoption
*   Integration with cloud platforms

## What Git Does

Git is a local version control tool that manages all versioning tasks on your machine. It records changes, preserves history, and organizes contributions.

## GitHub: Cloud Collaboration

GitHub is a cloud platform that hosts Git repositories online for team collaboration.

It enables:
*   Secure remote storage and backup
*   Team collaboration, code review, issue tracking
*   Displaying public contribution history

| Aspect          | Git              | GitHub                            |
| --------------- | ---------------- | --------------------------------- |
| Location        | Local system     | Cloud platform                    |
| Internet needed | Not required     | Required                          |
| Main purpose    | Version tracking | Collaboration, backup, visibility |

## Getting Ready

Before the session, ensure you:
*   Create a GitHub account using a **professional name**.
*   Use an email that will match your Git configuration for proper commit authorship.

---

Git manages project changes through a clear flow of how files move between different areas before becoming part of the project history.

---

## **1. The Three-Area Model**

Git organizes files across three logical areas that represent their state.

![Image](https://coding-platform.s3.amazonaws.com/dev/lms/tickets/07d42e41-6c25-4883-8b81-04fcc2c94420/UMQizQ3zQGscDIJV.png)

**Working Directory**
Where files are created, edited, or deleted. Changes here are not tracked until staged.

**Staging Area (Index)**
A preparation zone that collects selected changes. This allows forming intentional and clean snapshots.

**Local Repository**
Stores committed snapshots permanently with unique commit IDs.

---

## **2. Checking File States**

`git status` displays which files are modified, which are staged, and which remain unstaged.
Example (conceptually):

- A modified file may appear under “changes not staged.”
- A newly added file may appear under “changes to be committed.”

---

## **3. Staging Changes**

`git add` moves selected files into the staging area.
Examples:

- Staging a single file
- Staging multiple files
- Staging all tracked and modified files

Staging allows grouping related updates into meaningful commits.

---

## **4. Creating Commits**

A commit acts as a snapshot of all staged changes.
Commit messages typically start with verbs such as _Add_, _Fix_, _Update_, _Remove_ and describe the purpose of the change clearly.
Example messages:

- Add navbar component
- Fix validation issue

---

## **5. Viewing Project History**

`git log` lists past commits with details like ID, author, and timestamp.
A condensed format shows just commit IDs and short messages to provide a quick view of progression.

---

## **6. Comparing Versions**

`git diff` highlights differences between two states:

- Working directory vs staging area
- Staging area vs last commit
- One commit vs another

Conceptually, added lines appear with a plus symbol and removed lines with a minus symbol, allowing careful review before saving work.

---

## **7. Workflow Overview**

A typical flow involves:

1. Editing files
2. Checking their state
3. Staging selected updates
4. Reviewing staged content
5. Creating a commit
6. Inspecting history afterward

---

---

Git allows safe undo operations at different stages: working directory, staging area, and repository. This pre-read covers the basics of these undo capabilities.

## 1. Undoing Changes in the Working Directory

Uncommitted edits in the working directory can be reverted to the last committed version. For example, resetting an incorrectly edited configuration file. This only affects uncommitted changes.

## 2. Removing Files from the Staging Area

If wrong files are staged, they can be moved back to the working directory without losing edits. For example, unstaging a large log file. Unstaging affects only the staging area and preserves modifications.

## 3. Modifying the Most Recent Commit

The most recent commit can be updated to fix message typos or add forgotten files. This rewrites the last commit (changes its ID) and is safe before pushing it to a shared repository.

## 4. Undoing Based on the File Lifecycle

Undo actions depend on the file's stage: discard changes in the working directory, unstage from the staging area, or adjust the latest commit in the repository.

## 5. Common Mistake Scenarios

The session will cover how to handle common mistakes: discarding unwanted changes, unstaging files, correcting commit messages, and adding forgotten files to the last commit.

---

As projects grow, multiple types of work often happen at the same time—new features, bug fixes, experiments, and urgent changes. Git branching provides a structured way to manage this parallel work without affecting the stability of the main codebase.

---

## 1. Why Branching Exists

![Image](https://nvie.com/img/git-model%402x.png?utm_source=chatgpt.com)

![Image](https://itknowledgeexchange.techtarget.com/coffee-talk/files/2021/01/gitflow-hotfix-branch-diagram.jpg?utm_source=chatgpt.com)

In real-world development, a stable version of the application must remain reliable while new changes are developed. Without branches, all changes would mix, increasing risk and confusion.

---

## 2. What a Branch Represents

A branch is an independent line of development pointing to a specific commit.

- Each branch tracks its own sequence of commits.
- Work done in one branch does not impact others.
- The `main` branch usually represents stable code.

Branches are lightweight and easy to create or remove.

---

## 3. Isolated Development

![Image](https://anarsolutions.com/wp-content/uploads/2019/11/Gitflow.png?utm_source=chatgpt.com)

![Image](https://miro.medium.com/0%2AG2z5FjDvIsQRfKvM.png?utm_source=chatgpt.com)

Isolation is the core benefit of branching:
- Feature work continues without breaking stable code.
- Bug fixes do not interfere with feature development.
- Experiments can be discarded safely.

Each branch acts like a focused workspace for a specific purpose.

---

## 4. Managing Multiple Branches

Developers need ways to:
- View existing branches.
- Identify the currently active branch.
- Switch between different lines of work.

Clear visibility helps prevent working on the wrong branch.

---

## 5. Creating and Switching Branches

Branch creation allows starting new work without disturbing existing code. Switching branches changes the active workspace so new changes apply only to that branch.

---

## 6. Branch Naming Practices

Consistent naming improves readability and collaboration:
- Branch names indicate purpose (feature, bugfix, hotfix).
- Clear names reduce confusion.
- Poorly named branches are hard to track and maintain.

Naming conventions make repositories easier to manage long-term.

---

## 7. Deleting and Cleaning Up Branches

![Image](https://git-scm.com/book/en/v2/images/basic-merging-1.png?utm_source=chatgpt.com)

![Image](https://wac-cdn.atlassian.com/dam/jcr%3Ac6db91c1-1343-4d45-8c93-bdba910b9506/02%20Branch-1%20kopiera.png?cdnVersion=3129&utm_source=chatgpt.com)

Branches are temporary by design.
- A feature branch is removed after merging.
- An experimental branch is deleted when abandoned.
- Old branches are cleaned to avoid clutter.

Regular cleanup keeps the repository organized and readable.

---

## 8. Branch Lifecycle Overview

A typical branch follows a simple lifecycle:
1. Creation for a specific purpose.
2. Active development in isolation.
3. Integration back into stable code (merge covered later).
4. Deletion after use.

This lifecycle reflects how professional teams structure development work.

---

Git manages code locally, but collaboration requires a shared remote repository. Remotes enable teams to synchronize work, review changes, and control project evolution.

## **1. Git vs GitHub**
*   Git: Local version control.
*   GitHub: Remote hosting, collaboration.
*   Git manages code; GitHub manages teamwork.

## **2. Remote Repository**
A remote repository is a Git repository stored outside the local machine.
*   Shared source of truth.
*   Stores full project history.
*   Enables collaboration and backup.

## **3. Local and Remote Relationship**
*   Work happens locally first.
*   Changes are shared explicitly (push).
*   Remote updates are pulled intentionally (pull).

## **4. Meaning of `origin`**
*   Default name for the primary remote.
*   Shortcut reference.
*   A repository can have multiple remotes.

## **5. Repository Basics**
A repository contains code, history, and branches.
*   Local: On machines.
*   Remote: On GitHub.

## **6. Cloning**
*   Creates a local copy of a remote repository.
*   Includes complete commit history.
*   Automatically links to the remote.

## **7. Push and Pull**
*   Push: Sends local changes to remote.
*   Pull: Brings remote changes locally.
*   Synchronization is always manual.

## **8. Collaboration Models**
*   **Collaborators:** Direct access to same remote.
*   **Forking:** Independent copy when direct access is restricted.

## **9. Pull Requests**
*   Propose changes to a remote repository.
*   Enable review and discussion.
*   Control what gets merged.

## **10. Review Decisions**
*   Approve: Allows merging.
*   Request changes: Blocks merging.

## **11. Typical Collaboration Flow**
1.  Remote repository exists.
2.  Work done locally.
3.  Changes pushed.
4.  Pull Request opened.
5.  Review and merge.
6.  Local copies sync again.

---

Modern dev needs shared code storage. Remote repositories provide a safe, centralized space, allowing independent local work.

### Real-World Problems Without Remotes
Without remotes, code is isolated, sharing is manual (leading to outdated/lost changes, no review, overwrites). How do teams safely collaborate without emailing files?

### What a Remote Repository Provides
A remote repo is a centralized reference: stores code/history online, allows team sync, enforces permissions/reviews, acts as backup. Local work stays private until pushed.

### Git and GitHub — Different Responsibilities
Git manages local code history. GitHub hosts repos online and manages team collaboration. Git controls **code changes**; GitHub controls **team collaboration**.

### Local and Remote Working Together
Development is local first. Changes are pushed to share; updates pulled/fetched to receive. This allows offline work and controlled sharing.

### Cloning and Connecting Repositories
**Cloning** creates a full local copy of a remote repo. A local repo can also be **connected** to a remote later. Both link local work to a shared remote.

### Sharing and Receiving Changes
**Pushing** sends local changes to remote. **Pulling** brings remote changes into your local branch (merging). **Fetching** retrieves updates without merging. Understanding this prevents conflicts.

### Collaboration Using Branches and Pull Requests
Teams use feature branches, not direct pushes to stable branches. Pull Requests (PRs) facilitate review, discussion, and controlled merging on the remote platform.

### Why Repository Access Control Matters
Remote repos are shared. Access control defines who can view, contribute, review, merge, or manage settings. It protects stable branches, enforces reviews, and ensures accountability.

### Typical Collaboration Flow
Flow: Remote repo created → permissions assigned → clone → feature branch work → push → PR review → merge → team sync.

### Quick Self-Check
Self-check: Is code backed up? Can teammates review before main? Do permissions prevent damage? This highlights remotes and access control's importance.