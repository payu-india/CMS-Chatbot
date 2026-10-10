---
api:
  file: cards-si-api.yaml
  operationId: post_authorizetransaction-php
hidden: true
---
Completes card mandate creation by submitting the 3DS authentication result to PayU.After the customer submits the OTP, the merchant receives a response containing`bankData`. Add `siTokenDetails` (network token details) to this JSON and pass it as`authentication_info` to complete authorisation and register the mandate.On success, the response includes `IsStandingInstructionSet: "1"` confirming the mandatewas registered. The `mihpayid` in the response is the `authPayuId` required for allsubsequent pre-debit and recurring debit calls.**Hash formula:**`SHA512(key|txnid|amount|authentication_info|SALT)`Use the exact serialised `authentication_info` JSON string (not the object).> `siTokenDetails` is optional for the saved card flow when authentication was done via PayU.
