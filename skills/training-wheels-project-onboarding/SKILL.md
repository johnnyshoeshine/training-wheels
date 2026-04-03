---
name: training-wheels-project-onboarding
description: Use when you are starting work in a new repository or a new domain within a project. This skill ensures you build a complete mental map of the project in minutes.
---

# Project Onboarding

## Overview
`Project Onboarding` is a systematic approach to understanding an unfamiliar codebase. It focuses on identifying key patterns, build systems, and existing technical debt before writing any code.

## When to Use
- Entering a new repository for the first time.
- Starting a task in a different part of the project (e.g., from frontend to backend).
- When you need to understand the project structure and its dependencies quickly.

## Core Pattern: The First 5 Minutes
1. **Explore File Structure:** Use `list_directory` and `glob` to identify the project's skeleton.
2. **Find Entry Points:** Locate `main.py`, `index.ts`, or any other entry files.
3. **Map the Build & Test System:** Look for `package.json`, `requirements.txt`, `Makefile`, etc., to identify how to build and test.
4. **Identify Debt & Patterns:** Use `grep_search` for "TODO," "FIXME," and "HACK." Analyze existing naming and directory patterns.
5. **Establish Baseline:** Create or update `gemini.md` with the newly discovered project rules.

## Implementation Checklist
1. **Search for Instructions:** Does the repo already have `CLAUDE.md`, `GEMINI.md`, or a `README`? Read them first.
2. **Scan for Tech Stack:** Identify languages, frameworks, and libraries.
3. **Verify the Environment:** Run a simple build or test command to ensure the workspace is functional.
4. **Document Findings:** Summarize the project's architecture and any critical findings.

## Common Mistakes
- **Assuming Patterns:** Applying patterns from a different project without checking local conventions.
- **Starting Blind:** Writing code before understanding the build and test systems.
- **Ignoring Existing Docs:** Rediscovering rules that were already documented in a `README` or `gemini.md`.
