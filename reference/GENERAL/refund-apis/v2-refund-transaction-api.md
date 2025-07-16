---
title: 'v2 Refund Transaction API '
deprecated: false
hidden: true
metadata:
  robots: index
---
The **Refund Transaction** API allows merchants to initiate refunds for transactions. Its functionally similar to the **Cancel Refund Transaction** API, but is maintained only for backward compatibility with existing integrations. The v2 API offers enhanced functionality and improved response formats compared to the v1 API.

**Endpoint**

|                        |                                                                  |
| :--------------------- | :--------------------------------------------------------------- |
| Production Environment | [https://test.payu.in/v2/refund](https://test.payu.in/v2/refund) |
| Test Environment       | [https://info.payu.in/v2/refund](https://info.payu.in/v2/refund) |

## Request parameters

### Request header

<HeaderAuthentication />

### Body Parameters

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
      </th>

      <th>
        Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        key
        `mandatory`
      </td>

      <td>
        `String `This parameter must contain the merchant key provided by PayU.
      </td>

      <td>
        `iDJYfd`
      </td>
    </tr>

    <tr>
      <td>
        mihpayid
        `mandatory`
      </td>

      <td>
        `String `This parameter must contains the PayU ID (mihpayuid) that you receive in the response for a successful payment transaction.
      </td>

      <td>
        `999091000003794`
      </td>
    </tr>

    <tr>
      <td>
        request
        `mandatory`
      </td>

      <td>
        `JSON String `JSON string containing additional parameters. For more information, refer to [request JSON fields description](#request-json-fields-description).
      </td>

      <td>
        Refer to [request JSON fields description](#request-json-fields-description) .
      </td>
    </tr>
  </tbody>
</Table>

#### request JSON fields description

| Parameter                          | Description                                                                                                                                                                                                                                                                                                                                                                                                      | Example           |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| txn\_mode<br />`mandatory`         | Transaction refund mode (must be 1 for source)                                                                                                                                                                                                                                                                                                                                                                   | `1`               |
| token<br />`mandatory`             | Token ID (unique token from the merchant) for the refund request. Token ID has to be generated at your end for each new refund request. It is an identifier for each new refund request which can be used for tracking it. It must be unique for every new refund request generated – otherwise the refund request would not be generated successfully, Token ID length should not be greater than 23 characters | `11358998`        |
| amount<br />`mandatory`            | The specific amount that needs to be refunded                                                                                                                                                                                                                                                                                                                                                                    | `0.21`            |
| refundDetails<br />`optional`      | Additional details for the refund                                                                                                                                                                                                                                                                                                                                                                                | \`\`              |
| refundSplitRequest<br />`optional` | JSON object containing refund split details (if applicable)                                                                                                                                                                                                                                                                                                                                                      | See example below |

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