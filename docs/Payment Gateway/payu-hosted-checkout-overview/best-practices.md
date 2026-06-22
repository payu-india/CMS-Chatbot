---
title: Best Practices
excerpt: >-
  Best practices for a smoother PayU Hosted Checkout integration and payment
  experience.
deprecated: false
hidden: true
metadata:
  robots: index
---
Follow these best practices for the easy integration of PayU hosted checkout and for a better payment experience.

<Accordion title="1. Always Generate Hash on Your Backend" icon="fa-server">
Generate the payment request forward hash only on your server and not on:
- Browser

- Mobile app

- Frontend JavaScript

- Public APIs

The hash uses your merchant salt, which is a secret credential.

If the salt is exposed, attackers can forge payment requests by tampering critical request values.
</Accordion>

***

<Accordion title="2. Never Consider Browser Redirect as Payment Success" icon="fa-triangle-exclamation">
It is not recommended to mark an order as paid only because the customer lands on `surl`. Browser redirects are unreliable because:

- Customer may close browser

- Network may fail

- Browser may crash

- Redirect may be intercepted

- Response may be spoofed

It is recommended to mark the order as paid only after:

- Reverse hash validation succeeds

- Callback/webhook is verified

- Payment status is confirmed
</Accordion>

***

<Accordion title="3. Use Unique Transaction IDs for Every Payment Attempt" icon="fa-fingerprint">
Make sure every payment attempt has a unique `txnid`. A unique transaction IDs help:

- Prevent duplicate processing

- Improve reconciliation

- Simplify support debugging
</Accordion>

***

<Accordion title="4. Implement Idempotency for Order Processing" icon="fa-shield-check">
Payment systems are asynchronous. You may receive:

- duplicate callbacks
- duplicate webhooks
- repeated retries
- customer refresh events

Recommended safeguards:

- DB uniqueness constraints
- Order state machine
- Idempotency keys
- Duplicate callback detection
</Accordion>

***

<Accordion title="5. Validate Reverse Hash for Every Response" icon="fa-shield-halved">
Reverse hash validation is mandatory. It authenticates the received response.

For every callback:
- Receive response

- Extract response hash

- Generate reverse hash

- Compare hashes

- Reject mismatches
</Accordion>

<br />
