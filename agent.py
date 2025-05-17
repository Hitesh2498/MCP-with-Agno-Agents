import asyncio
import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.mcp import MCPTools
from mcp import StdioServerParameters

load_dotenv()

async def run_agent():
    server_params = StdioServerParameters(
        command="python",
        args=["./server.py"],
    )

    async with MCPTools(server_params=server_params) as mcp_tools:
        agent = Agent(
            model=OpenAIChat(id="gpt-4o-mini"),
            tools=[mcp_tools],
            markdown=True,
            show_tool_calls=True,
            debug_mode=True,
        )

        await agent.aprint_response("what's (3 + 5) x 12? and 5/9 and 6-9 and addition of all 3 outputs", stream=True)

if __name__ == "__main__":
    asyncio.run(run_agent())