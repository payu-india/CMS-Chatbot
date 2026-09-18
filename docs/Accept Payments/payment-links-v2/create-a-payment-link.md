---
title: Create a Payment Link
excerpt: >-
  Create a payment link in the PayU Dashboard and share it with your customer in
  under 5 minutes. No code required.
deprecated: false
hidden: true
metadata:
  title: Create a Payment Link — 5-Minute Quickstart | PayU Docs
  description: >-
    Step-by-step guide to creating and sending a PayU Payment Link in 5 minutes.
    No code required — share over WhatsApp, SMS, or email from the Dashboard.
  keywords:
    - send payment link payu
    - create payment link tutorial
    - how to create payment link india
    - payu payment link step by step
    - payment link whatsapp india
    - no code payment quickstart payu
    - payu dashboard create payment link
    - payment link sms notification
    - accept payment link no website
    - payu payment link guide
  robots: index
next:
  description: Explore related information and resources.
  pages:
    - slug: payment-links-v2
      title: Payment Links
      type: basic
---
{/* NEW CONTENT: Template F — T1 Quickstart/Tutorial (V2 format) */}

<Banner
  isInline={true}
  message="Integration effort: No code or website required"
  color="#15C614"
  textColor="#ffffff"
  fontSize="14px"
  fontWeight="bold"
/>

Create a Payment Link from the PayU Dashboard and share it with your customer in under 5 minutes without the help of a developer or code.

***

## What All I Need?

<Cards>
  <Card title="A PayU Merchant Account" icon="far fa-table-cells-column-unlock">
    <Columns layout="fixed">
      <Column>
        [Set up your account](doc:set-up-your-account) if you have not already.
      </Column>
    </Columns>
  </Card>

  <Card title="Dashboard Access" icon="far fa-pager">
    Log in to the [PayU Dashboard](https://onboarding.payu.in/) to check whether you have access to the PayU dashboard before you start.
  </Card>
</Cards>

***

## How Do I Create a Payment Link?

To create and send a Payment Link:

<Accordion title="1. Open Payment Links on the Dashboard" icon="far fa-grid-2">
  1. Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/app/account/signin?first_visit_url=https%3A%2F%2Fpayu.in%2F&last_visit_url=https%3A%2F%2Fpayu.in%2Fbusiness%2Chttps%3A%2F%2Fpayu.in%2F%2Chttps%3A%2F%2Fpayu.in%2Fbusiness%2Chttps%3A%2F%2Fpayu.in%2F">PayU dashboard</Anchor>.
  2. Expand **Payment Tools&#x20;**&#x61;nd clic&#x6B;**&#x20;Payment Links&#x20;**&#x64;isplayed in the left navigation.


  <Image src="https://files.readme.io/35fe8235c387b22f93c4af37425c7ce2077534a981c17a8abb22d037f98486a1-Screenshot_2026-09-18_at_11.04.00_AM.png" align="center" caption="Go to Payment Links" border={true} />

</Accordion>

<Accordion title="2. Create a new link" icon="far fa-link">
  1. Click **Create New Payment Links** displayed in the top-right corner of the **Payment Links** page.


  <Image src="https://files.readme.io/889bdf1e584b7531c1f79d1396230fbbfcb7ae0c6beaa5789d764d57c95aef8f-Screenshot_2026-09-18_at_11.06.18_AM.png" align="center" caption="Create New Payment Link panel" border={true} />


  2. Provide these details in the **Payment Link Details** section:

     <Callout icon="📘" theme="info">
       ### **Required Fields**

         <RequiredStar legend />
     </Callout>

     <Table>
       <thead>
         <tr>
           <th>
             Information
           </th>

           <th>
             Description
           </th>
         </tr>
       </thead>

       <tbody>
         <tr>
           <td>
             <requiredstar param="Item Description" bold="{true}"></RequiredStar>
           </td>

           <td>
             A short description about the link you are creating.
           </td>
         </tr>

         <tr>
           <td>
             **Total Amount**
           </td>

           <td>
             The total amount you want to collect. You can choose to leave this field for the open payments. Add an amount if you wan to allow partial payments.
           </td>
         </tr>

         <tr>
           <td>
             **Limit Link Access To**
           </td>

           <td>
             Use this filed to limit the payment link to number of customers or transactions.
           </td>
         </tr>

         <tr>
           <td>
             **Set Payment Due Date (Link Expiry)**
           </td>

           <td>
             Use this field if you want to set the expiry of the link. Post this date and time the link stops working and customers cannot make the payment using this link.
           </td>
         </tr>

         <tr>
           <td>
             **Enable Partial Payment**
           </td>

           <td>
             Enable this to accept <Glossary>partial payments</Glossary>.
           </td>
         </tr>
         
         <tr>
            <td>
              **Min. Initial Payment** (only if you enable partial payment)
            </td>

            <td>
             Enter the minimum part payment accepted.
            </td>
         </tr>
         
         <tr>
            <td>
              **Number of Instalments**
            </td>

            <td>
             Enter the number of instalments you want to allow on the payment link.
            </td>
         </tr>
       </tbody>
     </Table>


     <Image src="https://files.readme.io/7eb57e5f6f3a938989a98e19f63d223fe049d2f1d5b8e4258693879e27ac47b8-Screenshot_2026-09-18_at_1.36.52_PM.png" align="center" caption="Provide Payment Link Details" border={true} />

</Accordion>

<Accordion title="3. Add More Details (optional)" icon="far fa-file-invoice">
  1. Click **Add More Details** to include these additional configuration fields:

  | Field                         | Description                                  |
  | ----------------------------- | -------------------------------------------- |
  | **Add Invoice Number**        | Tie the link to your internal invoice ID     |
  | **Add Tax**                   | Add a tax line to the payment record         |
  | **Add Shipping**              | Add a shipping charge                        |
  | **Add Address Details**       | Collect delivery address from the customer   |
  | **Add UDF Details**           | Custom key-value fields for your own records |
  | **Add Merchant Reference ID** | Your internal order or booking reference     |


  <Image src="https://files.readme.io/c73e2f1739d759815cf7503096e7c971927f4986c8b0dddafc6951b4a760cff2-dashboard_create_new_payment_link_step2.png" border={true} />


  2. Click **Add Fields** to apply your selection and return to the main panel.
</Accordion>

<Accordion title="4. Customer Targeting" icon="far fa-user">
  Add these details under the **Customer Targeting&#x20;**&#x73;ection:

  | Fields           | Description                                               |
  | ---------------- | --------------------------------------------------------- |
  | **Phone number** | The customer phone number.                                |
  | **Send via SMS** | Select for PayU to send the link automatically via SMS.   |
  | **Name**         | The customer name.                                        |
  | **Email**        | The customer email ID.                                    |
  | **Send Email**   | Select for PayU to send the link automatically via email. |
  |                  |                                                           |


  <Image src="https://files.readme.io/e152dd0ea2bea18f00fd03a354e0fdecce071b2d84e4e54cd3fba858ac5400fb-Screenshot_2026-09-18_at_1.54.47_PM.png" align="center" caption="Enter Customer Details" border={true} />


  <Callout icon="📘" theme="info">
    ### **Note:**

    If you enter the customer's phone or email and toggle notifications on, PayU sends the link the moment you click **Create** — no manual copying or sharing needed.
  </Callout>
</Accordion>

<Accordion title="5. Customer Data Capture (optional)" icon="far fa-list-check">
  Specify what PayU collects from your customer at checkout under the **Customer Data Capture&#x20;**&#x73;ection:

  - Standard fields: Customer Email and Phone
  - Custom fields: click **Add new Fields+** and configure:
    - **Field Type**: Alphanumeric, Calendar, or Dropdown
    - **Field Name**: the label the customer sees
    - **Mark as Mandatory**: Select to require the field before payment can proceed


  <Image src="https://files.readme.io/2448391dfa55fcd56969ab1a3d5ba09c542d7caefe3ecb5181aa14cb19e5ce25-Screenshot_2026-09-18_at_2.09.25_PM.png" align="center" caption="Capture Customer Data" border={true} />

</Accordion>

<Accordion title="6. Create and send" icon="far fa-paper-plane">
  Click **Create and Send Payment link** in the top-right corner.


  <Image src="https://files.readme.io/14e447953ba5f3a9c4c0cabaf852255600b8ca63288b8f422a7ce90ca784efbd-Screenshot_2026-09-18_at_2.14.45_PM.png" align="center" caption="Create and Send a Payment Link" border={true} />


  **What happens next:**

  - **If notifications are on** → PayU sends the link to the customer immediately via SMS/email.
  - **If not** → the link appears in your Payment Links Dashboard. Copy the URL from the **Payment Link** column and share it over WhatsApp, email, or any channel.
</Accordion>

***

## How Do I Create Many Links at Once?

Use bulk upload to create hundreds of payment links in one go. Each row in the CSV becomes a separate link. Maximum file size allowed is 20 MB.

<Accordion title="1. Open Bulk Uploads" icon="far fa-folder-open">
  1. Log in to the [PayU Dashboard](https://onboarding.payu.in/).

  2. Expand **Payment Tools&#x20;**&#x61;nd clic&#x6B;**&#x20;Payment Links&#x20;**&#x64;isplayed in the left navigation.


     <Image src="https://files.readme.io/bc6fe9da1a24dc6d7bd3bf46b29fc136aa19c59a37319a5c5bdea81f01cfc566-image.png" align="center" caption="Go to Payment Links" border={true} />


  3. Click **Bulk Create** displayed at the top-right.


     <Image src="https://files.readme.io/b5ef3ea428e4c976ec9d8c8cbac1e1add683047cb998485b984b0885595b21db-Screenshot_2026-09-18_at_3.12.38_PM.png" align="center" caption="Go to Bulk Create" border={true} />

</Accordion>

<Accordion title="2. Download the sample file and review column definitions" icon="far fa-file-csv">
  1. On the **Generate Bulk Payment links&#x20;**&#x70;age, click **Download Sample File** to get the CSV template with the correct column structure.

     The CSV accepts the following columns:

  | Column                         | Required  | Description                                                                        |
  | ------------------------------ | --------- | ---------------------------------------------------------------------------------- |
  | **Amount**                     | Mandatory | Payment amount — must be ≥ 1                                                       |
  | **Product Description**        | Mandatory | Purpose of the payment shown on checkout                                           |
  | **Invoice ID**                 | Optional  | Your unique reference to identify this link                                        |
  | **Merchant Reference ID**      | Optional  | Unique ID per transaction — if entered, only one payment is allowed on the link    |
  | **Customer Name**              | Optional  | Pre-fills customer name at checkout                                                |
  | **Customer Email**             | Optional  | Customer's email address                                                           |
  | **Customer Mobile**            | Optional  | Customer's mobile number (10 digits)                                               |
  | **Validation Period**          | Optional  | Number of units the link is valid for (default: 365). Max: 1000 days from creation |
  | **Time Unit**                  | Optional  | Unit for Validation Period — `D` = days · `H` = hours · `M` = minutes              |
  | **Send SMS**                   | Optional  | `1` = send SMS · `0` or blank = do not send                                        |
  | **Is Partial Payment Allowed** | Optional  | `1` = allow partial payment · `0` or blank = full amount required                  |
  | **Max Payments Allowed**       | Optional  | Maximum number of payments on this link — blank means unlimited until expiry       |

  <Callout icon="🚧" theme="warning">
    ### **Note:**

    **Amount** and **Product Description** are the only mandatory columns. All other columns are optional. You can leave them blank if not required.
  </Callout>
</Accordion>

<Accordion title="3. Fill in your CSV" icon="far fa-table">
  Open the downloaded sample file and fill in one row per payment link.

  <Callout icon="📘" theme="success">
    ### **Error-free Upload Tips**

    - Do not change column headers — PayU maps fields by column name.

    - Ensure every row has a value for **Amount** and **Product Description**.

    - If using **Invoice ID**, each value must be unique across your merchant account.

    - If using **Validation Period** + **Time Unit** together — both fields must be filled.

    - Leave **Merchant Reference ID** blank if you want the link to be usable more than once.

    - Save the file as `.csv` (not `.xlsx`) before uploading.
  </Callout>
</Accordion>

<Accordion title="4. Upload your File and Set Batch Details" icon="far fa-upload">
  Back on the **Generate Bulk Payment links** page:

  1. Click **Select file from your library** and choose your completed CSV. Maximum file size allowed is 20 MB.
  2. Enter a **Batch ID (Optional)**: Your internal reference for this upload batch.
  3. Enter a **Batch description&#x20;**(optional): A label to help you identify this batch later.


     <Image src="https://files.readme.io/b736def75c804d83e56904bd5b75f7c9538f35d522567cfc46200274e2f48209-Screenshot_2026-09-18_at_3.32.33_PM.png" align="center" caption="Upload and Set Batch Detials" border={true} />

</Accordion>

<Accordion title="5. Choose Communication Channel Type" icon="far fa-bell">
  Under **Communication Channel Type**, select how PayU should notify customers when their link is created. You can select both, one, or neither. If neither is selected, links are created but not sent. You can share them manually from the Payment Links Dashboard.

  - **Email**: sends the link to the customer's email address (if provided in the CSV)
  - **SMS**: sends the link to the customer's mobile number (if provided in the CSV)

  <Callout icon="📘" theme="info">
    ### **Note:**

    Payment link reminders are not enabled by default. To set them up, go to **Reminder settings** in the Dashboard before uploading.
  </Callout>
</Accordion>

<Accordion title="6. Configure Customer Data Capture" icon="far fa-list-check">
  1. Under **Customer Data Capture**, select which information should PayU collect from customers on the checkout page. Below are the available options:
     - **Customer Name**
     - **Customer Address**
     - **Customer Email** _(checked by default)_
     - **Customer Phone** _(checked by default)_
  2. To add custom fields beyond these, click **+ Add New Fields** and configure the field type, label, and whether it is mandatory.
  3. Once done, click **Generate Payment Links** (or the upload/submit button) to process your batch.


     <Image src="https://files.readme.io/ed2ae0ea830f1c0c3cec866e2be547a59c9e589a2caf95dffa4075268d2b80f0-Screenshot_2026-09-18_at_3.39.58_PM.png" align="center" caption="Create and Send Payment Links" border={true} />

</Accordion>

<Accordion title="7. Review Upload Results" icon="far fa-magnifying-glass">
  After upload, PayU processes each row and creates the links. To check results:

  1. Go to the **Bulk Uploads** tab in the Payment Links Dashboard.
  2. Find your batch in the history list. Each batch shows the total links created and any errors.
  3. Click into a batch to see per-row results. Rows with errors are flagged with the specific issue.


  <Image src="https://files.readme.io/10ae907f614ea7970e1dcc010fd4e3c3707e570fe055beeaec4d11e607908e97-Screenshot_2026-09-18_at_3.44.35_PM.png" align="center" caption="Check Bulk Upload Status" border={true} />


  **Common Errors to Watch For:**

  | Error                              | Cause                                    | Fix                                                |
  | ---------------------------------- | ---------------------------------------- | -------------------------------------------------- |
  | "Amount is mandatory"              | Amount column is empty                   | Fill in Amount for every row                       |
  | "Product Description is mandatory" | Description column is empty              | Fill in Product Description for every row          |
  | "Invoice ID already exists"        | Duplicate Invoice ID across your account | Use a unique Invoice ID per row, or leave it blank |
  | "Invalid Time Unit"                | Time Unit value is not D, H, or M        | Use exactly `D`, `H`, or `M` (uppercase)           |
</Accordion>

***

## What Are the Different Statuses of a Payment Link?

| Status          | What it means                                  | How to get here                         | What you can do                                      |
| --------------- | ---------------------------------------------- | --------------------------------------- | ---------------------------------------------------- |
| **Active**      | Live — accepting payments                      | Link just created                       | Share, duplicate, deactivate                         |
| **Paid**        | Payment received (or max transactions reached) | Customer completed a payment            | Duplicate if you need to collect again               |
| **Expired**     | Expiry date passed                             | System auto-expires at the set date     | Duplicate with a new expiry; or extend via API       |
| **Deactivated** | Manually stopped                               | You disabled it in Dashboard or via API | Re-activate via API; or duplicate from the dashboard |

***

## What Happens After My Customer Pays?

After your customer makes the payment:

1. PayU updates the link status to **Paid** in your Dashboard.
2. The transaction appears in the **Transactions&#x20;**&#x74;ab in your Dashboard.
3. If you have webhooks configured, PayU sends a `payment.success` event to your server.

<Callout icon="📘" theme="info">
  ### **Webhooks**

  Webhooks are optional. Your Dashboard always reflects the current payment status without any webhook setup.
</Callout>

***

## What Do I Do If Something Goes Wrong?

| Problem                                         | Fix                                                                                                                                      |
| ----------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Customer says the link isn't opening            | Check the link status in your Dashboard — it may be expired or deactivated.                                                              |
| Customer didn't receive the SMS or email        | Confirm phone/email were entered and the notification toggle was on before creation. Reshare from **Actions > Share** in your Dashboard. |
| Customer paid but Dashboard still shows Pending | Wait 5–10 minutes and refresh. See [Payment Links Troubleshooting](doc:payment-links-troubleshooting).                                   |
| Wrong amount or details on the link             | Deactivate it and create a new one — links cannot be edited after creation. Duplicate the link to reuse the settings.                    |

***

## Sandbox for Your Testing

<PayUPaymentLinksWizard />

## Next Steps

<Cards>
  <Card title="Manage Payment Links" href="doc:manage-payment-links" icon="fa-list-check">
    Filter, duplicate, resend, deactivate, and export your links.
  </Card>

  <Card title="Payment Link Options" href="doc:payment-link-options" icon="fa-sliders">
    Expiry dates, partial payments, custom fields, and notifications.
  </Card>

  <Card title="Payment Links Overview" href="doc:payment-links-overview" icon="fa-circle-info">
    Full overview — use cases, supported payment methods, and API access.
  </Card>
</Cards>
