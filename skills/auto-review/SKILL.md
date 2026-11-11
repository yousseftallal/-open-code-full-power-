---
name: auto-review
description: "Automatic review before closing a goal: run reviewer + security-auditor + tester on all changes, then report. Use before marking any goal complete."
---

# Auto-Review (OpenCode)

## Overview
Before marking a **big goal** as done, run an automatic review:
- **reviewer** — correctness/regressions
- **security-auditor** — security issues
- **tester** (if available) — tests

## Workflow
1. **Implementation complete** → agents mark sub-goals done.
2. **Auto-review trigger:** Orchestrator launches:
   - `reviewer` (foreground) — review changes.
   - `security-auditor` (foreground) — security audit.
   - `tester` (if exists) — run tests.
3. **Collect findings** → if issues, fix → re-review.
4. **Mark big goal done** only when all reviews pass.

## How to request
> "Before closing this goal, run auto-review (reviewer + security-auditor)."

## Best Practices
- Always review before marking goal done.
- Fix issues found, then re-review.
- Use claude-mem to save review results.
- Keep review focused (not full codebase).