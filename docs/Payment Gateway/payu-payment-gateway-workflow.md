---
title: Payment Gateway Workflow
deprecated: false
hidden: false
metadata:
  robots: index
next:
  description: Refer to the following pages for additional information.
  pages:
    - slug: collect-payments-introduction
      title: Payment Gateway Overview
      type: basic
    - slug: choose-your-checkout-integration
      title: Start Here - Choose Your Integration
      type: basic
---
The following diagram illustrates how PayU payment gateway works.

<Image align="center" border={true} caption="PayU Payment Gateway Workflow" src="https://files.readme.io/e86f46efa326b45231453c864b3c325192d9f70927b617b38891175a73760e89-Payment_Checkout_Process-2026-03-31-063227.png" />

<Accordion title="1. Customer Initiates a Payment" icon="fa-check">
  A customer selects products or services on your website or app and clicks on “Pay Now” at checkout.
</Accordion>

<Accordion title="2. Customer Provides Payment Details" icon="fa-check">
  The customer enters their payment details (card, UPI, net banking, wallet, etc.) on the PayU-hosted or integrated checkout page.
</Accordion>

<Accordion title="3. PayU Encrypts the Data" icon="fa-check">
  PayU securely encrypts the payment information to ensure sensitive data is protected during transmission.
</Accordion>

<Accordion title="4. Request Sent to an Acquiring Bank" icon="fa-check">
  The encrypted payment request is sent to the acquiring bank (the bank that processes payments for the merchant).
</Accordion>

<Accordion title="5. Card Network or Payment Method Routing" icon="fa-check">
  If it is a card payment, the request is routed through the supoorted card network (like Visa, Mastercard, etc.).
</Accordion>

<Accordion title="6. Issuing Bank Verifies Payment" icon="fa-check">
  The issuing bank (customer’s bank):

  * Verifies if the account has sufficient balance and payment details are valid
  * Performs authentication (like OTP or 3D Secure)
</Accordion>

<Accordion title="7. Issuing Bank Gebnerates the Authorization Response" icon="fa-check">
  The issuing bank approves or declines the transaction and sends a response back through the same chain (network → acquiring bank → PayU).
</Accordion>

<Accordion title="8. PayU Shares the Response with Merchant and Customer" icon="fa-check">
  PayU receives the response and displays the final status (success or failure) to the customer on the checkout page. The merchant system is also updated with the transaction result.
</Accordion>

## Video Tutorial

Watch this video to know what is PayU Payment Gateway and how does it work.

<Embed typeOfEmbed="youtube" url="https://www.youtube.com/watch?v=7n8KrT6Bkfk" html="%3Ciframe%20class%3D%22embedly-embed%22%20src%3D%22%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Fsrc%3Dhttps%253A%252F%252Fwww.youtube.com%252Fembed%252F7n8KrT6Bkfk%253Ffeature%253Doembed%26display_name%3DYouTube%26url%3Dhttps%253A%252F%252Fwww.youtube.com%252Fwatch%253Fv%253D7n8KrT6Bkfk%26image%3Dhttps%253A%252F%252Fi.ytimg.com%252Fvi%252F7n8KrT6Bkfk%252Fhqdefault.jpg%26type%3Dtext%252Fhtml%26schema%3Dyoutube%22%20width%3D%22854%22%20height%3D%22480%22%20scrolling%3D%22no%22%20title%3D%22YouTube%20embed%22%20frameborder%3D%220%22%20allow%3D%22autoplay%3B%20fullscreen%3B%20encrypted-media%3B%20picture-in-picture%3B%22%20allowfullscreen%3D%22true%22%3E%3C%2Fiframe%3E" href="https://www.youtube.com/watch?v=7n8KrT6Bkfk" providerUrl="https://www.youtube.com/" providerName="YouTube" />

## Try PayU Checkout

You can try PayU checkout and make test transactions using our **Integration Labs**.

<PayU_Labs />

## Test Credentials

You can use these <Anchor label="test credentials" target="_blank" href="/docs/test-cards-upi-id-and-wallets">test credentials</Anchor> to test subscriptions, domestic, and international payments.

## Post-Transaction Capabilities

Once you integrate with PayU, you can also manage post-payment operations seamlessly:

<HoverCardGrid
  columns={3}
  items={[
    {
      title: 'Refunds',
      href: '/docs/introduction-refunds',
      text: 'Initiate full or partial refunds for successful transactions directly via PayU APIs or dashboard.',
    },
    {
      title: 'Split Settlements',
      href: '/docs/split-settlments',
      text: 'Automatically split incoming payments between multiple stakeholders (such as vendors or partners) as per predefined rules.',
    },
  ]}
/>

<br />