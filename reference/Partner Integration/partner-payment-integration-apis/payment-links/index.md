---
title: Payment Links [New]
excerpt: >-
  Read a partner payment link, start payment on it, and verify that transaction.
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  robots: index
next:
  description: Explore related information and resources.
  pages:
    - slug: partner-payment-link-metadata-api
      title: Payment link metadata API [New]
      type: basic
    - slug: partner-payment-link-payment-api
      title: Payment link payment API [New]
      type: basic
    - slug: partner-payment-link-verify-payment-api
      title: Verify payment link transaction API [New]
      type: basic
---
These three pages handle one partner payment link. Payment Link Metadata reads the link. Payment Link Payment starts payment with the customer's phone number. Verify Payment Link Transaction reads the status of that payment.

***

## Authentication

All three pages use a **Bearer token**.

| Environment | Base URL |
| :---------- | :------- |
| Test        | `https://test-partnerapilayer.payu.in/apilayer` |
| Production  | `https://api.payu.in` |

Send `Authorization: Bearer {access_token}` on every call.

| Page | Route | What you send |
| :--- | :---- | :------------ |
| Payment Link Metadata | `GET /partner/payment-link/metadata` | Query `payment_link` |
| Payment Link Payment | `POST /partner/payment-link/payment` | `payment_link_id` and `phone_number`. `redirect_url` is optional. |
| Verify Payment Link Transaction | `GET /partner/payment-link/verifyPayment` | Query `order_ref_id` and `payment_link_id` |

***

## Endpoints

These are the Payment Link pages.

<Cards>
  <Card title="Payment Link Metadata" href="https://docs.payu.in/reference/partner-payment-link-metadata-api" target="_blank">
    GET /partner/payment-link/metadata. Pass payment_link. Returns amount, currency, description, payment_link_id, payment_link_status, and expiry_time.
  </Card>
  <Card title="Payment Link Payment" href="https://docs.payu.in/reference/partner-payment-link-payment-api" target="_blank">
    POST /partner/payment-link/payment. Starts payment for payment_link_id and phone_number. The phone number is 5 to 16 digits. redirect_url is optional.
  </Card>
  <Card title="Verify Payment Link Transaction" href="https://docs.payu.in/reference/partner-payment-link-verify-payment-api" target="_blank">
    GET /partner/payment-link/verifyPayment. Requires order_ref_id and payment_link_id. Returns order_ref_id, payment_link_id, order_status, and payments. Each payment includes payment_id, status, method, and pg_error_message.
  </Card>
</Cards>

***

## How It Works

<Accordion title="Read the link" icon="fad fa-link">
  Call Payment Link Metadata with the `payment_link` query parameter. The page returns the amount, currency, description, link id, status, and expiry.
</Accordion>

<Accordion title="Start payment" icon="fad fa-credit-card">
  Call Payment Link Payment with `payment_link_id` and `phone_number`. Add `redirect_url` when the customer should return to your page.
</Accordion>

<Accordion title="Verify the transaction" icon="fab fa-searchengin">
  Call Verify Payment Link Transaction with `order_ref_id` and `payment_link_id`. The page returns `order_status` and the payments on that order.
</Accordion>
