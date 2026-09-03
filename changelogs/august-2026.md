---
title: August 2026
author: Raghuram Pandurangan
hidden: false
metadata:
  title: PayU Payments August 2026 Release Notes or Changelogs
  description: >-
    Discover PayU payment capabilities, API enhancements, and integration
    changes for August 2026. This changelog is for merchants and developers
    integrating PayU APIs. Availability can depend on merchant activation,
    payment-method support, or eligibility described in the relevant entry.
published_at: '2026-09-01T05:55:45.907Z'
---
Discover PayU payment capabilities, API enhancements, and integration changes for August 2026. This changelog is for merchants and developers integrating PayU APIs. Availability can depend on merchant activation, payment-method support, or eligibility described in the relevant entry.

## API

<Accordion title="Instant Refunds for eligible transactions" icon="fa-code">
  <Columns layout="auto">
    <Column>
      <div style={{ borderLeft: '3px solid #208B75', paddingLeft: '16px' }}>

        **Date:** August 6, 2026  
        **Product:** Refunds  
        **Feature/API:** Instant Refunds  
        **Impact:** Medium  
        **Breaking Change:** No  
        **Action Required:** Optional, subject to enablement and eligibility
      </div>
    </Column>
  </Columns>

  **Summary**

  When Instant Refunds are enabled for a merchant and a transaction is eligible, PayU can complete the refund within five minutes of the request. Merchants can initiate a full or partial refund from the PayU Dashboard or through the **Refund Transaction&#x20;**&#x41;PI.

  **Why this matters**

  Eligible customers can receive a faster refund to the original payment source, while merchants can use either an operations-led dashboard workflow or an automated API workflow.

  **Who is affected**

  - Merchants with Instant Refunds enabled.
  - Developers initiating and tracking refunds through APIs.
  - Operations teams initiating refunds from the PayU Dashboard.

  **What's new**

  - Initiate full or partial refunds for eligible transactions.
  - Use the PayU Dashboard for manual refund initiation or `cancel_refund_transaction` through the Refund Transaction API for automated initiation.
  - The documented refund modes include PayU routing, UPI, IMPS, and NEFT, with the required beneficiary fields depending on the mode.
  - When the PayU mode is used, PayU checks alternate instant-refund channels and falls back to the normal refund channel when an instant channel is not available.
  - Track progress through the documented refund status APIs, webhooks, or dashboard.

  **Action required**

  Confirm that Instant Refunds are enabled for the merchant, check the transaction and payment-method eligibility, and implement the selected Dashboard or API workflow. Handle a standard refund when the transaction or payment method is not eligible for instant processing.

  **Need to migrate**

  No migration is required for existing refund integrations. Activation is required, and eligibility varies by payment method, transaction status, and other risk or compliance checks. Unsupported or ineligible requests follow the standard refund flow.

  **Related documentation**

  - [Instant Refunds](doc:instant-refunds)
  - [Instant Refunds API parameters and modes](ref:instant-refunds-1)
  - [Refund Transaction API](ref:refund_transaction_api)
</Accordion>

<Accordion title="Get Checkout Details API" icon="fa-code">
  <Columns layout="auto">
    <Column>
      <div style={{ borderLeft: '3px solid #208B75', paddingLeft: '16px' }}>

        **Date:** August 5, 2026  
        **Product:** Checkout and payment-option discovery  
        **Feature/API:** Get Checkout Details  
        **Impact:** High for migrated merchants  
        **Breaking Change:** Yes for merchants still calling the legacy V2 path  
        **Action Required:** Required for affected integrations
      </div>
    </Column>
  </Columns>

  **Summary**

  Migrated merchants must use the Get Checkout Details API contract. The endpoints are listed here: <br />HTTP Method: `POST `&#x20;

  - **Production**: `https://api.payu.in/fems/v1/checkout/detail`&#x20;
  - **Test**: `https://apitest.payu.in/fems/v1/checkout/detail`&#x20;

  **Why this matters**

  The API provides the payment-option, EMI, charge, tax, downtime, and eligibility details needed to build a current custom checkout flow for migrated merchants.

  **Who is affected**

  - Developers integrating Get Checkout Details for new or updated custom checkouts.
  - Systems still sending requests to the legacy V2 GCD path.

  **What's new**

  - Use the JSON request contract at `/fems/v1/checkout/detail`.
  - Send `Content-Type: application/json` and `accept: application/json`.
  - Send a current UTC `Date` header and a signed `Authorization` header using the documented HMAC-SHA512 format.
  - Compute the signature from the exact raw JSON request body, the same `Date` value, and the merchant secret as documented: `sha512(raw_request_body|Date|merchant_secret)`.
  - The response supports payment-option details, extended EMI details, additional charges, tax configuration, downtime status, and customer eligibility.

  **Action required**

  Change affected integrations from the legacy V2 GCD path to the new endpoint. Generate a fresh `Date` and `Authorization` value for every request, and ensure the body used for signing exactly matches the body sent.

  **Need to migrate**

  Yes. Merchants migrated to this API must use the new endpoint and header-authentication contract. This entry does not change integrations that do not call Get Checkout Details.

  **Related documentation**

  - [Get Checkout Details API](ref:get_checkout_details)
  - [Get Checkout Details API contract](https://docs.payu.in/reference/get_checkout_details)
</Accordion>