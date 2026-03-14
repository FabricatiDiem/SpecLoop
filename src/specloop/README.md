# SpecLoop: Agent-Agnostic Skills Framework

This framework allows you to develop AI capabilities (skills, tools, scripts, subagents) that work across multiple AI agents like Claude Code, Gemini CLI, and OpenCode.

## Key Concepts

- **Skills**: Natural language procedures defined in Markdown.
- **Tools**: Executable logic implemented as MCP servers.
- **Scripts**: Python or Shell scripts exposed via a generic MCP runner.
- **Subagents**: Specialized agent definitions that compose skills and tools.
- **Manifest**: A central `skills.json` registry.

## Usage

### 1. Discovery
Scan the repository to update the manifest:
```bash
export PYTHONPATH=$PYTHONPATH:$(pwd)/src
python -m specloop.cli discover
```

### 2. Verification
Check the manifest against the schema:
```bash
python -m specloop.cli verify
```

### 3. Deployment
Sync capabilities to your preferred agent:
```bash
python -m specloop.cli deploy --target claude
python -m specloop.cli deploy --target gemini
python -m specloop.cli deploy --target opencode
```

## Structure
- `skills/`: Markdown procedures.
- `mcp_servers/`: Executable tools.
- `scripts/`: Task scripts.
- `subagents/`: Agent definitions.
- `src/specloop/`: Framework core logic.
