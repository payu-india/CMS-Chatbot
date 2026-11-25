---
title: Partner Payment Integration APIs [New]
excerpt: >-
  Overview of the partner payment pages for callbacks, card OTP, offers, EMI,
  payment links, QR, and Bolt.
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
This section lists the partner payment API pages. Payment Callbacks receives the payment and refund result. Card OTP submits or resends a card OTP. Offers fetches and validates offers. EMI reads the EMI amount, eligible bins, and a calculated plan. Payment Links reads a link, starts payment, and verifies it. QR and Omnichannel starts an omnichannel payment, checks its status, and creates a dynamic or static QR. Bolt builds the checkout hash and receives the Bolt postback.

***

## Authentication

| Environment | Base URL |
| :---------- | :------- |
| Test        | `https://test-partnerapilayer.payu.in/apilayer` |
| Production  | `https://api.payu.in` |

The pages below use the header set in this table. Each page has the full path.

| Pages | What the page uses |
| :---- | :----------------- |
| Submit Card OTP, Resend Card OTP, Fetch Offers, Validate Offer, Get EMI Amount, Get Eligible EMI Bins, Calculate EMI, Payment Link Metadata, Payment Link Payment, Verify Payment Link Transaction | `Authorization: Bearer {access_token}` |
| Initiate Payment, Verify Omnichannel Transaction Status, Dynamic Bharat QR | `X-PayU-Reseller-UUID`, `X-Partner-Token`, and `Authorization` |
| Static QR | `X-PayU-Reseller-UUID`, `X-PayU-Merchant-ID`, `X-Partner-Token`, `X-Partner-Hash`, and `X-Partner-Request-ID` |
| Bolt Generate Hash | `Authorization`, `X-PayU-Reseller-UUID`, and `X-PayU-Merchant-ID` |
| Payment Success, Payment Failure, Payment Cancelled, Payment S2S Callback, Partner Refund Callback, Static QR Callback, Bolt Payment Callback | PayU calls the route. The page documents the post PayU receives. |

***

## Endpoints

These are the pages in this section.

### Payment Callbacks

PayU receives the hosted-checkout result, the server-to-server payment postback, and the refund notification.

<Cards>
  <Card title="Payment Success Redirect Callback" href="https://docs.payu.in/reference/partner-payment-success-api" target="_blank">
    POST /partner/paymentSuccess. PayU receives the hosted-checkout result after a successful payment, then sends the customer to surl.
  </Card>
  <Card title="Payment Failure Redirect Callback" href="https://docs.payu.in/reference/partner-payment-failed-api" target="_blank">
    POST /partner/paymentFailed. PayU receives the failed result. error and error_Message carry the gateway reason, then the customer is sent to furl.
  </Card>
  <Card title="Payment Cancelled Redirect Callback" href="https://docs.payu.in/reference/partner-payment-cancelled-api" target="_blank">
    POST /partner/paymentCancelled. PayU receives the hosted-checkout result when the customer cancels.
  </Card>
  <Card title="Payment S2S Callback" href="https://docs.payu.in/reference/partner-payment-callback-api" target="_blank">
    POST /partner/paymentCallback. Server-to-server payment postback. PayU returns HTTP 200 with an empty body after it notifies the partner webhook.
  </Card>
  <Card title="Partner Refund Callback" href="https://docs.payu.in/reference/partner-refund-callback-api" target="_blank">
    POST /partner/refundCallback. Refund notification. The body can be the standard refund callback or the migrated callback (paymentId, refundId, refundAmount, refundStatus).
  </Card>
</Cards>

### Card OTP

Submit the OTP for a card payment, or send it again for the same reference id.

<Cards>
  <Card title="Submit Card OTP" href="https://docs.payu.in/reference/partner-submit-card-otp-api" target="_blank">
    POST /partner/submitCardOtp. Requires merchant_id, reseller_id, hash, reference_id, and otp. A verified OTP returns txnStatus, mihpayid, and "OTP verified successfully".
  </Card>
  <Card title="Resend Card OTP" href="https://docs.payu.in/reference/partner-resend-card-otp-api" target="_blank">
    POST /partner/resendCardOtp. Requires merchant_id, reseller_id, hash, and reference_id. A success message is "OTP resent successfully".
  </Card>
</Cards>

### Offers

Fetch the offers for a merchant, or validate one offer before payment.

<Cards>
  <Card title="Fetch Offers" href="https://docs.payu.in/reference/partner-fetch-offer-api" target="_blank">
    POST /partner/fetchOffer. Requires merchant_id, reseller_id, and hash. amount, offerKeys, paymentId, userToken, and skusDetail are optional. The response is the Offers service JSON.
  </Card>
  <Card title="Validate Offer" href="https://docs.payu.in/reference/partner-validate-offer-api" target="_blank">
    POST /partner/validateOffer. Requires merchant_id, reseller_id, hash, paymentDetail.category, and userDetail.userToken. The response is the Offers validate JSON.
  </Card>
</Cards>

### EMI

Read an EMI amount, the bins that can use EMI, or a calculated EMI plan.

<Cards>
  <Card title="Get EMI Amount" href="https://docs.payu.in/reference/partner-get-emi-amount-api" target="_blank">
    POST /partner/getEmiAmount. Requires merchant_id and amount. merchant_id must be digits. bankcode and tenure can be sent with the request.
  </Card>
  <Card title="Get Eligible EMI Bins" href="https://docs.payu.in/reference/partner-get-eligible-bins-api" target="_blank">
    POST /partner/getEligibleBins. Requires merchant_id, type, and var2. The request is forwarded to the eligible-bins service.
  </Card>
  <Card title="Calculate EMI" href="https://docs.payu.in/reference/partner-calculate-emi-api" target="_blank">
    POST /partner/calculateEmi. Requires merchant_id. amount and bankcode can be sent with the request.
  </Card>
</Cards>

### Payment Links

Read a payment link, start payment on it, and verify the transaction.

<Cards>
  <Card title="Payment Link Metadata" href="https://docs.payu.in/reference/partner-payment-link-metadata-api" target="_blank">
    GET /partner/payment-link/metadata. Query parameter payment_link. Returns amount, currency, description, payment_link_id, payment_link_status, and expiry_time.
  </Card>
  <Card title="Payment Link Payment" href="https://docs.payu.in/reference/partner-payment-link-payment-api" target="_blank">
    POST /partner/payment-link/payment. Requires payment_link_id and phone_number (5 to 16 digits). redirect_url is optional.
  </Card>
  <Card title="Verify Payment Link Transaction" href="https://docs.payu.in/reference/partner-payment-link-verify-payment-api" target="_blank">
    GET /partner/payment-link/verifyPayment. Requires order_ref_id and payment_link_id. Returns order_status and the payments on that order.
  </Card>
</Cards>

### QR and Omnichannel

Start an omnichannel payment, check its status, or create a dynamic Bharat QR or a static QR.

<Cards>
  <Card title="Initiate Payment" href="https://docs.payu.in/reference/partner-initiate-payment-api" target="_blank">
    POST /partner/initiatePayment. Requires accountId. txnId, amount, and callBackActions are read when they are sent. The body is forwarded to Core Payments.
  </Card>
  <Card title="Verify Omnichannel Transaction Status" href="https://docs.payu.in/reference/partner-transaction-verify-status-api" target="_blank">
    POST /partner/transaction/verifyStatus. txnId is forwarded with the rest of the body to the Bharat QR status command.
  </Card>
  <Card title="Dynamic Bharat QR" href="https://docs.payu.in/reference/partner-dbqr-api" target="_blank">
    POST /partner/dbqr. Reads vendorTransactionId, soundBoxTerminalId, expiryTime, and mihpayId when they are sent. The body is forwarded to the dynamic Bharat QR API.
  </Card>
  <Card title="Static QR" href="https://docs.payu.in/reference/partner-static-qr-api" target="_blank">
    POST /partner/staticQr. Requires merchantVpa. Returns a reusable QR. X-Partner-Hash is the SHA-512 of merchantId, the raw body, and the client secret.
  </Card>
  <Card title="Static QR Callback" href="https://docs.payu.in/reference/partner-static-qr-callback-api" target="_blank">
    POST /partner/staticQrCallback. PayU receives the static QR result. field4 (merchant VPA) and key are required.
  </Card>
</Cards>

### Bolt

Build the payload passed to bolt.launch, and receive the Bolt checkout postback.

<Cards>
  <Card title="Bolt Generate Hash" href="https://docs.payu.in/reference/partner-bolt-generate-hash-api" target="_blank">
    POST /partner/bolt/generateHash. Requires txnid, amount, productinfo, firstname, email, phone, surl, and furl. The 200 body is the bolt.launch payload.
  </Card>
  <Card title="Bolt Payment Callback" href="https://docs.payu.in/reference/partner-bolt-payment-callback-api" target="_blank">
    POST /partner/bolt/paymentCallback. PayU receives the Bolt checkout postback and returns an empty body.
  </Card>
</Cards>

***

## How It Works

<Accordion title="Payment Callbacks" icon="fad fa-hand-point-left">
  Open Payment Callbacks for the five routes PayU calls: payment success, payment failure, payment cancelled, the server-to-server payment callback, and the refund callback.
</Accordion>

<Accordion title="Card OTP" icon="fad fa-key-skeleton-left-right">
  Open Card OTP to submit an OTP for a reference id, or to resend that OTP.
</Accordion>

<Accordion title="Offers" icon="fad fa-tags">
  Open Offers to fetch offers for a merchant, or to validate one offer against the payment category and the customer.
</Accordion>

<Accordion title="EMI" icon="fad fa-calculator">
  Open EMI to get an EMI amount, list eligible bins, or calculate an EMI plan.
</Accordion>

<Accordion title="Payment Links" icon="fad fa-link">
  Open Payment Links to read a link, start payment with a phone number, and verify the transaction.
</Accordion>

<Accordion title="QR and Omnichannel" icon="fad fa-qrcode">
  Open QR and Omnichannel to initiate a payment, verify its status, create a dynamic Bharat QR, create a static QR, or receive the static QR callback.
</Accordion>

<Accordion title="Bolt" icon="fad fa-credit-card">
  Open Bolt to generate the hash payload for bolt.launch, then receive the Bolt payment callback.
</Accordion>
