# MCP with Agno: Overview

Full Blog : <https://hiteshai.com/understanding-mcp-with-agno-agents-a-comprehensive/>

## What is MCP?

MCP (Multi-Component Protocol) is a framework used in the provided codebase to define and expose tools (functions) that can be called by an agent. In the example, `FastMCP` from `mcp.server.fastmcp` creates a server (`server.py`) that hosts mathematical operations like `add`, `multiply`, `divide`, and `subtract`. These tools are registered using the `@mcp.tool()` decorator and run via a transport mechanism (e.g., `stdio`).

## MCP in Agno

In the Agno framework, MCP integrates as a tool provider for the `Agent` class. The `agent.py` script demonstrates this:

- **MCPTools**: The `MCPTools` class wraps the MCP server, enabling the agent to communicate with the tools defined in `server.py`.
- **Agent Integration**: The `Agent` is initialized with an `OpenAIChat` model and `MCPTools`, allowing it to call MCP-hosted functions to process queries like `(3 + 5) x 12`.

## MCP vs. Agent Tools

- **MCP**:
  - Acts as a standalone server hosting multiple tools.
  - Uses a protocol (e.g., stdio) for communication, making it independent of the agent framework.
  - Ideal for modular, reusable toolsets that can be shared across agents or systems.
- **Agent Tools**:
  - Typically defined directly within the agent framework (e.g., as methods or functions passed to the agent).
  - Tightly coupled with the agent’s runtime environment.
  - Less modular, as they are specific to the agent instance.

## Why Use MCP with Agno?

- **Modularity**: MCP allows tools to be developed and maintained separately from the agent logic.
- **Scalability**: Tools can be hosted on different servers or processes, enabling distributed systems.
- **Reusability**: MCP tools can serve multiple agents or applications, reducing redundancy.

## Example

In the provided code:

- `server.py` defines math tools using `FastMCP`.
- `agent.py` uses `MCPTools` to connect the agent to these tools.
- The agent processes a query like `(3 + 5) x 12` by calling `add` and `multiply` via MCP.

This setup showcases MCP’s role as a bridge between Agno’s agent and external toolsets, enhancing flexibility and modularity.

## Usage

### Step 1: Set Up the Project Directory

- Clone repository : “<https://github.com/Hitesh2498/MCP-with-Agno-Agents.git>“

  ```bash
  git clone https://github.com/Hitesh2498/MCP-with-Agno-Agents.git
  ```

### Step 2: Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

- `python-dotenv`: For loading environment variables.
- `agno`: The Agno framework.
- `mcp`: The MCP protocol library.

### Step 3: Configure the Environment

Edit the `.env` file to include your OpenAI API key:

```text
OPENAI_API_KEY=your-openai-api-key-here
```

Replace `your-openai-api-key-here` with your actual key.

### Step 4: Run the Application

Run the `agent.py` script:

```bash
python agent.py
```

This will:

1. Start the MCP server (`server.py`) in the background.
2. Initialize the Agno agent.
3. Process the query: "what's (3 + 5) x 12? and 5/9 and 6-9 and addition of all 3 outputs".
