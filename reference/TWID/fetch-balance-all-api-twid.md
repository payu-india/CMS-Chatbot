---
title: Fetch Balance All API - TWID
excerpt: Fetch Balance All API - TWID
deprecated: false
hidden: false
metadata:
  robots: index
---
The **Fetch Balance All** API retrieves balance information from multiple specified loyalty providers.

## Endpoint
```
\{\{loyalty-service-url}}/v1/balance/all
```

## Request header


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
<td>loyaltyProviders <code>mandatory</code></td>
<td><code>Array</code> - Array of loyalty provider names to fetch rewards from</td>
<td><code>["TWID", "ZILLION"]</code></td>
</tr>
<tr>
<td>mobileNumber <code>mandatory</code></td>
<td><code>String</code> - User's mobile number (masked for privacy)</td>
<td><code>"88001085**"</code></td>
</tr>
<tr>
<td>orderAmount <code>mandatory</code></td>
<td><code>Number</code> - Order amount for which reward points are applicable</td>
<td><code>1000</code></td>
</tr>
</tbody>
</table>
`}
</HTMLBlock>

## Sample request

### Non-seamless integration
```bash
curl -X POST "https://apitest.payu.in/loyalty-points/v1/balance/all" \
  -H "Content-Type: application/json" \
  -H "mid: YOUR_MERCHANT_ID" \
  -d '{
    "loyaltyProviders": ["TWID", "ZILLION"],
    "mobileNumber": "88001085**",
    "orderAmount": 1000
  }'
```

### Seamless integration
```bash
curl -X POST "https://apitest.payu.in/loyalty-points/v1/balance/all" \
  -H "Content-Type: application/json" \
  -H "Date: Wed, 08 Sep 2025 13:22:43 GMT" \
  -H "Authorization: hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"GENERATED_SIGNATURE\"" \
  -d '{
    "loyaltyProviders": ["TWID", "ZILLION"],
    "mobileNumber": "88001085**",
    "orderAmount": 1000
  }'
```
## Response parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| data[].loyaltyProvider | `String` - Loyalty provider identifier for this response entry | `"TWID"` |
| data[].usableAmount | `Number` - Maximum monetary amount that can be saved | `500.0` |
| data[].usablePoints | `Number` - Required reward points for maximum savings | `500` |
| data[].title | `String` - Display title describing the reward offer | `"Save Rs 500 using 500 TWID Cash Points"` |
| data[].earnConfig.points | `Number` - Points that can be earned | `0` |
| data[].issuerDetailDTO.logo | `String` - Logo URL of the brand/issuer | `"https://cdn.twidpay.com/brand_logo.png"` |
| data[].holdApplicable | `Boolean` - Indicates if points can be held for the reward | `false` |
| data[].customErrorMessage | `String` - Error message for specific provider (if applicable) | `"Unable to process request for provider"` |



## Sample response
```json
{
  "data": [
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
        "logo": "https://cdn.twidpay.com/brand_image.png",
        "issuerType": "brand"
      },
      "holdApplicable": false
    },
    {
      "loyaltyProvider": "ZILLION",
      "customErrorMessage": "Unable to process request for provider",
      "usableAmount": null,
      "usablePoints": null
    }
  ]
}
```

