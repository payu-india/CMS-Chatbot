---
title: Fetch Balance API
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
The **Fetch Balalnce** API is used to fetch balance and loyalty points applicable on transaction.

HTTP Method: **POST**

### Endpoint

|            |                                                            |
| :--------- | :--------------------------------------------------------- |
| Production | \<https://apitest.payu.in/loyalty-points/points/v1/balance> |
|            |                                                            |

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
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>&quot;LPX&quot;</code></p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>orderAmount<br><code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Total monetary value of the order.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>1000</code></p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>userDetail<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Information related to the user involved in the transaction.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>{ &quot;phoneNumber&quot;: &quot;8901555****&quot; }</code></p>
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

```plaintext
{
    "loyaltyProvider": "LPX",
    "orderAmount": 1000,
    "userDetail": {
        "phoneNumber": "8901555****"
    },
    "skusDetail": {
        "skus": [
            {
                "skuId": "airpod",
                "quantity": null,
                "skuAmount": 900,
                "skuOrderAmount": 1000
            }
        ]
    }
}

```

## Sample response

### Success scenario

- Without order amount posted

```plaintext
{
    "status": 1,
    "message": "Loyalty Retrieved Successfully",
    "result": {
        "userDetail": {
            "userId": "newGene775a048-1796-41d7-bb11-d3315dcb0620",
            "phoneNumber": "8901555****",
            "entityTypeId": 180013,
            "isLoyaltyEnrolled": true,  // can be false if not onboarded on loyalty-service
            "additionalDetail": null
        },
        "availablePoints": 10000
    }
}

```

- With order amount

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
        "burnConfig": [
            {
                "loyaltyKey": "test2@qjyAe2YiDwbH",
                "loyaltyId": 1234,
                "title": "test 2",
                "description": "test 2",
                "tnc": "terms and conditions",
                "tncLink": null,
                "minTxnAmount": 100.0,
                "maxTxnAmount": 100000.0,
                "loyaltyPointDetail": {
                    "pointType": "PERCENTAGE",
                    "pointPercentage": 10,
                    "burnPoints": 10,
                    "burnPointsAmount": 10
                }
            }
        ],
        "pointsAmountConversion": {
            "amountToPointUnit": 100,
            "pointCurrency": "ponits/coins/rewards/brownies"
        },
        "availablePoints": 10000,
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

### Failure scenario

```plaintext
{ 

"errorMessage":"Bad Request ", 

"errorType":"APPLICATION_EXCEPTION", 

"issueCode":"LS500_508" 

} 
```