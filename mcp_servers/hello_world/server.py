from mcp.server import Server
from mcp.types import Tool, TextContent

server = Server("hello-world")

@server.list_tools()
async def list_tools():
    return [
        Tool(
            name="hello",
            description="Say hello",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {"type": "string"}
                },
                "required": ["name"]
            }
        )
    ]

@server.call_tool("hello")
async def call_hello(name: str, arguments: dict):
    return [TextContent(type="text", text=f"Hello, {arguments.get('name')}!")]

if __name__ == "__main__":
    from mcp.server.stdio import stdio_server
    import asyncio
    asyncio.run(stdio_server(server))
