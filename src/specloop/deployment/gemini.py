from pathlib import Path
from specloop.deployment.base import BaseDeployment


class GeminiDeployment(BaseDeployment):
    def deploy(self) -> bool:
        """Sync to .gemini/tools/ for Gemini CLI."""
        gemini_dir = self.root_dir / ".gemini" / "tools"
        gemini_dir.mkdir(parents=True, exist_ok=True)

        config_path = gemini_dir / "skills.json"
        with open(config_path, "w") as f:
            f.write(self.manifest.model_dump_json(indent=2))

        self.log(f"Synced manifest to {config_path}")
        return True
