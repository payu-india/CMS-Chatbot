---
title: Errors and Troubleshooting
excerpt: >-
  Common PayU Hosted Checkout integration errors and how to fix them: invalid
  hash, page not loading, callback failures, reverse hash mismatch, and more.
deprecated: false
hidden: true
metadata:
  title: PayU Hosted Checkout Errors and Troubleshooting
  description: >-
    Diagnose and fix PayU Hosted Checkout integration issues: invalid hash,
    payment page not loading, callback not triggered, reverse hash mismatch,
    duplicate processing, and amount mismatch.
  keywords:
    - payu hosted checkout errors troubleshooting
    - payu invalid hash error fix
    - payu payment page not loading fix
    - payu surl furl callback not triggered
    - payu reverse hash mismatch fix
    - payu duplicate order processing prevention
    - payu checkout integration debug india
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
---
<Banner
  isInline={true}
  message="Integration effort: Minimal technical setup required"
  color="#FFC107"
  textColor="#ffffff"
  fontSize="14px"
  fontWeight="bold"
 />

Diagnose and fix common issues with your PayU Hosted Checkout integration. Find common integration errors, understand their causes, and follow the recommended solutions to resolve them.

***

<Accordion title="Invalid Hash" icon="fa-key">
  PayU returns a hash validation error; the payment page displays "Invalid Hash" or rejects the request outright.

  **Common Error Causes:**

  - Wrong parameter order in the hash string
  - Missing pipe (`|`) separators, especially for unused UDF fields
  - Incorrect salt (test salt used in production, or vice versa)
  - Extra spaces before or after any parameter value
  - Using SHA-256 or MD5 instead of SHA-512

  **Recommended Fix:**

  - Correct the parameter order and pipe separators.
  - Remove all leading/trailing spaces from parameter values.
  - Confirm you are using the correct environment salt (test vs production).
  - Generate the hash using SHA-512 and not SHA-256.
  - Never generate the hash client-side.
</Accordion>

<Accordion title="Payment Page Not Loading" icon="fa-display">
  The browser redirects but the PayU checkout page does not appear, shows a blank screen, or returns an error page.

  **Common Error Causes:**

  - Form uses `method="get"` instead of `method="post"`
  - Wrong endpoint URL (for example, using the production URL in test, or vice versa)
  - Missing mandatory parameters in the POST body
  - Browser or network firewall blocking the request
  - SSL/TLS error on the merchant's page preventing the form submission

  **Recommended Fix:**

  - Set `method="post"` on the form.
  - Use the correct endpoint for your environment: test → `https://test.payu.in/_payment`, production → `https://secure.payu.in/_payment`.
  - Ensure all these mandatory parameters are populated.
    - `key`&#x20;
    - `txnid`
    - `amount`
    - `productinfo`
    - `firstname`
    - `email`
    - `phone`
    - `surl`
    - `furl`
    - `hash`
  - Remove any `onsubmit` handlers that might be preventing form submission.
</Accordion>

<Accordion title="Callback Not Triggered (surl / furl)" icon="fa-link-slash">
  Payment completes but the browser does not redirect back, or your server does not receive a POST to `surl` / `furl`.

  **Common Error Causes:**

  - `surl` / `furl` is a localhost URL not reachable by PayU's servers
  - `surl` / `furl` uses HTTP instead of HTTPS
  - Firewall or VPN blocking incoming requests from PayU IPs
  - Callback endpoint returns a non-200 status code
  - Callback URL has path encoding issues or query string characters not URL-encoded

  **Recommended Fix:**

  - Use a publicly reachable HTTPS endpoint. During testing, use `https://test-payment-middleware.payu.in/simulatorResponse` as a temporary callback URL.
  - Do not use localhost, 127.0.0.1, or private/VPN-only addresses for `surl` / `furl`.
  - Ensure your endpoint returns HTTP 200 after processing the callback.

  <Callout icon="📘" theme="info">
    ### **Webhook as a Backup**

    Browser redirects to `surl` / `furl` can be disrupted if the customer closes their browser before the redirect completes. Configure webhooks as a reliable server-to-server fallback. See <Anchor target="_blank" href="https://docs.payu.in/docs/webhook-events-and-sample-payloads">Manage Webhooks</Anchor>.
  </Callout>
</Accordion>

<Accordion title="Reverse Hash Mismatch" icon="fa-shield-halved">
  Your server computes a reverse hash but it does not match the `hash` field in PayU's response. You reject the callback.

  **Common Error Causes:**

  - Using the forward hash formula instead of the reverse hash formula
  - Wrong parameter order in the reverse hash string
  - Missing or out-of-order UDF fields (reverse hash uses UDFs in reverse order: udf5 → udf1)
  - Wrong salt
  - Extra whitespace in response values

  **Recommended Fix:**

  - Use the correct reverse hash formula.
  - Include all response fields in the below sequence:&#x20;
    ```text Reverese Hash String
    SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key
    ```
  - Ensure empty UDF placeholders are preserved (six consecutive pipes: `||||||`).
  - Use the exact value of `status` from the response (e.g. `success`, `failure`, `pending`).
  - Use the [PayU Hash Verification Tool](https://payu-hashverificationtool.onrender.com/) to validate.
</Accordion>

<Accordion title="Duplicate Order Processing" icon="fa-clone">
  A single payment is processed twice. Customer sees a double charge, or your order management marks the same transaction as paid more than once.

  **Common Error Causes:**

  - Callback arrives multiple times (PayU retries if your endpoint doesn't return 200)
  - Webhook and callback both processed without deduplication
  - Customer navigates back and re-submits the payment form
  - No idempotency check on `txnid`

  **Recommended Fix:**

  - Implement idempotency: check if the `txnid` has already been processed before updating order status.
  - Use a database unique constraint on `txnid` (or a state machine that ignores updates if the order is already in a terminal state).
  - Return HTTP 200 from your callback endpoint after successfully processing the notification to prevent retry loops.
</Accordion>

<Accordion title="Amount Mismatch" icon="fa-receipt">
  <Callout icon="⚠️" theme="warn">
    **Symptoms:** The `amount` in PayU's response does not match the amount in your original order.
  </Callout>

  **Common causes:**

  - Discount or promotion applied at the PayU level (rare)
  - Amount rounded or formatted differently in your system vs what you sent to PayU
  - Incorrect amount used when computing the hash (hash was generated with a different amount than the form field)

  **How to check:**

  1. Compare the response `amount` with the value stored in your database for this `txnid`.
  2. Confirm the amount in the hash string exactly matches the `amount` form field — both should be the same string (e.g. `499.00`).

  **Fix:**

  - Reject callbacks where `amount` does not match your stored order amount.
  - Always use the exact decimal string representation when building the hash and in the form field (e.g. `499.00`, not `499` or `₹499`).
</Accordion>

***

## Still Having Issues?

If the issue persists, reach out to [PayU Support](https://support.payu.in/) with your `txnid` and the hash string you generated. This helps the support team locate the transaction and identify the exact failure point.

<br />
