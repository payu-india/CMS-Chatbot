---
title: Partner Payment Integration APIs [New]
excerpt: >-
  Partner-layer APIs for payment callbacks, card OTP, offers, EMI, payment
  links, QR, and Bolt.
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  robots: index
next:
  description: Explore related information and resources.
  pages:
    - slug: payment-callbacks
      title: Payment Callbacks [New]
      type: basic
    - slug: card-otp
      title: Card OTP [New]
      type: basic
    - slug: offers
      title: Offers [New]
      type: basic
    - slug: emi
      title: EMI [New]
      type: basic
    - slug: payment-links
      title: Payment Links [New]
      type: basic
    - slug: qr-and-omnichannel
      title: QR and Omnichannel [New]
      type: basic
    - slug: bolt
      title: Bolt [New]
      type: basic
---
These APIs sit on the partner layer next to <Anchor target="_blank" href="https://docs.payu.in/reference/collect-payment-for-partners">Collect Payment for Partners</Anchor>. Use them for the payment result, card OTP, offers, EMI, payment links, QR, and Bolt.

<Callout icon="📘" theme="info">
  ### **Where the payment starts**

  Hosted checkout, UPI Intent S2S, and UPI TPV are documented under <Anchor target="_blank" href="https://docs.payu.in/reference/collect-payment-for-partners">Collect Payment for Partners</Anchor>. The pages in this section cover the other partner-layer endpoints.
</Callout>

***

## Authentication

| Environment | Base URL |
| :---------- | :------- |
| Test        | `https://test-partnerapilayer.payu.in/apilayer` |
| Production  | `https://api.payu.in` |

Each API page has the full path. The header set depends on the API.

| APIs | What to send |
| :--- | :----------- |
| Card OTP, Offers, EMI, Payment links | `Authorization: Bearer {access_token}` |
| Initiate payment, verify status, dynamic Bharat QR | `X-PayU-Reseller-UUID`, `X-Partner-Token`, and `Authorization` |
| Static QR | Those QR headers, plus `X-PayU-Merchant-ID`, `X-Partner-Hash`, and `X-Partner-Request-ID` |
| Bolt generate hash | `Authorization`, `X-PayU-Reseller-UUID`, and `X-PayU-Merchant-ID` |
| Payment callbacks, static QR callback, Bolt payment callback | PayU calls these routes. They are not requests the partner sends. |

<Callout icon="📘" theme="info">
  ### **Access token**

  Bearer-token APIs send the partner access token as `Authorization: Bearer {access_token}`. Older partner accounts generate that token with the <Anchor target="_blank" href="https://docs.payu.in/reference/token-generation-flow-for-old-partner-merchants">token generation flow for partner payments</Anchor>.
</Callout>

***

## Endpoints

### Payment callbacks

<Cards>
  <Card title="Payment Success Redirect Callback" href="https://docs.payu.in/reference/partner-payment-success-api" target="_blank">
    PayU receives a successful hosted-checkout result, then sends the customer to surl.
  </Card>
  <Card title="Payment Failure Redirect Callback" href="https://docs.payu.in/reference/partner-payment-failed-api" target="_blank">
    PayU receives a failed hosted-checkout result, then sends the customer to furl.
  </Card>
  <Card title="Payment Cancelled Redirect Callback" href="https://docs.payu.in/reference/partner-payment-cancelled-api" target="_blank">
    PayU receives the result when the customer cancels on hosted checkout.
  </Card>
  <Card title="Payment S2S Callback" href="https://docs.payu.in/reference/partner-payment-callback-api" target="_blank">
    Server-to-server payment postback. PayU returns an empty HTTP 200.
  </Card>
  <Card title="Partner Refund Callback" href="https://docs.payu.in/reference/partner-refund-callback-api" target="_blank">
    Refund notification. The body can be the standard or the migrated refund callback.
  </Card>
</Cards>

### Card OTP

<Cards>
  <Card title="Submit Card OTP" href="https://docs.payu.in/reference/partner-submit-card-otp-api" target="_blank">
    Submit the OTP for a reference id. A verified OTP returns the transaction status and mihpayid.
  </Card>
  <Card title="Resend Card OTP" href="https://docs.payu.in/reference/partner-resend-card-otp-api" target="_blank">
    Resend the OTP for the same reference id.
  </Card>
</Cards>

### Offers

<Cards>
  <Card title="Fetch Offers" href="https://docs.payu.in/reference/partner-fetch-offer-api" target="_blank">
    Return offers for a merchant. Amount, offer keys, payment id, user token, and SKU details are optional.
  </Card>
  <Card title="Validate Offer" href="https://docs.payu.in/reference/partner-validate-offer-api" target="_blank">
    Check an offer against the payment category and the customer.
  </Card>
</Cards>

### EMI

<Cards>
  <Card title="Get EMI Amount" href="https://docs.payu.in/reference/partner-get-emi-amount-api" target="_blank">
    EMI amount for a merchant and a transaction amount.
  </Card>
  <Card title="Get Eligible EMI Bins" href="https://docs.payu.in/reference/partner-get-eligible-bins-api" target="_blank">
    Bins that are eligible for EMI.
  </Card>
  <Card title="Calculate EMI" href="https://docs.payu.in/reference/partner-calculate-emi-api" target="_blank">
    Calculate EMI for a merchant. Amount and bank code can be sent with the request.
  </Card>
</Cards>

### Payment links

<Cards>
  <Card title="Payment Link Metadata" href="https://docs.payu.in/reference/partner-payment-link-metadata-api" target="_blank">
    Amount, currency, description, status, and expiry for a payment link.
  </Card>
  <Card title="Payment Link Payment" href="https://docs.payu.in/reference/partner-payment-link-payment-api" target="_blank">
    Start payment with the payment link id and the customer phone number.
  </Card>
  <Card title="Verify Payment Link Transaction" href="https://docs.payu.in/reference/partner-payment-link-verify-payment-api" target="_blank">
    Payment status for an order reference and a payment link.
  </Card>
</Cards>

### QR and omnichannel

<Cards>
  <Card title="Initiate Payment" href="https://docs.payu.in/reference/partner-initiate-payment-api" target="_blank">
    Start an omnichannel payment for an account id.
  </Card>
  <Card title="Verify Omnichannel Transaction Status" href="https://docs.payu.in/reference/partner-transaction-verify-status-api" target="_blank">
    Check the status of an omnichannel transaction.
  </Card>
  <Card title="Dynamic Bharat QR" href="https://docs.payu.in/reference/partner-dbqr-api" target="_blank">
    Create a dynamic Bharat QR for a soundbox terminal.
  </Card>
  <Card title="Static QR" href="https://docs.payu.in/reference/partner-static-qr-api" target="_blank">
    Create a reusable static QR for a merchant VPA.
  </Card>
  <Card title="Static QR Callback" href="https://docs.payu.in/reference/partner-static-qr-callback-api" target="_blank">
    PayU receives the static QR payment result.
  </Card>
</Cards>

### Bolt

<Cards>
  <Card title="Bolt Generate Hash" href="https://docs.payu.in/reference/partner-bolt-generate-hash-api" target="_blank">
    Build the payload that is passed to bolt.launch.
  </Card>
  <Card title="Bolt Payment Callback" href="https://docs.payu.in/reference/partner-bolt-payment-callback-api" target="_blank">
    PayU receives the Bolt checkout postback and returns an empty body.
  </Card>
</Cards>

***

## How It Works

<Accordion title="Get an access token" icon="fad fa-key-skeleton-left-right">
  Send the partner access token as `Authorization: Bearer {access_token}` on Bearer-token APIs. Older partner accounts use the <Anchor target="_blank" href="https://docs.payu.in/reference/token-generation-flow-for-old-partner-merchants">token generation flow for partner payments</Anchor>. QR and Bolt calls also send the reseller headers listed on those pages.
</Accordion>

<Accordion title="Collect the payment" icon="fad fa-credit-card">
  Start the payment with <Anchor target="_blank" href="https://docs.payu.in/reference/collect-payment-for-partners">Collect Payment for Partners</Anchor>, a payment link, QR, or Bolt.
</Accordion>

<Accordion title="Receive the result" icon="fad fa-hand-point-left">
  PayU posts the hosted-checkout result to the success, failure, or cancelled route, and posts the server-to-server result to the payment callback. Refunds arrive on the refund callback.
</Accordion>

<Accordion title="Check status when you need it" icon="fab fa-searchengin">
  Use verify payment under Collect Payment for Partners, verify payment link, or verify omnichannel transaction status for the channel you used.
</Accordion>
