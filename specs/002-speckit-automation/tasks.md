# Tasks: SpecKit Automation Loop

**Input**: Design documents from `/specs/002-speckit-automation/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Tests are recommended for the parsers and orchestration engine.

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

- [X] T001 Create project structure per implementation plan: `src/speckit_loop/engine/`, `src/speckit_loop/parsers/`, `src/speckit_loop/git/`
- [X] T002 [P] Initialize Python dependencies in `pyproject.toml` (click, pydantic, pyyaml)
- [X] T003 [P] Configure linting and formatting (Ruff) in `pyproject.toml`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T004 Implement `EPICS.md` parser using Pydantic models in `src/speckit_loop/parsers/epic_parser.py`
- [X] T005 [P] Implement `GOALS.md` parser in `src/speckit_loop/parsers/goal_parser.py`
- [X] T006 [P] Implement Git wrapper for branch creation and grouped commits in `src/speckit_loop/git/wrapper.py`
- [X] T007 Initialize CLI entry point with `run` command in `src/speckit_loop/cli.py`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Automate a Single Epic Implementation (Priority: P1) 🎯 MVP

**Goal**: Automate the entire SpecKit lifecycle for one epic.

**Independent Test**: Run the script on a single epic and verify branch creation, file generation, implementation, and commit.

### Implementation for User Story 1

- [X] T008 Implement the core Workflow engine (state transitions) in `src/speckit_loop/engine/workflow.py`
- [X] T009 Implement subprocess command orchestration for SpecKit agent calls in `src/speckit_loop/engine/orchestrator.py`
- [X] T010 [P] Implement dynamic tool discovery from `constitution.md` in `src/speckit_loop/engine/verifier.py`
- [X] T011 [US1] Integrate `SPECIFY` and `PLAN` phases into the loop runner
- [X] T012 [US1] Integrate `TASKS`, `ANALYZE`, and `IMPLEMENT` phases into the loop runner
- [X] T013 [US1] Implement "auto-remedy" logic for the `ANALYZE` phase to accept recommended actions
- [X] T014 [US1] Implement self-verification gate (logs/debug/unit tests) for generated code in `IMPLEMENT` phase
- [X] T015 [US1] Implement `VERIFY` phase: trigger linter check per `constitution.md`
- [X] T016 [US1] Implement `VERIFY` phase: trigger unit test suite per `constitution.md`
- [X] T017 [US1] Implement `COMMIT` phase using the Git wrapper for grouped commits (per phase)
- [X] T018 [US2] Implement the main loop logic to select and process epics until none remain in `src/speckit_loop/engine/loop.py`
- [X] T019 [US2] Implement logic to update epic status in `EPICS.md` (e.g., [ ] -> [x]) in `src/speckit_loop/parsers/epic_parser.py`
- [X] T020 [US2] Add error handling and reporting for failed epics within the loop
- [X] T021 [US3] Update the orchestration engine to inject `GOALS.md` context into the SpecKit agent prompts
- [X] T022 [US3] Verify that generated specs reflect global project constraints
- [X] T023 [P] Finalize `quickstart.md` with concrete execution examples
- [X] T024 [P] Add README documentation for the SpecKit Loop engine in `src/speckit_loop/README.md`
- [X] T025 Run full system verification with a multi-epic test project
- [X] T026 Code cleanup and docstring additions across `src/speckit_loop/`

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - US1 (MVP) is the priority.
  - US2 builds on US1.
  - US3 enhances the context of the automation.
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### Parallel Opportunities

- Setup tasks (T002, T003) can run in parallel.
- Parser tasks (T004, T005) and Git wrapper (T006) can run in parallel.
- Documentation tasks (T020, T021) can run in parallel.

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Verify end-to-end automation for a single epic.

### Incremental Delivery

1. Complete Setup + Foundational -> Foundation ready
2. Add User Story 1 -> Test independently -> Deliver (Core Automation)
3. Add User Story 2 -> Test independently -> Deliver (Autonomous Loop)
4. Add User Story 3 -> Test independently -> Deliver (Mission Alignment)
