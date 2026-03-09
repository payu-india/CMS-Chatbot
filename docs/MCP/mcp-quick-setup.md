---
title: MCP Quick Setup
deprecated: false
hidden: false
metadata:
  robots: index
---
---
title: Quick Setup
deprecated: false
hidden: false
metadata:
  title: Remote MCP for Merchants - Quick Setup
  keywords:
    - Remote MCP Setup
    - MCP Client Configuration
    - Cursor MCP
    - Claude Desktop MCP
  robots: index
---

Get started with PayU Remote MCP for Merchants in three simple steps.

## Step 1: Configure Your MCP Client

Add the PayU Remote MCP service URL to your MCP client configuration.

### For Cursor IDE

Edit `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "payu-mcp": {
      "url": "https://api.payu.in/mcp",
      "transport": "http"
    }
  }
}
```

### For Claude Desktop

Edit the configuration file based on your operating system:

* **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
* **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "payu-mcp": {
      "url": "https://api.payu.in/mcp",
      "transport": "http"
    }
  }
}
```

### For Other MCP Clients

Use the following configuration values:

| Parameter     | Value                     |
| ------------- | ------------------------- |
| **URL**       | `https://api.payu.in/mcp` |
| **Transport** | `http`                    |

## Step 2: Authenticate

When you first use the service:

1. Your client automatically discovers authentication requirements
2. A browser window opens for PayU login
3. Enter your credentials and approve access
4. Client securely stores authentication tokens

> 📘 Note
>
> You won't need to authenticate again unless the token expires. Tokens typically last several hours and are automatically refreshed by your client.

## Step 3: Start Using Tools

Use natural language with your AI assistant to interact with PayU services:

```
"Show me transactions for the last 7 days"
"Process a refund for transaction TX-12345"
"Check the status of settlement S-567890"
```

## Verification

To verify your setup is working correctly:

1. Open your MCP-compatible client (Cursor, Claude Desktop, etc.)
2. Try a simple query: "What merchant accounts do I have access to?"
3. If prompted, complete the authentication flow in your browser
4. You should receive a response listing your merchant accounts

## Next Steps

* [Authentication](ref:authentication) - Learn more about OAuth 2.1 security
* [MCP Tools](doc:mcp-tools) - Read more examples of what you can do
* [MCP FAQs](doc:mcp-faqs) - Get help if something isn't working