---
title: Copy of PayU Hosted Checkout
excerpt: >-
  Understand PayU Hosted Checkout for payment gateway integration. Learn payment
  flow, key concepts, and how to handle online payments securely.
deprecated: false
hidden: true
metadata:
  title: PayU Hosted Checkout Overview | Payment Gateway Integration
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
---
This page helps you understand how **PayU Hosted Checkout** works before you begin integration.

<Callout icon="🟡" theme="info">
  ### **Some Technical Setup Required**

  This product integration needs minimum technical setup. A developer can help, but many merchants manage this with guided steps.
</Callout>

***

## What is PayU Hosted Checkout?

PayU Hosted Checkout is a payment integration method where:

- You redirect customers from your website to a **PayU-hosted payment page**
- PayU handles the entire payment experience, including security and processing
- After the payment is completed, customers are redirected back to your website

This is the simplest and fastest way to accept payments through a checkout flow on your website.

***

## When Should You Use This?

PayU Hosted Checkout is best when you want a straightforward, secure payment page and do not need it to match your website's design exactly. Most merchants start here because it gets you live quickly with minimal development effort.<br />

If you need complete control over how the payment page looks and feels — where every element matches your site's brand precisely — see [Merchant Hosted Checkout](https://docs.payu.in/docs/custom-checkout-merchant-hosted) instead. That approach requires more development work but gives you exact design control.<br />

<Callout icon="🟢" theme="info">
  ### Other Easy Ways

  - If you do not want a technical setup or you do not have a website yet, PayU also offers Pay Handle — a payment link you can send customers directly, with no integration required. See [Pay Handle](https://docs.payu.in/collect-payments/introduction-no-code-payments-integration/payment-links-dashboard) →
  - If you are not sure which product to use, answer few simple questions to get recommended products.
</Callout>

***

## What You Get

<Accordion title="Key Benefits" icon="fa-rocket">
  - **No PCI-DSS burden on you:** When a customer enters their card details on the PayU-hosted page, that sensitive payment data is handled entirely by PayU. PCI-DSS — the security standard that governs how card data must be stored, transmitted, and processed — is normally your responsibility to maintain; PayU Hosted Checkout takes that on for you, so you avoid the complexity and cost of certification.

  - **Multiple payment methods, one integration:** Accept payments via cards, UPI, netbanking, and wallets through a single integration, without building separate flows for each payment type. The PayU Checkout page automatically adapts to mobile screens and handles mobile payment intents (like UPI deep-linking on mobile web) without extra configuration on your side.

  - **Fast to launch, low ongoing engineering effort:** A ready-made checkout page hosted by PayU eliminates the need to build your own payment form, validation logic, or direct integrations with banks and payment providers. This requires far less development than building your own payment page, and PayU handles all of that infrastructure for you going forward.

  - **Manage payment methods without code:** When you want to enable or disable a payment option (like adding a new wallet or bank), you can do it from your PayU Dashboard without writing any code or redeploying your website — it's a configuration change, not a development task.

  - **Branding and conversion features:** While PayU hosts the payment page, you can still align it with your brand using your logo, color scheme, and language preferences (several Indian languages are supported). The page also includes features like saved payment preferences for returning customers and intelligent payment method recommendations that help more customers complete their purchases.
</Accordion>

***

## How it works

Below diagram depicts the customer experience during a payment using PayU Hosted Checkout:


<Image src="https://files.readme.io/bc1c758a83c0c601d161a5621e1fe47a6d4c757e847a893b33b05419972e693a-b7b3bc19c28693be346591ec8a2c29ee07fcf47cb088bc6c9a6c34950c2af0dc-payu_hosted_checkout-workflow.png" align="center" />


The following is the customer journey using cards as a payment method:

<Cards columns="3">
  <Card>
    <div style={{ color: "#000", padding: "8px" }}>
      <i className="fa fa-mouse-pointer" style={{ color: "#00b386", fontSize: "20px", marginBottom: "10px" }}></i>

      <h4 style={{ margin: "0 0 6px 0", fontWeight: "600" }}>Initiate Payment</h4>

      <p style={{ margin: 0 }}>

        Customer clicks <b>Pay Now</b> on your website or app. This payment attempt is called a <b>transaction</b>, and it's tracked with a unique transaction ID so you can look it up later in your PayU Dashboard or retrieve its details via API.
      </p>
    </div>
  </Card>

  <Card>
    <div style={{ color: "#000", padding: "8px" }}>
      <i className="fa fa-external-link-alt" style={{ color: "#00b386", fontSize: "20px", marginBottom: "10px" }}></i>

      <h4 style={{ margin: "0 0 6px 0", fontWeight: "600" }}>Redirect to PayU</h4>

      <p style={{ margin: 0 }}>

        Customer is redirected to the PayU Hosted Checkout page. At this point, your website or server sends PayU the transaction details — the order amount, customer information, and what's being purchased. This package of data is the <b>Payment Request</b>.
      </p>
    </div>
  </Card>

  <Card>
    <div style={{ color: "#000", padding: "8px" }}>
      <i className="fa fa-credit-card" style={{ color: "#00b386", fontSize: "20px", marginBottom: "10px" }}></i>

      <h4 style={{ margin: "0 0 6px 0", fontWeight: "600" }}>Enter Payment Details</h4>

      <p style={{ margin: 0 }}>

        Customer selects payment method and enters details (Card, UPI, NetBanking, Wallet).
      </p>
    </div>
  </Card>

  <Card>
    <div style={{ color: "#000", padding: "8px" }}>
      <i className="fa fa-shield-alt" style={{ color: "#00b386", fontSize: "20px", marginBottom: "10px" }}></i>

      <h4 style={{ margin: "0 0 6px 0", fontWeight: "600" }}>Authenticate Payment</h4>

      <p style={{ margin: 0 }}>

        Customer completes authentication (OTP, UPI approval, etc.).
      </p>
    </div>
  </Card>

  <Card>
    <div style={{ color: "#000", padding: "8px" }}>
      <i className="fa fa-university" style={{ color: "#00b386", fontSize: "20px", marginBottom: "10px" }}></i>

      <h4 style={{ margin: "0 0 6px 0", fontWeight: "600" }}>Payment Processing</h4>

      <p style={{ margin: 0 }}>

        PayU processes the transaction with the bank or payment provider.
      </p>
    </div>
  </Card>

  <Card>
    <div style={{ color: "#000", padding: "8px" }}>
      <i className="fa fa-check-circle" style={{ color: "#00b386", fontSize: "20px", marginBottom: "10px" }}></i>

      <h4 style={{ margin: "0 0 6px 0", fontWeight: "600" }}>Payment Status</h4>

      <p style={{ margin: 0 }}>

        Customer is redirected back to your website with success or failure status. PayU sends back the result — whether the transaction succeeded, failed, or is still pending, along with details like the transaction ID and payment method used. This is the <b>Payment Response</b>, which your site uses to show the customer a confirmation or retry message and to update your order records.
      </p>
    </div>
  </Card>
</Cards>

***

## Supported Payment Methods

PayU Hosted Checkout supports multiple payment methods commonly used in India:

- Credit Cards
- Debit Cards
- UPI
- NetBanking
- Wallets

This allows you to offer a wide range of payment options without additional integrations.

## What Happens After Payment

Once the payment is completed:

- PayU determines whether the transaction is successful or failed
- The customer is redirected back to your website (success or failure page)
- A payment response is sent with transaction details

<Callout icon="⚠️" theme="warn">
  **Important: Backend Verification**

  Even after redirection:

  - You should always verify the transaction on your backend by calling PayU's verification API or processing the webhook notification PayU sends to your server
  - This ensures the payment status is authentic and prevents tampering — a customer could theoretically modify the redirect URL in their browser, but they can't fake the server-to-server verification call that only your backend can make
</Callout>

<br />

## Next Steps

Now that you understand how PayU Hosted Checkout works:

- **Get started quickly:** Go to the [Quick Start Guide](https://docs.payu.in/docs/quick-start) to answer a few questions and see your recommended integration path — including guidance on whether you'll set this up yourself, hand it to a developer, or build with AI assistance.

- **See the full technical guide:** When you or your developer are ready to build, refer to [Web Integration - PayU Hosted](https://docs.payu.in/docs/prebuilt-checkout-page-integration) for complete step-by-step instructions on credentials, API parameters, hash generation, code samples, testing, and going live. That guide contains all the technical detail and code needed to integrate PayU Hosted Checkout on your website.
