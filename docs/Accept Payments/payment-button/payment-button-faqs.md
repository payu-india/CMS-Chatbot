---
title: FAQs (Frequently Asked Questions)
excerpt: >-
  Answers to common questions about PayU Payment Buttons — creation, embed,
  amount types, redirect pages, payments, and managing your buttons.
deprecated: false
hidden: true
metadata:
  title: Payment Button FAQs | PayU Developer Docs
  description: >-
    Answers to common PayU Payment Button questions — creating buttons, embed,
    code, fixed vs variable amount, redirect pages, disabling buttons, and more.
  keywords:
    - payu payment button faq
    - payment button vs payment link
    - multiple payment buttons payu
    - payment button fixed variable amount
    - edit payment button payu
    - payment button no code
    - payu embed button questions
  robots: index
next:
  description: Explore related information and resources.
  pages:
    - slug: payment-button
      title: Payment Button
      type: basic
    - slug: add-payment-button
      title: Add a Payment Button
      type: basic
    - slug: manage-payment-buttons
      title: Manage Payment Buttons
      type: basic
    - slug: payment-links-errors-and-troubleshooting
      title: Errors and Troubleshooting
      type: basic
---
{/* NEW CONTENT */}

## General

1. #### What is a Payment Button and how does it work?

<Accordion title="Answer" icon="fab fa-adn">
  A PayU <Anchor target="_blank" href="https://docs.payu.in/docs/payment-button">Payment Button</Anchor> is a **Buy Now**, **Pay Now**, **Book Now**, or **Donate Now** button you add to your website or blog. You create and configure it in the PayU Dashboard. We give you a short piece of code to paste on your page. When a visitor clicks the button, PayU's payment page opens and they can complete their payment. Once done, they are sent back to your website. No developer or server setup is required. Refer to <Anchor target="_blank" href="https://docs.payu.in/docs/add-payment-button">Add a Payment Button</Anchor> for steps top add a payment button
</Accordion>

***

2. #### Do I need a developer or any code to create a Payment Button?

<Accordion title="Answer" icon="fab fa-adn">
  You do not need a developer to create the payment button. You set it up in the PayU Dashboard and we give you the button code.

  You should paste that code onto your website. Most website builders such as WordPress, Wix, Squarespace, Webflow, have an HTML or Code block where you can do this without writing code. If your site is fully managed and you cannot add content yourself, ask whoever looks after your website to paste the code for you.
</Accordion>

***

3. #### Is a Payment Button the same as a Payment Link?

<Accordion title="Answer" icon="fab fa-adn">
  No. They serve different purposes:

  | Queries               | Payment Button                                         | Payment Link                             |
  | --------------------- | ------------------------------------------------------ | ---------------------------------------- |
  | How it works          | Sits on your webpage and customers click it            | A URL you share with a customer directly |
  | How it is shared      | Customer finds it on your website                      | You send it via WhatsApp, SMS, or email  |
  | Is a website Required | Yes. You need a page to add it to                      | No. You just share the link              |
  | Best for              | Always-available buy or donate buttons on a fixed page | One-off or personalised payment requests |

  <Callout icon="📘" theme="info">
    ### **Tips:**

    Both use PayU's payment page and support the same payment methods.
  </Callout>
</Accordion>

***

4. #### Which payment methods can customers use?

<Accordion title="Answer" icon="fab fa-adn">
  Customers can pay using any method enabled on your merchant account such as credit and debit cards (Visa, Mastercard, RuPay, Amex), UPI, Net Banking, Wallets, EMI, and BNPL. Contact <Anchor target="_blank" href="https://help.payu.in/raise-ticket">PayU support</Anchor> to enable or disable specific methods.
</Accordion>

***

5. #### Can I turn off a Payment Button and re-enable it later? <Badge type="success">New</Badge>

<Accordion title="Answer" icon="fab fa-adn">
  You cannot turn-off a payment button. However, you can [delete](https://docs.payu.in/docs/manage-payment-buttons#delete-a-payment-button) it to stop accepting payments permanently.

  If you have already deleted a button and need to accept payments again for the same purpose, create a new button with the same settings and add it to your website.
</Accordion>

***

6. #### Are Payment Buttons secure?

<Accordion title="Answer" icon="fab fa-adn">
  Yes. PayU Payment Buttons are PCI DSS compliant. We use encryption and tokenisation to protect customer payment data. No card or bank details are ever handled by your website, everything goes through PayU's secure payment page.
</Accordion>

***

## Creating and Configuring Buttons

1. #### Can I have multiple Payment Buttons on the same website?

<Accordion title="Answer" icon="fab fa-adn">
  Yes. You can create as many Payment Buttons as you need. Each button has its own unique code. For example, you can have a **Buy Now** button on a product page, a **Donate Now** button on a fundraising page, and a **Book Now** button on an events page, all on the same website.

  **Each button is independent:** changing or removing one does not affect the others.
</Accordion>

***

2. #### Can I use a fixed amount or let customers enter their own amount?

<Accordion title="Answer" icon="fab fa-adn">
  Both options are available:

  - **Fixed amount**: Enter a specific amount in the **Amount** field when creating the button. Customers cannot change it at checkout.
  - **Open amount**: Leave the **Amount** field blank. Customers will enter the amount themselves on the payment page.

  The open amount option is well suited for donations, tips, or any payment where the value differs per customer.
</Accordion>

***

3. #### Should I enter the amount in rupees or paise? <Badge type="success">New</Badge>

<Accordion title="Answer" icon="fab fa-adn">
  When creating a Payment Button from the **PayU Dashboard**, enter the amount in **rupees (INR)**. For example, enter `500` for ₹500.

  Do not enter the amount in paise. Paise values are only used in certain API integrations.
</Accordion>

***

4. #### Can I change the button label to something other than the four preset options?

<Accordion title="Answer" icon="fab fa-adn">
  No. The button label drop-down is limited to four options such as, **Buy Now**, **Pay Now**, **Book Now**, and **Donate Now**. Custom labels are not currently supported from the Dashboard.

  If none of the presets fit your use case, you can create your own button on your website and attach a <Anchor target="_blank" href="https://docs.payu.in/docs/payment-links">Payment Link</Anchor> to it. This way, you get full control over the button text while still using PayU's payment page.
</Accordion>

***

5. #### Can I edit a Payment Button after creating it?

<Accordion title="Answer" icon="fab fa-adn">
  Yes. You can <Anchor target="_blank" href="https://docs.payu.in/docs/manage-payment-buttons#edit-payment-button-details">edit a Payment Button</Anchor> settings cannot be changed after it is created. Afer you save the new btton configuration, a new code will be generated. You should copy and paste the new code in your website.
</Accordion>

***

6. #### Can I collect customer details (name, email, phone) with the payment?

<Accordion title="Answer" icon="fab fa-adn">
  Yes. When <Anchor target="_blank" href="https://docs.payu.in/docs/add-payment-button#how-do-i-add-a-payment-button">creating the button</Anchor>, switch on any standard fields in the **Custom Details** section such as **Customer Name**, **Customer Address**, **Customer Email**, and **Customer Mobile**. You can also add your own custom fields (text, calendar, or drop-down) with any label. Mark any field as mandatory to require it before the customer can proceed to pay.
</Accordion>

***

7. #### Can I add the custom redirect URL where customers are sent after they payment? <Badge type="success">New</Badge>

<Accordion title="Answer" icon="fab fa-adn">
  Yes. Under **Advanced Options** when creating the button, you can enter:

  - **Success URL**: Where customers are sent after a successful payment
  - **Cancel URL**: Where customers are sent if they close the payment page without paying
  - **Failure URL**: Where customers are sent if the payment does not go through<br />

  These are optional but recommended. Without them, customers land on a default PayU confirmation page and are not automatically returned to your website.
</Accordion>

***

## Embed and Technical

1. #### Where do I paste the button code on my website?

<Accordion title="Answer" icon="fab fa-adn">
  Paste the code in any **HTML or Code block** on your website. Common placements:

  - **WordPress**: Use a Custom HTML widget or block
  - **Wix**: Use an Embed HTML element
  - **Squarespace / Webflow**: Use a Code block
  - **Plain website**: Paste inside the `<body>` section of your page wherever you want the button to appear<br />

  The button appears as soon as the page loads.
</Accordion>

***

2. #### Can I use the same button code on multiple pages?

<Accordion title="Answer" icon="fab fa-adn">
  Yes. You can paste the same button code on as many pages as you like. Every customer who clicks the button will see the same settings (same amount, label, and checkout fields). If you need different settings on different pages, create a separate button for each page.
</Accordion>

***

3. #### Can I customise the button's appearance beyond what the Dashboard offers?

<Accordion title="Answer" icon="fab fa-adn">
  The Dashboard lets you choose colour, size, and label. Further styling such as custom fonts, border radius, hover effects, and so on is not supported through the Dashboard.

  If you need a fully custom-styled button, create your own button design on your website and attach a <Anchor target="_blank" href="https://docs.payu.in/docs/payment-links">Payment Link URL</Anchor> to it to get complete visual control while still using PayU's payment page.
</Accordion>

***

4. #### My success page shows an error after a customer pays. Why? <Badge type="success">New</Badge>

<Accordion title="Answer" icon="fab fa-adn">
  This is almost always a **POST vs GET** issue. PayU sends the customer to your success page using a **POST request**, not a GET request. The payment details (transaction ID, amount, status) are sent as POST parameters in the request body.<br />

  If your success page is set up to read URL parameters (GET), it will not find the payment data and may show an error, even though the payment went through successfully.<br />

  **How to fix:**

  - Update your success page to read POST parameters from the request body instead of URL parameters.
  - If your success page just shows a thank-you message and does not need to read payment data, it should load without issues. Check for any server-side errors on the page itself.<br />

  You can confirm the payment went through by checking the **Transactions** tab in your PayU Dashboard.
</Accordion>

***

5. #### The payment page opens on its own without my customer clicking the button. Why? <Badge type="success">New</Badge>

<Accordion title="Answer" icon="fab fa-adn">
  This can happen for one of these reasons:

  1. **The button code is inside a&#x20;**`<form>`**&#x20;tag.** If the surrounding page has a form that submits on load, it can trigger the button. Move the button code outside any `<form>` element.
  2. **A JavaScript conflict on your page.** Another script on your website may be triggering a click event on the button automatically. Check your browser console (`F12 → Console`) for JavaScript errors and test the page with other scripts temporarily disabled.
  3. **The page is caching an old session.** Clear your browser cache and test again in a private or incognito window.

  If the issue persists, contact <Anchor target="_blank" href="https://help.payu.in/raise-ticket">PayU support</Anchor> with your button name and the page URL where the button is added.
</Accordion>

***

## Payments and Reconciliation

1. #### How will I know when a customer has paid via a button?

<Accordion title="Answer" icon="fab fa-adn">
  The payment appears in the **Transactions** tab of your PayU Dashboard right away. For instant notifications, set up a webhook under **Settings → Webhooks** in the Dashboard. PayU will send a `payment.success` event to your server each time a payment is completed.

  → <Anchor target="_blank" href="https://docs.payu.in/docs/manage-webhooks-using-dashboard">Webhooks for Payments</Anchor>
</Accordion>

***

2. #### Can I issue a refund for a payment made via a Payment Button?

<Accordion title="Answer" icon="fab fa-adn">
  Yes. Find the transaction in the **Transactions** tab of your Dashboard and start a refund from there. The refund process is the same regardless of how the payment was collected.
</Accordion>

***

3. #### Can I use Payment Buttons for subscription or recurring payments? <Badge type="success">New</Badge>

<Accordion title="Answer" icon="fab fa-adn">
  No. Payment Buttons are for one-time payments only. Each time a customer clicks the button, it is a separate, individual payment.<br />

  If you need to charge customers on a recurring schedule, for example monthly fees, membership dues, or subscription plans, use PayU's <Anchor target="_blank" href="https://docs.payu.in/docs/introduction-recurring-payments-integration">Recurring Payments</Anchor> product instead.
</Accordion>

***

4. #### Why is a transaction showing as `Pending` in my Dashboard?

<Accordion title="Answer" icon="fab fa-adn">
  'Pending' means the payment was started but not yet confirmed by the customer's bank. This usually resolves within a few minutes.<br />

  If a transaction stays in Pending for more than 30 minutes, the customer's bank may not have completed the authorisation. The amount (if debited) is typically returned automatically by the bank within 5–7 business days.<br />

  If the Pending status does not resolve after an hour, contact <Anchor target="_blank" href="https://help.payu.in/query">PayU support</Anchor> with the transaction date, amount, and the customer's payment method.
</Accordion>

***

## Next Steps

<Cards>
  <Card title="Add a Payment Button" href="doc:add-a-payment-button" icon="far fa-plus">
    Step-by-step guide to creating and adding a button to your website.
  </Card>

  <Card title="Manage Payment Buttons" href="doc:manage-payment-buttons" icon="fa-list-check">
    View payments, filter, download records, and manage your buttons.
  </Card>

  <Card title="Payment Button Troubleshooting" href="doc:payment-button-troubleshooting" icon="fa-wrench">
    Fix issues with buttons not showing, payments failing, or redirects not working.
  </Card>

  <Card title="Payment Links" href="doc:payment-links-overview" icon="fa-link">
    Need to share a payment request instead of embedding a button? Use Payment Links.
  </Card>
</Cards>
