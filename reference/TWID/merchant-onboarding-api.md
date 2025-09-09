---
title: Merchant Onboarding API
deprecated: false
hidden: true
metadata:
  robots: index
---
The Merchant Onboarding API is used to onboard new merchants on the Twid platform.

## Environment

|            |                                                                            |
| :--------- | :------------------------------------------------------------------------- |
| Production | \{\{loyalty-service-url}}/merchant/v1                                      |
| Test       | [https://apitest.payu.in/merchant/v1](https://apitest.payu.in/merchant/v1) |

## Request header

### For non-seamless integration

* **Mandatory Header**: `mid`

### For seamless integration

<V2_paymentHeader />

<br />

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
<td>payuMerchantKey <code>mandatory</code></td>
<td><code>String</code> - PayU Merchant Key</td>
<td><code>"BCRVuw324"</code></td>
</tr>
<tr>
<td>payuMerchantId <code>mandatory</code></td>
<td><code>String</code> - PayU-assigned merchant ID</td>
<td><code>"12711755234"</code></td>
</tr>
<tr>
<td>name <code>mandatory</code></td>
<td><code>String</code> - Merchant name</td>
<td><code>"MerchantName"</code></td>
</tr>
<tr>
<td>category <code>mandatory</code></td>
<td><code>String</code> - Merchant category</td>
<td><code>"Merchant Category"</code></td>
</tr>
<tr>
<td>companyName <code>mandatory</code></td>
<td><code>String</code> - Merchant's company name</td>
<td><code>"Company name"</code></td>
</tr>
<tr>
<td>email <code>mandatory</code></td>
<td><code>String</code> - Merchant's email address</td>
<td><code>"test123@gmail.com"</code></td>
</tr>
<tr>
<td>phone <code>mandatory</code></td>
<td><code>String</code> - Merchant's phone number</td>
<td><code>"9999999999"</code></td>
</tr>
<tr>
<td>active <code>mandatory</code></td>
<td><code>Integer</code> - Merchant status (1 = Active, 0 = Inactive)</td>
<td><code>1</code></td>
</tr>
<tr>
<td>loyaltyProvider <code>mandatory</code></td>
<td><code>String</code> - Loyalty provider (e.g., TWID)</td>
<td><code>"TWID"</code></td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## Sample request

### Non-seamless integration

```bash
curl -X POST "https://apitest.payu.in/loyalty-points/merchant/v1" \
  -H "Content-Type: application/json" \
  -H "mid: YOUR_MERCHANT_ID" \
  -d '{
    "payuMerchantKey": "BCRVuw324",
    "payuMerchantId": "12711755234",
    "name": "MerchantName",
    "category": "Merchant Category",
    "companyName": "Company name",
    "email": "test123@gmail.com",
    "phone": "9999999999",
    "active": 1,
    "loyaltyProvider": "TWID"
  }'
```

### Seamless integration

```bash
curl -X POST "https://apitest.payu.in/loyalty-points/merchant/v1" \
  -H "Content-Type: application/json" \
  -H "Date: Wed, 08 Sep 2025 13:22:43 GMT" \
  -H "Authorization: hmac username="YOUR_MERCHANT_KEY", algorithm="sha512", headers="date", signature="GENERATED_SIGNATURE"" \
  -d '{
    "payuMerchantKey": "BCRVuw324",
    "payuMerchantId": "12711755234",
    "name": "MerchantName",
    "category": "Merchant Category",
    "companyName": "Company name",
    "email": "test123@gmail.com",
    "phone": "9999999999",
    "active": 1,
    "loyaltyProvider": "TWID"
  }'
```

## Response parameters

| Parameter          | Description                                                            | Example                                    |
| ------------------ | ---------------------------------------------------------------------- | ------------------------------------------ |
| loyaltyMerchantKey | `String` - Unique key assigned to the merchant for loyalty integration | `"LS309b6df5-4740-4459-889f-ea4b261d3d2a"` |
| msg                | `String` - The outcome message of the API call                         | `"SUCCESS"`                                |

## Sample response

```json
{
  "loyaltyMerchantKey": "LS309b6df5-4740-4459-889f-ea4b261d3d2a",
  "msg": "SUCCESS"
}
```