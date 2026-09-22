---
title: FAQs (Frequently Asked Questions)
excerpt: >-
  Answers to common questions about PayU Payment Links — creation, limits,
  customisation, payment methods, security, and API usage.
deprecated: false
hidden: true
metadata:
  title: Payment Links FAQs | PayU Developer Docs
  description: >-
    Answers to common PayU Payment Links questions — how they work, expiry,
    partial payments, supported methods, API authentication, and token scopes.
  keywords:
    - payu payment links faq
    - payment link questions answers
    - payu payment link how it works
    - payment link partial payment faq
    - payment link expiry faq
    - payment link api faq
    - payu oauth token faq
    - payment link supported methods
    - payment link security payu
    - payu payment link limits
  robots: index
next:
  description: Explore related information and resources.
  pages:
    - slug: payment-links
      title: Payment Links
      type: basic
    - slug: manage-payment-links
      title: Manage Payment Links
      type: basic
    - slug: payment-links-errors-and-troubleshooting
      title: Errors and Troubleshooting
      type: basic
---
{/* EXISTING CONTENT: Move + Rewrite from payment-links-dashboard/faqs-payment-links.md (V2 format) */}

{/* NEW CONTENT: Additional questions added where original FAQ had gaps */}

<Banner
  isInline={true}
  message="Integration effort: No code or website required"
  color="#15C614"
  textColor="#ffffff"
  fontSize="14px"
  fontWeight="bold"
/>

***

## General

1. #### What is a payment link and how does it work?

<Accordion title="Answer" icon="fab fa-adn">
  A <Anchor target="_blank" href="doc:payment-links-overview">payment link</Anchor> is a secure, shareable URL that lets your customer pay you without visiting your website or app. You <Anchor target="_blank" href="https://docs.payu.in/docs/create-a-payment-link">create the link</Anchor> in the PayU Dashboard or via <Anchor target="_blank" href="https://docs.payu.in/reference/create-payment-links">API</Anchor>, share it over any channel such as email, SMS, WhatsApp. Your customer clicks it to pay on a PayU-hosted checkout page. Once paid, you receive a notification and the transaction appears in your Dashboard.
</Accordion>

***

2. #### Do I need a developer or any code to create a Payment Link?

<Accordion title="Answer" icon="fab fa-adn">
  No. Payment Links is a no-code product. You can <Anchor target="_blank" href="https://docs.payu.in/docs/create-a-payment-link">create</Anchor>, <Anchor target="_blank" href="https://docs.payu.in/docs/manage-payment-links#what-can-i-do-with-a-payment-link-after-it-is-created">share</Anchor>, and <Anchor target="_blank" href="https://docs.payu.in/docs/manage-payment-links">manage</Anchor> links entirely from the PayU Dashboard. The [Payment Links API](doc:api-create-share) is available for merchants who want to automate link creation inside their own systems, but it is optional.
</Accordion>

***

3. #### Which payment methods can customers use to make payments?

<Accordion title="Answer" icon="fab fa-adn">
  {/* EXISTING CONTENT: adapted from faqs-payment-links.md */}

  Customers can pay using payment methods enabled on your merchant accounts such as&#x20;

  - Credit/Debit cards (Visa, Mastercard, RuPay and Amex)
  - UPI (GPay, PhonePe, Paytm, etc.)
  - NetBanking (50+ banks)
  - Wallets (Paytm, Mobikwik and Freecharge)
  - EMI (no-cost and standard)
  - BNPL.&#x20;

  Contact <Anchor target="_blank" href="https://help.payu.in/query">PayU support</Anchor> to enable or disable specific methods.
</Accordion>

***

4. #### Are Payment Links secure?

<Accordion title="Answer" icon="fab fa-adn">
  {/* EXISTING CONTENT: adapted from faqs-payment-links.md */}

  Yes. PayU Payment Links are PCI DSS compliant. PayU uses advanced encryption and tokenisation to protect customer payment data. No card or bank details pass through your systems. The customer pays directly on PayU's hosted checkout page.
</Accordion>

***

## Creating and Configuring Links

1. #### Can I set a custom amount for each link?

<Accordion title="Answer" icon="fab fa-adn">
  Yes. Each link has its own amount field. You can also leave the amount flexible so the customer fills it in at checkout. It is useful for donations or open-ended collections.
</Accordion>

***

2. #### Can I collect customer information with the payment?

<Accordion title="Answer" icon="fab fa-adn">
  Yes. You can add standard fields (name, email, phone, address) and fully custom fields (any label, any type) to the checkout page. Refere to the <Anchor target="_blank" href="https://docs.payu.in/docs/create-a-payment-link#how-do-i-create-a-payment-link">Create a Payment Link</Anchor> page for more details.
</Accordion>

***

3. #### Can I set an expiry date to the payment link?

<Accordion title="Answer" icon="fab fa-adn">
  Yes. The default expiry is 1 year. You can set any future date during creation. Once expired, the link cannot accept payments. To extend expiry after the fact, use the [Cancel / Change Status API](doc:api-cancel-status), or <Anchor target="_blank" href="https://docs.payu.in/docs/manage-payment-links#what-can-i-do-with-a-payment-link-after-it-is-created">duplicate</Anchor> the link from the Dashboard with a new expiry date.
</Accordion>

***

4. #### Can I limit how many times a payment link can be used?

<Accordion title="Answer" icon="fab fa-adn">
  Yes. Use the **Max Transactions** field when <Anchor target="_blank" href="https://docs.payu.in/docs/create-a-payment-link">creating the link</Anchor>. Leave it blank for unlimited. Once the limit is reached, the link automatically deactivates.
</Accordion>

***

5. #### Can I edit a payment link after creating it?

<Accordion title="Answer" icon="fab fa-adn">
  You cannot edit a link's amount, description, or configuration from the Dashboard after creation. To correct a mistake, <Anchor target="_blank" href="https://docs.payu.in/docs/manage-payment-links#what-can-i-do-with-a-payment-link-after-it-is-created">duplicate</Anchor> the link with the right details, then deactivate the original. Via API, you can update `active` status, `expiryDate`, `subAmount`, `tax`, `shippingCharge`, and `isPartialPaymentAllowed` using the [Cancel / Change Status API](doc:api-cancel-status).
</Accordion>

***

6. #### Can a customer pay in instalments?

<Accordion title="Answer" icon="fab fa-adn">
  Yes, if you enable **Partial Payment** on the link. The customer can pay any amount less than the total. You can specify a minimum amount a customer can pay. For structured auto-debiting, use [Recurring Payments](doc:recurring-payments).
</Accordion>

***

7. #### How many payment links can I create?

<Accordion title="Answer" icon="fab fa-adn">
  There is no hard limit on the number of payment links. For creating hundreds at once, use the [Bulk Upload](doc:manage-payment-links) feature or the [Create Payment Link API](doc:api-create-share).
</Accordion>

***

## Sharing and Notifications

1. #### How do I share a payment link with a customer?

<Accordion title="Answer" icon="fab fa-adn">
  You can copy the link URL from the Dashboard and share it over any channel (WhatsApp, email, etc.), send it directly from the Dashboard via SMS or email (enter the customer's phone/email at creation and toggle notifications on), or <Anchor target="_blank" href="https://docs.payu.in/docs/manage-payment-links#what-can-i-do-with-a-payment-link-after-it-is-created">reshare</Anchor> an existing link from **Actions > Share**.
</Accordion>

***

2. #### Can the same link be shared with multiple customers?

<Accordion title="Answer" icon="fab fa-adn">
  Yes. A single link can be opened and paid by different customers, up to the Max Transactions limit (unlimited by default). For a personalised link pre-filled with a specific customer's details, create one link per customer.
</Accordion>

***

## Payments and Reconciliation

1. #### How will I know when a customer has paid?

<Accordion title="Answer" icon="fab fa-adn">
  The link status in the Dashboard changes to **Paid** (or **Active** with a non-zero `totalRevenue` for partial-payment links). The transaction appears in the **Transactions&#x20;**&#x74;ab in the Dashboard. If you have webhooks configured, you receive a real-time `payment.success` event.
</Accordion>

***

2. #### What happens if a customer's payment fails?

<Accordion title="Answer" icon="fab fa-adn">
  The link remains **Active** and the customer can retry either immediately or later. A failed attempt does not count against the Max Transactions limit.
</Accordion>

***

3. #### Can I issue a refund for a payment made via a payment link?

<Accordion title="Answer" icon="fab fa-adn">
  Yes. Find the transaction in the **Transactions&#x20;**&#x74;ab and initiate a refund from there. The refund process is the same regardless of how the payment was collected.
</Accordion>
