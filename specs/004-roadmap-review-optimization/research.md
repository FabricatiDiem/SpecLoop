# Research: Roadmap Review and Optimization

This document explores strategies for implementing logical analysis and optimization of project roadmaps via natural language skills.

## Decision 1: Gap Detection Strategy

- **Decision**: The `/roadmap.review` skill will use a "Requirement Matrix" mental model.
- **Rationale**: The agent will be instructed to first list all implicit and explicit requirements from `GOALS.md` and `constitution.md`. Then, it will map existing epics to these requirements. Any requirement with zero mapping is reported as a "Gap".
- **Benefit**: This provides a systematic way to ensure 100% coverage of project goals.
- **Example Matrix**:

| Project Requirement | Mapping (Epics) | Status | Gap? |
|---------------------|-----------------|--------|------|
| [GOAL] SQLite support | Epic #12 (DB Setup) | Covered | No |
| [PRIN] Self-verification | N/A | Missing | **YES** |

## Decision 2: Dependency Parsing and Sorting

- **Decision**: Epics will be modeled as a directed acyclic graph (DAG) during the optimization phase.
- **Logic**:
    1. Extract all mentions of other epics from each epic's `Description` field.
    2. Build a list of edges (Epic A -> Epic B).
    3. Sort the list such that dependencies are completed first.
    4. If multiple epics are available, use the `Priority` integer as the secondary sorting key.
- **Rationale**: This mimics traditional project management software but is executed via the agent's reasoning engine, allowing it to understand semantic dependencies (e.g., "requires database integration" implies a dependency on the database epic even if not explicitly named).

## Decision 3: "Status Alignment" Validation

- **Decision**: Explicit check for "Impossible States".
- **Logic**: Identify epics marked `Completed` that depend on epics marked `Pending` or `In Progress`.
- **Rationale**: This detects manual editing errors in `EPICS.md` and ensures the source of truth for the automation loop is reliable.

## Decision 4: Output Format

- **Decision**: Use a structured Markdown table for gaps and alignment issues, and a suggested literal text block for the reordered `EPICS.md`.
- **Rationale**: High human readability and easy machine parsing for subsequent `/speckit.loop` runs.
