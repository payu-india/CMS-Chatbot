---
title: Merchant Hosted Checkout
excerpt: >-
  Collect payment details on your own checkout and post them to PayU. You own
  the payment form. PayU processes the payment and returns the result.
deprecated: false
hidden: true
metadata:
  title: Merchant Hosted Checkout — Overview
  description: >-
    PayU Merchant Hosted Checkout: build your own payment form, post card, UPI,
    net banking, wallet, PayPal, and Pluxee payments to _payment.
  keywords:
    - payu merchant hosted checkout
    - payu custom checkout integration
    - payu _payment merchant hosted
    - payu seamless checkout cards upi net banking
  robots: index
next:
  description: Explore related information and resources.
---
<Banner
  isInline={true}
  message="Integration effort: Developer required"
  color="#E9A23B"
  textColor="#ffffff"
  fontSize="14px"
  fontWeight="bold"
 />

## How Does Merchant Hosted Checkout Simplify My Business?

<Accordion title="Keep the payment form on your website">
  You design the checkout. The customer enters card, UPI, net banking, wallet, PayPal, or Pluxee details on your page. Your page form-posts those details to PayU. PayU does not show its own payment page for the customer to pick a method.
</Accordion>

<Accordion title="Accept the payment methods you enable">
  One `_payment` endpoint accepts the methods documented for this integration: cards, net banking, wallets, UPI Collect, PayPal, and Pluxee. You choose the method with `pg` and `bankcode`.<br />

  The method must be enabled on your PayU merchant account. PayPal is activated from the PayU Dashboard.
</Accordion>

<Accordion title="You are in PCI-DSS scope when you collect cards">
  Card numbers and CVV are entered on your website. The source says that if you store, process, or transmit cardholder data you must complete PCI-DSS SAQ A-EP. If you use only UPI and wallets, the site must still be secure.
</Accordion>

<Accordion title="The integration is a form post, a hash, and a verify call">
  Generate a SHA-512 hash on your server, post the form from the browser to `_payment`, verify the reverse hash on `surl` or `furl`, then confirm the payment with Verify Payment.
</Accordion>

<Accordion title="You own the customer journey up to the bank">
  The customer stays on your checkout until PayU sends them to the bank ACS, net banking login, wallet, or UPI flow. After that step, PayU redirects the customer back to your site.
</Accordion>

<Callout icon="📘" theme="info">
  ### **Tips:**

  Post the payment with an HTML form to the <Anchor target="_blank" href="https://docs.payu.in/reference/_payment_merchant_hosted">Collect Payment API — Merchant Hosted Checkout</Anchor>.
</Callout>

***

## Is Merchant Hosted Checkout Right for Me?

| I want to… | Works? |
| --- | :---: |
| Design every field of the payment form on my website | ✅ |
| Choose the method in the request with `pg` and `bankcode` | ✅ |
| Collect cards, UPI, net banking, and wallets on my page | ✅ |
| Accept card data on my site and take on PCI-DSS | ✅ |
| Post the payment with an HTML form | ✅ |
| Let PayU host and secure the payment page | ⚠️ Use [PayU Hosted Checkout](https://docs.payu.in/docs/payu-hosted-checkout-1) instead |
| Accept payments without a website or any technical setup | ⚠️ Use [Payment Links](https://docs.payu.in/docs/payment-links-dashboard) instead |
| Accept payments natively inside a mobile app | ⚠️ Use [PayU Mobile SDK](https://docs.payu.in/docs/mobile-sdk-integration) instead |
| Set up recurring auto-debit payments | ⚠️ Use [Recurring Payments](https://docs.payu.in/docs/introduction-recurring-payments-integration) instead |

<Callout icon="far fa-face-thinking" theme="warn">
  ### **Not Sure Which PayU Solution is Right For You?**

  Tell us what you want to achieve and how you plan to accept payments. We will recommend the best PayU solution that fits your needs.<br />

  <Anchor target="_blank" href="https://docs.payu.in/docs/start-here">Find the Right Product for You</Anchor> →
</Callout>

***

## Common Use Cases

<Cards columns="3">
  <Card title="Branded web checkout" icon="fa-bag-shopping" href="./integration-guide/build-integration">
    Collect the payment on your store and post the method the customer chose.
  </Card>
  <Card title="Saved-card repeat payment" icon="fa-credit-card" href="./integration-guide/build-integration/cards">
    Post a network token with `store_card_token` instead of the full card number.
  </Card>
  <Card title="UPI Collect" icon="fa-mobile-screen" href="./integration-guide/build-integration/upi-collect">
    Validate the VPA, then post `pg=UPI`, `bankcode=UPI`, and `vpa`.
  </Card>
  <Card title="International PayPal" icon="fa-globe" href="./integration-guide/build-integration/paypal">
    Post `pg=PAYPAL` and `bankcode=PAYPAL` after PayPal is activated.
  </Card>
  <Card title="Pluxee meal cards" icon="fa-utensils" href="./integration-guide/build-integration/pluxee">
    Check the balance, then post `pg=MC` and `bankcode=SODEXO`.
  </Card>
  <Card title="Net banking" icon="fa-building-columns" href="./integration-guide/build-integration/net-banking">
    Post the bank code for the bank the customer selected.
  </Card>
</Cards>

***

## What All I Need to Get Started?

Before you integrate, make sure you have:<br />

- [x] **A PayU merchant account:** a test account while you integrate, then a production account.
- [x] **API key and salt:** from the PayU Dashboard. The salt is used to generate the hash.
- [x] **A website on HTTPS:** where you collect the payment details.
- [x] **A backend that generates SHA-512:** the salt stays on the server.
- [x] **surl and furl:** URLs PayU can redirect the customer to.
- [x] **PCI-DSS SAQ A-EP:** if you store, process, or transmit cardholder data.

***

## Supported Payment Methods

These are the payment methods with integration steps in this guide:<br />

- Credit Cards and Debit Cards (`pg=CC`)
- Net Banking (`pg=NB` in the parameter table; test samples use `pg=TESTPG`)
- Wallets (`pg=CASH`; Advantage Club uses `pg=RD`)
- UPI Collect (`pg=UPI`, `bankcode=UPI`)
- PayPal (`pg=PAYPAL`, `bankcode=PAYPAL`)
- Pluxee (`pg=MC`, `bankcode=SODEXO`)

EMI, BNPL, EFTNET, and Net Banking TPV are linked from the legacy pages to other guides. They are not rewritten here.

***

## Is My Integration Secure?

You collect the payment details, including card data when the customer pays by card. Your server must not store the CVV or the full card number.<br />

Your integration has two security responsibilities:

<Tabs>
  <Tab title="Protect the Payment Request">
    Before the browser posts the form, your server generates a SHA-512 hash of the transaction parameters using your merchant salt. PayU uses this hash to verify that the request came from you and was not modified. The salt must stay on your server.
  </Tab>
  <Tab title="Verify the Payment Response">
    When PayU redirects the customer back, your server must verify the reverse hash and then call Verify Payment. Do not treat the browser redirect alone as success.
  </Tab>
</Tabs>

***

## How Does My Customer Pay?

The legacy overview includes this customer-journey diagram:


<Image src="https://files.readme.io/f3853b72839386d63dda5c0929a3d8f82812c794036a97a5e50f3940a6bea27c-merchant_hosted_customer_journey.png" align="center" alt="Merchant Hosted Checkout customer journey" border={true} />


The following is the customer journey using cards, as described in the source:<br />

1. The customer finishes checkout on your website and starts the payment.
2. The customer enters the card details, including CVV, on your page.
3. The browser posts the payment. The customer passes through a PayU environment that shows the transaction ID.
4. The customer completes the bank ACS page with the OTP the bank sends.
5. The customer returns to your website. You show success or failure from the PayU status.<br />

For request parameters, hash generation, and response handling, see [Build the Integration](./integration-guide/build-integration).

***

## What Happens After a Payment

After the customer completes a payment:<br />

- PayU determines the transaction result.
- The customer is redirected back to your `surl` or `furl`.
- A payment response is posted with transaction details, including `mihpayid`, `status`, `txnid`, `amount`, `hash`, `error`, and `error_Message`.

<Callout icon="⚠️" theme="warn">
  ### **Important:**

  Don't treat the browser redirect alone as confirmation that a payment succeeded. Confirm the transaction on the server with Verify Payment. The production checklist says to use webhooks if the callback fails.
</Callout>

Learn how to verify payment status in the [Integration Guide](./integration-guide).

***

## What If My Customer Wants the Money Back?

<Tabs>
  <Tab title="Refunds">
    Refund from the PayU Dashboard or with `command=cancel_refund_transaction`. The PayPal page says the PayPal account needs sufficient funds before a refund.
  </Tab>
  <Tab title="Settlements">
    PayPal settlements are processed in INR. Other settlement screens are not described in the Merchant Hosted pages.
  </Tab>
  <Tab title="Disputes and Chargebacks">
    The parameter tables say `email`, `phone`, and `address1` help with fraud detection and chargebacks. A chargeback walkthrough is not in this folder.
  </Tab>
</Tabs>

***

## Use AI to Help You

Ask your AI coding assistant using a prompt to get targeted help with your Merchant Hosted Checkout integration. Use these docs as the source. Do not paste your salt into a chat.

<Callout icon="📘" theme="info">
  Example prompts: "What is the SHA-512 request hash field order for PayU Merchant Hosted Checkout?" "Which pg and bankcode does UPI Collect use?" "What does error E1903 mean on a Merchant Hosted cards callback?"
</Callout>

***

## Next Steps

<Cards>
  <Card title="Quick Start" href="./quick-start">
    Set up and test your first net banking payment.
  </Card>
  <Card title="How Merchant Hosted Checkout Works" href="./how-it-works">
    Understand the form-post flow and key concepts.
  </Card>
  <Card title="Integration Guide" href="./integration-guide">
    Build, test, and prepare your integration for production.
  </Card>
</Cards>
