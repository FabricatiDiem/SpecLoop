# SpecKit Automation Loop

The SpecKit Automation Loop is a high-level orchestration engine designed to automate the entire development lifecycle of a repository based on a set of global goals and a backlog of epics.

## Core Components

- **Parsers**: Handles the reading and updating of `EPICS.md` and `GOALS.md`.
- **Engine**:
    - `LoopRunner`: Orchestrates the selection and processing of epics.
    - `WorkflowEngine`: Manages the state transitions through SpecKit phases.
    - `Orchestrator`: Simulates or executes SpecKit commands via subprocess calls.
    - `Verifier`: Dynamically discovers and runs project verification tools (e.g., `pytest`, `ruff`) from the project's `constitution.md`.
- **Git Wrapper**: Manages branch creation and grouped commits.

## Workflow

1.  **Selection**: The runner selects the first incomplete epic from `EPICS.md`.
2.  **Creation**: A new feature branch is created for the epic.
3.  **SpecKit Cycle**:
    - `SPECIFY`: Generates `spec.md` with global goal context.
    - `PLAN`: Generates implementation plans.
    - `TASKS`: Breaks down the work into prioritized tasks.
    - `ANALYZE`: Ensures consistency and applies auto-remedies for ambiguities.
    - `IMPLEMENT`: Executes the task definitions.
4.  **Verification**: Runs project-defined quality gates (linters, tests).
5.  **Commit**: Performs logical git commits per phase.
6.  **Update**: Marks the epic as completed in `EPICS.md`.
7.  **Recursion**: Loops back to step 1 until all epics are finished.

## Usage

```bash
export PYTHONPATH=$PYTHONPATH:$(pwd)/src
python3 -m speckit_loop.cli run --file EPICS.md --goals GOALS.md
```
