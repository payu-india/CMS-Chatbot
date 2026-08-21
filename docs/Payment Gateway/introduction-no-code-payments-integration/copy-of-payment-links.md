---
title: Payment Links V2
deprecated: false
hidden: true
metadata:
  title: Dashboard for Payment Links
  keywords:
    - 'Create Payment Link:'
    - Payment Link Integration
    - Create Payment Link in a few minutes
  robots: index
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

Payment Links lets you collect payments by creating a secure payment link and sharing it with your customer through WhatsApp, SMS, email, or any other channel you use to communicate with them.

You can use Payment Links to:

- Create a payment request without a website
- Share it through WhatsApp, SMS, email, etc.
- Collect payments using multiple payment methods
- Track and manage payments from the Dashboard

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

                <button onclick="window.open('https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/collection/rocz44o/payu-hosted-checkout-collection-complete-integration', '_blank')" 
                        class="tooltip-btn" 
                        data-tooltip="Click to see steps to create your first payment link.">
                    Create your first payment link →
                </button>
`}</HTMLBlock>

***

## Is Payment Links Right for Me?

Payment Links is a good choice if:

- **You don't have a website** and run your business through social media, messaging apps, or in person.
- **You want to request payment** from a specific customer for an invoice, order, or service.
- **You want to start collecting payments** quickly without building or learning a technical integration.
- **You run a small business or provide services** where you regularly send payment requests to individual customers.

Consider another PayU solution if:

- You want customers to pay directly on your website → **Hosted Checkout**
- You want to create payment links programmatically → **Payment Links APIs**

<Callout icon="far fa-face-thinking" theme="warn">
  ### **Not Sure Which PayU Solution is Right For You?**

  Tell us what you want to achieve and how you plan to accept payments. We will recommend the best PayU solution that fits your needs.

  Find the right solution →
</Callout>

***

## What Will I Need?

You don't need a website or developer to get started.

You'll need:

<Columns layout="fixed">
  <Column>
    **A PayU merchant account:** Sign up here if you do not have an account.
  </Column>
</Columns>

<Columns layout="fixed">
  <Column>
    **Access to the PayU Dashboard:** Where you will create and manage your payment links.
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
    **Need detailed steps?**  See Create a Payment Link →
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
        **You can export payment history**: Download a report of all payments received through your links
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

## Next Steps

<Cards>
  <Card title="**Ready to create your first payment link?**" icon="far fa-link">
    **[Create a Payment Link:](doc:create-a-new-payment-link)&#x20;**&#x73;tep-by-step guide to creating your first link from the PayU Dashboard
  </Card>

  <Card title="Want to create multiple payment links at once?" icon="far fa-check-double">
    **[Create Payment Links in Bulk:](doc:bulk-upload-to-create-multiple-payments-links)&#x20;**&#x75;pload a file to create many links at once
  </Card>

  <Card title="Need more control or want to automate link creation?" icon="fa-comments">
    **[Integration APIs for Payment Links](doc:integration-api-for-payment-links)** — technical documentation for developers who want to create links programmatically
  </Card>
</Cards>

***

## Video Tutorial

Check this video to see how PayU Payment Links work:

<Embed title="" typeOfEmbed="youtube" url="https://www.youtube.com/watch?v=rh_FQUMsaT0" href="https://www.youtube.com/watch?v=rh_FQUMsaT0" html="%3Ciframe%20class%3D%22embedly-embed%22%20src%3D%22%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Fsrc%3Dhttps%253A%252F%252Fwww.youtube.com%252Fembed%252Frh_FQUMsaT0%253Ffeature%253Doembed%26display_name%3DYouTube%26url%3Dhttps%253A%252F%252Fwww.youtube.com%252Fwatch%253Fv%253Drh_FQUMsaT0%26image%3Dhttps%253A%252F%252Fi.ytimg.com%252Fvi%252Frh_FQUMsaT0%252Fhqdefault.jpg%26type%3Dtext%252Fhtml%26schema%3Dyoutube%22%20width%3D%22854%22%20height%3D%22480%22%20scrolling%3D%22no%22%20title%3D%22YouTube%20embed%22%20frameborder%3D%220%22%20allow%3D%22autoplay%3B%20fullscreen%3B%20encrypted-media%3B%20picture-in-picture%3B%22%20allowfullscreen%3D%22true%22%3E%3C%2Fiframe%3E" providerName="YouTube" providerUrl="https://www.youtube.com/" />

<br />

<br />
