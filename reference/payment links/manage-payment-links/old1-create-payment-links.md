---
title: '[OLD]Create Payment Link API'
excerpt: ''
api:
  file: payment-link-29.json
  operationId: CreatePaymentLinkAPI
deprecated: false
hidden: true
metadata:
  title: Create a Payment Link API
  description: >-
    The document provides information on using the Create a Payment Link API to
    generate a payment link for customers, requiring an access token with the
    scope of create_payment_links. It includes sample requests, responses for
    success and failure scenarios, and details on request parameters.
  keywords:
    - Create a Payment Link API
    - Payment Link Creation API
    - Share Payment Link API
    - ' Send Payment Link API'
  robots: index
next:
  description: ''
---
The** Create a Payment Link** API is used to create a payment link for your customer.

**Environment**

|                        |                                           |
| :--------------------- | :---------------------------------------- |
| Test Environment       | <https://uatoneapi.payu.in/payment-links> |
| Production Environment | <https://oneapi.payu.in/payment-links>    |

> 📘 Note:
> 
> The access token with the scope as **create_payment_links** is required on the header. For more information on getting the access token, refer to [Get Token API - Payment Links](ref:get-token-api-payment-links).

<details><summary>Sample request</summary>

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

</details>

<details><summary>Sample response</summary>

**Success scenario**

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

**Failure scenario**

```
{
  "status": -1,
  "message": "Invoice Number already exists. Please enter new invoice number.",
  "result": null,
  "errorCode": null,
  "guid": null
}
```

</details>

## Request parameters

<details><summary>Reference info for request parameters</summary>

| Parameter     |                                                                                                                                                                  |
| :------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| client_id     | The client ID provided by PayU. For more information, refer to [Get Client ID and Secret from Dashboard](doc:get-client-id-and-secret-from-dashboard).           |
| client_secret | The client secret provided by PayU. For more information, refer to  [Get Client ID and Secret from Dashboard](doc:get-client-id-and-secret-from-dashboard).      |
| reminder      | This parameter is in a JSON format and the fields in this JSON are described in the [reminder JSON fields description ](#reminder-json-fields-description)table. |

### reminderJSON fields description

| Parameter   | Reference                                                                                                                                                                  |
| :---------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| isScheduled | This parameter must be set to "true" if this payment link is scheduled, The type and channels must have values if this field is set to "true."                             |
| type        | This field use to indicate the reminder type and can contain any of the following: 0 - Before expiry 1: After link creation. By default, the value for this field is null. |
| channels    | This field can contain any of the following: "email", "phone" or "email","phone"                                                                                           |

</details>

## Request parameters