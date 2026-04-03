---
name: training-wheels-ultraplan
description: Use when you need to create a comprehensive, multi-step execution plan for a complex task. This skill ensures deep reasoning, risk assessment, and clear project boundaries.
---

# Ultraplan

## Overview
`Ultraplan` is a specialized mode for high-stakes planning. It moves beyond a simple list of steps to provide a structured strategy that considers project scope, potential failures, and recovery procedures.

## When to Use
- Starting a major feature implementation.
- Planning a complex refactor or migration.
- Coordinating multi-step changes across different services or files.
- When the "blast radius" of a task is high and requires careful sequencing.

## Core Pattern
A complete `Ultraplan` MUST include the following sections:

1. **Goals:** What does success look like? What are we trying to achieve?
2. **Non-goals:** What is explicitly OUT of scope? (Prevents scope creep).
3. **Risks & Mitigations:** What could go wrong? How will we prevent or handle it?
4. **Implementation Sequence:** A logical, step-by-step order of operations.
5. **Verification Steps:** How will we prove each step worked?
6. **Rollback Plan:** How do we revert if a step fails or causes a regression?

## Implementation Checklist
1. **Understand the "Why":** Why are we doing this? (Sets the Goals).
2. **Define Boundaries:** What are we NOT doing? (Sets the Non-goals).
3. **Brainstorm Failures:** What is the worst-case scenario? (Sets Risks/Rollback).
4. **Sequence for Safety:** Order steps to minimize downtime and risk.
5. **Iterate:** Review the plan with the user before starting implementation.

## Common Mistakes
- **Vague Steps:** "Update code" instead of "Add `validate_token` method to `AuthService`."
- **Ignoring Risks:** Assuming everything will work perfectly the first time.
- **Missing Rollback:** Having no plan for when a migration fails halfway through.
- **Scope Creep:** Trying to fix unrelated bugs while implementing the plan.
