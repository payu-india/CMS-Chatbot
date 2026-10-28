---
title: Get Single Payment Link API - Partner Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
This API is used to get a single payment link using the payment link invoice number.

The invoice number in the request header must be included as a query parameter in the **invoice_number** field.

<Callout icon="📘" theme="info">
  ### **Note**:&#x20;

  The access token with the scope as **read_payment_links** is required on the header. For more information on getting the access token, refer to [User Token APIs](ref:partner-integration-user-token-apis).
</Callout>

### Environment

|                            |                                                             |
| :------------------------- | :---------------------------------------------------------- |
| **Test Environment**       | \<[https://uat-partner.payu.in](https://uatoneapi.payu.in)> |
| **Production Environment** | \<[https://oneapi.payu.in](https://partner.payu.in)>        |

## Request Header
| Parameter | Description | Example |
| :--- | :--- | :--- |
| Content-Type | The format of the request body. | `application/json` |
| Authorization | The Bearer access token used to authenticate the API request. The token must have the `create_payment_links` scope. | `Bearer {{access_token}}` |
| merchantId | The unique merchant identifier provided by PayU. | `4825038` |

## Sample Request
  ```curl
  curl --location -g '{{payu_base_url}}/payment-links/{{invoice_number}}' \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer {{access_token}}' \
  --header 'merchantId: 4825038'
  ```

## Sample Response
  **Success scenario**

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

  **Failure scenario**

  ```json
  {
    "status": -1,
    "message": "paymentLink not found",
    "result": null,
    "errorCode": null,
    "guid": null
  }
  ```