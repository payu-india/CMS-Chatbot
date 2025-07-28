---
title: 'Refund Initiation API '
deprecated: false
hidden: true
metadata:
  robots: index
---
The **Refund Initiation** API allows merchants to initiate refunds for transactions. Its functionally similar to the v1 **Cancel Refund Transaction** API, but is maintained only for backward compatibility with existing integrations. The v2 API offers enhanced functionality and improved response formats compared to the v1 API.

**Endpoint**

|                        |                                                                  |
| :--------------------- | :--------------------------------------------------------------- |
| Production Environment | [https://test.payu.in/v2/refund](https://test.payu.in/v2/refund) |
| Test Environment       | [https://info.payu.in/v2/refund](https://info.payu.in/v2/refund) |

## Request parameters

### Request header

<V2_payment_header_params />

### Request body


### Sample Request

```bash
curl --location 'https://test.payu.in/v2/refund' \
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

| Parameter   | Description                                                        | Example                     |
| ----------- | ------------------------------------------------------------------ | --------------------------- |
| status      | Indicates success (1) or failure (0) of the refund request         | `1`                         |
| statusCode  | Numeric code representing the status of the refund request         | `102`                       |
| message     | Descriptive message about the status of the refund request         | `"Refund request accepted"` |
| payuId      | Unique PayU transaction ID for which the refund was processed      | `999091000003794`           |
| refundToken | Unique token identifying the refund request                        | `11358934598`               |
| requestId   | Unique identifier for the refund request (if available)            | `4993824108552`             |
| refundId    | Unique identifier for the refund transaction (if successful)       | `123456789`                 |
| splitInfo   | Contains details of refunds for split transactions (if applicable) | See JSON example            |

### Sample Response

#### Success Response

```json
{
  "status": 1,
  "statusCode": 102,
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