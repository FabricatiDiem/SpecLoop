# Roadmap Optimization Contract

The `/roadmap.optimize` skill MUST produce a suggested `EPICS.md` content block that follows this structure.

## Suggested Optimized Order

1. **Topological Feasibility**: All dependencies MUST appear before the features that rely on them.
2. **Priority Weighting**: When multiple epics are feasible, the one with the lowest original `Priority` integer MUST be listed first.
3. **Justification**: The agent MUST provide a brief rationale for any priority changes.

### Example Suggestion

```markdown
# Project Epics (Optimized)

## [Database Setup]
Description: ...
Priority: 1
- [ ] Status: Pending

## [API Endpoints]
Description: (Depends on [Database Setup])
Priority: 2
- [ ] Status: Pending
```
