---
api:
  file: Create payment links.json
  operationId: post_partners-payment-links
hidden: false
---
This API is used to create a payment link for your customer with Partner Integration.

<Callout icon="📘" theme="info">
  **Note**:

  The access token with the scope as **create_payment_links** is required on the header. For more information on getting the access token, refer to [Get Token API](ref:get_token_api).
</Callout>

### Environment

|                            |                                                              |
| :------------------------- | :----------------------------------------------------------- |
| **Test Environment**       | \<[https://test-partner.payu.in](https://uatoneapi.payu.in)> |
| **Production Environment** | \<[https://partner.payu.in](https://oneapi.payu.in)>         |

<details>
  <summary>Sample request</summary>

  ```curl
  curl --location -g '{{payu_base_url}}/payment-links' \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer {{access_token}}' \
  --header 'merchantId: 4825038' \
  --data-raw '{
      "isAmountFilledByCustomer": false,
      "subAmount": 100,
      "description": "test",
      "currency": "INR",
      "source": "API",
      "address": {
          "line1": "test",
          "line2": "sample",
          "city": "gurgaon",
          "state": "UP",
          "country": "India",
          "zipCode": "122220"
      },
      "customer": {
          "name": "test",
          "phone": "999999999",
          "email": "test@payu.in"
      },
      "udf": {
          "udf1": "sampleUdf1",
          "udf2": "sampleUdf2",
          "udf3": "sampleUdf3"
      }
  }'
  ```
</details>

<details>
  <summary>Sample response</summary>

  * Success scenario

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

  * Failure scenario

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
