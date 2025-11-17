---
title: Get Checkout Details API
deprecated: false
hidden: false
metadata:
  robots: index
---
The **Get Checkout Details** (get_checkout_details) API is a generic API using which they can get information when you create the custom checkout pages, that will contain the payment options, offers, recommendations, and downtime details. The API provides the following details:

* **Payment option details**: The extended details for each payment option are available for the merchant.
* **Additional charges**: The additional charges are configured for all payment options.  
  eligibility details
* **Downtime details**: The downtime status of the payment options.

**Environment**

|                        |                                                                                      |
| :--------------------- | :----------------------------------------------------------------------------------- |
| Production Environment | [https://test.payu.in/v3/checkout/details](https://test.payu.in/v3/checkout/details) |
| Test Environment       | https://info.payu.in/v3/checkout/details                                             |

## Request headers

<V2_payment_header_params />

## Request parameters

| Parameter                                 | Description                                                                     | Example                     |
| ----------------------------------------- | ------------------------------------------------------------------------------- | --------------------------- |
| `key`<br /><code>mandatory</code>         | <code>String</code> The merchant key provided by PayU.                          | JPM7Fg                      |
| `requestData`<br /><code>mandatory</code> | <code>JSON Object</code> A JSON object containing detailed request information. | See JSON fields table below |

### requestData JSON Fields

| Field                                                          | Description                                                                     | Example              |
| -------------------------------------------------------------- | ------------------------------------------------------------------------------- | -------------------- |
| `requestId`<br /><code>mandatory</code>                        | <code>String</code> A unique identifier for the request.                        | 12345678             |
| `transactionDetails`<br /><code>mandatory</code>               | <code>JSON Object</code> Details about the transaction.                         | See sub-fields below |
| `transactionDetails.amount`<br /><code>mandatory</code>        | <code>Number</code> The transaction amount.                                     | 12345.12             |
| `useCase`<br /><code>optional</code>                           | <code>JSON Object</code> Specific use cases for the API.                        | See sub-fields below |
| `useCase.getExtendedPaymentDetails`<br /><code>optional</code> | <code>Boolean</code> Whether to fetch extended payment details.                 | true                 |
| `useCase.checkCustomerEligibility`<br /><code>optional</code>  | <code>Boolean</code> Whether to check customer eligibility for payment options. | true                 |
| `customerDetails`<br /><code>optional</code>                   | <code>JSON Object</code> Details about the customer.                            | See sub-fields below |
| `customerDetails.mobile`<br /><code>optional</code>            | <code>String</code> Mobile number of the customer.                              | 9098765432           |
| `filters`<br /><code>optional</code>                           | <code>JSON Object</code> Filters to apply on the payment options.               | See sub-fields below |
| `filters.paymentOptions`<br /><code>optional</code>            | <code>JSON Object</code> Filters for specific payment options.                  | See sub-fields below |
| `filters.paymentOptions.emi`<br /><code>optional</code>        | <code>JSON Object</code> Filters for EMI options.                               | See sub-fields below |
| `filters.paymentOptions.emi.dc`<br /><code>optional</code>     | <code>String</code> Comma-separated list of bank codes for debit card EMI.      | SBIN,KKBK,ICIC       |

## Sample Request (cURL)

```bash
curl --location 'https://info.payu.in/v3/checkout/details' \
--header 'Content-Type: application/json' \
--header 'date: {{date}}' \
--header 'Authorization: {{authorization}}' \
--data '{
  "requestId": "12345678",
  "transactionDetails": {
    "amount": 12345.12
  },
  "useCase": {
    "getExtendedPaymentDetails": true,
    "checkCustomerEligibility": true
  },
  "customerDetails": {
    "mobile": "9098765432"
  },
  "filters": {
    "paymentOptions": {
      "emi": {
        "dc": "SBIN,KKBK,ICIC"
      }
    }
  }
}'
```

## Sample Response

### Success Response

```json
{
  "status": 1,
  "message": "Success",
  "result": {
    "requestId": "12345678",
    "paymentOptions": {
      "cards": {
        "status": true,
        "credit": {
          "status": true,
          "details": [
            {
              "bankCode": "HDFC",
              "bankName": "HDFC Bank",
              "isDown": false,
              "downSince": "",
              "expectedUpTime": "",
              "downMessage": ""
            }
          ]
        },
        "debit": {
          "status": true,
          "details": [
            {
              "bankCode": "SBIN",
              "bankName": "State Bank of India",
              "isDown": false,
              "downSince": "",
              "expectedUpTime": "",
              "downMessage": ""
            }
          ]
        }
      },
      "netBanking": {
        "status": true,
        "details": [
          {
            "bankCode": "HDFC",
            "bankName": "HDFC Bank",
            "isDown": false,
            "downSince": "",
            "expectedUpTime": "",
            "downMessage": ""
          }
        ]
      },
      "emi": {
        "status": true,
        "credit": {
          "status": true,
          "details": [
            {
              "bankCode": "ICIC",
              "bankName": "ICICI Bank",
              "isDown": false,
              "tenures": [3, 6, 9, 12],
              "minAmount": 3000
            }
          ]
        },
        "debit": {
          "status": true,
          "details": [
            {
              "bankCode": "SBIN",
              "bankName": "State Bank of India",
              "isDown": false,
              "tenures": [3, 6, 9],
              "minAmount": 5000
            }
          ]
        }
      },
      "upi": {
        "status": true,
        "isDown": false
      },
      "wallet": {
        "status": true,
        "details": [
          {
            "walletCode": "PAYZ",
            "walletName": "Payzapp",
            "isDown": false
          }
        ]
      }
    }
  }
}
```

### Error Response

```json
{
  "status": 0,
  "message": "Invalid request parameters",
  "error_code": "E1001"
}
```

## Response Parameters

| Parameter    | Description                                               | Example                     |
| ------------ | --------------------------------------------------------- | --------------------------- |
| `status`     | Status of the API call. `1` for success, `0` for failure. | `1`                         |
| `message`    | Status message of the API call.                           | `Success`                   |
| `result`     | JSON object containing the checkout details.              | See JSON fields table below |
| `error_code` | Error code in case of failure.                            | `E1001`                     |

### result JSON Fields

| Field                       | Description                                               | Example              |
| --------------------------- | --------------------------------------------------------- | -------------------- |
| `requestId`                 | The request ID provided in the request.                   | `12345678`           |
| `paymentOptions`            | JSON object containing various payment options available. | See sub-fields below |
| `paymentOptions.cards`      | Details about card payment options.                       | See sub-fields below |
| `paymentOptions.netBanking` | Details about net banking payment options.                | See sub-fields below |
| `paymentOptions.emi`        | Details about EMI payment options.                        | See sub-fields below |
| `paymentOptions.upi`        | Details about UPI payment options.                        | See sub-fields below |
| `paymentOptions.wallet`     | Details about wallet payment options.                     | See sub-fields below |
