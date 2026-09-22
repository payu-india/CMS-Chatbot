---
title: Errors and Troubleshooting
excerpt: >-
  Diagnose and fix common Payment Links problems — links not opening, payments
  not reflecting, notifications not delivered, and API errors.
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  title: Payment Links Troubleshooting | PayU Developer Docs
  description: >-
    Fix PayU Payment Links issues — link not opening, payment not reflecting,
    SMS or email not delivered, bulk upload errors, and API failures explained.
  keywords:
    - payment link not working payu
    - payu payment link troubleshooting
    - fix payment link error
    - payment not reflecting payu dashboard
    - payment link sms not delivered
    - payment link email not received
    - payu bulk upload error
    - payu payment link expired
    - payment link deactivated fix
    - payu api 401 unauthorized payment links
  robots: index
next:
  description: Explore related information and resources.
  pages:
    - slug: payment-links
      title: Payment Links
      type: basic
    - slug: create-a-payment-link
      title: Create a Payment Link
      type: basic
    - slug: manage-payment-links
      title: Manage Payment Links
      type: basic
---
{/* NEW CONTENT: Template E — Troubleshooting (V2 format) */}

<Banner
  isInline={true}
  message="This page helps you troubleshoot issues that occur after you create a Payment Link."
  color="#16C612"
  textColor="#ffffff"
  fontSize="14px"
  fontWeight="bold"
/>

<Callout icon="📘" theme="info">
  ### **Payment Links**

  Have not created a payment link yet? → [Create a Payment Link](doc:send-a-payment-link)
</Callout>

***

## Why Is My Customer's Link Not Opening?

<Accordion title="Check the Link Status First" icon="far fa-magnifying-glass">
  Open the [Payment Links Dashboard](https://onboarding.payu.in/) and find the link. Check the **Status** column:

  | Status          | What it Means                                                      | What to Do                                                   |
  | --------------- | ------------------------------------------------------------------ | ------------------------------------------------------------ |
  | **Active**      | Link should work                                                   | Check for device or browser issues.                          |
  | **Expired**     | Link has expired                                                   | Duplicate the link with a new expiry date                    |
  | **Deactivated** | Manually disabled                                                  | Reactivate the link if you still need to collect payments    |
  | **Paid**        | Max transactions reached or the customer has paid the full amount. | Create a new link if you want to collect additional payments |

  **If status is Active but the link still doesn't open:**

  - Ask the customer to try open in a different browser or clear their cache.
  - Check if the link URL was truncated when shared (common over SMS). You can copy the full URL from the Dashboard and resend it.
  - Confirm the link was not shared as a screenshot instead of the actual URL.
</Accordion>

***

## Why Is not the Payment Showing in My Dashboard?

<Accordion title="Payment Not Reflecting After Customer Paid" icon="far fa-clock">
  Follow these troubleshooting steps:

  1. Wait for 5–10 minutes: Dashboard updates are near-real-time but occasionally delayed.
  2. Check in the **Transactions** (not Payment Links) tab: The transaction may appear there before the link status updates.
  3. Search for the transactio&#x6E;**&#x20;**&#x75;sing th&#x65;**&#x20;**&#x61;mount or date.

  <Columns layout="fixed">
    <Column>
      **If the transaction appears in Transactions but the link status is not updated:**

      The payment is received. The link will update within 30 minutes. Contact <Anchor target="_blank" href="https://help.payu.in/query">PayU support</Anchor> with the transaction ID if it persists beyond an hour.
    </Column>
  </Columns>

  <Columns layout="fixed">
    <Column>
      **If the transaction does not appear anywhere:**

      The payment may have failed on the customer's bank side even if their account was debited. Banks sometimes auto-reverse such debits within 5–7 business days. Ask the customer to check their bank statement. If the debit was not reversed, raise a dispute with <Anchor target="_blank" href="https://help.payu.in/query">PayU support</Anchor> and provide the customer's bank reference number.
    </Column>
  </Columns>

  <Callout icon="📘" theme="info">
    ### **Webhooks**

    If you have configured webhooks, a missing webhook event is a reliable sign the payment did not complete on PayU's side.
  </Callout>
</Accordion>

***

## Why Did not My Customer Receive the SMS or Email?

<Accordion title="Notification Not Delivered" icon="far fa-envelope">
  Check these:

  1. Confirm the customer's phone or email was entered correctly. To verify, open the link **Details** view in the Dashboard and check the details under the **Customer Details&#x20;**&#x73;ection.&#x20;

     **You Can:** Refer to the <Anchor target="_blank" href="https://docs.payu.in/docs/manage-payment-links#what-can-i-do-with-a-payment-link-after-it-is-created">Edit Payment Link Details</Anchor>**&#x20;**&#x66;or steps to edit information if they are incorrect.
  2. Confirm the **Send via SMS** or **Send Email** toggles were turned on at the time of the link creation. Notifications fire once, at creation — they cannot be re-triggered for an existing link.

     **You can:&#x20;**<Anchor target="_blank" href="https://docs.payu.in/docs/manage-payment-links#what-can-i-do-with-a-payment-link-after-it-is-created">Share or resend the link</Anchor> to the customer.
  3. Ask the customer to:
     - Check their spam or junk folder (for email).
     - Check if DND (Do Not Disturb) is active on their number. DND blocks all promotional messages from all senders.

  <Callout icon="🚧" theme="warning">
    Notification status is visible in the link's **Details** view under `emailStatus` and `smsStatus`. If either shows "not opted", the notification was not configured at creation time.
  </Callout>
</Accordion>

***

## Why Did My Customer's Payment Fail at Checkout?

<Accordion title="Payment failed on the checkout page" icon="far fa-circle-xmark">
  Ask the customer: what payment method did they try, and what error message did they see?

  | Customer error                 | Likely cause                       | Fix                                                                |
  | ------------------------------ | ---------------------------------- | ------------------------------------------------------------------ |
  | "Transaction declined by bank" | Bank or card issuer declined       | Try a different card, or contact their bank                        |
  | "Invalid OTP" or "OTP expired" | OTP entry timeout or typo          | Try again with the correct OTP within the time limit               |
  | "Payment method not available" | Method not enabled on your account | Contact PayU to enable the payment method                          |
  | "Amount exceeds limit"         | Card or UPI daily limit reached    | Try a different payment method or contact their bank               |
  | Page stuck / spinning          | Poor network on customer's side    | Try on a stable connection, different browser, or different device |

  **If payment methods are missing from the checkout page:** Contact PayU support — certain methods require activation at the merchant account level.
</Accordion>

***

## How Do I Fix a Link with Wrong Details?

<Accordion title="Wrong amount, description, or customer — link cannot be edited" icon="far fa-pen-to-square">
  Payment Link configuration **cannot be edited after creation**.

  **Fix:**

  1. Go to the link → **Actions** → **Duplicate**.
  2. Correct the details in the new link creation panel.
  3. Click **Create and Send Payment Link**.
  4. Go back to the original link → **Actions** → **Disable** to deactivate it.
</Accordion>

***

## Why Did My Bulk Upload Fail?

<Accordion title="CSV upload errors" icon="far fa-file-csv">
  **Check the upload result:**

  1. Go to the **Bulk Uploads** tab in the Payment Links Dashboard.
  2. Find your upload and review the error rows.

  | Error                           | Cause                                            | Fix                                                                  |
  | ------------------------------- | ------------------------------------------------ | -------------------------------------------------------------------- |
  | "Duplicate invoice number"      | A link with that invoice number already exists   | Use a unique invoice number per row, or leave blank to auto-generate |
  | "Missing mandatory field"       | `subAmount` or `description` is empty            | Fill in all required columns                                         |
  | "Invalid date format"           | `expiryDate` not in `YYYY-MM-DD HH:MM:SS` format | Correct the date format                                              |
  | "Amount must be greater than 0" | Zero or negative `subAmount`                     | Enter a positive amount                                              |
</Accordion>

***

## Why Is My API Request Failing?

<Accordion title="API error codes and fixes" icon="far fa-code">
  | Error                                           | Cause                                                      | Fix                                                               |
  | ----------------------------------------------- | ---------------------------------------------------------- | ----------------------------------------------------------------- |
  | `401 Unauthorized`                              | Token expired or wrong scope                               | [Generate a new token](doc:api-auth-token) with the correct scope |
  | `400 — Invoice Number already exists`           | `invoiceNumber` reused                                     | Use a unique invoice number or omit it                            |
  | `400 — furl/surl not recognised`                | Wrong parameter names                                      | Use `failureUrl` and `successUrl`                                 |
  | `400 — expiry cannot be less than current date` | `expiryDate` in the past                                   | Set a future date in `YYYY-MM-DD HH:MM:SS`                        |
  | `404 — paymentLink not found`                   | Invoice number doesn't match any link for your merchant ID | Verify invoice number and `merchantId` header                     |
</Accordion>

***

## Still Stuck?

Collect this before contacting support: the Payment Link URL or invoice number, a transaction ID (if the customer attempted payment), the date and time of the issue, and a screenshot of any error message.

Contact PayU Support via the Dashboard **Help** section, or email `support@payu.in`.

***

## Related Pages

<Cards>
  <Card title="Send a Payment Link" href="doc:send-a-payment-link" icon="fa-paper-plane">
    Step-by-step creation guide.
  </Card>

  <Card title="Manage Payment Links" href="doc:manage-payment-links" icon="fa-list-check">
    Duplicate, deactivate, and re-share links.
  </Card>

  <Card title="Payment Links FAQs" href="doc:payment-links-faqs" icon="fa-circle-question">
    Common questions about Payment Links.
  </Card>
</Cards>
