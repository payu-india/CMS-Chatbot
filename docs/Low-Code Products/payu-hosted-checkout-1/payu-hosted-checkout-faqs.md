---
title: FAQs (Frequently Asked Questions)
excerpt: >-
  Frequently asked questions about PayU Hosted Checkout: setup, hash generation,
  checkout experience, callbacks, webhooks, and production go-live.
deprecated: false
hidden: true
metadata:
  title: PayU Hosted Checkout FAQs
  description: >-
    Frequently asked questions about PayU Hosted Checkout: prerequisites,
    surl/furl, hash generation, reverse hash, callbacks vs webhooks, duplicate
    processing, and production readiness.
  keywords:
    - payu hosted checkout faq
    - payu hosted checkout frequently asked questions
    - payu integration questions answers india
    - payu hash generation faq sha512
    - payu webhook vs callback difference
    - payu surl furl explained
    - payu pci compliance hosted checkout
    - payu upi test vpa anything@payu sandbox
    - payu mihpayid txnid difference
    - payu status unmappedstatus difference
    - payu webhook hash verification reverse hash
    - payu webhook url configuration dashboard
    - payu txnid reuse retry failed payment
    - payu emi testing sandbox
    - payu _payment endpoint postman curl test
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
    - slug: payu-hosted-checkout-best-practices
      title: Best Practices
      type: basic
---
## Getting Started

1. #### What is PayU Hosted Checkout?

<Accordion title="Answer" icon="fab fa-adn">
  <Anchor target="_blank" href="https://docs.payu.in/docs/payu-hosted-checkout-1">PayU Hosted Checkout</Anchor> is a payment integration method where:

  - You redirect customers from your website to a PayU-hosted payment page
  - PayU handles the entire payment experience, including security and processing
  - After the payment is completed, customers are redirected back to your website

  This is the simplest and fastest way to start accepting payments without building or managing your own payment UI.
</Accordion>

2. #### What are the minimum prerequisites to integrate PayU Hosted Checkout?

<Accordion title="Answer" icon="fab fa-adn">
  These are required to integrate PayU Hosted Checkout:

  - [PayU merchant account](https://docs.payu.in/docs/register-for-a-merchant-account-on-dashboard)
  - [Merchant test Key and Salt](https://docs.payu.in/docs/generate-test-merchant-key-and-salt) for testing your integration
  - [Merchant live Key and Salt](https://docs.payu.in/docs/generate-merchant-key-and-salt-on-payu-dashboard) to go live
  - A backend server capable of generating a SHA-512 hash
  - An HTTPS-enabled, publicly reachable callback endpoint

  Minimum backend responsibilities:

  - Generate request hash
  - Validate reverse hash
  - Process callbacks and webhooks
  - Prevent duplicate order processing
</Accordion>

3. #### What payment methods are supported?

<Accordion title="Answer" icon="fab fa-adn">
  These payment methods are enabled by default for PayU Hosted Checkout:

  - NetBanking
  - Debit Card
  - Credit Card
  - UPI
  - Wallet

  You can request enablement of these additional methods from the PayU Dashboard if you are eligible:

  - BNPL
  - EMI
  - International Payments
</Accordion>

4. #### Does PayU Hosted Checkout reduce PCI compliance scope?

<Accordion title="Answer" icon="fab fa-adn">
  Yes. Since card data is collected on PayU infrastructure, PCI scope is reduced for your integration.<br />

  You should still secure:<br />

  - Your backend APIs and secrets
  - Callback and webhook endpoints
  - Never expose your merchant salt, authentication tokens, or secret keys.
</Accordion>

***

## Integration Setup

1. #### What are surl and furl?

<Accordion title="Answer" icon="fab fa-adn">
  - `surl` is the success URL. PayU redirects customers here after a successful payment.
  - `furl` is the failure URL. PayU redirects customers here if the payment fails or is cancelled.

  <Callout icon="far fa-circle-info" theme="info">
    ### **Tips:**

    A redirect to `surl` is not proof of payment. Browser redirects can fail if the customer closes their browser, the network drops, or the redirect is intercepted. Always verify payment status using reverse hash validation, a webhook, or the <Anchor target="_blank" href="https://docs.payu.in/reference/verify_payment_api">Verify Payment API</Anchor> before marking an order as paid.
  </Callout>
</Accordion>

2. #### Can localhost be used for testing callbacks?

<Accordion title="Answer" icon="fab fa-adn">
  No. PayU servers cannot reach:

  - Localhost or 127.0.0.1
  - Private IP addresses
  - VPN-only endpoints

  Your callback URL must be publicly reachable over HTTPS. For local development testing, use `https://test-payment-middleware.payu.in/simulatorResponse` as your `surl` and `furl`, or use a tunnelling service to expose your local server.
</Accordion>

3. #### How should I format the amount parameter?

<Accordion title="Answer" icon="fab fa-adn">
  Always use consistent decimal formatting. The exact `amount` string is included in the hash. Any mismatch between the hash string and the form field will cause a hash error.

  **Valid formats:** `100`, `100.00`, `99.50`

  **Invalid formats:** `₹100`, `100,00`, `100 INR`
</Accordion>

{/* NEW CONTENT: added from support case and AI chatbot analysis — high-frequency question (Postman/cURL testing) */}

4. #### Can I test the \_payment endpoint with Postman or cURL?

<Accordion title="Answer" icon="fab fa-adn">
  Yes, but with an important limitation: the `_payment` endpoint returns an HTML page (the PayU checkout UI), not a JSON response. A successful POST returns `HTTP 200` with checkout page HTML. This confirms your parameters and hash are accepted. However, the actual payment flow requires a browser to load and redirect through that HTML.<br />

  Use Postman or cURL to validate that your parameters and hash are correct before building the HTML form. Once validated, use the HTML form POST in a browser for the actual integration.<br />

  A ready-to-use cURL sample is available in the <Anchor target="_blank" href="https://docs.payu.in/docs/payu-hosted-checkout-build-integration#step-3-redirect-customers-to-payu-checkout">Build Integration → Step 3: Redirect Customers to PayU Checkout</Anchor>.
</Accordion>

{/* NEW CONTENT: added from support case analysis — mihpayid confusion is a common support ticket */}

5. #### What is mihpayid and how is it different from txnid?

<Accordion title="Answer" icon="fab fa-adn">
  | Field      | Generated by       | Purpose                                                                                                     |
  | ---------- | ------------------ | ----------------------------------------------------------------------------------------------------------- |
  | `txnid`    | You (the merchant) | Unique ID you create before each payment attempt. Used to match PayU's response to an order in your system. |
  | `mihpayid` | PayU               | PayU's internal transaction ID, returned in the payment response.                                           |

  Store both in your database. Use `txnid` to look up the order in your system. Use `mihpayid` when contacting [PayU Support.](https://help.payu.in/raise-ticket) It is the primary reference on PayU's side for locating a specific transaction.
</Accordion>

{/* NEW CONTENT: added from support case analysis — status vs unmappedstatus confusion seen in multiple cases */}

6. #### What is the difference between `status` and `unmappedstatus`?

<Accordion title="Answer" icon="fab fa-adn">
  `status` is the top-level outcome. `unmappedstatus` is the granular reason from the payment provider. Below is a list of `status` and `unmappedstatus` values.

  | `status`  | `unmappedstatus` | Description                                            |
  | --------- | ---------------- | ------------------------------------------------------ |
  | `success` | `captured`       | Payment confirmed and funds captured                   |
  | `failure` | `failed`         | Declined by the bank or payment provider               |
  | `failure` | `userCancelled`  | Customer clicked Back or cancelled the payment         |
  | `pending` | `pending`        | NEFT/RTGS transfer initiated, awaiting bank settlement |

  Both `failed` and `userCancelled` arrive as `status=failure`, use `unmappedstatus` to distinguish them and show the customer the right message. See <Anchor target="_blank" href="https://docs.payu.in/docs/payu-hosted-checkout-best-practices#error-recovery-ux">Best Practices → Error Recovery UX</Anchor> for recommended messaging per outcome.
</Accordion>

{/* NEW CONTENT: added from support case analysis — txnid reuse on retry is a frequent mistake seen in integration cases */}

7. #### Can I reuse a txnid after a failed payment retry?

<Accordion title="Answer" icon="fab fa-adn">
  No. Every payment attempt including retries must use a new, unique `txnid`. PayU may reject requests that reuse an existing transaction ID, or return the earlier transaction's result instead of processing a new one.<br />

  Generate a fresh `txnid` for every attempt, including retries from the same order.
</Accordion>

***

## Hash Generation

1. #### Why do I need to generate a hash?

<Accordion title="Answer" icon="fab fa-adn">
  You should generate a hash to secure the payment flow. PayU uses two types of hashing:

  | **Hash Type**    | Need                                                                                                                                                                                              |
  | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | **Forward Hash** | Authenticates your payment request. Computed before the transaction and submitted with it. Prevents an attacker from tampering with the payment amount, merchant key, or other fields in transit. |
  | **Reverse Hash** | Authenticates PayU's response. Computed after the transaction using the response fields. Confirms the response came from PayU and was not modified.                                               |
</Accordion>

2. #### What is the PayU Hosted Checkout forward hash formula?

<Accordion title="Answer" icon="fab fa-adn">
  ```text Hash Formula
  sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)
  ```

  Example with values (no UDFs sent):

  ```text
  gtKFFx|TXN001|100.00|Order123|Aarav|aarav@example.com|||||||||||eCwWELxi
  ```

  <Callout icon="far fa-circle-check" theme="success">
    ### **Important:**

    - [x] Include pipe separators even if UDF fields are empty.

    - [x] One missing pipe produces an invalid hash.

    - [x] Generate the hash on your server only and never in the browser.
  </Callout>
</Accordion>

3. #### How do I troubleshoot an invalid hash error?

<Accordion title="Answer" icon="fab fa-adn">
  Work through this debugging checklist:

  - [x] Verify the exact parameter order in your hash string.

  - [x] Verify the amount format (decimal string, e.g. `100.00`).

  - [x] Check for trailing or leading spaces in any parameter value.

  - [x] Confirm you are using the correct salt for the environment (test vs production).

  - [x] Confirm you have empty-string placeholders for unused UDF fields (still separated by `|`).

  - [x] Verify you are using SHA-512 (not SHA-256 or MD5).<br />

  Most hash failures come from wrong salt, missing pipes, whitespace, or amount format mismatch.
</Accordion>

4. #### Can I generate the hash in the browser or mobile app?

<Accordion title="Answer" icon="fab fa-adn">
  No. Generating the hash client-side would expose your merchant salt to anyone who inspects the source code. The salt is a secret credential. If it is exposed, attackers can forge payment requests. Hence, generate the hash on your server.
</Accordion>

***

## Checkout Experience

1. #### What happens if a customer closes their browser mid-payment?

<Accordion title="Answer" icon="fab fa-adn">
  The payment may still succeed depending on the stage at which the browser was closed. For example, if a customer approved a UPI payment and then closed the browser before being redirected:

  - The payment may have been captured successfully
  - The redirect to `surl` / `furl` will not arrive
  - A webhook notification will still arrive (if configured)

  <Callout icon="far fa-circle-info" theme="info">
    ### **Tips:**

    Always use <Anchor target="_blank" href="https://docs.payu.in/docs/manage-webhooks-using-dashboard">webhooks</Anchor>, the <Anchor target="_blank" href="https://docs.payu.in/reference/verify_payment_api">Verify Payment API</Anchor>, or the PayU Dashboard to confirm payment status.
  </Callout>
</Accordion>

***

## Testing

{/* NEW CONTENT: added from support case and AI chatbot analysis — UPI test VPA is the single highest-frequency question across both data sources (972 hits) */}

1. #### What UPI VPA should I use to test UPI payments in the sandbox?

<Accordion title="Answer" icon="fab fa-adn">
  Use `anything@payu` or `999999999@payu` as the UPI VPA (Virtual Payment Address) in the test environment (`https://test.payu.in/_payment`).

  <Callout icon="⚠️" theme="warn">
    ### **Warning!**

    These test VPAs only work with the `_payment` endpoint in the test environment. They do not work with the Validate VPA API, which requires a real registered VPA.
  </Callout>
</Accordion>

2. #### **Why does scanning the UPI QR code fail in the test environment?**

<Accordion title="Answer" icon="fab fa-adn">
  The test checkout page renders a UPI QR code, but it is not linked to a real UPI address. Scanning it with Google Pay, PhonePe, Paytm, or any other UPI app will return **Invalid UPI ID** or **Payment failed**. This is an expected behaviour in the sandbox. Instead of scanning the QR:

  1. On the PayU test checkout page, select **UPI**.
  2. Choose the **Enter UPI ID** option.
  3. Type `anything@payu` and proceed.
</Accordion>

{/* NEW CONTENT: added from support case analysis — EMI testing questions appear across 179 conversation hits */}

3. #### How do I test EMI payments in the sandbox?

<Accordion title="Answer" icon="fab fa-adn">
  Use a test credit card from the <Anchor target="_blank" href="https://docs.payu.in/docs/test-cards-upi-id-and-wallets">Test Integration</Anchor> page to attempt an EMI transaction. EMI will only appear as a payment option on the checkout page if:

  - Your merchant account has EMI enabled (**PayU Dashboard** → **Manage Checkout** → **Payment Modes**)
  - The credit card BIN is eligible for EMI<br />

  If EMI is not appearing even after enabling it, contact your PayU Key Account Manager to confirm eligibility and activation.<br />

  **Cardless EMI (BNPL):** Has a separate test flow. See the <Anchor target="_blank" href="https://docs.payu.in/docs/test-cards-upi-id-and-wallets#test-bnpl-credentials">Test BNPL credentials</Anchor> for test credentials and expected responses.
</Accordion>

***

## Reverse Hashing

1. #### What is reverse hash validation?

<Accordion title="Answer" icon="fab fa-adn">
  Reverse hash validation confirms that PayU's response is authentic and was not tampered with.<br />

  After a payment, PayU POSTs a response to your `surl` or `furl`. You should:

  1. Extract the `hash` field from the response.
  2. Compute the reverse hash using:&#x20;
     ```text Hash Formula
     sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
     ```
  3. Compare your computed hash with the `hash` from the response.
  4. If they match, the response is authentic. If not, reject it and log the event as a security alert.
</Accordion>

2. #### What causes a reverse hash mismatch?

<Accordion title="Answer" icon="fab fa-adn">
  Common causes for reverse hash mismatch are:

  - Using the forward hash formula instead of the reverse hash formula
  - Wrong parameter order (note: UDFs are in **reverse** order: udf5 → udf1)
  - Using the wrong salt
  - Response data was modified after receipt
  - Whitespace in any response parameter value
</Accordion>

***

## Callback vs Webhook

1. #### What is the difference between a callback and a webhook?

<Accordion title="Answer" icon="fab fa-adn">
  | Callback                                    | Webhook                                     |
  | ------------------------------------------- | ------------------------------------------- |
  | Browser redirect to `surl` or `furl`        | Server-to-server POST to your webhook URL   |
  | Depends on the customer's browser session   | Independent of the customer's browser       |
  | Can fail if browser closes or network drops | More reliable for guaranteed delivery       |
  | Arrives quickly                             | Arrives after PayU confirms the transaction |

  **We recommend to use both:** Handle the callback for immediate user feedback, and rely on webhooks for authoritative payment confirmation.
</Accordion>

{/* NEW CONTENT: added from support case analysis — webhook hash verification is one of the top webhook issues in SFDC cases */}

2. #### How do I verify the hash on a webhook notification?

<Accordion title="Answer" icon="fab fa-adn">
  Webhook notifications use the same hash formula as the browser callback. Compute the reverse hash on your server using:

  ```
  sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
  ```

  Use the exact field values from the webhook POST body. If your computed hash matches the `hash` field in the webhook payload, the notification is authentic.

  <Callout icon="⚠️" theme="warn">
    ### **Warning!**

    Note the UDF order in the reverse hash: **udf5 → udf1** (reverse of the forward hash). This is the most common cause of webhook hash mismatches.
  </Callout>

  See <Anchor target="_blank" href="https://docs.payu.in/docs/payu-hosted-checkout-build-integration#step-4-verify-response-via-reverse-hashing">Build Integration → Step 4: Verify Response via Reverse Hashing</Anchor> for language-specific implementation guidance and the full reverse hash formula.
</Accordion>

{/* NEW CONTENT: added from support case analysis — webhook configuration is the second most common webhook support ticket (54 cases on Help in configuration) */}

3. #### Where do I configure my webhook URL in PayU Dashboard?

<Accordion title="Answer" icon="fab fa-adn">
  Log in to [PayU Dashboard](https://onboarding.payu.in/) → **Developers&#x20;**→ **Webhooks**. Add your webhook endpoint URL there.

  Requirements for the webhook endpoint:

  - Publicly reachable over HTTPS
  - Returns HTTP 200 after receiving and processing the notification (returning any other code causes PayU to retry)

  See <Anchor target="_blank" href="https://docs.payu.in/docs/manage-webhooks-using-dashboard">Manage Webhooks</Anchor> for the full setup guide and webhook payload format.
</Accordion>

***

## Duplicate Processing

1. #### How do I prevent duplicate order processing?

<Accordion title="Answer" icon="fab fa-adn">
  PayU may send a callback or webhook more than once (if your endpoint didn't return HTTP 200, or due to retry logic). Implement idempotency:

  - Check if the `txnid` has already been processed before updating order status.
  - Use a database unique constraint on `txnid` or an order state machine (Unpaid → Processing → Paid) that ignores duplicate updates.
  - Return HTTP 200 from your callback/webhook handler immediately after receiving the notification to prevent retry loops.
</Accordion>

***

## Production Go-Live

1. #### What is the production readiness checklist?

<Accordion title="Answer" icon="fab fa-adn">
  Before going live, verify:

  **Security:**

  - [x] Merchant salt stored securely, never in source code


  - [x] Hash generated server-side only


  - [x] HTTPS enforced on all callback and webhook endpoints

  **Functional:**

  - [x] Success, failure, and pending transaction flows tested


  - [x] Reverse hash validation implemented and tested


  - [x] Webhook configured and receiving notifications


  - [x] Duplicate processing protection implemented

  See the <Anchor target="_blank" href="https://docs.payu.in/docs/payu-hosted-checkout-go-live-checklist">Go-Live Checklist</Anchor> for the complete list.
</Accordion>
