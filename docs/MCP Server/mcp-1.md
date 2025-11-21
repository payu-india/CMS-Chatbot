---
title: MCP
hidden: true
---
The PayU Developer Documentation Portal Model Context Protocol (MCP) server enables AI-powered code editors like Cursor and Windsurf, plus general-purpose tools like Claude Desktop, to interact directly with your PayU Developer Documentation Portal API and documentation.

## What is MCP?

Model Context Protocol (MCP) is an open standard that allows AI applications to securely access external data sources and tools. The PayU Developer Documentation Portal MCP server provides AI agents with:

* **Direct API access** to PayU Developer Documentation Portal functionality
* **Documentation search** capabilities
* **Real-time data** from your PayU Developer Documentation Portal account
* **Code generation** assistance for PayU Developer Documentation Portal integrations

## PayU Developer Documentation Portal MCP Server Setup

PayU Developer Documentation Portal hosts a remote MCP server at `https://docs.payu.in/mcp`. Configure your AI development tools to connect to this server. If your APIs require authentication, you can pass in headers via query parameters or however headers are configured in your MCP client.

<Tabs>
  <Tab title="Cursor">
    **Add to `~/.cursor/mcp.json`:**

    ```json
    {
      "mcpServers": {
        "payu-hosted-checkout": {
          "url": "https://docs.payu.in/mcp"
        }
      }
    }
    ```

    </Tab>
  <Tab title="Windsurf">
    **Add to `~/.codeium/windsurf/mcp_config.json`:**

    ```json
    {
      "mcpServers": {
        "payu-hosted-checkout": {
          "url": "https://docs.payu.in/mcp"
        }
      }
    }
    ```

  </Tab>
  <Tab title="Claude Desktop">
    **Add to `claude_desktop_config.json`:**

    ```json
    {
      "mcpServers": {
        "payu-hosted-checkout": {
          "url": "https://docs.payu.in/mcp"
        }
      }
    }
    ```

  </Tab>
</Tabs>

## Testing Your MCP Setup

Once configured, you can test your MCP server connection:

1. **Open your AI editor** (Cursor, Windsurf, etc.)
2. **Start a new chat** with the AI assistant
3. **Ask about PayU Developer Documentation Portal** - try questions like:
   * "How do I [common use case]?"
   * "Show me an example of [API functionality]"
   * "Create a [integration type] using PayU Developer Documentation Portal"

The AI should now have access to your PayU Developer Documentation Portal account data and documentation through the MCP server.