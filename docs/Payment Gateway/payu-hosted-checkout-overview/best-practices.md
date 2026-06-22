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

<Accordion title="## 1. Always Generate Hash on Your Backend" icon="fa-server">
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

### Recommended Source of Truth

Priority order:

1. Webhook
2. Server callback
3. Transaction verification API
4. Browser redirect (informational only)

### Common Mistake

```text
If user reaches success page → mark order paid
```

Avoid this.

***

## 3. Use Unique Transaction IDs for Every Payment Attempt

Every payment attempt must have a unique `txnid`.

### Best Practice

Generate transaction IDs using:

- UUID
- Order ID + retry count
- Timestamp-based IDs

Examples:

- ORD123\_ATTEMPT1
- ORD123\_ATTEMPT2
- TXN\_20260622\_0001

### Why this matters

Unique transaction IDs help:

- prevent duplicate processing
- improve reconciliation
- simplify support debugging

### Common Mistake

Reusing same transaction ID for retries.

This causes:

- duplicate payment confusion
- reconciliation issues
- inconsistent callbacks

***

## 4. Implement Idempotency for Order Processing

Payment systems are asynchronous.

You may receive:

- duplicate callbacks
- duplicate webhooks
- repeated retries
- customer refresh events

### Best Practice

Ensure:
**One successful payment = One order fulfillment**

Recommended safeguards:

- DB uniqueness constraints
- Order state machine
- Idempotency keys
- Duplicate callback detection

Example:

```text
if order.status == PAID:
   ignore duplicate callback
```

### Common Mistake

Shipping the same order twice because callback processed twice.

***

## 5. Validate Reverse Hash for Every Response

Reverse hash validation is mandatory.

Why?
It confirms the response originated from PayU and wasn’t tampered with.

### Best Practice

For every callback:

1. Receive response
2. Extract response hash
3. Generate reverse hash
4. Compare hashes
5. Reject mismatches

### Reject Immediately If

- Hash mismatch
- Missing fields
- Invalid status transition

### Common Mistake

Checking only:

```text
status == success
```

This is unsafe.

***

## 6. Handle Pending Payments Properly

Not every payment becomes success/failure immediately.

Common pending cases:

- UPI collect
- NetBanking timeout
- Bank latency
- PSP downtime

### Best Practice

Support 3 states:

- Pending
- Success
- Failed

Treat pending as a valid intermediate state.

### Common Mistake

Auto-failing pending payments after 30 seconds.

This creates false failures.

***

## 7. Build a Reconciliation Job

Even perfect integrations can miss callbacks.

Reasons:

- server outage
- DNS failure
- webhook timeout
- network partition

### Best Practice

Run periodic reconciliation:

- every 15 minutes
- hourly
- end-of-day

Compare:

- Merchant order records
- PayU payment records

Reconcile:

- missing success
- stuck pending
- duplicate records

This significantly reduces support tickets.

***

## 8. Use Webhooks for Reliable Payment State Updates

Webhooks are more reliable than browser redirects.

Why?
They are server-to-server notifications.

Use webhooks for:

- payment success
- payment failure
- refunds
- disputes
- settlements

### Best Practice

Webhook handler should:

- verify authenticity
- return HTTP 200 quickly
- process asynchronously

### Common Mistake

Doing heavy DB processing before responding.

This may trigger retries.

***

## 9. Make Callback Endpoints Public and Highly Available

PayU must reach your callback endpoint.

Requirements:

- Publicly accessible
- HTTPS enabled
- Low latency
- Highly available

Avoid:

- localhost
- private IPs
- VPN-only endpoints

### Best Practice

Deploy callback service separately if needed.

Target:

- > 99.9% uptime
- \<3s response time

***

## 10. Respond to Callbacks Quickly

Callback handlers should be fast.

Recommended:

- Validate request
- Queue processing
- Return 200

Avoid:

- heavy business logic
- slow third-party calls
- synchronous fulfillment

### Ideal Flow

```text
Receive callback
→ Validate
→ Queue event
→ Return 200
→ Process async
```

***

## 11. Log Everything Needed for Debugging (But No Secrets)

Good logs reduce support turnaround drastically.

Log:

- txnid
- order ID
- amount
- status
- callback timestamp
- hash validation result

Never log:

- salt
- full secrets
- auth credentials

### Best Practice

Mask sensitive values.

Example:

```text
merchant_salt = ******c92
```

***

## 12. Format Amount Consistently

Amount formatting is a common source of hash failures.

These are different strings:

- `100`
- `100.0`
- `100.00`

Hash output changes if formatting changes.

### Best Practice

Use canonical formatting.

Recommended:

- INR → always 2 decimals

Example:

```text
100.00
```

***

## 13. Protect Against Double Clicks and Refreshes

Users may click Pay multiple times.

This can create:

- duplicate requests
- multiple txnids
- accidental multiple payments

### Best Practice (Frontend)

- Disable Pay button after click
- Show loading state
- Prevent double submission

### Best Practice (Backend)

Reject duplicate active attempts for same cart/order.

***

## 14. Test Failure Scenarios, Not Just Success

Many teams only test successful payments.

Production failures happen in edge cases.

Must test:

- success
- failure
- timeout
- pending
- callback retry
- duplicate callback
- user closes browser

### Common Mistake

Go-live after one successful sandbox payment.

Not enough.

***

## 15. Maintain Separate Test and Production Configurations

Keep environments isolated.

Separate:

- keys
- salts
- callback URLs
- logging
- endpoints

### Best Practice

Use environment configuration:

- Sandbox
- Staging
- Production

### Common Mistake

Production using sandbox salt.

This causes hash mismatch.

***

## 16. Monitor Core Payment Metrics

Track payment health continuously.

Recommended metrics:

- Checkout open rate
- Payment success rate
- Drop-off rate
- Callback success rate
- Hash failure rate
- Pending aging
- Retry rate

Alert when:

- success rate drops
- callback latency spikes
- hash errors increase

***

## 17. Verify Payment Before Fulfillment

Before:

- shipping product
- activating subscription
- granting access

Verify payment.

Recommended checks:

- Status = success
- Reverse hash valid
- Order not already fulfilled
- Amount matches order

### Common Mistake

Delivering product before verification.

Risk:
Fraud + revenue loss.

***

## 18. Build for Failure Recovery

Payments fail in real-world systems.

Design recovery for:

- server crashes
- DB downtime
- callback failures
- partial order creation

### Best Practice

Use retry-safe architecture:

- event queues
- retries
- dead-letter handling
- reconciliation

Production-safe payment systems assume failures will happen.

***

## Go-Live Checklist

Before going live, confirm:

### Security

- Hash generation server-side
- Salt secured
- Reverse hash implemented

### Reliability

- Webhooks enabled
- Reconciliation job active
- Duplicate handling implemented

### UX

- Retry flow tested
- Failure messaging added
- Pending state supported

### Observability

- Logs enabled
- Alerts configured
- Metrics dashboard ready

<br />
