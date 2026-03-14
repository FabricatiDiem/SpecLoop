import json
from pathlib import Path
from specloop.deployment.base import BaseDeployment


class ClaudeDeployment(BaseDeployment):
    def deploy(self) -> bool:
        """Sync to .claudecode/ for Claude Code."""
        claude_dir = self.root_dir / ".claudecode"
        claude_dir.mkdir(exist_ok=True)

        # In a real scenario, this would update a config file
        # For now, we sync the manifest to the config directory
        config_path = claude_dir / "skills.json"
        with open(config_path, "w") as f:
            f.write(self.manifest.model_dump_json(indent=2))

        self.log(f"Synced manifest to {config_path}")
        return True
