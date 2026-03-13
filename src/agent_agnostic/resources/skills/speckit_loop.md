---
description: "Start the autonomous SpecKit development loop"
---

# SpecKit Loop

You are about to start an autonomous development cycle. 

1. **Launch the Subagent**: You MUST use the `@speckit-loop` subagent to perform this task.
2. **Autonomous Execution**: The subagent will read `EPICS.md`, create branches, and implement features one by one using the project's SpecKit templates and conventions.
3. **Observation**: You (the host agent) should monitor the subagent's progress but allow it to work autonomously.

Trigger the loop now:
`@speckit-loop begin the implementation loop defined in EPICS.md`
