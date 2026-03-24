---
title: 'Refund Initiation API '
deprecated: false
hidden: false
metadata:
  robots: index
---
The **Refund Initiation** API allows merchants to initiate refunds for transactions. Its functionally similar to the v1 **Cancel Refund Transaction** API, but is maintained only for backward compatibility with existing integrations. The v2 API offers enhanced functionality and improved response formats compared to the v1 API.

**Endpoint**

|                        |                                                                                                          |
| :--------------------- | :------------------------------------------------------------------------------------------------------- |
| Production Environment | [https://secure.payu.in/v2/refund/](https://secure.payu.in/v2/refund/)                                   |
| Test Environment       | [https://apitest.payu.in/refund/v1/refundInitiation](https://apitest.payu.in/refund/v1/refundInitiation) |

## Request header

<V2_payment_header_params />

## Request body

<HTMLBlock>{`
<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Description</th>
      <th>Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>payuId<br/><code>mandatory</code></td>
      <td><code>String</code> The unique PayU transaction identifier for which the refund is being initiated.</td>
      <td>9999999900009081231239182</td>
    </tr>
    <tr>
      <td>token<br/><code>mandatory</code></td>
      <td><code>String</code> Unique token identifier for the refund request.</td>
      <td>test_3</td>
    </tr>
    <tr>
      <td>amount<br/><code>mandatory</code></td>
      <td><code>Number</code> The refund amount to be processed.</td>
      <td>6</td>
    </tr>
    <tr>
      <td>source<br/><code>optional</code></td>
      <td><code>Number</code> Source identifier for the refund initiation request.</td>
      <td>1</td>
    </tr>
    <tr>
      <td>merchantCallbackUrl<br/><code>optional</code></td>
      <td><code>String</code> URL where PayU sends the merchant callback for this refund.</td>
      <td>https://merchant.example.com/refund/callback</td>
    </tr>
    <tr>
      <td>customerPhone<br/><code>optional</code></td>
      <td><code>String</code> This will the customer's phone number against which wallet is created. It must be 10-digit mobile number</td>
      <td>8127531459</td>
    </tr>
    <tr>
      <td>refundDetails<br/><code>optional</code></td>
      <td><code>Object</code> This field tells that refund should be process into customer's wallet instead of original back to source account. It must include the <code>refundType</code> field with the value as "wallet".</td>
      <td><code>{"refundType": "wallet"}</code></td>
    </tr>
    <tr>
      <td>refundSplitRequest<br/><code>optional</code></td>
      <td><code>Object</code> Information for split refund requests when applicable.</td>
      <td>null</td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

## Sample request

<Callout icon="📘" theme="info">
  **Note**: The following sample request is for Test Environment.
</Callout>

```curl
curl --location 'http://apitest.payu.in/refund/v1/refundInitiation' \
--header 'Authorization: hmac username="a4vGC2", algorithm="sha512", headers="date", signature="f861738a3b1c73230d0352e4b8eaa47d4140912011f5e6768d7a8307edb59f2adeb226559128239193ade16ee4ad1b646e414e27435cb70e236361f25e03482c"' \
--header 'date: Mon, 29 Dec 2025 09:45:14 GMT' \
--header 'Content-Type: application/json' \
--data '{
    "payuId": "403993715535614124",
    "amount": 100,
    "refundToken": "435239928",
    "source": 1,
    "merchantCallbackUrl": "https://merchant.example.com/refund/callback",
    "var1Type": "REWARD_REFUND"
}'
 
```

### Refund Initiation for Wallets

```curl
curl --location 'http://10.248.8.237:9095/refund/v1/refundInitiation' \
--header 'Content-Type: application/json' \
--header 'mid: 180012' \
--data '{
    "payuId": "99999000000592959",
    "amount":6,
    "refundToken": "test_3",
    "source": 1,
    "merchantCallbackUrl": "https://merchant.example.com/refund/callback",
    "customerPhone": "8127531459",
    "refundDetails": {
        "refundType": "wallet"
    }
}'
```

<br />

### Refund Initiaition With Split Settlements

```curl
curl --location 'http://apitest.payu.in/refund/v1/refundInitiation' \
--header 'Content-Type: application/json' \
--header 'mid: 8006653' \
--data '{
    "payuId": "999000000000478",
    "refundToken": "a*bv***w",
    "amount": 0.21,
    "refundSplitRequest": {
        "33rOiT": {
            "amount": 0.21
        }
    }
}'
```

## Response parameters

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

* General transaction

```json
{
    "status": 1,
    "statusCode": 102,
    "message": "Refund request accepted",
    "payuId": 403993715535614124,
    "requestId": "139136064",
    "refundToken": "435239928"
}
```

* With Split Settlements
  ```
  {
    "message": "Success",
    "status": 1,
    "result": [
      {
        "payuId": "999000000000478",
        "refundToken": "abb342vqw",
        "status": 1,
        "message": "Success",
        "splitInfo": {
          "33rOiT": {
            "status": 1,
            "statusCode": "102",
            "message": "Refund request accepted",
            "requestId": "4993824108553"
          }
        }
      }
    ]
  }

  ```
  ###

#### Failure Response

Any of the following response is displayed when the refund request is rejected:

```
{
    "status": 0,
    "statusCode": 106,
    "message": "Error code 106",
    "payuId": 403993715535614400,
    "refundToken": "43221129280909"
}
```

<br />

```
{
    "status": 0,
    "statusCode": 231,
    "message": "Error code 231",
    "payuId": 403993715535614400,
    "refundToken": "43221129280909"
}
```

<br />

```
{
    "status": 0,
    "statusCode": 214,
    "message": "Error code 214",
    "payuId": 403993715535614400,
    "refundToken": "43221129280909"
}
```

## Error Codes

| ID | status_code | Description                                                                                                  |
| -- | ----------- | ------------------------------------------------------------------------------------------------------------ |
| 1  | 100         | SUCCESS                                                                                                      |
| 2  | 101         | PENDING                                                                                                      |
| 3  | 102         | QUEUED                                                                                                       |
| 4  | 103         | REJECT - Request rejected on reconfirmation                                                                  |
| 5  | 104         | RECONFIRM - Confirmation required                                                                            |
| 6  | 105         | Refund FAILURE - Invalid amount                                                                              |
| 7  | 106         | Refund FAILURE - Token already exists.                                                                       |
| 8  | 107         | Refund FAILURE - Upgraded to refund                                                                          |
| 9  | 108         | Refund FAILURE                                                                                               |
| 10 | 109         | Refund FAILURE - Request is already logged                                                                   |
| 11 | 110         | Refund FAILURE - More than one partial refund of Maestro transactions are not allowed                        |
| 12 | 111         | Refund FAILURE - Invalid transaction status                                                                  |
| 13 | 112         | RISK_QUEUED                                                                                                  |
| 14 | 113         | Refund FAILURE - Invalid Amount - Chargeback of amount present                                               |
| 15 | 115         | Refund FAILURE - Invalid status to be updated                                                                |
| 16 | 116         | Refund FAILURE - Transaction Not Found                                                                       |
| 17 | 117         | Refund FAILURE - Amount Does not Match                                                                       |
| 18 | 119         | Refund FAILURE - No such Request Found                                                                       |
| 19 | 120         | Refund FAILURE - Transaction lock could not be obtained.                                                     |
| 20 | 121         | Refund FAILURE - Incorrect/Empty value passed in retry                                                       |
| 21 | 122         | APPROVAL PENDING                                                                                             |
| 22 | 123         | Refund FAILURE - Request set as pending - requires manual follow-up                                          |
| 23 | 124         | Refund FAILURE - Input Data missing                                                                          |
| 24 | 125         | Refund FAILURE - Merchant Failed the pending refund                                                          |
| 25 | 126         | IN_PROGRESS                                                                                                  |
| 26 | 127         | REQUESTED                                                                                                    |
| 27 | 128         | Refund FAILURE - Partial refunds not allowed                                                                 |
| 28 | 129         | Refund FAILURE - Remark is mandatory for retry 0                                                             |
| 29 | 130         | Refund FAILURE - Refunds not allowed after                                                                   |
| 30 | 214         | Refund FAILURE - Two refunds of same amount for same transaction within 5 minutes are not allowed            |
| 31 | 225         | PENDING - Overdraft has occurred. Kindly recheck the status tomorrow.                                        |
| 32 | 226         | PENDING - Capture has been initiated today. Please check for refund status tomorrow.                         |
| 33 | 227         | Refund FAILURE - Transactions with same amount and same token not allowed                                    |
| 34 | 230         | Refund FAILURE - Purged Transaction. Refund request requires manual follow-up                                |
| 35 | 231         | Refund could not be initiated due to some internal error                                                     |
| 36 | 232         | Refund FAILURE - Refund could not be initiated. Either refunds are not supported or need manual intervention |
| 37 | 233         | BLOCKED - Refund/Cancel Blocked From Merchant Panel. Contact KM.                                             |
| 38 | 234         | BLOCKED - Refund/Cancel Blocked From Merchant Panel And API. Contact KM.                                     |
| 39 | 235         | BLOCKED - Refund/Cancel Blocked. Contact KM.                                                                 |
| 40 | 236         | Refund FAILURE - Refund not possible on this transaction                                                     |
| 41 | 237         | Validation Failure for \{key_name}. Special Characters Not Allowed                                           |
| 42 | 238         | Validation Failure for \{key_name}. Mandatory Field.                                                         |
| 43 | 239         | API based alternate instant refunds not activated.                                                           |
| 44 | 240         | Refund FAILURE - Store card failed                                                                           |
| 45 | 241         | Refund is not supported by the bank because the payment is more than days.                                   |
| 46 | 242         | Refund FAILURE - Bank Code Not Supported. Raise it to PayU support team                                      |
| 47 | 243         | Virtual account setup to process instant refund is incomplete                                                |
| 48 | 244         | Beneficiary Code for Virtual Account Not Set                                                                 |
| 49 | 245         | BBPS transaction is not successful                                                                           |
| 50 | 246         | value is Invalid for the Merchant SKU.                                                                       |
| 51 | 247         | not allowed as no offers found for the SKU.                                                                  |
| 52 | 248         | BAL_CHECK_INIT                                                                                               |
| 53 | 249         | RETRY                                                                                                        |
| 54 | 250         | Refund FAILURE - Refund Failed On Uploading Successful Chargeback                                            |
| 55 | 251         | Refund Blocked for this PGMID by Bank                                                                        |
| 56 | 252         | Refund FAILURE - Refunds are not allowed from panel for this MID                                             |
| 57 | 253         | Refund FAILURE - Instant refunds invalid mode                                                                |
| 58 | 254         | Refund FAILURE - Remarks cannot contain special characters                                                   |
| 59 | 255         | Refund FAILURE - Token Length Exceeded for Refund                                                            |
| 60 | 256         | Refund FAILURE - Refund not supported on split transactions. Please initiate refund on the order transaction |
| 61 | 258         | initiated                                                                                                    |
| 62 | 259         | REQUESTED_RETRY                                                                                              |
| 63 | 261         | Refund FAILURE - Error while processing request                                                              |
| 64 | 262         | Refund FAILURE - Error while processing request                                                              |
| 65 | 263         | Refund FAILURE - Invalid requested amount                                                                    |
| 66 | 264         | Refund FAILURE - Error while processing request                                                              |
| 67 | 265         | Refund FAILURE - Error while processing request                                                              |
| 68 | 266         | Refund FAILURE - Chargeback is pending against this transaction                                              |
| 69 | 267         | Refund FAILURE - Lock acquired on TransactionMetaData                                                        |
| 70 | 299         | Refund FAILURE - Blocking refund initiation for Type A Merchant                                              |
| 71 | 301         | Refund FAILURE - Capture already successful for this transaction                                             |
| 72 | 302         | Refund FAILURE - Please try after some time                                                                  |
| 73 | 303         | Refund FAILURE - Amount greater than maximum capturable amount                                               |
| 74 | 304         | Refund FAILURE - Amount less than allowed                                                                    |
| 75 | 305         | Refund FAILURE - Amount more than allowed                                                                    |
| 76 | 306         | Refund FAILURE - Invalid amount tolerance configuration                                                      |
| 77 | 424         | Refund FAILURE - Transaction upgraded to capture/refund.                                                     |
| 78 | 500         | Refund FAILURE - Some Exception Occurred.                                                                    |
| 79 | 501         | Successfully Updated                                                                                         |
| 80 | 502         | Failed to update                                                                                             |
| 81 | 270         | FAILURE - Transaction not eligible for Instant Refund                                                        |
