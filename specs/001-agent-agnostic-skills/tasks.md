# Tasks: Agent-Agnostic Skills Framework

**Input**: Design documents from `/specs/001-agent-agnostic-skills/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Tests are OPTIONAL - only include them if explicitly requested in the feature specification. *Note: Spec mentions "Independent Test" criteria for verification, which will be implemented as integration checks.*

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

- [X] T001 Create project structure per implementation plan: `src/agent_agnostic/`, `mcp_servers/`, `skills/`, `subagents/`, `scripts/`, `tests/`
- [X] T002 [P] Initialize Python project with dependencies (`mcp`, `pydantic`, `pyyaml`) in `pyproject.toml`
- [X] T003 [P] Configure linting and formatting tools (Ruff) in `pyproject.toml`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T004 Implement Pydantic models for Manifest, Skill, Tool, Script, and Subagent in `src/agent_agnostic/models/manifest.py`
- [X] T005 Create JSON schema validation logic using `skills-schema.json` in `src/agent_agnostic/models/validator.py`
- [X] T006 Implement discovery logic to scan all artifact directories and generate/update `skills.json` in `src/agent_agnostic/discovery.py`
- [X] T007 Initialize CLI entry point with `discover` command in `src/agent_agnostic/cli.py`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Create an Agent-Agnostic Skill (Priority: P1) 🎯 MVP

**Goal**: Create a skill once so that it can be used across multiple AI agents (Gemini CLI, Claude Code, OpenCode).

**Independent Test**: Create a simple skill (procedure or tool) and verify it can be loaded and executed by at least two different agents.

### Implementation for User Story 1

- [X] T008 [P] [US1] Create a sample MCP-compliant "hello-world" tool in `mcp_servers/hello_world/server.py`
- [X] T009 [P] [US1] Create a sample Markdown procedure "greet-user" with OpenCode frontmatter in `skills/greet_user.md`
- [X] T010 [US1] Run discovery and verify `skills.json` contains both the new tool and skill
- [X] T011 [US1] Implement a verification command `skills verify` to check all skills/tools against the schema in `src/agent_agnostic/cli.py`

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently.

---

## Phase 4: User Story 2 - Deploy Skill to Multiple Environments (Priority: P2)

**Goal**: Unified deployment process for distributing skills to different agentic workflows.

**Independent Test**: Use a single command/script to deploy a skill to a shared location and update the `skills.json` manifest.

### Implementation for User Story 2

- [X] T012 [P] [US2] Implement deployment logic for Claude Code (syncing to `.claudecode`) in `src/agent_agnostic/deployment/claude.py`
- [X] T013 [P] [US2] Implement deployment logic for Gemini CLI in `src/agent_agnostic/deployment/gemini.py`
- [X] T014 [P] [US2] Implement deployment logic for OpenCode (syncing to `.opencode/command`) in `src/agent_agnostic/deployment/opencode.py`
- [X] T015 [US2] Add `deploy` command to the CLI supporting `--target` (claude, gemini, opencode) in `src/agent_agnostic/cli.py`
- [X] T016 [US2] Add deployment logging and error handling in `src/agent_agnostic/deployment/base.py`

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently.

---

## Phase 5: User Story 3 - Define and Register a Subagent (Priority: P3)

**Goal**: Define a subagent with specific instructions and required tools/skills.

**Independent Test**: Create a subagent definition in Markdown, list its tool dependencies, and verify it appears in the manifest and can be "installed" to a target harness.

### Implementation for User Story 3

- [ ] T017 [P] [US3] Implement subagent discovery logic (parsing system prompt and frontmatter) in `src/agent_agnostic/discovery.py`
- [ ] T018 [P] [US3] Create a sample "Code Reviewer" subagent in `subagents/code_reviewer.md` with dependencies on `greet-user`
- [ ] T019 [US3] Update deployment logic to include subagent "installation" (harness-specific config updates) in `src/agent_agnostic/deployment/`
- [ ] T020 [US3] Implement MCP-compliant script runner for Python/Shell scripts in `src/agent_agnostic/runner/server.py`
- [ ] T021 [US3] Integrate script runner discovery and deployment into the manifest and CLI

**Checkpoint**: All user stories should now be independently functional.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T022 [P] Finalize `quickstart.md` with concrete CLI command examples
- [ ] T023 [P] Add README documentation for the `agent_agnostic` framework in `src/agent_agnostic/README.md`
- [ ] T024 Run full verification of all capability types across all target agents
- [ ] T025 Code cleanup and docstring additions across `src/agent_agnostic/`

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Deployment scripts for different agents (T012, T013, T014) can run in parallel
- Subagent and Script Runner tasks (T017, T018, T020) can run in parallel

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Verify core definition and discovery functionality

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deliver (Core Capability)
3. Add User Story 2 → Test independently → Deliver (Multi-Agent Sync)
4. Add User Story 3 → Test independently → Deliver (Subagents & Scripts)
