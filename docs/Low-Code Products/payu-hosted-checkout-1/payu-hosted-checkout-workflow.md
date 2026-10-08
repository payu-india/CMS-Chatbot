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
PayU Hosted Checkout is a redirect-based payment integration. When a customer initiates a payment, your application redirects them to a PayU-hosted payment page where they complete the transaction. PayU handles the hosted payment experience — payment method selection, authentication, and processing. The payment result is then returned to your application through a configured callback.

***

## How Does the Payment Flow Work?


<Image src="https://files.readme.io/932f800-payuhosted_wf.png" alt="PayU Hosted Checkout payment flow" align="center" border={true} />


The payment moves through six stages:

1. **Initiation** — The customer proceeds to pay on your website or app. Your application prepares the payment details and redirects them to the PayU-hosted payment page.
2. **Redirect** — The customer arrives at the PayU checkout page. Your application is no longer involved in the payment interaction from this point.
3. **Payment selection and entry** — The customer selects a payment method and enters their payment details directly on PayU's hosted page.
4. **Authentication** — PayU manages all authentication: OTP prompts for card payments, UPI collect or intent flows, wallet logins, and net banking redirects.
5. **Processing** — PayU sends the transaction to the relevant bank, card network, or payment provider and receives the result.
6. **Return** — PayU redirects the customer back to your application and posts the payment result to your configured callback URL.

***

## What Happens When a Customer Makes a Payment?

The following shows the customer journey for a card payment. UPI, net banking, and wallet payments follow the same overall stages with method-specific authentication steps.


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

## What Happens After the Payment?

After the transaction completes, PayU determines the outcome and returns it to your application:

| Outcome       | Callback | What it means                                                                |
| ------------- | -------- | ---------------------------------------------------------------------------- |
| **Success**   | `surl`   | Payment was captured by the bank                                             |
| **Failure**   | `furl`   | Payment was declined or failed                                               |
| **Pending**   | `surl`   | Transaction is still being processed (for example, NEFT/RTGS or delayed UPI) |
| **Cancelled** | `furl`   | Customer cancelled before completing payment                                 |

The payment result arrives at your application in two ways:

- **Browser redirect** — PayU redirects the customer's browser to your `surl` or `furl` and posts the result. This depends on the customer's browser session remaining active through the redirect.
- **Webhook** — PayU posts the result server-to-server to a webhook endpoint you configure. Webhooks arrive independently of the browser session and are the more reliable mechanism for confirming payment outcomes.

Your application should verify the result before treating the payment as confirmed and updating its order or payment state.

For implementation details — callback URL configuration, result verification, and webhook setup — see [Build Integration](./integrate/build-integration).

***

## What Does PayU Handle?

- **Hosted payment page** — PayU serves the checkout interface the customer interacts with. Your website and servers have no involvement during this step.
- **Payment details collection** — Card numbers, UPI addresses, and other sensitive payment information are entered directly on PayU's infrastructure. Your application never receives this data.
- **Authentication** — PayU manages all authentication flows: 3DS OTP prompts for card payments, UPI collect and intent flows, wallet logins, and net banking redirects.
- **Payment processing** — PayU communicates with the relevant bank, card network, UPI provider, or wallet to process the transaction.
- **Returning the result** — PayU posts the payment outcome to your callback URL and redirects the customer's browser back to your application.

***

## What Does Your Application Handle?

- **Initiating the payment** — When the customer proceeds to pay, your application prepares the payment details and redirects them to the PayU payment page.
- **Securing the request** — Your application generates a security signature for the payment request on the server side. This ensures the request cannot be tampered with in transit and cannot be forged.
- **Receiving the payment result** — Your application exposes a callback endpoint that PayU posts the result to after the transaction.
- **Verifying the result** — Your application confirms that the result is authentic before acting on it. This is a mandatory step — the browser redirect alone is not sufficient confirmation.
- **Updating order state** — Based on the verified outcome, your application marks the order as paid, failed, or pending accordingly.

***

## Key Concepts

**Transaction** — A single payment attempt. Each transaction has a unique identifier you assign (`txnid`) that tracks the payment across your system and PayU.

**Payment Request** — The payment data your application sends to PayU to initiate a transaction: the amount, customer details, callback URLs, and a security signature.

**Redirect Flow** — The mechanism by which the customer's browser moves from your application to the PayU-hosted payment page and back. Your application initiates this by submitting the payment request.

**surl / furl** — The callback URLs your application provides. PayU posts the payment result to the success URL (`surl`) on a successful or pending outcome, and to the failure URL (`furl`) on failure or cancellation. Both must be publicly reachable HTTPS endpoints.

**Payment Response** — The result PayU posts to your `surl` or `furl` after the transaction. Contains the outcome, transaction identifiers, and a signature your application uses to verify authenticity before updating order state.

***

## Next Steps

- [Quick Start](./quick-start) — Set up and run your first test payment in the sandbox.
- [Build Integration](./integrate/build-integration) — Complete technical implementation: request parameters, security signature generation, endpoint configuration, response verification, and webhooks.
