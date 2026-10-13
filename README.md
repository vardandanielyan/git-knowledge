# 🚀 Git Knowledge & Junior Developer Training Ground

A practical, hands-on repository designed to teach junior developers professional Git workflows, branching strategies, merge conflict resolution, pull requests, and collaboration best practices.

---

## 📂 Repository Structure

```text
git-knowledge/
├── .github/workflows/
│   └── tests.yml          # Automated CI running tests on every push and PR
├── src/
│   ├── calculator.py      # Core calculator functions + exercise tasks
│   └── main.py            # Interactive CLI calculator app
├── tests/
│   └── test_calculator.py # Unit tests
├── EXERCISES.md           # Step-by-step hands-on Git tutorial
└── README.md              # Project documentation
```

---

## ⚡ Quick Start

### 1. Run the Calculator Application
```bash
python3 src/main.py
```

### 2. Run the Test Suite
```bash
python3 -m unittest discover -s tests
```

---

## 🎯 Hands-On Git Exercises

Check out **[`EXERCISES.md`](EXERCISES.md)** for detailed exercises covering:

1. **Repository Inspection:** `git status`, `git log --graph --oneline`
2. **Branching Workflows:** `git checkout -b feature/...`
3. **Clean Commits:** Atomic commits with conventional commit messages
4. **Pull Requests (PR):** Pushing to remote and collaborating on GitHub
5. **Rebasing & Syncing:** `git fetch` and `git rebase origin/main`
6. **Conflict Resolution:** Inducing and resolving merge conflicts hands-on
7. **Git Safety Tools:** `git stash`, `git restore`, `git reset`, and `git revert`

---

## 🤝 Contribution Guidelines

1. Never commit directly to `main`.
2. Always create a branch prefixed with `feature/`, `bugfix/`, or `chore/`.
3. Ensure all tests pass (`python3 -m unittest discover -s tests`) before committing.
4. Open a Pull Request and request a review.
