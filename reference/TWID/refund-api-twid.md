---
title: Refund API - TWID
deprecated: false
hidden: false
metadata:
  robots: index
---
The **Refund** API is used to initiate a refund request for a loyalty-based transaction.

## Endpoint
\{\{loyalty-service-url}}/refund/v1

## Request parameters

<HTMLBlock>
{`
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
<td>parentTxnId <code>mandatory</code></td>
<td><code>String</code> - Parent PayU transaction ID</td>
<td><code>"bd1a77b6-1596-46e1-b79f-2770bcb636c7"</code></td>
</tr>
<tr>
<td>merchantReferenceId <code>mandatory</code></td>
<td><code>String</code> - Merchant reference ID</td>
<td><code>"56as67ds7678asd"</code></td>
</tr>
<tr>
<td>refundAmount <code>mandatory</code></td>
<td><code>Number</code> - Amount requested for refund</td>
<td><code>200</code></td>
</tr>
<tr>
<td>refundId <code>mandatory</code></td>
<td><code>String</code> - Unique refund ID</td>
<td><code>"4656526"</code></td>
</tr>
</tbody>
</table>
`}
</HTMLBlock>

## Sample request

### Non-seamless integration
```bash
curl -X POST "https://apitest.payu.in/loyalty-points/refund/v1" \
  -H "Content-Type: application/json" \
  -H "mid: YOUR_MERCHANT_ID" \
  -d '{
    "parentTxnId": "9090909090909111",
    "merchantReferenceId": "56as67ds7678asd",
    "refundAmount": 200,
    "refundId": "4656526"
  }'
```
### Seamless integration
```bash
curl -X POST "https://apitest.payu.in/loyalty-points/refund/v1" \
  -H "Content-Type: application/json" \
  -H "Date: Wed, 08 Sep 2025 13:22:43 GMT" \
  -H "Authorization: hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"GENERATED_SIGNATURE\"" \
  -d '{
    "parentTxnId": "9090909090909111",
    "merchantReferenceId": "56as67ds7678asd",
    "refundAmount": 200,
    "refundId": "4656526"
  }'
```
## Response parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| message | `String` - Status message of the refund request | `"Queued"` |
| loyaltyRefundId | `String` - Loyalty refund ID for tracking | `"1213"` |

## Sample response
```json
{
  "message": "Queued",
  "loyaltyRefundId": "1213"
}
```

## Notes
- When the refund is queued, the status must be verified using the **Refund Status API** for confirmation
- The `loyaltyRefundId` returned should be used to check the refund status
