---
name: training-wheels-task-discipline
description: Use when you are managing a complex task or project with multiple sub-tasks. This skill ensures your task list is always current and that every completed step is verified.
---

# Task Discipline

## Overview
`Task Discipline` is the practice of maintaining a highly accurate, up-to-date representation of your current work progress. It ensures that no task is considered "done" until it is verified and its status is persisted.

## When to Use
- Executing an `Ultraplan` or any multi-step plan.
- Working across multiple sessions.
- Collaborating with sub-agents on independent tasks.
- When you need to provide a clear progress report to the user.

## Core Pattern
For every sub-task in your `write_todos` list:
1. **Mark as In-Progress:** Before you start work on a sub-task.
2. **Execute:** Perform the necessary changes.
3. **Verify:** Run a specific verification command or test.
4. **Evidence:** Report the verification output in your message.
5. **Mark as Completed:** Only AFTER successful verification.

## Implementation Checklist
1. **Keep Todos Accurate:** Update your task list immediately when work starts or finishes.
2. **One Thing at a Time:** Avoid having multiple unrelated tasks "in_progress" simultaneously.
3. **Verification Nudge:** If you finish a task, you MUST show the proof before moving on.
4. **Persistent State:** Ensure your task list reflects the reality of the codebase.

## Common Mistakes
- **Shadow Progress:** Finishing a task in your head but not updating the `write_todos` list.
- **Skipping Verification:** Marking a task "completed" because it "should work."
- **Cluttered Lists:** Keeping irrelevant or duplicate tasks in the `write_todos` list.
