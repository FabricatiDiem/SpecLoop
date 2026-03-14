# Tasks: Roadmap Review and Optimization Skill

**Input**: Design documents from `/specs/004-roadmap-review-optimization/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Tests are recommended for logical verification of the audit and optimization reasoning.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths assume single project structure as defined in plan.md

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create project structure per implementation plan: `skills/`
- [ ] T002 Initialize `skills/roadmap_review.md` with basic frontmatter
- [ ] T003 [P] Initialize `skills/roadmap_optimize.md` with basic frontmatter

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T004 Define shared Requirement Matrix prompts in `research.md`
- [ ] T005 [P] Create a mock project roadmap with known dependency conflicts for testing in `tests/fixtures/EPICS_MOCK.md`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Roadmap Alignment Audit (Priority: P1) 🎯 MVP

**Goal**: Identify gaps and alignment issues between goals and the roadmap.

**Independent Test**: Run `/roadmap.review` on a project with a set of epics and goals. Verify that the skill identifies at least one gap or alignment issue.

### Implementation for User Story 1

- [ ] T006 [US1] Implement context loading (read constitution, goals, epics) in `skills/roadmap_review.md`
- [ ] T007 [US1] Implement Requirement Mapping logic (Gap detection) with explicit principle citations in `skills/roadmap_review.md`
- [ ] T008 [US1] Implement Status Alignment logic (dependency vs status check) in `skills/roadmap_review.md`
- [ ] T009 [US1] Define structured output format (Markdown tables) in `skills/roadmap_review.md`
- [ ] T010 [US1] Manually audit audit results against `EPICS_MOCK.md` to verify accuracy (Self-verification gate)

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Dependency and Priority Optimization (Priority: P2)

**Goal**: Analyze dependencies and suggest an optimal ordering for the roadmap.

**Independent Test**: Create an `EPICS.md` with conflicting priorities and run `/roadmap.optimize` to verify it suggests reordering them correctly.

### Implementation for User Story 2

- [ ] T011 [US2] Implement dependency extraction logic from epic descriptions in `skills/roadmap_optimize.md`
- [ ] T012 [US2] Implement topological sorting logic with foundational tie-breakers and principle citations in `skills/roadmap_optimize.md`
- [ ] T013 [US2] Implement impossible state detection logic in `skills/roadmap_optimize.md`
- [ ] T014 [US2] Add literal `EPICS.md` output generation per contract in `skills/roadmap_optimize.md`
- [ ] T015 [US2] Verify optimized ordering logic against complex DAG scenarios in `tests/fixtures/EPICS_MOCK.md` (Self-verification gate)

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T016 [P] Update project `README.md` with instructions for `/roadmap.review` and `/roadmap.optimize`
- [ ] T017 Run `uv run skills discover` to verify registration of new skills
- [ ] T018 Run `uv run skills verify` to ensure manifest validity
- [ ] T019 [P] Finalize `quickstart.md` in `specs/004-roadmap-review-optimization/` with real-world examples

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel
  - Or sequentially in priority order (P1 → P2)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories

### Parallel Opportunities

- Setup tasks (T002, T003) can run in parallel
- US1 and US2 can be implemented in parallel by different agents
- Documentation tasks (T014, T017) can run in parallel

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Verify alignment audit identifies missing epics

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deliver (Audit)
3. Add User Story 2 → Test independently → Deliver (Optimization)
