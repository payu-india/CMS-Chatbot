---
api:
  file: cards-si-api.yaml
  operationId: post_authorizetransaction-php
hidden: true
---
After the customer completes OTP authentication in [Step 1](doc:cards-si-step1-payment-authentication), the merchant receives a `bankData` JSON in the OTP submission response. This step passes that `bankData` augmented with `siTokenDetails` (network token details) — as `authentication_info` to the `AuthorizeTransaction` API to complete authorization and register the mandate.

<Callout icon="👍" theme="okay">
  ### **On Success**

  The response contains `IsStandingInstructionSet: "1"` confirming the mandate is registered. Save the `mihpayid` from the `result` object — this is the `authPayuId` you will use in all subsequent [Pre-Debit and Recurring Payments](doc:cards-si-pre-debit-recurring) calls.
</Callout>

<Callout icon="📘" theme="info">
  ### **Saved Card Flow**

  `siTokenDetails` is **optional** when authentication was done via PayU for a saved card (Flow 2 in Step 1).
</Callout>

***

## Environments

| Environment | URL                                               |
| :---------- | :------------------------------------------------ |
| Test        | `https://test.payu.in/AuthorizeTransaction.php`   |
| Production  | `https://secure.payu.in/AuthorizeTransaction.php` |

***
