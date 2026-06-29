---
title: APIs used in Auth and Capture
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The following APIs are used in Pre-authorization and you can refer the API Reference to get more details:

* **Pre-Authorize Payments**: Pre-authorize payments using any of the following with "Try It" experience under API Refernece:
  * [PayU Hosted - Pre-Authorize Payment API](ref:pre_authorize_payment)
  * [Merchant Hosted - Pre-Authorize Payment API](ref:pre_authorize_payment_merchant_hosted)
* **Capture a Pre-Authorized Payment**: To capture a pre-authorized payment, use the **_payment** API. After the API command is successful, the transaction would be captured and settled to you. For more information, refer to [Capture a Pre-Authorized Payment](ref:capture_a_payment) API under API Reference.
* **Cancel a Pre-Authorized Transaction**: To cancel a pre-auth payment, refer to [Cancel a Pre-Authorized Transaction API](ref:cancel-a-pre-authorized-transaction).
* **One-Time Mandate APIs**: To set up one-time mandates, use the following APIs based on the :
  * [PayU Hosted - UPI One-Time Mandate API](https://docs.payu.in/reference/upi-one-time-mandate-transaction-api-payu-hosted)
  * [Merchant Hosted - UPI One-Time Mandate API ](https://docs.payu.in/reference/_payment-upi-one-time-mandate-transaction-api)
* **Check Refund Status**: The **check_action_status** API is used to check the final status of refund as the request gets queued at PayU. For more information, refer to  [Check Refund Status API with Request ID](ref:check_action_status_api_with_request_id).
