---
title: Fetch Balance API - TWID
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: Fetch Balance API - TWID
deprecated: false
hidden: true
metadata:
  robots: index
---
This API is used to fetch the user's reward point balance and its corresponding monetary savings for a specific loyalty provider.

## Environment

|            |                                                  |
| :--------- | :----------------------------------------------- |
| Test       | https://apitest.payu.in/loyalty-points/v1/balance |
| Production | https://api.payu.in/loyalty-points/v1/balance     |

HTTP method: **POST**

## Request header

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
<td>loyaltyProvider <code>mandatory</code></td>
<td><code>String</code> - Loyalty provider for the request</td>
<td><code>"TWID"</code></td>
</tr>
<tr>
<td>mobileNumber <code>mandatory</code></td>
<td><code>String</code> - User's mobile number used for identification</td>
<td><code>"88001085**"</code></td>
</tr>
<tr>
<td>fetchRevisedEarn <code>optional</code></td>
<td><code>Boolean</code> - Fetch revised earnings for Zilion</td>
<td><code>true</code></td>
</tr>
<tr>
<td>orderAmount <code>mandatory</code></td>
<td><code>Number</code> - Order amount for which reward points are applicable</td>
<td><code>1000</code></td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## Response parameters

| Parameter                 | Description                                                         | Example                                    |
| ------------------------- | ------------------------------------------------------------------- | ------------------------------------------ |
| loyaltyProvider           | `String` - The loyalty provider for the response                    | `"TWID"`                                   |
| usableAmount              | `Number` - Maximum monetary amount that can be saved                | `500.0`                                    |
| usablePoints              | `Number` - Required reward points for maximum savings               | `500`                                      |
| title                     | `String` - Display title of the reward offer                        | `"Save Rs 500 using 500 TWID Cash Points"` |
| earnConfig.points         | `Number` - Points that can be earned in this transaction            | `0`                                        |
| issuerDetailDTO.brandName | `String` - Brand name of the issuer                                 | `"TWID Cash"`                              |
| issuerDetailDTO.logo      | `String` - Logo URL of the brand or issuer                          | `"https://cdn.twidpay.com/..."`            |
| holdApplicable            | `Boolean` - Indicates if points can be held/reserved for the reward | `false`                                    |

## Sample request

### Non-seamless Integration

```bash
curl -X POST "https://apitest.payu.in/loyalty-points/v1/balance" \
  -H "Content-Type: application/json" \
  -H "mid: YOUR_MERCHANT_ID" \
  -d '{
    "loyaltyProvider": "TWID",
    "mobileNumber": "88001085**",
    "fetchRevisedEarn": true,
    "orderAmount": 1000
  }'
```

### Seamless Integration

```bash
curl -X POST "https://apitest.payu.in/loyalty-points/v1/balance" \
  -H "Content-Type: application/json" \
  -H "Date: Wed, 08 Sep 2025 13:22:43 GMT" \
  -H "Authorization: hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"GENERATED_SIGNATURE\"" \
  -d '{
    "loyaltyProvider": "TWID",
    "mobileNumber": "88001085**",
    "fetchRevisedEarn": true,
    "orderAmount": 1000
  }'
```

## Sample response

```json
{
  "loyaltyProvider": "TWID",
  "usableAmount": 500.0,
  "usablePoints": 500,
  "title": "Save Rs 500 using 500 TWID Cash Points",
  "earnConfig": { 
    "points": 0, 
    "amount": null, 
    "title": null 
  },
  "issuerDetailDTO": {
    "brandName": "TWID Cash",
    "logo": "https://cdn.twidpay.com/brand_logo.png",
    "issuerType": "brand"
  },
  "holdApplicable": false
}
```