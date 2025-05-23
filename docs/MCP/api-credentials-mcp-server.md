---
title: API Credentials - MCP Server
deprecated: false
hidden: true
metadata:
  title: API Credentials - MCP Server
  keywords:
    - API Credentials for MCP Server
    - MCP API Credentials
    - MCP Credentials
  robots: index
---
This section describes how to use the API credentials with PayU MCP Server.

> 📘 Reference:
>
> To obtain your API credentials, refer to [Get Client ID and Secret](https://docs.payu.in/docs/get-client-id-and-secret-from-dashboard).

Required credentials:

* **CLIENT\_ID**: Your PayU client ID
* **CLIENT\_SECRET**: Your PayU client secret
* **MERCHANT\_ID**: Your PayU merchant identifier

### Additional Permission Scopes

When configuring your API access, ensure you have the following permission scopes:

* **read\_transactions**:
  * Provides access to transaction history and details
  * Allows retrieval of transaction metadata.
  * Enables detailed transaction analysis and tracking
* **read\_invoices**:
  * Enables fetching comprehensive invoice details
  * Provides access to invoice status, amounts, and related transaction information
  * Read-only permission ensures secure access to invoice data

**Note**: Contact PayU support to confirm these specific scopes are available and properly configured for your merchant account.