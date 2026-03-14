# SpecLoop Toolkit

An agent-agnostic framework for developing, deploying, and automating AI capabilities (skills, tools, subagents).

## Features

- **Agent-Agnostic Skills**: Define skills once in Markdown and deploy to Claude Code, Gemini CLI, and OpenCode simultaneously.
- **MCP Tool Integration**: Build executable tools as Model Context Protocol (MCP) servers.
- **Autonomous Development Loop**: Automate the full GitHub SpecKit workflow (Specify -> Plan -> Tasks -> Implement -> Commit) via `EPICS.md` and `GOALS.md`.

## Installation

To use this toolkit in another project, install it directly from GitHub:

```bash
pip install git+https://github.com/anomalyco/SpecLoop.git
```

Or using `uv`:

```bash
uv add git+https://github.com/anomalyco/SpecLoop.git
```

## Getting Started in a New Project

1. **Initialize the structure**:
   ```bash
   specloop init
   ```
   This creates the necessary directories (`skills/`, `subagents/`, etc.) and template `EPICS.md` / `GOALS.md` files for all supported agents.

2. **Define your goals**:
   Draft your project mission and constraints:
   ```bash
   # In OpenCode, Claude, or Gemini
   /project.goals "I want to build a secure file sharing app"
   ```

3. **Add Epics**:
   Generate a loop-compatible roadmap:
   ```bash
   # In OpenCode, Claude, or Gemini
   /project.epics
   ```

4. **Review & Optimize Roadmap**:
   Audit alignment and optimize dependency ordering:
   ```bash
   # In OpenCode, Claude, or Gemini
   /roadmap.review
   /roadmap.optimize
   ```

5. **Deploy to Agents**:
   Sync your capabilities to all your AI harnesses:
   ```bash
   specloop deploy --target all
   ```

6. **Run the automation loop**:
   ```bash
   # Use the autonomous agent in your harness
   @specloop start the implementation loop
   
   # Or trigger it via command
   /specloop
   ```

## Development

If you are developing the toolkit itself:

```bash
# Set up development environment
uv sync
export PYTHONPATH=src

# Run discovery
python -m specloop.cli discover

# Run automation loop
python -m specloop.cli run
```
