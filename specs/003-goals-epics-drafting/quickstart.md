# Quickstart: Drafting Your Project Roadmap

This guide explains how to use the new drafting skills to scaffold a project.

## 1. Draft Project Goals

Trigger the goals skill:
```text
/project.goals "I want to build a secure file sharing app"
```
The agent will:
1. Propose a mission statement.
2. List potential constraints.
3. Write `GOALS.md` after your approval.

## 2. Draft Project Epics

Trigger the epics skill:
```text
/project.epics
```
The agent will:
1. Read `constitution.md` and `GOALS.md`.
2. Propose a list of high-level features (Epics).
3. Ensure they are formatted for the `speckit-loop`.
4. Write `EPICS.md` after your approval.

## 3. Verify Alignment

Once drafted, you can verify the format:
```bash
uv run skills discover
uv run skills verify
```
Your project is now ready for the autonomous implementation loop (`speckit-loop run`).
