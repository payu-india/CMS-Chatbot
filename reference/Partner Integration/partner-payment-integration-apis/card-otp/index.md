---
title: Card OTP [New]
excerpt: >-
  Submit or resend the OTP for a partner card payment.
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  robots: index
next:
  description: Explore related information and resources.
  pages:
    - slug: partner-submit-card-otp-api
      title: Submit card OTP API [New]
      type: basic
    - slug: partner-resend-card-otp-api
      title: Resend card OTP API [New]
      type: basic
---
Verify a card OTP, or send it again, for a partner card payment. Both calls use the same `reference_id`.

***

## Authentication

All Card OTP APIs use a **Bearer token**.

| Environment | Base URL |
| :---------- | :------- |
| Test        | `https://test-partnerapilayer.payu.in/apilayer` |
| Production  | `https://api.payu.in` |

Send the token on every call as `Authorization: Bearer {access_token}`.

<Callout icon="📘" theme="info">
  ### **Access token**

  Older partner accounts generate this token with the <Anchor target="_blank" href="https://docs.payu.in/reference/token-generation-flow-for-old-partner-merchants">token generation flow for partner payments</Anchor>.
</Callout>

***

## Endpoints

<Cards>
  <Card title="Submit Card OTP" href="https://docs.payu.in/reference/partner-submit-card-otp-api" target="_blank">
    Submit the OTP for a reference id. A verified OTP returns the transaction status and mihpayid.
  </Card>
  <Card title="Resend Card OTP" href="https://docs.payu.in/reference/partner-resend-card-otp-api" target="_blank">
    Resend the OTP for the same reference id.
  </Card>
</Cards>

***

## How It Works

<Accordion title="Submit the OTP" icon="fad fa-key-skeleton-left-right">
  Call Submit Card OTP with `merchant_id`, `reseller_id`, `hash`, `reference_id`, and `otp`.
</Accordion>

<Accordion title="Read the result" icon="fab fa-searchengin">
  A verified OTP adds `txnStatus`, `mihpayid`, and the message "OTP verified successfully". A failure returns status `failed`.
</Accordion>

<Accordion title="Resend when the customer needs a new OTP" icon="fad fa-rotate-left">
  Call Resend Card OTP with the same `reference_id`. Do not send `otp` on the resend request.
</Accordion>
