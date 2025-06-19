---
title: v2 Check Action Status API
deprecated: false
hidden: true
metadata:
  robots: index
---
The **Check Action Status** API is a new information service designed to allow merchants to retrieve the current status of transaction actions, particularly refund requests. Unlike the v1 API, this enhanced version provides comprehensive details about transaction lifecycles, including capture and refund actions, with improved response formats and support for complex use cases.

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
        `String` This parameter must contain the merchant key provided by PayU.
      </td>

      <td>
        `iDJYfd`
      </td>
    </tr>

    <tr>
      <td>
        requestId
        `optional`
      </td>

      <td>
        `String Array` This parameter includes array of child merchant request IDs to query.
      </td>

      <td>
        `["11763053990", "11763053112"]`
      </td>
    </tr>

    <tr>
      <td>
        payuId
        `optional`
      </td>

      <td>
        `String Array`This parameter must contain the PayU ID (mihpayuid) that you receive in the response for a successful payment transaction.
      </td>

      <td>
        `["11763053990"]`
      </td>
    </tr>

    <tr>
      <td>
        tokenId
        `optional`
      </td>

      <td>
        `String` Token ID (unique token from the merchant) for the refund request. Token ID has to be generated at your end for each new refund request. It is an identifier for each new refund request which can be used for tracking it. It must be unique for every new refund request generated – otherwise the refund request would not be generated successfully. Token ID length should not be greater than 23 characters
      </td>

      <td>
        `["TOKEN12345"]`
      </td>
    </tr>

    <tr>
      <td>
        request
        `mandatory`
      </td>

      <td>
        `JSON String` String containing additional parameters
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

> 📘 Note:
>
> At least one of the following parameters must be provided: `requestId`, `payuId`, or `tokenId`.

### Sample Request

```bash
curl --location 'http://localhost:8080/v1/transaction' \
--header 'mid: 8759546' \
--header 'Content-Type: application/json' \
--header 'Info-Command: check_action_status' \
--header 'Date: Thu, 17 Feb 2022 08:17:59 GMT' \
--header 'Digest: vpGay5D/dmfoDupALPplYGucJAln9gS29g5Orn+8TC0=' \
--header 'Authorization: hmac username="smsplus", algorithm="hmac-sha256", headers="date digest", signature="zGmP5Zeqm1pxNa+d68DWfQFXhxoqf3st353SkYvX8HI="' \
--header 'platformId: 1' \
--data '{
    "requestId": ["11763053990", "11763053112"],
    "payuId": null,
    "tokenId": null
}'
```

### Response Parameters

| Parameter                | Description                                           | Example                                    |
| ------------------------ | ----------------------------------------------------- | ------------------------------------------ |
| message                  | Indicates the result of the API call                  | `"Success"`                                |
| status                   | Status of the API call (1 for success, 0 for failure) | `1`                                        |
| result                   | Array containing the detailed transaction information | See JSON example                           |
| payuId                   | The PayU ID of the transaction                        | `17173825989`                              |
| transactionDetails       | Basic details of the transaction                      | Contains ID, status, amount, etc.          |
| transactionActionDetails | Actions performed on the transaction                  | Contains action type, status, amount, etc. |
| splitTransactionDetails  | Details of split transactions (if applicable)         | Array of split transaction details         |

### Sample Response

#### Success Response

```json
{
    "message": "Success",
    "status": 1,
    "result": [
        {
            "payuId": 17173825989,
            "transactionDetails": {
                "id": 17173825989,
                "transactionId": "PB34794479S",
                "status": "captured",
                "amount": 843.0,
                "mode": "CASH",
                "addedOn": "2023-04-13 20:29:30",
                "phone": "8448480680",
                "email": "example@example.com",
                "productInfo": "PBProduct",
                "errorCode": "E000",
                "errorMessage": "No Error"
            },
            "transactionActionDetails": [
                {
                    "id": 11968786530,
                    "bankRefNo": "T2304132030077646051321",
                    "actionType": "capture",
                    "amount": 843.0,
                    "status": "SUCCESS",
                    "updatedAt": "2023-04-17 12:26:11",
                    "createdAt": "2023-04-13 20:30:15",
                    "settlementId": null,
                    "refundMode": "-"
                }
            ]
        }
    ]
}
```

#### Failure Response

```json
{
    "status": 0,
    "msg": "0 out of 1 Transactions Fetched Successfully",
    "transaction_details": {
        "16988019552": "No action status found value of var1 sent in the request"
    }
}
```