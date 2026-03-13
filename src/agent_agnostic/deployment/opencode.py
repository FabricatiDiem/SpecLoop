import shutil
from pathlib import Path
from agent_agnostic.deployment.base import BaseDeployment

class OpenCodeDeployment(BaseDeployment):
    def deploy(self) -> bool:
        """Sync to .opencode/command/ for OpenCode."""
        opencode_dir = self.root_dir / ".opencode" / "command"
        opencode_dir.mkdir(parents=True, exist_ok=True)
        
        # OpenCode expects each skill to be a separate .md file in this directory
        for skill in self.manifest.skills:
            src_path = self.root_dir / skill.path
            dest_path = opencode_dir / f"speckit.{skill.id}.md"
            shutil.copy2(src_path, dest_path)
            self.log(f"Copied skill {skill.id} to {dest_path}")
        
        # Subagents also synced as .md files
        for subagent in self.manifest.subagents:
            src_path = self.root_dir / subagent.path
            dest_path = opencode_dir / f"speckit.agent.{subagent.id}.md"
            shutil.copy2(src_path, dest_path)
            self.log(f"Copied subagent {subagent.id} to {dest_path}")
        
        return True
