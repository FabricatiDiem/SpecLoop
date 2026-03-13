# Feature Specification: Agent-Agnostic Skills Framework

**Feature Branch**: `001-agent-agnostic-skills`  
**Created**: 2026-03-13  
**Status**: Draft  
**Input**: User description: "Skills being developed should be agent agnostic. That is, they should be developed and deployable in a way that works for Gemini CLI, Claude Code, OpenCode, etc."

## Clarifications

### Session 2026-03-13

- Q: What is the primary format for defining these skills? → A: Model Context Protocol (MCP) for executable tools; Markdown for natural language procedures (skills).
- Q: What is the preferred metadata standard for these Markdown skills? → A: OpenCode Standard Frontmatter.
- Q: How should the framework facilitate discovery across different agents? → A: Unified Manifest File (`skills.json`).
- Q: How should "subagents" be defined in this framework? → A: Markdown + YAML Frontmatter (Extension of Skills).
- Q: How should python and shell scripts be integrated into the agent-agnostic framework? → A: Exposed via MCP tool endpoints.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Create an Agent-Agnostic Skill (Priority: P1)

As a skill developer, I want to create a skill once so that I can use it across multiple AI agents (Gemini CLI, Claude Code, OpenCode) without rewriting the core logic or instructions.

**Why this priority**: This is the core requirement of the feature.
**Independent Test**: Create a simple skill (e.g., "hello-world" procedure or tool) and verify it can be loaded and executed by at least two different agents.

**Acceptance Scenarios**:

1. **Given** a new skill (Markdown or MCP), **When** deployed to Gemini CLI, **Then** the agent can discover and execute its capabilities correctly via the unified manifest.
2. **Given** the same skill, **When** deployed to Claude Code, **Then** the agent can discover and execute its capabilities correctly via the unified manifest.

---

### User Story 2 - Deploy Skill to Multiple Environments (Priority: P2)

As a developer, I want a unified deployment process for my skills so that I can easily distribute them to different agentic workflows.

**Why this priority**: Enhances the usability of the agent-agnostic approach.
**Independent Test**: Use a single command/script to deploy a skill to a shared location and update the `skills.json` manifest.

**Acceptance Scenarios**:

1. **Given** a skill ready for deployment, **When** the deployment script is run, **Then** the skill artifacts are placed in the correct locations and `skills.json` is updated.

---

### User Story 3 - Define and Register a Subagent (Priority: P3)

As an agent architect, I want to define a subagent with specific instructions and required tools so that I can deploy it to any supported harness (Gemini, Claude, OpenCode).

**Why this priority**: Fosters complex agentic workflows and modularizes high-level agent logic.
**Independent Test**: Create a subagent definition in Markdown, list its tool dependencies, and verify it appears in the manifest and can be "installed" to a target harness.

**Acceptance Scenarios**:

1. **Given** a subagent Markdown file, **When** discovery is run, **Then** the subagent is registered in `skills.json` with its tool dependencies mapped.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST define a standard schema for skills that is compatible with major AI agents.
- **FR-002**: Skills MUST be decoupled from agent-specific SDKs or APIs.
- **FR-003**: System MUST provide an abstraction layer for common agent actions (e.g., file read/write, shell execution).
- **FR-004**: System MUST maintain a unified manifest file (`skills.json`) for skill, tool, and subagent discovery.
- **FR-005**: Executable tools MUST be implemented as MCP servers to ensure cross-agent compatibility.
- **FR-006**: Natural language procedures (skills) MUST be defined in Markdown with OpenCode Standard Frontmatter (YAML).
- **FR-007**: The framework MUST provide a mechanism to translate or map these definitions to agent-specific formats (e.g., Claude's `.claudecode` configs or Gemini's tool definitions) using the `skills.json` manifest as the source of truth.
- **FR-008**: Subagents MUST be defined in Markdown with structured metadata identifying their system prompt, required tools (MCP), and required skills (Markdown).
- **FR-009**: The system MUST provide a principled location (e.g., `subagents/`) for storing and organizing these definitions.
- **FR-010**: Python and Shell scripts MUST be exposed as tools via an MCP-compliant runner to ensure agent-agnostic execution.
- **FR-011**: The manifest MUST include script metadata (interpreter, arguments, permissions) for mapping to MCP tool definitions.

### Key Entities

- **Skill (NL)**: A Markdown-based natural language procedure with structured metadata.
- **Tool (Executable)**: An MCP-compliant server providing deterministic capabilities.
- **Subagent**: A Markdown-based agent definition containing a system prompt and a dependency list of skills/tools.
- **Script**: A Python or Shell file that is dynamically exposed as a tool via an MCP server.
- **Manifest (`skills.json`)**: A central registry of all available skills, tools, and subagents, including metadata and execution paths.
- **Agent Integration**: The bridge between a generic skill/tool/subagent and an agent's specific tool/function call system.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: A single skill definition can be successfully used by 3+ different AI agents without modification.
- **SC-002**: Time to adapt an existing skill for a new agent is reduced by 80% compared to a custom implementation.
- **SC-003**: Skill discovery and execution overhead is less than 100ms per call across all supported agents.
- **SC-004**: Subagents can be successfully "installed" (mapped to harness config) on 3+ different AI agents.
