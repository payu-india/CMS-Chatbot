---
title: Hold TWID Points API
deprecated: false
hidden: true
metadata:
  robots: index
---
The **Hold TWID Points** API is used to hold (reserve) reward points for a specific transaction before proceeding to final payment.

## Environment

|            |                                                    |
| :--------- | :------------------------------------------------- |
| Production | \{\{loyalty-service-url}}/payment/v1/createPayment |

HTTP Method: **POST**

## Request header

<V2_paymentHeader />

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
<td>surl <code>optional</code></td>
<td><code>String</code> - Success URL after holding points</td>
<td><code>"http://api.payu.in/success"</code></td>
</tr>
<tr>
<td>furl <code>optional</code></td>
<td><code>String</code> - Failure URL after holding points</td>
<td><code>"http://api.payu.in/failure"</code></td>
</tr>
<tr>
<td>merchantKey <code>mandatory</code></td>
<td><code>String</code> - PayU merchant key for authentication</td>
<td><code>"18001"</code></td>
</tr>
<tr>
<td>parentPayuTxnId <code>mandatory</code></td>
<td><code>String</code> - Parent transaction ID from main payment transaction</td>
<td><code>"65646400234509041"</code></td>
</tr>
<tr>
<td>totalAmount <code>mandatory</code></td>
<td><code>Number</code> - Total monetary reward amount to be held/redeemed</td>
<td><code>1000</code></td>
</tr>
<tr>
<td>mobile <code>mandatory</code></td>
<td><code>String</code> - User's mobile number</td>
<td><code>"9304204**"</code></td>
</tr>
<tr>
<td>loyaltyProvider <code>mandatory</code></td>
<td><code>String</code> - Loyalty provider identifier</td>
<td><code>"TWID"</code></td>
</tr>
<tr>
<td>orderAmount <code>mandatory</code></td>
<td><code>Number</code> - Total order/bill amount for transaction</td>
<td><code>10000</code></td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## Sample request

### Non-seamless Integration

```bash
curl -X POST "\{\{loyalty-service-url}}/payment/v1/createPaymentt" \
  -H "Content-Type: application/json" \
  -H "mid: YOUR_MERCHANT_ID" \
  -d '{
    "surl": "http://api.payu.in/success",
    "furl": "http://api.payu.in/failure",
    "merchantKey": "18001",
    "parentPayuTxnId": "65646400234509041",
    "totalAmount": 1000,
    "mobile": "9304204**",
    "loyaltyProvider": "TWID",
    "orderAmount": 10000
  }'
```

### Seamless Integration

```bash
curl -X POST "\{\{loyalty-service-url}}/payment/v1/createPayment" \
  -H "Content-Type: application/json" \
  -H "Date: Wed, 08 Sep 2025 13:22:43 GMT" \
  -H "Authorization: hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"GENERATED_SIGNATURE\"" \
  -d '{
    "surl": "http://api.payu.in/success",
    "furl": "http://api.payu.in/failure",
    "merchantKey": "18001",
    "parentPayuTxnId": "65646400234509041",
    "totalAmount": 1000,
    "mobile": "9304204**",
    "loyaltyProvider": "TWID",
    "orderAmount": 10000
  }'
```

## Response parameters

| Parameter          | Description                                              | Example                                  |
| ------------------ | -------------------------------------------------------- | ---------------------------------------- |
| statusCode         | `Number` - Indicates successful transaction (1=success)  | `1`                                      |
| status             | `String` - Transaction status (PENDING, SUCCESS, FAILED) | `"PENDING"`                              |
| loyaltyTxnId       | `String` - Unique loyalty transaction ID for tracking    | `"d1dce98d-98ec-4b90-a7d8-853fee82a113"` |
| rewardPartnerRefId | `String` - Reference ID from the reward provider         | `null`                                   |

## Sample response

```json
{
  "statusCode": 1,
  "status": "PENDING",
  "loyaltyTxnId": "d1dce98d-98ec-4b90-a7d8-853fee82a113",
  "rewardPartnerRefId": null
}
```
