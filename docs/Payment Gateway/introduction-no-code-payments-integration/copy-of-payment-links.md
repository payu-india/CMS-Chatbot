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
<Callout icon="🟢" theme="success">
  **No Coding Required**

  Create and share payment links directly from your PayU Dashboard — no website or technical setup needed.
</Callout>

***

## What is Payment Links?

Payment Links lets you collect payments by creating a secure payment link and sharing it with your customer through WhatsApp, SMS, email, or any other channel you use to communicate with them.

Your customer clicks the link, enters their payment details, and completes the payment — all without needing a website or checkout page.

***

## Is this right for me?

Payment Links is best when:

- **You don't have a website** — you run your business through social media, messaging apps, or in person
- **You want to request payment from a specific customer** — for an invoice, order, or service
- **You want to collect payments quickly** — without building or learning how to use technical integrations
- **You operate a small business or provide services** — where you send payment requests to individual customers

If you want customers to pay directly on your website during checkout, consider [PayU Hosted Checkout](https://docs.payu.in/docs/prebuilt-checkout-page-integration) instead.

***

## What you'll need

To start using Payment Links:

- **PayU merchant account** — [Sign up here](https://onboarding.payu.in/) if you don't have one yet
- **Access to PayU Dashboard** — where you'll create your payment links
- **Customer contact details** — so you can share the link (email, phone number, WhatsApp, etc.)
- **Payment details** — amount, purpose/description, and any custom information you want to collect from the customer

***

## How it works

Here's what you do:

<Cards columns="3">
  <Card>
    <div style={{ color: "#000", padding: "8px" }}>
      <i className="fa fa-plus-circle" style={{ color: "#00b386", fontSize: "20px", marginBottom: "10px" }}></i>

      <h4 style={{ margin: "0 0 6px 0", fontWeight: "600" }}>1. Create a payment link</h4>

      <p style={{ margin: 0 }}>

        Log in to your PayU Dashboard, go to <b>Payment Tools → Payment Links</b>, and create a new link. Enter the amount, purpose, and any custom details you want to collect from your customer (like name, delivery address, or order details).
      </p>
    </div>
  </Card>

  <Card>
    <div style={{ color: "#000", padding: "8px" }}>
      <i className="fa fa-share-alt" style={{ color: "#00b386", fontSize: "20px", marginBottom: "10px" }}></i>

      <h4 style={{ margin: "0 0 6px 0", fontWeight: "600" }}>2. Share the link</h4>

      <p style={{ margin: 0 }}>

        Copy the payment link and send it to your customer through WhatsApp, SMS, email, or any other channel. You can also share it through social media or your messaging platform.
      </p>
    </div>
  </Card>

  <Card>
    <div style={{ color: "#000", padding: "8px" }}>
      <i className="fa fa-check-circle" style={{ color: "#00b386", fontSize: "20px", marginBottom: "10px" }}></i>

      <h4 style={{ margin: "0 0 6px 0", fontWeight: "600" }}>3. Customer pays</h4>

      <p style={{ margin: 0 }}>

        Your customer clicks the link, fills in any requested details (if you've set up a form), and completes the payment using their preferred payment method.
      </p>
    </div>
  </Card>
</Cards>

You can create payment links one at a time, or upload multiple links at once if you need to send payment requests to many customers.

***

## What your customer does

When your customer receives the payment link:

1. **Opens the link** — clicks the URL you sent them
2. **Sees the payment details** — amount, purpose, and any message you included
3. **Fills in any required information** (optional) — if you've set up a form to collect details like name, delivery address, or customer ID
4. **Chooses payment method** — UPI, cards, net banking, or wallets
5. **Completes payment** — enters payment details and confirms
6. **Receives confirmation** — sees a success or failure message

Your customer doesn't need a PayU account or any special app — the link works in any browser.

***

## What happens after payment?

Once your customer completes the payment:

- **You see the payment status immediately** in your PayU Dashboard under **Payment Tools → Payment Links**
- **Payment details are recorded** — you can see the amount, date, customer details, and transaction status
- **You can export payment history** — download a report of all payments received through your links
- **Links can be reused or deactivated** — you control whether a link can be used multiple times or just once, and you can disable links that are no longer needed

If a payment fails, you can share the same link again for the customer to retry, or create a new one.

***

## Next steps

Ready to create your first payment link?

- **[Create a Payment Link](doc:create-a-new-payment-link)** — step-by-step guide to creating your first link from the PayU Dashboard

Want to create multiple payment links at once?

- **[Create Payment Links in Bulk](doc:bulk-upload-to-create-multiple-payments-links)** — upload a file to create many links at once

Need more control or want to automate link creation?

- **[Integration APIs for Payment Links](doc:integration-api-for-payment-links)** — technical documentation for developers who want to create links programmatically

<br />

### More resources

Check this video to see how PayU Payment Links work:

<Embed title="" typeOfEmbed="youtube" url="https://www.youtube.com/watch?v=rh_FQUMsaT0" href="https://www.youtube.com/watch?v=rh_FQUMsaT0" html="%3Ciframe%20class%3D%22embedly-embed%22%20src%3D%22%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Fsrc%3Dhttps%253A%252F%252Fwww.youtube.com%252Fembed%252Frh_FQUMsaT0%253Ffeature%253Doembed%26display_name%3DYouTube%26url%3Dhttps%253A%252F%252Fwww.youtube.com%252Fwatch%253Fv%253Drh_FQUMsaT0%26image%3Dhttps%253A%252F%252Fi.ytimg.com%252Fvi%252Frh_FQUMsaT0%252Fhqdefault.jpg%26type%3Dtext%252Fhtml%26schema%3Dyoutube%22%20width%3D%22854%22%20height%3D%22480%22%20scrolling%3D%22no%22%20title%3D%22YouTube%20embed%22%20frameborder%3D%220%22%20allow%3D%22autoplay%3B%20fullscreen%3B%20encrypted-media%3B%20picture-in-picture%3B%22%20allowfullscreen%3D%22true%22%3E%3C%2Fiframe%3E" providerName="YouTube" providerUrl="https://www.youtube.com/" />

<br />

### All Payment Links guides

- [Create a Payment Link](doc:create-a-new-payment-link)
- [Create Payment Links in Bulk](doc:bulk-upload-to-create-multiple-payments-links)
- [Customize the Calendar View for Payment Links](doc:customize-the-calendar-view-for-payment-links)
- [Categorize the Payment Links View](doc:categorize-the-payment-links-view)
- [Export the Payment Link History](doc:export-the-payment-link-history)
- [Integration APIs for Payment Links](doc:integration-api-for-payment-links)
- [FAQs - Payment Links](doc:faqs-payment-links)