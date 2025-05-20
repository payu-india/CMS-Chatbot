---
title: PayU MCP Server
deprecated: false
hidden: false
metadata:
  robots: index
---
PayU MCP Server provides specialized integration that enables AI tools to securely access PayU payment APIs through the Model Context Protocol (MCP). This integration allows AI assistants to create payment links, retrieve transaction details, and access invoice information directly, making your payment workflows smarter and more efficient.

## What is the Model Context Protocol (MCP)?

> The Model Context Protocol (MCP) is an open protocol that enables seamless integration between LLM applications and external data sources and tools. Whether you're building an AI-powered IDE, enhancing a chat interface, or creating custom AI workflows, MCP provides a standardized way to connect LLMs with the context they need.
>
> — [Model Context Protocol](https://github.com/modelcontextprotocol)

## Available Tools

| Tool Name                   | Description                                       |
| --------------------------- | ------------------------------------------------- |
| **create-payment-link**     | Generate a new payment link for your customers    |
| **get-invoice-details**     | Retrieve comprehensive details for any invoice ID |
| **get-transaction-details** | Access complete transaction information           |

## Getting Started

### Prerequisites

* Python 3.10 or higher
* PayU Merchant Account with API access
* MCP-compatible AI client (Claude AI, etc.)

<br />

## Usage Examples

### Creating a Payment Link

Once configured, your MCP Client can create payment links with a natural language request:

1. Payment link with contacts

```text
Create a payment link for ₹5000 for Web Development Services and send to ABC
```

2. Payment link with email

```text
Create a payment link for ₹5000 for Web Development Services and send to <abc@example.com>
```

### Fetching transactions for Invoice Number/Payment Link

Once configured, your AI assistant can help you fetch invoice number details with a natural language request:

```text
Get the invoice details for <Invoice-ID>
```

### Fetching details for any transaction

Once configured, your AI assistant can help you fetch transaction details with a natural language request:

```text
Provide the transaction details for <Transaction-ID>
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.