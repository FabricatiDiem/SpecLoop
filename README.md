# newSkills Toolkit

An agent-agnostic framework for developing, deploying, and automating AI capabilities (skills, tools, subagents).

## Features

- **Agent-Agnostic Skills**: Define skills once in Markdown and deploy to Claude Code, Gemini CLI, or OpenCode.
- **MCP Tool Integration**: Build executable tools as Model Context Protocol (MCP) servers.
- **Autonomous Development Loop**: Automate the full GitHub SpecKit workflow (Specify -> Plan -> Tasks -> Implement -> Commit) via `EPICS.md` and `GOALS.md`.

## Installation

To use this toolkit in another project, install it directly from GitHub:

```bash
pip install git+https://github.com/anomalyco/newSkills.git
```

Or using `uv`:

```bash
uv add git+https://github.com/anomalyco/newSkills.git
```

## Getting Started in a New Project

1. **Initialize the structure**:
   ```bash
   skills init
   ```
   This creates the necessary directories (`skills/`, `subagents/`, etc.) and template `EPICS.md` / `GOALS.md` files.

2. **Define your goals**:
   Update `GOALS.md` with your project mission and constraints.

3. **Add an Epic**:
   Add a feature to `EPICS.md`.

4. **Run the automation loop**:
   ```bash
   speckit-loop run
   ```

## Development

If you are developing the toolkit itself:

```bash
# Set up development environment
uv sync
export PYTHONPATH=src

# Run discovery
python -m agent_agnostic.cli discover

# Run automation loop
python -m speckit_loop.cli run
```
