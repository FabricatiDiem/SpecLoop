import asyncio
import subprocess
import json
from pathlib import Path
from mcp.server import Server
from mcp.types import Tool, TextContent
from agent_agnostic.models.validator import get_manifest_from_file

def create_script_runner(manifest_path: Path, root_dir: Path):
    server = Server("script-runner")
    manifest = get_manifest_from_file(str(manifest_path))

    @server.list_tools()
    async def list_tools():
        tools = []
        for script in manifest.scripts:
            tools.append(Tool(
                name=script.id,
                description=f"Run script: {script.name}",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "args": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Arguments to pass to the script"
                        }
                    }
                }
            ))
        return tools

    @server.call_tool()
    async def call_tool(name: str, arguments: dict):
        script = next((s for s in manifest.scripts if s.id == name), None)
        if not script:
            return [TextContent(type="text", text=f"Script {name} not found.")]

        script_path = root_dir / script.path
        cmd = [script.interpreter, str(script_path)]
        if "args" in arguments:
            cmd.extend(arguments["args"])

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            return [TextContent(type="text", text=result.stdout)]
        except subprocess.CalledProcessError as e:
            return [TextContent(type="text", text=f"Error running script: {e.stderr}")]

    return server

if __name__ == "__main__":
    from mcp.server.stdio import stdio_server
    import os
    
    root = Path(os.getcwd())
    manifest_p = root / "skills.json"
    
    if manifest_p.exists():
        srv = create_script_runner(manifest_p, root)
        asyncio.run(stdio_server(srv))
    else:
        print("skills.json not found.")
