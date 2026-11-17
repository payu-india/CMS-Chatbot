---
title: Best Practices
excerpt: Practices that follow how Checkout Plus actually behaves on your page
deprecated: false
hidden: false
updatedAt: "2026-11-17"
metadata:
  title: Checkout Plus Best Practices | PayU Developer Docs
  description: >-
    Checkout Plus best practices for the in-modal retry, customer fields, unique
    transaction IDs, Verify Payment, and keeping Bolt out of an in-app WebView.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

These practices come from the Checkout Plus overview, the launch contract, and the response rules. They are not a copy of the PayU Hosted Checkout best-practices page. That page describes a full-page redirect.

## Keep the Customer in the Modal

The overview says that when a payment fails at the bank or on the 3-D Secure page, the customer can return to the Checkout Plus payment form and continue the current order, without starting checkout again.

The customer journey shows the same idea for UPI: on failure, Retry returns the customer to the payment flow.

## Pass the Customer Details You Already Have

The UPI journey starts with the customer entering a mobile number and email on your page, then clicking Buy Now. The launch request requires `firstname`, `email`, and `phone`. Pass the values you collected. The published sample does not show the modal asking for those three fields again.

## Use a Transaction ID Only Once

`txnid` is your order reference. The parameter description says it can be used only once, and that PayU does not accept a duplicate transaction ID.

<!-- DOCUMENTATION GAP: Character length, allowed characters, and a recommended txnid format are not documented for Checkout Plus. -->

## Decide What Retry Means for txnid

<!-- VALIDATION NEEDED: Checkout Plus says the customer continues the current order after a failure, without starting the transaction process again. PayU Hosted Checkout best practices say each retry needs a new txnid and a new hash. The Checkout Plus pages never say whether Retry reuses txnid or requires a new one. Do not write a retry procedure until the docs team confirms this. -->

Until that is confirmed, do not invent a retry implementation. What is documented:

- The customer can retry from the Checkout Plus form without going back to the start of your checkout.
- A duplicate `txnid` is not accepted.

## Fulfil Only After Verify Payment

The launch sample treats `BOLT.response.txnStatus` of `SUCCESS` as a successful payment in the browser. The API page says the [Verify Payment API](https://docs.payu.in/reference/verify_payment_api) (`verify_payment`) retrieves status for reconciliation with PayU.

Fulfil the order only after that server call agrees with the result you are about to honour. The launch sample itself does not call Verify Payment.

<!-- DOCUMENTATION GAP: The Checkout Plus pages do not include the Verify Payment request body. -->

## Pending

The response table says `status` may be `success`, `failure`, or `pending`, and that you should treat `failure` or `pending` as a failed transaction.

<!-- VALIDATION NEEDED: That pending rule is what the Checkout Plus response table states. It is not the same as the PayU Hosted Checkout guidance to leave pending open and wait for a final status. Do not copy NEFT or RTGS pending handling onto this page. -->

`unmappedstatus` can also be `pending`, along with `dropped`, `bounced`, `captured`, `auth`, `failed`, and `usercancelled`. The page links those values to [Payment State Explanations](ref:payment-state-explanations) and does not define a customer message for each one.

## Do Not Open the Bolt Modal in a WebView

The integrate page says Checkout Plus is not recommended for app browsers such as WebView or Chrome Custom Tabs. Use redirection-based [PayU Hosted Checkout](../payu-hosted-checkout-1) for that case, including the [Hosted Checkout WebView guide](../payu-hosted-checkout-1/payu-hosted-checkout-webview-integration).

The older Checkout Plus WebView notes are restructured on [WebView for Mobile Apps](./integrate-webview-for-mobile-apps-checkout-plus). That page is hidden. It documents an Android `loadUrl` setup. It does not call `bolt.launch()`.

## Modal Controls That Change What the Customer Sees

Only these fields are documented:

| Field | Documented behaviour |
| --- | --- |
| `enforce_paymethod` | Enforce payment modes, card schemes, and specific net-banking banks. Sample: `creditcard\|debitcard\|HDFB\|AXIB` |
| `drop_category` | Hide one or more payment options. Sample: `creditcard\|debitcard` |
| `custom_note` | Note for the transaction. |
| `note_category` | Limits where `custom_note` appears. Source example: `CC, NB` for Credit Card and Net Banking. |
| `display_lang` | The launch sample sets `Hindi`. |

<!-- DOCUMENTATION GAP: No list of display_lang values is published in the Checkout Plus pages. Do not copy the Hosted Checkout language table into this page. -->
