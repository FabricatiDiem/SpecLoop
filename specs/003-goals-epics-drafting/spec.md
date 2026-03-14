# Feature Specification: Drafting Skills for GOALS and EPICS

**Feature Branch**: `003-goals-epics-drafting`  
**Created**: 2026-03-13  
**Status**: Draft  
**Input**: User description: "Let's add a few new skills. I need a skill which helps the user draft an appropriate GOALS.md file, and I need a skill which helps the user draft an appropriate EPICS.md file based on the constitution.mnd and the GOALS.md. The EPICS.md file must be in the format expected by the speckit loop agent."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Project Mission Definition (Priority: P1)

As a project lead, I want to use a skill to draft a `GOALS.md` file so that I can clearly define the project's mission and constraints in a standardized format.

**Why this priority**: Goals provide the necessary context for all subsequent automation and planning.
**Independent Test**: Run `/project.goals` and verify that a valid `GOALS.md` is created with a mission statement and constraints.

**Acceptance Scenarios**:

1. **Given** a new project, **When** I trigger the goals drafting skill with my mission ideas, **Then** it produces a `GOALS.md` file with "# Project Mission" and "# Constraints" headers.

---

### User Story 2 - Automated Roadmap Drafting (Priority: P2)

As a developer, I want a skill to generate an `EPICS.md` file that is aligned with the project's constitution and goals so that I can establish a roadmap that is compatible with the SpecKit automation loop.

**Why this priority**: Standardized epics are required for the autonomous loop to function.
**Independent Test**: Run `/project.epics` and verify the output file is successfully parsed by the `speckit-loop` CLI.

**Acceptance Scenarios**:

1. **Given** an existing `GOALS.md` and `constitution.md`, **When** I trigger the epics drafting skill, **Then** it generates an `EPICS.md` file where each feature uses the `## [Title]` format.
2. **Given** a generated `EPICS.md`, **When** I run `uv run speckit-loop next`, **Then** the first pending epic is correctly identified.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST provide a skill (`/project.goals`) to assist in creating or updating `GOALS.md`.
- **FR-002**: System MUST provide a skill (`/project.epics`) to assist in creating or updating `EPICS.md`.
- **FR-003**: The EPICS drafting skill MUST read `.specify/memory/constitution.md` and `GOALS.md` to ensure feature sets align with project principles and mission.
- **FR-004**: `EPICS.md` MUST use the format: `## [Title]`, `Description: <text>`, `Priority: <int>`, and `- [ ] Status: <status>`.
- **FR-005**: The drafting skills SHOULD provide templates or suggestions if the user provides minimal input.

### Key Entities

- **Goal Set**: The combination of mission statement and constraints defined in `GOALS.md`.
- **Epic Entry**: A structured feature definition in `EPICS.md` compatible with the automation engine.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Generated `EPICS.md` passes `speckit-loop` validation with 100% accuracy.
- **SC-002**: Drafted goals and epics are explicitly linked to at least one principle from the project constitution.
- **SC-003**: Time to scaffold a project roadmap is reduced from ~30 minutes to under 5 minutes.

## Edge Cases

- **Missing Constitution**: If `constitution.md` is missing, the skill MUST warn the user but still offer to draft based on provided context.
- **Duplicate Priorities**: The skill SHOULD ensure that generated epics have unique, sequential priority numbers.
