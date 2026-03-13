# Research: Agent-Agnostic Skills Framework

This document records the architectural research and decisions made for the framework to ensure cross-agent compatibility.

## Decision 1: Model Context Protocol (MCP) for Tools

- **Decision**: Adopt MCP as the primary protocol for all executable tools.
- **Rationale**: MCP (Model Context Protocol) is the industry standard for connecting LLMs to external tools and data sources. It is natively supported by Claude Code and has increasing community support. By implementing tools as MCP servers, we ensure they can be used by any MCP-compliant agent without modification.

## Decision 2: Markdown for Natural Language Procedures (Skills)

- **Decision**: Define high-level skills as Markdown files.
- **Rationale**: Agents like OpenCode and Gemini CLI are designed to follow natural language procedures. Markdown provides a human-readable and machine-parsable format. It allows for rich documentation, step-by-step instructions, and embedded examples.

## Decision 3: OpenCode Standard Frontmatter for Metadata

- **Decision**: Use YAML frontmatter in Markdown skills, following the OpenCode format.
- **Rationale**: OpenCode already has a defined schema for its skills (`description`, `handoffs`, `inputs`). By adopting this format, we ensure immediate compatibility with OpenCode while providing a structured way for other agents to parse skill metadata.

## Decision 4: Unified Manifest (`skills.json`) for Discovery

- **Decision**: A central `skills.json` file will act as the source of truth for all available skills and tools in the repository.
- **Rationale**: Discovery mechanisms vary significantly between agents. A unified manifest allows a single deployment tool to read the entire repository state and synchronize it to the correct agent-specific locations.

## Decision 5: Subagents as Composite Markdown Definitions

- **Decision**: Define subagents as Markdown files with YAML frontmatter listing their dependencies (tools, skills).
- **Rationale**: Subagents are essentially specialized configurations of an LLM (System Prompt + Tools). Using Markdown allows the system prompt to be primary, while the frontmatter provides the "harness-agnostic" configuration for tool installation.
- **Integration**: During deployment, the framework will map these dependencies to the specific tool-registration format of the target agent (e.g., adding to the `tools` array in a Claude config).

## Decision 6: MCP-Compliant Script Runner

- **Decision**: Implement a generic MCP server that dynamically exposes Python/Shell scripts as tools.
- **Rationale**: To keep scripts harness-agnostic, they shouldn't rely on the agent's native script execution logic (which varies). An MCP runner acts as an abstraction layer: the agent calls the MCP tool, the runner executes the script locally and returns the output. This ensures scripts work identically across Gemini, Claude, and OpenCode.
