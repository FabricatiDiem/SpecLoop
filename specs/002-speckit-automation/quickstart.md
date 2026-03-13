# Quickstart: running the SpecKit Automation Loop

This guide explains how to set up your project goals and epics, and then run the autonomous developer loop.

## 1. Define Project Goals

Create `GOALS.md` in the repository root:

```markdown
# Project Mission
Build a robust agentic framework for cross-platform skill deployment.

# Constraints
- Python 3.11+ only.
- Strict type checking with Pydantic.
- Every tool must be MCP-compliant.
```

## 2. Populate the Epic Backlog

Create `EPICS.md` in the repository root:

```markdown
# Project Epics

## [Add User Authentication]
Description: Implement a secure JWT-based authentication system.
Priority: 1
- [ ] Status: Pending

## [Integrate Database]
Description: Add PostgreSQL support via SQLAlchemy.
Priority: 2
- [ ] Status: Pending
```

## 3. Run the Automation Engine

Ensure the `PYTHONPATH` is set and execute the loop:

```bash
export PYTHONPATH=$PYTHONPATH:$(pwd)/src
python -m speckit_loop.cli run --file EPICS.md
```

## 4. Monitoring Progress

The script will:
1.  Checkout a new feature branch for the top epic.
2.  Log progress through Specify, Plan, and Implement phases.
3.  Automatically commit changes when tests pass.
4.  Update the status in `EPICS.md` to `[x] Status: Completed`.
5.  Continue to the next epic until the file is fully processed.
