# newSkills Development Guidelines

Auto-generated from all feature plans. Last updated: 2026-03-13

## Active Technologies
- Python 3.11+, Bash/Shell + `mcp` (SDK), `pydantic`, `pyyaml` (001-agent-agnostic-skills)
- Local filesystem (JSON manifest, directory-based artifact storage) (001-agent-agnostic-skills)
- Python 3.11+, Bash/Shell + `click` (CLI), `pydantic` (Data Parsing), `git` (CLI), `pyyaml` (002-speckit-automation)
- Filesystem (`EPICS.md`, `GOALS.md`, `specs/`) (002-speckit-automation)
- Python 3.11+, Markdown + `newskills` (the local agent-agnostic framework) (003-goals-epics-drafting)
- Filesystem (Markdown files) (003-goals-epics-drafting)

- Python 3.11+, Bash/Shell + `mcp` (SDK), `pydantic` (for manifest validation), `pyyaml` (001-agent-agnostic-skills)

## Project Structure

```text
src/
tests/
```

## Commands

cd src [ONLY COMMANDS FOR ACTIVE TECHNOLOGIES][ONLY COMMANDS FOR ACTIVE TECHNOLOGIES] pytest [ONLY COMMANDS FOR ACTIVE TECHNOLOGIES][ONLY COMMANDS FOR ACTIVE TECHNOLOGIES] ruff check .

## Code Style

Python 3.11+, Bash/Shell: Follow standard conventions

## Recent Changes
- 003-goals-epics-drafting: Added Python 3.11+, Markdown + `newskills` (the local agent-agnostic framework)
- 002-speckit-automation: Added Python 3.11+, Bash/Shell + `click` (CLI), `pydantic` (Data Parsing), `git` (CLI), `pyyaml`
- 001-agent-agnostic-skills: Added Python 3.11+, Bash/Shell + `mcp` (SDK), `pydantic`, `pyyaml`


<!-- MANUAL ADDITIONS START -->
<!-- MANUAL ADDITIONS END -->
