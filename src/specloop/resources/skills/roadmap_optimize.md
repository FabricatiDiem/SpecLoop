---
description: "Optimize the roadmap execution order based on dependencies and priorities"
---

# Roadmap Optimization Skill

This skill analyzes epic dependencies and priorities to suggest an optimal execution order.

## User Input

```text
$ARGUMENTS
```

## Procedure

1. **Context Loading**:
   - Use the `read` tool to load `EPICS.md` and `GOALS.md`.

2. **Dependency Extraction**:
   - For every epic in `EPICS.md`, extract dependencies from the `Description` field.
   - Look for keywords: "depends on", "requires", "after X", "prerequisite".
   - Note down the relationships (Prerequisite -> Dependent).

3. **Ordering Logic (Optimization)**:
   - **Topological Sort**: Arrange epics such that every prerequisite appears before its dependents.
   - **Priority Tie-breaking**: If multiple epics are "ready" to be worked on (no unfinished prerequisites), sort them by their original `Priority` integer (lowest first).
   - **Foundational Value Tie-breaking**: If priorities are tied, calculate the "Foundational Value" (how many other epics depend on this one) and prioritize the one with the highest value.
   - **Status Validation**: Check for "Impossible States" (e.g., Epic marked `Completed` while its prerequisite is `Pending`).

4. **Proposal Phase**:
   - Generate a new content block for `EPICS.md` representing the optimized order.
   - Renumber the `Priority` integers sequentially starting from 1.
   - Provide a "Change Justification" table.

### Justification of Reordering

| Epic | New Priority | Change Type | Rationale |
|------|--------------|-------------|-----------|
| [Title] | [New #] | [Upgrade/Downgrade] | [Dependency/Foundational reasoning] |

5. **Write Instruction**:
   - Present the optimized order to the user.
   - After approval, write the new content to `EPICS.md`.

## Rules for Agents

- **Preserve Descriptions**: Do not modify the `Description` text of epics unless specifically asked.
- **Sequential Integrity**: Ensure the final `Priority` list has no gaps or duplicates.
- **Citations**: Explicitly link reordering decisions to the dependency text found in the descriptions.
