import click
import json
from pathlib import Path
import os
from speckit_loop.engine.loop import LoopRunner
from speckit_loop.parsers.epic_parser import EpicParser, EpicStatus
from speckit_loop.parsers.goal_parser import GoalParser


@click.group()
def cli():
    """SpecKit Automation Loop CLI"""
    pass


@cli.command()
@click.option("--file", default="EPICS.md", help="Path to EPICS.md file")
@click.option("--goals", default="GOALS.md", help="Path to GOALS.md file")
def run(file, goals):
    """Run the autonomous developer loop (Python-driven)."""
    root_dir = Path(os.getcwd())
    epics_path = root_dir / file
    goals_path = root_dir / goals

    click.echo(f"Starting SpecKit Loop with {file}")

    runner = LoopRunner(root_dir, epics_path, goals_path)
    runner.run()


@cli.command()
@click.option("--file", default="EPICS.md", help="Path to EPICS.md file")
@click.option("--goals", default="GOALS.md", help="Path to GOALS.md file")
def next(file, goals):
    """Get the next pending epic and project context as JSON."""
    root_dir = Path(os.getcwd())
    epics_path = root_dir / file
    goals_path = root_dir / goals

    epics = EpicParser.parse_file(epics_path)
    goal = GoalParser.parse_file(goals_path)

    pending = [e for e in epics if e.status == EpicStatus.PENDING]

    if not pending:
        click.echo(
            json.dumps({"status": "complete", "message": "No pending epics found."})
        )
        return

    current = pending[0]
    output = {
        "status": "todo",
        "epic": {
            "title": current.title,
            "description": current.description,
            "priority": current.priority,
        },
        "context": {"mission": goal.mission, "constraints": goal.constraints},
    }
    click.echo(json.dumps(output, indent=2))


@cli.command()
@click.argument("title")
@click.option("--file", default="EPICS.md", help="Path to EPICS.md file")
@click.option(
    "--status",
    default="Completed",
    type=click.Choice(["Completed", "Failed", "In Progress", "Pending"]),
)
def update(title, file, status):
    """Update the status of an epic in EPICS.md."""
    root_dir = Path(os.getcwd())
    epics_path = root_dir / file

    # Map string back to EpicStatus
    status_map = {
        "Completed": EpicStatus.COMPLETED,
        "Failed": EpicStatus.FAILED,
        "In Progress": EpicStatus.IN_PROGRESS,
        "Pending": EpicStatus.PENDING,
    }

    EpicParser.update_status(epics_path, title, status_map[status])
    click.echo(f"Updated epic '{title}' to {status}")


if __name__ == "__main__":
    cli()
