---
title: PayU Hosted Checkout
excerpt: >-
  Accept online payments by redirecting customers to PayU's secure, prebuilt
  payment page with PayU handling the payment experience for you.
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

##

## How Does PayU Hosted Checkout Simplify My Business?

<Accordion title="Redirect to PayU's secure checkout without the need to build a payment UI">
  When a customer proceeds to pay, you send them to PayU's hosted payment page. PayU handles the entire payment experience such as page rendering, mobile optimisation, 3DS authentication, UPI flows, and net banking redirects. Your application is no longer involved in the payment interaction once the customer is redirected.
</Accordion>

<Accordion title="Accept all major Indian payment methods ">
  A single integration with PayU Hosted Checkout enables cards (credit and debit), UPI, netbanking, wallets, EMI, and BNPL payment modes. PayU's checkout page automatically presents the payment methods enabled on your account.<br />

  To add or remove a payment method such as enabling international payments or BNPL, you make a configuration change in your PayU Dashboard.
</Accordion>

<Accordion title="PCI-DSS scope reduced to near zero">
  Card numbers and other sensitive payment data are entered directly on PayU's infrastructure, not on your website or your server. The most demanding parts of PCI-DSS compliance such as handling, storing, and transmitting raw card data are PayU's responsibility.<br />

  Your integration deals with transaction parameters and response verification. Your application never receives or handles raw card data.
</Accordion>

<Accordion title="Go live quickly, stay low-effort">
  PayU Hosted Checkout can be integrated in hours, not days. The essentials are: generate a SHA-512 hash on your server, POST a form to PayU's endpoint, and verify the response when it returns. There is no payment UI to build or maintain, and no ongoing infrastructure to manage as payment methods evolve.
</Accordion>

<Accordion title="Mobile-optimised and branded out of the box">
  The PayU checkout page adapts to mobile screens automatically. UPI deep-linking for Google Pay, PhonePe, and Paytm works on mobile web without extra configuration on your side.<br />

  You can customise the checkout experience by adding your logo, setting a colour scheme, and choosing the checkout language (Hindi, Kannada, Tamil, Telugu, Gujarati, Marathi, or English) from the PayU Dashboard. See <Anchor target="_blank" href="https://docs.payu.in/docs/customise-payu-hosted-checkout">Customise PayU Hosted Checkout</Anchor>.
</Accordion>

<Callout icon="📘" theme="info">
  ### **Tips:**

  You can initiate the redirect using an HTML form POST or by calling the <Anchor target="_blank" href="https://docs.payu.in/reference/_payment_payu_hosted_checkout">Collect Payment API</Anchor> directly from your server.
</Callout>

***

## Is PayU Hosted Checkout Right for Me?

| I want to…                                                     |                                                Works?                                                |
| -------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------: |
| Accept payments on my website with minimal development effort  |                                                   ✅                                                  |
| Support cards, UPI, netbanking, and wallets in one integration |                                                   ✅                                                  |
| Let PayU host and secure the payment page                      |                                                   ✅                                                  |
| Reduce my PCI-DSS compliance scope                             |                                                   ✅                                                  |
| Integrate using an HTML form POST or a server-side API call    |                                                   ✅                                                  |
| Mobile-optimised checkout with UPI deep-linking                |                                                   ✅                                                  |
| Fully customise the payment page design to match my website    | ⚠️ Use [Merchant Hosted Checkout](https://docs.payu.in/docs/custom-checkout-merchant-hosted) instead |
| Accept payments without a website or any technical setup       |           ⚠️ Use [Payment Links](https://docs.payu.in/docs/payment-links-dashboard) instead          |
| Accept payments natively inside a mobile app                   |          ⚠️ Use [PayU Mobile SDK](https://docs.payu.in/docs/mobile-sdk-integration) instead          |
| Set up recurring auto-debit payments                           |           ⚠️ Use [Recurring Payments](https://docs.payu.in/docs/recurring-payments) instead          |

<Callout icon="far fa-face-thinking" theme="warn">
  ### **Not Sure Which PayU Solution is Right For You?**

  Tell us what you want to achieve and how you plan to accept payments. We will recommend the best PayU solution that fits your needs.<br />

  <Anchor target="_blank" href="https://docs.payu.in/docs/start-here">Find the Right Product for You</Anchor> →
</Callout>

***

## Common Use Cases

<Cards columns="3">
  <Card title="E-commerce & Online Retail" icon="fa-bag-shopping">
    Accept product and cart payments on your store. One integration covers cards, UPI, netbanking, and EMI.
  </Card>

  <Card title="EdTech & Online Courses" icon="fa-graduation-cap">
    Collect fees for courses, certifications, and learning programmes. Supports all major payment methods used by students.
  </Card>

  <Card title="SaaS & Subscription Platforms" icon="fa-layer-group">
    Bill customers at sign-up or on plan selection. For auto-debit after the initial payment, combine with [Recurring Payments](https://docs.payu.in/docs/recurring-payments).
  </Card>

  <Card title="Travel & Hospitality" icon="fa-plane">
    Accept booking and reservation payments with a full checkout experience, including EMI for high-value transactions.
  </Card>

  <Card title="Healthcare & Diagnostics" icon="fa-stethoscope">
    Collect consultation fees, lab test payments, and copays. Supports wallets and UPI for patients who prefer low-friction payment.
  </Card>

  <Card title="B2B & Enterprise" icon="fa-building">
    Handle invoice-based payments or multi-product purchases. Supports netbanking NEFT/RTGS for large transfers.
  </Card>
</Cards>

***

## What All I Need to Get Started?

Before you integrate, make sure you have:<br />

- [x] **A PayU merchant account:** <Anchor target="_blank" href="https://docs.payu.in/docs/set-up-your-account">Sign up here</Anchor> if you do not have an account.
- [x] **Access to the PayU Dashboard:** Where you will manage checkout transactions.
- [x] **A website or application**: Where you want to accept payments.
- [x] **Access to your website's technical setup**: Either yourself or through a developer to integrate PayU Hosted checkout.
- [x] **A way to test the integration** before going live.

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

## Is My Integration Secure?

PayU Hosted Checkout is designed so that the most sensitive part of a payment such as card number entry and bank authentication happens on PayU's infrastructure, not on your website. Your server never handles raw card data.<br />

Your integration has two security responsibilities:

<Tabs>
  <Tab title="Protect the Payment Request">
    Before redirecting the customer to PayU, your server generates a SHA-512 hash of the transaction parameters using your merchant salt. PayU uses this hash to verify that the request came from you and not modified in transit. The salt must stay secret on your server and should never appear in browser code, mobile apps, or anywhere a customer could inspect it.
  </Tab>

  <Tab title="Verify the Payment Response">
    When PayU redirects the customer back with the payment result, your server must verify the response using reverse hash validation and not just read the status from the redirect URL.
  </Tab>
</Tabs>

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

## What If My Customer Wants the Money Back?

It depends on:<br />

- Whether you want to return the money yourself. Use PayU refunds to initiate.
  <Cards>
    <Card title="Refunds" href="doc:introduction-refunds" icon="fad fa-arrow-rotate-left" target="_blank">
      Issue a partial or full refund to a customer directly from the Dashboard or via the Refunds API.
    </Card>
  </Cards>
- You are waiting for the amount to reach your account. PayU settlements can help you find out when the amount will be settled.
  <Cards>
    <Card title="Settlements" href="doc:split-settlments" icon="fad fa-building-columns" target="_blank">
      Understand how PayU settles funds to your bank account, view settlement reports, and split funds across multiple beneficiaries.
    </Card>
  </Cards>
- Your customer has raised a complaint with their bank.
  <Cards>
    <Card title="Disputes and Chargebacks" href="doc:chargeback" icon="fad fa-shield-halved" target="_blank">
      Respond to customer disputes and chargebacks raised through their bank — track status and submit evidence from the Dashboard
    </Card>
  </Cards>

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
  <Card title="Quick Start" href="https://docs.payu.in/docs/payu-hosted-checkout-quick-start" target="_blank">
    Set up and test your first payment.
  </Card>

  <Card title="How PayU Hosted Checkout Works" href="https://docs.payu.in/docs/payu-hosted-checkout-workflow" target="_blank">
    Understand the Hosted Checkout flow and key concepts.
  </Card>

  <Card title="Integrate PayU Hosted Checkout" href="https://docs.payu.in/docs/integrate-payu-hosted-checkout" target="_blank">
    Build, test, and prepare your integration for production.
  </Card>
</Cards>