---
title: How PayU Hosted Checkout Works
excerpt: >-
  Understand the complete payment journey. From your website to PayU and back.
  Learn what happens at each step, including redirect, authentication, and
  payment response.
deprecated: false
hidden: true
metadata:
  title: How PayU Hosted Checkout Works
  description: >-
    Step-by-step explanation of the PayU Hosted Checkout payment flow: payment
    request, redirect, authentication, response, and verification.
  keywords:
    - payu hosted checkout payment flow
    - how payu hosted checkout works
    - payu redirect payment flow india
    - payu checkout customer journey
    - payu surl furl callback explained
    - payu payment response verification flow
    - payu transaction outcomes success failure pending
  robots: index
next:
  description: Explore related information and resources.
  pages:
    - slug: payu-hosted-checkout-1
      title: PayU Hosted Checkout
      type: basic
---
{/* NEW CONTENT: This page was created to support the Tier 2 documentation model. The payment flow diagrams and customer journey cards are moved from the existing Overview page; the conceptual explanations of key terms are new. */}

This page explains what happens during a PayU Hosted Checkout payment — from the moment a customer clicks **Pay Now** to the moment you confirm the transaction on your server.

Understanding this flow helps you build the integration correctly and handle edge cases with confidence.

***

## The Integration Workflow

{/* Source: "What you're building" description — docs/Collect Payments/introduction-web/prebuilt-checkout-payu-hosted/prebuilt-checkout-page-integration.md; workflow image — docs/Docs For Internal Review/payu-hosted-checkout/index.md; hash formulas and endpoints confirmed across integrate/build-integration.md and accept-payments-using-payu-hosted-checkout.md. */}

What you're building: a server-generated redirect that sends customers from your site to the PayU-hosted payment page, then returns them to your success or failure URLs. You prepare payment parameters server-side, generate a SHA-512 hash for request integrity, and POST them to PayU. PayU handles the payment UI, bank authentication, and payment processing.


<Image src="https://files.readme.io/932f800-payuhosted_wf.png" alt="PayU Hosted Checkout Integration Workflow" align="center" border={true} />


<Accordion title="Step 1: Prepare request parameters on your server" icon="fa-list-check">
  When a customer proceeds to pay, your server collects the mandatory transaction fields: `key` (your merchant key), `txnid` (a unique transaction ID you generate), `amount`, `productinfo`, `firstname`, `email`, `phone`, `surl`, and `furl`.

  Generate a unique `txnid` for each transaction — this is your primary reference for tracking, reconciliation, and preventing duplicate processing.

  See [Build Integration](./integrate/build-integration) for the full mandatory and optional parameter list.
</Accordion>

<Accordion title="Step 2: Generate the SHA-512 hash on your server" icon="fa-lock">
  Before sending the request to PayU, your server computes a SHA-512 hash of the payment parameters. This hash authenticates the request and prevents parameter tampering in transit.

  **Hash formula:**

  ```text
  sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)
  ```

  The hash must be generated on your server using your merchant salt — never in the browser or in client-side code. Exposing the salt client-side allows attackers to forge payment requests.
</Accordion>

<Accordion title="Step 3: POST the payment request to PayU" icon="fa-paper-plane">
  Submit all parameters — including the computed hash — as an HTML form `POST` to the PayU payment endpoint:

  | Environment | Endpoint                          |
  | ----------- | --------------------------------- |
  | Test        | `https://test.payu.in/_payment`   |
  | Production  | `https://secure.payu.in/_payment` |

  The customer's browser is redirected to the PayU-hosted checkout page. From this point, PayU handles the entire payment UI — collecting payment details, managing bank authentication (OTP, UPI approval, 3DS flows), and communicating with the bank or payment provider. Your server is not involved in this step and never receives raw card data.
</Accordion>

<Accordion title="Step 4: PayU POSTs the result to your callback URL" icon="fa-reply">
  After the customer completes or abandons payment, PayU POSTs the payment result to your `surl` (on success) or `furl` (on failure or cancellation). The POST body contains the transaction status (`success`, `failure`, or `pending`), PayU's transaction ID (`mihpayid`), the original `txnid`, and a response hash.
</Accordion>

<Accordion title="Step 5: Verify the response hash on your server" icon="fa-shield-check">
  Before updating your order records, your server validates the response using the reverse hash:

  **Reverse hash formula:**

  ```text
  sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
  ```

  1. Compute the reverse hash from the response fields.
  2. Compare it with the `hash` field in PayU's response.
  3. If they match, the response is authentic — update order status based on `status`.
  4. If they don't match, reject the response and log it as a security event.

  Never mark an order as paid based on the browser redirect or `status` field alone — always validate the reverse hash first.
</Accordion>

***

## The Customer Experience

The following shows the customer journey when paying by card. Other payment methods (UPI, netbanking, wallet) follow the same overall flow with method-specific authentication steps.


<Image src="https://files.readme.io/bc1c758a83c0c601d161a5621e1fe47a6d4c757e847a893b33b05419972e693a-b7b3bc19c28693be346591ec8a2c29ee07fcf47cb088bc6c9a6c34950c2af0dc-payu_hosted_checkout-workflow.png" align="center" />


<Cards>
  <Card>
    <div style={{ color: "#000", padding: "8px" }}>
      <div style={{ display: "flex", alignItems: "center", gap: "10px", marginBottom: "6px" }}>
        <i className="fa fa-mouse-pointer" style={{ color: "#00b386", fontSize: "20px", lineHeight: 1 }}></i>
        <h4 style={{ margin: 0, fontWeight: "600" }}>Initiate Payment</h4>
      </div>
      <p style={{ margin: 0 }}>Customer clicks <b>Pay Now</b> on your website or app.</p>
    </div>
  </Card>

  <Card>
    <div style={{ color: "#000", padding: "8px" }}>
      <div style={{ display: "flex", alignItems: "center", gap: "10px", marginBottom: "6px" }}>
        <i className="fa fa-external-link-alt" style={{ color: "#00b386", fontSize: "20px", lineHeight: 1 }}></i>
        <h4 style={{ margin: 0, fontWeight: "600" }}>Redirect to PayU</h4>
      </div>
      <p style={{ margin: 0 }}>Customer is redirected to the PayU Hosted Checkout page.</p>
    </div>
  </Card>

  <Card>
    <div style={{ color: "#000", padding: "8px" }}>
      <div style={{ display: "flex", alignItems: "center", gap: "10px", marginBottom: "6px" }}>
        <i className="fa fa-credit-card" style={{ color: "#00b386", fontSize: "20px", lineHeight: 1 }}></i>
        <h4 style={{ margin: 0, fontWeight: "600" }}>Enter Payment Details</h4>
      </div>
      <p style={{ margin: 0 }}>Customer selects a payment method and enters details (Card, UPI, NetBanking, Wallet).</p>
    </div>
  </Card>

  <Card>
    <div style={{ color: "#000", padding: "8px" }}>
      <div style={{ display: "flex", alignItems: "center", gap: "10px", marginBottom: "6px" }}>
        <i className="fa fa-shield-alt" style={{ color: "#00b386", fontSize: "20px", lineHeight: 1 }}></i>
        <h4 style={{ margin: 0, fontWeight: "600" }}>Authenticate Payment</h4>
      </div>
      <p style={{ margin: 0 }}>Customer completes authentication (OTP, UPI approval, etc.).</p>
    </div>
  </Card>

  <Card>
    <div style={{ color: "#000", padding: "8px" }}>
      <div style={{ display: "flex", alignItems: "center", gap: "10px", marginBottom: "6px" }}>
        <i className="fa fa-university" style={{ color: "#00b386", fontSize: "20px", lineHeight: 1 }}></i>
        <h4 style={{ margin: 0, fontWeight: "600" }}>Payment Processing</h4>
      </div>
      <p style={{ margin: 0 }}>PayU processes the transaction with the bank or payment provider.</p>
    </div>
  </Card>

  <Card>
    <div style={{ color: "#000", padding: "8px" }}>
      <div style={{ display: "flex", alignItems: "center", gap: "10px", marginBottom: "6px" }}>
        <i className="fa fa-check-circle" style={{ color: "#00b386", fontSize: "20px", lineHeight: 1 }}></i>
        <h4 style={{ margin: 0, fontWeight: "600" }}>Payment Status</h4>
      </div>
      <p style={{ margin: 0 }}>Customer is redirected back to your website with success or failure status.</p>
    </div>
  </Card>
</Cards>

***

## Key Terms

{/* NEW CONTENT: Conceptual explanations to help mixed audiences (merchants + developers) understand the integration vocabulary. */}

Understanding these concepts makes the integration guide easier to follow.

**Transaction** — A single payment attempt. Each transaction has a unique ID (`txnid`) that you generate and that PayU uses to track the payment across all systems.

**Payment Request** — The data your server sends to PayU to initiate a transaction. It includes the order amount, customer information, callback URLs, and a secure hash.

**Hash (forward hash)** — A SHA-512 digest of your payment parameters. It proves to PayU that the request hasn't been tampered with in transit. Generated on your server using your merchant salt — never in the browser.

**Redirect flow** — The customer's browser is redirected from your site to PayU's checkout page, then back to your site. You post the payment request as an HTML form `POST` to PayU's endpoint.

**surl / furl** — Your success URL and failure URL. PayU POSTs the payment result back to these endpoints after the transaction completes. They must be publicly reachable HTTPS URLs.

**Payment Response** — What PayU sends back to your `surl` or `furl`. Contains the transaction status, PayU's transaction ID (`mihpayid`), and a response hash you must verify.

**Reverse hash** — A SHA-512 hash generated from the response parameters. You generate it on your server and compare it with the hash in PayU's response. If they match, the response is authentic.

**Webhook** — A server-to-server notification PayU sends to your server when a transaction completes. More reliable than the browser redirect, because it doesn't depend on the customer's browser session.

***

## Transaction Outcomes

After a payment attempt, PayU redirects the customer to one of your URLs and POSTs the result:

| Outcome       | Redirect | What it means                                         |
| ------------- | -------- | ----------------------------------------------------- |
| **Success**   | `surl`   | Payment was captured by the bank                      |
| **Failure**   | `furl`   | Payment was declined or failed                        |
| **Pending**   | `surl`   | Transaction is in progress (NEFT/RTGS or delayed UPI) |
| **Cancelled** | `furl`   | Customer cancelled before completing payment          |

<Callout icon="⚠️" theme="warn">
  **Always verify on your server**

  Never mark an order as paid based on the browser redirect alone. Browser redirects can fail, be intercepted, or be spoofed. Always verify the response hash (reverse hash) on your backend before updating order status.
</Callout>

***

## Next Step

Ready to build? Go to the [Quick Start](./quick-start) to make your first test payment, or go directly to [Build Integration](./integrate/build-integration) for the full step-by-step technical guide.

<br />
