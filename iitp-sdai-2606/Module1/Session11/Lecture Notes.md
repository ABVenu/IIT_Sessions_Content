# Intro to VCS, Git & Repository Management

## What You Will Learn in This Lesson

In the previous session, you practised **intermediate DSA problem solving** — analysing constraints, using **nested logic** with lists and dictionaries, and applying **Bubble Sort** and **Selection Sort** on your local machine.

You can now write and run Python programs in **VS Code**. The next challenge is not "how to write code," but **how to keep that code safe, organised, and shareable**.

This lesson follows a practical order — set up first, then build:

1. **Create your GitHub account** and note your username and email
2. **Configure Git on your laptop** using the **same username and email** as GitHub
3. Understand why **version control** matters
4. Use **Git** locally with `init`, `add`, and `commit`
5. Connect to **GitHub**, then **clone**, **stage**, **commit**, and **push**

By the end, your Git identity will match your GitHub profile, and you will be able to track project history and upload code with confidence.

---

## Before You Code: Create Your GitHub Account

Start here — before running any Git commands on your laptop.

- **Official Definition:** **GitHub** is a cloud-based hosting platform for Git repositories, used for storage, sharing, and collaboration.
- **In Simple Words:** GitHub is your online developer profile and project cupboard on the internet.
- **Real-Life Example:** Like creating a college email ID before submitting assignments — you need the account first, then you upload work to it.

### Create the account

1. Open [github.com](https://github.com) in your browser.
2. Click **Sign up** and complete registration.
3. Choose a **username** carefully — this becomes your public GitHub identity.
4. Use an **email address** you check regularly (college or personal).
5. Verify your email when GitHub asks you to.

### Write these two details down

Keep them visible while you work in this session:

| Detail | Example | Your value |
|---|---|---|
| **GitHub username** | `priya-sharma-dev` | __________ |
| **GitHub email** | `priya@example.com` | __________ |

You will use **exactly these same details** when configuring Git on your laptop. Matching the **email** helps GitHub recognise your commits as yours. Matching the **username** keeps your identity consistent across tools in this course.

**Common mistake:** Using a random nickname or a different email in `git config`. Keep both values aligned with your GitHub account from day one.

---

## Configure Git with Your GitHub Identity

Git needs to know who is making each commit. Set this **once per laptop** using your GitHub username and email.

First, confirm Git is installed. Open **Terminal** (Mac) or **Command Prompt / Git Bash** (Windows):

```bash
git --version
```

**How the command works:**

- `git` calls the Git program; `--version` prints the installed version
- If you see `git version 2.x.x`, Git is ready
- If you see an error, install Git from the official website, then reopen the terminal

**Common mistake:** Using a capital `G` (`Git --version`). Keep the command lowercase: `git`.

Now configure your identity — replace the placeholders with **your GitHub username and email**:

```bash
git config --global user.name "your-github-username"
git config --global user.email "your-github-email@example.com"
```

**How the commands work:**

- `user.name` should match your **GitHub username** (not a random nickname)
- `user.email` should match the **email on your GitHub account**
- `--global` saves these settings for all Git projects on this laptop
- Every future commit will carry this identity

Verify the setup:

```bash
git config --global user.name
git config --global user.email
```

Both values should match what you wrote down from your GitHub account.

**Common doubt:** "Can I use a different email on my laptop?"  
For this course, use the **same email as GitHub** so your commits and profile stay connected without confusion.

---

## Why Version Control Matters

- **Official Definition:** **Version Control** (also called **VCS** — Version Control System) is a system that records changes to files over time so you can recall specific versions later.
- **In Simple Words:** Version control is a **time machine for your files**. It remembers every important save, with a message about what changed.
- **Real-Life Example:** Think of a college assignment register. Instead of renaming files as `final.py`, `final2.py`, and `final_really_final.py`, the register keeps dated entries: *"Monday — added average marks"* and *"Tuesday — fixed duplicate check."*

Without version control, beginners often face these problems:

- A working program breaks after a late-night edit, and the old version is lost
- Team members overwrite each other's files on a shared drive
- Nobody remembers why a change was made last week
- Sharing code means sending confusing ZIP files on WhatsApp

With version control, you get a clear **history**, the power to **go back**, a clean way to **share**, and habits every software company expects.

**Common doubt:** "I already press Ctrl+S. Is that enough?"  
Saving updates the current file only. Version control stores **many snapshots** of the project over time, not just the latest copy.

![Version control saves history — messy duplicate file names like final.py and final_really_final.py versus an organised dated timeline of safe snapshots you can return to anytime](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session11/session11-01-version-control-timeline.png?v=20260713)

### Activity: Feel the Chaos Without Version Control

Create a Desktop folder named `vcs_chaos_demo`. Add `marks.py` with `print("Version 1")`, save it, then change the text to `"Version 2"` and save again.

Now ask yourself: **What exactly was written in Version 1?** You cannot recover it unless you remembered it. That is the pain Git removes.

---

## Meet Git — The Tool You Will Use

- **Official Definition:** **Git** is a distributed version control system used to track changes in source code during software development.
- **In Simple Words:** Git is the software that sits inside your project folder and carefully records your history when you ask it to.
- **Real-Life Example:** If your project folder is a notebook, Git is the librarian who stamps each completed chapter and keeps older chapters safely on the shelf.

Key ideas:

- Git works **on your laptop first** — this is a **local repository**
- You decide when to create a snapshot (a **commit**)
- Your GitHub account (already created) is where you **push** that history online

Git is free and used by almost every professional development team. Learning it now prepares you for web apps, backend APIs, and the final capstone.

---

## Local Repository — Your Project's Private Diary

- **Official Definition:** A **repository** (short form: **repo**) is a project folder that Git is tracking, including its complete history of commits.
- **In Simple Words:** A repository is a normal folder plus a hidden Git notebook that stores snapshots.
- **Real-Life Example:** Your school bag holds books (files). The attendance register inside the bag is the history. Together, they form the "repo."

| Type | Where it lives | Simple meaning |
|---|---|---|
| **Local repository** | On your laptop | Your private copy with full history |
| **Remote repository** | On GitHub (internet) | The shared online copy for backup and collaboration |

First build confidence with the **local** side. Then connect it to the **GitHub account you created at the start**.

![Local repository as a project diary — a laptop folder with project files plus a hidden .git history register storing stamped commit snapshots, like books in a bag with an attendance register inside](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session11/session11-02-local-repository-diary.png?v=20260713)

---

## Initializing a Repository with `git init`

- **Official Definition:** `git init` creates a new Git repository in the current folder by adding a hidden `.git` directory.
- **In Simple Words:** `git init` tells Git, "Start watching this folder from now on."
- **Real-Life Example:** Buying a new homework register and writing the subject name on the first page.

1. Create a project folder, for example `scholarship_tracker`.
2. Move into that folder and initialize Git:

```bash
cd scholarship_tracker
git init
```

**How the commands work:**

- `cd scholarship_tracker` changes into the project folder
- `git init` creates a hidden `.git` folder that stores Git's internal history
- After this, the folder becomes a **local repository**
- Do **not** edit `.git` manually — Git manages it for you

**Common mistake:** Running `git init` on Desktop instead of inside the project. Always `cd` first.

---

## Checking Status with `git status`

After initializing, check status often:

```bash
git status
```

**How the command works:**

- Shows which files are **untracked** (new), **modified**, or **staged**
- Use it before and after every major step so you never feel lost

Think of `git status` as asking: *"Which notebooks are still on my desk, and which ones are already submitted for stamping?"*

---

## Creating Your First Project Files

Create `README.md`:

```md
# Scholarship Tracker

This project calculates average marks for students.
```

Create `main.py`:

```python
print("Scholarship Tracker - Version 1")  # Show a simple welcome message
```

Then run `git status`. Both files should appear as **untracked** — Git sees them, but has not recorded them in history yet.

---

## Staging Files with `git add`

- **Official Definition:** **Staging** means selecting which changed files will be included in the next commit.
- **In Simple Words:** Staging is putting chosen notebooks on the teacher's table before the stamp.
- **Real-Life Example:** Before submitting an assignment, you choose which pages to submit — not every rough note.

```bash
git add README.md
git add .
```

**How the commands work:**

- `git add README.md` stages only that file into the **staging area**
- `git add .` stages all new and modified files in the current folder
- Staging does **not** create history yet — it only prepares the next snapshot
- Run `git status` again to confirm files moved to "Changes to be committed"

Why two steps before history? You may edit five files but only two are ready. Staging keeps each commit focused on one clear purpose — like selecting exact pages at a photocopy shop instead of copying your whole bag.

**Common mistake:** Editing a file after staging, then committing without staging again. After every important edit, run `git add` again.

---

## Creating a Snapshot with `git commit`

- **Official Definition:** A **commit** is a saved snapshot of staged files along with a message, author details, and a unique ID.
- **In Simple Words:** A commit is Git's permanent stamp for one clear set of changes.
- **Real-Life Example:** The teacher stamps your homework and writes: *"13 July — Unit test answers submitted."*

Your Git identity is already configured with your GitHub username and email. Now create the commit:

```bash
git commit -m "Add README and first version of main program"
```

**How the command works:**

- `git commit -m "..."` creates a snapshot using only the staged files
- The message should briefly explain **why** this change matters
- Git attaches your configured **username** and **email** to this commit automatically

Good messages: `Add average marks function`, `Fix incorrect pass percentage formula`.  
Avoid vague messages like `update` or `changes`.

**Common mistake:** Running `git commit` when nothing is staged. Git will refuse and remind you to use `git add` first.

![Local Git workflow — edit files in your editor, stage selected files into the staging area, then commit a permanent stamped snapshot into your project history register](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session11/session11-03-edit-stage-commit-workflow.png?v=20260713)

---

## Viewing History with `git log`

```bash
git log --oneline
```

**How the command works:**

- Shows commit history in a short format
- Each line includes a short **commit ID** and your message
- This proves your work is a timeline, not a single file overwrite

---

## Activity: Complete One Local Git Cycle

In your `scholarship_tracker` folder:

1. Confirm Git works with `git status`.
2. Change `main.py` to print `"Scholarship Tracker - Version 2"`.
3. Run `git status` and notice the file is modified.
4. Stage with `git add main.py`.
5. Commit:

```bash
git commit -m "Update welcome message to Version 2"
```

6. Run `git log --oneline` and confirm at least two commits.

If you finish this cycle, you understand local Git: **edit → stage → commit**.

---

## GitHub — Connect Your Local Work Online

Local history protects one laptop. But what if it crashes, or your mentor needs to review from another city?

You already created your GitHub account at the start. Now you will use it to host projects online.

- **In Simple Words:** GitHub is the online cupboard where your Git project can live safely on the internet.
- **Real-Life Example:** Your homework register stays in your bag (local). A photocopy sits in the staff room cupboard (GitHub) so teachers can check it anytime.

| Term | Meaning |
|---|---|
| **Git** | The tool on your computer that tracks history |
| **GitHub** | The website/service that hosts repositories online |

You can use Git without GitHub. GitHub makes backup, sharing, and teamwork much easier — and is where assignments are often submitted in this course.

![Git versus GitHub — Git tracks history on your laptop in a local repository while GitHub hosts the online remote copy; push uploads commits to the cloud and clone downloads the full project back to your machine](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session11/session11-04-git-github-local-remote.png?v=20260713)

---

## Creating a Remote Repository on GitHub

1. Sign in to the **GitHub account you created earlier**.
2. Click **New repository**.
3. Name it clearly, for example `scholarship-tracker`.
4. Keep it empty for now (no README if your local project already has files).
5. Create the repository and copy its HTTPS URL.

That URL is your **remote repository** address.

- **Official Definition:** A **remote** is a named reference in Git that points to another repository, usually on a hosting service like GitHub.
- **In Simple Words:** A remote is a nickname for "the online copy of this project."
- **Real-Life Example:** Saving a contact as "Home" in your phone — nickname locally, actual address elsewhere.

---

## Connecting Local and Remote with `git remote add`

```bash
git remote add origin https://github.com/your-username/scholarship-tracker.git
git remote -v
```

**How the commands work:**

- `git remote add` creates a new remote connection
- `origin` is the common default nickname for the main remote
- The URL is the GitHub address — this only **links** local and remote; it does not upload yet
- `git remote -v` lists remotes so you can confirm `origin` is set

**Common mistake:** Adding `origin` twice. Check with `git remote -v` first.

---

## Pushing Code to GitHub with `git push`

- **Official Definition:** **Push** uploads local commits to a remote repository.
- **In Simple Words:** Push means "send my saved snapshots from my laptop to GitHub."
- **Real-Life Example:** Photocopying today's stamped register pages and placing them in the staff room cupboard.

```bash
git branch -M main
git push -u origin main
```

**How the commands work:**

- `git branch -M main` renames the current branch to `main` (common standard)
- `git push` sends local commits to the remote
- `-u origin main` sets upstream tracking so later you can simply run `git push`
- After success, refresh GitHub — your files should appear online

**Common doubt:** "Did push replace my laptop files?" No — push copies history **to** GitHub. Local files stay with you.

**Common mistake:** Pushing before any commit exists. Git needs at least one local commit.

---

## Cloning a Repository with `git clone`

The reverse skill matters too: starting from an existing GitHub project.

- **Official Definition:** `git clone` creates a local copy of a remote repository, including its files and commit history.
- **In Simple Words:** Clone means "download this whole project from GitHub to my laptop, ready for Git."
- **Real-Life Example:** Borrowing a full photocopy of a friend's project folder — not one file, but the organised pack with history.

```bash
cd Desktop
git clone https://github.com/your-username/scholarship-tracker.git
cd scholarship-tracker
```

**How the commands work:**

- `git clone <url>` downloads the repository into a new folder
- The cloned folder is already a Git repo — do **not** run `git init` again
- Run `git log --oneline` to see that history came with the download

Clone when you need a mentor's starter project, a team repo, or a fresh copy on a new laptop.

**Common mistake:** Running `git init` inside a freshly cloned folder. Cloning already includes Git setup.

After cloning, the daily rhythm stays the same: edit → `git status` → `git add` → `git commit -m "message"` → `git push`.

---

## Staging vs Committing vs Pushing — One Clear Picture

Beginners often mix these three words. Keep this separation clear:

| Action | Where it happens | What it does |
|---|---|---|
| **Stage** (`git add`) | Local staging area | Chooses which changes are ready |
| **Commit** (`git commit`) | Local repository | Saves a permanent snapshot on your laptop |
| **Push** (`git push`) | Remote (GitHub) | Uploads saved snapshots to the internet |

A useful order to remember:

1. Make the change in your editor
2. Stage only the ready files
3. Commit with a clear message
4. Push when you want GitHub to match your laptop

If you skip staging, commit has nothing useful to save. If you skip commit, push has nothing new to upload.

---

## The Complete Remote Workflow (End-to-End)

### Path A — Start a brand new project

1. Create a project folder and run `git init`
2. Create files (`README.md`, `main.py`, and so on)
3. Run `git add .` then `git commit -m "Initial commit"`
4. Create an empty repository on GitHub
5. Run `git remote add origin <url>`
6. Run `git push -u origin main`

### Path B — Start from an existing GitHub project

1. Copy the repository HTTPS URL from GitHub
2. Run `git clone <url>` and enter the folder
3. Edit files, then `git add .`
4. Run `git commit -m "Describe your change"`
5. Run `git push`

Both paths end at the same skill: work tracked locally and visible on GitHub.

![Complete remote Git workflow — create or clone a project, edit files, stage and commit on your laptop, push to GitHub, and confirm the updated files appear in the online repository](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session11/session11-05-remote-workflow-end-to-end.png?v=20260713)

---

## Activity: Stage, Commit, and Push One Real Change

Use Path A or Path B, then:

1. Update `main.py`:

```python
print("Scholarship Tracker - Version 1")  # Existing welcome line
print("Tracking student marks safely with Git")  # New line describing purpose
```

2. Run `git status` and confirm the file is modified.
3. Stage, commit, and push:

```bash
git add main.py
git commit -m "Add project purpose message in main program"
git push
```

4. Open GitHub and confirm the updated `main.py` is visible.

If the website shows your latest change, you have completed the remote workflow.

---

## Common Errors and How to Fix Them Calmly

| Situation | What it usually means | What to do |
|---|---|---|
| `not a git repository` | Outside a Git folder, or never ran `git init` / `git clone` | `cd` into the project, then init or clone correctly |
| `nothing to commit` | No staged changes, or no changes at all | Edit a file, then `git add`, then commit |
| `remote origin already exists` | Remote already linked | Check with `git remote -v` |
| Push asks for login | GitHub needs authentication | Sign in with credentials or access token as guided |
| Wrong folder tracked | `git init` ran in the parent folder | Start fresh in the correct project folder |

Mistakes are normal. Read the error, check `git status`, and move one careful step at a time.

### Quick Self-Check Before You Leave Practice

Ask yourself these four questions:

- Did I create my GitHub account and configure Git with the **same username and email**?
- Can I explain why version control is better than `final_v2.py` naming?
- Can I run `init → add → commit` on a brand new folder?
- Can I connect a local repo to GitHub and push, or clone and make one new commit?

If any answer is "not yet," repeat that part of the workflow once more before moving on.

---

## How This Fits Your Journey Ahead

You have moved from "I can write Python" to "I can protect and share my Python."

In the upcoming session, you will go deeper into **branching**, **merging**, and team-style collaboration on GitHub. Those skills depend on today's foundation: local commits and remote push/clone confidence.

Every later module — frontend, backend, and AI features — will expect project history on GitHub. Treat today's workflow as a daily professional habit.

---

## Key Takeaways

- **Create GitHub first**, then configure Git with the **same username and email** before your first commit.
- **Version control** keeps a timeline of your project so you never depend on confusing file names like `final_v3.py`.
- **Git** tracks history on your laptop using `init`, `add`, and `commit` inside a **local repository**.
- **GitHub** hosts the **remote repository** so your work is backed up online and easy to share.
- The core remote workflow is always: **edit → stage → commit → push**; use **clone** when starting from an existing online project.
- Strong Git habits now prepare you for team collaboration and every project you will build in later modules.

---

## Important Commands, Libraries, Terminologies Used

| Term / Command | Meaning in Simple Words |
|---|---|
| **VCS / Version Control** | System that records file history over time |
| **Git** | Tool that performs version control on your machine |
| **Repository (repo)** | Project folder tracked by Git, including history |
| **Local repository** | Git project stored on your laptop |
| **Remote repository** | Git project hosted online (usually on GitHub) |
| **GitHub** | Website/service for hosting and sharing Git repositories |
| **Staging area** | Waiting zone for files chosen for the next commit |
| **Commit** | Saved snapshot of staged changes with a message |
| **Clone** | Download a full remote repository to your laptop |
| **Push** | Upload local commits to the remote repository |
| **Origin** | Common nickname for the main remote connection |
| `git --version` | Check whether Git is installed |
| `git init` | Start tracking the current folder as a Git repo |
| `git status` | Show current tracked/untracked/staged state |
| `git add <file>` / `git add .` | Stage one file or all files |
| `git commit -m "message"` | Create a snapshot with a message |
| `git log --oneline` | View short commit history |
| `git remote add origin <url>` | Link local repo to GitHub URL |
| `git remote -v` | List configured remotes |
| `git clone <url>` | Copy a remote repository locally |
| `git push -u origin main` | Push commits and set upstream tracking |
| `git config --global user.name` / `user.email` | Set Git identity — use same values as your GitHub username and email |
