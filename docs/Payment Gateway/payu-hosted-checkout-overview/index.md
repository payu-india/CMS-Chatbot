---
title: PayU Hosted Checkout Overview
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Prebuilt Web Checkout or PayU Hosted Checkout Integration
  description: >-
    Understand PayU Hosted Checkout for payment gateway integration. Learn
    payment flow, key concepts, and how to handle online payments securely.
  keywords:
    - PayU Hosted Checkout
    - payment gateway integration
    - payment flow
    - online payments
    - PayU integration
  robots: index
next:
  description: ''
---
This page helps you understand how **PayU Hosted Checkout** works before you begin integration.

## What is PayU Hosted Checkout?

PayU Hosted Checkout is a payment integration method where:

* You redirect users from your website to a **PayU-hosted payment page**
* PayU handles the entire payment experience, including security and processing
* After the payment is completed, users are redirected back to your website

This is the **simplest and fastest way** to start accepting payments without building or managing your own payment UI.

***

## How Payment Flow Works

The payment journey in Hosted Checkout looks like this:

<Image align="center" alt="PayU Hosted Checkout Workflow" border={true} src="https://files.readme.io/932f800-payuhosted_wf.png" className="border" />

<Accordion title="Step 1: Initiate Payment" icon="fa-shopping-cart">
  Customer selects items and initiates the payment on the merchant website.
</Accordion>

<Accordion title="Step 2: Redirect to PayU" icon="fa-external-link-alt">
  Customer is redirected to PayU Checkout to enter payment details.
</Accordion>

<Accordion title="Step 3: Send to Bank" icon="fa-paper-plane">
  PayU sends the payment request with transaction details to the bank or provider.
</Accordion>

<Accordion title="Step 4: Process Payment" icon="fa-university">
  The bank processes the transaction and returns a success or failure status to PayU.
</Accordion>

<Accordion title="Step 5: Return Response" icon="fa-reply">
  PayU redirects the customer back to the merchant website with the payment result.
</Accordion>

This flow ensures that sensitive payment data is handled by PayU, reducing your security and compliance overhead.

***

## Customer journey

Below diagram depicts the end user experience during a payment using PayU Hosted Checkout:

<Image align="center" src="https://files.readme.io/bc1c758a83c0c601d161a5621e1fe47a6d4c757e847a893b33b05419972e693a-b7b3bc19c28693be346591ec8a2c29ee07fcf47cb088bc6c9a6c34950c2af0dc-payu_hosted_checkout-workflow.png" />

The following is the customer journey using cards as a payment method:

<Cards columns={3}>
  <Card>
    <div style={{ color: "#000", padding: "8px" }}>
      <i className="fa fa-mouse-pointer" style={{ color: "#00b386", fontSize: "20px", marginBottom: "10px" }} />

      <h4 style={{ margin: "0 0 6px 0", fontWeight: "600" }}>Initiate Payment</h4>

      <p style={{ margin: 0 }}>
        Customer clicks <b>Pay Now</b> on your website or app.
      </p>
    </div>
  </Card>

  <Card>
    <div style={{ color: "#000", padding: "8px" }}>
      <i className="fa fa-external-link-alt" style={{ color: "#00b386", fontSize: "20px", marginBottom: "10px" }} />

      <h4 style={{ margin: "0 0 6px 0", fontWeight: "600" }}>Redirect to PayU</h4>

      <p style={{ margin: 0 }}>
        Customer is redirected to the PayU Hosted Checkout page.
      </p>
    </div>
  </Card>

  <Card>
    <div style={{ color: "#000", padding: "8px" }}>
      <i className="fa fa-credit-card" style={{ color: "#00b386", fontSize: "20px", marginBottom: "10px" }} />

      <h4 style={{ margin: "0 0 6px 0", fontWeight: "600" }}>Enter Payment Details</h4>

      <p style={{ margin: 0 }}>
        Customer selects payment method and enters details (Card, UPI, NetBanking, Wallet).
      </p>
    </div>
  </Card>

  <Card>
    <div style={{ color: "#000", padding: "8px" }}>
      <i className="fa fa-shield-alt" style={{ color: "#00b386", fontSize: "20px", marginBottom: "10px" }} />

      <h4 style={{ margin: "0 0 6px 0", fontWeight: "600" }}>Authenticate Payment</h4>

      <p style={{ margin: 0 }}>
        Customer completes authentication (OTP, UPI approval, etc.).
      </p>
    </div>
  </Card>

  <Card>
    <div style={{ color: "#000", padding: "8px" }}>
      <i className="fa fa-university" style={{ color: "#00b386", fontSize: "20px", marginBottom: "10px" }} />

      <h4 style={{ margin: "0 0 6px 0", fontWeight: "600" }}>Payment Processing</h4>

      <p style={{ margin: 0 }}>
        PayU processes the transaction with the bank or payment provider.
      </p>
    </div>
  </Card>

  <Card>
    <div style={{ color: "#000", padding: "8px" }}>
      <i className="fa fa-check-circle" style={{ color: "#00b386", fontSize: "20px", marginBottom: "10px" }} />

      <h4 style={{ margin: "0 0 6px 0", fontWeight: "600" }}>Payment Status</h4>

      <p style={{ margin: 0 }}>
        Customer is redirected back to your website with success or failure status.
      </p>
    </div>
  </Card>
</Cards>

***

## Key Concepts

Understanding the following basic concepts will help you navigate the integration more easily:

<Cards columns={3}>
  <Card>
    <div style={{ color: "#000", padding: "8px" }}>
      <i className="fa fa-exchange-alt" style={{ color: "#00b386", fontSize: "20px", marginBottom: "10px" }} />

      <h4 style={{ margin: "0 0 6px 0", fontWeight: "600" }}>Transaction</h4>

      <p style={{ margin: 0 }}>
        A single payment attempt initiated by the customer on your website.
      </p>
    </div>
  </Card>

  <Card>
    <div style={{ color: "#000", padding: "8px" }}>
      <i className="fa fa-paper-plane" style={{ color: "#00b386", fontSize: "20px", marginBottom: "10px" }} />

      <h4 style={{ margin: "0 0 6px 0", fontWeight: "600" }}>Payment Request</h4>

      <p style={{ margin: 0 }}>
        The payment data sent from your server to PayU to initiate a transaction.
      </p>
    </div>
  </Card>

  <Card>
    <div style={{ color: "#000", padding: "8px" }}>
      <i className="fa fa-reply" style={{ color: "#00b386", fontSize: "20px", marginBottom: "10px" }} />

      <h4 style={{ margin: "0 0 6px 0", fontWeight: "600" }}>Payment Response</h4>

      <p style={{ margin: 0 }}>
        The transaction result returned by PayU after payment processing.
      </p>
    </div>
  </Card>

  <Card>
    <div style={{ color: "#000", padding: "8px" }}>
      <i className="fa fa-random" style={{ color: "#00b386", fontSize: "20px", marginBottom: "10px" }} />

      <h4 style={{ margin: "0 0 6px 0", fontWeight: "600" }}>Redirect Flow</h4>

      <p style={{ margin: 0 }}>
        Customer is redirected to PayU for payment and back to your site after completion.
      </p>
    </div>
  </Card>

  <Card>
    <div style={{ color: "#000", padding: "8px" }}>
      <i className="fa fa-server" style={{ color: "#00b386", fontSize: "20px", marginBottom: "10px" }} />

      <h4 style={{ margin: "0 0 6px 0", fontWeight: "600" }}>API Flow</h4>

      <p style={{ margin: 0 }}>
        Server-to-server communication for handling payment verification and status updates.
      </p>
    </div>
  </Card>
</Cards>

***

## Why Use PayU Hosted Checkout

PayU Hosted Checkout helps you accept online payments quickly without building or managing a payment interface.

<Accordion title="Benefits" icon="fa-rocket">
  * **Faster Go-Live**: Integrate and start accepting payments with minimal development effort.
  * **Built-in Security and Compliance:** Sensitive payment data is handled by PayU, reducing your PCI-DSS compliance burden.
  * **Multiple Payment Methods:** Accept payments via cards, UPI, netbanking, and wallets through a single integration.
  * **Easy Payment Method Enablement:** Enable or disable payment options without additional development effort.
  * **Customizable Checkout Experience:** Align the PayU-hosted payment page with your brand using logos, colors, and language options.
  * **Improved Conversion Experience:** Leverage optimized checkout flows, saved preferences, and payment recommendations.
  * **Reduced Engineering Overhead:** No need to build or maintain payment UI, validation, or bank integrations.
</Accordion>

***

## Capabilities of PayU Hosted Checkout

<Accordion title="Features" icon="fa-cogs">
  * **Prebuilt Payment Page:** A ready-made checkout page hosted by PayU to collect payment details securely.
  * **Redirect-Based Integration:** Simple integration using a redirect flow from your website to PayU.
  * **Secure Payment Handling:** Handles authentication flows such as OTP and bank verification securely.
  * **Quick Integration Setup:** Integration kits and APIs enable faster implementation with minimal setup.
  * **Mobile-Optimized Experience:** Supports responsive checkout flows and mobile payment intents (UPI).
  * **Smart Payment Experience:** Supports features like payment recommendations and saved preferences.
</Accordion>

<br />

## Next Steps

To integrate PayU Hosted Integration on your website or mobile, refer to:

* [Web Integration - PayU Hosted](https://docs.payu.in/docs/prebuilt-checkout-page-integration) using the **Collect Payment **API (**_payment** API),

* [Integrate WebView for Mobile Apps](https://docs.payu.in/docs/webview-for-mobile-apps) by embedding PayU's Hosted Checkout experience inside a WebView container within your mobile app.

<br />

<Callout icon="📮" theme="default">
  **Postman Collection**: Download the PayU Hosted Checkout Postman Collection from the following location:

  [https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/collection/rocz44o/payu-hosted-checkout-collection-complete-integration](https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/collection/rocz44o/payu-hosted-checkout-collection-complete-integration)
</Callout>

<br />
