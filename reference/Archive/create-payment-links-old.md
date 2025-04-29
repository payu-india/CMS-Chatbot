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
The **Create a Payment Link** API is used to create a payment link for your customer.

HTTP Method: **POST**

**Environment**

<table><tbody><tr><td><strong>Test Environment</strong></td><td>https://uat-accounts.payu.in/payment-links</td></tr><tr><td><strong>Production Environment</strong></td><td>https://accounts.payu.in/payment-links</td></tr></tbody></table>

## Request headers

<Table>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        mid
        **mandatory**
      </td>

      <td>
        `String` This contains the merchant identifier.
      </td>
    </tr>

    <tr>
      <td>
        Authorization\
        **mandatory**
      </td>

      <td>
        Bearer `String` This contains the client\_token. For getting a token, refer to [Get Token API](ref:get-token-api-payment-links).
      </td>
    </tr>
  </tbody>
</Table>

## Request parameters

<Table>
  <thead>
    <tr>
      <th>
        **Parameter**
      </th>

      <th>
        **Description**
      </th>

      <th>
        **Example**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        subAmount
        **mandatory**
      </td>

      <td>
        `double` This parameter must contain the payment amount. The value must be greater than 1.
      </td>

      <td>
        1000
      </td>
    </tr>

    <tr>
      <td>
        description\
        **mandatory**
      </td>

      <td>
        `String` This parameter must contain the description or purpose of creating the.payment link.
      </td>

      <td>
        Car Insurance Premium
      </td>
    </tr>

    <tr>
      <td>
        invoiceNumber\
        **optional**
      </td>

      <td>
        `String` This parameter contains the unique string which is used for identifying a payment link. This must be alphanumeric.
      </td>

      <td>
        INV8446471886220
      </td>
    </tr>

    <tr>
      <td>
        expiryDate\
        **optional**
      </td>

      <td>
        `String` This parameter contains the expiry date of the payment link. This is strictly in yyyy-MM-dd HH:mm:ss format (will be 365 days in all other cases).
      </td>

      <td>
        2012-11-21 22:11:11
      </td>
    </tr>

    <tr>
      <td>
        tax\
        **optional**
      </td>

      <td>
        `double` This parameter contains the tax amount for the payment transaction. This value must be greater than zero.
      </td>

      <td>
        10
      </td>
    </tr>

    <tr>
      <td>
        shippingCharge\
        **optional**
      </td>

      <td>
        `double` This parameter contains the shipping charges for delivering the goods. This value must be greater than zero.
      </td>

      <td>
        25
      </td>
    </tr>

    <tr>
      <td>
        source\
        **mandatory**
      </td>

      <td>
        `String` This parameter contains the source of payment generation.
      </td>

      <td>
        API
      </td>
    </tr>

    <tr>
      <td>
        isPartialPaymentAllowed\
        **optional**
      </td>

      <td>
        `Boolean` This parameter contains any of the following values to specify whether for partial payment is enabled:  

        * **true**-The part payment is enabled  
        * **false**-The part payment is not enabled
      </td>

      <td>
        true
      </td>
    </tr>

    <tr>
      <td>
        maxPaymentsAllowed\
        **optional**
      </td>

      <td>
        `Integer` This parameter is used to specify the number of payments that can be accepted on a link.
      </td>

      <td>
        25
      </td>
    </tr>

    <tr>
      <td>
        customer.name\
        **optional**
      </td>

      <td>
        `String` This field contains the customer name for whom the payment link is created.
      </td>

      <td>
        Ashish
      </td>
    </tr>

    <tr>
      <td>
        customer.email\
        **optional**
      </td>

      <td>
        `String` This field contains the customer email to which the created payment link is sent.
      </td>

      <td>
        [ashish1234@gmail.com](mailto:ashish1234@gmail.com)
      </td>
    </tr>

    <tr>
      <td>
        customer.phone\
        **optional**
      </td>

      <td>
        `String` This field contains the customer phone number to which the payment link needs to be sent.
      </td>

      <td>
        9876543210
      </td>
    </tr>

    <tr>
      <td>
        address\
        **optional**
      </td>

      <td>
        `JSON` This parameter contains the customer address to which the goods are delivered.
      </td>

      <td>
        H.No- 17, Block C, Kalyan Bldg, Khardilkar Road, Mumbai
      </td>
    </tr>

    <tr>
      <td>
        udf1 - udf5\
        **optional**
      </td>

      <td>
        `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5. Maximum character limit for this parameter is: `255`
      </td>

      <td>
         
      </td>
    </tr>

    <tr>
      <td>
        minAmountForCustomer\
        **optional**
      </td>

      <td>
        `Double` This parameter contains the minimum amount a customer needs to pay in case of partial payment.
      </td>

      <td>
        800
      </td>
    </tr>

    <tr>
      <td>
        isAmountFilledByCustomer\
        **optional**
      </td>

      <td>
        `boolean` This parameter contains any of the following values to specify whether it is an open invoices (when customer fills amount) or fixed amount:\
            \- **true**-It is an open invoice where the customer can fill the amount. The subamount parameter must be null in this case\
            \- **false**-It is closed invoice and amount is fixed
      </td>

      <td>
        false
      </td>
    </tr>

    <tr>
      <td>
        currency\
        **optional**
      </td>

      <td>
        `String` This parameter contains the currency used.
      </td>

      <td>
        Rupee
      </td>
    </tr>

    <tr>
      <td>
        viaEmail\
        **optional**
      </td>

      <td>
        `Boolean` This parameter contains any of the following values to specify whether to directly send an email to customer upon payment link generation or later:\
            \- **true**-The payment link is sent to the email upon generation\
            \- **false**-The payment link is not sent to the email upon generation
      </td>

      <td>
        true
      </td>
    </tr>

    <tr>
      <td>
        viaSms\
        **optional**
      </td>

      <td>
        `Boolean` This parameter contains any of the following values to specify whether to directly send as SMS to customer upon payment link generation or later:  

        * **true**-The payment link is sent as SMS upon generation  
        * **false**-The payment link is not sent as email upon generation
      </td>

      <td>
        true
      </td>
    </tr>
  </tbody>
</Table>

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
