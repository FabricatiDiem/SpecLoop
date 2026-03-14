# Tasks: Drafting Skills for GOALS and EPICS

**Input**: Design documents from `/specs/003-goals-epics-drafting/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Tests are recommended for the drafting logic via manual verification or simulated agent runs.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create root `skills/` directory if missing
- [ ] T002 Initialize `skills/project_goals.md` with basic frontmatter
- [ ] T003 [P] Initialize `skills/project_epics.md` with basic frontmatter

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

- [ ] T004 Create a shared drafting prompt template or pattern for agent instructions

---

## Phase 3: User Story 1 - Project Mission Definition (Priority: P1) 🎯 MVP

**Goal**: Draft a `GOALS.md` file with mission statement and constraints.

**Independent Test**: Run `/project.goals` and verify that a valid `GOALS.md` is created with a mission statement and constraints.

### Implementation for User Story 1

- [ ] T005 [US1] Implement procedure in `skills/project_goals.md` to read `constitution.md` first
- [ ] T006 [US1] Implement interactive drafting logic in `skills/project_goals.md` (Mission and Constraints)
- [ ] T007 [US1] Add file write instruction for `GOALS.md` in `skills/project_goals.md`
- [ ] T008 [US1] Add user confirmation gate before writing `GOALS.md`

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently.

---

## Phase 4: User Story 2 - Automated Roadmap Drafting (Priority: P2)

**Goal**: Generate an `EPICS.md` file aligned with constitution and goals, formatted for the automation loop.

**Independent Test**: Run `/project.epics` and verify the output file is successfully parsed by the `speckit-loop` CLI.

### Implementation for User Story 2

- [ ] T009 [US2] Implement procedure in `skills/project_epics.md` to read `constitution.md` and `GOALS.md`
- [ ] T010 [US2] Implement "Schema Template" block in `skills/project_epics.md` for strict enforcement of the `speckit-loop` format
- [ ] T011 [US2] Implement logic to link each epic to at least one constitution principle
- [ ] T012 [US2] Implement iterative refinement logic (Draft -> Review -> Finalize) in `skills/project_epics.md`
- [ ] T013 [US2] Add file write instruction for `EPICS.md` in `skills/project_epics.md`

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently.

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T014 [P] Update `README.md` with instructions for the new `/project.goals` and `/project.epics` commands
- [ ] T015 Run `uv run skills discover` to verify new skills are correctly registered
- [ ] T016 Run `uv run skills verify` to ensure the manifest is valid with the new skills
- [ ] T017 [P] Finalize `quickstart.md` in `specs/003-goals-epics-drafting/` with real examples

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User Story 1 (P1) is the primary priority
  - User Story 2 (P2) can be worked on after or in parallel with US1 (since they are separate files)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2)
- **User Story 2 (P2)**: Can start after Foundational (Phase 2); depends on `GOALS.md` existing for testing, but implementation can be parallel

### Parallel Opportunities

- Setup tasks (T002, T003) can run in parallel
- US1 and US2 can run in parallel as they affect different files
- Documentation tasks (T014, T017) can run in parallel

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Verify `/project.goals` creates `GOALS.md` correctly.

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deliver (Goal Drafting)
3. Add User Story 2 → Test independently → Deliver (Epic Drafting)
