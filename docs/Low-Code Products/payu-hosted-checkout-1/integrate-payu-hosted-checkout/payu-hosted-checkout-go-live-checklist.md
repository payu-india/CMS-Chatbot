---
title: Go-live Checklist
excerpt: >-
  Production readiness checklist for PayU Hosted Checkout. Switch credentials,
  update endpoints, verify security requirements, and configure webhooks before
  going live.
deprecated: false
hidden: true
metadata:
  title: PayU Hosted Checkout Go-live Checklist
  description: >-
    Complete checklist to go live with PayU Hosted Checkout: production
    credentials, endpoint switch, security verification, webhook setup, and
    production readiness sign-off.
  keywords:
    - payu hosted checkout go live production
    - payu live key salt production credentials
    - payu secure.payu.in production endpoint
    - payu checkout production security checklist
    - payu webhook configuration production
    - payu payment integration production readiness india
    - payu hosted checkout launch checklist
  robots: index
next:
  description: Explore related information and resources.
---
<Banner
  isInline={true}
  message="Integration effort: Minimal technical setup required"
  color="#15C614"
  textColor="#ffffff"
  fontSize="14px"
  fontWeight="bold"
 />

Work through this checklist before switching your PayU Hosted Checkout integration to production. Each item must be verified and confirmed.

***

## 1. Switch to Production Credentials

<Accordion title="Replace test credentials with live credentials" icon="fa-user-lock">
  - [ ] **Generate your live merchant key and salt** from PayU Dashboard → Developer Settings → Live Keys. See [Generate Live Key and Salt](https://docs.payu.in/docs/generate-merchant-key-and-salt-on-payu-dashboard).
  - [ ] Replace `key` in all payment requests with your **live key**.
  - [ ] Update your server-side hash generation to use your **live salt** — not the test salt.
  - [ ] Confirm that your live key and salt are stored in environment variables or a secrets manager, not in source code.

  <Callout icon="⚠️" theme="warn">
    Never commit keys or salts to version control. Treat them as passwords.
  </Callout>
</Accordion>

***

## 2. Switch to the Production Endpoint

<Accordion title="Update the payment form action URL" icon="fa-link">
  - [ ] Update your HTML form `action` to `https://secure.payu.in/_payment`.
  - [ ] Confirm the form still uses `method="post"`.
  - [ ] Remove any references to `https://test.payu.in/_payment` from production code.

  | Environment    | URL                               |
  | -------------- | --------------------------------- |
  | Test           | `https://test.payu.in/_payment`   |
  | **Production** | `https://secure.payu.in/_payment` |
</Accordion>

***

## 3. Security Checklist

<Accordion title="Verify all security requirements" icon="fa-shield-check">
  - [ ] Hash is generated **server-side only** — never in browser JavaScript, mobile app code, or any client-facing code.
  - [ ] Your merchant **salt is never exposed** in logs, API responses, client-side code, or source control.
  - [ ] All callback endpoints (`surl`, `furl`, webhook URL) are served over **HTTPS**.
  - [ ] Reverse hash validation is implemented and runs on every callback received.
  - [ ] Sensitive parameters (key, salt, hash values) are **not logged** in application logs.
  - [ ] Your payment request hash matches the documented SHA-512 formula exactly.
</Accordion>

***

## 4. Configure Webhooks

<Accordion title="Set up server-to-server payment notifications" icon="fa-plug">
  Webhooks are strongly recommended for production. They provide reliable payment confirmation that doesn't depend on the customer's browser session staying active.

  - [ ] Configure your webhook endpoint in PayU Dashboard → Developer Settings → Webhooks.
  - [ ] Webhook endpoint is a publicly reachable HTTPS URL.
  - [ ] Webhook handler verifies the response hash before processing.
  - [ ] Webhook handler returns HTTP 200 after successfully processing the notification.
  - [ ] Webhook handler handles duplicate notifications idempotently (same `txnid` arriving twice does not create two successful orders).

  See [Manage Webhooks](https://docs.payu.in/docs/webhook-events-and-sample-payloads) for setup details.
</Accordion>

***

## 5. Production Readiness Verification

<Accordion title="Functional verification" icon="fa-clipboard-check">
  - [ ] Successful payment flow tested end-to-end in test environment.
  - [ ] Failed payment flow tested — `furl` triggers, order remains unpaid.
  - [ ] Pending payment flow handled — `surl` triggers with `status=pending`, order not marked as paid until confirmed.
  - [ ] Customer browser-close / abandonment scenario handled gracefully.
  - [ ] Reverse hash validation implemented and tested.
  - [ ] Duplicate callback/webhook protection implemented.
  - [ ] Callback retry handling: if `surl`/`furl` or webhook fails, PayU retries — ensure your handler is idempotent.
  - [ ] Alerting or monitoring in place for failed hash validations and webhook delivery failures.
</Accordion>

<Accordion title="Order management verification" icon="fa-list-check">
  - [ ] Unique `txnid` generated for every payment attempt (including retries).
  - [ ] `txnid` stored in your database before redirecting the customer.
  - [ ] Order status transitions are consistent: Unpaid → Pending → Paid (or Failed).
  - [ ] Amount validation: response `amount` is verified against the order amount in your system.
  - [ ] `txnid` validation: response `txnid` is verified against a known order in your system.
</Accordion>

***

## 6. Final Sign-off

Once all items above are checked, you are ready to go live.

<Callout icon="✅" theme="success">
  **After going live:** Monitor your first few live transactions closely. Check PayU Dashboard → Transactions to confirm payments appear with `status=success` and your webhook/callback handler is receiving and processing responses correctly.
</Callout>

If you run into issues during or after go-live, see [Errors and Troubleshooting](../errors-and-troubleshooting) or contact [PayU Support](https://support.payu.in/).
