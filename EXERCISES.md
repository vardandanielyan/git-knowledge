# 🎓 Git Practice Exercises for Junior Developers

Welcome to the hands-on Git practice guide! This guide takes you step-by-step through real-world Git operations that professional developers use daily.

---

## 🛠️ Prerequisites

1. Ensure your terminal is authenticated with GitHub (see **[`AUTHENTICATION.md`](AUTHENTICATION.md)**).
2. Clone the repository to your local machine:
```bash
git clone git@github.com:vardandanielyan/git-knowledge.git
cd git-knowledge
```

3. Verify test suite runs:
```bash
python3 -m unittest discover -s tests
```

---

## 📌 Exercise 1: Exploring Repository History & Status

**Goal:** Understand the current state and commit history.

```bash
# Check current branch and staged/unstaged changes
git status

# View commit history in one-line format
git log --oneline

# View branch visual tree
git log --oneline --graph --all
```

---

## 📌 Exercise 2: Creating a Feature Branch

**Goal:** Never code directly on `main`. Always create a descriptive branch.

1. Ensure your local `main` is up-to-date:
   ```bash
   git checkout main
   git pull origin main
   ```

2. Create and switch to a new branch for a new feature:
   ```bash
   git checkout -b feature/power-function
   ```

3. Open `src/calculator.py` and implement the `power(base, exponent)` function:
   ```python
   def power(base: float, exponent: float) -> float:
       """Returns base raised to the power of exponent."""
       return base ** exponent
   ```

4. Add a test in `tests/test_calculator.py`:
   ```python
   def test_power(self):
       self.assertEqual(power(2, 3), 8)
       self.assertEqual(power(5, 0), 1)
   ```

5. Run tests:
   ```bash
   python3 -m unittest discover -s tests
   ```

---

## 📌 Exercise 3: Staging & Committing Changes

**Goal:** Make clean, atomic commits following conventional commit syntax.

1. Review changes before staging:
   ```bash
   git diff
   ```

2. Stage the modified files:
   ```bash
   git add src/calculator.py tests/test_calculator.py
   ```

3. Commit with a clear, descriptive message:
   ```bash
   git commit -m "feat: add power function with unit tests"
   ```

---

## 📌 Exercise 4: Pushing Branch & Opening a Pull Request (PR)

**Goal:** Push your local branch to GitHub and create a Pull Request.

1. Push your branch to the remote repository:
   ```bash
   git push -u origin feature/power-function
   ```

2. Go to [GitHub Repository](https://github.com/vardandanielyan/git-knowledge) in your browser.
3. You will see a banner: **"feature/power-function had recent pushes"** -> Click **Compare & pull request**.
4. Fill out the PR description and submit!

---

## 📌 Exercise 5: Syncing Your Branch with `main` (Rebase)

**Goal:** Keep your feature branch fresh when `main` gets updated by teammates.

```bash
# 1. Fetch latest changes from remote without modifying local working directory
git fetch origin

# 2. Rebase your current feature branch onto updated main
git rebase origin/main
```
> 💡 *Why rebase?* Rebase applies your commits on top of the newest `main`, creating a clean, linear commit history.

---

## 📌 Exercise 6: Hands-On Merge Conflict Resolution

**Goal:** Learn how to resolve a Git merge conflict with confidence.

### Step 1: Simulate Conflict
Two developers edit the same line in `src/calculator.py` (`APP_VERSION`).

```bash
# Checkout main and branch off
git checkout main
git checkout -b feature/conflict-test-A

# Change APP_VERSION in src/calculator.py to "1.1.0-alpha"
# Commit it:
git add src/calculator.py
git commit -m "chore: bump version to 1.1.0-alpha"

# Now switch back to main and create another branch
git checkout main
git checkout -b feature/conflict-test-B

# In branch B, change APP_VERSION in src/calculator.py to "1.1.0-beta"
# Commit it:
git add src/calculator.py
git commit -m "chore: bump version to 1.1.0-beta"
```

### Step 2: Merge and Trigger Conflict
```bash
git merge feature/conflict-test-A
```
Git will stop and announce:
```
CONFLICT (content): Merge conflict in src/calculator.py
Automatic merge failed; fix conflicts and then commit the result.
```

### Step 3: Inspect & Resolve
Open `src/calculator.py`. You will see markers:
```python
<<<<<<< HEAD
APP_VERSION = "1.1.0-beta"
=======
APP_VERSION = "1.1.0-alpha"
>>>>>>> feature/conflict-test-A
```

1. Edit the file, remove the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`), and choose the final correct version (e.g. `APP_VERSION = "1.1.0"`).
2. Save the file.
3. Stage and finish the merge:
   ```bash
   git add src/calculator.py
   git commit -m "resolve: merge version update conflict"
   ```

---

## 📌 Exercise 7: Undoing Mistakes & Git Stash

| Scenario | Command |
|---|---|
| Discard uncommitted changes in a file | `git restore src/calculator.py` |
| Unstage a file without losing edits | `git restore --staged src/calculator.py` |
| Save dirty work temporarily before switching branch | `git stash` |
| Restore stashed work | `git stash pop` |
| Undo the last commit (keep the changes in working files) | `git reset --soft HEAD~1` |
| Revert a pushed commit safely by creating an inverted commit | `git revert <commit-hash>` |

---

## 📌 Exercise 8: Cherry-Picking a Specific Commit (`git cherry-pick`)

**Goal:** Copy a specific commit from another branch into your branch without merging everything.

### 🎭 Real-World Scenario
A teammate pushed a branch called `feature/scientific-ops`. That branch has **two commits**:
1. `a89e31f` (`feat: add modulo operation with unit tests`) → **Finished, tested, ready to use!**
2. `15a0a5f` (`wip: draft factorial function`) → **Unfinished broken draft!**

You need the `modulo` operation on your branch right now, but you do **NOT** want to merge the unfinished `factorial` code. **Solution:** Cherry-pick!

---

### Step-by-Step Hands-On Practice

#### 1. Fetch the latest branches from GitHub
```bash
git fetch origin
```

#### 2. Inspect the commits on the remote branch
```bash
git log --oneline origin/feature/scientific-ops -n 3
```
Notice the two commits:
```text
15a0a5f (origin/feature/scientific-ops) wip: draft factorial function (not ready for main)
a89e31f feat: add modulo operation with unit tests
```

#### 3. Create your own practice branch from `main`
```bash
git checkout main
git checkout -b practice/cherrypick-modulo
```

#### 4. Cherry-pick ONLY the `modulo` commit (`a89e31f`)
```bash
git cherry-pick a89e31f
```

#### 5. Verify the result
```bash
# Check that the commit was copied onto your branch with a new hash
git log -n 1 --oneline

# Run tests to prove modulo works
python3 -m unittest discover -s tests

# Check src/calculator.py to verify modulo is present, but NOT the unfinished factorial!
git diff HEAD~1
```

#### 6. Push your practice branch to GitHub
```bash
git push -u origin practice/cherrypick-modulo
```

---

## 🏆 Checklist for Junior Devs

- [ ] Cloned the repo and verified tests pass.
- [ ] Created a feature branch (`feature/...`).
- [ ] Added a feature with tests.
- [ ] Pushed the feature branch to GitHub.
- [ ] Successfully simulated and resolved a merge conflict.
- [ ] Used `git stash` to switch context and resume work.
- [ ] Practiced `git cherry-pick` using the `feature/scientific-ops` branch.
