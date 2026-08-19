---
title: PayU Hosted Checkout V2
excerpt: >-
  Understand PayU Hosted Checkout for payment gateway integration. Learn payment
  flow, key concepts, and how to handle online payments securely.
deprecated: false
hidden: true
metadata:
  robots: index
---
This page helps you understand how **PayU Hosted Checkout** works before you begin integration.

<Callout icon="🟡" theme="info">
  ### Som&#x65;**&#x20;Technical Setup Required**

  You can follow the guided steps to set up Hosted Checkout. If you have a developer or technical team, you can share the integration guide with them.
</Callout>

<Callout icon="far fa-face-thinking" theme="success">
  ### **Not Sure Hosted Checkout is Fight for You?**

  Tell us what you are trying to achieve and how you plan to set it up. We will help you find the right PayU solution.

  \[Find the right integration →]
</Callout>

***

## What is PayU Hosted Checkout?

PayU Hosted Checkout is a payment integration method where:<br />

- You redirect customers from your website to a **PayU-hosted payment page**
- PayU handles the entire payment experience, including security and processing
- After the payment is completed, customers are redirected back to your website

This is a simple way to accept online payments without building and hosting your own payment page.

***

## Is this right for you?

<Columns layout="fixed">
  <Column>
    **Best For:** Businesses that have a website or app and want PayU to host the payment page while they retain control of the surrounding checkout experience.
  </Column>
</Columns>

<Columns layout="fixed">
  <Column>
    **Use Hosted Checkout when:&#x20;**&#x79;ou want a straightforward, secure payment page and do not need it to match your website's design exactly. It gets you live quickly with some development effort.
  </Column>
</Columns>

<Columns layout="fixed">
  <Column>
    **Consider alternatives if:&#x20;**&#x79;ou need complete control over how the payment page looks and feels — where every element matches your site's brand precisely — see [Merchant Hosted Checkout](https://docs.payu.in/docs/custom-checkout-merchant-hosted) instead. That approach requires more development work but gives you exact design control.
  </Column>
</Columns>

<Callout icon="🟢" theme="info">
  ### Other Easy Ways

  - If you do not want a technical setup or you do not have a website yet, PayU also offers Pay Handle — a payment link you can send customers directly, with no integration required. See [Pay Handle](https://docs.payu.in/collect-payments/introduction-no-code-payments-integration/payment-links-dashboard) →
</Callout>

***

## What You Get

<Accordion title="Key Benefits" icon="fa-rocket">
  - **Ready-to-use payment page:** PayU hosts the checkout experience, so you do not need to build your own payment page.

  - **Multiple payment methods**: Accept cards, UPI, NetBanking and wallets through one integration.

  - **Secure payment handling**: PayU handles sensitive payment information on the hosted payment page.

  - **Customization options**: Add your branding and configure supported payment options from the PayU Dashboard.

  - **Faster implementation:** Start with a ready-made checkout instead of building a payment experience from scratch.
</Accordion>

***

## How it works

Below diagram depicts the customer experience during a payment using PayU Hosted Checkout:


<Image src="https://files.readme.io/bc1c758a83c0c601d161a5621e1fe47a6d4c757e847a893b33b05419972e693a-b7b3bc19c28693be346591ec8a2c29ee07fcf47cb088bc6c9a6c34950c2af0dc-payu_hosted_checkout-workflow.png" align="center" />


The following is the customer journey using cards as a payment method:

1. Customer clicks **Pay Now**.
2. Your website starts a payment with PayU.
3. Customer is redirected to PayU's payment page.
4. Customer selects a payment method and completes payment.
5. PayU processes the payment.
6. Customer returns to your website with the payment result.

<Columns layout="fixed">
  <Column>
    **For Developers**

    The integration sends a payment request to PayU and receives a payment response. See the \[technical integration guide] for request parameters, hash generation and response handling.
  </Column>
</Columns>

***

## What You Will Need (Prerequisites)

You need:

- A website or application where you want to accept payments
- A PayU account
- Access to your website's technical setup, either yourself or through a developer
- A way to test the integration before going live

***

## Supported Payment Methods

PayU Hosted Checkout supports multiple payment methods:

- Credit Cards
- Debit Cards
- UPI
- NetBanking
- Wallets

This allows you to offer a wide range of payment options without additional integrations.

***

## What Happens After a Payment

Once the payment is completed:

- PayU determines whether the transaction is successful or failed
- The customer is redirected back to your website (success or failure page)
- A payment response is sent with transaction details

<Callout icon="⚠️" theme="warn">
  ### **Important:**

  Don't treat the browser redirect alone as confirmation that a payment succeeded. Your integration should verify the payment status using PayU's server-side verification mechanism.
</Callout>

<Columns layout="fixed">
  <Column>
    **For Developers:**

    Learn how to verify payment status and handle webhooks in the technical integration guide.
  </Column>
</Columns>

***

## Ready to integrate?

**Start with Quick Start**

Follow the guided steps to set up and test your first payment.

**Need technical implementation details?**

If you are a developer or working with one, use the complete integration guide.