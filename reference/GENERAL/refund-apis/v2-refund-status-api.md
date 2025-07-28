---
title: v2 Refund Status API
deprecated: false
hidden: true
metadata:
  robots: index
---
The **Refund Status** API for Split Payments provides a specialized mechanism for tracking refund statuses in split payment scenarios. It's designed for aggregator merchants who process payments divided among multiple recipients. Unlike the v1 API, this enhanced version provides complete visibility into parent-child transaction relationships, refund actions, and settlement details.

**Endpoint**

|                        |                                                                              |
| :--------------------- | :--------------------------------------------------------------------------- |
| Test Environment       | [https://test.payu.in/v2/refundstatus](https://test.payu.in/v2/refundstatus) |
| Production Environment | [https://info.payu.in/v2/refundstatus](https://info.payu.in/v2/refundstatus) |

## Request parameters

### Request headers

<HeaderAuthentication />

### Body parameters

> 📘 Note:
>
> At least one of the following parameters must be provided: `requestId`, `payuId`, or `tokenId`.

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
        requestId
        `conditional`
      </td>

      <td>
        `String Array `Array of request IDs for which the refund information is required.
      </td>

      <td>
        `["11763053990", "11763053112"]`
      </td>
    </tr>

    <tr>
      <td>
        payuId
        `conditional`
      </td>

      <td>
        `String Array `Array of PayU transaction IDs or PayU ID for which the refund information is required. Payu ID (mihpayuid) that you receive in the response for a successful payment transaction.
      </td>

      <td>
        `["11763053990"]`
      </td>
    </tr>

    <tr>
      <td>
        tokenId
        `conditional`
      </td>

      <td>
        `String Array `This parameter must contain the Token ID (unique token from the merchant) for the refund request. Token ID has to be generated at your end for each new refund request. It is an identifier for each new refund request which can be used for tracking it. It must be unique for every new refund request generated – otherwise the refund request would not be generated successfully. Token ID length should not be greater than 23 characters
      </td>

      <td>
        `["TOKEN12345"]`
      </td>
    </tr>
  </tbody>
</Table>

### Sample request

```bash
curl --location 'https://test.payu.in/v2/refundstatus' \
--header 'mid: 8759546' \
--header 'Content-Type: application/json' \
--header 'Info-Command: aggregator_check_action_status_txnid' \
--header 'Date: Thu, 17 Feb 2022 08:17:59 GMT' \
--header 'Digest: vpGay5D/dmfoDupALPplYGucJAln9gS29g5Orn+8TC0=' \
--header 'Authorization: hmac username="smsplus", algorithm="hmac-sha256", headers="date digest", signature="zGmP5Zeqm1pxNa+d68DWfQFXhxoqf3st353SkYvX8HI="' \
--header 'platformId: 1' \
--data '{
    "requestId": null,
    "payuId": ["11763053990"],
    "tokenId": null
}'
```

### Response parameters

| Parameter                            | Description                                               | Example                                    |
| ------------------------------------ | --------------------------------------------------------- | ------------------------------------------ |
| message                              | Indicates the result of the API call                      | `"Success"`                                |
| status                               | Status of the API call (1 for success, 0 for failure)     | `1`                                        |
| result                               | Array containing the parent and split transaction details | See JSON example                           |
| payuId                               | The PayU ID of the parent transaction                     | `17253043342`                              |
| transactionDetails                   | Basic details of the parent transaction                   | Contains ID, status, amount, etc.          |
| transactionActionDetails             | Actions performed on the parent transaction               | Contains action type, status, amount, etc. |
| splitTransactionDetails              | Array of split transaction details                        | Contains payuId, transactionDetails, etc.  |
| transactionActionDetails (in splits) | Actions performed on each split transaction               | Contains refund actions and their details  |

### Sample response

#### Success response

```json
{
    "message": "Success",
    "status": 1,
    "result": [
        {
            "payuId": 17253043342,
            "transactionDetails": {
                "id": 17253043342,
                "transactionId": "PB35163007S",
                "status": "autoRefund",
                "discount": 0.0,
                "amount": 0.0,
                "transactionFee": 2259.0,
                "additionalCharges": 0.0,
                "mode": "CASH",
                "baseTxnId": 0,
                "firstName": "Masood",
                "lastName": "Masood Ahmed Wani",
                "addedOn": "2023-04-27 16:18:16",
                "phone": "8448480680",
                "email": "example@example.com",
                "productInfo": "PBProduct",
                "errorCode": "E000",
                "ibiboCode": "FREC",
                "merchantKey": "iDJYfd",
                "errorMessage": "No Error",
                "paymentSource": "payuS2S"
            },
            "transactionActionDetails": [
                {
                    "id": 12031063143,
                    "bankRefNo": "5jeF8wMyZ9jnZ9_17253043342_1",
                    "token": null,
                    "actionType": "capture",
                    "prevStatus": "failed",
                    "amount": 2259.0,
                    "status": "SUCCESS",
                    "bankArn": "5jeF8wMyZ9jnZ9_17253043342_1",
                    "updatedAt": "2023-04-28 10:09:04",
                    "createdAt": "2023-04-28 10:01:14",
                    "settlementId": null,
                    "amountSettled": null,
                    "refundMode": "-",
                    "settledOn": null,
                    "merchantUTR": null
                }
            ],
            "splitTransactionDetails": [
                {
                    "payuId": 12071315088,
                    "transactionDetails": {
                        "id": 12071315088,
                        "transactionId": "PB35163007S_1",
                        "status": "success",
                        "discount": 0.0,
                        "amount": 2259.0,
                        "transactionFee": 0.0,
                        "additionalCharges": 0.0,
                        "mode": "CASH",
                        "baseTxnId": 17253043342,
                        "firstName": "Masood",
                        "lastName": "Masood Ahmed Wani",
                        "addedOn": "2023-05-06 16:07:40",
                        "phone": "8448480680",
                        "email": "example@example.com",
                        "productInfo": "PBProduct",
                        "errorCode": "E000",
                        "ibiboCode": "FREC",
                        "merchantKey": "iDJYfd",
                        "errorMessage": "No Error",
                        "paymentSource": "payuS2S"
                    },
                    "transactionActionDetails": [
                        {
                            "id": 12071315088,
                            "bankRefNo": "5jeF8wMyZ9jnZ9_12031097474recon__1",
                            "token": "recon_17253043342",
                            "actionType": "refund",
                            "prevStatus": "requested",
                            "amount": 2259.0,
                            "status": "success",
                            "bankArn": "5jeF8wMyZ9jnZ9_12031097474recon__1",
                            "updatedAt": "2023-05-11 11:49:04",
                            "createdAt": "2023-05-06 16:07:40",
                            "settlementId": null,
                            "amountSettled": null,
                            "refundMode": "Back to Source",
                            "settledOn": null,
                            "merchantUTR": null
                        }
                    ]
                }
            ]
        }
    ]
}
```

#### Failure response

```json
{
  "status": 0,
  "msg": "0 out of 1 Transactions Fetched Successfully",
  "transaction_details": {
    "16988019552": "No action status found value of var1 sent in the request"
  }
}
```