# Quickstart: Reviewing and Optimizing Your Roadmap

This guide explains how to use the roadmap intelligence skills to refine your project trajectory.

## 1. Run Alignment Review

Trigger the review skill in your agent:
```text
/roadmap.review
```
The agent will:
1. Read `constitution.md`, `GOALS.md`, and `EPICS.md`.
2. Identify functional gaps (goals not covered by epics).
3. Identify alignment issues (conflicts with project principles).
4. Identify status alignment issues (impossible state transitions).

## 2. Run Dependency Optimization

Trigger the optimization skill:
```text
/roadmap.optimize
```
The agent will:
1. Analyze all epics for implicit and explicit dependencies.
2. Calculate an optimal execution order based on blocking relationships and priorities.
3. Propose a new, reordered `EPICS.md` content block for your review.

## 3. Apply Changes

Once you approve the suggestions:
1. The agent will write the new epics to `EPICS.md`.
2. You can then resume the autonomous loop:
   ```bash
   uv run speckit-loop run
   ```
