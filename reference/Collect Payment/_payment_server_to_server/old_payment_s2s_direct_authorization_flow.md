---
title: ' [OLD]Cards Direct Authorization Flow'
excerpt: 'Resource: **_payment**'
api:
  file: payu-api-29.json
  operationId: S2SDirectAuthorizationFlow
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  pages:
    - slug: integrate-with-direct-authorization-s2s
      title: Direct Authorization Integration
      type: basic
---
PayU enables merchants to process direct authorization for pre-authenticated transactions (external MPI/3DSS). This section describes how to integrate with PayU’s direct authorization flow. Initiate an authorization request with the payment details provided post a successful authentication through the MPI/3DSS as explained in this API Reference. You can get the sample request and response when use the "Try It" experience. For more information remaining steps of integration, refer to [Direct Authorization Integration](doc:integrate-with-direct-authorization-s2s).

> 📘 Note:
>
> This API is backward compatible and you can continue to the existing integration parameters to process the 3DS 1.0.2 transactions.

<Accordion title="Reference information for request parameters" icon="fa-book">
  > 📘 Reference
  >
  > For the character limit of each parameter and detailed description, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis).

  <AddionalCards_paymentRequestParametersInformation />

  > 📘 Note:
  >
  > Collecting the information for the following parameters from customers is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information:
  >
  > * email
  > * phone
  > * address1
  > * s2s\_client\_ip
  > * s2s\_device\_info
</Accordion>

<Accordion_Collect_Fraud_Detection />

<br />

## Response parameters

For the response parameters, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis).

## Request parameters

<TransactionStages />

> 🚧 Values to be used in Test environment
>
> For values to be used in Test environment, refer to <a href="test-cards-upi-id-and-wallets#web-checkout" target="_blank">Test Cards</a>.
