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

        skills_copied = 0
        agents_deployed = 0

        # OpenCode expects each skill to be a separate .md file in the command directory
        for skill in self.manifest.skills:
            src_path = Path(skill.path)
            if not src_path.exists():
                self.log(f"Warning: Skill source not found: {src_path}")
                continue

            dest_path = command_dir / f"speckit.{skill.id}.md"
            shutil.copy2(src_path, dest_path)
            skills_copied += 1
            self.log(
                f"Copied skill {skill.id} to {dest_path.relative_to(self.root_dir)}"
            )

        # Subagents must be synced to .opencode/agents/ as .md files
        for subagent in self.manifest.subagents:
            src_path = Path(subagent.path)
            if not src_path.exists():
                self.log(f"Warning: Subagent source not found: {src_path}")
                continue

            dest_path = agents_dir / f"{subagent.id}.md"

            # Ensure the frontmatter is correctly formatted for OpenCode
            try:
                with open(src_path, "r", encoding="utf-8") as f:
                    content = f.read()

                if "mode: subagent" not in content:
                    if content.startswith("---"):
                        parts = content.split("---", 2)
                        if len(parts) >= 2:
                            frontmatter = yaml.safe_load(parts[1]) or {}
                            frontmatter["mode"] = "subagent"
                            new_frontmatter = yaml.dump(frontmatter)
                            content = f"---\n{new_frontmatter}---{parts[2]}"

                with open(dest_path, "w", encoding="utf-8") as f:
                    f.write(content)

                agents_deployed += 1
                self.log(
                    f"Deployed subagent {subagent.id} to {dest_path.relative_to(self.root_dir)}"
                )
            except Exception as e:
                self.log(f"Error deploying subagent {subagent.id}: {e}")

        self.log(
            f"OpenCode Deployment Summary: {skills_copied} skills, {agents_deployed} agents."
        )
        return True
