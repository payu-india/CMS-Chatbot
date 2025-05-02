---
title: Hold Points or Burn Points API
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The **Hold Points** API is used to hold points against **orderId** in the Loyalty Rewards integration.

HTTP Method: **POST**

### Endpoint

|            |                                                         |
| :--------- | :------------------------------------------------------ |
| Production | \<https://apitest.payu.in/loyalty-points/points/v1/hold> |
|            |                                                         |

## Request parameters

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;">Parameter</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Example*</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>loyaltyProvider<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Identifier for the loyalty service provider.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>&quot;LPX&quot;</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>redemptionDetail<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Details about the points being redeemed in the transaction.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>{&quot;redeemLoyaltyKey&quot;: &quot;Diamond@RUISebLORdLw&quot;, &quot;redeemPoints&quot;: 100}</code></p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>orderId<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>A unique identifier assigned to the order.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>&quot;8878787&quot;</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>orderAmount<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Total monetary value of the order.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>1000</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>loyaltyRefId<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Reference ID given for tracking the loyalty transaction.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>&quot;534&quot;</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>txnAmount<br><code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Amount transacted after applying loyalty points reductions.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>900</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>userDetail<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Information related to the user participating in the transaction.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>{&quot;phoneNumber&quot;: &quot;8901555****&quot;}</code></p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

<br />

## Sample request body

```plaintext
{
    "loyaltyProvider": "LPX",
    "orderId": "8878787",
    "orderAmount": 1000,
    "loyaltyRefId": "534",
    "txnAmount": 900,
    "userDetail": {
        "phoneNumber": "8901555****"
    },
    "redemptionDetails": {
        "redeemLoyaltyKey": "Diamond@RUISebLORdLw",
        "redeemPoints": 100
    }
}
```

## Sample response

### Success scenario

```plaintext
{
    "status": 1,
    "message": "Loyalty points used successfully",
    "result": {
        "orderId": "657898761",
        "orderAmount": "1000",
        "loyaltyRefId": "896",
        "burnReason": "Loyalty applied successfully",
        "earnCalculation": "TXN_AMOUNT",
        "burnConfig": [
            {
                "reason": "Loyalty applied successfully",
                "isValid": true,
                "pointsExpiryDate": null,
                "loyaltyKey": "Diamond@RUISebLORdLw",
                "title": "Diamond",
                "description": null,
                "tnc": null,
                "minTxnAmount": 100.0,
                "maxTxnAmount": 100000.0,
                "validFrom": null,
                "validTo": null,
                "isSku": false,
                "paymentMethods": null,
                "isAllPaymentMethodsAvailable": null,
                "skuDetail": null,
                "isAcrossSkuQuantity": null,
                "loyaltyPointDetail": {
                    "pointType": "ABSOLUTE",
                    "burnPoints": 100.0,
                    "burnPointsAmount": 1.0
                }
            }
        ],
        "pointsAmountConversion": {
            "amountToPointUnit": 100,
            "pointCurrency": "Diamond",
            "pointIconUrl": "https://d24r6yy703ziu6.cloudfront.net/web/images/assets/loyalty/icons/coin.svg"
        },
        "availablePoints": 800.00,
        "isBurnValid": true
    }
}
```

### Failure Scenario

- Customer is not onboarded

```plaintext
{
    "issueCode": "LS500-503",
    "errorMessage": "Customer is not onboarded on Loyalty-service",
    "errorType": "APPLICATION_EXCEPTION"
}
```

- Session expiry

```plaintext
{
    "issueCode": "LS404-401",
    "errorMessage": "Session Expired unable to redeem points",
    "errorType": "APPLICATION_EXCEPTION"
}
```