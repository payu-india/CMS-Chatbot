---
title: '[OLD]Create a Payment Link API'
excerpt: 'Resource: **payment-links**'
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The** Create a Payment Link** API is used to create a payment link for your customer.

HTTP Method: **POST**

**Environment**

<table><tbody><tr><td><strong>Test Environment</strong></td><td>https://uat-accounts.payu.in/payment-links</td></tr><tr><td><strong>Production Environment</strong></td><td>https://accounts.payu.in/payment-links</td></tr></tbody></table>

## Request headers

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "0-0": "mid  \n**mandatory**",
    "0-1": "`String` This contains the merchant identifier.",
    "1-0": "Authorization  \n**mandatory**",
    "1-1": "Bearer `String` This contains the client\\_token. For getting a token, refer to [Get Token API](ref:get-token-api-payment-links)."
  },
  "cols": 2,
  "rows": 2,
  "align": [
    null,
    null
  ]
}
[/block]


## Request parameters

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "subAmount  \n**mandatory**",
    "0-1": "`double` This parameter must contain the payment amount. The value must be greater than 1.",
    "0-2": "1000",
    "1-0": "description  \n**mandatory**",
    "1-1": "`String` This parameter must contain the description or purpose of creating the.payment link.",
    "1-2": "Car Insurance Premium",
    "2-0": "invoiceNumber  \n**optional**",
    "2-1": "`String` This parameter contains the unique string which is used for identifying a payment link. This must be alphanumeric.",
    "2-2": "INV8446471886220",
    "3-0": "expiryDate  \n**optional**",
    "3-1": "`String` This parameter contains the expiry date of the payment link. This is strictly in yyyy-MM-dd HH:mm:ss format (will be 365 days in all other cases).",
    "3-2": "2012-11-21 22:11:11",
    "4-0": "tax  \n**optional**",
    "4-1": "`double` This parameter contains the tax amount for the payment transaction. This value must be greater than zero.",
    "4-2": "10",
    "5-0": "shippingCharge  \n**optional**",
    "5-1": "`double` This parameter contains the shipping charges for delivering the goods. This value must be greater than zero.",
    "5-2": "25",
    "6-0": "source  \n**mandatory**",
    "6-1": "`String` This parameter contains the source of payment generation.",
    "6-2": "API",
    "7-0": "isPartialPaymentAllowed  \n**optional**",
    "7-1": "`Boolean` This parameter contains any of the following values to specify whether for partial payment is enabled:  \n   - **true**-The part payment is enabled  \n   - **false**-The part payment is not enabled",
    "7-2": "true",
    "8-0": "maxPaymentsAllowed  \n**optional**",
    "8-1": "`Integer` This parameter is used to specify the number of payments that can be accepted on a link.",
    "8-2": "25",
    "9-0": "customer.name  \n**optional**",
    "9-1": "`String` This field contains the customer name for whom the payment link is created.",
    "9-2": "Ashish",
    "10-0": "customer.email  \n**optional**",
    "10-1": "`String` This field contains the customer email to which the created payment link is sent.",
    "10-2": "[ashish1234@gmail.com](mailto:ashish1234@gmail.com)",
    "11-0": "customer.phone  \n**optional**",
    "11-1": "`String` This field contains the customer phone number to which the payment link needs to be sent.",
    "11-2": "9876543210",
    "12-0": "address  \n**optional**",
    "12-1": "`JSON` This parameter contains the customer address to which the goods are delivered.",
    "12-2": "H.No- 17, Block C, Kalyan Bldg, Khardilkar Road, Mumbai",
    "13-0": "udf1 - udf5  \n**optional**",
    "13-1": "`String` User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5. Maximum character limit for this parameter is: `255`",
    "13-2": " ",
    "14-0": "minAmountForCustomer  \n**optional**",
    "14-1": "`Double` This parameter contains the minimum amount a customer needs to pay in case of partial payment.",
    "14-2": "800",
    "15-0": "isAmountFilledByCustomer  \n**optional**",
    "15-1": "`boolean` This parameter contains any of the following values to specify whether it is an open invoices (when customer fills amount) or fixed amount:  \n    - **true**-It is an open invoice where the customer can fill the amount. The subamount parameter must be null in this case  \n    - **false**-It is closed invoice and amount is fixed",
    "15-2": "false",
    "16-0": "currency  \n**optional**",
    "16-1": "`String` This parameter contains the currency used.",
    "16-2": "Rupee",
    "17-0": "viaEmail  \n**optional**",
    "17-1": "`Boolean` This parameter contains any of the following values to specify whether to directly send an email to customer upon payment link generation or later:  \n    - **true**-The payment link is sent to the email upon generation  \n    - **false**-The payment link is not sent to the email upon generation",
    "17-2": "true",
    "18-0": "viaSms  \n**optional**",
    "18-1": "`Boolean` This parameter contains any of the following values to specify whether to directly send as SMS to customer upon payment link generation or later:  \n   - **true**-The payment link is sent as SMS upon generation  \n    - **false**-The payment link is not sent as email upon generation",
    "18-2": "true"
  },
  "cols": 3,
  "rows": 19,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


## Sample request

```curl
curl --location -g --request POST 'https://uatoneapi.payu.in/payment-links/' \
--header 'merchantId: {{merchantId}}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{access_token}}' \
--data-raw '{
"subAmount":2,
"isPartialPaymentAllowed":false,
"description":"paymentLink for testing",
"source":"API"
}'
```
```python
import http.client
import json

conn = http.client.HTTPSConnection("{{baseUrl}}")
payload = json.dumps({
  "subAmount": 2,
  "isPartialPaymentAllowed": False,
  "description": "paymentLink for testing",
  "source": "API"
})
headers = {
  'merchantId': '{{merchantId}}',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer {{access_token}}'
}
conn.request("POST", "/payment-links/", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```
```javascript
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\r\n\"subAmount\":2,\r\n\"isPartialPaymentAllowed\":false,\r\n\"description\":\"paymentLink for testing\",\r\n\"source\":\"API\"\r\n}");
Request request = new Request.Builder()
  .url("{{baseUrl}}/payment-links/")
  .method("POST", body)
  .addHeader("merchantId", "{{merchantId}}")
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{access_token}}")
  .build();
Response response = client.newCall(request).execute();
```

## Sample response

### Success scenario

```
{
  "status": 0,
  "message": "paymentLink generated",
  "result": {
    "subAmount": 2,
    "tax": 0,
    "shippingCharge": 0,
    "totalAmount": 2,
    "invoiceNumber": "INV7711514022032",
    "paymentLink": "http://pp72.pmny.in/MIioqucT8hXV",
    "description": "paymentLink for testing",
    "active": true,
    "isPartialPaymentAllowed": false,
    "expiryDate": "2023-03-21 17:58:30",
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
    "emailStatus": "not opted",
    "smsStatus": "not opted"
  },
  "errorCode": null,
  "guid": null
}
```

### Failure scenario

```
{
  "status": -1,
  "message": "Invoice Number already exists. Please enter new invoice number.",
  "result": null,
  "errorCode": null,
  "guid": null
}
```