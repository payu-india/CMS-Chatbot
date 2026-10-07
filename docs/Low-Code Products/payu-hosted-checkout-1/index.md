---
title: PayU Hosted Checkout
excerpt: >-
  Accept online payments by redirecting customers to PayU's secure, prebuilt
  payment page. Minimal development effort — PayU handles the payment experience
  for you.
deprecated: false
hidden: true
metadata:
  title: PayU Hosted Checkout — Overview
  description: 'PayU Hosted Checkout: redirect customers to a secure PayU-hosted payment '
  robots: index
next:
  description: Explore related information and resources.
---
<Banner
  isInline={true}
  message="Integration effort: Some technical setup required"
  color="#FFC107"
  textColor="#000000"
  fontSize="14px"
  fontWeight="bold"
/>

## What is PayU Hosted Checkout?

PayU Hosted Checkout is a payment integration method that lets you accept online payments without building and hosting your own payment page.<br />

With the PayU Hosted Checkout:<br />

- Customers are redirected from your website or application to a secured <br />PayU-hosted payment page.
- PayU handles the payment experience on the hosted page.
- Customers are redirected back to your website after the payment.

***

## Is PayU Hosted Checkout Right for Me?

PayU Hosted Checkout is a good choice if you:<br />

- **Have a website or application** where customers need to make payments.
- **Want PayU to host** the payment page.
- **Want a ready-made checkout experience** instead of building your own.
- **Can handle some technical setup** or have a developer or technical team<br />to help.

### **Consider another PayU solution if:**<br />

- **You don't have a website or don't want technical setup:&#x20;**&#x43;onsider [Payment Links](...).
- **You need complete control over the payment page:&#x20;**&#x43;onside&#x72;**&#x20;**[Merchant Hosted Checkout](...).

<Callout icon="far fa-face-thinking" theme="warn">
  ### **Not Sure Which PayU Solution is Right For You?**

  Tell us what you want to achieve and how you plan to accept payments. We will recommend the best PayU solution that fits your needs.<br />

  <Anchor target="_blank" href="https://docs.payu.in/docs/start-here">Find the Right Product for You</Anchor> →
</Callout>

***

## What Will I Need? (Prerequisites)

You need these to get started:<br />

<Columns layout="fixed">
  <Column>
    - **A PayU merchant account:** <Anchor target="_blank" href="https://docs.payu.in/docs/set-up-your-account">Sign up here</Anchor> if you do not have an account.
  </Column>
</Columns>

<Columns layout="fixed">
  <Column>
    - **Access to the PayU Dashboard:** Where you will manage checkout transactions.
  </Column>
</Columns>

<Columns layout="fixed">
  <Column>
    - **A website or application**: Where you want to accept payments.
  </Column>
</Columns>

<Columns layout="fixed">
  <Column>
    - **Access to your website's technical setup**: Either yourself or through a developer to integrate PayU Hosted checkout.
  </Column>
</Columns>

<Columns layout="fixed">
  <Column>
    - **A way to test the integration** before going live.
  </Column>
</Columns>

<HTMLBlock>{`
                <style>
                .tooltip-btn {
                    position: relative;
                    background-color: #4CAF50;
                    color: white;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                    font-weight: bold; /* Added this line */
                }
                .tooltip-btn:hover::after {
                    content: attr(data-tooltip);
                    position: absolute;
                    bottom: 125%;
                    left: 50%;
                    transform: translateX(-50%);
                    background-color: #333;
                    color: white;
                    padding: 5px 10px;
                    border-radius: 4px;
                    white-space: nowrap;
                    font-size: 12px;
                    z-index: 1;
                }
                </style>

                <button onclick="window.open('https://docs.payu.in/docs/create-a-payment-link#how-do-i-create-a-payment-link', '_blank')" 
                        class="tooltip-btn" 
                        data-tooltip="Follow the guided steps to set up and test your first payment.">
                    Set Up and Test Your First Payment →
                </button>
`}</HTMLBlock>

***

## Supported Payment Methods

These are the payment methods supported in PayU Hosted Checkout:<br />

- Credit Cards
- Debit Cards
- UPI
- NetBanking
- Wallets

***

## How Does My Customer Pay?

Below diagram depicts the customer experience during a payment using PayU Hosted Checkout:


<Image src="https://files.readme.io/82a36292bc83035576726e9defb6f5c88591a33556a392867b68144b2a4f8b40-image.png" align="center" caption="Customer Journey" border={true} />


The following is the customer journey using cards as a payment method:<br />

1. Customer clicks **Pay Now**.
2. Your website starts a payment with PayU.
3. Customer is redirected to PayU's payment page.
4. Customer selects a payment method and completes payment.
5. PayU processes the payment.
6. Customer returns to your website with the payment result.<br />

<Columns layout="fixed">
  <Column>
    For request parameters, hash generation, and response handling, see Build Integration.
  </Column>
</Columns>

***

## What Happens After a Payment

After the customer completes a payment:<br />

- PayU determines the transaction result.
- The customer is redirected back to your website.
- A payment response is sent with transaction details.

<Callout icon="⚠️" theme="warn">
  ### **Important:**

  Don't treat the browser redirect alone as confirmation that a payment succeeded. Your integration should verify the payment status using PayU's server-side verification mechanism.
</Callout>

Learn how to verify payment status and handle webhooks in the technical integration guide.

***

## Why Use PayU Hosted Checkout?

These are the PayU Hosted checkout integration benefits:

<Accordion title="Key Benefits" icon="fa-rocket">
  - **Ready-to-use payment page:** PayU hosts the checkout experience, so you do not need to build your own payment page.

  - **Multiple payment methods**: Accept cards, UPI, NetBanking and wallets through one integration.

  - **Secure payment handling**: PayU handles sensitive payment information on the hosted payment page.

  - **Customization options**: Add your branding and configure supported payment options from the PayU Dashboard.

  - **Faster implementation:** Start with a ready-made checkout instead of building a payment experience from scratch.
</Accordion>

***

## Next Steps

<Cards>
  <Card title="Quick Start">
    Set up and test your first payment.
  </Card>

  <Card title="How It Works">
    Understand the Hosted Checkout flow and key concepts.
  </Card>

  <Card title="Integrate PayU Hosted Checkout">
    Build, test, and prepare your integration for production.
  </Card>
</Cards>
