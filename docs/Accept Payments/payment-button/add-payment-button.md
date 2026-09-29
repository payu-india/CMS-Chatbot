---
title: Add a Payment Button
excerpt: >-
  Create a payment button in the PayU Dashboard, configure it, and embed the
  generated snippet on your website or blog.
deprecated: false
hidden: true
metadata:
  title: Add a PayU Payment Button to Your Website | Developer Docs
  description: >-
    Create a PayU payment button in the Dashboard, configure label, amount,
    colour, and redirect URLs, then copy the embed snippet to your website.
  keywords:
    - add payment button payu
    - create payment button dashboard
    - embed payment button website
    - payu buy now button
    - payu donate now button
    - payment button embed code
    - payu payment button quickstart
  robots: index
next:
  description: Explore related information and resources.
  pages:
    - slug: payment-button
      title: Payment Button
      type: basic
---
{/* EXISTING CONTENT: adapted from payment-buttons-dashboard.md */}

<Banner
  isInline={true}
  message="Integration effort: No code or website developer required"
  color="#15C614"
  textColor="#ffffff"
  fontSize="14px"
  fontWeight="bold"
/>

{/* NEW CONTENT */}

<Callout icon="📘" theme="info">
  **What you need:** An active PayU merchant account and a website or page editor where you can paste HTML.
</Callout>

***

## Step 1 — Open the Payment Buttons Dashboard

{/* EXISTING CONTENT: adapted from payment-buttons-dashboard.md */}

1. Log in to the [PayU Dashboard](https://onboarding.payu.in/).
2. From the left sidebar, go to **Payment Tools → Payment Buttons**.

   All existing buttons are listed here.


<Image src="https://files.readme.io/a494bb1de682ae83ec3d1023e1e13dfb65e02db0ef5332ca52b6e85232638c63-Screenshot_2025-06-02_at_7.09.40_PM.png" align="center" caption="Payment Buttons list" border={true} />


3. Click **Create New Button** at the top-right corner.

   The **Create New Payment Button** page opens.


<Image src="https://files.readme.io/dace80a25807f722b25d1ee7054db2836a7a3d44d97cb7ca82f67664bdbfd54b-Screenshot_2025-06-02_at_7.09.15_PM.png" align="center" caption="Create New Payment Button" border={true} />


***

## Step 2 — Configure the Button

{/* EXISTING CONTENT: adapted from payment-buttons-dashboard.md */}

1. Choose a **Button Text** label from the drop-down:
   - Buy Now
   - Pay Now
   - Book Now
   - Donate Now

2. Enter a description in the **Item Name** field — this is shown to the customer on the checkout page as the product or purpose.

3. Enter the amount in the **Amount** field.

<Callout icon="📘" theme="info">
  Leave **Amount** blank if you want customers to enter the amount themselves at checkout — useful for donations or tip jars.
</Callout>

4. Select the **button colour** — choose from the preset palette or use the colour picker for a custom hex value.

5. Select the **button size** that fits your page layout:
   - Small
   - Medium
   - Large

***

## Step 3 — Configure Checkout Fields (Optional)

{/* EXISTING CONTENT: adapted from payment-buttons-dashboard.md */}

Add extra fields to the checkout page to collect information from customers before they pay.

1. Scroll to the **Custom Details** section.


<Image src="https://files.readme.io/b3a27b5d2959197102e56442a3f0fa6054486c1db2caba39ba45c7bbab504f4f-Screenshot_2025-06-04_at_12.32.20_PM.png" align="center" width="250px" caption="Custom Details section" border={true} />


2. Toggle on any standard fields you want to collect: **Customer Name**, **Customer Address**, **Customer Email**, **Customer Mobile**.

3. To add a custom field, click **Add Fields** and fill in:

| Field             | What to enter                                           |
| ----------------- | ------------------------------------------------------- |
| Field Type        | Text, Calendar, or Drop-down                            |
| Field Name        | The label the customer sees on the checkout page        |
| Mark as mandatory | Toggle on to require this field before payment proceeds |


<Image src="https://files.readme.io/1eb6333ecf79f41c3bb978bd2c289d2af3822688df83f22b10edda2199e93a21-Screenshot_2025-06-04_at_12.33.44_PM.png" align="center" width="312px" caption="Add custom field" border={true} />


4. Click **Add Field** to save each field.


<Image src="https://files.readme.io/865616d7519cf08e3ca37a1583db494fb638d457de658d32e0a157f9309388ac-Screenshot_2025-06-04_at_12.37.53_PM.png" align="center" caption="Custom fields displayed on the PayU checkout page" border={true} />


***

## Step 4 — Set Redirect URLs and Generate

{/* EXISTING CONTENT: adapted from payment-buttons-dashboard.md */}

1. Scroll down to the **Advanced Options** section.


<Image src="https://files.readme.io/414d861556b165c6f6065aa4eebc25ecbc543e74e4ba08a1d6ab5fc5d7ff4fbe-Screenshot_2025-06-02_at_7.22.41_PM.png" align="center" width="412px" caption="Advanced options — redirect URLs" border={true} />


2. Enter your redirect URLs:

| URL             | When it is used                                                  |
| --------------- | ---------------------------------------------------------------- |
| **Success URL** | Customer is redirected here after a successful payment           |
| **Cancel URL**  | Customer is redirected here if they cancel or close the checkout |
| **Failure URL** | Customer is redirected here if the payment fails                 |

{/* NEW CONTENT */}

<Callout icon="🚧" theme="warning">
  Redirect URLs are optional but strongly recommended. Without them, customers land on a default PayU confirmation page after payment — they won't return to your website automatically.
</Callout>

{/* EXISTING CONTENT: adapted from payment-buttons-dashboard.md */}

3. Click **Generate Button**.

   PayU generates your embed snippet.

***

## Step 5 — Copy and Embed the Snippet

{/* NEW CONTENT */}

1. Copy the generated HTML snippet.
2. Paste it into your website wherever you want the button to appear:
   - In your page builder's HTML block (WordPress, Wix, Squarespace, Webflow)
   - Directly into your page's `<body>` HTML
   - In a blog post's HTML editor

The button renders immediately. No server setup or further configuration is required.

<Callout icon="📘" theme="info">
  The embed snippet contains your PayU merchant key. Each button has a unique snippet — do not reuse snippets across different buttons with different configurations.
</Callout>

***

## What Happens Next

{/* NEW CONTENT */}

When a customer clicks the button:

1. PayU's hosted checkout page opens.
2. The customer selects a payment method and completes the payment.
3. PayU redirects them to your **Success URL** (or **Failure URL** if the payment fails).
4. The transaction appears in your **Transactions** tab in the PayU Dashboard.
5. Funds are settled to your bank on the standard settlement cycle.

For real-time payment notifications, configure a webhook under **Settings → Webhooks** in the Dashboard. → [Webhooks for Payments](doc:webhooks)

***

## Next Steps

<Cards>
  <Card title="Customize Payment Button" href="doc:customize-payment-button" icon="fa-sliders">
    Change colours, size, amount type, and redirect URLs on an existing button.
  </Card>

  <Card title="Payment Button Troubleshooting" href="doc:payment-button-troubleshooting" icon="fa-wrench">
    Button not showing on your page? Fix common embedding issues.
  </Card>

  <Card title="Manage Payment Buttons" href="doc:add-a-payment-button" icon="fa-list-check">
    Filter, export, and review your existing buttons.
  </Card>
</Cards>
