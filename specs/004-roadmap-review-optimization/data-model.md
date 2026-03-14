# Data Model: Roadmap Review and Optimization

This document defines the logical entities used by the roadmap analysis skills.

## 1. Requirement Node (Internal)

Derived from `GOALS.md` and `constitution.md`.

| Field | Description |
| :--- | :--- |
| `Source` | File path and line number or section header. |
| `Intent` | The core requirement or goal stated in the text. |
| `Type` | `Mission Goal` or `Core Principle`. |

## 2. Gap Entity

| Field | Description |
| :--- | :--- |
| `Requirement` | The missing goal or principle. |
| `Rationale` | Why this is considered a gap (e.g., "Goal X requires capability Y, but no epic provides Y"). |
| `Recommendation` | Suggested title and description for a new epic to fill the gap. |

## 3. Alignment Issue Entity

| Field | Description |
| :--- | :--- |
| `Target Epic` | The epic being flagged. |
| `Conflict` | The specific contradiction found (e.g., "Epic violates Principle II: Self-verification"). |
| `Severity` | `Blocker`, `Warning`, or `Suggestion`. |

## 4. Dependency Node

| Field | Description |
| :--- | :--- |
| `Epic Title` | The subject of the node. |
| `Prerequisites` | List of other epic titles that MUST be completed first. |
| `Foundational Value` | Qualitative score (1-5) representing how many other epics depend on this one. Used for tie-breaking priorities. |
| `Priority` | Original priority value from `EPICS.md`. |
| `Calculated Priority`| The new priority value assigned after optimization. |
