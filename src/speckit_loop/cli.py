import click
from pathlib import Path
import os
from speckit_loop.engine.loop import LoopRunner


@click.group()
def cli():
    """SpecKit Automation Loop CLI"""
    pass


@cli.command()
@click.option("--file", default="EPICS.md", help="Path to EPICS.md file")
@click.option("--goals", default="GOALS.md", help="Path to GOALS.md file")
def run(file, goals):
    """Run the autonomous developer loop."""
    root_dir = Path(os.getcwd())
    epics_path = root_dir / file
    goals_path = root_dir / goals

    click.echo(f"Starting SpecKit Loop with {file}")

    runner = LoopRunner(root_dir, epics_path, goals_path)
    runner.run()


if __name__ == "__main__":
    cli()
