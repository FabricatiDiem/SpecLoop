# Research: SpecKit Automation Loop

## Epic Parsing Strategies

- **Decision**: Use a strict Markdown checkbox and header hierarchy for `EPICS.md`.
- **Rationale**: This allows for both human readability and easy machine parsing via regex or Markdown AST parsers. It follows the existing SpecKit convention for `tasks.md`.
- **Structure**: 
  - `## [Feature Name]` (Epic title)
  - `Description: ...` (Passed to `/speckit.specify`)
  - `- [ ] Status: Pending`

## Command Orchestration

- **Decision**: The Python orchestrator will use `subprocess` to invoke the agent-based commands (e.g., `opencode speckit.specify`).
- **Rationale**: Since SpecKit commands are delivered via agent-specific files (`.opencode/command/`), the loop runner must act as a harness that feeds the correct inputs to the agent and monitors the resulting file outputs.
- **Handling Ambiguity**: For commands like `/speckit.analyze`, the orchestrator will pass a pre-prompt instruction: "You are running in an autonomous loop. For any ambiguities or decision points, proceed with the 'Recommended' action immediately without requesting user input." This ensures non-blocking execution while maintaining SpecKit's quality standards.

## Recursive Loop Mechanism

- **Decision**: State-based recursion.
- **Rationale**: The loop runner will:
  1. Parse `EPICS.md`.
  2. Select the first incomplete `[ ]` item.
  3. Change its status to `[~] In Progress`.
  4. Execute SpecKit sequence.
  5. On success, mark as `[x] Completed`.
  6. On failure, mark as `[!] Failed` and stop.
  7. Re-parse and continue if `[ ]` remains.

## Integration with constitution.md

- **Decision**: The `Test` and `Commit` phases will dynamically read the `Technology Stack` and `Quality Assurance` sections of `constitution.md`.
- **Rationale**: This ensures the automation script remains project-agnostic. If the constitution says `pytest`, the script runs `pytest`. If it says `npm test`, it runs that.
