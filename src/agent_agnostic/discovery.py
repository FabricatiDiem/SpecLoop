import json
import yaml
import os
from pathlib import Path
from typing import List, Dict
from agent_agnostic.models.manifest import Manifest, Skill, Tool, Subagent, Script, SubagentDependencies

def extract_frontmatter(file_path: Path) -> Dict:
    """Extract YAML frontmatter from a Markdown file."""
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        if content.startswith('---'):
            _, frontmatter, _ = content.split('---', 2)
            return yaml.safe_load(frontmatter)
    except (ValueError, yaml.YAMLError) as e:
        print(f"Error parsing frontmatter in {file_path}: {e}")
    return {}

def discover_skills(root_dir: Path) -> List[Skill]:
    """Scan the skills/ directory for Markdown procedures."""
    skills = []
    skills_dir = root_dir / "skills"
    if not skills_dir.exists():
        return skills
    
    for file in skills_dir.glob("*.md"):
        metadata = extract_frontmatter(file)
        skills.append(Skill(
            id=file.stem,
            name=metadata.get("name", file.stem.replace("-", " ").title()),
            path=str(file.relative_to(root_dir)),
            metadata=metadata
        ))
    return skills

def discover_tools(root_dir: Path) -> List[Tool]:
    """Scan the mcp_servers/ directory for executable tools."""
    tools = []
    mcp_dir = root_dir / "mcp_servers"
    if not mcp_dir.exists():
        return tools
    
    # In this phase, we look for server.py in subdirectories
    for server_file in mcp_dir.glob("**/server.py"):
        server_dir = server_file.parent
        tools.append(Tool(
            id=server_dir.name,
            name=server_dir.name.replace("_", " ").title(),
            command=f"python {server_file.relative_to(root_dir)}"
        ))
    return tools

def discover_subagents(root_dir: Path) -> List[Subagent]:
    """Scan the subagents/ directory for Markdown-based subagents."""
    subagents = []
    sub_dir = root_dir / "subagents"
    if not sub_dir.exists():
        return subagents
    
    for file in sub_dir.glob("*.md"):
        content = ""
        with open(file, 'r') as f:
            content = f.read()
        
        metadata = extract_frontmatter(file)
        system_prompt = content
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) == 3:
                system_prompt = parts[2].strip()
        
        deps_data = metadata.get("dependencies", {})
        deps = SubagentDependencies(
            skills=deps_data.get("skills", []),
            tools=deps_data.get("tools", []),
            scripts=deps_data.get("scripts", [])
        )
        
        subagents.append(Subagent(
            id=file.stem,
            name=metadata.get("name", file.stem.replace("-", " ").title()),
            path=str(file.relative_to(root_dir)),
            system_prompt=system_prompt,
            dependencies=deps
        ))
    return subagents

def discover_scripts(root_dir: Path) -> List[Script]:
    """Scan the scripts/ directory for Python and Shell scripts."""
    scripts = []
    scripts_dir = root_dir / "scripts"
    if not scripts_dir.exists():
        return scripts
    
    for file in scripts_dir.glob("*"):
        if file.suffix in [".py", ".sh"]:
            interpreter = "python" if file.suffix == ".py" else "bash"
            scripts.append(Script(
                id=file.stem,
                name=file.stem.replace("_", " ").title(),
                interpreter=interpreter,
                path=str(file.relative_to(root_dir))
            ))
    return scripts

def generate_manifest(root_dir: Path, version: str = "1.0.0") -> Manifest:
    """Scan all directories and build a complete Manifest."""
    return Manifest(
        version=version,
        repository=str(root_dir.name),
        skills=discover_skills(root_dir),
        tools=discover_tools(root_dir),
        subagents=discover_subagents(root_dir),
        scripts=discover_scripts(root_dir)
    )

def save_manifest(manifest: Manifest, file_path: Path):
    """Save the manifest to a JSON file."""
    with open(file_path, 'w') as f:
        f.write(manifest.model_dump_json(indent=2))
