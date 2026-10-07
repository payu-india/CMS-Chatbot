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

PayU Hosted Checkout is a payment integration method that lets you accept<br />online payments without building and hosting your own payment page.<br />

With the PayU Hosted Checkout:

- Customers are redirected from your website or application to a secured <br />PayU-hosted payment page.
- PayU handles the payment experience on the hosted page.
- Customers are redirected back to your website after the payment.

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
                        data-tooltip="Click to see steps to create your first payment link.">
                    Create your Test PayU Hosted Checkout →
                </button>
`}</HTMLBlock>

***

## Is PayU Hosted Checkout Right for Me?

PayU Hosted Checkout is a good choice if you:

- **Have a website or application** where customers need to make payments.
- **Want PayU to host** the payment page.
- **Want a ready-made checkout experience** instead of building your own.
- **Can handle some technical setup** or have a developer or technical team<br />to help.<br />

Consider another PayU solution if:

- **You don't have a website or don't want technical setup&#x20;**→ [Payment Links](...).
- **You need complete control over the payment page&#x20;**→ [Merchant Hosted Checkout](...).

<Callout icon="far fa-face-thinking" theme="warn">
  ### **Not Sure Which PayU Solution is Right For You?**

  Tell us what you want to achieve and how you plan to accept payments. We will recommend the best PayU solution that fits your needs.<br />

  <Anchor target="_blank" href="https://docs.payu.in/docs/start-here">Find the Right Product for You</Anchor> →
</Callout>

## How does PayU Hosted Checkout work?

The payment flow is:

1. The customer initiates a payment on your website or application.
2. Your integration sends the payment request to PayU.
3. The customer is redirected to the PayU-hosted payment page.
4. The customer selects a payment method and completes the payment.
5. PayU processes the payment.
6. The customer is returned to your website with the payment result.

\[Workflow diagram]

For the detailed integration flow, see
[How It Works](...).

## What do you need to get started?

You need:

- A website or application where you want to accept payments.
- A PayU account.
- Access to your website's technical setup, either yourself or through
  a developer.
- A way to test the integration before going live.

For the complete prerequisites and setup path, see
[Quick Start](...).

## What can you do with PayU Hosted Checkout?

With Hosted Checkout, you can:

- Accept payments through supported payment methods.
- Use a ready-made payment page hosted by PayU.
- Configure supported payment options.
- Customize supported branding options.
- Handle payment results and verify transactions.

## Supported Payment Methods

PayU Hosted Checkout supports:

- Credit Cards
- Debit Cards
- UPI
- NetBanking
- Wallets

## What happens after a payment?

After the customer completes a payment:

- PayU determines the transaction result.
- The customer is redirected back to your website.
- Your integration receives the payment result.

Do not rely only on the browser redirect to confirm a successful payment.
Verify the transaction using the appropriate server-side verification
mechanism.

## Next Steps

- **Quick Start:** Set up and test your first payment.
- **Build Integration:** Implement PayU Hosted Checkout.
- **Test Integration:** Verify your integration.
- **Go-live Checklist:** Prepare your integration for production.
