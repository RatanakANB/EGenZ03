# Git-Flow Track Command Analysis

> **Project:** Python Git-Flow Calculator (`scenario03`)  
> **Version:** 0.1.0  
> **Role:** Git-Flow Next Master  
> **Date:** 2026-04-02

---

## 📌 Branch Overview

| Type    | Branch Name                       | Parent Branch |
|---------|-----------------------------------|---------------|
| feature | `feature/01/add-subtract`         | `develop`     |
| feature | `feature/02/multiply-divide`      | `develop`     |
| bugfix  | `bugfix/01/fix-error-handling`    | `develop`     |
| hotfix  | `hotfix/01/fix-multiply-menu`     | `main`        |

---

## 🔍 Code Analysis (Source of Truth for Branch Naming)

### `calculator.py`
- All four operations (`add`, `subtract`, `multiply`, `divide`) are **stubbed with `pass`** — bodies are commented out.
- This indicates the features are **not yet implemented** and are tracked from remote:
  - `feature/01/add-subtract` → implements `add()` and `subtract()`
  - `feature/02/multiply-divide` → implements `multiply()` and `divide()`

### `main.py`
- Line 20: `# elif choice == '3':  a,b = _ab(); print(calculator.multiply(a,b)) # hotfix`
  - The multiply menu option is **commented out** → this is the scope of `hotfix/01/fix-multiply-menu` on `main`
- Line 24: `# print(f'Error: {e}') # bugfix`
  - The error handler is **commented out** → this is the scope of `bugfix/01/fix-error-handling` on `develop`

### `logger.py`
- Fully implemented. Logs every action with timestamp to `calc_history.log`.
- Supports features once `log_action()` is uncommented in `calculator.py`.

### `pyproject.toml`
- Project is `scenario`, version `0.1.0`.
- Dependencies: `mermaid-py`, `ipykernel` — used for local visualization in Jupyter.

---

## ⚙️ Git-Flow Track Commands

> `git flow <type> track <name>` — tracks (checks out) a remote branch that was published by another team member.

---

### 🌿 Feature 1 — `add-subtract`

```bash
git flow feature track 01/add-subtract
```

**What it does:**
- Fetches and checks out `feature/01/add-subtract` from the remote (`origin`).
- Sets up tracking so local branch follows `origin/feature/01/add-subtract`.
- Intended scope: implement `add()` and `subtract()` in `calculator.py`.

**Expected result:**
```
Branch 'feature/01/add-subtract' set up to track remote branch 'feature/01/add-subtract' from 'origin'.
Switched to a new branch 'feature/01/add-subtract'
```

---

### 🌿 Feature 2 — `multiply-divide`

```bash
git flow feature track 02/multiply-divide
```

**What it does:**
- Fetches and checks out `feature/02/multiply-divide` from the remote.
- Sets up tracking so local branch follows `origin/feature/02/multiply-divide`.
- Intended scope: implement `multiply()` and `divide()` in `calculator.py`.

**Expected result:**
```
Branch 'feature/02/multiply-divide' set up to track remote branch 'feature/02/multiply-divide' from 'origin'.
Switched to a new branch 'feature/02/multiply-divide'
```

---

### 🐛 Bugfix — `fix-error-handling`

```bash
git flow bugfix track 01/fix-error-handling
```

**What it does:**
- Fetches and checks out `bugfix/01/fix-error-handling` from the remote.
- Parent branch: `develop`.
- Intended scope: uncomment `print(f'Error: {e}')` in `main.py` (line 24) to restore error reporting.

**Expected result:**
```
Branch 'bugfix/01/fix-error-handling' set up to track remote branch 'bugfix/01/fix-error-handling' from 'origin'.
Switched to a new branch 'bugfix/01/fix-error-handling'
```

---

### 🔥 Hotfix — `fix-multiply-menu`

```bash
git flow hotfix track 01/fix-multiply-menu
```

**What it does:**
- Fetches and checks out `hotfix/01/fix-multiply-menu` from the remote.
- Parent branch: `main` (production fix).
- Intended scope: uncomment the multiply option in `main.py` (line 20) — restoring choice `'3'` in the menu.

**Expected result:**
```
Branch 'hotfix/01/fix-multiply-menu' set up to track remote branch 'hotfix/01/fix-multiply-menu' from 'origin'.
Switched to a new branch 'hotfix/01/fix-multiply-menu'
```

---

## 🗺️ Full Git-Flow Lifecycle (All Commands per Branch)

### Feature 1: `add-subtract`

```bash
# Start (done by feature owner)
git flow feature start 01/add-subtract

# Publish to remote (feature owner pushes)
git flow feature publish 01/add-subtract

# Track (other team members pull and follow)
git flow feature track 01/add-subtract

# Finish (merge back to develop)
git flow feature finish 01/add-subtract
```

---

### Feature 2: `multiply-divide`

```bash
# Start
git flow feature start 02/multiply-divide

# Publish
git flow feature publish 02/multiply-divide

# Track
git flow feature track 02/multiply-divide

# Finish
git flow feature finish 02/multiply-divide
```

---

### Bugfix: `fix-error-handling`

```bash
# Start (from develop)
git flow bugfix start 01/fix-error-handling

# Publish
git flow bugfix publish 01/fix-error-handling

# Track
git flow bugfix track 01/fix-error-handling

# Finish (merges back to develop)
git flow bugfix finish 01/fix-error-handling
```

---

### Hotfix: `fix-multiply-menu`

```bash
# Start (from main — production branch)
git flow hotfix start 01/fix-multiply-menu

# Publish
git flow hotfix publish 01/fix-multiply-menu

# Track
git flow hotfix track 01/fix-multiply-menu

# Finish (merges back to both main AND develop)
git flow hotfix finish 01/fix-multiply-menu
```

---

## 🧭 Branch Flow Diagram

```
main
 │
 ├──── hotfix/01/fix-multiply-menu  ──────────────────────────────► main + develop
 │
develop
 │
 ├──── feature/01/add-subtract      ──────────────────────────────► develop
 │
 ├──── feature/02/multiply-divide   ──────────────────────────────► develop
 │
 └──── bugfix/01/fix-error-handling ──────────────────────────────► develop
```

---

## ✅ Summary Table — Track Commands

| Branch Type | Branch Name                    | Track Command                                      |
|-------------|--------------------------------|----------------------------------------------------|
| feature     | `01/add-subtract`              | `git flow feature track 01/add-subtract`           |
| feature     | `02/multiply-divide`           | `git flow feature track 02/multiply-divide`        |
| bugfix      | `01/fix-error-handling`        | `git flow bugfix track 01/fix-error-handling`      |
| hotfix      | `01/fix-multiply-menu`         | `git flow hotfix track 01/fix-multiply-menu`       |
