---
title: APIs used in Auth and Capture
excerpt: ''
deprecated: false
hidden: true
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
* **Capture a Pre-Authorized Payment**: To capture a pre-authorized payment, use the following command. After the API command is successful, the transaction would be captured and settled to you. For more information, refer to [Capture a Pre-Authorized Payment](ref:capture_a_payment) API under API Reference.
* **Check Refund Status**: The **check\_action\_status** API is used to check the final status of refund as the request gets queued at PayU. For more information, refer to  [Check Refund Status API with Request ID](ref:check_action_status_api_with_request_id).
