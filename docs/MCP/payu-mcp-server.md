---
title: Introduction
deprecated: false
hidden: false
metadata:
  robots: index
---
PayU MCP Server provides specialized integration that enables AI tools to securely access PayU payment APIs through the Model Context Protocol (MCP). This integration allows AI assistants to create payment links, retrieve transaction details, and access invoice information directly, making your payment workflows smarter and more efficient.

## What is MCP?

The Model Context Protocol (MCP) is an open protocol that enables seamless integration between LLM applications and external data sources and tools. Whether you're building an AI-powered IDE, enhancing a chat interface, or creating custom AI workflows, MCP provides a standardized way to connect LLMs with the context they need. For more information, refer to [Model Context Protocol](https://github.com/modelcontextprotocol).

## MCP Tools

| Tool Name                   | Description                                       |
| --------------------------- | ------------------------------------------------- |
| **create-payment-link**     | Generate a new payment link for your customers    |
| **get-invoice-details**     | Retrieve comprehensive details for any invoice ID |
| **get-transaction-details** | Access complete transaction information           |

## Prerequisites

* Python 3.10 or higher
* PayU Merchant Account with API access
* MCP-compatible AI client (Claude AI, etc.)

For the steps to install, refer to [Install and Configure MCP](doc:install-and-configure-payu-mcp-server).

## License

This project is licensed under the MIT License. For more information, refer to [PayU Github > MCP > LICENSE ](https://github.com/payu-intrepos/payu-mcp-server/blob/main/LICENSE)page.