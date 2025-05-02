---
title: Add User API
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
The **Create Order** API is used to add a customer to your Loyalty Rewards program.

HTTP Method: **POST**

### Endpoint

|            |                                                         |
| :--------- | :------------------------------------------------------ |
| Production | &lt;https://apitest.payu.in/loyalty-points/points/v1/user&gt; |
|            |                                                         |

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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>A static identifier for the loyalty provider to facilitate the Close Loop flow.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>&quot;LPX&quot;</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>orderAmount<br><code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Represents the total monetary value of the order, affecting loyalty calculations.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>1000</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>userDetail<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>An object containing details about the user, such as the phone number.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{ &quot;phoneNumber&quot;: &quot;8901555****&quot; }</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>phoneNumber<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The customer phone number, used as a unique identifier in the loyalty system.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>8901555****</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## Sample request body

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
    "result": {
        "userDetail": {
            "userId": "17277864939c4f18a2-cbe5-4f85-bdb8-23b04d5fc1d3",
            "phoneNumber": "8901555****",
            "entityTypeId": 180012,
            "additionalDetail": null,
            "isLoyaltyEnrolled": false
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