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

A Payment Button is a "Buy Now" or "Pay Now" button you add to your website or blog. When a visitor clicks it, PayU's payment page opens, they pay, and they're brought back to your site — you don't need to write any code or build anything.<br />

You can use Payment Buttons to:

- Add a **Buy Now**, **Pay Now**, or **Donate** button to any webpage or blog post
- Accept payments from website visitors without setting up a full online store
- Collect donations where visitors type in the amount they want to pay
- Choose the button text, colour, size, and amount from the Dashboard

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

## Is Payment Button Right for Me?

A Payment Button is a good choice if: <br />

* **You have a website or blog** and want to start accepting payments quickly.
* **You want customers to pay directly from your page** — no payment link to share separately.
* **You sell a single product, service, or collect donations** from your website.
* **You use a website builder** like WordPress, Wix, or Squarespace and can add content to your pages.<br />

Consider another PayU solution if:<br />

* You do not have a website and want to send a payment request using a link → <Anchor target="_blank" href="https://docs.payu.in/docs/payment-links">**Payment Links**</Anchor>
* You need a full online store with a shopping cart → <Anchor target="_blank" href="https://docs.payu.in/docs/prebuilt-checkout-payu-hosted">**PayU Hosted Checkout**</Anchor>
* You want to build a custom checkout page that matches your website exactly → <Anchor target="_blank" href="doc:merchant-hosted-checkout">**Merchant Hosted Checkout**</Anchor>

<Callout icon="far fa-face-thinking" theme="warn">
  ### **Not Sure Which PayU Solution is Right For You?**

  Tell us what you want to achieve and how you plan to accept payments. We will recommend the best PayU solution that fits your needs.

  <Anchor target="_blank" href="https://docs.payu.in/docs/start-here">Find the right solution</Anchor> →
</Callout>

***

## What Will I Need?

You don't need a developer or any coding experience to get started.<br />

All You need is:<br />

<Columns layout="fixed">
  <Column>
    **A PayU merchant account:** <Anchor target="_blank" href="doc:set-up-your-account">Sign up here</Anchor> if you do not have an account.
  </Column>
</Columns>

<Columns layout="fixed">
  <Column>
    **A website, blog, or page builder:** Any site where you can add content to your pages. For example WordPress, Wix, Squarespace, or any website with a page editor.
  </Column>
</Columns>

<Columns layout="fixed">
  <Column>
    **Access to the PayU Dashboard:** Where you will create and manage your payment buttons.
  </Column>
</Columns>

***

## How do I Add a Payment Button?

Here is how it works:

<Accordion title="1. Create a Button in the Dashboard" icon="far fa-grid-2">
  1. Log in to your <Anchor target="_blank" href="https://onboarding.payu.in/app/account/signin">PayU Dashboard</Anchor> and go to **Payment Tools** → **Payment Buttons** from the menu on the left.
  2. Click **Create Payment Button** and and enter the button details.
</Accordion>

<Accordion title="2. Get Your Button Code" icon="far fa-code">
  Click **Generate Button**. PayU creates your button and gives you a short piece of text to add to your website. Click **Copy**. That is all you need.
</Accordion>

<Accordion title="3. Paste It on Your Website" icon="far fa-paste">
  Go to your website editor and paste the code where you want the button to appear. The button shows up right away. No other set up is required.
</Accordion>

<Columns layout="fixed">
  <Column>
    **Need detailed steps?** See [Add a Payment Button →](doc:add-a-payment-button)
  </Column>
</Columns>

<Columns layout="fixed">
  <Column>
    You can create multiple payment buttons and add them to different pages of your site.
  </Column>
</Columns>

***

## How does My Customer Pay?

When your customer visits your website:

<Accordion title="1. Sees the Button" icon="far fa-eye">
  The button appears on your page exactly where you added it.
</Accordion>

<Accordion title="2. Clicks the Button" icon="far fa-computer-mouse">
  PayU's payment page opens and the customer can complete their payment.
</Accordion>

<Accordion title="3. Answers Any Extra Questions You Have Added (optional)" icon="far fa-keyboard-down">
  If you have asked for extra details such as name, email, or a note, the customer fills those in.
</Accordion>

<Accordion title="4. Completes payment" icon="far fa-money-bills">
  The customer chooses the payment method, enters their payment details and confirms. PayU handles the rest securely.
</Accordion>

<Accordion title="5. Brought Back to Your Site" icon="far fa-diagram-successor">
  Once the payment is done, the customer is taken to your website or an error page if something went wrong.
</Accordion>

***

## How do I Manage My Payment Buttons?

Once your button is live:<br />

<Columns layout="fixed">
  <Column>
    **You see all payments immediately** in your PayU Dashboard under **Payment Tools → Payment Buttons**
  </Column>
</Columns>

<Columns layout="fixed">
  <Column>
    **Every payment is recorded:** You can see the amount, date, customer details, and whether the payment went through.
  </Column>
</Columns>

<Columns layout="fixed">
  <Column>
    **You can download your payment records:** <Anchor target="_blank" href="doc:customize-payment-button">Download a report</Anchor> of all payments received through your buttons.
  </Column>
</Columns>

<Columns layout="fixed">
  <Column>
    **Buttons can be turned off:** You can stop a button from accepting payments at any time — useful when a product sells out or an event ends.
  </Column>
</Columns>

***

## Next Steps

<Cards>
  <Card title="Add a Payment Button" href="doc:add-a-payment-button" icon="far fa-plus">
    **Create a Payment Button:** Simple steps to set up your button in the PayU Dashboard.
  </Card>

  <Card title="Customize Your Button" href="doc:customize-payment-button" icon="fa-sliders">
    **Change the button text, colour, amount, and what happens after a payment** to match your needs.
  </Card>

  <Card title="Payment Button FAQs" href="doc:payment-button-faqs" icon="fa-circle-question">
    Common questions about Payment Buttons — display issues, setup tips, and tracking your payments.
  </Card>
</Cards>
