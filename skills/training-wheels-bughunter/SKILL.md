---
name: training-wheels-bughunter
description: Use when you need to perform a systematic audit of a codebase or specific files to identify bugs, correctness issues, or security vulnerabilities.
---

# Bughunter

## Overview
`Bughunter` is a specialized mode for identifying and prioritizing software defects. Instead of a general code review, `Bughunter` focuses on concrete findings that could lead to crashes, security breaches, or incorrect behavior.

## When to Use
- Before a release or pull request merge.
- When investigating a reported bug without a clear root cause.
- To perform a security audit on a new module.
- When cleaning up legacy code for correctness.

## Core Pattern
Identify, categorize, and prioritize defects. Always include:
1. **File Path & Line Number:** Where is the bug?
2. **Severity:** How critical is it? (Critical, High, Medium, Low)
3. **Description:** What is the issue? (e.g., "ZeroDivisionError", "Path Traversal")
4. **Suggested Fix:** How can we fix it?

### Example: Bug Report
**Task:** Audit `buggy_script.py`.

**Bughunter Output:**
- **File:** `buggy_script.py`
- **Line:** 9
- **Severity:** High
- **Issue:** `ZeroDivisionError` in `calculate_average`.
- **Fix:** Add a check `if not numbers: return 0` at the start of the function.

- **File:** `buggy_script.py`
- **Line:** 4
- **Severity:** Critical
- **Issue:** `Path Traversal Vulnerability` in `delete_file`.
- **Fix:** Use `os.path.basename(filename)` to sanitize the path or validate it against an allowlist of directories.

## Implementation Checklist
1. **Define Scope:** Which files or directories are we auditing?
2. **Scan for Common Antipatterns:** (e.g., unvalidated input, missing error handling, resource leaks).
3. **Use Tools:** (e.g., `grep_search` to find dangerous patterns like `os.remove` or `eval`).
4. **Prioritize:** Focus on the most critical/high-severity issues first.
5. **Verify:** If possible, write a small test case to confirm the bug exists before reporting it.

## Common Mistakes
- **Vague Descriptions:** Saying "this code is messy" instead of "this will crash if `name` is `None`."
- **Ignoring Security:** Overlooking path traversal or injection risks.
- **Reporting "Cleanliness" Issues:** Mixing up stylistic choices with actual bugs. Keep `Bughunter` focused on correctness.

## Real-World Impact
- **Correctness:** Prevents runtime crashes and data corruption.
- **Security:** Identifies vulnerabilities before they can be exploited.
- **Reliability:** Improves the overall stability and robustness of the codebase.
