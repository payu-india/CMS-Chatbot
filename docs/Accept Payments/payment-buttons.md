---
title: Payment Button
deprecated: false
hidden: true
metadata:
  robots: index
---
{/* NEW CONTENT */}

<Banner
  isInline={true}
  message="Integration effort: No code or website developer required"
  color="#15C614"
  textColor="#ffffff"
  fontSize="14px"
  fontWeight="bold"
/>

A Payment Button is a small widget you embed directly on your website or blog. Visitors click it, pay on PayU's hosted checkout page, and are redirected back to your site — all without you writing a single line of payment code.

***

## What Is a Payment Button?

{/* EXISTING CONTENT: adapted from payment-buttons-dashboard.md */}

PayU generates an HTML embed snippet in the Dashboard. You paste it anywhere on your website — a product page, a blog sidebar, a fundraising page — and it renders as a clickable button. You configure the button label, amount, colour, and size; PayU handles the rest.


<Image src="https://files.readme.io/a494bb1de682ae83ec3d1023e1e13dfb65e02db0ef5332ca52b6e85232638c63-Screenshot_2025-06-02_at_7.09.40_PM.png" align="center" caption="Payment Buttons list in the PayU Dashboard" border={true} />


***

## When Should I Use a Payment Button?

{/* NEW CONTENT */}

| Use case                            | Example                                                                      |
| ----------------------------------- | ---------------------------------------------------------------------------- |
| **Single product / service**        | "Buy this e-book — ₹299" button on a blog post                               |
| **Donation or tip jar**             | "Support us" button with a variable amount the visitor fills in              |
| **Event registration**              | "Book your seat — ₹500" on an event landing page                             |
| **Quick checkout on a static site** | Embed on a website builder (WordPress, Wix, Squarespace) without a full cart |

***

## How Is It Different from a Payment Link?

{/* NEW CONTENT */}

|                           | Payment Button                                         | Payment Link                                                  |
| ------------------------- | ------------------------------------------------------ | ------------------------------------------------------------- |
| **How it's shared**       | Embedded on a webpage                                  | Shared via SMS, email, or WhatsApp                            |
| **Where customer pays**   | Clicks button → PayU checkout opens in-page or new tab | Clicks link → PayU checkout page                              |
| **Best for**              | Websites and blogs with a fixed buying context         | One-off collections, invoices, or customers without a website |
| **Technical requirement** | Paste embed code on your site                          | None — share the URL                                          |

Both products use PayU's hosted checkout page and support the same payment methods.

***

## How It Works

{/* NEW CONTENT */}

<Steps>
  <Step title="Create the button in the Dashboard">
    Go to **Payment Tools → Payment Buttons → Create New Button**. Configure the label, amount, colour, and any custom checkout fields.
  </Step>
  <Step title="Copy the embed snippet">
    Click **Generate Button**. PayU produces a short HTML snippet.
  </Step>
  <Step title="Paste it on your website">
    Copy the snippet and paste it into your website's HTML or page editor. The button renders immediately — no further setup required.
  </Step>
  <Step title="Customer clicks and pays">
    Your visitor clicks the button and completes payment on PayU's hosted checkout page. They are redirected to your Success or Failure URL once done.
  </Step>
  <Step title="You receive the payment">
    The transaction appears in your PayU Dashboard under **Transactions**. Funds are settled to your bank account on the standard settlement cycle.
  </Step>
</Steps>

***

## What Do I Need?

{/* NEW CONTENT */}

- A PayU merchant account (active and KYC-verified)
- A website, blog, or page builder where you can paste HTML

You do not need a developer, a server, or any API integration.

***

## Next Steps

{/* NEW CONTENT */}

<Cards>
  <Card title="Add a Payment Button" href="doc:add-a-payment-button" icon="fa-circle-plus">
    Step-by-step guide to creating and embedding your first button.
  </Card>

  <Card title="Customize Payment Button" href="doc:customize-payment-button" icon="fa-sliders">
    Configure colours, size, amounts, redirect URLs, and custom fields.
  </Card>

  <Card title="Payment Button FAQs" href="doc:payment-button-faqs" icon="fa-circle-question">
    Common questions about Payment Buttons.
  </Card>

  <Card title="Payment Links Overview" href="doc:payment-links-overview" icon="fa-link">
    Need to share a payment request instead of embedding a button? Use Payment Links.
  </Card>
</Cards>
