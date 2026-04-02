## LO–11.1.1: Version Control & Foundation of Git (15 minutes)

### 1. The Challenge: Why Version Control? (2 minutes)
Imagine you've added a new feature, but it broke everything. How do you get back your old, working code? Or, think about multiple developers working on the same file. How do you prevent overwriting each other's work? Manual file copies or shouting across desks aren't scalable. We need a systematic solution.

### 2. What is Version Control? (2 minutes)
Version Control Systems, or VCS, are tools that track every change made to your files over time. They let us:
*   Restore older versions of our code.
*   Collaborate without overwriting each other's work.
*   See the full history of who changed what and why.
*   Act as a safe backup for our project.

### 3. How Version Control Works (2 minutes)
VCS works by saving snapshots, or "versions," of your project at different points. Think of it like saving multiple drafts of a document: "Report_v1", "Report_v2". With VCS, you can instantly jump between these saved versions, compare what changed between any two points, and even revert specific changes. It's a project timeline for your code.

### 4. Problems Version Control Solves (1 minute)
VCS prevents critical issues in development:
*   Overwriting conflicts among team members.
*   Accidental deletion or irreversible changes.
*   Lack of clear history for debugging.
*   Code tied only to one machine.
It's essential for professional development.

### 5. Types of Version Control (2 minutes)
VCS evolved through three main types:
*   **Local VCS:** History on one machine (e.g., RCS). Simple, but risky if that machine fails.
*   **Centralized VCS:** A single server holds all history (e.g., SVN). Good for collaboration, but dependent on the server.
*   **Distributed VCS (DVCS):** Every developer has a full copy of the project history (e.g., Git). This is the modern standard, offering offline work and robust collaboration.

### 6. Git and GitHub (2 minutes)
**Git** is the most widely used Distributed Version Control System today. It's popular for its speed, flexibility, offline capabilities, and strong support for collaboration through branching and merging.
**GitHub** is a popular cloud-based platform where we host our Git projects. Think of Git as the tool, and GitHub as the online service that helps teams share and manage their Git projects.

### 7. Conclusion & Reflection (4 minutes)
Version Control is fundamental for modern software development. It ensures code safety, enables seamless teamwork, and makes projects manageable.
Take a moment to reflect: How do you currently track different versions of your work? How would you recover old code? Version Control is the professional answer to these challenges.

---

## LO–11.1.2: Install & configure Git identity (20 minutes)

### 1. SCM Tools Overview
Welcome! We're diving into Git. First, let's acknowledge that many Source Code Management tools exist. Some are centralized like SVN, while others, like Git, are distributed.

### 2. Why Git Dominates
Git is the industry standard for solid reasons: it works offline, operations are incredibly fast, it has strong branching and merging capabilities, built-in security, and huge community support. These make it flexible for any project size.

### 3. What is Git?
At its core, Git is a local version control tool. It tracks every change in your project, records versions through commits, allows you to experiment safely with branches, and helps merge contributions. It runs right on your machine.

### 4. Git vs. GitHub
While Git is local version control, GitHub is a cloud platform for hosting Git repositories and collaboration. Think of Git as the engine and GitHub as the garage where teams share and work on projects. GitHub enables backup, team collaboration, pull requests, and showcasing your contributions online.

### 5. GitHub Account Creation
Before installing Git, it's crucial to create your GitHub account. Please use a professional name and an email address you'll consistently use. This ensures your commits are properly attributed to your GitHub profile, which is essential for showcasing your contributions later. The signup process is straightforward on github.com/signup. We'll proceed, so please complete this step on your own during the subsequent setup time.

### 6. Git Installation
Now, let's get Git installed.
*   **Windows users:** Download the installer from git-scm.com and use the default settings.
*   **macOS users:** The easiest way is via Homebrew: `brew install git`. Alternatively, Xcode Command Line Tools also include Git: `xcode-select --install`.
*   **Linux users (Debian/Ubuntu):** Use `sudo apt update` then `sudo apt install git`.
After installation, verify it by running `git --version` in your terminal. Please proceed with your installation now.

### 7. Basic Git Setup
Finally, configure Git with your identity. This must match your GitHub account exactly for proper attribution.
Use these commands:
`git config --global user.name "Your Full GitHub Name"`
`git config --global user.email "your.email@example.com"`
You can check your settings with `git config --list`. This step is critical for tracking your contributions correctly on GitHub. Please complete this setup now.

---

## LO–11.1.3: Track & manage file changes (20 minutes)

Open your 'First-Git-Project' in VS Code and have the terminal ready.

First, let's see Git's 3-area model:

1.  **Working Directory**: Create `demo.txt` with 'Hello Git'. Save. Run `git status`. Git shows it's _untracked_—it's in your **working directory**.
2.  **Staging Area**: Stage the file: `git add demo.txt`. Run `git status`. Now it's in the **staging area**, ready for a snapshot.
3.  **Local Repository**: Commit it: `git commit -m "Add demo.txt"`. This snapshot is now in your **local repository**.

Now, let's explore `git status` further. Edit `demo.txt`, add 'Learning staging'. Save. Run `git status`. Notice the unstaged changes. `git status` is your real-time dashboard.

Let's try staging variants. Stage everything: `git add .`. Undo staging: `git reset`. Stage only modified (no new files): `git add -u`. These commands help control what gets committed.

Commit again with a meaningful message: `git commit -m "Update demo.txt"`. Messages should be short, action-based, and present tense.

View your history: `git log --oneline`. Each line is a commit, a snapshot of your project.

Finally, `git diff` to compare changes:
*   Modify file: add 'Diff practice'. Save. Run `git diff`. This shows unstaged changes (Working vs Staging).
*   Stage it: `git add demo.txt`. Run `git diff --staged`. This shows what's _about to be committed_ (Staging vs Repository).
*   Compare two commits (e.g., `git diff <commit-ID-1> <commit-ID-2>`). Git shows additions (+) and deletions (-).

Now, let's practice this full workflow:
1.  Edit any file.
2.  Run `git status`.
3.  Stage using `git add <file>`.
4.  Check with `git diff --staged`.
5.  Commit with a meaningful message.
6.  View your commit using `git log --oneline`.

---

## LO–11.1.4: Undo mistakes safely (20 minutes)

### Undoing Working Directory Changes — `git restore`

Sometimes you make unintended edits. Git helps you safely discard uncommitted changes. Let's try it: modify `app.js` with some random text. Run `git status` to see `modified: app.js`. Now, restore it: `git restore app.js`. Check `app.js` again—it's back to its last committed state. This is how you discard unwanted edits. You can also restore all uncommitted changes across your project by using `git restore .`.

### Unstaging Changes — `git reset` or `git restore --staged`

If you stage a file accidentally, Git lets you pull it back without losing your changes. Edit `config.js`, save it, and stage it: `git add config.js`. Run `git status` to confirm it's staged. To unstage it, you can use `git reset config.js` or `git restore --staged config.js`. Now, `git status` shows it's modified, but no longer staged. To unstage all files, simply run `git reset`.

### Updating the Last Commit — `git commit --amend`

You can update your most recent commit, perhaps fixing a typo or adding a forgotten file, *before* pushing it. First, make a commit, even with a mistake in the message: `git commit -m "Addd login page"`. To fix just the message, use `git commit --amend -m "Add login page"`. If you forgot to include a file, first stage it (e.g., `git add validation.js`), then run `git commit --amend` without a message. This updates the previous commit to include the staged file.

### Choosing the Correct Undo Action

To summarize: use `git restore <file>` to discard uncommitted working directory changes. Use `git reset <file>` or `git restore --staged <file>` to unstage changes from the staging area. And use `git commit --amend` to fix the last commit's message or contents, but only *before* pushing it to a shared remote.

---

## LO–11.1.5: Develop features using branches (20 minutes)

### 1. Start with an Ideal Scenario Activity

- Imagine a team:
  - Developer 1: new feature
  - Developer 2: another new feature
  - Developer 3: critical bug fix
  - Developer 4: experimental change
- All modify the same project, sometimes the same file.

- Can all push to `main` directly? What if a feature is incomplete, or an experiment breaks things? Can a bug fix be released alone?

- Direct work on `main` mixes unrelated changes, risks breaking stable code, and makes parallel development unsafe.

- We need a system for independent work, selective acceptance, and stable code protection.

---

### 2. Connect to Branching

- In professional development, `main` means stable, production-ready code.
- New features, fixes, experiments should not disturb `main`'s stability.
- Git **branching** provides this solution: **isolation**.

---

### 3. Introduce the Concept of a Branch

- A branch is an independent line of development.
- Each branch has its own commit history. Changes in one don't affect others.
- `main` is the default stable branch.
- Branching allows parallel work without conflict.

---

### 4. Explain Isolated Development Using Branches

- Branches allow:
  - Feature development without risk
  - Bug fixes without blocking work
  - Experiments without fear of failure
- Each developer works on a separate branch. Only completed, approved work integrates with `main`.
- Each branch acts like a separate workspace.

---

### 5. Demonstrate Viewing Existing Branches

- To list local branches, use:

  ```bash
  git branch
  ```

- The `*` indicates your current branch. Always know your current branch before making changes.

---

### 6. Demonstrate Creating a Branch

- To create a new branch without switching to it:

  ```bash
  git branch feature-login
  ```

- The branch is created, but you remain on your current branch. Verify with `git branch`.

---

### 7. Demonstrate Switching Between Branches

- To switch to an existing branch:

  ```bash
  git switch feature-login
  # or
  git checkout feature-login
  ```

- All new work now belongs to `feature-login`. Your context entirely switches.

---

### 8. Demonstrate Creating and Switching in One Step

- The most common workflow: create and switch immediately:

  ```bash
  git checkout -b feature-signup
  # or
  git switch -c feature-signup
  ```

---

### 9. Working Inside an Isolated Branch

- Typical workflow:
  1. Switch to a branch.
  2. Modify or create files.
  3. Stage and commit changes.

  ```bash
  git switch feature-login
  git add login.js
  git commit -m "Add login form UI"
  ```

- Switch back to `main` (`git switch main`). Notice your login changes are not there. Isolation is preserved.

---

### 10. Student Practice — Repeat Isolation

- Now, you create a new branch, switch to it, make a small change, commit it, then switch back to `main`.
- Try this twice: once for a `bugfix-header`, once for an `experiment-dark-mode`.

---

### 11. Introduce Branch Naming Conventions

- Recommended patterns:
  - `feature-login`
  - `bugfix-navbar`
  - `hotfix-payment-issue`
  - `experiment-ui-layout`
- Rules: lowercase, hyphen-separated, purpose-driven. Avoid generic names.

---

### 12. Demonstrate Deleting Branches

- Branches are temporary. After merging, they should be deleted.
- Safe deletion (only if merged):

  ```bash
  git branch -d feature-login
  ```

- Force deletion (for unmerged/abandoned branches):

  ```bash
  git branch -D experiment-old-ui
  ```

---

### 13. Branch Cleanup Best Practices

- Cleanup is crucial to avoid clutter, reduce confusion, and prevent outdated work.
- Recommended flow:

  ```bash
  git switch main
  git branch -d feature-login
  ```

---

### 14. Explain Branch Lifecycle

- Stages:
  - Branch creation
  - Active development
  - Merge into main (our next topic)
  - Branch deletion
- This lifecycle is standard in professional teams.

---

### 15. Conclude with Key Takeaways

- Remember:
  - One task per branch.
  - `main` must remain stable.
  - Branches enable parallel, safe development.
  - Cleanup is mandatory.
- Next, we'll see how to integrate these isolated changes back into `main`.

---

## LO–11.2.1: Configure & synchronize remote repositories (20 minutes)

### **1. Team Collaboration & Remote Repositories**
*   **Problem:** Multiple developers, shared codebase, how to sync work and avoid overwrites? Local Git is for individuals. Teamwork needs a shared system.
*   **Solution:** A **remote repository**.
*   **Git vs. GitHub:** Git manages code history *locally*. GitHub enables collaboration *remotely* – it's an online platform. Git works offline; GitHub is online.
*   **Remote Repository Definition:** A Git repo stored outside your local machine, typically on a server like GitHub. It's the shared source of truth, central for collaboration, and a project backup. Every developer has a local repo; all connect to the same remote.

### **2. Local-Remote Mechanics & "origin"**
*   **Work Flow:** You make code changes and commits *locally*. Nothing is shared automatically.
*   **Synchronization:** Changes go to remote only when you **push**. Remote changes come locally only when you **pull**. This allows offline work and controlled sharing, isolating local mistakes.
*   **"origin":** This is the conventional name for the primary remote repository. It's a shortcut, not a special keyword. A project can have multiple remotes, but `origin` usually points to GitHub.
*   **Repository Definition:** A container holding source code, commit history, branches, etc. Differentiate local (your machine) from remote (GitHub). Collaboration depends on the remote.

### **3. Setting Up & Syncing**
*   **Creating on GitHub:** Establishes a remote location, defines ownership/access. At this point, no local machine is connected; the repo exists in the cloud.
*   **Cloning:** Creates a local copy of a remote repo. It provides project files, full history, and automatically connects your local repo to the remote (`origin`). After cloning, you work locally and can sync.
*   **Synchronization:** Use `pull` to get remote changes to local, `push` to send local changes to remote. Git *never* syncs automatically; you explicitly decide when to share, preventing accidental overwrites.

### **4. Collaboration Models**
*   **Collaborators:** Contributors with direct access to a remote repository. They can push branches/commits and participate in reviews. Typical for company teams or trusted contributors.
*   **Permission Management:** Not all collaborators have equal access. GitHub enforces permissions to protect branches, control approvals, and ensure accountability. Local Git doesn't control this.
*   **Forking:** An alternative when direct write access isn't granted. You create a *separate remote repository* under your own account. The original repo remains protected; you work independently.

### **5. Pull Request Workflow**
*   **Pull Requests (PRs):** A request to merge your changes into a remote repository. PRs exist entirely on GitHub. They connect branches (or forks to original repo).
*   **Purpose of PRs:** Code review, discussion, approval tracking, controlled merging.
*   **Review and Decision:** After a PR is opened, reviewers examine changes, provide feedback, and discuss.
    *   **Approve:** Allows the merge.
    *   **Request Changes:** Blocks merge until issues are resolved. This ensures quality control.

### **6. End-to-End Collaboration Cycle & Conclusion**
*   **Typical Workflow:**
    1.  Remote repo on GitHub.
    2.  Developers clone/fork.
    3.  Work locally.
    4.  Push changes to remote.
    5.  Create a Pull Request.
    6.  Code review occurs.
    7.  Approved changes are merged.
    8.  Remote repo updates.
    9.  Local repos sync again (pull).
    This cycle repeats continuously.
*   **Conclusion:** Git manages history. GitHub manages collaboration. Remote repositories are the backbone of teamwork, enabling organized, reviewed, and synchronized development.
*   **Next:** Hands-on implementation of GitHub collaboration workflows.

### **6b. One rhythm to memorize — mirrors Lecture Notes Part VIII**

Say: “Everything we fragmented across Parts III–VII is really **one path**. When you’re lost, open **Part VIII** in the Notes.”

Speak through the block slowly; pause after `push -u` and stress that **opening a PR is in the browser**, not in Git.

```bash
git clone <repo-url>
cd <repository-folder>

git switch -c feature-login
# make changes in the editor

git add .
git commit -m "Add login feature"
git push -u origin feature-login
# GitHub → Create Pull Request (feature-login → main) → review → merge
```

*   Emphasize **`git push -u origin feature-login`**: first time you publish that branch, `-u` links local to remote; later, `git push` on that branch is often enough.
*   Remind: **Pull Request is not a Git command** — it’s the team’s gate to merge safely.
*   Optional habit before *new* work (also in Part VIII):

```bash
git switch main
git pull origin main
git switch -c feature-your-next-task
```

*   If they break something **before** the push, undo with **Part IV** patterns (`restore`, unstage, `amend`). After the push, they coordinate with the team — no silent history rewrites.

---

## LO–11.2.2: Collaborate using PRs & repository access control (20 minutes)

### 1. Introduce the Need for a Remote Repository
Git manages code locally; collaboration requires a shared **remote repository**. It hosts project code centrally, defines ownership, enforces collaboration rules, and acts as the **single source of truth**. Initially, it exists only on GitHub without any local connection.

### 2. Demonstrate Creating a Remote Repository (Manual Demo)
(Open GitHub in browser) We'll create a repository. (Walk through: name, visibility, description). Explain: At this point, the repository exists only on GitHub. No code is present locally, and access rules are controlled remotely. We are not connecting any local repository yet.

### 3. Demonstrate Cloning a Remote Repository (Manual Demo)
Cloning creates a local working copy of the remote repository. (Demonstrate `git clone <repository-URL>`). This downloads all project files, copies the full commit history, and automatically configures a remote named `origin`. Now, developers work locally, using the remote as the shared reference point.

### 4. Demonstrate Connecting an Existing Local Repository to a Remote (Manual Demo)
Imagine you started a project locally, and the remote repository was created later. (Demonstrate `git remote add origin <remote-repository-url>`). This registers the remote and names it `origin` by convention. It does not push code automatically. Your local and remote are now connected, but not synchronized.

### 5. Demonstrate Pushing Code to the Remote (Manual Demo)
Pushing transfers your local commits to the remote. (Demonstrate `git push origin main`). This uploads your commits, updates the remote branch, and makes your changes visible to collaborators. Pushing is explicit; nothing is shared without intent.

### 6. Demonstrate Upstream Branch Concept (Manual Demo)
The first push often establishes a long-term relationship. (Demonstrate `git push -u origin main`). Using `-u` sets an upstream branch, linking your local branch to its remote counterpart. This simplifies future `git push` and `git pull` commands, reducing repetition and mistakes.

### 7. Demonstrate Pull vs Fetch (Manual Demo)
To receive updates from the remote: (Demonstrate `git fetch origin`). Fetching downloads changes, but your local branches remain unchanged. It's a safe inspection step. (Demonstrate `git pull origin main`). Pulling fetches changes AND immediately merges them into your current branch. Remember, `git pull = git fetch + git merge`. Understanding this distinction prevents unintended merges.

### 8. Demonstrate Collaboration Using Branches (Manual Demo)
Professional teams do not push directly to `main`. Instead, (Demonstrate: creating a feature branch and pushing it to the remote). Each branch represents isolated work, ensuring shared branches remain stable. This prepares us for Pull Requests.

### 9. Demonstrate Pull Requests (Manual Demo)
(Open GitHub and show the Pull Request interface). (Demonstrate: selecting source and target branches, writing a PR title and description). A Pull Request (PR) requests integration of changes, initiates review and discussion, and controls when code is merged. (Conclude hands-on). All further concepts will be explained theoretically.

## Theoretical Explanation (No Live Demo from This Point)

### 10. Explain Pull Requests as a Collaboration Contract
Pull Requests are a formal agreement to merge changes. PRs document what was changed and why, record discussions permanently, and provide approval control. Importantly, PRs exist only on the remote platform; local Git has no concept of PRs.

### 11. Explain Repository Access Control
A remote repository is a shared resource. Access control defines who can push, who can review, who can merge, and who can manage settings. This control is enforced at the remote level only.

### 12. Explain Why Access Control Is Essential
Without access control, risks include production breakage, accidental deletions, and a lack of accountability. With it, you gain a protected `main` branch, mandatory reviews, and clear responsibilities – the foundation of safe collaboration.

### 13. Explain Role-Based Access Types
GitHub roles include Read, Write, Maintain, and Admin. Each role allows specific actions, with intentional restrictions to minimize risk.

### 14. Explain How Access Control Is Enforced
Enforcement involves an identity check, role validation, and action authorization. For example, a push might be blocked due to missing permission, or a merge due to an insufficient role.

### 15. Explain Adding and Managing Collaborators
To add a collaborator, you send an invitation and assign a permission level; the collaborator must accept. Access can be modified or revoked immediately, protecting against outdated permissions.

### 16. Explain Access Control Impact on Pull Requests
Permissions influence PRs by defining who can open them, who can approve, and who can merge. This separates contribution from decision-making, ensuring the stability of shared branches.

### 17. Walk Through End-to-End Collaboration Flow
The complete lifecycle involves: remote repository creation, role assignment, cloning, branch creation, local commits, pushing to remote, Pull Request creation, review and approval, merging, and synchronization. All steps are governed by remote access rules.

### 18. Close the loop — Lecture Notes Part VIII (anchor)

**Say:** “We’ve walked policies and demos; your **take-home spine** is **Part VIII** in the Lecture Notes. That section is deliberately short: one happy path, one ‘before I start new work’ habit, and a table that points back to Parts III–VII if you need detail.”

*   Project the Part VIII code block (clone → `cd` → `git switch -c` → edit → `git add .` → `git commit -m` → `git push -u` → **Create PR on GitHub**). Ask the room to read it once silently — this is the answer to “what do I actually run?”
*   Repeat the **three-sentence summary**: (1) work on a branch, not directly on `main` when collaborating; (2) push the branch and open a PR; (3) merge only after review.
*   Point to the **Part VIII habit**: `git switch main` → `git pull origin main` → `git switch -c feature-…` so every new task starts from up-to-date shared history.
*   Remind them **Part VIII’s map table** lists where each command is explained (Part III vs V vs VI vs VII) — it’s the index for self-study.
*   One line on safety: **Part IV** for mistakes before `push`; after `push`, use team process, not solo `amend` / force-push, unless everyone agrees.