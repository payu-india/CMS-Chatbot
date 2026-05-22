---
title: Introduction
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: Introduction
deprecated: false
hidden: false
metadata:
  title: Remote MCP for Merchants - Introduction
  keywords:
    - Remote MCP
    - MCP Client Integration
    - PayU Remote MCP
    - Merchant Services
  robots: index
---

PayU Remote MCP for Merchants is a secure service that provides access to PayU's merchant services through a single OAuth-protected endpoint. This guide covers everything you need to integrate and start using the service with your MCP-compatible client.

<Callout icon="📘" theme="info">
  **Enable PayU Remote MCP**: To enable PayU MCP, contact your PayU Key Account Manager or contact <Anchor label="PayU Support" target="_blank" href="https://help.payu.in">PayU Support</Anchor>.
</Callout>

## What Is Remote MCP?

Remote MCP for Merchants enables AI assistants to interact with PayU's payment services using natural language through the Model Context Protocol. Unlike the local MCP server that runs on your machine, the Remote MCP is a hosted service that handles authentication and merchant operations centrally.

## Key Benefits

| Feature                        | Description                                                      |
| ------------------------------ | ---------------------------------------------------------------- |
| **Single Endpoint**            | Access all PayU merchant operations through one URL              |
| **OAuth 2.1 Security**         | Industry-standard authentication with automatic token management |
| **Natural Language Interface** | Interact with PayU services using conversational commands        |
| **Multi-Merchant Support**     | Manage multiple merchant accounts from a single integration      |
| **Data Privacy Protection**    | Automatic PII filtering in responses                             |

## How Is This Different from Local MCP Server?

| Feature            | Remote MCP             | Local MCP Server                 |
| ------------------ | ---------------------- | -------------------------------- |
| **Hosting**        | PayU-hosted service    | Self-hosted on your machine      |
| **Setup**          | URL configuration only | Clone repo, install dependencies |
| **Authentication** | OAuth 2.1 via browser  | API credentials in config        |
| **Updates**        | Automatic              | Manual updates required          |

## Next Steps

* [MCP Quick Setup](doc:mcp-quick-setup) - Get started in 3 simple steps
* [MCP Authentication](doc:mcp-authentication) - Understand the OAuth 2.1 flow
* [MCP Tools](doc:mcp-tools) - Explore available capabilities