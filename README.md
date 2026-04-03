# training-wheels-claudia

A personalized Gemini CLI harness containing specialized skills and engineering standards. This is for gemini as it is what i use (goddam google got me by the precious memories...), i'm sure they will work as guardrails or whatnot for OSS stuff - as others are trying out haha 

## Purpose
This repository serves as a localized set of "training wheels" for Gemini CLI. It includes specialized skills for planning, research, auditing, and task discipline, as well as a defined set of engineering rules (`gemini.md`).

## Origin
The patterns and logic in this repository were inspired by and adapted from the [Claw Code](https://github.com/instructkr/claw-code) repository. This project captures the architectural insights of that harness while being rebuilt for a personalized Gemini CLI workflow.

## Contents
- **`gemini.md`**: Core engineering rules and "Verification Nudge" protocols.
- **`skills/`**: A collection of specialized Gemini skills:
    - `training-wheels-agent-personas`: Specialized personas for sub-agents.
    - `training-wheels-bughunter`: Systematic bug auditing.
    - `training-wheels-project-onboarding`: Fast codebase mapping.
    - `training-wheels-prompt-aware-researcher`: Surgical web research.
    - `training-wheels-task-discipline`: Verified task management.
    - `training-wheels-ultraplan`: Deep execution planning.

## Usage
To use these skills in your own Gemini CLI session:
1. Clone this repository.
2. In your project, run `/skills reload` to discover the new skills.
3. Call them using `?training-wheels-<name>`.
