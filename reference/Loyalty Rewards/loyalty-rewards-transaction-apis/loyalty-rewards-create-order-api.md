---
title: Create Order API
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
The **Create Order** API is used to create order against **orderId** in the Loyalty Rewards integration.

HTTP Method: **POST**

### Endpoint

|            |                                                          |
| :--------- | :------------------------------------------------------- |
| Production | \<https://apitest.payu.in/loyalty-points/points/v1/order> |
|            |                                                          |

## Request Parameters

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;">Parameter</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Example</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>loyaltyProvider<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>A static value which need to passed for LoyaltyPointClose Loop flow</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>&quot;LPX&quot;</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>orderId<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Identifier for the order</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>&quot;223234&quot;</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>orderAmount<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The total amount of the order</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>1000</p>
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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>userDetail<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The user details such as phone number</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{<br>        &quot;phoneNumber&quot;: &quot;8901555****&quot;<br>    }</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## Sample request Body

```plaintext
{
    "loyaltyProvider": "LPX",
    "orderId": "223234",
    "orderAmount": 1000,
    "txnAmount": 950,
    "userDetail": {
        "phoneNumber": "8901555****"
    }
}
```

## Sample response

### Success scenario

```plaintext
{
    "status": 1,
    "message": "Order created successfully!",
    "result": {
        "userDetail": {
            "userId": "1726853623d5babd27-98d2-4e5f-83f9-2deb1fe44efe",
            "phoneNumber": "8800108523",
            "entityTypeId": 2,
            "additionalDetail": null,
            "isLoyaltyEnrolled": false
        },
        "orderId": "657898761",
        "orderAmount": "1000",
        "loyaltyRefId": "896",
        "availablePoints": 800.00
    }
}
```

### Failure scenario

```plaintext
{ 
"errorMessage":"Bad Request ", 
"errorType":"VALIDATION_EXCEPTION", 
"issueCode":"LS400_408" 
} 
```