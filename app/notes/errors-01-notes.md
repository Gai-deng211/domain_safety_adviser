# CI Pipeline — WHOIS Project

**Date:** June 22, 2026

---

## Summary

Set up GitHub Actions continuous integration to automate testing on pushes and pull requests to the main branch.

---

## Issues Encountered

- `.github/workflows/ci.yml` location error. It was nested inside `app/`
- `requirements.txt` missing from root directory (was located in `app/`)
- Import error: `No module named 'services'` due to improper import paths and project structure
- Minor test failure from mismatch in `status` value formatting

---

## Solutions Applied

- Moved `.github/workflows/ci.yml` to the root repo location
- Moved `requirements.txt` to repository root for CI visibility
- Updated scraper logic to standardize/normalize `status` field values
- Adjusted test discovery to work from repo root

---

## Results

- ✅ CI pipeline executes successfully
- ✅ Dependencies install without issues
- ✅ All unit tests pass in a clean environment