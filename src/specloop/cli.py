import click
import json
from pathlib import Path
import os
from specloop.discovery import generate_manifest, save_manifest
from specloop.models.validator import validate_manifest, get_manifest_from_file
from specloop.deployment.claude import ClaudeDeployment
from specloop.deployment.gemini import GeminiDeployment
from specloop.deployment.opencode import OpenCodeDeployment
from specloop.engine.loop import LoopRunner
from specloop.parsers.epic_parser import EpicParser, EpicStatus
from specloop.parsers.goal_parser import GoalParser


@click.group()
def cli():
    """SpecLoop: Agent-Agnostic Skills & Automation Framework (v0.1.1)"""
    pass


@cli.command()
@click.option("--root", default=".", help="Root directory to scan")
@click.option("--output", default="skills.json", help="Output manifest file")
@click.option("--version", default="1.0.0", help="Manifest version")
def discover(root, output, version):
    """Scan directories and generate a skills.json manifest."""
    root_path = Path(root).absolute()
    output_path = root_path / output

    click.echo(f"Scanning directory: {root_path}")
    manifest = generate_manifest(root_path, version)

    save_manifest(manifest, output_path)
    click.echo(f"Manifest saved to: {output_path}")


@cli.command()
def init():
    """Initialize a new project with the SpecLoop structure."""
    root_path = Path(".").absolute()

    dirs = [
        "skills",
        "mcp_servers",
        "subagents",
        "scripts",
        ".opencode/agents",
        ".opencode/command",
        ".claude/commands",
        ".claude/agents",
        ".gemini/skills",
        ".gemini/agents",
    ]
    for d in dirs:
        (root_path / d).mkdir(parents=True, exist_ok=True)
        click.echo(f"Created directory: {d}/")

    # Create EPICS.md if it doesn't exist
    epics_path = root_path / "EPICS.md"
    if not epics_path.exists():
        with open(epics_path, "w") as f:
            f.write(
                "# Project Epics\n\n## [Initial Epic]\nDescription: My first automated feature.\nPriority: 1\n- [ ] Status: Pending\n"
            )
        click.echo("Created EPICS.md")

    # Create GOALS.md if it doesn't exist
    goals_path = root_path / "GOALS.md"
    if not goals_path.exists():
        with open(goals_path, "w") as f:
            f.write(
                "# Project Mission\nSet your project mission here.\n\n# Constraints\n- Constraint 1\n"
            )
        click.echo("Created GOALS.md")


@cli.command()
@click.option("--manifest", default="skills.json", help="Path to manifest file")
@click.option("--schema", help="Path to schema file")
def verify(manifest, schema):
    """Verify a manifest file against a schema."""
    current_path = Path(".").absolute()
    manifest_path = current_path / manifest

    if not schema:
        # 1. Try bundled schema first
        bundled_schema = Path(__file__).parent / "schema" / "skills-schema.json"
        if bundled_schema.exists():
            schema_path = bundled_schema
        else:
            # 2. Fallback to searching current and parent directories
            search_dirs = [current_path] + list(current_path.parents)
            schema_path = None
            for d in search_dirs:
                possible_schemas = list(d.glob("specs/**/skills-schema.json"))
                if possible_schemas:
                    schema_path = possible_schemas[0]
                    break

        if not schema_path:
            click.echo(
                "Error: Could not find skills-schema.json automatically. Please provide --schema."
            )
            return
    else:
        schema_path = Path(schema).absolute()

    click.echo(f"Verifying {manifest_path} against {schema_path}...")
    if validate_manifest(str(manifest_path), str(schema_path)):
        click.echo("✓ Manifest is valid.")
    else:
        click.echo("✗ Manifest validation failed.")


@cli.command()
@click.option(
    "--target",
    required=True,
    type=click.Choice(["claude", "gemini", "opencode"]),
    help="Target harness to deploy to",
)
@click.option("--manifest", default="skills.json", help="Path to manifest file")
@click.option(
    "--autodiscover/--no-autodiscover",
    default=True,
    help="Automatically run discovery before deployment",
)
def deploy(target, manifest, autodiscover):
    """Deploy skills and tools to a target harness."""
    root_path = Path(".").absolute()
    manifest_path = root_path / manifest

    if autodiscover or not manifest_path.exists():
        click.echo("Running discovery...")
        manifest_obj = generate_manifest(root_path)
        save_manifest(manifest_obj, manifest_path)
    else:
        manifest_obj = get_manifest_from_file(str(manifest_path))

    deployer = None
    if target == "claude":
        deployer = ClaudeDeployment(manifest_obj, root_path)
    elif target == "gemini":
        deployer = GeminiDeployment(manifest_obj, root_path)
    elif target == "opencode":
        deployer = OpenCodeDeployment(manifest_obj, root_path)

    if deployer and deployer.deploy():
        click.echo(f"✓ Deployment to {target} successful.")
        click.echo(f"  - Skills: {len(manifest_obj.skills)}")
        click.echo(f"  - Subagents: {len(manifest_obj.subagents)}")
        click.echo(f"  - Tools: {len(manifest_obj.tools)}")
        click.echo(f"  - Scripts: {len(manifest_obj.scripts)}")
    else:
        click.echo(f"✗ Deployment to {target} failed.")


@cli.command()
@click.option("--file", default="EPICS.md", help="Path to EPICS.md file")
@click.option("--goals", default="GOALS.md", help="Path to GOALS.md file")
def run(file, goals):
    """Run the autonomous developer loop (Python-driven)."""
    root_dir = Path(os.getcwd())
    epics_path = root_dir / file
    goals_path = root_dir / goals

    click.echo(f"Starting SpecLoop with {file}")

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
