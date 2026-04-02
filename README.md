# scenario03 — Python Git-Flow Calculator

A hands-on Git-Flow training project built with a Python CLI calculator.  
This project follows the **Git-Flow branching strategy** and is used to practice collaborative development workflows.

---

## 📋 Project Scope

This project contains:

| Branch Type | Count | Purpose |
|-------------|-------|---------|
| `feature`   | 2     | Implement calculator operations |
| `bugfix`    | 1     | Fix error handling in the CLI |
| `hotfix`    | 1     | Restore missing menu option in production |
| `release`   | 1     | Prepare and tag a stable release |

---

## 🌿 Branch Naming Convention

Every branch name **must include the assigned issue ID** as a prefix, followed by a descriptive slug.

### Format

```
<type>/<issue-id>/<short-description>
```

### Examples

| Issue ID | Feature Name    | Branch Name                          | Command |
|----------|-----------------|--------------------------------------|---------|
| `#45`    | add-subtract    | `feature/45/add-subtract`            | `git flow feature start 45/add-subtract` |
| `#12`    | multiply-divide | `feature/12/multiply-divide`         | `git flow feature start 12/multiply-divide` |
| `#3`     | fix-error       | `bugfix/3/fix-error-handling`        | `git flow bugfix start 3/fix-error-handling` |

> **Rule:** The `{name}` in `git flow <type> start {name}` must always follow the pattern `{issue-id}/{description}`.

---

## 🔄 Git-Flow Lifecycle

Follow this order when working through the project:

```
1. Features     ──► develop
2. Bugfix       ──► develop
3. Release      ──► main + develop  (tag version)
4. Hotfix       ──► main + develop  (production fix)
```

### Step-by-Step

```bash
# 1. Start and publish your branch
git flow feature start <issue-id>/<name>
git flow feature publish <issue-id>/<name>

# 2. Team members track your branch
git flow feature track <issue-id>/<name>

# 3. Finish and merge back
git flow feature finish <issue-id>/<name>

# 4. After features and bugfix are done — cut a release
git flow release start <version>
git flow release finish <version>

# 5. Fix any production issue as a hotfix (from main)
git flow hotfix start <issue-id>/<name>
git flow hotfix finish <issue-id>/<name>
```

---

## 🤝 Team Guidelines

- **Always publish** your branch after starting it so teammates can track your progress.
- **Always communicate** before making changes that may affect shared branches.
- **Use `track`** to follow a remotely published branch created by another team member.
- **Open a Pull Request** when your branch is ready for review — do not merge directly without team leader approval.
- **Never force push** to `develop` or `main`.

---

## 📁 Project Structure

```
scenario03/
├── main.py          # CLI entry point
├── calculator.py    # Core operations: add, subtract, multiply, divide
├── logger.py        # Action logger (writes to calc_history.log)
├── pyproject.toml   # Project metadata and dependencies
├── track.md         # Git-Flow track command reference
└── README.md        # This file
```

---

## ⚙️ Requirements

- Python `>= 3.14`
- Dependencies: `mermaid-py >= 0.8.4`, `ipykernel`