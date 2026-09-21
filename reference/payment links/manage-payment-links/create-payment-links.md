---
api:
  file: payment-link-33.json
  operationId: CreatePaymentLinkAPI
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

|                        |                                                |
| :--------------------- | :--------------------------------------------- |
| Test Environment       | {user.https://uatoneapi.payu.in/payment-links} |
| Production Environment | {user.https://oneapi.payu.in/payment-links}    |

<Callout icon="📘" theme="info">
### Notes:
  * The access token with the scope as **create_payment_links** is required on the header. For more information on getting the access token, refer to [Get Access Token](https://docs.payu.in/reference/get-token-api-for-payment-links).
  * To create a seamless eNACH payment link, the **enforcePayMethod** parameter must be passed with "enach" as the only method.
</Callout>
<Accordion title="Other items to be noted" icon="fa-list">
  - `paymentDeadline` and `partialPaymentDeadline` use `yyyy-MM-dd HH:mm:ss`.
  - `whatsappRecipients` accepts no more than four entries. Each `phone` value must contain 10 to 15 digits.
  - `reminder.isScheduled` and `reminder.channels` are required when `reminder` is supplied. `reminder.type` is optional and accepts `0` or `1`.
  - `offerKey` is limited to 255 characters.
  - `partnerWebhookSuccessUrls` and `partnerWebhookFailureUrls` are limited to 512 characters each.
  - `amountStatus` accepts `UNPAID`, `PARTIALLY_PAID`, `FULLY_PAID`, or `OVERDUE`.
  - The four `beneficiarydetail` arrays support a maximum of four entries and must have matching lengths.
  - `beneficiaryAccountType` accepts `SAVINGS` or `CURRENT`.
  - Use `enforcePayMethod: "enach"` alone when creating a seamless eNACH payment link.
  </Accordion>

### Sample Requests

<Accordion title="Create a payment link" icon="fa-code">
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

### For various other scenarios

<Accordion title="Create an open-invoice payment link" icon="fa--info-split">
  Set `isAmountFilledByCustomer` to `true`. In this flow, `subAmount` must be `null` because the customer enters the amount.

  ```curl
  curl --location -g --request POST 'https://uatoneapi.payu.in/payment-links/' \
    --header 'merchantId: {{merchantId}}' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Bearer {{access_token}}' \
    --data-raw '{
      "isAmountFilledByCustomer": true,
      "subAmount": null,
      "description": "Customer-entered payment for {{customerReference}}",
      "source": "API"
    }'
  ```
</Accordion>

<Accordion title="Allow partial payments" icon="fa--info-split">
  Set `isPartialPaymentAllowed` to `true`. Use `minAmountForCustomer` when the customer must pay at least a specified amount.

  ```curl
  curl --location -g --request POST 'https://uatoneapi.payu.in/payment-links/' \
    --header 'merchantId: {{merchantId}}' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Bearer {{access_token}}' \
    --data-raw '{
      "subAmount": 5000,
      "isPartialPaymentAllowed": true,
      "minAmountForCustomer": 500,
      "paymentDeadline": "2026-10-15 23:59:59",
      "description": "Part-payment for order {{orderId}}",
      "source": "API"
    }'
  ```
</Accordion>

<Accordion title="Create a recurring or SI payment link" icon="fa--info-clock">
  Use `si_payment_link` as the `source` and provide the recurring schedule in `siDetails`.

  ```curl
  curl --location -g --request POST 'https://uatoneapi.payu.in/payment-links/' \
    --header 'merchantId: {{merchantId}}' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Bearer {{access_token}}' \
    --data-raw '{
      "subAmount": 500,
      "description": "Monthly subscription for {{customerId}}",
      "source": "si_payment_link",
      "siDetails": {
        "billingAmount": 500,
        "billingCurrency": "INR",
        "billingCycle": "MONTHLY",
        "billingInterval": 1,
        "paymentStartDate": "2026-10-01",
        "paymentEndDate": "2027-09-30"
      }
    }'
  ```
</Accordion>

<Accordion title="Create a seamless eNACH payment link" icon="fa-code">
  For a seamless eNACH link, pass `enforcePayMethod` with `enach` as the only method. The eNACH `bankDetails` object is nested inside `siDetails`.

  ```curl
  curl --location -g --request POST 'https://uatoneapi.payu.in/payment-links/' \
    --header 'merchantId: {{merchantId}}' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Bearer {{access_token}}' \
    --data-raw '{
      "subAmount": 500,
      "description": "eNACH subscription for {{customerId}}",
      "source": "si_payment_link",
      "enforcePayMethod": "enach",
      "siDetails": {
        "billingAmount": 500,
        "billingCycle": "MONTHLY",
        "paymentStartDate": "2026-10-01",
        "bankDetails": {
          "bankCode": "{{bankCode}}",
          "bankAccountNumber": "{{customerBankAccountNumber}}",
          "ifsc": "{{customerIfsc}}",
          "accountType": "SAVINGS"
        }
      }
    }'
  ```
</Accordion>

<Accordion title="Schedule a payment reminder" icon="fa-code">
  Set `reminder.isScheduled` to `true`, choose the reminder timing with `reminder.type`, and provide one or both supported channels.

  ```curl
  curl --location -g --request POST 'https://uatoneapi.payu.in/payment-links/' \
    --header 'merchantId: {{merchantId}}' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Bearer {{access_token}}' \
    --data-raw '{
      "subAmount": 2500,
      "paymentDeadline": "2026-10-15 23:59:59",
      "reminder": {
        "isScheduled": true,
        "type": 0,
        "channels": ["email", "phone"]
      },
      "description": "Payment with reminder for {{orderId}}",
      "source": "API"
    }'
  ```
</Accordion>

<Accordion title="Send a payment link to multiple WhatsApp recipients" icon="fa-code">
  Set `viaWhatsapp` to `true` and provide up to four recipient objects in `whatsappRecipients`. Use `whatsappTemplateName` to select the WhatsApp notification template.

  ```curl
  curl --location -g --request POST 'https://uatoneapi.payu.in/payment-links/' \
    --header 'merchantId: {{merchantId}}' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Bearer {{access_token}}' \
    --data-raw '{
      "subAmount": 1500,
      "viaWhatsapp": true,
      "whatsappRecipients": [
        {"phone": "9876543210"},
        {"phone": "9123456789"}
      ],
      "whatsappTemplateName": "{{whatsappTemplateName}}",
      "description": "WhatsApp payment link for {{orderId}}",
      "source": "API"
    }'
  ```
</Accordion>

<Accordion title="Attach an offer or coupon" icon="fa-code">
  Pass the offer or coupon identifier in `offerKey`.

  ```curl
  curl --location -g --request POST 'https://uatoneapi.payu.in/payment-links/' \
    --header 'merchantId: {{merchantId}}' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Bearer {{access_token}}' \
    --data-raw '{
      "subAmount": 2000,
      "offerKey": "{{offerKey}}",
      "description": "Payment link with offer for {{orderId}}",
      "source": "API"
    }'
  ```
</Accordion>

<Accordion title="Specify payout beneficiaries" icon="fa-code">
  Use `beneficiarydetail` for NEFT or IMPS payout flows. Keep the four arrays aligned by position and do not send more than four entries.

  ```curl
  curl --location -g --request POST 'https://uatoneapi.payu.in/payment-links/' \
    --header 'merchantId: {{merchantId}}' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Bearer {{access_token}}' \
    --data-raw '{
      "subAmount": 4000,
      "beneficiarydetail": {
        "beneficiaryAccountNumber": ["{{beneficiaryAccountNumber1}}"],
        "ifscCode": ["{{beneficiaryIfsc1}}"],
        "beneficiaryName": ["{{beneficiaryName1}}"],
        "beneficiaryAccountType": ["SAVINGS"]
      },
      "description": "Payment link with payout beneficiary",
      "source": "API"
    }'
  ```
</Accordion>

<Accordion title="Hold a pre-authorisation" icon="fa-code">
  Pass the number of days to hold the pre-authorisation in `blockDaysForPreAuthorizeLinks`.

  ```curl
  curl --location -g --request POST 'https://uatoneapi.payu.in/payment-links/' \
    --header 'merchantId: {{merchantId}}' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Bearer {{access_token}}' \
    --data-raw '{
      "subAmount": 7500,
      "blockDaysForPreAuthorizeLinks": 7,
      "description": "Pre-authorisation payment link for {{orderId}}",
      "source": "API"
    }'
  ```
</Accordion>

<br />

## Sample response

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

## Request parameters

The following fields are available when creating a payment link. Unless marked otherwise, the fields in this section are optional and should be included only for the corresponding payment-link flow.

> **Important:** The examples below use illustrative values and placeholders. Replace every value in `{{double_curly_braces}}` with a value from your integration. Do not use real customer or bank data in documentation examples.

<Accordion title="Parameters used in Advanced Payment Link flows" icon="fa-table">
  | Parameter                       | Type                                | Description                                                                                                              |
  | :------------------------------ | :---------------------------------- | :----------------------------------------------------------------------------------------------------------------------- |
  | `paymentDeadline`               | String                              | Deadline by which the customer must complete payment, independent of `expiryDate`. Use the `yyyy-MM-dd HH:mm:ss` format. |
  | `whatsappRecipients`            | Array of objects, maximum 4 entries | WhatsApp recipients. Each object must contain a `phone` value with 10 to 15 digits.                                      |
  | `whatsappTemplateName`          | String                              | WhatsApp notification template name.                                                                                     |
  | `offerKey`                      | String, maximum 255 characters      | Offer or coupon key to attach to the payment link.                                                                       |
  | `blockDaysForPreAuthorizeLinks` | Integer                             | Number of days to hold a pre-authorisation.                                                                              |

  `viaWhatsapp` is the existing switch for WhatsApp notification. Use it with `whatsappRecipients` when the link must be sent to more than one WhatsApp number.

  ### `reminder` object

  Use `reminder` to configure a payment reminder.

  | Field         | Type             | Required | Description                                                                  |
  | :------------ | :--------------- | :------- | :--------------------------------------------------------------------------- |
  | `isScheduled` | Boolean          | Yes      | Whether a reminder is scheduled.                                             |
  | `type`        | Integer          | No       | `0` means before the payment deadline; `1` means after the payment deadline. |
  | `channels`    | Array of strings | Yes      | Reminder channels. Supported values are `email` and `phone`.                 |

  ### `additionalDetails` object

  | Field                       | Type                           | Description                                                                                    |
  | :-------------------------- | :----------------------------- | :--------------------------------------------------------------------------------------------- |
  | `partnerWebhookSuccessUrls` | String, maximum 512 characters | Partner webhook URL for a successful payment. This is separate from the merchant `successURL`. |
  | `partnerWebhookFailureUrls` | String, maximum 512 characters | Partner webhook URL for a failed payment.                                                      |
  | `amountStatus`              | Enum                           | Current payment status: `UNPAID`, `PARTIALLY_PAID`, `FULLY_PAID`, or `OVERDUE`.                |
  | `partialPaymentDeadline`    | String                         | Deadline specifically for completing partial payments. Use the `yyyy-MM-dd HH:mm:ss` format.   |
  | `sendWhatsapp`              | Boolean                        | Whether WhatsApp notification is enabled for the link.                                         |

  ### `beneficiarydetail` object

  Use `beneficiarydetail` to specify bank-account beneficiaries for NEFT or IMPS payout flows. You can provide up to four entries. The arrays must contain the same number of entries, and each position represents one beneficiary.

  | Field                      | Type             | Maximum entries | Description                                                             |
  | :------------------------- | :--------------- | :-------------: | :---------------------------------------------------------------------- |
  | `beneficiaryAccountNumber` | Array of strings |        4        | Bank account numbers.                                                   |
  | `ifscCode`                 | Array of strings |        4        | IFSC codes. The number of values must match `beneficiaryAccountNumber`. |
  | `beneficiaryName`          | Array of strings |        4        | Account-holder names.                                                   |
  | `beneficiaryAccountType`   | Array of strings |        4        | Account types. Each value must be `SAVINGS` or `CURRENT`.               |
</Accordion>
