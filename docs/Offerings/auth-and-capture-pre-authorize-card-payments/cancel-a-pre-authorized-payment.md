---
title: Cancel a Pre-Authorized Payment
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
You can cancel a pre-authorized payment or refund. You must use the **cancel_transaction** API command for cancelling a pre-authorized payment. For more information, refer to [Cancel a Pre-Authorized Transaction API](ref:cancel-a-pre-authorized-transaction).

<Callout icon="📘" theme="info">
  **Variation in Response for Regular Pre-Authorized Payment and UPI OTM**

  You must look for the variation in the success and failure responses for the UPI OTM integration when compared to Regular Pre-Authorized Payment integration. For example, UPI OTM success scenario is similar to the following:

  ```
  {"status":1,"action":"MANDATE_REVOKE","message":"Mandate Revoke request processed successfully"} 
  ```
</Callout>

<br />
