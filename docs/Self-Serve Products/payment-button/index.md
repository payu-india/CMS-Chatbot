---
title: Payment Button
excerpt: >-
  Add a PayU-powered payment button to any website or blog. Get a ready-to-use
  button code from the Dashboard and paste it onto your page.
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

##

## How Does Payment Button Simplify My Business?

<Accordion title="Go from zero to accepting payments with a copy-paste">
  Create a button in the PayU Dashboard, copy one line of code, and paste it anywhere on your website. No coding knowledge required, no developer to hire. If you can paste text into a website editor, you can add a payment button.
</Accordion>

<Accordion title="Works on any website, blog, or page builder">
  WordPress, Wix, Squarespace, Webflow, a hand-coded HTML page, or any site that lets you add content. Payment Buttons work anywhere. You add the button code to a page the same way you'd add an image or a video embed.
</Accordion>

<Accordion title="Customise the button to match your brand">
  Choose the button label ("Buy Now", "Donate", "Enrol", or any text you prefer), the colour, the size, and the fixed amount, all from the Dashboard with no code changes. Update the settings any time; the button on your site updates automatically.
</Accordion>

<Accordion title="Let customers enter their own amount">
  Enable **Collect Amount** mode and the payment page prompts customers to type in the amount they want to pay. Ideal for donations, tips, or open-ended contributions where you don't want to set a fixed price.
</Accordion>

<Accordion title="Supports every Indian payment method">
  UPI (all apps), credit and debit cards, net banking (50+ banks), wallets, EMI, and BNPL. The payment page automatically presents the methods enabled on your PayU account. No extra configuration needed for each method.
</Accordion>

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

## Is a Payment Button Right for Me?

| I want to…                                                  |                                            Works?                                            |
| ----------------------------------------------------------- | :------------------------------------------------------------------------------------------: |
| Accept payments on my website without writing code          |                                               ✅                                              |
| Add a "Buy Now", "Pay Now", or "Donate" button to a webpage |                                               ✅                                              |
| Let customers enter their own donation or payment amount    |                                    ✅ (Collect Amount mode)                                   |
| Sell a single product or service directly from my page      |                                               ✅                                              |
| Accept payments without a website                           |           ⚠️ Use [Payment Links](https://docs.payu.in/docs/payment-links-overview)           |
| Share a payment request over WhatsApp or SMS                |           ⚠️ Use [Payment Links](https://docs.payu.in/docs/payment-links-overview)           |
| Set up recurring auto-debit or subscriptions                |           ⚠️ Use [Recurring Payments](https://docs.payu.in/docs/recurring-payments)          |
| Build a full online store with a shopping cart              |            ⚠️ Use [eCommerce Plugins](https://docs.payu.in/docs/ecommerce-plugins)           |
| Full server-side control over the checkout flow             | ⚠️ Use [Merchant Hosted Checkout](https://docs.payu.in/docs/custom-checkout-merchant-hosted) |

<Callout icon="far fa-face-thinking" theme="warn">
  ### **Not Sure Which PayU Solution is Right For You?**

  Tell us what you want to achieve and how you plan to accept payments. We will recommend the best PayU solution that fits your needs.

  <Anchor target="_blank" href="https://docs.payu.in/docs/start-here">Find the right solution</Anchor> →
</Callout>

***

## Common Use Cases

<Cards>
  <Card title="Event Organisers">
    Embed a **Register Now** button on your event page. Set the exact ticket price, cap registrations with a max-transaction limit if seats are limited, and disable the button the moment they sell out — all from your Dashboard, without touching the page code again.
  </Card>

  <Card title="NGOs and Fundraisers">
    Turn on **Collect Amount** mode and let supporters decide how much they want to give — ₹100 or ₹10,000 goes through the same button. Every donation appears in your Dashboard in real time, so your finance team can track inflows without waiting for a bank statement.
  </Card>

  <Card title="Small Businesses">
    One landing page. One product. One **Buy Now** button. Change the price from the Dashboard whenever you need to, no page edit, no developer call. No cart, no plugin, no monthly platform fee on top of your payment costs.
  </Card>

  <Card title="Educational Institutes">
    Create separate payment buttons for tuition, hostel, exam registration, and extracurricular fees, each button tracks its own payments independently in the Dashboard. Students pay from the fee page; you see every entry categorised by button name without manual reconciliation.
  </Card>

  <Card title="Freelancers and Individuals">
    Add a **Pay for Session** or **Book Now** button to your portfolio page, personal website, or bio link. Clients click, choose their payment method, and pay in one step, no bank transfer details to share, no invoice follow-up, no missed payments because the link expired.
  </Card>
</Cards>

## What Will I Need?

You don't need a developer or any coding experience to get started.<br />

All You need is:<br />

- <Columns layout="fixed">
    <Column>
      **A PayU merchant account:** <Anchor target="_blank" href="doc:set-up-your-account">Sign up here</Anchor> if you do not have an account.
    </Column>
  </Columns>
- <Columns layout="fixed">
    <Column>
      **A website, blog, or page builder:** Any site where you can add content to your pages. For example WordPress, Wix, Squarespace, or any website with a page editor.
    </Column>
  </Columns>
- <Columns layout="fixed">
    <Column>
      **Access to the PayU Dashboard:** Where you will create and manage your payment buttons.
    </Column>
  </Columns>

***

## How Do I Add a Payment Button?

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

## Is a Payment Button Secure?

Yes. When a customer clicks your button, PayU's PCI-DSS compliant hosted payment page opens, their card and UPI details are entered directly on PayU's page and never pass through your website. You do not need to configure anything for this.

Make sure **the page where you embed the button should be HTTPS.** If your page loads over HTTP, some browsers will show a mixed-content warning when the button tries to open PayU's secure checkout. Most modern website builders (WordPress, Wix, Squarespace) use HTTPS by default. If you are not sure, check your site settings.

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