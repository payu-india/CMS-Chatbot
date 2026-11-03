---
title: Best Practices
excerpt: >-
  Conversion, reliability, and error-recovery best practices for PayU Hosted
  Checkout. Pre-fill customer data, handle pending payments, build resilient
  callbacks, and design clear failure flows.
deprecated: false
hidden: true
metadata:
  title: PayU Hosted Checkout Best Practices
  description: >-
    Best practices for PayU Hosted Checkout: pre-fill customer data, vernacular
    checkout for conversion, txnid generation, NEFT/RTGS pending handling,
    resilient callbacks, webhook idempotency, and payment retry design.
  keywords:
    - payu hosted checkout best practices
    - payu checkout conversion optimisation
    - payu txnid unique generation
    - payu neft rtgs pending payment handling
    - payu webhook idempotency
    - payu payment retry flow india
    - payu checkout error recovery ux
    - payu display_lang regional conversion
  robots: index
next:
  description: Explore related information and resources.
  pages:
    - slug: payu-hosted-checkout-1
      title: PayU Hosted Checkout
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
    - slug: payu-hosted-errors-troubleshooting
      title: Errors and Troubleshooting
      type: basic
---
These practices cover the areas where integrations most often have subtle gaps: conversion friction, pending payment handling, callback resilience, and failure UX.&#x20;

To apply these practices, your integration should already be built and tested:

<Cards columns="2">
  <Card title="Build Integration" href="https://docs.payu.in/docs/payu-hosted-checkout-build-integration" icon="fa-code" target="_blank">
    Request parameters, hash generation, form POST, response handling, and server-side verification.
  </Card>

  <Card title="Test Integration" href="https://docs.payu.in/docs/payu-hosted-checkout-test-integration" icon="fa-flask" target="_blank">
    Test credentials and scenarios for all payment methods.
  </Card>
</Cards>

***

## Conversion and UX

{/* NEW CONTENT: Pre-fill and vernacular checkout are UX best practices not stated as recommendations on any existing page, only implied by parameter descriptions. */}

<Accordion title="Pre-fill Customer Data to Reduce Checkout Friction" icon="fa-user-pen">
  The PayU checkout page pre-populates fields you send in the request. Customers who arrive with their name, email, and phone already filled in complete checkout faster and abandon less.

  Send these parameters from your logged-in session whenever available:

  | Parameter                              | Source                 | Effect                               |
  | -------------------------------------- | ---------------------- | ------------------------------------ |
  | `firstname`                            | Customer account name  | Pre-fills the name field on checkout |
  | `email`                                | Customer account email | Pre-fills the email field            |
  | `phone`                                | Customer account phone | Pre-fills the phone field            |
  | `address1`, `city`, `state`, `zipcode` | Saved address          | Aids fraud detection and chargebacks |

  You still need to include these fields in your hash string exactly as described in <Anchor target="_blank" href="https://docs.payu.in/docs/payu-hosted-checkout-build-integration#step-1-prepare-payment-request-parameters">Step 1 of Build Integration</Anchor>. Pre-filling is about passing real values instead of placeholder values without changing the hash formula.

  <Callout icon="📘" theme="info">
    ### **Tips:**

    `address1`, `city`, `state`, `zipcode`, and `country` are optional but strengthen fraud detection for card payments. Include them when available.
  </Callout>
</Accordion>

<Accordion title="Use Vernacular Checkout for Regional Audiences" icon="fa-language">
  Pass `display_lang` in the payment request to show the PayU checkout page in the customer's preferred language. This is particularly effective for regional audiences where customers are more comfortable completing payment in their native language.

  **Supported values:**

  | Language          | Value      |
  | ----------------- | ---------- |
  | English (default) | `English`  |
  | Hindi             | `Hindi`    |
  | Kannada           | `Kannada`  |
  | Telugu            | `Telugu`   |
  | Tamil             | `Tamil`    |
  | Gujarati          | `Gujarati` |
  | Marathi           | `Marathi`  |

  Set `display_lang` based on the customer's app/site language preference, not their browser locale.

  See <Anchor target="_blank" href="https://docs.payu.in/docs/customise-payu-hosted-checkout">Customise PayU Hosted Checkout</Anchor> for the full `display_lang` reference and a visual preview.
</Accordion>

<Accordion title="Prevent Duplicate Form Submissions With a Loading State" icon="fa-spinner">
  The HTML payment form auto-submits on page load using `onload="document.forms.payu.submit()"`. On slow connections, customers sometimes tap or click the submit button multiple times before the redirect happens, which can trigger multiple form submissions.

  Add a brief visual loading state after the form submits to prevent this:

  ```html
  <!doctype html>
  <html>
    <head>
      <style>
        #loading { display: none; text-align: center; padding: 40px; font-family: sans-serif; }
      </style>
    </head>
    <body onload="submitForm()">
      <form id="payu-form" name="payu" method="post" action="https://secure.payu.in/_payment">
        <input type="hidden" name="key"         value="YOUR_KEY">
        <input type="hidden" name="txnid"       value="YOUR_TXNID">
        <input type="hidden" name="amount"      value="499.00">
        <input type="hidden" name="productinfo" value="Pro Plan">
        <input type="hidden" name="firstname"   value="Aditi">
        <input type="hidden" name="email"       value="aditi@example.com">
        <input type="hidden" name="phone"       value="9999999999">
        <input type="hidden" name="surl"        value="https://yourapp.com/payu/success">
        <input type="hidden" name="furl"        value="https://yourapp.com/payu/failure">
        <input type="hidden" name="hash"        value="YOUR_HASH">
      </form>
      <div id="loading">Redirecting to payment page…</div>
      <script>
        function submitForm() {
          document.getElementById('loading').style.display = 'block';
          document.forms.payu.submit();
        }
      </script>
    </body>
  </html>
  ```

  The loading message reassures customers that something is happening during the redirect, and the form cannot be submitted twice because the page navigates away immediately after `submit()`.
</Accordion>

***

## Transaction ID Strategy

{/* NEW CONTENT: txnid generation strategy and retry flow are not explained on any existing page beyond the brief "generate unique txnid" callout in build-integration.md. */}

<Accordion title="Generate Collision-proof Transaction IDs" icon="fa-fingerprint">
  PayU requires a unique `txnid` for every payment attempt. If you submit a `txnid` that has already been used, PayU will reject the request or return the earlier transaction's status.

  **Recommended Approach:**

  Generate a `txnid` by combining a prefix, the order or session identifier from your database, and a short random or timestamp component. This makes each ID unique, traceable back to a specific order, and human-readable in the PayU Dashboard.

  ```
  Format:  {prefix}-{order_id}-{random_suffix}
  Example: ORD-78245-a3f9
  ```

  Constraints to respect:

  - Maximum 25 characters
  - Alphanumeric and hyphens. No spaces or special characters
  - Store the `txnid` in your database before redirecting the customer, so you can reconcile it against the callback response

  <Callout icon="⚠️" theme="warn">
    ### **Warning!**

    Do not use a customer's email address, phone number, or any personally identifiable information as the `txnid`. Use an internal order ID or a generated UUID.
  </Callout>
</Accordion>

<Accordion title="Design a Safe Payment Retry Flow" icon="fa-rotate-right">
  When a payment fails and the customer wants to try again with a different card or payment method, your system must generate a ne&#x77;**&#x20;**`txnid` for each attempt. Do not reuse the failed transaction's ID.

  **Safe Retry Pattern:**

  1. Customer arrives at the payment failure page after a `status=failure` response.
  2. Customer clicks **Try Again**.
  3. Your server creates a new payment attempt record in your database with a new unique `txnid` (linked to the same order).
  4. Your server generates a new hash using the new `txnid`.
  5. Your server renders a new HTML form with the new `txnid` and new hash and redirects the customer.

  Mark the order as paid only when one of its `PaymentAttempt` records receives `status=success` with a valid reverse hash.
</Accordion>

***

## Handling Pending Payments

{/* NEW CONTENT: Guidance on NEFT/RTGS pending UX and when to confirm orders is absent from all existing pages — only the status/unmappedstatus values are documented. */}

<Accordion title="Treat NEFT/RTGS Pending Status Correctly" icon="fa-clock">
  NEFT and RTGS payments always return `status=pending` in the initial callback to your `surl`. This is expected as the bank might have not yet settled the funds.

  **What to Do When You Receive&#x20;**`status=pending` :

  - Do not mark the order as paid as the payment has not been confirmed yet.
  - Do not mark the order as failed as the payment is still in progress and may complete successfully

  * Show the customer a **Payment Pending** confirmation page that explains the timeline (NEFT: same day to next business day; RTGS: typically same day).
  * Store the `txnid` and `mihpayid` in your database against the order with a `pending` status.
  * Wait for the final status via webhook. When the webhook arrives with `status=success`, mark the order as paid and trigger fulfilment. If the webhook arrives with `status=failure`, mark the order as failed.
</Accordion>

***

## Callback Resilience

{/* NEW CONTENT: Proactive callback verification approach is not described on any existing page. The Verify Payment API is mentioned in build-integration.md Step 1.5 but without guidance on when/how to use it as a fallback. */}

<Accordion title="Proactively verify status when the callback doesn't arrive" icon="fa-satellite-dish">
  Browser-based callbacks to `surl` and `furl` depend on the customer's browser session staying active through the redirect. Callbacks can fail to arrive if the customer closes the browser tab, loses network connectivity, or navigates away during the redirect.

  **If a callback does not arrive within a reasonable window (e.g. 5–10 minutes after the customer was redirected to PayU):**

  1. Query the [Verify Payment API](ref:verify_payment_api) from your server using the `txnid`.
  2. Use the API response to determine the final payment status.
  3. Update your order status based on the verified result.

  This is particularly important for orders where the customer's session may have dropped — for example, mobile browsers on unstable connections.

  <Callout icon="📘" theme="info">
    Webhooks are a more reliable alternative to browser callbacks because they are server-to-server and not dependent on the customer's browser. Configure webhooks in PayU Dashboard → Developer Settings → Webhooks. See the [Go-live Checklist](./integrate/go-live-checklist) for setup steps.
  </Callout>
</Accordion>

<Accordion title="Process webhook notifications idempotently" icon="fa-shield-halved">
  PayU may deliver a callback or webhook notification for the same transaction more than once (network retries, timeout re-delivery). Your handler must be idempotent — processing the same `txnid` twice must not create two successful orders or trigger fulfilment twice.

  **Implementation pattern:**

  ```
  1. Receive callback/webhook POST
  2. Verify reverse hash — reject immediately if mismatch
  3. Look up txnid in your database
     a. If txnid not found → reject (unknown transaction)
     b. If order already marked as paid → return 200, do nothing
     c. If order is pending → proceed with verification
  4. Verify amount matches stored order amount
  5. Update order status
  6. Return HTTP 200
  ```

  Returning HTTP 200 even for duplicates prevents PayU from retrying delivery. Returning an error code causes PayU to retry, which can result in repeated duplicate notifications.
</Accordion>

***

## Error Recovery UX

{/* NEW CONTENT: Error recovery UX guidance by unmappedstatus value is not on any existing page. unmappedstatus values are only documented in the Payment Outcomes table in build-integration.md without UX guidance. */}

<Accordion title="Show the right message for each failure type" icon="fa-triangle-exclamation">
  The `unmappedstatus` field in the callback response tells you exactly why a payment failed. Use it to show customers a specific, actionable message rather than a generic "payment failed" error.

  | `unmappedstatus` | What happened                                     | Recommended message                                                                      |
  | ---------------- | ------------------------------------------------- | ---------------------------------------------------------------------------------------- |
  | `failed`         | Bank or card issuer declined the payment          | "Your payment was declined by your bank. Please try a different card or payment method." |
  | `userCancelled`  | Customer clicked Back or cancelled the flow       | "Looks like you cancelled the payment. Ready to try again?"                              |
  | `pending`        | NEFT/RTGS transfer initiated, awaiting settlement | "Your payment is being processed. We'll confirm your order once the transfer completes." |

  <Callout icon="⚠️" theme="warn">
    **What not to do:**

    - Do not show a generic "Something went wrong" message for all failures — it gives the customer no path forward.
    - Do not tell the customer their card number is wrong unless you have confirmed this from the `error_Message` field — an incorrect message can erode trust.
    - Do not mark the order as abandoned on `userCancelled` without giving the customer an easy retry path — this is the highest-recovery failure type.
  </Callout>
</Accordion>

<Accordion title="Surface the error_Message for actionable failures" icon="fa-message">
  The `error_Message` field in the PayU response contains a human-readable description of what went wrong. For bank declines and card errors, this often provides enough context for the customer to take action.

  **Pattern for using error_Message:**

  - Log the raw `error_Message` for your support team (useful for diagnosing integration issues).
  - For `unmappedstatus=failed`, you can surface a sanitised version of `error_Message` to the customer if it is actionable (e.g. "Transaction Failed at bank end" → prompt customer to retry or use a different method).
  - Do not expose raw technical error codes (like `E308`) directly to customers — translate them into plain language.

  Common response patterns:

  | `error` | `error_Message`                   | What it means                                                     |
  | ------- | --------------------------------- | ----------------------------------------------------------------- |
  | `E000`  | `No Error`                        | Successful transaction                                            |
  | `E227`  | `Transaction is Pending`          | NEFT/RTGS awaiting settlement                                     |
  | `E308`  | `Transaction Failed at bank end.` | Bank-side decline — customer should retry with a different method |

  For a complete list of error codes, see [Errors and Troubleshooting](./errors-and-troubleshooting).
</Accordion>

***

## Next Steps

<Cards columns="3">
  <Card title="Customise Checkout" href="./customise-payu-hosted-checkout" icon="fa-sliders">
    Control payment methods, set checkout language, and enable BNPL/EMI.
  </Card>

  <Card title="Errors and Troubleshooting" href="./errors-and-troubleshooting" icon="fa-circle-xmark">
    Full error code reference and solutions for common integration issues.
  </Card>

  <Card title="PayU Hosted Checkout APIs" href="./payu-hosted-checkout-apis" icon="fa-rectangle-api">
    Collect Payment, Verify Payment, and Webhooks API reference.
  </Card>
</Cards>