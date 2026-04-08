# Version control and GitHub

Projects drift: new features break old behavior, two people edit the same file, and “final_final_v2” copies stop scaling.

**Version control** records every saved state with context, lets you compare and revert, and gives teams a disciplined way to merge work instead of emailing zips.

**Git** is the tool on your machine. **GitHub** (and similar hosts) stores the shared **remote**, backs up history, and layers review and permissions on top.

Below follows the lecture thread: why VCS, Git vs GitHub and VCS shapes, the **three-area** workflow, undoing mistakes, **branching**, **remotes** and sync, collaboration (**PRs**, access), and the compact **end-to-end** rhythm from the notes.

## 1. Why version control matters (summary)

| Situation | Without version control | With version control |
| --- | --- | --- |
| Need yesterday’s working tree | Guess which folder; diffs by hand | Checkout or reset to a known commit |
| Two authors, one file | Overwrites; who changed what unclear | History, merge workflow, blame |
| Try risky refactor | Fear of losing stable code | **Branch**; discard or merge when ready |
| Laptop dies | Local file loss | **Remote** holds full repo + history |
| Release debugging | “When did this break?” opaque | **Log** and **diff** between commits |

The point is not backup alone—it is **repeatable, attributable evolution** of the codebase.

## 2. Git, GitHub, and shapes of VCS

**Local** systems keep history on one machine (fragile). **Centralized** (e.g. SVN): one server is canonical, so you need the network for many operations.

**Distributed** (Git, Mercurial): every clone carries full **history**; you can work offline and sync by **push** / **pull** when connected. Industry practice centers on **Git**.

| Aspect | Git | GitHub |
| --- | --- | --- |
| Runs where | Your computer (CLI) | Cloud service (browser + API) |
| Needs internet | No, for commit/log/branch locally | Yes, for hosting and PR UI |
| Main job | Track versions, branches, merges | Host **remotes**, permissions, PRs, CI hooks |

Git answers *how the graph of commits evolves*; GitHub answers *how people share and gate changes*.

## 3. The three-area model and the daily loop

Git places every file change in a lifecycle: **working directory** (your edits) → **staging area** (index: what will go into the next snapshot) → **local repository** (**commit**: permanent snapshot with ID and message).

**Semantics.** Nothing is “saved to history” until **`git commit`**.

**`git add`** moves paths from working tree into staging so you can craft intentional commits instead of dumping every accidental edit.

```bash
git status          # what changed, what is staged
git add path/to/file
git diff            # working tree vs staging (unstaged)
git diff --staged   # staging vs last commit
git commit -m "Add login route handler"
git log --oneline
```

**Commit messages** in professional style: short, imperative (“Add…”, “Fix…”), specific—avoid “changes” or “update stuff”.

## 4. Undoing at the right stage

The fix depends on where the mistake lives:

| Stage | Intent | Typical command |
| --- | --- | --- |
| Working directory | Drop uncommitted edits | `git restore file` or `git restore .` |
| Staging | Unstage but keep edits | `git restore --staged file` or `git reset file` |
| Last commit only | Fix message or add forgotten files | Stage, then `git commit --amend` |

**Semantics of `git commit --amend`.** Replaces the tip commit (new hash).

**Safe before `push`** to a branch others rely on; after sharing, rewriting history needs team agreement.

## 5. Branching

**Why.** Stable **main** (or **master**) should not accumulate half-done features.

A **branch** is a movable pointer to a commit—a separate line of development until you integrate.

**Create / switch.**

```bash
git branch                    # list; * marks current
git branch feature-login      # create, stay put
git switch feature-login      # move HEAD (modern)
git switch -c feature-signup  # create and switch
```

**Cleanup.** `git branch -d name` deletes if merged; `-D` forces.

Deleting stale branches keeps `git branch` output honest.

**Naming.** Prefix by intent: `feature-…`, `bugfix-…`, `hotfix-…`; lowercase, hyphens; avoid `temp` / `test`.

The lecture ties **merge** to bringing a branch into another. The exact merge mechanics sit in the full notes—here the idea is **isolation** then **integration**.

## 6. Remotes and synchronization

**Remote** = Git repository URL you treat as shared (often GitHub).

**`origin`** is the conventional name for the default remote; `git remote -v` lists URLs.

**Clone** copies repo + full history and sets **`origin`**:

```bash
git clone https://github.com/user/repo.git
```

**Push** sends your commits to the remote branch.

**Pull** typically **fetches** remote updates and **merges** into your current branch (`pull` ≈ `fetch` + `merge` in the common case). **`git fetch`** alone downloads objects without moving your branch—useful to inspect before merging.

**Upstream.** First push of a new branch often uses:

```bash
git push -u origin feature-login
```

so later **`git push`** / **`git pull`** on that branch know the default pairing.

## 7. Collaboration on GitHub

**Direct collaborators** have rights on one org/user repo—push branches, open **Pull Requests**.

**Forking** copies the repo under your account when you must not push upstream; changes flow back via PR from your fork.

**Pull Request (PR).** Not a Git CLI feature—a request on GitHub to merge one branch into another, with diff, discussion, and **Approve** / **Request changes**.

Access rules (read, write, maintain, admin) control who may merge and who may bypass. Professional teams often protect **main** so integration goes through review.

## 8. End-to-end rhythm (lecture anchor)

**Happy path** many beginners internalize:

```bash
git clone <repo-url>
cd <repository-folder>
git switch -c feature-login
# edit, save
git add .
git commit -m "Add login feature"
git push -u origin feature-login
# browser: open GitHub → Create Pull Request → review → merge
```

**Before new work** on an existing clone:

```bash
git switch main
git pull origin main
git switch -c feature-next-task
```

Full diagrams, access-control detail, and command tables are in **Lecture Notes.md**.

Use **Part VIII** there as the step-by-step workflow anchor.

## 9. Pitfalls (quick checklist)

1. **`git commit --amend`** after already **pushing** that commit—rewrites shared history unless coordinated.
2. **`git restore .`** in the wrong directory—discards all uncommitted work there; confirm with **`git status`** / **`git diff`** first.
3. **Committing** without **`git add`**—staging and working tree drift; always read **`git status`** before commit.
4. **`git pull`** without understanding you may merge—unexpected merge commits or conflicts; sometimes **`fetch`** then decide.
5. **Confusing Git and GitHub**—PR creation and permissions are on the host; your local tool is still Git.
6. **`user.email` / `user.name`** not matching GitHub—contributions and attribution look wrong; set **`git config --global`** once, deliberately.

**Before class.** Create a GitHub account at [github.com/signup](https://github.com/signup). Install Git from [git-scm.com](https://git-scm.com/download) and verify `git --version`.

Then run:

```bash
git config --global user.name "Your Full Name"
git config --global user.email "your@email.example"
```
