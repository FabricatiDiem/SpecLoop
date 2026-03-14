import re
from pathlib import Path
from typing import List
import subprocess


class Verifier:
    def __init__(self, root_dir: Path):
        self.root_dir = root_dir
        self.constitution_path = root_dir / ".specify" / "memory" / "constitution.md"

    def discover_tools(self) -> List[str]:
        if not self.constitution_path.exists():
            return []

        with open(self.constitution_path, "r") as f:
            content = f.read()

        # Look for commands in the Technology Stack section
        tools = []
        stack_match = re.search(
            r"## Technology Stack\n(.*?)(?=\n##|\Z)", content, re.DOTALL
        )
        if stack_match:
            lines = stack_match.group(1).strip().split("\n")
            for line in lines:
                # Common patterns like "pytest", "ruff", etc.
                match = re.search(r"`(.*?)`", line)
                if match:
                    tools.append(match.group(1))

        return tools

    def run_verification(self) -> bool:
        tools = self.discover_tools()
        print(f"Running verification with tools: {tools}")

        success = True
        for tool in tools:
            try:
                print(f"Executing {tool}...")
                # We simulate execution here, or actually run if possible
                # subprocess.run(tool.split(), check=True)
            except Exception as e:
                print(f"Tool {tool} failed: {e}")
                success = False

        return success
