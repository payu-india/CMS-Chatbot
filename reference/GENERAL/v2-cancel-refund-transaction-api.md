---
title: v2 Cancel Refund Transaction API
deprecated: false
hidden: true
metadata:
  robots: index
---
The **Cancel Refund Transaction** API allows merchants to initiate and process refund cancellations for transactions. It is part of PayU's modernized API suite and differs from the v1 API by providing enhanced functionality, improved response formats, and better support for complex use cases.

The **Cancel Refund Transaction** API allows merchants to initiate and process refund cancellations for transactions. It is part of PayU's modernized API suite and differs from the v1 API by providing enhanced functionality, improved response formats, and better support for complex use cases such as split payments. This API is exposed to both new and existing merchants as a core API for processing refunds.

### Endpoint

```
POST /v1/transaction
```

## Request parameters

### Request header

<HeaderAuthentication />

### Body parameters

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
        `JSON String` The JSON object contains the transaction mode and token. For more information, refer to [request JSON fields description](#request-json-fields-description) .
      </td>

      <td>
        [request JSON fields description](#request-json-fields-description)
      </td>
    </tr>
  </tbody>
</Table>

> 📘 Note:
>
> At least one of the following parameters must be provided: `requestId`, `payuId`, or `tokenId`.

### request JSON fields description

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
        txn\_mode
        `mandatory`
      </td>

      <td>
        Transaction refund mode (must be 1 for Source)
      </td>

      <td>
        `1`
      </td>
    </tr>

    <tr>
      <td>
        token
        `mandatory`
      </td>

      <td>
        Unique token for the refund transaction
      </td>

      <td>
        `abbv98vqw`
      </td>
    </tr>
  </tbody>
</Table>

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

### Response parameters

| Parameter   | Description                                                            | Example                     |
| ----------- | ---------------------------------------------------------------------- | --------------------------- |
| status      | Indicates success (1) or failure (0) of the API call                   | `1`                         |
| statusCode  | Specific code for the status of the request                            | `102`                       |
| message     | Describes the outcome of the API call                                  | `"Refund request accepted"` |
| refundId    | Unique identifier for the refund request (present only if successful)  | `123456789`                 |
| payuId      | PayU transaction ID associated with the refund request                 | `999091000003794`           |
| refundToken | Unique token used to identify the refund request                       | `11358934598`               |
| splitInfo   | Contains details of refunds for each split transaction (if applicable) |                             |

### Sample response

#### Success response

```json
{
  "status": 1,
  "statusCode": "102",
  "message": "Refund request accepted",
  "refundId": "123456789"
}
```

#### Failure response

```json
{
  "status": 0,
  "errorcode": "4000",
  "message": "Refund request rejected"
}
```