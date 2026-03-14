---
description: "Audit the project roadmap against goals and constitution"
---

# Roadmap Review Skill

This skill analyzes the relationship between `constitution.md`, `GOALS.md`, and `EPICS.md` to identify functional gaps and alignment issues.

## User Input

```text
$ARGUMENTS
```

## Procedure

1. **Context Loading**:
   - Use the `read` tool to load:
     - `.specify/memory/constitution.md`
     - `GOALS.md`
     - `EPICS.md`

2. **Requirement Extraction**:
   - Parse `GOALS.md` for the Mission Statement and all Constraints.
   - Parse `constitution.md` for all Core Principles (MUST/SHOULD rules).
   - Create an internal list of "Active Requirements".

3. **Requirement Mapping (Gap Detection)**:
   - For every Requirement identified in Step 2, search `EPICS.md` for a feature that satisfies it.
   - If a requirement has no mapping epic, mark it as a **Gap**.
   - **CRITICAL**: You MUST cite the specific principle or goal (e.g., "Principle II: SpecKit Backbone") for every finding.

4. **Alignment Check**:
   - Check if any epic description implies a technology or practice that contradicts a Constraint in `GOALS.md` or a Principle in `constitution.md`.
   - Perform a **Status Alignment Audit**:
     - Identify if an epic marked `Completed` depends on another epic that is `Pending` or `In Progress`.
     - Cross-reference descriptions for implicit "requires" or "depends on" keywords.

5. **Reporting**:
   - Produce a structured analysis report using the following tables.

### Roadmap Gaps

| Requirement Source | Missing Requirement | Rationale | Suggested Epic |
|--------------------|---------------------|-----------|----------------|
| [File:Section]     | [Description]       | [Why it's a gap] | [Proposed Title] |

### Alignment Issues

| Target Epic | Conflict | Severity | Citation |
|-------------|----------|----------|----------|
| [Title]     | [Description of contradiction] | [Blocker/Warning] | [Source Principle/Goal] |

## Rules for Agents

- **Evidence-Based Findings**: Do not hallucinate gaps. Every gap must be tied to a literal line in the source documents.
- **Tone**: Professional and analytical.
- **Actionability**: Recommendations should be concrete enough to be added to `EPICS.md` immediately.
