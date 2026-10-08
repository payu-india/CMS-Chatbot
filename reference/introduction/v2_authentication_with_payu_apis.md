---
title: Authentication Header for v2 APIs
deprecated: false
hidden: false
metadata:
  title: Authentication with PayU APIs
  description: 'Learn how to securely authenticate and integrate with PayU India’s v2 APIs. '
  keywords:
    - PayU India API authentication
    - Merchant key and salt for PayU APIs
    - REST API authentication with PayU
    - Hash parameter in PayU API requests
    - SHA512 encryption for PayU API security
    - Reverse hashing using PayU node SDK
    - Generate hash for PayU API parameters
  robots: index
---
---
title: Authentication for PayU v2 APIs
deprecated: false
hidden: false
metadata:
  title: Authentication with PayU APIs
  description: Learn how to authenticate requests to PayU v2 APIs using the documented SHA-512 request signature.
  keywords:
    - PayU API authentication
    - PayU v2 API authentication
    - SHA-512 request signature
    - PayU merchant key and secret
  robots: index
---

## Overview

PayU v2 API requests use a request signature generated with SHA-512. The signature is calculated from the exact request body, the value of the `date` header, and the merchant secret.

> **Important:** This construction is a SHA-512 digest. It is not HMAC. Do not describe it as HMAC in application code or documentation.

Use sandbox credentials while testing. Replace the placeholders in the examples with credentials issued for your environment. Never publish a merchant secret, session cookie, internal host, or real merchant data in an example.

## Request headers

The endpoint reference is the source of truth for endpoint-specific headers and values. The following headers are used by the v2 authentication format:

| Header | Required use | Description |
| :--- | :--- | :--- |
| `date` | Required for signed requests | The date and time used in the signature. Send it in the HTTP-date format, for example, `Wed, 28 Jun 2023 11:25:19 GMT`. Use the exact same string when calculating the signature and sending the request. |
| `authorization` | Required for signed requests | The authorization value containing the merchant key, algorithm, signed-header list, and SHA-512 signature. |
| `Content-Type` | Required for JSON request bodies | Send `application/json` when the request body is JSON. The endpoint reference must identify any different content type. |
| `Info-Command` | Include when required by the endpoint reference | The endpoint reference must define the value when this header is required. Do not invent a value or send an undocumented command. |

## Authorization value

Use this format for the `authorization` header:

```text
hmac username="<SANDBOX_MERCHANT_KEY>", algorithm="sha512", headers="date", signature="<SHA512_HEX_DIGEST>"
```

Although the header value retains the documented `hmac` scheme token, the digest described on this page is the SHA-512 construction below, not an HMAC calculation.

| Field | Description |
| :--- | :--- |
| `username` | The sandbox merchant key. |
| `algorithm` | `sha512`. |
| `headers` | The headers included in the signature. The documented format signs `date`. |
| `signature` | The lowercase hexadecimal SHA-512 digest. |

## Hashing algorithm

Calculate the signature as follows:

```text
sha512(<exact request body bytes as sent> + "|" + <date header value> + "|" + <merchant secret>)
```

Use the same body bytes for hashing and transmission. Do not reformat, reorder, pretty-print, or otherwise modify a serialized JSON body after calculating the signature.

For a request with no body, use an empty body component and follow the endpoint reference for the applicable method:

```text
sha512("" + "|" + <date header value> + "|" + <merchant secret>)
```

The endpoint reference must state whether a method accepts an empty body and which headers it requires. Do not hash a different representation of query parameters unless the endpoint-specific contract explicitly requires it.

### Date validity and clock skew

The `date` value used for signing must be the value sent in the request. The accepted clock-skew tolerance is environment- and service-specific and must be confirmed by PayU engineering before it is published as a numeric value. Clients should use a synchronised system clock and generate the date immediately before sending the request.

## Node.js example

The following example is a Node.js example. The body string is illustrative sample data. In a real request, send the exact same `body` string that is hashed.

```javascript
const crypto = require('node:crypto');

const merchantKey = '<SANDBOX_MERCHANT_KEY>';
const merchantSecret = '<SANDBOX_SECRET>';
const date = new Date().toUTCString();

// Illustrative sample body. Hash and send this exact string.
const body = '{"referenceId":"TEST-ORDER-001","amount":"10.00","currency":"INR"}';

const hashInput = `${body}|${date}|${merchantSecret}`;
const signature = crypto
  .createHash('sha512')
  .update(hashInput, 'utf8')
  .digest('hex');

const authorization =
  `hmac username="${merchantKey}", ` +
  `algorithm="sha512", headers="date", signature="${signature}"`;

console.log({
  date,
  authorization,
  contentType: 'application/json'
});
```

## Implementation checklist

Before publishing or sending a request, confirm that:

- The request uses sandbox credentials during testing.
- The body is serialized once and the exact transmitted bytes are hashed.
- The same `date` string is used in the hash and request header.
- The `authorization` value uses `algorithm="sha512"`.
- `Content-Type` and `Info-Command` follow the endpoint reference.
- No real merchant data, internal infrastructure data, cookies, or secrets appear in examples.
- The request is tested in the sandbox before publication.
