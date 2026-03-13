from typing import List, Optional, Dict
from pydantic import BaseModel, Field

class Skill(BaseModel):
    id: str
    name: str
    path: str
    metadata: Optional[Dict] = None
    tags: List[str] = []

class Tool(BaseModel):
    id: str
    name: str
    type: str = "mcp"
    command: str
    env: Dict[str, str] = {}
    capabilities: List[str] = []

class Script(BaseModel):
    id: str
    name: str
    interpreter: str
    path: str
    args: List[str] = []

class SubagentDependencies(BaseModel):
    skills: List[str] = []
    tools: List[str] = []
    scripts: List[str] = []

class Subagent(BaseModel):
    id: str
    name: str
    path: str
    system_prompt: str
    dependencies: SubagentDependencies = Field(default_factory=SubagentDependencies)

class Manifest(BaseModel):
    version: str = "1.0.0"
    repository: Optional[str] = None
    skills: List[Skill] = []
    tools: List[Tool] = []
    subagents: List[Subagent] = []
    scripts: List[Script] = []
