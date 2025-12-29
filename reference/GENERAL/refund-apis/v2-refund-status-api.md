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
            "payuId": 403993715535600711,
            "transactionDetails": {
                "id": 403993715535600711,
                "transactionId": "Txn_1198922289338911",
                "merchantKey": "a4vGC2",
                "merchantName": "SunitPayuTesting",
                "status": "captured",
                "discount": 0.00,
                "amount": 121.51,
                "transactionFee": 100.00,
                "additionalCharges": 21.51,
                "mode": "NB",
                "baseTxnId": 0,
                "firstName": "sartaj",
                "lastName": "",
                "addedOn": "2025-12-26 13:35:16",
                "phone": "9876543210",
                "email": "testv2@example.in",
                "productInfo": "string",
                "errorCode": "E000",
                "ibiboCode": "TESTPGNB",
                "address": "",
                "city": "Bharatpur",
                "zipcode": "321028",
                "cardNo": null,
                "cardType": null,
                "cardToken": null,
                "udf1": "Hello",
                "udf2": "udf2",
                "udf3": "udf3",
                "udf4": "udf4",
                "udf5": null,
                "field0": null,
                "field1": null,
                "field2": null,
                "field3": null,
                "field4": null,
                "field5": null,
                "field6": null,
                "field7": null,
                "field8": null,
                "field9": "Transaction Completed Successfully",
                "errorMessage": "No Error",
                "paymentSource": "payu",
                "partnerToken": null,
                "clearToken": false,
                "ccAvenueOrderid": null,
                "merchantUTR": null,
                "threeDsEci": null,
                "threeDSEnrolled": null,
                "threeDSStatus": null,
                "appName": null,
                "mcpLookupId": null,
                "mcpAmount": null,
                "mcpCurrency": null,
                "mcpExchangeRate": null,
                "rupayAuthRefNo": null,
                "originalCurrency": null,
                "curl": "https://test.payu.in/admin/test_response",
                "furl": "https://test.payu.in/admin/test_response",
                "surl": null,
                "state": null,
                "country": null,
                "bankRefNo": null,
                "ip": null,
                "issuingBank": null,
                "paymentGateway": null,
                "address2": null
            },
            "transactionActionDetails": [
                {
                    "id": 139128152,
                    "bankRefNo": null,
                    "token": "3528998",
                    "actionType": "refund",
                    "prevStatus": null,
                    "amount": 2.0,
                    "status": "queued",
                    "bankArn": null,
                    "updatedAt": "2025-12-26 15:44:07",
                    "createdAt": "2025-12-26 15:44:02",
                    "settlementId": null,
                    "amountSettled": null,
                    "refundMode": "Back to Source",
                    "settledOn": null,
                    "merchantUTR": null,
                    "merchantServiceFee": 0.0,
                    "merchantServiceTax": 0.0,
                    "successAmount": null
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
