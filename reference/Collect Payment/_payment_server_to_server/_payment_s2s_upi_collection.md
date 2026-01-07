---
title: UPI Collect - S2S
excerpt: ''
api:
  file: merchant-hosted-36.json
  operationId: S2S-UPICollection
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
  pages:
    - type: basic
      slug: upi-collection-s2s
      title: UPI Collection S2S Integration
---
This section provides the request and response parameters used in Step 1 of [UPI Collection S2S Integration](doc:upi-collection-s2s). You can get the sample request and response when use the "Try It" experience. For the complete integration steps, refer to [UPI Collection S2S Integration](doc:upi-collection-s2s).

<Callout icon="📘" theme="info">
  **Reference**: For the character limit of each parameter and detailed description, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis).
</Callout>

<Additional_paymentRequestParams />

<Accordion_Collect_Fraud_Detection />

## Response parameters

For the response parameters, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis).

## Request parameters

<Callout icon="❗️" theme="error">
  **Error handling**: If any error message is displayed with an error code, refer to the <a href="error-codes" target="_blank">Error Codes</a> section to understand the reason for these error codes.
</Callout>

<Callout icon="🚧" theme="warn">
  **Values to be used in Test environment**: For values to be used in Test environment, refer to <a href="https://docs.payu.in/docs/test-cards-upi-id-and-wallets#web-checkout" target="_blank">Test Cards</a>.
</Callout>