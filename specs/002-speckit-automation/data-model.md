# Data Model: SpecKit Automation Loop

## Epic Structure

Represented internally as a Pydantic model for parsing `EPICS.md`.

| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | `str` | Derived from title (kebab-case). |
| `title` | `str` | Human-readable name. |
| `description` | `str` | The high-level requirement passed to `/specify`. |
| `priority` | `int` | Execution order (1 being highest). |
| `status` | `enum` | `pending`, `in_progress`, `completed`, `failed`. |
| `branch` | `str` | The git branch created for this epic. |

## Global Goal

Represented internally as a project context object.

| Field | Type | Description |
| :--- | :--- | :--- |
| `mission` | `str` | High-level project mission from `GOALS.md`. |
| `constraints`| `List[str]`| List of project-wide non-functional requirements. |

## Workflow Phases

The automation engine tracks state through these phases:

1. `SPECIFY`: Creates `spec.md`.
2. `PLAN`: Creates `plan.md` and `research.md`.
3. `TASKS`: Creates `tasks.md`.
4. `ANALYZE`: Consistency check across all docs.
5. `IMPLEMENT`: Iterative code generation based on `tasks.md`.
6. `VERify`: Runs tests and linters from `constitution.md`.
7. `COMMIT`: Logical git commits.
8. `UPDATE`: Mark epic as done in `EPICS.md`.
