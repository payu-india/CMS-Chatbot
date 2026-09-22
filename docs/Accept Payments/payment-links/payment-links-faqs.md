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

<Accordion title="Are Payment Links secure?" icon="far fa-shield">
  {/* EXISTING CONTENT: adapted from faqs-payment-links.md */}

  Yes. PayU Payment Links are PCI DSS compliant. PayU uses advanced encryption and tokenisation to protect customer payment data. No card or bank details pass through your systems — the customer pays directly on PayU's hosted checkout page.
</Accordion>

***

## Creating and Configuring Links

<Accordion title="Can I set a custom amount for each link?" icon="far fa-money-bill">
  Yes. Each link has its own amount field. You can also leave the amount flexible so the customer fills it in at checkout — useful for donations or open-ended collections.
</Accordion>

<Accordion title="Can I collect customer information with the payment?" icon="far fa-list-check">
  Yes. You can add standard fields (name, email, phone, address) and fully custom fields (any label, any type) to the checkout page. See [Payment Link Options](doc:payment-link-options) for details.
</Accordion>

<Accordion title="Can I set an expiry date?" icon="far fa-calendar-xmark">
  Yes. The default expiry is 1 year. You can set any future date during creation. Once expired, the link cannot accept payments. To extend expiry after the fact, use the [Cancel / Change Status API](doc:api-cancel-status), or duplicate the link from the Dashboard with a new expiry date.
</Accordion>

<Accordion title="Can I limit how many times a link can be used?" icon="far fa-hashtag">
  Yes — use the **Max Transactions** field when creating the link. Leave it blank for unlimited. Once the limit is reached, the link automatically deactivates.
</Accordion>

<Accordion title="Can I edit a payment link after creating it?" icon="far fa-pen-to-square">
  You cannot edit a link's amount, description, or configuration from the Dashboard after creation. To correct a mistake, duplicate the link with the right details, then deactivate the original. Via API, you can update `active` status, `expiryDate`, `subAmount`, `tax`, `shippingCharge`, and `isPartialPaymentAllowed` using the [Cancel / Change Status API](doc:api-cancel-status).
</Accordion>

<Accordion title="Can a customer pay in instalments?" icon="far fa-money-bill-wave">
  Yes, if you enable **Partial Payment** on the link. The customer can pay any amount less than the total — you cannot specify a minimum. For structured auto-debiting, use [Recurring Payments](doc:recurring-payments).
</Accordion>

<Accordion title="How many payment links can I create?" icon="far fa-infinity">
  There is no hard limit on the number of payment links. For creating hundreds at once, use the [Bulk Upload](doc:manage-payment-links) feature or the [Create Payment Link API](doc:api-create-share).
</Accordion>

***

## Sharing and Notifications

<Accordion title="How do I share a payment link with a customer?" icon="far fa-share">
  You can copy the link URL from the Dashboard and share it over any channel (WhatsApp, email, etc.), send it directly from the Dashboard via SMS or email (enter the customer's phone/email at creation and toggle notifications on), or reshare an existing link from **Actions > Share**.
</Accordion>

<Accordion title="Can the same link be shared with multiple customers?" icon="far fa-users">
  Yes — a single link can be opened and paid by different customers, up to the Max Transactions limit (unlimited by default). For a personalised link pre-filled with a specific customer's details, create one link per customer.
</Accordion>

***

## Payments and Reconciliation

<Accordion title="How will I know when a customer has paid?" icon="far fa-bell">
  The link status in the Dashboard changes to **Paid** (or **Active** with a non-zero `totalRevenue` for partial-payment links). The transaction appears in **Transactions** in the Dashboard. If you have webhooks configured, you receive a real-time `payment.success` event → [Webhooks: Receive & Verify](doc:receive-and-verify-a-webhook)
</Accordion>

<Accordion title="What happens if a customer's payment fails?" icon="far fa-rotate-left">
  The link remains **Active** and the customer can try again — either immediately or later. A failed attempt does not count against the Max Transactions limit.
</Accordion>

<Accordion title="Can I issue a refund for a payment made via a payment link?" icon="far fa-money-bill-transfer">
  Yes. Find the transaction in **Transactions** and initiate a refund from there. The refund process is the same regardless of how the payment was collected.
</Accordion>

***

## API Usage

<Accordion title="Do I need a special API key for Payment Links?" icon="far fa-key">
  {/* EXISTING CONTENT: adapted from faqs-payment-links.md */}

  Payment Links APIs use **OAuth2 Bearer token** authentication — separate from your standard PayU `key` + `salt` + SHA-512 hash. You need a **Client ID** and **Client Secret** from the Dashboard to get a token.

  → [Authentication (Token)](doc:api-auth-token)
</Accordion>

<Accordion title="What scopes does each API operation require?" icon="far fa-lock">
  {/* EXISTING CONTENT: adapted from faqs-payment-links.md */}

  | Operation              | Required scope         |
  | ---------------------- | ---------------------- |
  | Create a payment link  | `create_payment_links` |
  | Share a payment link   | `read_payment_links`   |
  | Fetch a single link    | `read_payment_links`   |
  | Fetch all links        | `read_payment_links`   |
  | Update / cancel a link | `update_payment_links` |

  Request multiple scopes in one token by separating them with spaces: `create_payment_links update_payment_links read_payment_links`.
</Accordion>

<Accordion title="How long is a token valid, and can I reuse it?" icon="far fa-clock">
  Tokens expire after the number of seconds in the `expires_in` field (typically 3600 = 1 hour). A token is valid for multiple API calls until it expires or is revoked — you do not need a new token per request. Generate a new token before it expires; do not hard-code tokens in your application.
</Accordion>

<Accordion title="Why am I getting 'furl/surl not recognised'?" icon="far fa-triangle-exclamation">
  {/* EXISTING CONTENT: adapted from faqs-payment-links.md */}

  The Payment Links API does not use the shorthand `furl` and `surl`. Use `failureUrl` and `successUrl` instead.
</Accordion>

<Accordion title="Why am I getting 'Invoice Number already exists'?" icon="far fa-triangle-exclamation">
  Each payment link must have a unique `invoiceNumber` within your merchant account. Either use a different value, or omit `invoiceNumber` entirely — PayU will auto-generate a unique one.
</Accordion>

***

## Related Pages

<Cards>
  <Card title="Payment Links Overview" href="doc:payment-links-overview" icon="fa-circle-info">
    What Payment Links is, use cases, and how it works.
  </Card>

  <Card title="Payment Links Troubleshooting" href="doc:payment-links-troubleshooting" icon="fa-wrench">
    Fix issues with links not working, payments not reflecting, and API errors.
  </Card>

  <Card title="Payment Link Options" href="doc:payment-link-options" icon="fa-sliders">
    Full reference for all configuration options.
  </Card>
</Cards>
