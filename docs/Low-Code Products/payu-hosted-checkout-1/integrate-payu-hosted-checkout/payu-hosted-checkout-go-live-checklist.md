---
title: Go-Live Checklist
excerpt: >-
  Production readiness checklist for PayU Hosted Checkout. Switch credentials,
  update endpoints, verify security requirements, and configure webhooks before
  going live.
deprecated: false
hidden: true
link:
  new_tab: false
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

Before you start this checklist, make sure you have completed the previous two stages of the integration:

<Cards columns="2">
  <Card title="Build Integration" href="./build-integration" icon="fa-code">
    Implement request parameters, hash generation, HTML form POST, response handling, and server-side verification.
  </Card>

  <Card title="Test Integration" href="./test-integration" icon="fa-flask">
    Run all payment scenarios — success, failure, and abandonment — using test credentials in the sandbox.
  </Card>
</Cards>

***

## 1. Switch to Production Credentials

<Accordion title="Replace Test Credentials With Live Credentials" icon="fa-user-lock">
  - [x] **Generate your live merchant key and salt** from **PayU Dashboard** → **Developer** → **API Keys&#x20;**&#x69;n the live mode.
  - [x] Replace `key` in all payment requests with your **live key**.
  - [x] Update your server-side hash generation to use your **live salt**.
  - [x] Confirm that your live key and salt are stored in environment variables or a secrets manager, not in source code.

  <Callout icon="far fa-octagon-exclamation" theme="error">
    ### **Important:**

    Never commit keys or salts to version control. Treat them as passwords.
  </Callout>
</Accordion>

***

## 2. Switch to the Production Endpoint

<Accordion title="Update the Payment Form Action URL" icon="fa-link">
  - [x] Update your HTML form `action` to `https://secure.payu.in/_payment`.
  - [x] Confirm the form still uses `method="post"`.
  - [x] Remove any references to `https://test.payu.in/_payment` from production code.

  | Environment    | URL                               |
  | -------------- | --------------------------------- |
  | Test           | `https://test.payu.in/_payment`   |
  | **Production** | `https://secure.payu.in/_payment` |
</Accordion>

***

## 3. Security Checklist

<Accordion title="Verify All Security Requirements" icon="fa-shield-check">
  - [x] Hash is generated **server-side only** and never in browser JavaScript, mobile app code, or any client-facing code.
  - [x] Your merchant **salt is never exposed** in logs, API responses, client-side code, or source control.
  - [x] All callback endpoints (`surl`, `furl`, webhook URL) are served over **HTTPS**.
  - [x] Reverse hash validation is implemented and runs on every callback received.
  - [x] Sensitive parameters (key, salt, and hash values) are **not logged** in application logs.
  - [x] Your payment request hash matches the documented SHA-512 formula exactly.
</Accordion>

***

## 4. Configure Webhooks

<Accordion title="Set Up Server-To-Server Payment Notifications" icon="fa-plug">
  Webhooks are strongly recommended for production. They provide reliable payment confirmation that does not depend on the customer's browser session staying active.

  - [x] Configure your webhook endpoint in **PayU Dashboard** → **Developer** → **Webhooks**.
  - [x] Webhook endpoint is a publicly reachable HTTPS URL.
  - [x] Webhook handler verifies the response hash before processing.
  - [x] Webhook handler returns HTTP 200 after successfully processing the notification.
  - [x] Webhook handler handles duplicate notifications idempotently (same `txnid` arriving twice does not create two successful orders).

  See <Anchor target="_blank" href="https://docs.payu.in/docs/manage-webhooks-using-dashboard">Manage Webhooks</Anchor> for setup details.
</Accordion>

***

## 5. Production Readiness Verification

<Accordion title="Functional Verification" icon="fa-clipboard-check">
  - [x] Successful payment flow tested end-to-end in test environment.
  - [x] Failed payment flow tested — `furl` triggers, order remains unpaid.
  - [x] Pending payment flow handled — `surl` triggers with `status=pending`, order not marked as paid until confirmed.
  - [x] Customer browser-close / abandonment scenario handled gracefully.
  - [x] Reverse hash validation implemented and tested.
  - [x] Duplicate callback/webhook protection implemented.
  - [x] Callback retry handling: if `surl`/`furl` or webhook fails, PayU retries — ensure your handler is idempotent.
  - [x] Alerting or monitoring in place for failed hash validations and webhook delivery failures.
</Accordion>

<Accordion title="Order Management Verification" icon="fa-list-check">
  - [x] Unique `txnid` generated for every payment attempt (including retries).
  - [x] `txnid` stored in your database before redirecting the customer.
  - [x] Order status transitions are consistent: Unpaid → Pending → Paid (or Failed).
  - [x] Amount validation: response `amount` is verified against the order amount in your system.
  - [x] `txnid` validation: response `txnid` is verified against a known order in your system.
</Accordion>

***

## 6. Final Sign-off

Once all items above are checked, you are ready to go live.

<Callout icon="✅" theme="success">
  ### **After Going Live:**

  Monitor your first few live transactions closely. Check **PayU Dashboard** → **Transactions** to confirm payments appear with `status=success` and your webhook/callback handler is receiving and processing responses correctly.
</Callout>

If you run into issues during or after go-live, see [Errors and Troubleshooting](../errors-and-troubleshooting) or contact [PayU Support](https://support.payu.in/).