---
title: PayU Hosted Checkout APIs
excerpt: >-
  API reference index for PayU Hosted Checkout: collect payment, verify
  transaction, check EMI eligibility, and webhook events.
deprecated: false
hidden: true
metadata:
  title: PayU Hosted Checkout APIs
  description: >-
    Complete API reference for PayU Hosted Checkout: Collect Payment API, Verify
    Payment API, Get Checkout Details, EMI eligibility APIs, and webhook events.
  keywords:
    - payu hosted checkout api reference
    - payu _payment api collect payment endpoint
    - payu verify payment api india
    - payu emi eligibility bin api
    - payu get checkout details api
    - payu webhook events hosted checkout
    - payu hosted checkout api list
  robots: index
next:
  description: Explore related information and resources.
  pages:
    - slug: payu-hosted-checkout-1
      title: PayU Hosted Checkout
      type: basic
    - slug: payu-hosted-checkout-workflow
      title: How PayU Hosted Checkout Works
      type: basic
    - slug: payu-hosted-checkout-quick-start
      title: Quick Start
      type: basic
    - slug: integrate-payu-hosted-checkout
      title: Integrate PayU Hosted Checkout
      type: basic
    - slug: customise-payu-hosted-checkout
      title: Customise PayU Hosted Checkout
      type: basic
    - slug: payu-hosted-checkout-webview-integration
      title: PayU Hosted Checkout WebView Integration
      type: basic
    - slug: payu-hosted-checkout-best-practices
      title: Best Practices
      type: basic
    - slug: payu-hosted-errors-troubleshooting
      title: Errors and Troubleshooting
      type: basic
    - slug: payu-hosted-checkout-faqs
      title: FAQs (Frequently Asked Questions)
      type: basic
---
{/* NEW CONTENT: This page replaces and expands the existing "APIs used for Integration" page (list-of-apis-used-for-payu-hosted-checkout-integration.md). That page listed EMI-specific APIs only. This page covers all APIs used in the full integration flow. */}

These are the APIs used in a complete PayU Hosted Checkout integration.

***

## Collect Payment

| Use case               | API Reference                                                                   | Description                                                                                                                   |
| ---------------------- | ------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Initiate a transaction | [Collect Payment API — PayU Hosted Checkout](ref:_payment_payu_hosted_checkout) | POST payment request to the PayU-hosted payment page. Customers complete payment and are redirected back via `surl` / `furl`. |

**Endpoint:**

| Environment | URL                               |
| ----------- | --------------------------------- |
| Test        | `https://test.payu.in/_payment`   |
| Production  | `https://secure.payu.in/_payment` |

**Method:** `POST` | **Content-Type:** `application/x-www-form-urlencoded`

See [Build Integration](./integrate/build-integration) for the full request parameter reference and code samples.

***

## Verify Payment

| Use case                  | API Reference                                | Description                                                                                                                                     |
| ------------------------- | -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Verify transaction status | [Verify Payment API](ref:verify_payment_api) | Poll from your server to confirm the transaction status after payment. Use when you need programmatic confirmation beyond the browser callback. |

<Callout icon="✅" theme="okay">
  **Recommended verification order:** (1) Reverse hash validation → (2) Webhook → (3) Verify Payment API → (4) PayU Dashboard. Use the Verify Payment API as a fallback when your webhook did not arrive or you need to reconcile a specific transaction.
</Callout>

***

## Check Checkout Eligibility (EMI)

These APIs check customer or card eligibility before initiating an EMI transaction.

| Use case                        | API Reference                                                                                   | Description                                                                                                                    |
| ------------------------------- | ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| Check customer eligibility      | [Get Checkout Details API](ref:get_checkout_details)                                            | Check customer eligibility by mobile number for debit-card pre-EMI and cardless EMI.                                           |
| Calculate EMI amounts           | [Get EMI According to Interest API](ref:get_emi_according_to_interest_api)                      | Calculate interest, monthly instalment, processing fee, No-Cost EMI, tenure, and the corresponding `bankcode` for an EMI plan. |
| Check card BIN eligibility (v1) | [Eligible BINs for EMI API v1.0](ref:eligiblebinsforemi)                                        | Check credit-card EMI eligibility from the card BIN. Returns the issuing bank and minimum eligible amount.                     |
| Check card BIN eligibility (v2) | [Eligible BINs for EMI API v2.0](https://docs.payu.in/v2/reference/eligible-bin-for-emi-api-v2) | Check EMI eligibility by card BIN or network token. Returns the issuing bank and minimum eligible amount.                      |

***

## Webhooks

Webhooks provide server-to-server payment notifications and are more reliable than browser callbacks.

| Use case                             | Reference                                                                                          |
| ------------------------------------ | -------------------------------------------------------------------------------------------------- |
| Receive payment status notifications | [Webhook Events and Sample Payloads](https://docs.payu.in/docs/webhook-events-and-sample-payloads) |

Configure your webhook endpoint in PayU Dashboard → Developer Settings → Webhooks.

***

## Security

{/* Source: Hash authentication requirement from prebuilt-checkout-page-integration.md; General API hash formula from docs/API basics/api-authentication-and-security.md reference; response verification from build-integration.md Step 1.4. */}

**Collect Payment API — every request must be hash-authenticated.** The `hash` parameter in your payment request is a SHA-512 digest of the transaction parameters computed server-side using your merchant salt. PayU recomputes this hash on receipt and rejects any request where the values don't match. Never generate this hash in the browser or mobile app — doing so exposes your salt.

**Verify Payment API and General APIs — separate hash formula.** The Collect Payment endpoint uses the payment-specific hash formula. The Verify Payment API and other General APIs use a different formula: `sha512(key|command|var1|salt)`. See [API Authentication](https://docs.payu.in/docs/api-authentication-and-security) for the full General API authentication requirements.

**Always verify PayU's response before updating order status.** When PayU POSTs a result to your `surl`, `furl`, or webhook endpoint, your server must validate the reverse hash before marking any order as paid. See [Build Integration → Step 1.4](./integrate/build-integration#step-14-verify-response-via-reverse-hashing).

***

## Related Guides

- [Build Integration](./integrate/build-integration) — full parameter reference and code samples for the Collect Payment API
- [Test Integration](./integrate/test-integration) — test credentials and payment scenarios
- [Errors and Troubleshooting](./errors-and-troubleshooting) — error codes and fixes
