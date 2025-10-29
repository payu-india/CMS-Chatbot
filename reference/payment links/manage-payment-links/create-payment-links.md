---
title: Create a Payment Link API
excerpt: ''
api:
  file: payment-link-33.json
  operationId: CreatePaymentLinkAPI
deprecated: false
hidden: false
metadata:
  title: Create a Payment Link API
  description: >-
    The Create a Payment Link API allows users to generate payment links for
    customers, requiring an access token with the "create_payment_links" scope,
    and supports both test and production environments.
  keywords:
    - Create a Payment Link API
    - Payment Link Creation API
    - Share Payment Link API
    - ' Send Payment Link API'
    - ' SI Payment Link'
    - ' Recurring Payment Link'
  robots: index
next:
  description: ''
---
The **Create a Payment Link** API is used to create a regular payment link, recurring or SI payment link for your customer.

**Environment**

|                        |                                                                                       |
| :--------------------- | :------------------------------------------------------------------------------------ |
| Test Environment       | \<[https://uatoneapi.payu.in/payment-links](https://uatoneapi.payu.in/payment-links)> |
| Production Environment | \<[https://oneapi.payu.in/payment-links](https://oneapi.payu.in/payment-links)>       |

> 📘 Notes:
>
> * The access token with the scope as **create_payment_links** is required on the header. For more information on getting the access token, refer to [Get Token API - Payment Links](ref:get-token-api-payment-links).
> * To create a seamless eNACH payment link, the **enforcePayMethod** parameter must be passed with "enach" as the only method.

<Accordion title="Sample request" icon="fa-upload">
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
</Accordion>

<Accordion title="Sample response" icon="fa-download">
  **Success scenario**

  ```json
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

  ```json
  {
    "status": -1,
    "message": "Invoice Number already exists. Please enter new invoice number.",
    "result": null,
    "errorCode": null,
    "guid": null
  }
  ```
</Accordion>

## Request parameters
