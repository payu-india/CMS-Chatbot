---
title: Partner Payment Integration APIs [New]
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  robots: index
---
These APIs are the partner-layer endpoints for payment callbacks, card OTP, offers, EMI, payment links, QR, and Bolt. Open a section below for the summary, then the API page for the request and response.

## Payment callbacks

PayU receives the hosted-checkout result, the server-to-server payment postback, and the refund notification on these routes. These are PayU endpoints. They are not URLs the partner hosts.

* [Payment Success Redirect Callback API](ref:partner-payment-success-api)
* [Payment Failure Redirect Callback API](ref:partner-payment-failed-api)
* [Payment Cancelled Redirect Callback API](ref:partner-payment-cancelled-api)
* [Payment S2S Callback API](ref:partner-payment-callback-api)
* [Partner Refund Callback API](ref:partner-refund-callback-api)

## Card OTP

Submit or resend the OTP for a card payment.

* [Submit card OTP API](ref:partner-submit-card-otp-api)
* [Resend card OTP API](ref:partner-resend-card-otp-api)

## Offers

Fetch the offers available for a merchant, or validate one offer against the payment and the customer.

* [Fetch offers API](ref:partner-fetch-offer-api)
* [Validate offer API](ref:partner-validate-offer-api)

## EMI

Read the EMI amount, the bins that can use EMI, or a calculated EMI plan.

* [Get EMI amount API](ref:partner-get-emi-amount-api)
* [Get eligible EMI bins API](ref:partner-get-eligible-bins-api)
* [Calculate EMI API](ref:partner-calculate-emi-api)

## Payment links

Read a payment link, start payment on it, and verify the transaction.

* [Payment link metadata API](ref:partner-payment-link-metadata-api)
* [Payment link payment API](ref:partner-payment-link-payment-api)
* [Verify payment link transaction API](ref:partner-payment-link-verify-payment-api)

## QR and omnichannel

Start an omnichannel payment, check its status, or create a dynamic Bharat QR or a static QR.

* [Initiate payment API](ref:partner-initiate-payment-api)
* [Verify omnichannel transaction status API](ref:partner-transaction-verify-status-api)
* [Dynamic Bharat QR API](ref:partner-dbqr-api)
* [Static QR API](ref:partner-static-qr-api)
* [Static QR callback API](ref:partner-static-qr-callback-api)

## Bolt

Create the hash payload for Bolt checkout, and receive the Bolt payment postback.

* [Bolt generate hash API](ref:partner-bolt-generate-hash-api)
* [Bolt payment callback API](ref:partner-bolt-payment-callback-api)
