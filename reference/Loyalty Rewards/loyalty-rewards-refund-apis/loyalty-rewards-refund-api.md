---
title: Refund API
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
The **Refund** API is used to refund loyalty points for the Loyalty Rewards integration.

HTTP Method: **POST**

### Endpoint

|            |                                                           |
| :--------- | :-------------------------------------------------------- |
| Production | \<https://apitest.payu.in/loyalty-points/points/v1/refund> |
|            |                                                           |

## Request Parameters

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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>orderId<code> mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The unique identifier of the merchant&#39;s transaction.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>&quot;merchantTxnId&quot;</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>refundType<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Specifies whether the refund is partial or full.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>&quot;PARTIAL&quot;</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>refundAmount<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Amount to be refunded to the customer.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>1000</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>skuInfo<code> mandatory for SKUs</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Details of stock keeping units (SKUs) in the transaction. This parameter must contain the array of SKU details (skus as in example) For the description of the fields in <strong>skus</strong>, refer to<a href="skus-json-field-description"> skus JSON field description</a> .</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>&quot;skus&quot;: [<br>            {<br>                &quot;skuId&quot;: &quot;airpod&quot;,<br>                &quot;quantity&quot;: null,<br>                &quot;skuAmount&quot;: 900,<br>                &quot;skuOrderAmount&quot;: 1000<br>            }<br>]</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>refundId<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Unique identifier for the refund transaction. Optional identifier for tracking.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>&quot;refundId&quot;</p>
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

## Request body

```plaintext
{ 
  "refundType":"PARTIAL/FULL", 
  "refundAmount":1000, 
  "skuInfo":null, 
  "orderId": "merchantTxnId", 
  "refundId":"refundId" 
} 
```

## Sample response

### Success scenario

```plaintext
{
    "status": 1,
    "message": "Refund processed successfully",
    "refundInfo": {
        "referenceId": "1234", // loyalty-pg reference-id
        "adjustmentId": "adj1", // can be null
        "refundAmount": 110,
        "split": {
            "pgAmount": 100,
            "loyaltyPoint": 10,
            "loyaltyPointAmount": 10
        },
        "adjustment": {
            "loyaltyPoint": 10,
            "loyaltyPointAmount": 10
        }
    }
}
```

### Failure scenario

```
{ 
"errorMessage":"Bad Request ", 
"errorType":"APPLICATION_EXCEPTION", 
"issueCode":"LS500_508" 
} 
```