---
title: V2 Cancel Refund Transaction API
deprecated: false
hidden: false
metadata:
  robots: index
---
The **Cancel Refund Transaction** API allows merchants to initiate and process refund cancellations for transactions. It is part of PayU's modernized API suite and differs from the v1 API by providing enhanced functionality, improved response formats, and better support for complex use cases.

### Endpoint

```
POST /v1/transaction
```

### Request Parameters

<Table>
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
        `String` Merchant key provided by PayU while onbaording.
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
        PayU transaction ID (also called PayU ID) that is found in the PayU payment response.
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
        JSON string containing additional parameters.
      </td>

      <td>
        See JSON Fields below
      </td>
    </tr>
  </tbody>
</Table>

#### JSON Fields in the `request` Parameter:

| Parameter   | Description                                    | Example     |
| ----------- | ---------------------------------------------- | ----------- |
| txn\_mode   |                                                |             |
| `mandatory` | Transaction refund mode (must be 1 for Source) | `1`         |
| token       |                                                |             |
| `mandatory` | Unique token for the refund transaction        | `abbv98vqw` |

### Sample Request

```bash
curl --location 'http://localhost:8085/apilayer/v2/refund/secure' \
--header 'Content-Type: application/json' \
--header 'mid: 8006653' \
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

| Parameter   | Description                                                            | Example                     |
| ----------- | ---------------------------------------------------------------------- | --------------------------- |
| status      | Indicates success (1) or failure (0) of the API call                   | `1`                         |
| statusCode  | Specific code for the status of the request                            | `102`                       |
| message     | Describes the outcome of the API call                                  | `"Refund request accepted"` |
| refundId    | Unique identifier for the refund request (present only if successful)  | `123456789`                 |
| payuId      | PayU transaction ID associated with the refund request                 | `999091000003794`           |
| refundToken | Unique token used to identify the refund request                       | `11358934598`               |
| splitInfo   | Contains details of refunds for each split transaction (if applicable) | See JSON example            |

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