import json
import yaml
import os
from pathlib import Path
from typing import List, Dict, Optional
from specloop.models.manifest import (
    Manifest,
    Skill,
    Tool,
    Subagent,
    Script,
    SubagentDependencies,
)


def extract_frontmatter(file_path: Path) -> Dict:
    """Extract YAML frontmatter from a Markdown file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 2:
                return yaml.safe_load(parts[1]) or {}
    except (ValueError, yaml.YAMLError) as e:
        print(f"Error parsing frontmatter in {file_path}: {e}")
    return {}


def discover_skills(root_dir: Path, subdir: str = "skills") -> List[Skill]:
    """Scan a directory for Markdown procedures."""
    skills = []
    skills_dir = root_dir / subdir
    if not skills_dir.exists():
        return skills

    for file in skills_dir.glob("*.md"):
        metadata = extract_frontmatter(file)
        skills.append(
            Skill(
                id=file.stem,
                name=metadata.get(
                    "name", file.stem.replace("-", " ").replace("_", " ").title()
                ),
                path=str(file.absolute()),
                metadata=metadata,
            )
        )
    return skills


def discover_tools(root_dir: Path, subdir: str = "mcp_servers") -> List[Tool]:
    """Scan a directory for executable tools."""
    tools = []
    mcp_dir = root_dir / subdir
    if not mcp_dir.exists():
        return tools

    for server_file in mcp_dir.glob("**/server.py"):
        server_dir = server_file.parent
        tools.append(
            Tool(
                id=server_dir.name,
                name=server_dir.name.replace("_", " ").title(),
                command=f"python {server_file.absolute()}",
            )
        )
    return tools


def discover_subagents(root_dir: Path, subdir: str = "subagents") -> List[Subagent]:
    """Scan a directory for Markdown-based subagents."""
    subagents = []
    sub_dir = root_dir / subdir
    if not sub_dir.exists():
        return subagents

    for file in sub_dir.glob("*.md"):
        try:
            with open(file, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading {file}: {e}")
            continue

        metadata = extract_frontmatter(file)
        system_prompt = content
        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) == 3:
                system_prompt = parts[2].strip()

        deps_data = metadata.get("dependencies", {})
        deps = SubagentDependencies(
            skills=deps_data.get("skills", []),
            tools=deps_data.get("tools", []),
            scripts=deps_data.get("scripts", []),
        )

        subagents.append(
            Subagent(
                id=file.stem,
                name=metadata.get(
                    "name", file.stem.replace("-", " ").replace("_", " ").title()
                ),
                path=str(file.absolute()),
                system_prompt=system_prompt,
                dependencies=deps,
            )
        )
    return subagents


def discover_scripts(root_dir: Path, subdir: str = "scripts") -> List[Script]:
    """Scan a directory for Python and Shell scripts."""
    scripts = []
    scripts_dir = root_dir / subdir
    if not scripts_dir.exists():
        return scripts

    for file in scripts_dir.glob("*"):
        if file.suffix in [".py", ".sh"]:
            interpreter = "python" if file.suffix == ".py" else "bash"
            scripts.append(
                Script(
                    id=file.stem,
                    name=file.stem.replace("_", " ").title(),
                    interpreter=interpreter,
                    path=str(file.absolute()),
                )
            )
    return scripts


def get_resource_dir() -> Optional[Path]:
    """Get the internal resources directory of the package."""
    try:
        return Path(__file__).parent / "resources"
    except NameError:
        return None


def generate_manifest(root_dir: Path, version: str = "1.0.0") -> Manifest:
    """Build a complete Manifest by merging built-in resources and local project files."""

    # 1. Discover from local project (User Defined)
    skills = discover_skills(root_dir)
    tools = discover_tools(root_dir)
    subagents = discover_subagents(root_dir)
    scripts = discover_scripts(root_dir)

    # 2. Discover from built-in resources
    res_dir = get_resource_dir()
    if res_dir and res_dir.exists():
        # Merge, but avoid duplicates (local overrides built-in if IDs match)
        existing_skill_ids = {s.id for s in skills}
        for s in discover_skills(res_dir):
            if s.id not in existing_skill_ids:
                skills.append(s)

        existing_tool_ids = {t.id for t in tools}
        for t in discover_tools(res_dir):
            if t.id not in existing_tool_ids:
                tools.append(t)

        existing_subagent_ids = {a.id for a in subagents}
        for a in discover_subagents(res_dir):
            if a.id not in existing_subagent_ids:
                subagents.append(a)

        existing_script_ids = {sc.id for sc in scripts}
        for sc in discover_scripts(res_dir):
            if sc.id not in existing_script_ids:
                scripts.append(sc)

    return Manifest(
        version=version,
        repository=str(root_dir.name),
        skills=skills,
        tools=tools,
        subagents=subagents,
        scripts=scripts,
    )


def save_manifest(manifest: Manifest, file_path: Path):
    """Save the manifest to a JSON file."""
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(manifest.model_dump_json(indent=2))
