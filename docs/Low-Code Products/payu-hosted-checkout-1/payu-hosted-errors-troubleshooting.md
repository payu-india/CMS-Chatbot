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

Use this guide to diagnose and fix common issues with your PayU Hosted Checkout integration.

***

## Invalid Hash

**Symptoms:** PayU returns a hash validation error; the payment page displays "Invalid Hash" or rejects the request outright.

**Common causes:**

- Wrong parameter order in the hash string
- Missing pipe (`|`) separators — especially for unused UDF fields
- Incorrect salt (test salt used in production, or vice versa)
- Extra spaces before or after any parameter value
- Using SHA-256 or MD5 instead of SHA-512

**How to check:**

1. Print the exact string you pass to the hash function on your server before hashing.
2. Verify the order exactly matches: `key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT`
3. If UDF fields are empty, they must still appear as empty strings: `...email|||||||||||SALT` (five empty UDF positions + 6 empty trailing pipes before SALT).
4. Verify the salt value from your PayU Dashboard → Developer Settings matches what you're using.
5. Use the [PayU Hash Verification Tool](https://payu-hashverificationtool.onrender.com/) to validate your hash string independently.

**Fix:**

- Correct the parameter order and pipe separators.
- Remove all leading/trailing spaces from parameter values.
- Confirm you are using the correct environment salt (test vs production).
- Generate the hash using SHA-512, not SHA-256.
- Never generate the hash client-side.

***

## Payment Page Not Loading

**Symptoms:** The browser redirects but the PayU checkout page does not appear, shows a blank screen, or returns an error page.

**Common causes:**

- Form uses `method="get"` instead of `method="post"`
- Wrong endpoint URL (for example, using the production URL in test, or vice versa)
- Missing mandatory parameters in the POST body
- Browser or network firewall blocking the request
- SSL/TLS error on the merchant's page preventing the form submission

**How to check:**

1. Inspect the form element: confirm `method="post"` and `action="https://test.payu.in/_payment"` (or the production URL).
2. Open browser developer tools → Network tab. Check that a POST request was made to the PayU endpoint and inspect the request payload.
3. Confirm all 10 mandatory parameters are present and non-empty: `key`, `txnid`, `amount`, `productinfo`, `firstname`, `email`, `phone`, `surl`, `furl`, `hash`.
4. Check the browser console for JavaScript errors that may have prevented the form submission.

**Fix:**

- Set `method="post"` on the form.
- Use the correct endpoint for your environment: test → `https://test.payu.in/_payment`, production → `https://secure.payu.in/_payment`.
- Ensure all mandatory parameters are populated.
- Remove any `onsubmit` handlers that might be preventing form submission.

***

## Callback Not Triggered (surl / furl)

**Symptoms:** Payment completes but the browser does not redirect back, or your server does not receive a POST to `surl` / `furl`.

**Common causes:**

- `surl` / `furl` is a localhost URL not reachable by PayU's servers
- `surl` / `furl` uses HTTP instead of HTTPS
- Firewall or VPN blocking incoming requests from PayU IPs
- Callback endpoint returns a non-200 status code
- Callback URL has path encoding issues or query string characters not URL-encoded

**How to check:**

1. Confirm your callback URL is publicly reachable from the internet over HTTPS. Test it with a tool like [webhook.site](https://webhook.site) or [requestbin](https://pipedream.com/requestbin).
2. Confirm the URL uses `https://` not `http://`.
3. Check your server logs: is PayU's POST arriving but returning an error?

**Fix:**

- Use a publicly reachable HTTPS endpoint. During testing, use `https://test-payment-middleware.payu.in/simulatorResponse` as a temporary callback URL.
- Do not use localhost, 127.0.0.1, or private/VPN-only addresses for `surl` / `furl`.
- Ensure your endpoint returns HTTP 200 after processing the callback.
- If using tools like ngrok for local testing, ensure the tunnel is active.

<Callout icon="📘" theme="info">
  **Webhook as backup** — Browser redirects to `surl` / `furl` can be disrupted if the customer closes their browser before the redirect completes. Configure webhooks as a reliable server-to-server fallback. See [Manage Webhooks](https://docs.payu.in/docs/webhook-events-and-sample-payloads).
</Callout>

***

## Reverse Hash Mismatch

**Symptoms:** Your server computes a reverse hash but it does not match the `hash` field in PayU's response. You reject the callback.

**Common causes:**

- Using the forward hash formula instead of the reverse hash formula
- Wrong parameter order in the reverse hash string
- Missing or out-of-order UDF fields (reverse hash uses UDFs in reverse order: udf5 → udf1)
- Wrong salt
- Extra whitespace in response values

**How to check:**

1. Confirm you are using the reverse hash formula, not the forward hash: `sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)`
2. Note the UDF order: reverse hash uses **udf5 to udf1** (opposite of the forward hash).
3. Print the exact string before hashing and compare field by field against the response values.
4. Verify the salt value is your merchant salt, not the key.
5. Use the [PayU Hash Verification Tool](https://payu-hashverificationtool.onrender.com/) to validate.

**Fix:**

- Use the correct reverse hash formula.
- Include all response fields in the exact sequence: `SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key`
- Ensure empty UDF placeholders are preserved (six consecutive pipes: `||||||`).
- Use the exact value of `status` from the response (e.g. `success`, `failure`, `pending`).

***

## Duplicate Order Processing

**Symptoms:** A single payment is processed twice — customer sees a double charge, or your order management marks the same transaction as paid more than once.

**Common causes:**

- Callback arrives multiple times (PayU retries if your endpoint doesn't return 200)
- Webhook and callback both processed without deduplication
- Customer navigates back and re-submits the payment form
- No idempotency check on `txnid`

**How to check:**

1. Confirm your callback handler returns HTTP 200 promptly — PayU retries callbacks that don't receive 200.
2. Check if the same `txnid` is appearing in your database multiple times.
3. Check whether both your callback handler and webhook handler are processing the same transaction independently.

**Fix:**

- Implement idempotency: check if the `txnid` has already been processed before updating order status.
- Use a database unique constraint on `txnid` (or a state machine that ignores updates if the order is already in a terminal state).
- Return HTTP 200 from your callback endpoint after successfully processing the notification to prevent retry loops.

***

## Amount Mismatch

**Symptoms:** The `amount` in PayU's response does not match the amount in your original order.

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

***

## Still Having Issues?

If the issue is not covered above:

- Check [FAQs](./faqs) for common questions.
- Review the [Build Integration](./integrate/build-integration) guide for the correct parameter sequence and hash formulas.
- Use the [Verify Payment API](ref:verify_payment_api) to check transaction status directly from your server — useful when callbacks or webhooks are not arriving and you need to determine whether a payment was captured.
- See [PayU Hosted Checkout APIs](./payu-hosted-checkout-apis) for the full API reference.
- Contact [PayU Support](https://support.payu.in/) with your `txnid` and the hash string you generated.