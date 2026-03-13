<!--
Sync Impact Report:
- Version change: N/A → 1.0.0 (Initial Ratification)
- List of modified principles:
    - [PRINCIPLE_1_NAME] → I. Reusable Agentic Enablement
    - [PRINCIPLE_2_NAME] → II. GitHub SpecKit Backbone
    - [PRINCIPLE_3_NAME] → III. Modular Polyglot Architecture
    - [PRINCIPLE_4_NAME] → IV. Automated Enablement
    - [PRINCIPLE_5_NAME] → V. Semantic Versioning & Governance
- Added sections: Technology Stack, Quality Assurance
- Removed sections: None
- Templates requiring updates:
    - ✅ .specify/templates/plan-template.md (Aligned with Constitution Check gate)
    - ✅ .specify/templates/spec-template.md (Aligned with SpecKit workflow)
    - ✅ .specify/templates/tasks-template.md (Aligned with task categorization)
    - ✅ .opencode/command/speckit.constitution.md (Generic guidance verified)
- Follow-up TODOs: None
-->

# newSkills Constitution

## Core Principles

### I. Reusable Agentic Enablement
Every artifact (skill, prompt, MCP server) MUST be designed as a reusable template for other projects. Documentation MUST include clear usage instructions, integration patterns, and example workflows. Rationale: The core purpose is to serve as a backbone for future agentic workflows across diverse coding environments.

### II. GitHub SpecKit Backbone
All coding tasks MUST adhere to the GitHub SpecKit workflow (Analyze → Specify → Plan → Implement). Non-coding tasks, such as pure markdown skill creation, SHOULD still follow a structured documentation lifecycle to ensure consistency, traceability, and high quality across all project outputs.

### III. Modular Polyglot Architecture
The repository MUST support a mix of Markdown (skills/prompts), Python (MCP servers/processing), and Shell scripts (action enablement). Each component MUST be modular, independently testable where applicable, and maintainable within its domain while adhering to global integration standards.

### IV. Automated Enablement
Python and Shell scripts SHOULD be used to automate repetitive tasks, data processing, and environment setup. All automation tools MUST be documented, easily executable, and follow standard error handling practices to enhance developer efficiency and ensure repeatable processes.

### V. Semantic Versioning & Governance
The project MUST use semantic versioning (MAJOR.MINOR.PATCH) for the constitution and all major enablement modules. Any breaking changes in governance, core principles, or integration contracts MUST trigger a major version bump to provide a predictable framework for evolution.

## Technology Stack

- **Workflow**: GitHub SpecKit (Primary workflow for all development cycles)
- **Languages**: Python 3.11+ (MCP servers, processing), Bash/Shell (action enablement)
- **Formats**: Markdown (skills, prompts, docs), YAML/JSON (configuration and data)

## Quality Assurance

- All code changes MUST undergo self-verification via logs, debug statements, or unit tests.
- Core principles MUST be checked at the start of every implementation plan (Constitution Check).
- Any deviation from the constitution MUST be documented in the Complexity Tracking section of the plan and explicitly justified.

## Governance

- This constitution is the supreme governing document for the repository and supersedes all other informal practices.
- Amendments require a clear Sync Impact Report and must be propagated across all dependent templates and command files.
- All Pull Requests and reviews MUST verify compliance with these core principles before merging.
- Project evolution must prioritize simplicity and modularity to remain effective as a template repository.

**Version**: 1.0.0 | **Ratified**: 2026-03-13 | **Last Amended**: 2026-03-13
