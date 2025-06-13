---
title: V2 Cancel Refund Transaction API
deprecated: false
hidden: true
metadata:
  robots: index
---
The **Cancel Refund Transaction** API allows merchants to initiate and process refund cancellations for transactions. It is part of PayU's modernized API suite and differs from the v1 API by providing enhanced functionality, improved response formats, and better support for complex use cases.

The Cancel Refund Transaction API allows merchants to initiate and process refund cancellations for transactions. It is part of PayU's modernized API suite and differs from the v1 API by providing enhanced functionality, improved response formats, and better support for complex use cases such as split payments. This API is exposed to both new and existing merchants as a core API for processing refunds.


### Endpoint

```
POST /v1/transaction
```

### Request Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| key
`mandatory` | Merchant key for authentication | `iDJYfd` |
| mihpayid
`mandatory` | PayU transaction ID (also called PayU ID) | `999091000003794` |
| request
`mandatory` | JSON string containing additional parameters | See JSON Fields below |

#### JSON Fields in the `request` Parameter:

| Parameter | Description | Example |
|-----------|-------------|---------|
| txn_mode
`mandatory` | Transaction refund mode (must be 1 for Source) | `1` |
| token
`mandatory` | Unique token for the refund transaction | `abbv98vqw` |

### Sample Request
```bash
curl --location 'http://localhost:8085/apilayer/v2/refund/secure' \
--header 'Content-Type: application/json' \
--header 'mid: 8006653' \
--header 'Date: Thu, 17 Feb 2022 08:17:59 GMT' \
--header 'Digest: vpGay5D/dmfoDupALPplYGucJAln9gS29g5Orn+8TC0=' \
--header 'Authorization: hmac username="smsplus", algorithm="hmac-sha256", headers="date digest", signature="zGmP5Zeqm1pxNa+d68DWfQFXhxoqf3st353SkYvX8HI="' \
--header 'platformId: 1' \
--data '{
    "mihpayId": "999000000000478",
    "refundToken": "abbv98vqw",
    "amount": 0.1,
    "refundDetails": {},
    "refundSplitRequest": {
        "33rOiT": {
            "amount": 0.21
        }
    }
}'
```

### Response Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| status | Indicates success (1) or failure (0) of the API call | `1` |
| statusCode | Specific code for the status of the request | `102` |
| message | Describes the outcome of the API call | `"Refund request accepted"` |
| refundId | Unique identifier for the refund request (present only if successful) | `123456789` |
| payuId | PayU transaction ID associated with the refund request | `999091000003794` |
| refundToken | Unique token used to identify the refund request | `11358934598` |
| splitInfo | Contains details of refunds for each split transaction (if applicable) | See JSON example |

### Sample Response

#### Success Response
```json
{
  "status": 1,
  "statusCode": "102",
  "message": "Refund request accepted",
  "refundId": "123456789"
}
```

#### Failure Response
```json
{
  "status": 0,
  "errorcode": "4000",
  "message": "Refund request rejected"
}
```
