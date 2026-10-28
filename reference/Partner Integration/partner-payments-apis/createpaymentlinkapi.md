---
title: Create Payment Link API - Partner Integration
deprecated: false
hidden: true
metadata:
  title: Create Payment Link API - Partner Integration
  robots: index
---
This API is used to create a payment link for your customer with Partner Integration.

<Callout icon="📘" theme="info">
  ### **Note**:

  The access token with the scope as **create_payment_links** is required on the header. For more information on getting the access token, refer to [Get Token API](ref:get_token_api).
</Callout>

### Environment

|                            |                                                                |
| :------------------------- | :------------------------------------------------------------- |
| **Test Environment**       | \<[https://test-partner.payu.in](https://uat-partner.payu.in)> |
| **Production Environment** | \<[https://partner.payu.in](https://oneapi.payu.in)>           |

## Request Parameters

### Request Header

| Parameter     | Description                                                                                                         | Example                   |
| :------------ | :------------------------------------------------------------------------------------------------------------------ | :------------------------ |
| Content-Type  | The format of the request body.                                                                                     | `application/json`        |
| Authorization | The Bearer access token used to authenticate the API request. The token must have the `create_payment_links` scope. | `Bearer {{access_token}}` |
| merchantId    | The unique merchant identifier provided by PayU.                                                                    | `4825038`                 |

### Body Parameters

**Mandatory parameters**

| Parameter | Description | Example |
| :--- | :--- | :--- |
| isAmountFilledByCustomer | Indicates whether the customer will enter the payment amount on the payment link page. Set to `false` if the amount is prefilled by the merchant. | `false` |
| subAmount | The subtotal amount for the payment link. | `100` |
| currency | The currency of the transaction. | `INR` |
| source | The source of the payment link creation request. | `API` |
| customer | A JSON object containing the customer's details. | Refer to customer JSON Fields description table below. |
### customer JSON fields description
| Field | Description | Example |
| :--- | :--- | :--- |
| name | The name of the customer. | `test` |
| phone | The phone number of the customer. | `999999999` |
| email | The email address of the customer. | `test@payu.in` |

**Optional parameters**

| Parameter | Description | Example |
| :--- | :--- | :--- |
| description | A short description or note for the payment link. | `test` |
| address | A JSON object containing the customer's address details. | Refer to address JSON Fields description table below. |

### address JSON Fields description
| Field | Description | Example |
| :--- | :--- | :--- |
| line1 | The first line of the customer's address. | `test` |
| line2 | The second line of the customer's address. | `sample` |
| city | The city of the customer's address. | `gurgaon` |
| state | The state of the customer's address. | `UP` |
| country | The country of the customer's address. | `India` |
| zipCode | The postal or ZIP code of the customer's address. | `122220` |
| udf | A JSON object for user-defined fields that can carry custom metadata for the transaction. | Refer to udf JSON Fields description table below. |

### udf JSON fields description
| Field | Description | Example |
| :--- | :--- | :--- |
| udf1 | User-defined field 1 to pass any custom information. | `sampleUdf1` |
| udf2 | User-defined field 2 to pass any custom information. | `sampleUdf2` |
| udf3 | User-defined field 3 to pass any custom information. | `sampleUdf3` |


## Sample Request

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
## Sample Response

* Success Scenario

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

* Failure Scenario

```
{
  "status": -1,
  "message": "Invoice Number already exists. Please enter new invoice number.",
  "result": null,
  "errorCode": null,
  "guid": null
}
```