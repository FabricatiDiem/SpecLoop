import subprocess
from pathlib import Path
from typing import Optional


class Orchestrator:
    def __init__(self, root_dir: Path):
        self.root_dir = root_dir

    def run_command(
        self, cmd: str, args: str = "", pre_prompt: Optional[str] = None
    ) -> bool:
        """
        Emits a recognizable instruction for an AI agent to intercept.
        """
        print(f"\n[Orchestrator] Requesting SpecKit Action: {cmd}")
        if pre_prompt:
            print(f"[Orchestrator] Context: {pre_prompt}")

        # Emit the instruction marker
        print(f"AGENT_INSTRUCTION: /{cmd} {args}")

        # In this mode, we don't write files. We expect the Agent to perform the logic.
        return True
