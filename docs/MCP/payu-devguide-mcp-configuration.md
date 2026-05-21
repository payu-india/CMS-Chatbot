---
title: PayU Devguide MCP Configuration
deprecated: false
hidden: false
metadata:
  robots: index
---
---
title: PayU Devguide MCP Configuration
excerpt: >-
  Search PayU documentation, browse the integration catalog, and fetch
  production-ready code from Cursor, VS Code, or Claude.
hidden: false
metadata:
  title: PayU Developer MCP — Documentation Search & Integration Code
  description: >-
    Connect Cursor, VS Code, or Claude to PayU developer docs via MCP. Semantic
    doc search, integration catalog, and copy-paste snippets for payments APIs.
  keywords:
    - PayU Developer MCP
    - MCP server
    - Cursor MCP
    - VS Code MCP
    - PayU integration catalog
  robots: index
---
Search PayU documentation, browse the payment integration catalog, and fetch production-ready code — directly from your AI assistant.

This is PayU’s **developer documentation** MCP server. It helps you integrate PayU payments (checkout, UPI, cards, webhooks, refunds, and more) without leaving Cursor, VS Code, or Claude.

For **llms.txt**, the **OpenAPI catalog**, and the legacy docs MCP endpoint, see [AI Discovery and OpenAPI Specs](doc:ai-discovery-and-openapi-specs). For merchant dashboard operations (transactions, refunds, payment links), see [PayU Remote MCP Server Integration](doc:payu-remote-mcp-server-integration).

## Supported Features

### Documentation Search

Semantic search across [PayU’s official developer docs](https://docs.payu.in/).

**Conceptual guides** — Payment flows, webhooks, 3DS, refunds, error handling, and API reference topics

**Natural-language queries** — Ask in plain English; the server returns relevant excerpts with source URLs

***

### Integration Catalog

Discover what PayU supports before you write code.

**Browse by product** — UPI, Net Banking, EMI, Cards, Tokenization, Core SDK, and more

**Filter by platform** — Web, iOS, Android, React Native, Flutter, Cordova, or pure API

**Filter by integration type** — PayU Hosted, Merchant Hosted, API, or SDK

***

### Integration Code

Production-ready snippets matched to your stack.

**Multi-language** — `curl`, PHP, JavaScript, Java, Python, Swift, Objective-C, Kotlin, React JS

**Copy-paste ready** — Hosted checkout, merchant-hosted, and API examples with doc links

**Scored results** — Best-matching pages returned with URLs for deeper reading

## Available Tools

| Tool | Description |
| --- | --- |
| `get_payu_integration_catalog` | Browse integrations by product, platform, and resource type |
| `get_payu_integration_code` | Fetch ready-to-use code for a specific integration |
| `search_payu_docs` | Semantic search over PayU developer documentation |

**Recommended workflow**

1. Call `get_payu_integration_catalog` to see valid platform / language / type combinations.
2. Call `get_payu_integration_code` with your product, platform, language, and resource type.
3. Call `search_payu_docs` for conceptual questions (flows, webhooks, errors, etc.).

## Getting Started

### API key (optional)

You can use the server **without** an API key on the **anonymous tier**:

* **30 requests / minute**
* **100 requests / day**

For higher limits, email **ai-admin@payu.in** to request an API key, then add it as the `x-api-key` header in your MCP client config (see manual setup below).

No OAuth is required for this developer-docs server.

## Setup Instructions

### Add PayU Developer MCP to Cursor

[![Install MCP Server](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/en-US/install-mcp?name=payu-developer-mcp&config=eyJ0eXBlIjoiaHR0cCIsInVybCI6Imh0dHBzOi8vYXNrLWFpLW1jcC03MTA1NzUxNzcxMTIuYXNpYS1zb3V0aDEucnVuLmFwcC9tY3AifQ==)

### Add PayU Developer MCP to VS Code

[![Install MCP Server](https://img.shields.io/badge/Install-MCP-blue)](https://insiders.vscode.dev/redirect?url=vscode:mcp/install?%7B%22type%22%3A%22http%22%2C%22name%22%3A%22payu-developer-mcp%22%2C%22version%22%3A%221.0.0%22%2C%22description%22%3A%22Search%20PayU%20docs%2C%20browse%20integrations%2C%20and%20fetch%20code%20snippets%22%2C%22url%22%3A%22https%3A%2F%2Fask-ai-mcp-710575177112.asia-south1.run.app%2Fmcp%22%2C%22author%22%3A%22PayU%22%2C%22tags%22%3A%5B%22payu%22%2C%22payments%22%2C%22developer%22%2C%22mcp%22%5D%2C%22categories%22%3A%5B%22mcp%22%5D%7D)

### OR

**Manual setup:** Update your `mcp.json` configuration file (for Cursor: `~/.cursor/mcp.json`) with:

```json
{
  "mcpServers": {
    "payu-developer-mcp": {
      "type": "http",
      "url": "https://ask-ai-mcp-710575177112.asia-south1.run.app/mcp"
    }
  }
}
```

**With an API key** (higher rate limits):

```json
{
  "mcpServers": {
    "payu-developer-mcp": {
      "type": "http",
      "url": "https://ask-ai-mcp-710575177112.asia-south1.run.app/mcp",
      "headers": {
        "x-api-key": "YOUR_API_KEY_HERE"
      }
    }
  }
}
```

Save the file and reload your editor to activate the integration.

#### For Claude Desktop / Pro Users

1. Open Claude Desktop
2. Go to **Settings → Connectors → Add custom connector**
3. Name: `PayU Developer MCP` (or any name you prefer)
4. URL: `https://ask-ai-mcp-710575177112.asia-south1.run.app/mcp`
5. If you have an API key, configure the `x-api-key` header in your client’s advanced settings
6. Save and restart Claude

#### Other MCP Clients

```json
{
  "mcpServers": {
    "payu-developer-mcp": {
      "type": "http",
      "url": "https://ask-ai-mcp-710575177112.asia-south1.run.app/mcp"
    }
  }
}
```

## Workflows You Can Try

### Integration Discovery

> Find the right PayU integration for your stack

```
I need to accept UPI payments on my React Native app. Browse the PayU integration
catalog for UPI options on React Native and show me what's available (Hosted vs SDK vs API).
```

### Fetch Integration Code

> Get copy-paste snippets for your language and platform

```
Give me PayU Core SDK integration code for Android in Kotlin using the SDK resource type.
Include setup steps and the main payment initiation snippet.
```

### Web Checkout (Hosted)

> Stand up PayU Hosted Checkout on a website

```
I'm building a Node.js website and want PayU Hosted Checkout for cards and UPI.
Show me the integration catalog entry for Web + PayU Hosted, then fetch JavaScript
integration code I can use in my backend and frontend.
```

### Merchant-Hosted / API Flow

> Server-side payment APIs without the hosted UI

```
Explain the difference between PayU Hosted and Merchant Hosted checkout. Then fetch
PHP API integration code for creating a payment request with hash generation.
```

### Webhooks & Post-Payment

> Understand callbacks and verification

```
How does PayU's payment webhook work? What events are sent, how do I verify the hash,
and what should my idempotent handler do on success vs failure?
Search the docs and summarize with links.
```

### Refunds & Settlements

> Operational flows after go-live

```
Walk me through PayU's refund API: required parameters, sync vs async behavior,
and common error codes. Pull relevant doc sections.
```

### Compare Payment Modes

> Pick between Net Banking, EMI, Wallets, etc.

```
I want Net Banking with TPV on Web. Search the catalog for Net Banking integrations,
then get curl examples for the API resource type so I can test in Postman first.
```

### Multi-Platform (Flutter)

> Same product, mobile framework

```
List Flutter integrations available for Cards and EMI. Then get Dart/Flutter SDK
snippets for EMI on Android and iOS.
```

## Tips for Best Results

* **Start with the catalog** — Call `get_payu_integration_catalog` before `get_payu_integration_code` so platform, language, and resource type are valid.
* **Be specific** — Include product (e.g. "UPI Collect", "Core SDK"), platform (`Web`, `Android`, …), and language (`javascript`, `kotlin`, …).
* **Use doc search for "why"** — Flows, compliance, webhooks, and troubleshooting → `search_payu_docs`.
* **Use code fetch for "how"** — Implementation snippets → `get_payu_integration_code`.
* **Request an API key for heavy use** — Anonymous limits are fine for exploration; production or team usage should use `x-api-key`.

## Important Notes

<Callout icon="⚠️" theme="warning">
  **Developer docs only** — This server does not create payment links, run transactions, or access your merchant dashboard. Use the [merchant MCP](doc:payu-remote-mcp-server-integration) for those operations.
</Callout>

<Callout icon="⚠️" theme="warning">
  **Rate limits** — Anonymous usage is capped at 30 req/min and 100 req/day. Contact **ai-admin@payu.in** for a key if you hit limits.
</Callout>

<Callout icon="⚠️" theme="warning">
  **Verify in dashboard** — Always confirm credentials, salt, and environment (test vs production) in the [PayU Dashboard](https://onboarding.payu.in/) before going live.
</Callout>

<Callout icon="⚠️" theme="warning">
  **Docs are authoritative** — Snippets are sourced from PayU documentation; re-check hash algorithms, endpoints, and field names against the latest docs before production deploys.
</Callout>

## Support

* **API key requests** — [ai-admin@payu.in](mailto:ai-admin@payu.in)
* **Developer documentation** — [https://docs.payu.in/](https://docs.payu.in/)
* **Repository** — [https://github.com/payu-intrepos/payu-developer-mcp](https://github.com/payu-intrepos/payu-developer-mcp)
