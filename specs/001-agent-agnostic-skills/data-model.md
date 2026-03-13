# Data Model: Agent-Agnostic Skills Framework

This document defines the core entities and data structures for managing agent-agnostic skills and tools.

## 1. Manifest (`skills.json`)

The manifest is the root registry for all capabilities in the repository.

| Field | Type | Description |
| :--- | :--- | :--- |
| `version` | `string` | Semantic version of the manifest format. |
| `repository` | `string` | URL or name of the source repository. |
| `skills` | `Array<Skill>` | List of Markdown-based natural language skills. |
| `tools` | `Array<Tool>` | List of MCP-compliant executable tools. |
| `subagents` | `Array<Subagent>`| List of Markdown-based subagent definitions. |
| `scripts` | `Array<Script>` | List of Python and Shell scripts. |

## 2. Skill Entity

Represents a natural language procedure.

| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | `string` | Unique identifier (kebab-case). |
| `name` | `string` | Human-readable name. |
| `path` | `string` | Relative path to the `.md` file. |
| `metadata` | `object` | Parsed YAML frontmatter (OpenCode format). |
| `tags` | `Array<string>` | Categorization tags. |

## 3. Tool Entity

Represents an executable MCP server.

| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | `string` | Unique identifier (kebab-case). |
| `name` | `string` | Human-readable name. |
| `type` | `string` | `mcp` (always `mcp` for this phase). |
| `command` | `string` | Command to start the server (e.g., `python -m server`). |
| `env` | `object` | Required environment variables. |
| `capabilities` | `Array<string>`| List of tool names exposed by this server. |

## 4. Subagent Entity

Represents a high-level agent definition.

| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | `string` | Unique identifier (kebab-case). |
| `name` | `string` | Human-readable name. |
| `path` | `string` | Relative path to the `.md` file. |
| `system_prompt`| `string` | The natural language instructions for the agent. |
| `dependencies` | `object` | Required skills, tools, and scripts. |

## 5. Script Entity

Represents a Python or Shell file exposed via MCP.

| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | `string` | Unique identifier (kebab-case). |
| `name` | `string` | Human-readable name. |
| `interpreter` | `string` | `python` or `bash`. |
| `path` | `string` | Relative path to the script file. |
| `args` | `Array<string>`| Argument schema for the script. |

## 6. State Transitions

- **Discovery**: The framework scans the `skills/`, `mcp_servers/`, `subagents/`, and `scripts/` directories to generate or update the `skills.json` manifest.
- **Deployment**: The deployment CLI reads `skills.json` and synchronizes the state to the target agent (e.g., writing to `~/.config/claude/config.json`).
