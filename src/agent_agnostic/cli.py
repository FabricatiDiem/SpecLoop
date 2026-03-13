import click
from pathlib import Path
from agent_agnostic.discovery import generate_manifest, save_manifest
from agent_agnostic.models.validator import validate_manifest, get_manifest_from_file
from agent_agnostic.deployment.claude import ClaudeDeployment
from agent_agnostic.deployment.gemini import GeminiDeployment
from agent_agnostic.deployment.opencode import OpenCodeDeployment


@click.group()
def cli():
    """Agent-Agnostic Skills CLI"""
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
    """Initialize a new project with the skills framework structure."""
    root_path = Path(".").absolute()

    dirs = ["skills", "mcp_servers", "subagents", "scripts"]
    for d in dirs:
        (root_path / d).mkdir(exist_ok=True)
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
        # Search current and parent directories for the schema
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
def deploy(target, manifest):
    """Deploy skills and tools to a target harness."""
    root_path = Path(".").absolute()
    manifest_path = root_path / manifest

    if not manifest_path.exists():
        click.echo(f"Error: Manifest {manifest_path} not found. Run 'discover' first.")
        return

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
    else:
        click.echo(f"✗ Deployment to {target} failed.")


if __name__ == "__main__":
    cli()
