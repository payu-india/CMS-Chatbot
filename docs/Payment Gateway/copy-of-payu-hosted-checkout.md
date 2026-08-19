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
## What is PayU Hosted Checkout?

PayU Hosted Checkout is a payment integration method where:

- You redirect customers from your website to a **PayU-hosted payment page**
- PayU handles the entire payment experience, including security and processing
- After the payment is completed, customers are redirected back to your website

This is the **simplest and fastest way** to start accepting payments from web without building or managing your own payment UI.

***

## When should you use this?

PayU Hosted Checkout is best when you want a straightforward, secure payment page and don't need it to match your website's design exactly. Most merchants start here because it gets you live quickly with minimal development effort.

If you need complete control over how the payment page looks and feels — where every element matches your site's brand precisely — see [Merchant Hosted Checkout](https://docs.payu.in/docs/custom-checkout-merchant-hosted) instead. That approach requires more development work but gives you exact design control.

***

## Why Use PayU Hosted Checkout

PayU Hosted Checkout helps you accept online payments quickly without building or managing a payment interface.

<Accordion title="Benefits" icon="fa-rocket">
  - **Faster Go-Live**: Integrate and start accepting payments with minimal development effort — often in hours, not days.
  - **Built-in Security and Compliance:** When a customer enters their card details on the PayU-hosted page, that sensitive payment data is handled entirely by PayU, reducing your compliance burden. PCI-DSS — the security standard that governs how card data must be stored, transmitted, and processed — is normally your responsibility to maintain; PayU Hosted Checkout takes that on for you, so you avoid the complexity and cost of certification.
  - **Multiple Payment Methods:** Accept payments via cards, UPI, netbanking, and wallets through a single integration, without building separate flows for each payment type.
  - **Easy Payment Method Enablement:** When you want to enable or disable a payment option (like adding a new wallet or bank), you can do it from your PayU Dashboard without writing any code or redeploying your website — it's a configuration change, not a development task.
  - **Customizable Checkout Experience:** While PayU hosts the payment page, you can still align it with your brand using your logo, color scheme, and language preferences (several Indian languages are supported) — so the experience doesn't feel entirely disconnected from your site.
  - **Improved Conversion Experience:** Leverage PayU's optimized checkout flows, which include features like saved payment preferences for returning customers and intelligent payment method recommendations that help more customers complete their purchases.
  - **Reduced Engineering Overhead:** No need to build or maintain payment UI, form validation, or direct integrations with banks and payment providers — PayU handles all of that infrastructure for you.
</Accordion>

***

## Key Concepts

Understanding the following basic concepts will help you navigate the integration more easily:

<Cards columns="3">
  <Card>
    <div style={{ color: "#000", padding: "8px" }}>
      <i className="fa fa-exchange-alt" style={{ color: "#00b386", fontSize: "20px", marginBottom: "10px" }}></i>

      <h4 style={{ margin: "0 0 6px 0", fontWeight: "600" }}>Transaction</h4>

      <p style={{ margin: 0 }}>

        When a customer clicks "Pay" on your website and attempts to complete a purchase, that single payment attempt is called a transaction. Each transaction is tracked with a unique identifier (transaction ID) so you can look it up later in your PayU Dashboard or retrieve its details via API.
      </p>
    </div>
  </Card>

  <Card>
    <div style={{ color: "#000", padding: "8px" }}>
      <i className="fa fa-paper-plane" style={{ color: "#00b386", fontSize: "20px", marginBottom: "10px" }}></i>

      <h4 style={{ margin: "0 0 6px 0", fontWeight: "600" }}>Payment Request</h4>

      <p style={{ margin: 0 }}>

        When a customer clicks "Pay," your website or server sends PayU the transaction details — the order amount, customer information, and what's being purchased. This package of data, sent as parameters in a redirect or API call, is the Payment Request. It's how PayU knows what payment to collect and for whom.
      </p>
    </div>
  </Card>

  <Card>
    <div style={{ color: "#000", padding: "8px" }}>
      <i className="fa fa-reply" style={{ color: "#00b386", fontSize: "20px", marginBottom: "10px" }}></i>

      <h4 style={{ margin: "0 0 6px 0", fontWeight: "600" }}>Payment Response</h4>

      <p style={{ margin: 0 }}>

        After the customer completes (or cancels) the payment on PayU's page, PayU sends back the result — whether the transaction succeeded, failed, or is still pending, along with details like the transaction ID and payment method used. This result, returned to your website and server, is the Payment Response. Your site uses it to show the customer a confirmation or retry message and to update your order records.
      </p>
    </div>
  </Card>

  <Card>
    <div style={{ color: "#000", padding: "8px" }}>
      <i className="fa fa-random" style={{ color: "#00b386", fontSize: "20px", marginBottom: "10px" }}></i>

      <h4 style={{ margin: "0 0 6px 0", fontWeight: "600" }}>Redirect Flow</h4>

      <p style={{ margin: 0 }}>

        The sequence where your customer is sent to PayU's payment page to enter their details, then returned to your site after payment is complete — that back-and-forth journey is the Redirect Flow. It's what makes Hosted Checkout "hosted": the payment page lives on PayU's servers, not yours, and the customer visibly moves between the two.
      </p>
    </div>
  </Card>

  <Card>
    <div style={{ color: "#000", padding: "8px" }}>
      <i className="fa fa-server" style={{ color: "#00b386", fontSize: "20px", marginBottom: "10px" }}></i>

      <h4 style={{ margin: "0 0 6px 0", fontWeight: "600" }}>API Flow</h4>

      <p style={{ margin: 0 }}>

        While your customer sees the redirect and payment page, behind the scenes your server and PayU's server exchange data directly — verifying the transaction status, checking payment details, and confirming the result. This server-to-server communication, which happens in the background to keep your records accurate and secure, is the API Flow.
      </p>
    </div>
  </Card>
</Cards>

***

## How Payment Flow Works

The payment journey in Hosted Checkout looks like this:


<Image src="https://files.readme.io/932f800-payuhosted_wf.png" alt="PayU Hosted Checkout Workflow" align="center" border={true} />


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

Below diagram depicts the customer experience during a payment using PayU Hosted Checkout:


<Image src="https://files.readme.io/bc1c758a83c0c601d161a5621e1fe47a6d4c757e847a893b33b05419972e693a-b7b3bc19c28693be346591ec8a2c29ee07fcf47cb088bc6c9a6c34950c2af0dc-payu_hosted_checkout-workflow.png" align="center" />


The following is the customer journey using cards as a payment method:

<Cards columns="3">
  <Card>
    <div style={{ color: "#000", padding: "8px" }}>
      <i className="fa fa-mouse-pointer" style={{ color: "#00b386", fontSize: "20px", marginBottom: "10px" }}></i>

      <h4 style={{ margin: "0 0 6px 0", fontWeight: "600" }}>Initiate Payment</h4>

      <p style={{ margin: 0 }}>

        Customer clicks <b>Pay Now</b> on your website or app.
      </p>
    </div>
  </Card>

  <Card>
    <div style={{ color: "#000", padding: "8px" }}>
      <i className="fa fa-external-link-alt" style={{ color: "#00b386", fontSize: "20px", marginBottom: "10px" }}></i>

      <h4 style={{ margin: "0 0 6px 0", fontWeight: "600" }}>Redirect to PayU</h4>

      <p style={{ margin: 0 }}>

        Customer is redirected to the PayU Hosted Checkout page.
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

        Customer is redirected back to your website with success or failure status.
      </p>
    </div>
  </Card>
</Cards>

***

## Capabilities of PayU Hosted Checkout

<Accordion title="Features" icon="fa-cogs">
  - **Prebuilt Payment Page:** A ready-made checkout page hosted by PayU collects payment details securely, eliminating the need for you to build your own payment form — reducing both development time and security risk.
  - **Redirect-Based Integration:** Simple integration using a redirect flow from your website to PayU — typically requires only server-side code to build the redirect with transaction parameters and a secure hash, then handle the response when the customer returns.
  - **Secure Payment Handling:** Handles authentication flows such as OTP verification and bank redirects securely, so your customers' payment credentials are protected throughout the transaction without you having to manage the authentication infrastructure.
  - **Quick Integration Setup:** Integration kits and APIs enable faster implementation with minimal setup — most merchants can complete a test payment within hours of starting the integration.
  - **Mobile-Optimized Experience:** The PayU Checkout page automatically adapts to mobile screens, supports responsive checkout flows, and handles mobile payment intents (like UPI deep-linking on mobile web) without extra configuration on your side.
  - **Smart Payment Experience:** Supports features like payment method recommendations (suggesting the most relevant payment option for each customer based on their history and preferences) and saved payment preferences for returning customers, helping improve conversion rates.
</Accordion>

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
