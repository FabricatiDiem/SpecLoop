# Data Model: Project Metadata

This document defines the structured contents of the project's high-level metadata files.

## 1. GOALS.md Entity

| Section | Description |
| :--- | :--- |
| `Project Mission` | A high-level statement of the project's purpose and primary goal. |
| `Constraints` | A list of non-functional requirements or technological boundaries. |

## 2. EPICS.md Entity

An ordered list of high-level feature sets.

| Field | Description |
| :--- | :--- |
| `Title` | The name of the feature, enclosed in brackets (e.g., `## [Add User Auth]`). |
| `Description` | A detailed summary of what the feature achieves. |
| `Priority` | A sequential integer starting from 1. |
| `Status` | A checkbox-based status (`Pending`, `In Progress`, `Completed`, `Failed`). |

## 3. Relationships

- `constitution.md` -> defines the **Principles** that constrain the `GOALS.md`.
- `GOALS.md` -> defines the **Mission** that informs the selection of `EPICS.md`.
- `EPICS.md` -> defines the **Roadmap** that is implemented by the `speckit-loop`.
