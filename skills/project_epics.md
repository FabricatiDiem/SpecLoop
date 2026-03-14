---
description: "Draft or update the project's EPICS.md file"
---

# Project Epics Drafting Skill

This skill assists you in defining the feature roadmap (epics) for your project, ensuring compatibility with the autonomous loop.

## User Input

```text
$ARGUMENTS
```

## Procedure

1. **Context Loading**:
   - Read `.specify/memory/constitution.md` and `GOALS.md`.
   - If `EPICS.md` already exists, read it to understand the current roadmap.

2. **Analysis**:
   - Analyze the mission and constraints from `GOALS.md`.
   - Ensure every proposed epic is aligned with at least one principle in the constitution.

3. **Propose Phase**:
   - Generate a list of high-level feature sets (Epics).
   - Each epic MUST have a clear Description and a suggested Priority.
   - Present the proposed roadmap to the user, explicitly noting which constitution principle each epic serves.

4. **Review Phase**:
   - Refine the list based on user feedback.
   - Ensure the priorities are sequential and reflect the desired development order.

5. **Write Phase**:
   - **CRITICAL**: Only proceed after user approval.
   - Write the finalized roadmap to `EPICS.md` in the repository root.
   - **STRICT ENFORCEMENT**: You MUST use the exact schema template below.

## Schema Template

```markdown
# Project Epics

## [[Title of Epic]]
Description: [Full context, achievements, and remaining tasks]
Priority: [Integer]
- [ ] Status: Pending
```

## Rules for Agents

1. **Headers**: Use H2 (`##`) for the title.
2. **Brackets**: The title MUST be enclosed in `[...]`.
3. **Fields**: `Description`, `Priority`, and `Status` must be on separate lines.
4. **Ordering**: Epics should be listed in increasing order of priority.
