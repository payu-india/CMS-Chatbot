---
title: Cards Decoupled Flow
excerpt: ''
api:
  file: s2s.json
  operationId: S2S-DecoupledFlow
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
      slug: integrate-with-decoupled-flow-s2s
      title: Decoupled Flow Integration
---
You can collect card payments without redirection to bank page for entering OTP using S2S integration. This section provides the request and response parameters used in Step 1 of [Decoupled Flow Integration](doc:integrate-with-decoupled-flow-s2s). You can get the sample request and response when use the "Try It" experience. For more information remaining steps of integration, refer to [Decoupled Flow Integration](doc:integrate-with-decoupled-flow-s2s).

  > 📘 Reference
  >
  > For the character limit of each parameter and detailed description, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis).


  > 📘 Note:
  >
  > Collecting the information for the following parameters from customers is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information:
  >
  > * email
  > * phone
  > * address1
  > * s2s\_client\_ip
  > * s2s\_device\_info


## Response parameters

For the response parameters, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis).

## Request parameters

> 🚧 Values to be used in Test environment
>
> For values to be used in Test environment, refer to <a href="test-cards-upi-id-and-wallets#web-checkout" target="_blank">Test Cards</a>.
