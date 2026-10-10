---
title: Payment Links
excerpt: >-
  Create a secure payment link in 2 minutes and share it over WhatsApp, SMS, or
  email. No code, no website, no checkout page needed.
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  title: PayU Payment Links — No-Code Payment Collection | PayU Docs
  description: >-
    Create and share PayU Payment Links to collect payments from anyone — no
    website or code needed. Share over WhatsApp, SMS, or email in minutes.
  keywords:
    - payu payment links
    - create payment link india
    - payment link whatsapp
    - no code payment collection
    - accept payment without website
    - payment link upi india
    - online payment link
    - payu dashboard payment
    - payment link sms email
    - share payment request
  robots: index
next:
  description: Explore related information and resources.
  pages:
    - slug: create-a-payment-link
      title: Create a Payment Link
      type: basic
    - slug: create-a-payment-link-with-ai-assistant
      title: AI Coding Assistants to Create a Payment Link
      type: basic
    - slug: manage-payment-links
      title: Manage Payment Links
      type: basic
    - slug: payment-button-errors-troubleshooting
      title: Errors and Troubleshooting
      type: basic
    - slug: payment-button-faqs
      title: FAQs (Frequently Asked Questions)
      type: basic
    - slug: payment-links-apis
      title: Payment Links APIs
      type: basic
    - slug: payment-links-workflow
      title: How Payment Links Works
      type: basic
---
<Banner
  isInline={true}
  message="Integration effort: No code or website required"
  color="#15C614"
  textColor="#ffffff"
  fontSize="14px"
  fontWeight="bold"
 />

## Why Use Payment Links?

<Accordion title="Create-to-Collect in Minutes" icon="fa-bolt">
  Create a <Glossary>payment links</Glossary> in a few clicks and start collecting money right away. No website, no developer, no waiting.
</Accordion>

<Accordion title="Automatically Delivers Link to Your Customers" icon="fa-paper-plane">
  Toggle on SMS and email delivery — PayU sends the link to your customer the moment it's created. No copy-pasting or manual sharing needed.
</Accordion>

<Accordion title="Set Expiry Dates" icon="fa-clock">
  Control exactly when a link stops accepting payments. Set a due date so your customers know when to act — and your links don't stay open indefinitely.
</Accordion>

<Accordion title="Collect a Deposit, Settle the Balance Later" icon="fa-money-bill-wave">
  Enable partial payments so customers can pay a portion upfront and the rest when they are ready. You set the minimum first payment — keeping the transaction moving on your terms.
</Accordion>

<Accordion title="Supports Every Indian Payment Method" icon="fa-credit-card">
  UPI (all apps), credit and debit cards, net banking (50+ banks), wallets, EMI, and BNPL. One link, every way to pay.
</Accordion>

Check this video to see how PayU Payment Links work

<Embed title="" typeOfEmbed="youtube" url="https://www.youtube.com/watch?v=rh_FQUMsaT0" href="https://www.youtube.com/watch?v=rh_FQUMsaT0" html="%3Ciframe%20class%3D%22embedly-embed%22%20src%3D%22%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Fsrc%3Dhttps%253A%252F%252Fwww.youtube.com%252Fembed%252Frh_FQUMsaT0%253Ffeature%253Doembed%26display_name%3DYouTube%26url%3Dhttps%253A%252F%252Fwww.youtube.com%252Fwatch%253Fv%253Drh_FQUMsaT0%26image%3Dhttps%253A%252F%252Fi.ytimg.com%252Fvi%252Frh_FQUMsaT0%252Fhqdefault.jpg%26type%3Dtext%252Fhtml%26schema%3Dyoutube%22%20width%3D%22854%22%20height%3D%22480%22%20scrolling%3D%22no%22%20title%3D%22YouTube%20embed%22%20frameborder%3D%220%22%20allow%3D%22autoplay%3B%20fullscreen%3B%20encrypted-media%3B%20picture-in-picture%3B%22%20allowfullscreen%3D%22true%22%3E%3C%2Fiframe%3E" providerName="YouTube" providerUrl="https://www.youtube.com/" />

<br />

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
                    Create your first payment link →
                </button>
`}</HTMLBlock>

***

## Is Payment Links Right for Me?

| I want to…                                      |                              Works?                             |
| ----------------------------------------------- | :-------------------------------------------------------------: |
| Collect payment without a website or app        |                                ✅                                |
| Share payment requests on WhatsApp or SMS       |                                ✅                                |
| Create hundreds of links at once                |                         ✅ (Bulk Upload)                         |
| Automate link creation from my own system       |                           ✅ (via API)                           |
| Embed a pay button on my website                |       ⚠️ Use [Payment Button](doc:payment-button-overview)      |
| Set up recurring auto-debit or subscriptions    |       ⚠️ Use [Recurring Payments](doc:recurring-payments)       |
| Full server-side control over the checkout flow | ⚠️ Use [Merchant Hosted Checkout](doc:merchant-hosted-checkout) |

<Callout icon="far fa-face-thinking" theme="warn">
  ### **Not Sure Which PayU Solution is Right For You?**

  Tell us what you want to achieve and how you plan to accept payments. We will recommend the best PayU solution that fits your needs.<br />

  <Anchor target="_blank" href="https://docs.payu.in/docs/start-here">Find the Right Product for You</Anchor> →
</Callout>

***

## Common Use Cases

<Cards>
  <Card title="Local Retailer" icon="fa-store">
    Collect payment for a custom or pre-ordered product before you start work or dispatch.
  </Card>

  <Card title="Freelancer or Service Provider" icon="fa-briefcase">
    Send a payment link with your invoice amount and description — get paid without sharing bank details.
  </Card>

  <Card title="Educator or Training Institute" icon="fa-graduation-cap">
    Collect course fees or registration payments individually or in bulk for an entire student batch.
  </Card>

  <Card title="Event Organiser or Hospitality Business" icon="fa-calendar-days">
    Take a deposit to confirm a booking and let the customer settle the balance later.
  </Card>

  <Card title="Social Seller or D2C Brand" icon="fa-basket-shopping">
    Share a payment link directly in a WhatsApp or Instagram conversation — no website needed.
  </Card>
</Cards>

***

## What Will I Need?

You do not need a website or developer to get started.<br />

You will need:<br />

<Columns layout="fixed">
  <Column>
    **A PayU merchant account:** <Anchor target="_blank" href="https://docs.payu.in/docs/set-up-your-account">Sign up here</Anchor> if you do not have an account.
  </Column>
</Columns>

<Columns layout="fixed">
  <Column>
    **Access to the PayU Dashboard:** Where you will create and manage your <Glossary>payment links</Glossary>.
  </Column>
</Columns>

<Columns layout="fixed">
  <Column>
    **Customer contact details**: Required details such as a phone number, email address, or WhatsApp contact.
  </Column>
</Columns>

<Columns layout="fixed">
  <Column>
    **Payment details**: Such as the amount, purpose, and any additional information you want to collect.
  </Column>
</Columns>

***

## How do I Create a Payment Link?

<Accordion title="1. Create a payment link" icon="far fa-link">
  1. Log in to your PayU Dashboard and go to **Payment Tools** → **Payment Links&#x20;**&#x66;rom then left navigation.
  2. Enter the amount, purpose, and any additional details you want to collect from your customer.
</Accordion>

<Accordion title="2. Share the link" icon="far fa-share-nodes">
  Share the payment link with your customer through WhatsApp, SMS, email, social media, or another channel.
</Accordion>

<Accordion title="3. Customer pays" icon="far fa-credit-card">
  Your customer opens the link, provides any requested information, chooses a payment method, and completes the payment.
</Accordion>

<Columns layout="fixed">
  <Column>
    **Need detailed steps?**  See [Create a Payment Link →](https://docs.payu.in/docs/create-a-payment-link)
  </Column>
</Columns>

<Columns layout="fixed">
  <Column>
    You can create payment links one at a time, or upload multiple links at once if you need to send payment requests to many customers.
  </Column>
</Columns>

***

## How does My Customer Pay?

When your customer receives the payment link:

<Accordion title="1. Opens the link" icon="far fa-link">
  Clicks the URL you sent them
</Accordion>

<Accordion title="Sees the payment details" icon="far fa-square-sliders-vertical">
  Amount, purpose, and any message you included
</Accordion>

<Accordion title="Fills in any required information (optional)" icon="far fa-keyboard-down">
  If you have set up a form to collect details like name, delivery address, or customer ID
</Accordion>

<Accordion title="Chooses payment method" icon="far fa-credit-card">
  UPI, cards, net banking, or wallets
</Accordion>

<Accordion title="Completes payment" icon="far fa-money-bills">
  enters payment details and confirms
</Accordion>

<Accordion title="Receives confirmation" icon="far fa-diagram-successor">
  sees a success or failure message
</Accordion>

Your customer does not need a PayU account or any special app. The link works in any browser.

***

## How do I Manage Payments?

Once your customer completes the payment:

<Accordion title="Filter and search" icon="far fa-filter">
  View links by status — **Active**, **Paid**, **Expired**, or **Deactivated** — or narrow by creation date. Use the calendar picker to set a custom date range.
</Accordion>

<Accordion title="Edit a link" icon="far fa-pen-to-square">
  Open a link's Detail view and click **Edit** to update the amount, expiry date, partial payment settings, or customer details after the link has been created.
</Accordion>

<Accordion title="Duplicate a link" icon="far fa-copy">
  Create a new link pre-filled with the same settings — amount, purpose, and options. Use it to reuse a configuration, correct a mistake, or send the same request to a different customer.
</Accordion>

<Accordion title="Resend a link" icon="far fa-share">
  Share any Active link again via SMS, email, or by copying the URL and sending it over WhatsApp or any channel — no limit on how many times you can resend.
</Accordion>

<Accordion title="Export records" icon="far fa-download">
  Download your payment link history as CSV or Excel — either a link-level summary or a transaction-level detail report — for reconciliation or reporting.
</Accordion>

<Accordion title="Deactivate a link" icon="far fa-ban">
  Stop a link from accepting further payments at any time from the Dashboard. To re-activate a deactivated or expired link, use the [Cancel / Change Status API](doc:api-cancel-status).
</Accordion>

→ [Manage Payment Links](doc:manage-payment-links)

***

## Use AI to Help You

You can manage Payment Links by conversation instead of navigating the Dashboard. Use **PayU Ask AI** — or paste these prompts directly into Claude, ChatGPT, or any AI assistant:

<Callout icon="🤖" theme="info">
  ### **Example Prompts to Try:**

  <br />

  - _"Create a PayU payment link for ₹500 that expires in 24 hours"_
  - _"Show me all my unpaid active payment links"_
  - _"Send invoice INV-2026-1042 to&#x20;_[priya@example.com](mailto:priya@example.com)_"_
  - _"Deactivate the payment link for order INV-2026-1042 — the customer paid by cash"_
  - _"How do I set up a partial payment link for a ₹10,000 deposit?"_

  For more context, prefix your prompt with: _"You are a PayU merchant assistant. I am using PayU Payment Links."_
</Callout>

If you are a **developer** building a backend service or AI agent that manages payment links programmatically, see [Integrate with AI Coding Assistants](doc:use-with-ai) (direct API) or [Use with AI Agents via MCP](doc:use-with-mcp) (MCP tool calls).

***

## Is Payment Links Secure?

Yes. Every Payment Link is served over HTTPS on PayU's PCI-DSS compliant hosted payment page. Your customer's card and UPI details never pass through your system. You do not configure anything; PayU handles it.<br />

You control additional fraud exposure through two settings available at link creation:<br />

- **Expiry date**: the link stops accepting payments after the date you set.
- **Single-use**: the link closes after the first successful payment, even if shared multiple times.

<Cards>
  <Card title="For Developers" icon="fad fa-key">
    Webhook signature verification for Payment Links uses your `client_secret`. Using the wrong secret will cause every hash check to fail silently. See <Anchor target="_blank" href="https://docs.payu.in/reference/webhooks">Webhooks</Anchor> for the correct formula and code examples.
  </Card>
</Cards>

***

## Next Steps

<Cards>
  <Card title="Start Using Payment Links" href="https://docs.payu.in/docs/create-a-payment-link" icon="far fa-link" target="_blank">
    - **Create a Payment Link:&#x20;**&#x43;reate your first link from the PayU Dashboard.
    - **Create Payment Links in Bulk:** Create multiple payment links at once.
  </Card>

  <Card title="For Developers" href="https://docs.payu.in/reference/payment-links" icon="far fa-gear-api" target="_blank">
    **Automate Payment Links with APIs:** Create and manage payment links programmatically.
  </Card>

  <Card title="How Payment Links Works" href="https://docs.payu.in/docs/payment-links-workflow" icon="fa-diagram-project" target="_blank">
    See the end-to-end flow — from creating a link to receiving funds in your bank.
  </Card>
</Cards>
