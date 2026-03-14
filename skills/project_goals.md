---
description: "Draft or update the project's GOALS.md file"
---

# Project Goals Drafting Skill

This skill assists you in defining the high-level mission and constraints for your project.

## User Input

```text
$ARGUMENTS
```

## Procedure

1. **Context Loading**: 
   - Read `.specify/memory/constitution.md` to understand the project's core principles.
   - If `GOALS.md` already exists, read it to preserve existing context.

2. **Analysis**:
   - Analyze the user's input (if provided) alongside the constitution.
   - If user input is minimal, infer the project's purpose from the repository name and directory structure.

3. **Propose Phase**:
   - Generate a draft `# Project Mission` statement.
   - Generate a list of `# Constraints` (e.g., technology choices, quality targets like "Python 3.11+", "Strict Type Safety").
   - Present this draft to the user for review.

4. **Review Phase**:
   - Ask the user for feedback or adjustments.
   - Iterate on the draft until the user is satisfied.

5. **Write Phase**:
   - **CRITICAL**: Only proceed after user approval.
   - Write the finalized content to `GOALS.md` in the repository root.

## Template

```markdown
# Project Mission
[Finalized Mission Statement]

# Constraints
- [Constraint 1]
- [Constraint 2]
```
