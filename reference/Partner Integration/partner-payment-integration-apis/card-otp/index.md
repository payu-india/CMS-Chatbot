---
title: Card OTP [New]
excerpt: >-
  Submit a card OTP for a reference id, or resend that OTP.
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
These two pages complete a card OTP. Submit Card OTP checks the OTP for a `reference_id`. Resend Card OTP sends a new OTP for that same `reference_id`.

***

## Authentication

Both pages use a **Bearer token**.

| Environment | Base URL |
| :---------- | :------- |
| Test        | `https://test-partnerapilayer.payu.in/apilayer` |
| Production  | `https://api.payu.in` |

Send `Authorization: Bearer {access_token}` on both calls. Both also require `merchant_id`, `reseller_id`, `hash`, and `reference_id`.

| Page | Route | Required body |
| :--- | :---- | :------------ |
| Submit Card OTP | `POST /partner/submitCardOtp` | `merchant_id`, `reseller_id`, `hash`, `reference_id`, `otp` |
| Resend Card OTP | `POST /partner/resendCardOtp` | `merchant_id`, `reseller_id`, `hash`, `reference_id` |

***

## Endpoints

These are the Card OTP pages.

<Cards>
  <Card title="Submit Card OTP" href="https://docs.payu.in/reference/partner-submit-card-otp-api" target="_blank">
    POST /partner/submitCardOtp. Send the OTP with the reference id. A verified OTP returns txnStatus, mihpayid, and the message "OTP verified successfully". A failure uses status "failed".
  </Card>
  <Card title="Resend Card OTP" href="https://docs.payu.in/reference/partner-resend-card-otp-api" target="_blank">
    POST /partner/resendCardOtp. Send the same reference id without an OTP. On success the message is "OTP resent successfully".
  </Card>
</Cards>

***

## How It Works

<Accordion title="Submit the OTP" icon="fad fa-key-skeleton-left-right">
  Call Submit Card OTP with `merchant_id`, `reseller_id`, `hash`, `reference_id`, and `otp`.
</Accordion>

<Accordion title="Read the submit result" icon="fab fa-searchengin">
  A verified OTP on Submit Card OTP adds `txnStatus`, `mihpayid`, and "OTP verified successfully". Failures return status `failed` and a message.
</Accordion>

<Accordion title="Resend the OTP" icon="fad fa-rotate-left">
  Call Resend Card OTP with the same `reference_id`. Do not send `otp`. The success message is "OTP resent successfully".
</Accordion>
