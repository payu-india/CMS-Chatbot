---
title: MCP FAQs
deprecated: false
hidden: false
metadata:
  robots: index
---
---
title: MCP FAQs
deprecated: false
hidden: false
metadata:
  title: Remote MCP for Merchants - FAQ
  keywords:
    - MCP FAQ
    - Common Questions
    - MCP Help
  robots: index
---

Frequently asked questions about PayU Remote MCP for Merchants.

## Setup & Configuration

### Do I need to configure anything besides the service URL?

No! Just add the URL to your MCP client configuration, and everything else is automatic.

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

### Which MCP clients are supported?

PayU Remote MCP works with any MCP-compatible client, including:

* **Cursor IDE** - Configuration in `~/.cursor/mcp.json`
* **Claude Desktop** - Configuration in the Claude desktop config file
* **Custom clients** - Any client implementing the MCP specification

### Do I need to install anything?

No installation required! Unlike the local MCP server, Remote MCP is a hosted service. You only need to configure the URL in your MCP client.

## Authentication

### How long do I stay authenticated?

Tokens last several hours. Your client will automatically refresh them when needed, so you rarely need to re-authenticate manually.

### What if I get logged out?

If your token expires:

1. Your next request will trigger the authentication flow
2. A browser window opens for PayU login
3. Complete the login and continue using the service

### Can I use the same credentials for multiple clients?

Yes! You can use your PayU credentials on multiple MCP clients. Each client will have its own authentication session.

## Merchant Accounts

### Can I use multiple merchant accounts?

Yes! Use the account switching commands to change between accounts:

```
"What merchant accounts do I have access to?"
"Switch to merchant account 180012"
```

Your selection is cached for 1 hour.

### Why am I asked to select a merchant account?

If you have access to multiple merchant accounts, you need to specify which one to use. Single-account users are automatically connected.

### Can I access accounts I don't own?

No. You can only access merchant accounts that have been explicitly granted to your PayU user account.

## Security & Privacy

### Is my data secure?

Yes. All communication is encrypted using TLS, and sensitive data (PII) is automatically filtered from responses.

### What data does PayU collect from MCP usage?

PayU logs requests for security and troubleshooting purposes. Your actual query content and personal data are protected according to PayU's privacy policy.

### Can I revoke MCP access?

Yes. You can revoke access anytime through your PayU account settings under "Connected Applications" or "API Access."

## Tools & Capabilities

### What can I do with Remote MCP?

Common operations include:

* View transaction history
* Get transaction details
* Process refunds
* Check payment status
* View settlements
* Generate reports

### Why can't I access certain tools?

Tool availability depends on your account permissions. Some tools require additional permissions. Contact your account administrator for access.

### Are there rate limits?

Yes, the service implements fair-use rate limits. If you exceed limits, you'll receive an HTTP 429 error. Wait and retry after the indicated time.

## Comparison with Local MCP Server

### How is Remote MCP different from the local MCP server?

| Feature            | Remote MCP             | Local MCP Server                 |
| ------------------ | ---------------------- | -------------------------------- |
| **Hosting**        | PayU-hosted service    | Self-hosted on your machine      |
| **Setup**          | URL configuration only | Clone repo, install dependencies |
| **Authentication** | OAuth 2.1 via browser  | API credentials in config        |
| **Updates**        | Automatic              | Manual updates required          |
| **Maintenance**    | Managed by PayU        | Managed by you                   |

### Which should I use?

**Use Remote MCP if you want:**

* Simple setup (just a URL)
* No installation or maintenance
* Automatic updates
* OAuth-based authentication

**Use Local MCP Server if you want:**

* Full control over the server
* Offline operation capability
* Custom modifications
* Direct credential management

### Can I use both?

Yes! You can configure both in your MCP client and choose which to use for different purposes.

## Troubleshooting

### What should I do if something isn't working?

1. Check the [Troubleshooting](doc:remote-mcp-troubleshooting) guide
2. Verify your configuration
3. Try re-authenticating
4. Contact PayU support if issues persist

### Where can I get help?

* **Documentation**: This documentation site
* **Support**: Contact your PayU service administrator
* **Technical Issues**: Reach out to PayU support

### What happens if I lose access?

You'll receive an authentication error. Simply re-authenticate by restarting your client or triggering manual authentication to regain access.

## Additional Questions

### Is Remote MCP available 24/7?

The service is designed for high availability. However, like any service, maintenance windows may occasionally occur. Check with PayU support for status updates.

### Are there any costs associated with Remote MCP?

Contact your PayU account manager for information about pricing and included features.

### How do I provide feedback?

Contact your PayU service administrator with feature requests, bug reports, or general feedback.

## Additional Resources

### For Developers

* **MCP Specification:** [https://spec.modelcontextprotocol.io/](https://spec.modelcontextprotocol.io/)
* **OAuth 2.1 Specification:** [https://oauth.net/2.1/](https://oauth.net/2.1/)

### Related Documentation

* [Remote MCP Introduction](doc:remote-mcp-introduction)
* [PayU MCP Server (Local)](doc:payu-mcp-server)
* [MCP Usage Examples](doc:mcp-usage-examples)
