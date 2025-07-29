---
title: PayU India API Reference - v2 APIs
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: PayU API Documentation
  description: >-
    This document is the PayU India API Reference documentation, which provides
    developers with information on how to integrate PayU's payment processing
    capabilities into their applications and websites. It includes a list of
    APIs and instructions on how to use them.
  keywords:
    - PayU APIs
    - ' PayU API documentation'
    - ' PayU API reference'
  robots: index
next:
  description: ''
---
You can find the following implementation using **v2/payments** API for collecting payments.

## General APIs

* **Check Transaction APIs**
  * [Verify Payment API](https://docs.payu.in/v2/reference/v2_verify_payment_api)
* **Refund APIs**
  * [Refund Transaction API](https://docs.payu.in/v2/reference/v2-refund-transaction-api)
  * [Refund Status API](https://docs.payu.in/v2/reference/v2-refund-status-api)
* [Validate VPA API](https://docs.payu.in/v2/reference/v2-validate-vpa-api)
* **BIN APIs**
  * [Eligible Bin for EMI API v2](https://docs.payu.in/v2/reference/eligible-bin-for-emi-api-v2)
  * [Get BIN Info API](https://docs.payu.in/v2/reference/v2-get-bin-info-api)
  * [Check is Domestic Card API](https://docs.payu.in/v2/reference/v2-check-is-domestic-card-api)
  * [Issuing Bank Status API](https://docs.payu.in/v2/reference/v2-issuing-bank-status-api)
  * [S2S Eligible BINs API](https://docs.payu.in/v2/reference/v2_s2s-eligible-bins-api)
* [Get Payment Details API](https://docs.payu.in/v2/reference/v2-get-payment-details-api)
* [Generate UPI Intent API](https://docs.payu.in/v2/reference/v2-generate-upi-intent-api)
* [Get Checkout Details](https://docs.payu.in/v2/reference/v2-get-checkout-details)

## Web integration

### Non-seamless integration

* [Non-Seamless Integration](https://docs.payu.in/v2/reference/collect-payment-api-payu-hosted-v2-_payment)

### Seamless integration

* [Net Banking ](https://docs.payu.in/v2/reference/_payment_v2_merchant_hosted_netbanking)
* [Cards](https://docs.payu.in/v2/reference/_payment-v2-merchant-hosted-cards)
* [UPI](https://docs.payu.in/v2/reference/_payment_v2_merchant_hosted_upi)
* [Wallet](https://docs.payu.in/v2/reference/collect_v2_payment_wallet)
* [EMI](https://docs.payu.in/v2/reference/collect-payments-with-emi-v2_payment)
* [BNPL](https://docs.payu.in/v2/reference/bnpl-v2_payment-merchant-hosted)

#### Flows

* [Cards Classic Integration](https://docs.payu.in/v2/reference/cards-classic-integration)
* [Cards Decoupled Flow](https://docs.payu.in/v2/reference/cards-decoupled-flow-s2s-v2-_payment)
* [Cards Direct Authorization Flow](https://docs.payu.in/v2/reference/cards-direct-authorization-flow-s2s-v2-_payment)
* [UPI](https://docs.payu.in/v2/reference/upi-s2s-_payment-v2)

## Save Cards

* [Simple REST APIs](https://docs.payu.in/v2/reference/model-3-simple-rest-apis)
  * [Get Payment Details API](https://docs.payu.in/v2/reference/v2-get-payment-details-api)
  * [Get Payment Instrument API](https://docs.payu.in/v2/reference/v2-get-payment-instrument-api)
  * [Save Card API](https://docs.payu.in/v2/reference/v2_save_card_api)
  * [Delete a Saved Card API](https://docs.payu.in/v2/reference/v2_delete-card-api)
* [Collect Payments - Save Card](https://docs.payu.in/v2/reference/collect-payments-save-card)
  * [Payment with Zero Code Change](https://docs.payu.in/v2/reference/zero-code-change-payment)
  * [Complete Card Details](https://docs.payu.in/v2/reference/complete-card-details-payment)
  * [Using Network Tokens](https://docs.payu.in/v2/reference/using-network-tokens)
* [Get User Cards API](https://docs.payu.in/v2/reference/v2_get_user_cards_api)

## Third-Party Verification

* [Non-Seamless](https://docs.payu.in/v2/reference/v2_tpv_collect_payment_api_non_seamless)
* [Seamless Integration](https://docs.payu.in/v2/reference/seamless-integration-tpv)
  * [NEFT Integration](https://docs.payu.in/v2/reference/v2_payment_tpv_merchant_hosted_v2_integration)
  * [UPI Integration](https://docs.payu.in/v2/reference/v2_payment_tpv_merchant_hosted_v2_integration-1)

## PreAuthorize Payment

* [Non-Seamless Integration](https://docs.payu.in/v2/reference/v2-payment-api-preauth-non-seamless)
* [Seamless Integration](https://docs.payu.in/v2/reference/payment-api-preauth-seamless)
* [Capture Transaction API](https://docs.payu.in/v2/reference/v2-capture-transaction-api)

## Get support

Should you encounter any issues or have questions during your integration process, our dedicated support team is here to assist you. Visit [https://help.payu.in](https://help.payu.in) and raise a ticket.