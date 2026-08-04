---
title: Best Practices
deprecated: false
hidden: true
metadata:
  robots: index
---
These best practices apply across PayU API families. Product guides may add stricter requirements for subscriptions, payouts, or partner onboarding.

<Accordion title="Authentication and Secrets" icon="far fa-circle-user-circle-question">
  - Generate hashes and OAuth tokens **only on your server**.

  - Never ship salt, client secret, or Production keys in frontend or mobile binaries.

  - Rotate credentials immediately if leaked.

  - Keep Test and Production secrets in separate configuration spaces.

  Refer to the [API Authentication and Security](doc:api-authentication-and-security) for more information.
</Accordion>

<Accordion title="Payment Creation" icon="far fa-display-code">
  - Use a new unique `txnid` for every new payment attempt.

  - Persist `txnid` before calling PayU so callbacks can be correlated.

  - Send mandatory fields exactly as documented; avoid unused dummy values that break hash input.

  - Prefer HTTPS absolute URLs for `surl` and `furl`.
</Accordion>

<Accordion title="Status Confirmation" icon="far fa-sagittarius">
  - Treat redirect callbacks as **untrusted user browser events**.

  - Validate reverse hash on callbacks.

  - Confirm final success with [Verify Payment](ref:verify_payment_api) or equivalent server APIs.

  - Design for pending states — especially UPI and some bank flows.
</Accordion>

<Accordion title="Webhooks" icon="far fa-webhook">
  - Configure webhooks in the Dashboard for asynchronous reliability.

  - Verify signatures/reverse hashes.

  - Process events idempotently.

  - Return 2xx quickly; continue heavy fulfillment asynchronously.
</Accordion>

<Accordion title="Retries and Timeouts" icon="far fa-rectangle-history">
  - Use reasonable timeouts on server-to-server calls.

  - Retry transient network failures with backoff.

  - Do not blindly retry payment creation with the same `txnid` after an unknown result — verify first.

  - If you see throttling/rate-limit style errors, wait and retry with backoff.
</Accordion>

<Accordion title="Logging and Observability" icon="far fa-arrow-right-long-to-line">
  - Log request IDs, `txnid`, `mihpayid`, and response status codes.

  - Never log full card data, CVV, salt, or raw secrets.

  - Alert on spikes in hash mismatches, open pending payments, and webhook delivery failures.
</Accordion>

<Accordion title="Environment Hygiene" icon="far fa-objects-align-center-vertical">
  - Develop against Test hosts and Test credentials.

  - Switch host + key + salt together at go-live.

  - Re-test callbacks and webhooks on Production URLs.

  Refer to [API Environments and Base URLs](doc:api-environments-and-base-urls) and [Testing PayU APIs](doc:testing-payu-apis) for more information.
</Accordion>

<Accordion title="Design for Reconciliation" icon="far fa-circle-location-arrow">
  - Run periodic reconciliation jobs using transaction/settlement APIs.

  - Build admin tools to re-verify ambiguous orders.

  - Store raw PayU payloads for dispute and support windows.
</Accordion>

<Accordion title="Product-specific Caution" icon="far fa-list-timeline">
  | If you integrate… | Extra care                                                    |
  | :---------------- | :------------------------------------------------------------ |
  | S2S card flows    | PCI scope, OTP/native flows, and data handling                |
  | Subscriptions     | Consent state machine and recurring failure handling          |
  | Split settlements | Child merchant mapping and refund split behavior              |
  | Payouts           | OAuth token lifecycle and beneficiary validation              |
  | Cross-border      | Additional compliance documents and on-hold settlement states |
</Accordion>