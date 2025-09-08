---
title: Enquire Transaction API - TWID
deprecated: false
hidden: false
metadata:
  robots: index
---
This API allows the merchant to verify the status of a specific loyalty transaction either using the `loyaltyTxnId` or `payuTxnId` parameter. Both parameters are optional but at least one must be provided. The use cases for this API are:

* Reconciliation or to confirm the final status of loyalty transactions
* Transaction status verification during payment processing

\{\{loyalty-service-url}}/payment/v1/enquiry

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
curl -X POST "https://apitest.payu.in/loyalty-points/payment/v1/enquiry" \
  -H "Content-Type: application/json" \
  -H "mid: YOUR_MERCHANT_ID" \
  -d '{
    "loyaltyTxnId": "bd1a77b6-1596-46e1-b79f-2770bcb636c7",
    "payuTxnId": "89887897898"
  }'
```

### Seamless integration

```bash
curl -X POST "https://apitest.payu.in/loyalty-points/payment/v1/enquiry" \
  -H "Content-Type: application/json" \
  -H "Date: Wed, 08 Sep 2025 13:22:43 GMT" \
  -H "Authorization: hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"GENERATED_SIGNATURE\"" \
  -d '{
    "loyaltyTxnId": "bd1a77b6-1596-46e1-b79f-2770bcb636c7",
    "payuTxnId": "89887897898"
  }'
```

## Response parameters

| Parameter          | Description                                                                        | Example                                                                                                                              |
| ------------------ | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| status             | `String` - Transaction processing status. For example, SUCCESS, PENDING, or FAILED | `"SUCCESS"`                                                                                                                          |
| merchantKey        | `String` - Unique merchant key for tracking purposes                               | `"123ParentMerchantKey"`                                                                                                             |
| loyaltyTxnId       | `String` - Reference ID used for the loyalty transaction                           | `"1821b1e2-34dd-47e3-9b54-b56b9d352a6b"`                                                                                             |
| payuTxnId          | `String` - PayU transaction ID linked to the loyalty transaction                   | `"89887897898111"`                                                                                                                   |
| amount             | `Number` - Amount being processed in the transaction                               | `10.00`                                                                                                                              |
| phoneNumber        | `String` - Masked mobile number of the user                                        | `"88001085**"`                                                                                                                       |
| rewardPartnerRefId | `String` - Partner reference ID used for reconciliation                            | `"7251650385664368640"`                                                                                                              |
| checksum           | `String` - SHA-512 hash for validation and verification                            | `"fdcd69afce1ac4910d897727f9c2beb372b9569df7fcad374be52ab1d6ee6588771783e0e1574c49dc40d65d8bca5baf4787f2515d4cba6ebf1dc1d859f98c8f"` |
| issueCode          | `String` - Error code (for failure responses)                                      | `"LS404-401"`                                                                                                                        |
| errorMessage       | `String` - Error description (for failure responses)                               | `"Transaction details not present in the DB"`                                                                                        |
| errorType          | `String` - Type of error (for failure responses)                                   | `"VALIDATION_EXCEPTION"`                                                                                                             |

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