---
title: TWID Refund Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
The **Refund** API is used to initiate refund and **Refund Status** API used to check the status of refund for TWID API integration. This section describes the steps to integrate TWID Refund integration.

## Step 1: Initiate the refund
### Environment

|            |                                     |
| :--------- | :---------------------------------- |
| Production | \{\{loyalty-service-url}}/refund/v1 |

<Accordion title="Request parameters" icon="fa-info-table" />

**Request header**

**Request parameters**

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
`}</HTMLBlock>


<Accordion title="Request parameters" icon="fa-info-pay" />
**Non-seamless integration**

```bash
curl -X POST "{{loyalty-service-url}}/refund/v1" \
  -H "Content-Type: application/json" \
  -H "mid: YOUR_MERCHANT_ID" \
  -d '{
    "parentTxnId": "9090909090909111",
    "merchantReferenceId": "56as67ds7678asd",
    "refundAmount": 200,
    "refundId": "4656526"
  }'
```

**Seamless integration**

```bash
curl -X POST "{{loyalty-service-url}}/refund/v1" \
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


<Accordion title="Response details" icon="fa-info-table" />
**Response parameters**

| Parameter       | Description                                     | Example    |
| --------------- | ----------------------------------------------- | ---------- |
| message         | `String` - Status message of the refund request | `"Queued"` |
| loyaltyRefundId | `String` - Loyalty refund ID for tracking       | `"1213"`   |

**Sample response**

```json
{
  "message": "Queued",
  "loyaltyRefundId": "1213"
}
```

<Callout icon="📘" theme="info">
  **Notes:**

  * When the refund is queued, the status must be verified using the **Refund Status API** for confirmation.
  * The `loyaltyRefundId` returned should be used to check the refund status
</Callout>



## Step 2: Capture the loyaltyRefundId from the response

## Step 3: Check the status of the refund
