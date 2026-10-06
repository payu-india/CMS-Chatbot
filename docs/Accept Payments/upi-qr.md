---
title: UPI QR
excerpt: >-
  Generate a UPI QR code in the PayU Dashboard, display it at your counter or on
  a standee, and accept instant UPI payments — no developer needed.
deprecated: false
hidden: true
metadata:
  title: PayU UPI QR — No-Code In-Person Payments | Developer Docs
  description: >-
    Generate a UPI QR code from the PayU Dashboard and accept UPI payments
    in-person. No developer or technical setup needed.
  keywords:
    - payu upi qr
    - upi qr code payu
    - accept upi payment qr
    - payu qr code generator
    - static qr code payu
    - upi qr dashboard payu
    - no code upi payment india
    - payu bharat qr
    - offline upi payment payu
    - upi qr standee payu
  robots: index
next:
  description: Explore related information and resources.
---
<Banner
  isInline={true}
  message="Integration effort: No code or website developer required"
  color="#15C614"
  textColor="#ffffff"
  fontSize="14px"
  fontWeight="bold"
/>

PayU UPI QR lets you generate a QR code that your customers scan with any UPI app to pay you instantly no card machine or website required.<br />

You can use UPI QR to:<br />

* Generate a static QR code for your store counter, table, or printed standee
* Accept UPI payments from any app such as PhonePe, Google Pay, Paytm, BHIM, and all other UPI-enabled apps
* Set a fixed amount on the QR, or let the customer choose how much to pay
* Track all payments received against your QR codes in the Dashboard
* Download or print the QR code image directly from the Dashboard
* Deactivate a QR code at any time if it is no longer required<br />

<HTMLBlock>{`
  <style>
  .uqr-btn {
    position: relative;
    background-color: #00A550;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-weight: bold;
  }
  .uqr-btn:hover::after {
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
  <button onclick="window.open('https://docs.payu.in/docs/generate-a-upi-qr-code', '_blank')"
          class="uqr-btn"
          data-tooltip="Click to see steps to generate your first UPI QR code.">
    Generate your first UPI QR →
  </button>
`}</HTMLBlock>

***

## Is UPI QR Right for Me?

A UPI QR code is a good choice if:<br />

* **You have a physical store, stall, or counter** and want to accept digital payments without a card machine.
* **You run events, pop-up shops, or mobile businesses** where a printed QR on a standee is the easiest option.
* **Your customers already use UPI** — it is the most widely used payment method in India.
* **You want zero setup** — generate a QR in one minute and start accepting payments immediately.<br />

Consider another PayU solution if:<br />

* You need to collect payments remotely or online → <Anchor target="_blank" href="doc:payment-links-overview">**Payment Links**</Anchor>
* You want a pay button on your website → <Anchor target="_blank" href="doc:payment-button-overview">**Payment Buttons**</Anchor>
* You need to send a formal GST invoice to a customer → <Anchor target="_blank" href="doc:invoices-overview">**Invoices**</Anchor>
* You need a fully custom checkout with cards, net banking, and wallets → <Anchor target="_blank" href="doc:merchant-hosted-checkout">**Merchant Hosted Checkout**</Anchor>

<Callout icon="far fa-face-thinking" theme="warn">
  ### **Not Sure Which PayU Solution Is Right For You?**

  Tell us what you want to achieve and how you plan to accept payments. We will recommend the best PayU solution for your needs.

  <Anchor target="_blank" href="doc:start-here">Find the right solution</Anchor> →
</Callout>

***

## What Will I Need?

You don't need a developer or any technical setup to get started.

You'll need:

<Columns layout="fixed">
  <Column>
    **A PayU merchant account:** <Anchor target="_blank" href="doc:set-up-your-account">Sign up here</Anchor> if you do not have one.
  </Column>
</Columns>

<Columns layout="fixed">
  <Column>
    **A way to display the QR code:** A phone or tablet screen, a printed standee, a poster, or any surface your customers can point their UPI app at.
  </Column>
</Columns>

That's it. No developer needed.

***

## How Do I Generate a UPI QR Code?

Here is how it works:

<Accordion title="1. Open UPI QR in the Dashboard" icon="far fa-grid-2">
  Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/">PayU Dashboard</Anchor>, expand **Payment Tools**, and click **UPI QR**.
</Accordion>

<Accordion title="2. Click Generate New QR Code" icon="far fa-qrcode">
  Click **Generate New QR Code** at the top-right corner. Enter a name or label for the QR code so you can identify it later — for example, "Store Counter" or "Table 4".
</Accordion>

<Accordion title="3. Choose your QR type" icon="far fa-sliders">
  Select whether customers should pay a **fixed amount** (you enter the amount and the QR is locked to it) or **any amount** (customers enter the amount themselves in their UPI app). For standee or store-counter use, any-amount QR is the most common choice.
</Accordion>

<Accordion title="4. Download or display the QR code" icon="far fa-arrow-down-to-bracket">
  Click **Generate**. Your QR code is created immediately. Download it as a PNG image to print, or display the QR on screen for customers to scan directly.
</Accordion>

<Columns layout="fixed">
  <Column>
    **Need detailed steps?** See [Generate a UPI QR Code →](doc:generate-a-upi-qr-code)
  </Column>
</Columns>

***

## How Does My Customer Pay?

When your customer sees the QR code:

<Accordion title="1. Opens their UPI app" icon="far fa-mobile">
  The customer opens any UPI-enabled app — PhonePe, Google Pay, Paytm, BHIM, or any bank's UPI app — and taps **Scan QR** or the camera icon.
</Accordion>

<Accordion title="2. Scans the QR code" icon="far fa-qrcode">
  They point their camera at the QR code. The app reads it instantly and opens the payment screen. If the QR has a fixed amount, the amount is filled in automatically. If it is an any-amount QR, the customer types in the amount.
</Accordion>

<Accordion title="3. Confirms and pays" icon="far fa-circle-check">
  The customer reviews the merchant name and amount, enters their UPI PIN, and confirms the payment. The transaction completes in seconds.
</Accordion>

<Accordion title="4. You receive confirmation" icon="far fa-bell">
  Your Dashboard shows the payment immediately under the QR code's transaction history. The customer's UPI app also shows a success screen.
</Accordion>

Your customer does not need a PayU account — they can pay using any UPI app on any phone.

***

## How Do I Manage My QR Codes?

Once your QR codes are live:

<Columns layout="fixed">
  <Column>
    **View all QR codes** in one place — active and deactivated — from **Payment Tools → UPI QR** in the Dashboard.
  </Column>
</Columns>

<Columns layout="fixed">
  <Column>
    **See payment history** for any QR code — filter by date to see all transactions against a specific code.
  </Column>
</Columns>

<Columns layout="fixed">
  <Column>
    **Download records** — export transaction data as CSV or Excel for your accounts.
  </Column>
</Columns>

<Columns layout="fixed">
  <Column>
    **Deactivate a QR code** at any time if it has been lost, stolen, or is no longer needed.
  </Column>
</Columns>

***

## Next Steps

<Cards>
  <Card title="Generate a UPI QR Code" href="doc:generate-a-upi-qr-code" icon="far fa-qrcode">
    Step-by-step guide to generating and displaying your first QR code.
  </Card>

  <Card title="Manage UPI QR Codes" href="doc:manage-upi-qr-codes" icon="fa-list-check">
    View payments, download records, and manage your QR codes.
  </Card>

  <Card title="UPI QR FAQs" href="doc:upi-qr-faqs" icon="fa-circle-question">
    Common questions about PayU UPI QR.
  </Card>
</Cards>
