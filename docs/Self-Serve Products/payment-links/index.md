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

## What Can I Do with Payment Links?

<Glossary>Payment Links</Glossary> lets you collect payments by creating a secure payment link and sharing it with your customer through WhatsApp, SMS, email, or any other channel you use to communicate with them.<br />

You can use Payment Links to:<br />

- Create a payment request without a website
- Share it through WhatsApp, SMS, email, etc.
- Collect payments using multiple payment methods
- Track and manage payments from the Dashboard<br />

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

<Glossary>Payment Links</Glossary> is a good choice if: <br />

- **You don't have a website** and run your business through social media, messaging apps, or in person.
- **You want to request payment** from a specific customer for an invoice, order, or service.
- **You want to start collecting payments** quickly without building or learning a technical integration.
- **You run a small business or provide services** where you regularly send payment requests to individual customers.<br />

Consider another PayU solution if:<br />

- You want customers to pay directly on your website → <Anchor target="_blank" href="https://docs.payu.in/docs/prebuilt-checkout-payu-hosted">**Hosted Checkout**</Anchor>
- You want to create payment links programmatically → <Anchor target="_blank" href="https://docs.payu.in/reference/payment-links">**Payment Links APIs**</Anchor>

<Callout icon="far fa-face-thinking" theme="warn">
  ### **Not Sure Which PayU Solution is Right For You?**

  Tell us what you want to achieve and how you plan to accept payments. We will recommend the best PayU solution that fits your needs.<br />

  <Anchor target="_blank" href="https://docs.payu.in/docs/start-here">Find the Right Product for You</Anchor> →
</Callout>

***

## What Will I Need?

You don't need a website or developer to get started.<br />

You'll need:<br />

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

Here is how it works:

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

Your customer doesn't need a PayU account or any special app — the link works in any browser.

***

## How do I Manage Payments?

Once your customer completes the payment:

<Columns layout="fixed">
  <Column>
    **You see the payment status immediately&#x20;**&#x69;n your PayU Dashboard under **Payment Tools → Payment Links**
  </Column>
</Columns>

<Columns layout="fixed">
  <Column>
    <Columns layout="fixed">
      <Column>
        **Payment details are recorded**: You can see the amount, date, customer details, and transaction status
      </Column>
    </Columns>
  </Column>
</Columns>

<Columns layout="fixed">
  <Column>
    <Columns layout="fixed">
      <Column>
        **You can export payment history**: <Anchor target="_blank" href="https://docs.payu.in/docs/manage-payment-links#what-can-i-do-with-a-payment-link-after-it-is-created">Download a report</Anchor> of all payments received through your links
      </Column>
    </Columns>
  </Column>
</Columns>

<Columns layout="fixed">
  <Column>
    **Links can be reused or deactivated**: You control whether a link can be used multiple times or just once, and you can disable links that are no longer needed
  </Column>
</Columns>

If a payment fails, you can share the same link again for the customer to retry, or create a new one.

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
  <Card title="Start using Payment Links" href="https://docs.payu.in/docs/create-a-payment-link" icon="far fa-link" target="_blank">
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
