# Feature Specification: Roadmap Review and Optimization Skill

**Feature Branch**: `004-roadmap-review-optimization`  
**Created**: 2026-03-13  
**Status**: Draft  
**Input**: User description: "Let's create a new skill which reviews the constitution.md, GOALS.md, and EPICS.md and reviews for any epic-level gaps, status alignment, suggestions, etc. It should also review the dependencies and priorities of each epic and suggest an optimal ordering."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Roadmap Alignment Audit (Priority: P1)

As a project lead, I want to review the current roadmap against the project goals and constitution so that I can identify gaps in planned features and ensure we are building the right things.

**Why this priority**: Alignment is fundamental to project success. Without it, the roadmap might drift from the core mission.

**Independent Test**: Run `/roadmap.review` on a project with a set of epics and goals. Verify that the skill identifies at least one gap or alignment issue if the epics don't fully cover the mission statement.

**Acceptance Scenarios**:

1. **Given** a `GOALS.md` with a specific mission and an `EPICS.md` that missing key features to achieve that mission, **When** I run `/roadmap.review`, **Then** the system identifies the missing feature sets as "gaps".
2. **Given** a `constitution.md` with strict quality principles, **When** I run `/roadmap.review`, **Then** it checks if the current epics provide enough coverage for those quality principles (e.g., observability, testing).

---

### User Story 2 - Dependency and Priority Optimization (Priority: P2)

As a developer, I want the system to analyze the dependencies between epics and suggest an optimal ordering so that we avoid blockers and maximize development efficiency.

**Why this priority**: Efficient execution saves time and resources. Incorrect ordering can lead to costly rework.

**Independent Test**: Create an `EPICS.md` with conflicting priorities (e.g., Epic B depends on Epic A, but Epic B has higher priority). Run `/roadmap.optimize` and verify it suggests reordering them correctly.

**Acceptance Scenarios**:

1. **Given** epics with implied or explicit dependencies, **When** I run `/roadmap.optimize`, **Then** the system proposes an ordering where dependencies are completed before the features that rely on them.
2. **Given** multiple epics with the same priority, **When** I run `/roadmap.optimize`, **Then** it suggests a tie-breaking order based on complexity or foundational value.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The system MUST provide a skill (`/roadmap.review`) to analyze the relationship between `constitution.md`, `GOALS.md`, and `EPICS.md`.
- **FR-002**: The system MUST identify "Epic-level gaps"—features required by goals or constitution but missing from the roadmap.
- **FR-003**: The system MUST check for "Status Alignment"—identifying inconsistencies between epic status and their dependencies (e.g., an epic marked `Completed` while its dependency is `Pending`).
- **FR-004**: The system MUST provide a skill (`/roadmap.optimize`) to analyze dependencies and priorities.
- **FR-005**: The optimization skill MUST suggest a reordered list of epics that minimizes blocking and aligns with stated priorities.
- **FR-006**: The system MUST explicitly reference specific principles from `constitution.md` when suggesting changes or identifying gaps.

### Key Entities

- **Gap**: A requirement derived from goals or constitution that is not addressed by any existing epic.
- **Alignment Issue**: A contradiction between files (e.g., goal says "Go only", epic description says "implement in Node.js").
- **Optimal Order**: A permutation of epics that satisfies all dependencies while respecting priority weightings as much as possible.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Auditing a roadmap for alignment takes less than 2 minutes of agent processing time.
- **SC-002**: 100% of detected dependency conflicts in `EPICS.md` are correctly flagged by the system.
- **SC-003**: Proposed roadmap updates are explicitly justified by quoting at least one line from the source documents (`constitution.md`, `GOALS.md`).

## Edge Cases

- **Circular Dependencies**: How should the system handle epics that appear to depend on each other? (Should flag as an error/blocker).
- **Ambiguous Descriptions**: If an epic description is too vague to determine alignment, the system SHOULD request clarification.
- **Conflicting Goals**: If `GOALS.md` has internal contradictions, the system SHOULD flag this during the review.
