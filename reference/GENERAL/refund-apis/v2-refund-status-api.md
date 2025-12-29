---
title: Refund Status API
deprecated: false
hidden: false
metadata:
  title: Refund Status API
  robots: index
---
The **Refund Status** API for Split Payments provides a specialized mechanism for tracking refund statuses in split payment scenarios. It's designed for aggregator merchants who process payments divided among multiple recipients. Unlike the v1 API, this enhanced version provides complete visibility into parent-child transaction relationships, refund actions, and settlement details.

**Endpoint**

|                        |                                                                                  |
| :--------------------- | :------------------------------------------------------------------------------- |
| Test Environment       | https://apitest.payu.in/v2/refunds/status                                        |
| Production Environment | [https://info.payu.in/v2/refunds/status](https://info.payu.in/v2/refunds/status) |

## Request headers

<V2_payment_header_params />

### Request body

<Callout icon="📘" theme="info">
  **Note**: At least one of the following parameters must be provided: `requestId`, `payuId`, or `tokenId`.
</Callout>

<br />

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
        requestId<br/>
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
        payuId<br/>
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
        tokenId<br/>
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

## Sample request

```bash
curl --location 'https://apitest.payu.in/v2/refunds/status' \
--header 'Authorization: hmac username="a4vGC2", algorithm="sha512", headers="date", signature="de60f419117f667dda7a7c7f403474e4cd8aa7de3137f116ddfaac90cb6112148f20ef5fb5f470826dacb820c36fa74c95236e5bfbc2ab61cc03d9791a49dc35"' \
--header 'date: Mon, 29 Dec 2025 09:57:23 GMT' \
--header 'Info-Command: check_action_status' \
--header 'Content-Type: application/json' \
--data '{
    "requestId": [
        "139128152"
    ]
}'
```

<br />

## Response parameters

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

## Sample response

### Success response

* General use case

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

### Failure scenarios

* Transaction not found for normal merchant

```
{    "message": "Success",    "status": 1,    "result": []}
```

* Transaction not found for aggregator merchant

```
{    "message": "transaction does not exists",    "status": 0,    "traceId": "10.251.120.218-8081-1-24318369-1-1753192554.523"}
```

* Bad request

```
{    "timestamp": "2025-07-22T13:56:21.488+00:00",    "status": 400,    "error": "Bad Request",    "path": "/v1/transaction"}
```

* Invalid merchant

```
{    "message": "There is no merchant with this mid or key",    "request_id": "9d530d367c3b4e749c8f5c2f693d6e55"}
```

* Authentication failure

```
{    "message": "Unauthorized",    "request_id": "44303808ec378607cdf3ab352d7d0845"}
```

<br />
