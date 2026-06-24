# Date: Jun 23, 2026
# Git & CI Workflow Summary

## Branch Structure
- **main:** stable, production-ready
- **dev:** active development/testing

---

## Standard Workflow

**Start a new dev branch:**
```bash
git checkout -b dev
git add .
git commit -m "your message"
git push -u origin dev
```

**Merge dev into main:**
```bash
git checkout main
git pull origin main
git merge dev
git push origin main
```

**Keep dev updated with main:**
```bash
git checkout dev
git merge main
```

**Force-reset dev to main (destructive):**
```bash
git checkout dev
git reset --hard main
git push -f origin dev
```

---

## Continuous Integration (CI)
- Tests run automatically via GitHub Actions
- Uses `pytest`
- **If tests pass (`✅`)**: safe to merge
- **If tests fail (`❌`)**: fix issues before merging

**Golden Rule:**  
🛑 **Never merge failing CI into `main`.**

## Conceptual Model

- `main`: always stable & deployable
- `dev`: for ongoing changes & experimentation
- CI: automatic safety net before merges