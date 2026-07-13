# Git Remotes, Branching & Advanced Operations

## What You Will Learn in This Lesson

In the previous session, you set up **Git** and **GitHub**, configured your identity, and practised the core loop: **init → add → commit → push** (and **clone** when starting from an existing online project).

You can already keep a safe history of one line of work on `main`. Real projects need more — teammates (or even your future self) often work on features in parallel without breaking the stable copy.

In this lesson, you will learn:

- What a **branch** is and why teams create them
- How to **create**, **switch**, and **list** branches with Git
- How to **merge** a finished branch back into the main line
- How to **spot and resolve merge conflicts** calmly
- How to **collaborate** on a shared GitHub repository (pull, push on a branch, and open a pull request)

By the end, you will treat branching as a normal daily habit — not a scary advanced topic.

---

## Quick Refresh: Local, Remote, and Why Branches Exist

Before branching, lock one mental picture:

| Place | What it is | Simple picture |
|---|---|---|
| **Local repository** | Git project on your laptop | Your personal notebook |
| **Remote repository** | Copy on GitHub | The shared cupboard in the cloud |
| **`main` (or `master`)** | Default stable branch | The "published" version everyone trusts |
| **Feature branch** | Separate line of work | A draft notebook page for one idea |

- **Official Definition:** A **remote** is a Git repository hosted elsewhere (usually GitHub) that your local repo can push to and pull from.
- **In Simple Words:** Remote means "the online copy," not a different kind of Git.
- **Real-Life Example:** Your phone gallery is local; Google Photos backup is remote. Both hold photos, but in different places.

**Why branches are needed now:** If everyone edits only `main` at the same time, unfinished experiments mix with working code. Branches let you build a feature safely, then merge when it is ready.

**Common doubt:** "I already push to GitHub. Isn't that enough?"  
Pushing saves history. **Branches** organise *parallel* history so multiple ideas can grow without colliding every minute.

---

## Introduction to Branching

- **Official Definition:** A **branch** in Git is a movable pointer to a commit, allowing an independent line of development from the same project history.
- **In Simple Words:** A branch is a named path of work — like a side road that later rejoins the highway.
- **Real-Life Example:** In a college fest committee, the main plan stays on the official notice board (`main`). The decoration team keeps draft ideas in a separate notebook (`feature/decorations`). When approved, those notes join the official plan (a **merge**).

### Why branching matters

- Try risky changes without breaking the stable `main` copy.
- Work on Feature A while a teammate works on Feature B.
- Pause one feature and switch to a bug fix on another branch.
- Reviewers can look at one feature at a time before it joins `main`.

**Logic to remember:** Branch early for a clear purpose. Name the branch after the work (`add-login`, `fix-typo`) — not after yourself (`rahul-branch`).

![A branch is a side road off the main highway — main stays stable while feature-welcome-message grows in parallel, then rejoins through a merge like fest draft notes joining the official notice board](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session12/session12-01-branching-side-road.png?v=20260713)

---

## Creating and Switching Branches

Always know where you stand before you edit files.

```bash
git status
git branch
```

**How the commands work:**

- `git status` shows `On branch main` (or another name) near the top — that branch receives your next commit
- `git branch` lists local branches; the one with `*` is current
- **Common mistake:** Editing without reading `On branch ...`

### Create a branch (without switching yet)

```bash
git branch feature-welcome-message
```

**How the command works:**

- `git branch` followed by a name creates a new branch pointer
- The new branch starts from your **current commit**
- You stay on the old branch until you switch

### Switch to an existing branch

```bash
git switch feature-welcome-message
```

**How the command works:**

- `git switch` moves you onto the named branch
- Your working folder updates to match that branch's files
- Future commits will go to `feature-welcome-message`
- Prefer `git switch` over older `git checkout` for changing branches — it is clearer for beginners

### Create and switch in one step (recommended)

```bash
git switch -c feature-welcome-message
```

**How the command works:**

- `-c` means **create** the branch and switch to it immediately
- This is the most common day-to-day pattern for starting new work
- Confirm with `git status` — you should see `On branch feature-welcome-message`

### Naming tips that keep teams happy

- Use lowercase and hyphens: `add-student-form`, `fix-null-error`
- Keep names short but meaningful
- Avoid spaces and special symbols
- One purpose per branch — do not mix "login + payment + UI redesign" on one branch

**Real-Life Example:** Naming a branch `feature-welcome-message` is like labelling a folder `Fest_Decor_Draft_2026` instead of `misc_stuff`.

![Create and switch branches — git branch creates a new path, git switch moves you onto it, and git switch -c does both in one step like changing lanes between main and a feature branch](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session12/session12-02-create-switch-branches.png?v=20260713)

### Activity: Confirm Your Starting Point

1. Open a practice repository from the previous lesson (or create a small new one with at least one commit).
2. Run `git status` and `git branch`.
3. Write down: **Current branch = ______**

You should see `main` (or `master`) with the `*` marker before you create a new branch.

---

## Making Commits on a Feature Branch

Once you are on the feature branch, the familiar loop stays the same.

Create or edit `main.py`:

```python
# main.py — simple student helper message for practice
print("Welcome to Scholarship Tracker")  # Show the app name
print("Feature branch practice: greeting improved")  # Temporary practice line
```

Stage and commit on the branch:

```bash
git add main.py
git commit -m "Improve welcome message on feature branch"
git status
git log --oneline --graph --decorate -5
```

**How the commands work:**

- `git add` stages the file; `git commit -m "..."` saves the snapshot **on the current branch only**
- `git status` confirms a clean tree; the log graph shows recent commits and branch tips
- Commits on a feature branch do **not** appear on `main` until you merge — that isolation is the point

### Activity: One Feature, One Branch

1. From `main`, run `git switch -c feature-welcome-message`.
2. Edit `main.py`, then stage and commit with a clear message.
3. Confirm `*` is next to your feature branch with `git branch`.
4. Switch back with `git switch main`, open `main.py`, and notice the new line is **gone** here (it still exists on the feature branch).

This "disappearing line" moment is when branching becomes real for most learners.

---

## Pushing a Branch to GitHub

Local branches are useful. Sharing them on GitHub lets mentors and teammates review your work.

```bash
git switch feature-welcome-message
git push -u origin feature-welcome-message
```

**How the commands work:**

- Be on the branch you want to publish; `git push` uploads commits
- `-u origin feature-welcome-message` sets **upstream tracking** so later plain `git push` / `git pull` work on this branch
- After a successful push, GitHub shows the branch in the branch dropdown

**Common mistake:** Running `git push` while still on `main` after committing on a feature branch. Check `git status` first.

**Common doubt:** "Do I push every branch?" Push branches you want backed up or reviewed.

---

## Introduction to Merging

- **Official Definition:** A **merge** combines the commit histories of two branches into one, bringing changes from a source branch into a target branch.
- **In Simple Words:** Merging means "copy the finished side-road work back onto the main highway."
- **Real-Life Example:** After the decoration notebook is approved, the secretary updates the official fest plan with those final points.

### Typical merge workflow

1. Finish and commit all work on the feature branch.
2. Switch to the receiving branch (usually `main`).
3. Update `main` from GitHub if needed (`git pull`).
4. Merge the feature branch into `main`, then push.
5. Optionally delete the feature branch after a successful merge.

```bash
git switch main
git pull origin main
git merge feature-welcome-message
git push origin main
```

**How the commands work:**

- `git switch main` puts you on the receiving branch
- `git pull origin main` brings remote updates before you merge
- `git merge feature-welcome-message` joins that branch into `main`
- `git push origin main` publishes the combined result

If Git can combine cleanly, you get a smooth merge (sometimes a **fast-forward** when history is simple). If both sides edited the same lines, Git pauses for a **conflict**.

![Merge workflow — finish work on a feature branch, switch to main, pull latest updates, merge the feature in, then push so the combined history is shared on GitHub](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session12/session12-03-merge-workflow.png?v=20260713)

### Activity: Merge Your Feature into Main

1. Ensure your feature branch has at least one commit.
2. Switch to `main` and run `git merge feature-welcome-message`.
3. Confirm the feature line is now in `main.py`.
4. Run `git log --oneline --graph --decorate -8` and observe how history connects.

You have completed the core pattern: **branch → commit → merge → push**.

---

## Understanding and Resolving Merge Conflicts

Conflicts sound scary. They are simply Git asking you to choose when two edits cannot be auto-combined.

- **Official Definition:** A **merge conflict** occurs when Git cannot automatically reconcile competing changes to the same part of a file during a merge.
- **In Simple Words:** Two branches changed the same lines differently, and Git needs you to pick the final wording.
- **Real-Life Example:** Two classmates edit the same paragraph offline, then try to combine — both versions are highlighted until someone decides.

Conflicts usually appear when the same lines were edited on `main` and a feature branch. **Prevention:** keep feature branches short-lived and pull `main` regularly.

### Setup: create a deliberate conflict

Use a **fresh branch** for this drill so it does not clash with earlier merge practice.

On `main`, create `notes.txt` with:

```text
Team motto: Practice daily
```

Commit on `main`. Then create and switch to a new branch:

```bash
git switch -c feature-motto
```

On `feature-motto`, change the same line to:

```text
Team motto: Practice daily with Git branches
```

Commit on `feature-motto`. Switch back to `main` and change the same line to:

```text
Team motto: Practice daily and push often
```

Commit on `main`. Now merge the feature branch:

```bash
git switch main
git merge feature-motto
```

Git will stop and report a conflict in `notes.txt`.

### What conflict markers look like

Open the file. You may see markers like this:

```text
<<<<<<< HEAD
Team motto: Practice daily and push often
=======
Team motto: Practice daily with Git branches
>>>>>>> feature-motto
```

**How to read the markers:**

- `<<<<<<< HEAD` starts **your current branch** version (here: `main`)
- `=======` separates the two versions
- `>>>>>>> feature-motto` ends the **incoming** branch version
- Everything between the markers is temporary scaffolding — it must not remain in the final file

![Resolve merge conflicts calmly — two branches edited the same line differently, Git highlights both versions with markers, you choose the final wording, delete the markers, and save a clean combined file](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session12/session12-04-merge-conflict-resolution.png?v=20260713)

### Fix the file like a professional

1. Decide the final correct content (keep one side, or write a combined sentence).
2. Delete all conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`).
3. Save the clean file. Example final line:

```text
Team motto: Practice daily with Git branches and push often
```

4. Tell Git the conflict is resolved:

```bash
git add notes.txt
git commit -m "Resolve merge conflict in team motto notes"
```

**How the commands work:**

- After editing, `git add` marks the file as resolved
- `git commit` completes the merge commit
- Run `git status` until the working tree is clean
- To cancel mid-merge: `git merge --abort` returns you to the pre-merge state

**Common mistakes:** Leaving `<<<<<<<` in the file; forgetting `git add` before commit.

### Activity: Resolve One Conflict End-to-End

1. Create the deliberate conflict using the steps above (or a similar two-line edit).
2. Run the merge and open the conflicted file.
3. Remove markers and keep one clear final version.
4. `git add` the file and finish the merge commit.
5. Push `main` to GitHub and confirm the clean file online.

If the online file has **no** conflict markers, you resolved it correctly.

---

## Collaboration on Shared GitHub Repositories

Branching becomes powerful when more than one person shares a remote.

- **Official Definition:** **Collaboration** on GitHub means multiple people contribute to the same remote repository using branches, reviews, and controlled merges.
- **In Simple Words:** Everyone clones the same project cupboard, works on labelled draft shelves (branches), and only approved drafts join the main shelf.
- **Real-Life Example:** A group assignment folder where each member edits a chapter draft, then the team lead merges chapters into the final submission.

### Core collaboration habits

- **Clone once** — do not run `git init` again inside a cloned folder.
- **Pull before you push** on shared branches (especially `main`).
- Prefer **feature branches + pull requests** instead of everyone committing straight to `main`.
- Write clear commit messages so teammates understand history without calling you.

```bash
git switch main
git pull origin main
```

**How the commands work:**

- `git pull` fetches remote updates and merges them into your current branch
- Do this at the start of work and before creating a new feature branch from `main`
- If pull reports conflicts, resolve them the same way you practised earlier

**Common mistake:** Coding for days without pulling, then facing a giant conflict pile. Small, frequent syncs are kinder.

---

## Pull Requests: The Team Review Door

Pushing a branch uploads code. A **pull request (PR)** asks to merge that branch into another branch (usually `main`) with discussion and review.

- **Official Definition:** A **pull request** is a GitHub workflow request to merge one branch into another, typically with review comments before the merge happens.
- **In Simple Words:** A PR is a polite request: "Please review my feature branch and merge it into main if it looks good."
- **Real-Life Example:** Submitting an assignment draft to a mentor for comments before the final upload.

### Simple PR workflow

1. Create and commit on your feature branch, then `git push -u origin <branch>`.
2. On GitHub, click **Compare & pull request** (or **Pull requests → New**).
3. Set base to `main` and compare to your feature branch.
4. Write a short title and description (what changed, why, how to test).
5. Create the PR; after review (or self-review in practice), merge on GitHub.
6. On your laptop: `git switch main` then `git pull` so local `main` matches.

**Common doubt:** "Can I merge my own PR while learning?"  
Yes for practice repos. On real team projects, follow the team's review rules.

![Pull request collaboration — push your feature branch to GitHub, open a PR for review, discuss changes, then merge into main so the team shares one trusted codebase](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module1/session12/session12-05-pull-request-collaboration.png?v=20260713)

### Activity: Open One Practice Pull Request

1. Create a tiny change on a new branch (one line in `README.md` is enough).
2. Push the branch, open a PR into `main`, and read the Files changed tab.
3. Merge the PR (practice repo), then `git pull` on local `main`.

You have now practised the collaboration loop used in industry and hackathons.

---

## A Clean Daily Workflow You Can Reuse

Use this checklist whenever you start work on a shared project:

1. `git switch main`
2. `git pull origin main`
3. `git switch -c short-feature-name`
4. Edit → `git status` → `git add` → `git commit -m "..."` (repeat as needed)
5. `git push -u origin short-feature-name`
6. Open a pull request on GitHub
7. After merge, `git switch main` and `git pull origin main`
8. Delete the old local branch if you no longer need it:

```bash
git branch -d short-feature-name
```

**How the delete command works:**

- `-d` deletes a branch that is already merged (safe delete)
- Git refuses if the branch still has unmerged work (protection)
- Use `-D` only when you intentionally discard an unmerged branch

---

## Common Errors and How to Fix Them Calmly

| Situation | What it usually means | What to do |
|---|---|---|
| `Your branch is behind 'origin/main'` | Remote has commits you lack | `git pull` before merging or pushing |
| Merge conflict markers in files | Merge paused for manual fix | Edit file, remove markers, `git add`, commit |
| `error: you need to resolve your current index first` | Merge still in progress | Finish resolving or run `git merge --abort` |
| Pushed to wrong branch | Commits landed where you did not intend | Check `git status` / `git log`; discuss recovery with a mentor if unsure |
| `branch is not fully merged` on delete | Branch still has unique commits | Merge first, or keep the branch until work is finished |
| PR cannot merge cleanly | Conflicts between PR branch and base | Update your branch from `main`, resolve, push again |

Mistakes are normal. Read the error, check `git status`, and take one careful step.

### Quick Self-Check Before You Leave Practice

- Can I create a branch with `git switch -c ...` and commit only on that branch?
- Can I merge a feature branch into `main` and explain what merge means?
- Can I recognise conflict markers and produce a clean final file?
- Can I push a branch and open a pull request on GitHub?
- Do I pull `main` before starting new shared work?

If any answer is "not yet," repeat that activity once more.

---

## How This Fits Your Journey Ahead

You have moved from "I can save and share one line of history" to "I can develop in parallel, merge safely, and collaborate like a team."

In the upcoming session, you will use **AI coding tools** to strengthen DSA intuition — explaining concepts, generating pseudocode, and debugging with assistance. Clean Git habits will still matter: keep AI-assisted experiments on feature branches so `main` stays trustworthy.

---

## Key Takeaways

- A **branch** is a separate line of work; create it with purpose and switch with `git switch` / `git switch -c`.
- **Merge** brings finished branch work into `main`; pull latest remote changes before merging on shared projects.
- **Merge conflicts** are normal decisions — remove markers, keep the correct final text, then `git add` and commit.
- **Collaboration** works best with feature branches, frequent `git pull`, and **pull requests** before joining `main`.
- The reusable loop: update `main` → new branch → commit → push branch → open PR → merge → pull `main` again.

These habits prepare you for every group project and every later module where code lives on GitHub.

---

## Important Commands, Libraries, Terminologies Used

| Term / Command | Meaning in Simple Words |
|---|---|
| **Branch** | Named line of development in a repository |
| **`main` / `master`** | Default stable branch in most projects |
| **Feature branch** | Short-lived branch for one piece of work |
| **Merge** | Combine one branch's history into another |
| **Merge conflict** | Same area changed differently; needs manual choice |
| **Conflict markers** | `<<<<<<<`, `=======`, `>>>>>>>` temporary guides in files |
| **Remote / origin** | Online repository connection (usually GitHub) |
| **Pull** | Download remote commits and update your current branch |
| **Push (branch)** | Upload your branch commits to GitHub |
| **Upstream (`-u`)** | Saved link between local branch and remote branch |
| **Pull request (PR)** | GitHub request to review and merge a branch |
| **Fast-forward** | Simple merge where history moves forward cleanly |
| `git branch` | List local branches (`*` = current) |
| `git switch <name>` | Move to an existing branch |
| `git switch -c <name>` | Create a branch and switch to it |
| `git merge <branch>` | Merge named branch into the current branch |
| `git merge --abort` | Cancel an in-progress merge |
| `git pull origin main` | Update local `main` from GitHub |
| `git push -u origin <branch>` | Publish branch and set tracking |
| `git branch -d <name>` | Delete a merged local branch |
| `git log --oneline --graph --decorate` | Short visual history of branches and commits |
| `git status` | See current branch, changes, and conflict state |
