# Research: Drafting Skills for GOALS and EPICS

This document explores the logic and alignment strategies for the automated drafting of project metadata.

## Decision 1: Context Injection Strategy

- **Decision**: The skills will explicitly instruct the agent to use the `read` tool on `constitution.md` and `GOALS.md` as the first step of the procedure.
- **Rationale**: Agents need immediate access to the "ground truth" of the project before proposing a roadmap. By making this a mandatory first step in the skill instruction, we ensure alignment with project principles and mission.
- **Alternatives considered**: Expecting the user to provide the context in the prompt. Rejected as it increases user friction and error rates.

## Decision 2: Epic Formatting Enforcement

- **Decision**: Use a "Schema Template" block within the `project_epics.md` skill.
- **Rationale**: Providing a literal text block that the agent can copy-paste ensures the highest fidelity to the schema required by the `speckit-loop` runner.
- **Best Practice**: Use the `## [Title]` and `Description: ...` labels exactly as defined in the `002-speckit-automation` specification.

## Decision 3: Collaborative Drafting Pattern

- **Decision**: The skills will follow a "Draft -> Review -> Finalize" pattern.
- **Rationale**: Scaffolding a project mission or roadmap is high-stakes. The skill will first propose a set of items and then ask for user confirmation or adjustments before writing the final file.
- **Integration**: Leverages the natural conversational abilities of agents like Claude or OpenCode.
