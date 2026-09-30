---
title: Payment Button Troubleshooting
excerpt: >-
  Fix common Payment Button problems — button not showing on your page, payment
  not completing, redirect not working, and transaction not reflecting in the
  Dashboard.
deprecated: false
hidden: true
metadata:
  title: Payment Button Troubleshooting | PayU Developer Docs
  description: >-
    Fix PayU Payment Button issues — button not showing on page, payment not
    completing, redirect not working, and transaction not showing in the
    Dashboard.
  keywords:
    - payment button not showing payu
    - payment button not working
    - payment button redirect not working
    - payu payment button troubleshooting
    - payment button transaction not showing
    - payu button click nothing happens
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
---
{/* NEW CONTENT */}

Something not working after adding your <Anchor target="_blank" href="https://docs.payu.in/docs/payment-button">Payment Button</Anchor> to your website? Go through the most common issues such as button not showing on your page, the payment page not opening, payments not reflecting in your Dashboard, and ways to fix them.

<Callout icon="📘" theme="info">
  ### **Payment Buttons**

  Haven't added a payment button yet? → <Anchor target="_blank" href="https://docs.payu.in/docs/add-payment-button">Add a Payment Button</Anchor>
</Callout>

***

## Why Is My Button Not Showing on My Page?

<Accordion title="Button Not Appearing After Adding the Code" icon="far fa-eye-slash">
  Check these in order:

  1. **Make sure the code is in a code or HTML block — not a text block.** Page builders like WordPress, Wix, and Squarespace have separate Text blocks and HTML/Code blocks. The button code must go in an **HTML or Code block**. Pasting it into a text editor will display it as plain text, not a button.

  2. **Copy the code again from the Dashboard.** Go to **Payment Tools → Payment Buttons**, find your button, and copy the complete code. Even one missing character will stop it from working.

  3. **Check the published page, not the preview.** Some website builders only load the button on a live, published page — it may not appear in draft or preview mode.

  4. **Clear your browser cache and reload the page.** Old cached files sometimes prevent updates from showing.

  5. **Test in a different browser.** If the button shows in one browser but not another, a browser extension or setting may be blocking it. Try in a private/incognito window with extensions turned off.

  <Callout icon="📘" theme="info">
    If your website has strong custom styling and it is affecting how the button looks — for example it appears too large or out of place — contact your web designer. The fix is a style adjustment on your website, not on the button code.
  </Callout>
</Accordion>

***

## Why Is the Payment Page Not Opening When the Button Is Clicked?

<Accordion title="Button Click Does Nothing or Opens a Blank Page" icon="far fa-rectangle-xmark">
  Check these:

  1. **Pop-up blocker.** PayU's payment page opens in a new tab or pop-up window. Most browsers block pop-ups by default. Ask your customer to allow pop-ups for your website, or test it yourself in a browser with pop-ups turned on.

  2. **Copy the button code again.** If the code on your website is old or incomplete, clicking the button may fail silently. Remove the existing code, copy it again from the Dashboard, and paste it fresh.

  3. **Make sure your website uses HTTPS.** PayU's payment page requires a secure connection. If your website address starts with `http://` instead of `https://`, the button may be blocked by the browser. Contact your web hosting provider to enable HTTPS.
</Accordion>

***

## Why Is the Payment Not Going Through?

<Accordion title="Customer Reaches the Payment Page but Payment Fails" icon="far fa-circle-xmark">
  Ask your customer: what payment method did they try, and what message did they see?

  | Message the Customer Saw       | Likely Reason                                      | What to Do                                                                                           |
  | ------------------------------ | -------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
  | "Transaction declined by bank" | Their bank or card issuer declined the payment     | Ask them to try a different card or contact their bank                                               |
  | "Payment method not available" | That method is not turned on for your account      | Contact <Anchor target="_blank" href="https://help.payu.in/query">PayU support</Anchor> to enable it |
  | Page stuck or keeps loading    | Poor internet connection on the customer's side    | Ask them to try on a better connection or a different browser                                        |
  | "Amount exceeds limit"         | The customer's card or UPI daily limit was reached | Ask them to try a different payment method                                                           |

  **If no payment methods appear at all on the payment page:** contact <Anchor target="_blank" href="https://help.payu.in/query">PayU support</Anchor> — your account may need specific payment methods turned on.
</Accordion>

***

## Why Is My Customer Not Being Sent Back to My Website After Payment?

<Accordion title="Customer Is Not Redirected to My Thank-You or Error Page" icon="far fa-arrow-right-arrow-left">
  Check the following:

  1. **Were redirect pages set when the button was created?** Redirect pages are set at the time you create the button and cannot be changed after. If you did not set them, your customer will land on PayU's default confirmation page — not your website. Create a new button with the correct pages filled in under **Advanced Options**.

  2. **Check for typos in the page addresses.** A single character error — missing `https://`, wrong domain name — causes the redirect to fail. Make sure each address starts with `https://` and points to a real, live page on your website.

  3. **Make sure the pages are live and publicly accessible.** The redirect pages must be reachable by anyone on the internet. Pages that are behind a login or still in draft will not work.

  <Callout icon="📘" theme="info">
    Payment Buttons cannot be changed after creation. If your redirect pages are wrong, create a new button with the correct addresses and replace the code on your website.
  </Callout>
</Accordion>

***

## Why Is the Transaction Not Showing in My Dashboard?

<Accordion title="Payment Looks Successful but I Cannot Find It" icon="far fa-clock">
  Follow these steps:

  1. **Wait 5–10 minutes and refresh.** The Dashboard updates in near-real-time but can occasionally take a few minutes.
  2. **Look in the Transactions tab** — not the Payment Buttons tab. Payments made through your buttons appear in the main **Transactions** section of your Dashboard.
  3. **Search by amount or date** to find the specific payment.

  <Columns layout="fixed">
    <Column>
      **If the transaction appears in Transactions but the button status has not updated:**

      The payment has been received. The button record will update within 30 minutes. Contact <Anchor target="_blank" href="https://help.payu.in/query">PayU support</Anchor> with the transaction ID if it does not update within an hour.
    </Column>
  </Columns>

  <Columns layout="fixed">
    <Column>
      **If the transaction does not appear anywhere after 30 minutes:**

      The payment may have failed on the customer's bank side, even if it appeared to go through. Banks sometimes automatically reverse such charges within 5–7 business days. Ask your customer to check their bank statement. If the charge was not reversed, contact <Anchor target="_blank" href="https://help.payu.in/query">PayU support</Anchor> with the customer's bank reference number.
    </Column>
  </Columns>
</Accordion>

***

## How Do I Fix a Button with Wrong Details?

<Accordion title="Wrong Amount, Label, or Redirect Page on the Button" icon="far fa-pen-to-square">
  Payment Buttons cannot be changed after creation.

  **What to do:** Create a new button with the correct details, copy the new button code, and replace the old code on your website. If the old button is still live on any page, replace it there too so customers do not accidentally use it.
</Accordion>

***

## Still Stuck?

Contact PayU support with these details:

* [x] Payment Button name (from your Dashboard)
* [x] The page on your website where the button is added
* [x] Transaction ID (if your customer attempted a payment)
* [x] Date and time of the issue
* [x] Screenshot of any error message
* [x] Browser and device your customer was using

Contact PayU Support via the Dashboard **Help** section, or email `support@payu.in`.

***

## Next Steps

<Cards>
  <Card title="Add a Payment Button" href="doc:add-a-payment-button" icon="far fa-plus">
    Create a new payment button and add it to your website.
  </Card>

  <Card title="Manage Payment Buttons" href="doc:manage-payment-buttons" icon="fa-list-check">
    View payments, filter your buttons, and download records.
  </Card>

  <Card title="Payment Button FAQs" href="doc:payment-button-faqs" icon="fa-circle-question">
    Common questions about Payment Buttons.
  </Card>
</Cards>
