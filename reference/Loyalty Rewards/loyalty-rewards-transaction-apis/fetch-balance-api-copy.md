---
title: Transaction Notify API
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
The **Transactoin Notify** API is used to  notify transaction status , and redeem/earn loyalty points.

HTTP Method: **POST**

### Endpoint

|            |                                                             |
| :--------- | :---------------------------------------------------------- |
| Production | \<https://apitest.payu.in/loyalty-points/points/v1/transact> |
|            |                                                             |

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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>\`LPX</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>txnAmount<br><code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The transaction amount after discounts and loyalty point reductions.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>900</code></p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>orderAmount<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The total order amount before applying any discounts or loyalty points.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>1000</code></p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>status<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Transaction status indicating success or failure.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>&quot;SUCCESS&quot; or &quot;FAILED&quot;</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>pgPaymentId<br><code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Payment gateway ID. For example, IDs for Razorpay or PayU.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>&quot;31234124234234&quot;</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>orderId<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Unique identifier for the order assigned by the merchant.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>&quot;merchantTxnId&quot;</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>loyaltyRefId<br><code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Reference ID for the loyalty transaction.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>&quot;504&quot;</p>
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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>redemptionDetails<br><code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Details of redemption, including key and points redeemed.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{ &quot;redeemLoyaltyKey&quot;: &quot;test@lzbevLxNILTS&quot;, &quot;redeemPoints&quot;: 100 }</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>earnDetails<br><code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Details regarding points earned in the transaction.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>{ &quot;earnLoyaltyKey&quot;: &quot;test@lzbevLxNILTS&quot;, &quot;earnPoints&quot;: 100, &quot;autoApply&quot;: true }</code></p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>paymentDetails<br><code>mandatory for seamless</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Includes payment method info such as card number.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>{ &quot;category&quot;: &quot;CREDITCARD&quot;, &quot;paymentCode&quot;: &quot;CC&quot;, &quot;cardNumber&quot;: &quot;4808550000000000&quot; }</code></p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>


### paymentDetails JSON field description

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
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>category</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Indicates the type or category of payment method being used. It can be any of the following:  </p>
<ul>
<li>CREDITCARD</li>
<li>DEBITCARD</li>
<li>NETBANKING</li>
</ul>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>paymentCode</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>A specific code representing the payment method; often used to facilitate backend processing.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>&quot;CC&quot;</code></p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>cardNumber</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The masked or partially visible card number used for the transaction, usually following PCI DSS standards.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>&quot;4808550000000000&quot;</code></p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>


## Sample request body

### Regular request body

````plaintext
Here's the formatted JSON:

```json
{
    "loyaltyProvider": "LPX",
    "txnAmount": 900,
    "orderAmount": 1000,
    "status": "SUCCESS/FAILED",
    "pgPaymentId": "31234124234234", // Example: razorpayid, payuid.
    "orderId": "merchantTxnId",
    "loyaltyRefId": "504",
    "userDetail": {
        "phoneNumber": "8901555****"
    },
    "redemptionDetails": {
        "redeemLoyaltyKey": "test@lzbevLxNILTS",
        "redeemPoints": 100
    },
    "earnDetails": {
        "earnLoyaltyKey": "test@lzbevLxNILTS",
        "earnPoints": 100,
        "autoApply": true // Default: false
    },
    "paymentDetails": {
        "cardBin": null,
        "cardHash": null,
        "cardMask": null,
        "category": "CREDITCARD",
        "isCollect": null,
        "paymentCode": "CC",
        "vpa": null,
        "cardNumber": "4808550000000000",
        "cardToken": null,
        "cardTokenType": null
    }
}
```
This formatted JSON aligns the elements clearly and maintains comments for context-specific details like examples and defaults. If there's anything else you need, feel free to ask! 😊
````

### Request with SKU

```
{
    "loyaltyProvider": "LPX",
    "txnAmount": 900,
    "orderAmount": 1000,
    "status": "SUCCESS/FAILED",
    "pgPaymentId": "31234124234234", // example: razorpyid, payuid.
    "orderId": "merchantTxnId",
    "loyaltyRefId": "504",
    "userDetail": {
        "phoneNumber": "8901555****"
    },
    "redemptionDetails": {
        "redeemLoyaltyKey": "test@lzbevLxNILTS",
        "redeemPoints": 100
    },
    "skusDetail": {
        "skus": [
            {
                "skuAmount": "1000.00",
                "skuOrderAmount": 1000,
                "quantity": "1",
                "skuId": "iphone",
                "earnConfig": {
                    "key": [],
                    "autoApply": "true", // Boolean
                    "earnPoints": null
                }
            }
        ]
    },
    // Payment details is mandatory in SEAMLESS mode,
    // Construct will be same as offer. because offer requires that.
    "paymentDetails": {
        "cardBin": null,
        "cardHash": null,
        "cardMask": null,
        "category": "CREDITCARD",
        "isCollect": null,
        "paymentCode": "CC",
        "vpa": null,
        "cardNumber": "4808550000000000",
        "cardToken": null,
        "cardTokenType": null
    }
}

```

<br />

## Sample response

### Success scenario

- Without order amount posted

```plaintext
{
    "orderId": "8878787",
    "loyaltyRefId": "534",
    "pgPaymentId": "31234124234234",
    "redemptionInfo": {
        "redeemLoyaltyKey": "Diamond@RUISebLORdLw",
        "redeemPoints": 100.0,
        "referenceId": "120"
    },
    // Earn on SKU
    "earnInfo": {
        "autoApply": true,
        "earnPoints": 200,
        "referenceId": "115"
    }
}

```

### Failure scenario

- Validation exception

```plaintext
{ 
"errorMessage":"Bad Request ", 
"errorType":"VALIDATION_EXCEPTION", 
"issueCode":"LS400_408" 
} 

```

- Session expired

```
{ 
    "issueCode": "LS404-401", 
    "errorMessage": "Session Expired unable to redeem points", 
    "errorType": "APPLICATION_EXCEPTION" 
}
```