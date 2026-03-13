import shutil
import yaml
from pathlib import Path
from agent_agnostic.deployment.base import BaseDeployment

class OpenCodeDeployment(BaseDeployment):
    def deploy(self) -> bool:
        """Sync to .opencode/command/ and .opencode/agents/ for OpenCode."""
        command_dir = self.root_dir / ".opencode" / "command"
        agents_dir = self.root_dir / ".opencode" / "agents"
        
        command_dir.mkdir(parents=True, exist_ok=True)
        agents_dir.mkdir(parents=True, exist_ok=True)
        
        # OpenCode expects each skill to be a separate .md file in the command directory
        for skill in self.manifest.skills:
            src_path = self.root_dir / skill.path
            dest_path = command_dir / f"speckit.{skill.id}.md"
            shutil.copy2(src_path, dest_path)
            self.log(f"Copied skill {skill.id} to {dest_path}")
        
        # Subagents must be synced to .opencode/agents/ as .md files
        for subagent in self.manifest.subagents:
            src_path = self.root_dir / subagent.path
            dest_path = agents_dir / f"{subagent.id}.md"
            
            # Ensure the frontmatter is correctly formatted for OpenCode
            # OpenCode uses 'mode: subagent'
            with open(src_path, 'r') as f:
                content = f.read()
            
            if 'mode: subagent' not in content:
                if content.startswith('---'):
                    parts = content.split('---', 2)
                    frontmatter = yaml.safe_load(parts[1])
                    frontmatter['mode'] = 'subagent'
                    new_frontmatter = yaml.dump(frontmatter)
                    content = f"---\n{new_frontmatter}---{parts[2]}"
            
            with open(dest_path, 'w') as f:
                f.write(content)
                
            self.log(f"Deployed subagent {subagent.id} to {dest_path}")
        
        return True
