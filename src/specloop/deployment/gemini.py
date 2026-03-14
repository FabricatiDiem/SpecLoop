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
        # Gemini expects: .gemini/skills/{skill_id}/SKILL.md
        for skill in self.manifest.skills:
            src_path = Path(skill.path)
            if not src_path.exists():
                self.log(f"Warning: Skill source not found: {src_path}")
                continue

            # Ensure valid slug for directory name
            skill_id_slug = skill.id.replace("_", "-")
            skill_container = skills_dir / skill_id_slug
            skill_container.mkdir(exist_ok=True)
            dest_path = skill_container / "SKILL.md"

            # Ensure the frontmatter is compatible with Gemini
            try:
                with open(src_path, "r", encoding="utf-8") as f:
                    content = f.read()

                if content.startswith("---"):
                    parts = content.split("---", 2)
                    if len(parts) >= 2:
                        frontmatter = yaml.safe_load(parts[1]) or {}

                        # Gemini mandatory fields for skills
                        gemini_skill_frontmatter = {
                            "name": skill_id_slug,  # Use the slugified ID as name
                            "description": frontmatter.get("description", skill.name),
                        }

                        # Preserve other common fields if they exist
                        for key in ["inputs", "handoffs", "tools"]:
                            if key in frontmatter:
                                gemini_skill_frontmatter[key] = frontmatter[key]

                        new_frontmatter = yaml.dump(gemini_skill_frontmatter)
                        content = f"---\n{new_frontmatter}---{parts[2]}"

                with open(dest_path, "w", encoding="utf-8") as f:
                    f.write(content)

                skills_copied += 1
                self.log(
                    f"Copied skill {skill.id} to {dest_path.relative_to(self.root_dir)}"
                )
            except Exception as e:
                self.log(f"Error deploying skill {skill.id}: {e}")

        # Sync subagents
        # Gemini expects: .gemini/agents/{agent_id}.md with name/description in frontmatter
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

                        # Gemini mandatory fields and strict schema
                        # We create a new dict to ensure no unrecognized keys are passed
                        gemini_frontmatter = {
                            "name": subagent.id.replace("_", "-"),  # Ensure valid slug
                            "description": frontmatter.get(
                                "description", f"SpecLoop Subagent: {subagent.name}"
                            ),
                            "kind": frontmatter.get("kind", "local"),
                        }

                        # Gemini tools list (must be array of strings)
                        # We use ['*'] by default to ensure access to all tools
                        tools = frontmatter.get("tools", ["*"])
                        if isinstance(tools, dict):
                            # If it was an object (OpenCode style), convert to list
                            tools = ["*"]
                        elif not isinstance(tools, list):
                            tools = [str(tools)]

                        gemini_frontmatter["tools"] = tools

                        # Optional Gemini fields
                        for key in [
                            "model",
                            "temperature",
                            "max_turns",
                            "timeout_mins",
                        ]:
                            if key in frontmatter:
                                gemini_frontmatter[key] = frontmatter[key]

                        new_frontmatter = yaml.dump(gemini_frontmatter)
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
