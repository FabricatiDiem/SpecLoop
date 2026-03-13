# Quickstart: Creating and Deploying Capabilities

This guide explains how to add skills, tools, subagents, and scripts to the repository and deploy them to your AI agents.

## 1. Adding a New Skill (Markdown)

1. Create a new `.md` file in the `skills/` directory.
2. Add the OpenCode-compatible YAML frontmatter at the top:

```markdown
---
description: "Brief description of what the skill does"
inputs:
  - name: "arg1"
    description: "Description of the first argument"
handoffs:
  - label: "Next Step"
    agent: "other.skill"
    prompt: "Proceed to the next task..."
---

# Skill Name

1. Step one...
2. Step two...
```

3. Run discovery: `python -m agent_agnostic discover`

## 2. Adding a New Tool (MCP Server)

1. Create a new directory in `mcp_servers/`.
2. Implement your MCP server (e.g., with Python `mcp` SDK).
3. Register the tool in `skills.json` via the manifest discovery.

## 3. Adding a New Script (Python/Shell)

1. Create a Python or Shell file in the `scripts/` directory.
2. The framework's MCP runner will dynamically expose it as a tool.
3. Add it to the manifest with its interpreter and argument schema.

## 4. Adding a New Subagent (Composite Markdown)

1. Create a new `.md` file in the `subagents/` directory.
2. Add the required frontmatter to list tool/skill dependencies:

```markdown
---
name: "Code Reviewer Subagent"
description: "Specialized subagent for code analysis"
dependencies:
  skills: ["git-workflow"]
  tools: ["diff-analysis"]
  scripts: ["lint-check"]
---

# Code Reviewer Instructions

You are a senior software engineer specialized in code quality...
```

## 5. Deploying to Agents

To synchronize all capabilities (skills, tools, scripts, subagents) with a specific agent, run:

```bash
# Sync with Claude Code
python -m agent_agnostic deploy --target claude

# Sync with Gemini CLI
python -m agent_agnostic deploy --target gemini

# Sync with OpenCode
python -m agent_agnostic deploy --target opencode
```

## 6. Verification

Verify by asking the agent to list its capabilities or by invoking a new subagent or script directly.
