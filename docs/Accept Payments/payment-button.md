---
title: Payment Button
deprecated: false
hidden: true
metadata:
  title: PayU Payment Button — Overview | Developer Docs
  description: >-
    Add a PayU payment button to your website or blog without writing code.
    Generate an embed snippet in the Dashboard, customise the label, amount, and
    colour, then paste it on your page.
  keywords:
    - payu payment button
    - embed payment button website
    - buy now button payu
    - donate now button payu
    - payu no-code payment button
    - payment button dashboard payu
    - payu payment button vs payment link
  robots: index
next:
  description: Explore related information and resources.
---
{/* NEW CONTENT */}

<Banner
  isInline={true}
  message="Integration effort: No code or website developer required"
  color="#15C614"
  textColor="#ffffff"
  fontSize="14px"
  fontWeight="bold"
/>

## What Can I Do with a Payment Button?

Payment Buttons let you accept payments directly on your website or blog without building a custom checkout.<br />

You can use Payment Buttons to:<br />

* Add a "Buy Now", "Pay Now", or "Donate" button to any webpage or blog post
* Accept payments from website visitors without a shopping cart or checkout integration
* Collect donations with a variable-amount button your visitors fill in
* Customise the button label, colour, size, and amount from the Dashboard
* Track all transactions in the PayU Dashboard

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
                    font-weight: bold;
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

                <button onclick="window.open('https://docs.payu.in/docs/add-a-payment-button', '_blank')" 
                        class="tooltip-btn" 
                        data-tooltip="Click to see steps to add your first payment button.">
                    Add your first payment button →
                </button>
`}</HTMLBlock>

***

##

Payment Buttons let you accept payments directly on your website or blog without building a custom checkout.<br />

You can use Payment Buttons to:<br />

* Add a "Buy Now", "Pay Now", or "Donate" button to any webpage or blog post
* Accept payments from website visitors without a shopping cart or checkout integration
* Collect donations with a variable-amount button your visitors fill in
* Customise the button label, colour, size, and amount from the Dashboard
* Track all transactions in the PayU Dashboard<br />


<Image src="https://files.readme.io/a494bb1de682ae83ec3d1023e1e13dfb65e02db0ef5332ca52b6e85232638c63-Screenshot_2025-06-02_at_7.09.40_PM.png" align="center" caption="Payment Buttons list in the PayU Dashboard" border={true} />


***

## Is a Payment Button Right for Me?

A Payment Button is a good choice if: <br />

* **You have a website or blog** and want to accept payments with minimal setup.
* **You want customers to pay directly from your page** — no payment link to share separately.
* **You sell a single product, service, or collect donations** from a static or simple site.
* **You use a website builder** like WordPress, Wix, or Squarespace and can paste an HTML snippet.<br />

Consider another PayU solution if:<br />

* You don't have a website and want to send a payment request → **Payment Links**
* You want to collect payment by sharing a URL over WhatsApp, SMS, or email → <Anchor target="_blank" href="doc:payment-links-overview">**Payment Links**</Anchor>
* You need a full multi-product cart experience → **PayU Hosted Checkout**
* You need developer-level control over the checkout flow → <Anchor target="_blank" href="doc:merchant-hosted-checkout">**Merchant Hosted Checkout**</Anchor>

<Callout icon="far fa-face-thinking" theme="warn">
  ### **Not Sure Which PayU Solution is Right For You?**

  Tell us what you want to achieve and how you plan to accept payments. We will recommend the best PayU solution that fits your needs.

  <Anchor target="_blank" href="doc:start-here">Find the right solution</Anchor> →
</Callout>

***

## What Will I Need?

You don't need a developer or any coding experience to get started.

You'll need:

<Columns layout="fixed">
  <Column>
    **A PayU merchant account:** <Anchor target="_blank" href="doc:set-up-your-account">Sign up here</Anchor> if you do not have an account.
  </Column>
</Columns>

<Columns layout="fixed">
  <Column>
    **A website, blog, or page builder:** Any site where you can paste an HTML snippet — WordPress, Wix, Squarespace, or a custom site with an HTML editor.
  </Column>
</Columns>

<Columns layout="fixed">
  <Column>
    **Access to the PayU Dashboard:** Where you will create, configure, and manage your payment buttons.
  </Column>
</Columns>

***

## How do I Add a Payment Button?

Here is how it works:

<Accordion title="1. Create the button in the Dashboard" icon="far fa-grid-2">
  1. Log in to your PayU Dashboard and go to **Payment Tools** → **Payment Buttons** from the left navigation.
  2. Click **Create New Button** and configure the label, amount, colour, and size.
</Accordion>

<Accordion title="2. Copy the embed snippet" icon="far fa-code">
  Click **Generate Button**. PayU produces a short HTML embed snippet. Click **Copy** to copy it to your clipboard.
</Accordion>

<Accordion title="3. Paste it on your website" icon="far fa-paste">
  Open your website editor and paste the snippet into your page's HTML. The button renders immediately — no further setup required.
</Accordion>

<Columns layout="fixed">
  <Column>
    **Need detailed steps?** See [Add a Payment Button →](doc:add-a-payment-button)
  </Column>
</Columns>

<Columns layout="fixed">
  <Column>
    You can create multiple payment buttons — one for each product, service, or event — and embed them on different pages of your site.
  </Column>
</Columns>

***

## How does My Customer Pay?

When a visitor sees your payment button on your website:

<Accordion title="1. Sees the button" icon="far fa-eye">
  The button appears on your page exactly where you placed the embed snippet.
</Accordion>

<Accordion title="2. Clicks the button" icon="far fa-computer-mouse">
  PayU's hosted checkout page opens — the customer can complete payment without leaving your site or in a new tab, depending on your configuration.
</Accordion>

<Accordion title="3. Fills in any required information (optional)" icon="far fa-keyboard-down">
  If you have set up custom checkout fields, the customer fills in details like name, email, or order ID.
</Accordion>

<Accordion title="4. Chooses a payment method" icon="far fa-credit-card">
  UPI, cards, net banking, or wallets — all payment methods enabled on your account are available.
</Accordion>

<Accordion title="5. Completes payment" icon="far fa-money-bills">
  Enters payment details and confirms. PayU processes the payment securely.
</Accordion>

<Accordion title="6. Redirected back to your site" icon="far fa-diagram-successor">
  The customer is redirected to your Success or Failure URL once the payment is processed.
</Accordion>

Your customer doesn't need a PayU account or any special app — the checkout works in any browser.

***

## How do I Manage My Payment Buttons?

Once your button is live:

<Columns layout="fixed">
  <Column>
    **You see all transactions immediately** in your PayU Dashboard under **Payment Tools → Payment Buttons**
  </Column>
</Columns>

<Columns layout="fixed">
  <Column>
    **Payment details are recorded:** You can see the amount, date, customer details, and transaction status for every payment received through a button.
  </Column>
</Columns>

<Columns layout="fixed">
  <Column>
    **You can export payment history:** <Anchor target="_blank" href="doc:customize-payment-button">Download a report</Anchor> of all payments received through your buttons.
  </Column>
</Columns>

<Columns layout="fixed">
  <Column>
    **Buttons can be deactivated:** You control whether a button remains active — useful when a product sells out or an event ends.
  </Column>
</Columns>

***

## Next Steps

<Cards>
  <Card title="Add a Payment Button" href="doc:add-a-payment-button" icon="far fa-plus">
    - **Create a Payment Button:** Step-by-step guide to creating your button from the PayU Dashboard.
    - **Embed on your website:** Copy the snippet and paste it onto any page or blog post.
  </Card>

  <Card title="Customize Your Button" href="doc:customize-payment-button" icon="fa-sliders">
    **Configure label, colour, size, redirect URLs, and custom fields** to match your brand and use case.
  </Card>

  <Card title="Payment Button FAQs" href="doc:payment-button-faqs" icon="fa-circle-question">
    Common questions about Payment Buttons — rendering, embed tips, and reconciliation.
  </Card>

  <Card title="Payment Links" href="doc:payment-links-overview" icon="fa-link">
    Need to share a payment request instead of embedding a button? Use Payment Links.
  </Card>
</Cards>
