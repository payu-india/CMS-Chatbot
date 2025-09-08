---
title: Enquire Transaction API - TWID
deprecated: false
hidden: true
metadata:
  robots: index
---
The **Enquire Transaction** API allows the merchant to verify the status of a specific loyalty transaction either using the `loyaltyTxnId` or `payuTxnId` parameter. Both parameters are optional but at least one must be provided. The use cases for this API are:

* Reconciliation or to confirm the final status of loyalty transactions
* Transaction status verification during payment processing

## Environment

|            |                                              |
| :--------- | :------------------------------------------- |
| Production | \{\{loyalty-service-url}}/payment/v1/enquiry |

HTTP Method: **POST**

## Request parameters

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
<td>loyaltyTxnId <code>optional</code></td>
<td><code>String</code> - Reference ID generated during \`Create Payment\` or \`Redeem TWID Points\` calls</td>
<td><code>"bd1a77b6-1596-46e1-b79f-2770bcb636c7"</code></td>
</tr>
<tr>
<td>payuTxnId <code>optional</code></td>
<td><code>String</code> - PayU transaction ID</td>
<td><code>"89887897898"</code></td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

<Callout icon="📘" theme="info">
  **Note**: At least one of the above parameters must be provided.
</Callout>

## Sample request

### Non-seamless integration

```bash
curl -X POST "{{loyalty-service-url}}/payment/v1/enquiry" \
  -H "Content-Type: application/json" \
  -H "mid: YOUR_MERCHANT_ID" \
  -d '{
    "loyaltyTxnId": "bd1a77b6-1596-46e1-b79f-2770bcb636c7",
    "payuTxnId": "89887897898"
  }'
```

### Seamless integration

```bash
curl -X POST "{{loyalty-service-url}}/payment/v1/enquiry" \
  -H "Content-Type: application/json" \
  -H "Date: Wed, 08 Sep 2025 13:22:43 GMT" \
  -H "Authorization: hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"GENERATED_SIGNATURE\"" \
  -d '{
    "loyaltyTxnId": "bd1a77b6-1596-46e1-b79f-2770bcb636c7",
    "payuTxnId": "89887897898"
  }'
```

## Response parameters

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
        status
      </td>

      <td>
        `String` - Transaction processing status. For example, SUCCESS, PENDING, or FAILED
      </td>

      <td>
        `"SUCCESS"`
      </td>
    </tr>

    <tr>
      <td>
        merchantKey
      </td>

      <td>
        `String` - Unique merchant key for tracking purposes
      </td>

      <td>
        `"123ParentMerchantKey"`
      </td>
    </tr>

    <tr>
      <td>
        loyaltyTxnId
      </td>

      <td>
        `String` - Reference ID used for the loyalty transaction
      </td>

      <td>
        `"1821b1e2-
        34dd-
        47e3-
        9b54-
        b56b9d352a6b"`
      </td>
    </tr>

    <tr>
      <td>
        payuTxnId
      </td>

      <td>
        `String` - PayU transaction ID linked to the loyalty transaction
      </td>

      <td>
        `"89887897898111"`
      </td>
    </tr>

    <tr>
      <td>
        amount
      </td>

      <td>
        `Number` - Amount being processed in the transaction
      </td>

      <td>
        `10.00`
      </td>
    </tr>

    <tr>
      <td>
        phoneNumber
      </td>

      <td>
        `String` - Masked mobile number of the user
      </td>

      <td>
        `"88001085**"`
      </td>
    </tr>

    <tr>
      <td>
        rewardPartnerRefId
      </td>

      <td>
        `String` - Partner reference ID used for reconciliation
      </td>

      <td>
        `"7251650385664368640"`
      </td>
    </tr>

    <tr>
      <td>
        checksum
      </td>

      <td>
        `String` - SHA-512 hash for validation and verification
      </td>

      <td>
        `"fdcd69afce1ac4910d89772
        7f9c2beb372b9569df7fcad37
        4be52ab1d6ee6588771783e0e1
        574c49dc40d65d8bca5baf4787
        f2515d4cba6ebf1dc1d859f98c8f"`
      </td>
    </tr>

    <tr>
      <td>
        issueCode
      </td>

      <td>
        `String` - Error code (for failure responses)
      </td>

      <td>
        `"LS404-401"`
      </td>
    </tr>

    <tr>
      <td>
        errorMessage
      </td>

      <td>
        `String` - Error description (for failure responses)
      </td>

      <td>
        `"Transaction details not present in the DB"`
      </td>
    </tr>

    <tr>
      <td>
        errorType
      </td>

      <td>
        `String` - Type of error (for failure responses)
      </td>

      <td>
        `"VALIDATION_EXCEPTION"`
      </td>
    </tr>
  </tbody>
</Table>

## Sample response

### Success scenario

```json
{
  "status": "SUCCESS",
  "merchantKey": "123ParentMerchantKey",
  "payuTxnId": "89887897898111",
  "loyaltyTxnId": "1821b1e2-34dd-47e3-9b54-b56b9d352a6b",
  "amount": 10.00,
  "phoneNumber": "88001085**",
  "rewardPartnerRefId": "7251650385664368640",
  "checksum": "fdcd69afce1ac4910d897727f9c2beb372b9569df7fcad374be52ab1d6ee6588771783e0e1574c49dc40d65d8bca5baf4787f2515d4cba6ebf1dc1d859f98c8f"
}
```

## Failure scenario

```json
{
  "issueCode": "LS404-401",
  "errorMessage": "Transaction details not present in the DB",
  "errorType": "VALIDATION_EXCEPTION"
}
```
