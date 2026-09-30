---
title: Manage Payment Buttons
excerpt: >-
  View, filter, turn off, and download records for your Payment Buttons — all
  from the PayU Dashboard.
deprecated: false
hidden: true
metadata:
  title: Manage PayU Payment Buttons — Dashboard Guide | Developer
  description: >-
    View payments, filter, export records, and manage your PayU Payment Buttons
    from the Dashboard. No code needed.
  keywords:
    - manage payment buttons payu
    - view payment button transactions
    - filter payment buttons dashboard
    - export payment button history
    - turn off payment button payu
    - payment button records download
    - payu dashboard payment buttons
  robots: index
next:
  description: Explore related information and resources.
---
{/* NEW CONTENT */}

{/* EXISTING CONTENT: adapted from payment-buttons-dashboard.md */}

<Banner
  isInline={true}
  message="Integration effort: No code or website developer required"
  color="#15C614"
  textColor="#ffffff"
  fontSize="14px"
  fontWeight="bold"
/>

You can manage your payment buttons from the PayU Dashboard after they are created and live on your website.

***

## How Do I Access My Payment Buttons?

To open payment buttons: log in to [PayU Dashboard](https://onboarding.payu.in/) and click **Payment Buttons** under **Payment Tools**.


<Image src="https://files.readme.io/ac2a025ae66a2cd9b63d9fa8f3a9ac924b697623f07dc73137cd1b69d8215ce0-Screenshot_2026-09-30_at_10.33.20_AM.png" align="center" caption="Access Payment Buttons" border={true} />


***

## What Can I Do With a Payment Button After It Is Created?

You can perform the following actions after a button is created:

- View Payment Button Details
- Edit Payment Button Details
- Delete a Payment Button

### View Payment Button Details

<Accordion title="Steps to View Button Details" icon="far fa-rectangle-list">
  To see the details and payment history for a payment button:

  1. Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/">PayU Dashboard</Anchor> and click **Payment Buttons** under **Payment Tools**.

     <Image src="https://files.readme.io/b11382e235cabbde457cdb61efa569f6680bb561c03b067c79c540f425e7a4f4-image.png" align="center" caption="Access Payment Buttons" border={true} />


  A list of all your payment buttons is displayed with the following information:

  - **Created On**
  - **Button ID**
  - **Button Text**
  - **Item Name**
  - **Amount**
  - **Actions:&#x20;**&#x43;ontains buttons to perform varios actions.

  2. Click the button you want to view.

  The details are split into the following sections:

  <Accordion title="Button Details" icon="fad fa-tablet-button">
    The upper half of the **Button Details&#x20;**&#x70;age displays the following information:

    - **Button ID:&#x20;**&#x54;he unique button ID.

    - **Created On:&#x20;**&#x54;he date and time on which the payment button was created.

    - **Button Text:&#x20;**&#x54;he button text you have selected while creating the payment button.

    - **Action Buttons:&#x20;**&#x41;ction buttons to edit, duplicate and view the code of the payment button.

      <Image src="https://files.readme.io/c5ce7b7324ea3e725ccaefce214c591f5d59fcddbc1b3b6fd787e94a9249cfe8-Screenshot_2026-09-30_at_11.35.04_AM.png" align="center" caption="Payment Button Details" border={true} />

  </Accordion>

  <Accordion title="Details and Transactions" icon="fad fa-money-bills">
    <Tabs>
      <Tab title="Details">
        The **Details&#x20;**&#x74;ab displays the following information:

        - **Button Text:** The label on the button — Buy Now, Pay Now, Book Now, or Donate Now.
        - **Item Name:** The product or purpose description shown to the customer at checkout.
        - **Amount:** The fixed amount, or blank if the customer enters it themselves.
        - **Colour and Size:** The visual settings for the button on your website.
        - **Status:** Whether the button is active or turned off.
        - **Button Code:** The code you added to your website. Copy it from here if you need to add it to another page.
      </Tab>

      <Tab title="Transactions">
        Every payment made through this button is listed here:

        - **Date:** When the payment was made.
        - **Transaction ID:** PayU's unique ID for each payment. You can copy it.
        - **Customer Email**
        - **Amount:** How much was paid.
        - **Status:** Whether the payment went through successfully.
      </Tab>
    </Tabs>
  </Accordion>
</Accordion>

<Accordion title="Turn Off a Button" icon="far fa-ban">
  Turning off a button stops any further payments through it. Anyone who clicks it on your website will see a message that it is no longer active.

  To turn off a button:

  1. Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/">PayU Dashboard</Anchor> and click **Payment Buttons** under **Payment Tools**.


  <Image src="https://files.readme.io/a494bb1de682ae83ec3d1023e1e13dfb65e02db0ef5332ca52b6e85232638c63-Screenshot_2025-06-02_at_7.09.40_PM.png" align="center" caption="Payment Buttons list" border={true} />


  2. Click the menu icon next to the button you want to turn off and click **Disable**.
  3. Click **Yes** in the confirmation window.

  The button status changes to **Inactive**.

  <Callout icon="🚧" theme="warning">
    ### **Watch Out!**

    Once a button is turned off, it cannot be turned back on. If you need to accept payments again for the same product or purpose, create a new button and add it to your website.
  </Callout>
</Accordion>

***

## How Do I Search for a Button?

You can filter the payment buttons list using the following options:

<Accordion title="Filter by Button Type" icon="far fa-filter">
  To filter your buttons by type:

  1. Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/">PayU Dashboard</Anchor> and click **Payment Buttons** under **Payment Tools**.


  <Image src="https://files.readme.io/a494bb1de682ae83ec3d1023e1e13dfb65e02db0ef5332ca52b6e85232638c63-Screenshot_2025-06-02_at_7.09.40_PM.png" align="center" caption="Payment Buttons list" border={true} />


  2. Click the **Filter** drop-down at the top of the list and select the button types you want to see.
  3. Click **Apply** to filter the list.


  <Image src="https://files.readme.io/aa8017f76337f733c85c604f5405b654e85a9d2ab165d9b60e1f34dc716fda54-Screenshot_2025-06-02_at_7.25.33_PM.png" align="center" caption="Filter by button type" border={true} />


  4. To remove the filter and see all buttons again, click **Reset** inside the filter panel.
</Accordion>

<Accordion title="Filter by Date" icon="far fa-calendar">
  To filter your buttons by when they were created:

  1. Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/">PayU Dashboard</Anchor> and click **Payment Buttons** under **Payment Tools**.


  <Image src="https://files.readme.io/a494bb1de682ae83ec3d1023e1e13dfb65e02db0ef5332ca52b6e85232638c63-Screenshot_2025-06-02_at_7.09.40_PM.png" align="center" caption="Payment Buttons list" border={true} />


  2. Click the **Past 1 Year** drop-down at the top of the list and select a time period:
     - Today
     - Yesterday
     - Past 7 days
     - Past 30 days
     - Past 1 year
     - Custom Range

  3. For a custom range, pick a start and end date and click **Apply**.


  <Image src="https://files.readme.io/aa8017f76337f733c85c604f5405b654e85a9d2ab165d9b60e1f34dc716fda54-Screenshot_2025-06-02_at_7.25.33_PM.png" align="center" caption="Date filter on the Payment Buttons list" border={true} />

</Accordion>

***

## How Do I Download My Payment Button Records?

<Accordion title="Export Payment Button Records" icon="far fa-download">
  To download payment button records:

  1. Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/">PayU Dashboard</Anchor> and click **Payment Buttons** under **Payment Tools**.


  <Image src="https://files.readme.io/a494bb1de682ae83ec3d1023e1e13dfb65e02db0ef5332ca52b6e85232638c63-Screenshot_2025-06-02_at_7.09.40_PM.png" align="center" caption="Payment Buttons list" border={true} />


  2. Click the **Download** drop-down at the top of the list and select a format:

  | Format   | What it includes                            |
  | -------- | ------------------------------------------- |
  | **CSV**  | All payment button records as a spreadsheet |
  | **XLSX** | The same records in Excel format            |


  <Image src="https://files.readme.io/7e99a0e3631c410b75ab966f9d02613852a8565cb802ce7be22f23347bcddaab-Screenshot_2025-06-02_at_7.26.33_PM.png" align="center" caption="Download menu for payment button records" border={true} />


  3. Click **Download** on the pop-up when your report is ready.

  <Callout icon="📘" theme="info">
    You can also send the report to an email address. In the pop-up, enter one or more email addresses separated by commas and click **Share**.
  </Callout>
</Accordion>

***

## Next Steps

<Cards>
  <Card title="Add a Payment Button" href="doc:add-a-payment-button" icon="far fa-plus">
    Create a new payment button and add it to your website.
  </Card>

  <Card title="Customize Your Button" href="doc:customize-payment-button" icon="fa-sliders">
    Set the button text, colour, amount, and redirect pages before you create it.
  </Card>

  <Card title="Payment Button Troubleshooting" href="doc:payment-button-troubleshooting" icon="fa-wrench">
    Fix issues with buttons not showing, payments not going through, or records not appearing.
  </Card>

  <Card title="Payment Button FAQs" href="doc:payment-button-faqs" icon="fa-circle-question">
    Common questions about Payment Buttons.
  </Card>
</Cards>
