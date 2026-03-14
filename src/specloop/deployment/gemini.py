import shutil
import yaml
from pathlib import Path
from specloop.deployment.base import BaseDeployment


class GeminiDeployment(BaseDeployment):
    def deploy(self) -> bool:
        """Sync to .gemini/skills/ and .gemini/agents/ for Gemini CLI."""
        target_root = self.root_dir / ".gemini"

        skills_dir = target_root / "skills"
        agents_dir = target_root / "agents"

        skills_dir.mkdir(parents=True, exist_ok=True)
        agents_dir.mkdir(parents=True, exist_ok=True)

        skills_copied = 0
        agents_deployed = 0

        # Sync skills (Markdown procedures)
        for skill in self.manifest.skills:
            src_path = Path(skill.path)
            if not src_path.exists():
                self.log(f"Warning: Skill source not found: {src_path}")
                continue

            dest_path = skills_dir / f"{skill.id}.md"
            shutil.copy2(src_path, dest_path)
            skills_copied += 1
            self.log(
                f"Copied skill {skill.id} to {dest_path.relative_to(self.root_dir)}"
            )

        # Sync subagents
        for subagent in self.manifest.subagents:
            src_path = Path(subagent.path)
            if not src_path.exists():
                self.log(f"Warning: Subagent source not found: {src_path}")
                continue

            dest_path = agents_dir / f"{subagent.id}.md"

            # Ensure the frontmatter is compatible with Gemini
            try:
                with open(src_path, "r", encoding="utf-8") as f:
                    content = f.read()

                if content.startswith("---"):
                    parts = content.split("---", 2)
                    if len(parts) >= 2:
                        frontmatter = yaml.safe_load(parts[1]) or {}
                        # Standardize description for Gemini if missing
                        if "description" not in frontmatter:
                            frontmatter["description"] = (
                                f"SpecLoop Subagent: {subagent.name}"
                            )

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

        # Also keep skills.json for compatibility/tracking
        config_path = target_root / "skills.json"
        with open(config_path, "w") as f:
            f.write(self.manifest.model_dump_json(indent=2))

        self.log(
            f"Gemini Deployment Summary: {skills_copied} skills, {agents_deployed} agents."
        )
        return True
