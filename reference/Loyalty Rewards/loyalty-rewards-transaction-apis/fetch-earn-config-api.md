---
title: Fetch Earn Config API
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
The **Fetch Earn Config** API is used to fetch loyalty earn point config on transaction.

HTTP Method: **POST**

### Endpoint

|            |                                                               |
| :--------- | :------------------------------------------------------------ |
| Production | \<https://apitest.payu.in/loyalty-points/points/v1/earnConfig> |
|            |                                                               |

## Request parameters

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Parameter</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Example</strong></th>
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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>orderAmount<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Total monetary value of the order.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>1000</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>userDetail<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Information related to the user involved in the transaction.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{ &quot;phoneNumber&quot;: &quot;8901555****&quot; }</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>txnAmount<br><code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The order amount that can be any of the following purposes:  </p>
<ul>
<li>discount</li>
<li>burn points amount</li>
</ul>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>900</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>isCampaignTncRequired<br><code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>To indicate if the campaign Terms &amp; Conditions required.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>true</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>skusDetail<br><code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Details of stock keeping units (SKUs) in the transaction. This parameter must contain the array of SKU details (skus as in example) For the description of the fields in <strong>skus</strong>, refer to<a href="skus-json-field-description"> skus JSON field description</a>.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> &quot;skus&quot;: [<br>            {<br>                &quot;skuId&quot;: &quot;airpod&quot;,<br>                &quot;quantity&quot;: null,<br>                &quot;skuAmount&quot;: 900,<br>                &quot;skuOrderAmount&quot;: 1000<br>            }<br>]</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>


### skus JSON field description

| **Parameter**  | **Description**                                           | **Example** |
| -------------- | --------------------------------------------------------- | ----------- |
| skuId          | Unique identifier for each SKU in the transaction.        | "airpod"    |
| quantity       | Number of units for the SKU, can be null if unquantified. | null        |
| skuAmount      | Total amount for each SKU unit.                           | 900         |
| skuOrderAmount | Order amount associated with each SKU.                    | 1000        |

## Sample request body

### Regular request

```
{ 
    "loyaltyProvider": "LPX", 
    "orderAmount": 1000,//Mandatory 
    "txnAmount":900 , 
    "isCampaignTncRequired":true , 
    "userDetail": { 
        "phoneNumber":"8901555****" 
    } 
} 
```

### Request with SKU details

```plaintext
{
    "loyaltyProvider": "LPX",
    "orderAmount": 1000, // Mandatory
    "txnAmount": 900,
    "userDetail": {
        "phoneNumber": "8901555****"
    },
    "skusDetail": {
        "skus": [
            {
                "skuId": "airpod",
                "quantity": null,
                "skuAmount": 1000,
                "skuOrderAmount": 1000
            }
        ]
    }
}

```

## Sample response

### Success scenario

- Without SKU

```
{
    "status": 1,
    "message": "Loyalty Retrieved Successfully",
    "result": {
        "userDetail": {
            "userId": "newGene775a048-1796-41d7-bb11-d3315dcb0620",
            "phoneNumber": "8901555****",
            "entityTypeId": 180013,
            "isLoyaltyEnrolled": true, // can be false if not onboarded on loyalty-service
            "additionalDetail": null
        },
        "mid": "8235901",
        "amount": "900",
        "orderAmount": "1000",
        "earnConfig": [
            {
                "isValid": true,
                "pointsExpiryDate": null,
                "loyaltyKey": "TestSeamlessCampaign@vtpuYAh4rIy6",
                "title": "TestSeamlessCampaign",
                "description": "Heading2",
                "tnc": "Body2",
                "minTxnAmount": 250.0,
                "maxTxnAmount": 50000.0,
                "validFrom": "2024-09-12 12:09:24",
                "validTo": "2034-09-12 12:09:24",
                "paymentMethods": {
                    "creditCard": null,
                    "debitCard": null,
                    "netBanking": null,
                    "wallet": null,
                    "clw": null,
                    "upi": null,
                    "emi": null,
                    "bnpl": null
                },
                "isAllPaymentMethodsAvailable": true,
                "loyaltyPointDetail": {
                    "pointType": "ABSOLUTE",
                    "earnPoints": 200.0,
                    "earnPointsAmount": 2.0
                }
            }
        ],
        "pointsAmountConversion": {
            "amountToPointUnit": 100,
            "pointCurrency": "Diamond",
            "pointIconUrl": "https://d24r6yy703ziu6.cloudfront.net/web/images/assets/loyalty/icons/coin.svg"
        },
        "pointExpiryDetails": {
            "loyaltyPoints": 1000,
            "days": 5
        },
        "pointsSummary": {
            "lifeTimeEarnPoints": 100.00,
            "lifeTimeEarnAmount": 2000.00,
            "lifeTimeBurnPoints": 10.00,
            "lifeTimeBurnAmount": 200.00
        }
    }
}

```

- With SKU

```plaintext
{
    "status": 1,
    "message": "Loyalty Retrieved Successfully",
    "result": {
        "userDetail": {
            "userId": "newGene775a048-1796-41d7-bb11-d3315dcb0620",
            "phoneNumber": "8901555****",
            "entityTypeId": 180013,
            "isLoyaltyEnrolled": true, // can be false if not onboarded on loyalty-service
            "additionalDetail": null
        },
        "mid": "8235901",
        "amount": "900",
        "orderAmount": "1000",
        "skusDetail": {
            "skus": [
                {
                    "skuId": "iphone",
                    "quantity": 1,
                    "skuAmount": 2500,
                    "suppressSkuQuantity": false,
                    "earnConfig": [
                        {
                            "reason": null,
                            "isValid": true,
                            "pointsExpiryDate": "2024-09-18",
                            "loyaltyKey": "SkuDuplicateTest@u78FEHQK6ZKF",
                            "title": "SkuDuplicateTest",
                            "description": "SkuDuplicateTest",
                            "tnc": "{\"text\":\"SkuDuplicateTest\\n\",\"html\":\"<p>SkuDuplicateTest</p>\",\"ops\":[{\"insert\":\"SkuDuplicateTest\\n\"}]}",
                            "minTxnAmount": 1000.0,
                            "maxTxnAmount": 1000000.0,
                            "validFrom": "2024-09-11 15:35:34",
                            "validTo": "2034-09-11 15:35:34",
                            "isSku": true,
                            "paymentMethods": {
                                "creditCard": [
                                    {
                                        "networks": [],
                                        "banks": [
                                            {
                                                "code": "ICICI",
                                                "title": "ICICI"
                                            }
                                        ],
                                        "title": null,
                                        "paymentCode": null,
                                        "handle": null
                                    }
                                ],
                                "debitCard": null,
                                "netBanking": null,
                                "wallet": null,
                                "clw": null,
                                "upi": null,
                                "emi": null,
                                "bnpl": null
                            },
                            "isAllPaymentMethodsAvailable": null,
                            "skuDetail": null,
                            "isAcrossSkuQuantity": null,
                            "loyaltyPointDetail": {
                                "pointType": "ABSOLUTE",
                                "earnPoints": 551.0,
                                "earnPointsAmount": 5.51
                            }
                        }
                    ],
                    "skuOrderAmount": 2500,
                    "earnFailureReason": null,
                    "earnIsValid": true
                },
                {
                    "skuId": "airpod",
                    "quantity": 1,
                    "skuAmount": 2500,
                    "suppressSkuQuantity": false,
                    "earnConfig": [
                        {
                            "reason": null,
                            "isValid": true,
                            "pointsExpiryDate": "2024-09-18",
                            "loyaltyKey": "SkuDuplicateTest@u78FEHQK6ZKF",
                            "title": "SkuDuplicateTest",
                            "description": "SkuDuplicateTest",
                            "tnc": "{\"text\":\"SkuDuplicateTest\\n\",\"html\":\"<p>SkuDuplicateTest</p>\",\"ops\":[{\"insert\":\"SkuDuplicateTest\\n\"}]}",
                            "minTxnAmount": 1000.0,
                            "maxTxnAmount": 1000000.0,
                            "validFrom": "2024-09-11 15:35:34",
                            "validTo": "2034-09-11 15:35:34",
                            "isSku": true,
                            "paymentMethods": {
                                "creditCard": [
                                    {
                                        "networks": [],
                                        "banks": [
                                            {
                                                "code": "ICICI",
                                                "title": "ICICI"
                                            }
                                        ],
                                        "title": null,
                                        "paymentCode": null,
                                        "handle": null
                                    }
                                ],
                                "debitCard": null,
                                "netBanking": null,
                                "wallet": null,
                                "clw": null,
                                "upi": null,
                                "emi": null,
                                "bnpl": null
                            },
                            "isAllPaymentMethodsAvailable": null,
                            "skuDetail": null,
                            "isAcrossSkuQuantity": null,
                            "loyaltyPointDetail": {
                                "pointType": "ABSOLUTE",
                                "earnPoints": 551.0,
                                "earnPointsAmount": 5.51
                            }
                        }
                    ],
                    "skuOrderAmount": 2500,
                    "earnFailureReason": null,
                    "earnIsValid": true
                }
            ]
        },
        "pointsAmountConversion": {
            "amountToPointUnit": 100,
            "pointCurrency": "Diamond",
            "pointIconUrl": "https://d24r6yy703ziu6.cloudfront.net/web/images/assets/loyalty/icons/coin.svg"
        },
        "pointExpiryDetails": null,
        "pointsSummary": null
    }
}

```

<br />

### Failure scenario

```plaintext
  { 
"errorMessage":"Bad Request ", 
"errorType":"APPLICATION_EXCEPTION", 
"issueCode":"LS500_508" 
} 
```