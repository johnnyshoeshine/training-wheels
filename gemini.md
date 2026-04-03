# Gemini CLI Project Rules

## Doing Tasks
- Read relevant code before changing it and keep changes tightly scoped to the request.
- Do not add speculative abstractions, compatibility shims, or unrelated cleanup.
- Do not create files unless they are required to complete the task.
- If an approach fails, diagnose the failure before switching tactics.
- Report outcomes faithfully: if verification fails or was not run, say so explicitly.

## Action Care
- Carefully consider reversibility and blast radius. Local, reversible actions like editing files or running tests are usually fine.
- Actions that affect shared systems, publish state, delete data, or otherwise have high blast radius should be explicitly authorized by the user.

## Verification Nudge
**CRITICAL:** Before claiming a task is complete, you MUST verify the behavior.
1. **Identify the Verification Command:** (e.g., `pytest`, `npm test`, or a custom reproduction script).
2. **Execute the Command:** Run it and examine the output.
3. **Evidence Before Claims:** Your final message must include the output or a summary of the verification results.
4. **No Success Reports Without Evidence:** Do not say "Done" or "Fixed" without showing the verification evidence.

## Specialized Modes (Skills)
- Use `/prompt-aware-researcher` for surgical data extraction from the web.
- Use `/bughunter` for systematic audits of codebase correctness and security.
- Use `/ultraplan` for deep, multi-step execution planning with risk assessment.
- Use `/task-discipline` to maintain an accurate task list and ensure verification.
- Use `/project-onboarding` for a systematic first-look at a new codebase.
- Use `/agent-personas` to dispatch specialized sub-agents via the `generalist` tool.
