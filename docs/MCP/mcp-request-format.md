---
title: MCP Request Format
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: Request Format
deprecated: false
hidden: false
metadata:
  title: Remote MCP for Merchants - Request Format
  keywords:
    - MCP Request Format
    - JSON-RPC
    - API Format
    - Custom MCP Client
  robots: index
---

This section provides technical details for developers building custom MCP clients or integrating with PayU Remote MCP programmatically.

PayU Remote MCP uses the JSON-RPC 2.0 protocol over HTTP. All requests are sent to a single endpoint with OAuth 2.1 bearer token authentication.

## Service Endpoint

| Property      | Value                     |
| ------------- | ------------------------- |
| **URL**       | `https://api.payu.in/mcp` |
| **Method**    | `POST`                    |
| **Protocol**  | JSON-RPC 2.0              |
| **Transport** | HTTP                      |

## Authentication Header

All requests must include an OAuth bearer token in the Authorization header:

```
Authorization: Bearer YOUR_ACCESS_TOKEN
```

### Obtaining Access Tokens

Access tokens are obtained through the OAuth 2.1 flow:

1. Initiate authorization request with PKCE
2. User authenticates via browser
3. Receive authorization code
4. Exchange code for access token
5. Use token in Authorization header

> 📘 Note
>
> Most MCP clients handle token management automatically. You only need to implement this if building a custom client.

## Tool Call Format

### Request Structure

```http
POST https://api.payu.in/mcp
Authorization: Bearer YOUR_ACCESS_TOKEN
Content-Type: application/json

{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "params": {
    "name": "TOOL_NAME",
    "arguments": {
      "param1": "value1",
      "param2": "value2"
    }
  },
  "id": 1
}
```

### Request Fields

| Parameter                        | Description                                               | Example                        |
| :------------------------------- | :-------------------------------------------------------- | :----------------------------- |
| jsonrpc<br />`mandatory`         | `String` - JSON-RPC version. Must be "2.0"                | 2.0                            |
| method<br />`mandatory`          | `String` - The MCP method to call                         | tools/call                     |
| params<br />`mandatory`          | `Object` - Parameters for the method                      | See below                      |
| params.name<br />`mandatory`     | `String` - Name of the tool to invoke                     | get-transaction-details        |
| params.arguments<br />`optional` | `Object` - Arguments for the tool                         | \{"transactionId": "TX-12345"} |
| id<br />`mandatory`              | `String` or `Number` - Request identifier for correlation | 1                              |

## Response Format

### Successful Response

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "Result of the tool call"
      }
    ]
  }
}
```

### Response Fields

| Field                   | Description                        |
| ----------------------- | ---------------------------------- |
| `jsonrpc`               | Always "2.0"                       |
| `id`                    | Matches the request ID             |
| `result`                | Contains the tool execution result |
| `result.content`        | Array of content items             |
| `result.content[].type` | Content type (usually "text")      |
| `result.content[].text` | The actual result text             |

### Error Response

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "error": {
    "code": -32600,
    "message": "Invalid Request",
    "data": {
      "details": "Additional error information"
    }
  }
}
```

### Error Codes

| Code     | Message          | Description                  |
| -------- | ---------------- | ---------------------------- |
| `-32700` | Parse error      | Invalid JSON                 |
| `-32600` | Invalid Request  | Request structure is invalid |
| `-32601` | Method not found | Tool doesn't exist           |
| `-32602` | Invalid params   | Invalid tool arguments       |
| `-32603` | Internal error   | Server-side error            |

## Example Requests

### List Tools

```json
{
  "jsonrpc": "2.0",
  "method": "tools/list",
  "params": {},
  "id": 1
}
```

### Get Transaction Details

```json
{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "params": {
    "name": "get-transaction-details",
    "arguments": {
      "transactionId": "TX-98765"
    }
  },
  "id": 2
}
```

### Process Refund

```json
{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "params": {
    "name": "process-refund",
    "arguments": {
      "transactionId": "TX-12345",
      "amount": 500.00,
      "reason": "Customer request"
    }
  },
  "id": 3
}
```

## HTTP Headers

### Required Headers

| Header          | Value              | Description            |
| --------------- | ------------------ | ---------------------- |
| `Authorization` | `Bearer {token}`   | OAuth 2.1 access token |
| `Content-Type`  | `application/json` | Request body format    |

### Optional Headers

| Header         | Value              | Description         |
| -------------- | ------------------ | ------------------- |
| `X-Request-ID` | UUID               | For request tracing |
| `Accept`       | `application/json` | Response format     |

## Rate Limiting

The service implements rate limiting to ensure fair usage:

* Rate limits are applied per merchant account
* Exceeding limits returns HTTP 429 (Too Many Requests)
* Include `Retry-After` header indicates wait time

## Best Practices

1. **Reuse Connections** - Use HTTP keep-alive for better performance
2. **Handle Errors Gracefully** - Implement proper error handling for all response codes
3. **Implement Retry Logic** - Retry failed requests with exponential backoff
4. **Validate Responses** - Always validate the response structure before processing
5. **Log Request IDs** - Include unique request IDs for debugging

## Next Steps

* [MCP Tools](doc:mcp-tools): Check all available tools and their parameters
* [MCP FAQs](doc:mcp-faqs): Refer the Frequently Asked Questions if you are facing issues with MCP.
