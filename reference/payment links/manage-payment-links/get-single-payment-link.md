---
title: Get Single Payment Link API
excerpt: 'Resource: **payment-links**'
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The Get Single Payment Link API is used to get a single payment link using the payment link invoice number.

HTTP Method: **GET**

**Environment**

|                        |                                                                                       |
| :--------------------- | :------------------------------------------------------------------------------------ |
| Test Environment       | \<[https://uatoneapi.payu.in/payment-links](https://uatoneapi.payu.in/payment-links)> |
| Production Environment | \<[https://oneapi.payu.in/payment-links](https://oneapi.payu.in/payment-links)>       |

> 📘 Note:
>
> The access token with the scope as **read_payment_links** is required on the header. For more information on getting the access token, refer to [Get Token API - Payment Links](ref:get-token-api-payment-links).

## Request headers

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;">Parameter</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>mid<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This contains the merchant identifier.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Authorization<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Bearer <code>String</code> This contains the client_token. For getting a token, refer to <a href="https://docs.payu.in/reference/get-token-api-payment-links">Get Token API - Payment Links</a> .</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## Path parameters

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Parameters</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Example</strong></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Id<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This parameter must contain the payment link invoice number.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>INV8446471886220</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## Sample request

```curl
curl --location --request GET 'https://uatoneapi.payu.in/payment-links/INV0063002462' \
--header 'merchantId: 8237550' \
--header 'Authorization: Bearer e53f7d25071e6c2e631a920f38b9dbceeb571d6aadaed7e100f55fc7dab110ff'
```

## Sample response

### Success scenario

```json
{
  "status": 0,
  "message": null,
  "result": {
    "summary": {
      "amountRequested": 2,
      "totalRevenue": 0,
      "totalViews": 0
    },
    "subAmount": 2,
    "tax": 0,
    "shippingCharge": 0,
    "totalAmount": 2,
    "totalAmountCollected": 0,
    "invoiceNumber": "INV8446471886220",
    "paymentLink": "http://pp72.pmny.in/4IwlctBtwp2V",
    "description": "paymentLink for testing",
    "active": true,
    "isPartialPaymentAllowed": false,
    "status": "active",
    "expiryDate": "2023-03-21T14:53:52.000+0530",
    "udf": {
      "udf1": null,
      "udf2": null,
      "udf3": null,
      "udf4": null,
      "udf5": null
    },
    "address": {
      "line1": null,
      "line2": null,
      "city": null,
      "state": null,
      "country": null,
      "zipCode": null
    },
    "addedOn": "2022-03-21T14:53:53.000+0530",
    "isAmountFilledByCustomer": false,
    "isScheduled": 0,
    "reminderCount": 0,
    "customAttributes": []
  },
  "errorCode": null,
  "guid": null
}
```

### Failure scenario

```json
{
  "status": -1,
  "message": "paymentLink not found",
  "result": null,
  "errorCode": null,
  "guid": null
}
```
