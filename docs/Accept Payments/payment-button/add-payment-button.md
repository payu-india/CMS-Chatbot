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

{/* NEW CONTENT */}

<Banner
  isInline={true}
  message="Integration effort: No code or website developer required"
  color="#15C614"
  textColor="#ffffff"
  fontSize="14px"
  fontWeight="bold"
/>

Add a payment button to your website or blog from the PayU Dashboard in just a few minutes without any code.

***

## What All I Need?

<Cards>
  <Card title="A PayU Merchant Account" icon="far fa-table-cells-column-unlock">
    <Columns layout="fixed">
      <Column>
        <Anchor target="_blank" href="doc:set-up-your-account">Set up your account</Anchor> if you have not already done so.
      </Column>
    </Columns>
  </Card>

  <Card title="A Website or Page Builder" icon="far fa-pager">
    Any website where you can add content to your pages — WordPress, Wix, Squarespace, or any site with a page editor.
  </Card>
</Cards>

***

## How Do I Add a Payment Button?

To add a payment button:

<Accordion title="1. Open Payment Buttons on the Dashboard" icon="far fa-grid-2">
  1. Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/">PayU Dashboard</Anchor>.
  2. Expand **Payment Tools&#x20;**&#x61;nd clic&#x6B;**&#x20;Payment Links&#x20;**&#x64;isplayed in the left navigation.

  All your existing buttons are listed here.


  <Image src="https://files.readme.io/e1baadd4cfb07131a0a41849f9b4f824cda27ee5d1f9129d458a44ecf4cfcc12-Screenshot_2026-09-29_at_3.41.17_PM.png" align="center" caption="Access Payment Buttons" border={true} />

</Accordion>

<Accordion title="2. Create a New Payment Button" icon="far fa-plus">
  1. Click **Create New Button** displayed at the top-right corner of the page.

     The **Create New Payment Button** page is displayed.


  <Image src="https://files.readme.io/dace80a25807f722b25d1ee7054db2836a7a3d44d97cb7ca82f67664bdbfd54b-Screenshot_2025-06-02_at_7.09.15_PM.png" align="center" caption="Create New Payment Button Page" border={true} />


  2. Provide these **Button Details** to set up how your button looks and works:
     <Table>
       <thead>
         <tr>
           <th>
             Field
           </th>

           <th>
             Description
           </th>
         </tr>
       </thead>

       <tbody>
         <tr>
           <td>
             **Button Text**
           </td>

           <td>
             The text displayed on the button . Choose any of these text from the drop-down:

             - **Buy Now**
             - **Pay Now**
             - **Book Now**
             - **Donate Now**
           </td>
         </tr>

         <tr>
           <td>
             **Item Name**<br />_Required_
           </td>

           <td>
             Enter a short description of the product or service. This is shown to the customer on the payment page
           </td>
         </tr>

         <tr>
           <td>
             **Amount**
           </td>

           <td>
             Enter the amount you want to collect. You can leave blank to let your customer type in the amount
           </td>
         </tr>

         <tr>
           <td>
             **Colour**
           </td>

           <td>
             Choose a colour from the palette or enter a custom colour
           </td>
         </tr>

         <tr>
           <td>
             **Size**
           </td>

           <td>
             The size of the button. Choose any of these from the drop-down:&#x20;

             - **Small**
             - **Medium**
             - **Large**
           </td>
         </tr>
       </tbody>
     </Table>

     <Image src="https://files.readme.io/da83ac123dfde2852f1aae8a044448c59baf4b4fb0b4fe10a0fedc2a4f786bd6-Screenshot_2026-09-29_at_4.14.23_PM.png" align="center" caption="Add Button Details" border={true} />

</Accordion>

<Accordion title="3. Add Checkout Fields (Optional)" icon="far fa-list-check">
  Add custom fields to collect information from your customer before they pay.

  1. Scroll to the **Custom Details** section and switch on any of the ready-made fields you want to collect:
     - **Customer Name**
     - **Customer Address**
     - **Customer Email**
     - **Customer Mobile**

     <Image src="https://files.readme.io/b1640075e80da6845b2db91376ddc70cf909ac9ebed3f6ed33230fcfe1387586-Screenshot_2026-09-29_at_4.12.16_PM.png" align="center" caption="Add Custom Detials" border={true} />

  2. To add a field of your own, click **Add Fields** and fill in:

  | Field                 | What to Enter                                             |
  | --------------------- | --------------------------------------------------------- |
  | **Field Type**        | Text, Calendar, or Drop-down                              |
  | **Field Name**        | The question or label your customer will see              |
  | **Mark as mandatory** | Switch on if the customer must fill this in before paying |


  <Image src="https://files.readme.io/85ce648929644ea85ad3a4474b95e6b6ad10df34254b6e1e49beeb132be6321c-Screenshot_2026-09-29_at_4.16.51_PM.png" align="center" width="312px" caption="Add Your Own Field" border={true} />


  4. Click **Add Field** to save each field.
</Accordion>

<Accordion title="5. Add Redirect Pages (Optional)" icon="far fa-arrow-right-from-bracket">
  Under **Advanced Options**, you can tell PayU where to send your customer after they pay:

  | Page            | When it is used                                                           |
  | --------------- | ------------------------------------------------------------------------- |
  | **Success URL** | Your customer is taken here after a successful payment                    |
  | **Cancel URL**  | Your customer is taken here if they close the payment page without paying |
  | **Failure URL** | Your customer is taken here if the payment is unsuccessful                |


  <Image src="https://files.readme.io/414d861556b165c6f6065aa4eebc25ecbc543e74e4ba08a1d6ab5fc5d7ff4fbe-Screenshot_2025-06-02_at_7.22.41_PM.png" align="center" width="412px" caption="Add Redirect URLs" border={true} />


  <Callout icon="📘" theme="info">
    ### **Note:**

    These pages are optional but we recommend setting them. Without a success page, customers end up on a default PayU page after paying and do not automatically come back to your website.
  </Callout>
</Accordion>

<Accordion title="6. Generate the Button and Add It To Your Website" icon="far fa-code">
  1. Click **Generate Button**.

  PayU creates your button and gives you a short piece of code to copy.

  2. Click **Copy Code** to copy the button code.

     <Image src="https://files.readme.io/0d5b65c380ca96a02549e4a8af8c31f9f890bc3b3cadd3d91a564328aee7b2e9-Screenshot_2026-09-29_at_4.26.21_PM.png" align="center" caption="Add the Code to Your Website" border={true} />



  3. Go to your website and paste the code where you want the button to appear:

  | Website builder    | How to add the code                                                   |
  | ------------------ | --------------------------------------------------------------------- |
  | **WordPress**      | Add a **Custom HTML** block to your page and paste the code inside it |
  | **Wix**            | Add an **HTML iframe** element to your page and paste the code        |
  | **Squarespace**    | Add a **Code Block** to your page and paste the code                  |
  | **Other builders** | Look for an "HTML", "Code", or "Embed" block in your page editor      |

  The button appears on your page right away.

  <Callout icon="🚧" theme="warning">
    **Payment Buttons cannot be changed after creation.** If you need to update the label, amount, colour, or any other setting — create a new button with the correct details and replace the code on your website.
  </Callout>
</Accordion>

***

## What Happens After My Customer Pays?

After your customer clicks the button and completes a payment:

1. PayU updates the payment status in your Dashboard right away.
2. The payment appears in the **Transactions** tab in your PayU Dashboard.
3. Your customer is taken to your success page — or your failure page if the payment did not go through.
4. The money is settled to your bank account on the standard settlement cycle.

<Callout icon="📘" theme="info">
  ### **Want to be notified the moment a payment comes in?**

  You can set up webhooks under **Settings → Webhooks** in the Dashboard. Webhooks are optional — your Dashboard always shows you the latest payment status whether or not you set them up.
</Callout>

***

## What Do I Do If Something Goes Wrong?

| Problem                                              | Fix                                                                                                                                                                         |
| ---------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The button is not showing on my website              | Make sure the code was pasted into a code or HTML block — not as plain text. Clear your browser cache and reload the page.                                                  |
| Customer clicks the button but nothing happens       | The button code may not have loaded correctly. Remove it, paste it again in a fresh code block, and reload the page.                                                        |
| I entered the wrong amount or button text            | Payment Buttons cannot be changed after creation. Create a new button with the correct details, copy the new code, and replace the old code on your website.                |
| Customer paid but I cannot see it in my Dashboard    | Wait a few minutes and refresh. If it still does not appear, see <Anchor target="_blank" href="doc:payment-button-troubleshooting">Payment Button Troubleshooting</Anchor>. |
| Customer was not taken to my success or failure page | Check that you entered the correct page addresses under **Advanced Options**. Make sure each address starts with `https://`.                                                |

***

## What If My Customer Wants the Money Back?

<Cards>
  <Card title="Refunds" href="doc:introduction-refunds" icon="fad fa-arrow-rotate-left">
    Return all or part of a payment to your customer — directly from the PayU Dashboard.
  </Card>

  <Card title="Settlements" href="doc:split-settlments" icon="fad fa-building-columns">
    Find out when your money will reach your bank account and see your settlement history.
  </Card>

  <Card title="Disputes and Chargebacks" href="doc:chargeback" icon="fad fa-shield-halved">
    Handle cases where a customer has raised a complaint with their bank about a payment.
  </Card>
</Cards>

***

## Next Steps

<Cards>
  <Card title="Customize Your Button" href="doc:customize-payment-button" icon="fa-sliders">
    See all the ways you can configure your button — colours, size, amount type, and redirect pages.
  </Card>

  <Card title="Manage Payment Buttons" href="doc:manage-payment-buttons" icon="fa-list-check">
    Check payments received, filter your buttons, and download records.
  </Card>

  <Card title="Payment Button Troubleshooting" href="doc:payment-button-troubleshooting" icon="fa-wrench">
    Fix issues with buttons not showing, payments not going through, or records not appearing.
  </Card>

  <Card title="Payment Button FAQs" href="doc:payment-button-faqs" icon="fa-circle-question">
    Common questions about Payment Buttons.
  </Card>
</Cards>
