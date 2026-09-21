---
title: Manage Payment Links
excerpt: >-
  View, filter, duplicate, share, deactivate, and export your Payment Links, all
  from the PayU Dashboard.
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  title: Manage Payment Links — Dashboard Guide | PayU Developer
  description: >-
    Filter, duplicate, share, deactivate, and export PayU Payment Links from the
    Dashboard — no developer needed. Includes bulk upload and CSV export.
  keywords:
    - manage payment links payu
    - filter payment links dashboard
    - deactivate payment link payu
    - export payment links csv
    - duplicate payment link
    - bulk upload payment links
    - payu payment links dashboard
    - share payment link again
    - payment link history export
    - payu no code payment management
  robots: index
next:
  description: Explore related information and resources.
---
{/* NEW CONTENT: Template B1 — T1 Dashboard Walkthrough (V2 format) */}

{/* EXISTING CONTENT: adapted from categorize-the-payment-links-view.md, export-the-payment-link-history.md, customize-the-calendar-view-for-payment-links.md */}

<Banner
  isInline={true}
  message="Integration effort: No code or website required"
  color="#15C614"
  textColor="#ffffff"
  fontSize="14px"
  fontWeight="bold"
/>

You can manage payment links from the PayU Dashboard after they are created and live.

<Callout icon="fad fa-rectangle-new" theme="warn">
  ### New to Payment Links?

  Start with the [Payment Links Overview](doc:payment-links-overview) or follow the [step-by-step guide to create your first link](doc:send-a-payment-link). To manage links from your own system, see the [Fetch API](doc:api-fetch) and [Cancel / Update Status API](doc:api-cancel-status).
</Callout>

***

## How Do I Access My Payment Links?

To open your links: log in to [PayU Dashboard](https://onboarding.payu.in/) and click **Payment Links&#x20;**&#x75;nder **Payment Tools**.


<Image src="https://files.readme.io/bca170f5ad6ba34eb18f1e8ba1a7072d45be0b24fd0f32fd4bfdf22d015682ca-Screenshot_2026-09-21_at_9.35.56_AM.png" align="center" caption="Access Payment Links" border={true} />


***

## What Can I Do With a Payment Link After It Is Created?

You can perform the following actions after a link is created:

<Accordion title="See Payment Link Details" icon="far fa-rectangle-list">
  To see payment link details:

  1. Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/app/account/signin?first_visit_url=https%3A%2F%2Fpayu.in%2F&last_visit_url=https%3A%2F%2Fpayu.in%2Fbusiness%2Chttps%3A%2F%2Fpayu.in%2F%2Chttps%3A%2F%2Fpayu.in%2Fbusiness%2Chttps%3A%2F%2Fpayu.in%2F">PayU dashboard</Anchor> and go to **Payment Links&#x20;**&#x75;nder **Payment Tools.**


     <Image src="https://files.readme.io/53215c3e4e7294d15669cb34cd231730787e24e86505214a8d80d48cb5b67c19-image.png" align="center" caption="Access Payment Links" border={true} />


     A list of created payment links is displayed with the following information:

     - **Created On**
     - **Purpose of Payment**
     - **Invoice ID**
     - **Amount**
     - **Payment Link**
     - **Payment Type**
     - **Payment Status**
     - **Status**
  2. Click the Payment Link you want to view the details.


     <Image src="https://files.readme.io/fada3c576d9d091f8a41e2cefe2ce555ff3878f8debea9b8ddc1e08b76191d43-Screenshot_2026-09-21_at_10.21.28_AM.png" align="center" caption="Click to view details" border={true} />


  The link details are divided in to the following sections:<br />

  <Accordion title="Link Details" icon="fad fa-link">
    The link and customer detials are displayed in two sub-sections.

    <Tabs>
      <Tab title="Link Details">
        - **Name:&#x20;**&#x4E;ame of the Payment Link you enterd during creation.

        - **Status:&#x20;**&#x53;tatus of the payment link. Refer to the Payment Link statuses for more information.

        - **Link:&#x20;**&#x54;he payment with options to copy and share via WhatsApp and Facebook.

        - **Invoice ID:&#x20;**&#x54;he auto generated invoice ID. For example, **INV331178996540608300.**

        - **Total Amount:&#x20;**&#x54;he total amount for which the link is created.

        - **Type:&#x20;**&#x54;he payment type. The value can be either **Partial&#x20;**&#x6F;r **Full**.

        - **Share:&#x20;**&#x4F;ptions to copy the link or share via WhatsApp, Facebook or to any other mobile number or email ID.


          <Image src="https://files.readme.io/18374beecc40c725bf806f3eea419f259e50c0928a43a7573e94c8a661280637-Screenshot_2026-09-21_at_10.40.08_AM.png" border={true} />

      </Tab>

      <Tab title="Customer Details">
        - **Email**
        - **Phone Number**


        <Image src="https://files.readme.io/4b110954b53faf10c794ef87abc99530181f9de6a892369ba8a942c526bd9e9a-Screenshot_2026-09-21_at_11.51.29_AM.png" align="center" caption="Customer Details" border={true} />

      </Tab>
    </Tabs>
  </Accordion>

  <Accordion title="Details and Transactions" icon="far fa-money-bills">
    This section has two different tabs:<br />

    <Tabs>
      <Tab title="Details">
        The **Details&#x20;**&#x74;ab diaplys the following link information:

        - **Created On:&#x20;**&#x54;he date and time at which the link was created.
        - **Balance:&#x20;**&#x54;he balance amount to be paid (only if the partial payment is enabled).
        - **Min. Initial Payment:&#x20;**&#x54;he minimum amount allowed to pay.
        - **Limit Access To:&#x20;**&#x54;he number of transactions allowed.&#x20;
        - **Creator Email**
        - **Expiry Date:&#x20;**&#x54;he link expiry date an time beyond which the link will be deactivated.
        - **Partial Payment**
        - **Status:&#x20;**&#x53;tatus of the payment.
        - **Auto Reminder**


        <Image src="https://files.readme.io/575f5f4799fc68845cea4977f74665bddb91165fd06ddf4a8e18d11bafc0fa43-Screenshot_2026-09-21_at_11.22.45_AM.png" align="center" caption="Link Details" border={true} />

      </Tab>

      <Tab title="Transactions">
        This tab displays the following transaction information of the link:

        - **Date:&#x20;**&#x44;ate and time at which the payment was made.
        - **Payu ID (Transaction ID):&#x20;**&#x41; unique transaction ID. You have an option to copy it.
        - **Customer Email**
        - **Amount:&#x20;**&#x54;he amount of the transaction.
        - **Status:&#x20;**&#x54;he status of the transaction.


        <Image src="https://files.readme.io/b60e913b8bd066fb40ca89de88be1bf31dfe0469a98502b6b53a5aa20a5ec9dd-Screenshot_2026-09-21_at_11.29.48_AM.png" align="center" caption="Transaction Details" border={true} />

      </Tab>
    </Tabs>
  </Accordion>
</Accordion>

<Accordion title="Duplicate a Link" icon="far fa-copy">
  Duplicating creates a brand-new link pre-filled with the same details such as, amount, purpose, and options so that you do not have to fill everything in again. Use it to reuse a configuration, correct a mistake on an existing link, or run the same payment request for a different customer.<br />

  To duplicate a link:

  1. Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/app/account/signin?first_visit_url=https%3A%2F%2Fpayu.in%2F&last_visit_url=https%3A%2F%2Fpayu.in%2Fbusiness%2Chttps%3A%2F%2Fpayu.in%2F%2Chttps%3A%2F%2Fpayu.in%2Fbusiness%2Chttps%3A%2F%2Fpayu.in%2F">PayU dashboard</Anchor> and go to **Payment Links&#x20;**&#x75;nder **Payment Tools.**


     <Image src="https://files.readme.io/16cc602d7fea50b82cf305a021d8ec949b3f3ca9219a632f468ab9745bbdc5dd-image.png" align="center" caption="Access Payment Links" border={true} />


  2. Click the menu icon against a required payment link and click **Duplicate.**


     <Image src="https://files.readme.io/ba9d25a123f142ce6b98c768421c302cd0d3486ac7351ca72555f27624801fc5-Screenshot_2026-09-21_at_12.02.28_PM.png" align="center" caption="Click Duplicate" border={true} />


  3. The **Create new payment link** page opens with the existing link's details pre-filled.

  4. Edit any fields you need to change. For example, the expiry date or customer details.

  5. Click **Create and Send Payment link**.


     <Image src="https://files.readme.io/eb3a59aa72227334bc5d2e66dd3f100eef9594aa8cbc4084e3c93dd19a9f2d46-screen-recording.gif" align="center" caption="Duplicate a Payment Link" border={true} />


     <Callout icon="📘" theme="info">
       ### **Note:**

       Duplicating does not deactivate the original link. If you want to replace a link (e.g., wrong amount was set), duplicate it with the correct details first, then deactivate the original.
     </Callout>

     The link is created and sent to the customer. You can see it in the **Payment Links&#x20;**&#x70;age.
</Accordion>

<Accordion title="Share or Resend a Link" icon="far fa-share">
  You can send the link to a customer at any time as long as it is still **Active**.

  To share or resend a link:

  1. Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/app/account/signin?first_visit_url=https%3A%2F%2Fpayu.in%2F&last_visit_url=https%3A%2F%2Fpayu.in%2Fbusiness%2Chttps%3A%2F%2Fpayu.in%2F%2Chttps%3A%2F%2Fpayu.in%2Fbusiness%2Chttps%3A%2F%2Fpayu.in%2F">PayU dashboard</Anchor> and go to **Payment Links&#x20;**&#x75;nder **Payment Tools.**


     <Image src="https://files.readme.io/4bdd9694005c1b8b87943da0a39ec512d18b55e48941bc7a9010b1ff106647c4-image.png" align="center" caption="Access Payment Links" border={true} />


  2. Click the menu icon against a required payment link and click **Share.**


     <Image src="https://files.readme.io/27172438300911c6a248a792664a3004e425677962fdccd55c1f1ee51715b116-Screenshot_2026-09-21_at_1.15.27_PM.png" align="center" caption="Click Share" border={true} />


  3. Copy the link or share via WhatsApp, Facebook or to any other mobile number or email ID as required.


     <Image src="https://files.readme.io/4a76daed789c0c72bb8a54ca89827a29fdd263504516d6c6388982729010863e-image.png" align="center" caption="Share or Resend the Link." border={true} />


  There is no limit on how many times you can share a link. Each share just sends the same URL again.
</Accordion>

<Accordion title="Edit the Details of a Link" icon="far fa-pen-to-square">
  You can edit certain details such as the expiry date, amount, and status of a payment link after it is created.

  To edit the details:

  1. Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/app/account/signin?first_visit_url=https%3A%2F%2Fpayu.in%2F&last_visit_url=https%3A%2F%2Fpayu.in%2Fbusiness%2Chttps%3A%2F%2Fpayu.in%2F%2Chttps%3A%2F%2Fpayu.in%2Fbusiness%2Chttps%3A%2F%2Fpayu.in%2F">PayU dashboard</Anchor> and go to **Payment Links&#x20;**&#x75;nder **Payment Tools.**


     <Image src="https://files.readme.io/0edfad7491b4d310e15206fed91377c0067061f06c99a2d0e8cc9401b6abff22-image.png" align="center" caption="Access Payment Links" border={true} />


  2. Click the menu icon against a required payment link and click **Edit Details.**


     <Image src="https://files.readme.io/9ffda282631c77994e3f79648f454f60252605cbc90148606d2056933573dd8a-Screenshot_2026-09-21_at_1.29.51_PM.png" align="center" caption="Click Edit Details" border={true} />


  3. Make changes to the required details. You can edit only the following details.
     - **Item Description**
     - **Set Payment Due Date (Link Expiry):&#x20;**&#x53;et or remove the link expiry
     - **Enable Partial Payment:&#x20;**&#x45;nable or disable the partial payment
     - **Number of Instalments**
     - **Add More Details**
       - **Add Address Details**
       - **Add UDF Details**
     - **Phone number**
     - **Name**
     - **Email**

  4. Click **Edit Payment Link&#x20;**&#x74;o save the changes.


     <Image src="https://files.readme.io/e658e847683bc35ac6dbad46081b3c761143df81736a55e53d4410a43a2e2037-screen-recording-2.gif" align="center" caption="Edit Payment Link Details" border={true} />


  <Callout icon="🚧" theme="warning">
    ### **Watch Out!**

    Not all fields can be edited after creation. If you need to change the purpose or customer details, duplicate the link with the correct settings and deactivate the original. To update fields programmatically, use the [Cancel / Update Status API](doc:api-cancel-status).
  </Callout>
</Accordion>

<Accordion title="Deactivate a Link" icon="far fa-ban">
  Deactivating stops any further payments on the link. Customers who click it will see a message that it is no longer active.

  To deactivate a link:

  1. Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/app/account/signin?first_visit_url=https%3A%2F%2Fpayu.in%2F&last_visit_url=https%3A%2F%2Fpayu.in%2Fbusiness%2Chttps%3A%2F%2Fpayu.in%2F%2Chttps%3A%2F%2Fpayu.in%2Fbusiness%2Chttps%3A%2F%2Fpayu.in%2F">PayU dashboard</Anchor> and go to **Payment Links&#x20;**&#x75;nder **Payment Tools.**


     <Image src="https://files.readme.io/517b591fde2b0d734063b91df9a7efd015f4d4eb75e35c147f198ec2e07929cb-image.png" align="center" caption="Access Payment Links" border={true} />


  2. Click the menu icon against a required payment link and click **Deactivate.**


     <Image src="https://files.readme.io/615e8c4c1da7afcbe5befc1657e14d1878c6e9a5f33ac59571d6a8c5ea50ed74-Screenshot_2026-09-21_at_1.47.19_PM.png" align="center" caption="Click Deactivate" border={true} />


  3. Click **Yes** in the confirmation window.

  The link status changes to **Deactivated**.
</Accordion>

<Accordion title="Reactivate a Link" icon="far fa-clock-rotate-left">
  You can reactivate a deactivated link from the dashboard:

  To reactivate a link:

  1. Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/app/account/signin?first_visit_url=https%3A%2F%2Fpayu.in%2F&last_visit_url=https%3A%2F%2Fpayu.in%2Fbusiness%2Chttps%3A%2F%2Fpayu.in%2F%2Chttps%3A%2F%2Fpayu.in%2Fbusiness%2Chttps%3A%2F%2Fpayu.in%2F">PayU dashboard</Anchor> and go to **Payment Links&#x20;**&#x75;nder **Payment Tools.**


     <Image src="https://files.readme.io/538f6c20473e9c0da496e892ac68071e166879f495dda0f71227fcbda7fc0de5-image.png" align="center" caption="Access Payment Links" border={true} />


  2. Click the menu icon against a deactivated payment link and click **Activate.**


     <Image src="https://files.readme.io/aa31df7ffbf655de3e172a8e8089bf4c82f7ee8fac69a7d531a7dc3881f7579b-Screenshot_2026-09-21_at_1.58.59_PM.png" align="center" caption="Click Activate" border={true} />


  3. Click **Yes&#x20;**&#x69;n the confirmation window to activate.

  The link status changes to **Active**.
</Accordion>

***

## How Do I Find a Specific Payment Link?

You can filter the payment links list using the following options:

<Callout icon="📘" theme="info">
  ### **Payment Link Status**

  Not sure what **Active**, **Paid**, **Expired**, or **Deactivated** mean? See [Payment Link Statuses](doc:send-a-payment-link).
</Callout>

<Accordion title="Filter by Status and Payment Type" icon="far fa-filter">
  To filter the list by status:

  1. Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/app/account/signin?first_visit_url=https%3A%2F%2Fpayu.in%2F&last_visit_url=https%3A%2F%2Fpayu.in%2Fbusiness%2Chttps%3A%2F%2Fpayu.in%2F%2Chttps%3A%2F%2Fpayu.in%2Fbusiness%2Chttps%3A%2F%2Fpayu.in%2F">PayU dashboard</Anchor> and go to **Payment Links&#x20;**&#x75;nder **Payment Tools.**


     <Image src="https://files.readme.io/42a033de863c821718096d7b68198aba4cf6907b5cedbfa20c5cce9a399753ec-image.png" align="center" caption="Access Payment Links" border={true} />


  2. Click the **Filter** drop-down and select one or more status and payment type checkboxes. These are the available options:

     - **Status**

       - **Active**
       - **Paid**
       - **Deactivated**
       - **Expired**
         <Callout icon="📘" theme="info">


       ### **Payment Link Status**

       Not sure what **Active**, **Paid**, **Expired**, or **Deactivated** mean? See [Payment Link Statuses](doc:send-a-payment-link).

       </Callout>
     - **Payment Type**
       - **Standard**
       - **Partial Payment**


     <Image src="https://files.readme.io/38e42794f7726239255a7ec9ab9003684361bdc839446e56ce2dab84e8794489-Screenshot_2026-09-21_at_2.23.12_PM.png" align="center" caption="Filter Payment Link List" border={true} />


  3. Click **Apply&#x20;**&#x74;o filter the list.
</Accordion>

<Accordion title="Filter by Date Range" icon="far fa-calendar">
  To filter the list by date range:

  1. Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/app/account/signin?first_visit_url=https%3A%2F%2Fpayu.in%2F&last_visit_url=https%3A%2F%2Fpayu.in%2Fbusiness%2Chttps%3A%2F%2Fpayu.in%2F%2Chttps%3A%2F%2Fpayu.in%2Fbusiness%2Chttps%3A%2F%2Fpayu.in%2F">PayU dashboard</Anchor> and go to **Payment Links&#x20;**&#x75;nder **Payment Tools.**


     <Image src="https://files.readme.io/87f833f0e3b63b7a43a5ea66318e367c44468236472eb90f95fcf468fc965c6a-image.png" align="center" caption="Access Payment Links" border={true} />


  2. Click the calendar icon and select any of the following.
     1. For a quick range, click **Today**, **Yesterday**, **Last 7 days**, or **Last 30 days**.


        <Image src="https://files.readme.io/5c16e927eb9fa8f01f539d7cbe087d5bf072c1dc49e3b477a2c82153148b8e8d-Screenshot_2026-09-21_at_2.32.18_PM.png" align="center" caption="Select Date Range" border={true} />


     2. For a custom range, click **Custom Range**, pick a start and end date from the calendar, then click **Apply**.

        <Callout icon="fad fa-star-exclamation" theme="warn">
          ### **Watch Out!**

          You can select a maximum date range of 90 days.
        </Callout>


        <Image src="https://files.readme.io/ca476fe9b764393c8b3ffd3b620b17308e3ad2e371807355b3f3531919e85ab2-Screenshot_2026-09-21_at_2.33.21_PM.png" align="center" caption="Select Custom Range" border={true} />

</Accordion>

<Accordion title="Search a Payment Link" icon="fad fa-magnifying-glass">
  You can search a payment using purpose and InvoiceNumber.

  To search a payment link:

  1. Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/app/account/signin?first_visit_url=https%3A%2F%2Fpayu.in%2F&last_visit_url=https%3A%2F%2Fpayu.in%2Fbusiness%2Chttps%3A%2F%2Fpayu.in%2F%2Chttps%3A%2F%2Fpayu.in%2Fbusiness%2Chttps%3A%2F%2Fpayu.in%2F">PayU dashboard</Anchor> and go to **Payment Links&#x20;**&#x75;nder **Payment Tools.**


     <Image src="https://files.readme.io/16f19c44171f05b7d9ce1394576e538eb0e5459b9f54c3f1f0a2355c46e03974-image.png" align="center" caption="Access Payment Links" border={true} />


  2. Use the drop-down next to the search to select the search type. Below are the available options:

     - **Purpose**
     - **InvoiceNumber**


     <Image src="https://files.readme.io/296c997061ba5287303445fafc09c121ce72269f1715382f60217f126339242c-Screenshot_2026-09-21_at_3.01.23_PM.png" align="center" caption="Select Search Type" border={true} />


  3. Enter the required information in the search bar based on your selection and click **Search**.
</Accordion>

***

## Can I Download All My Payment Link Records?

<Accordion title="Export Payment Link Records" icon="far fa-download">
  To download payment link records:

  1. Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/app/account/signin?first_visit_url=https%3A%2F%2Fpayu.in%2F&last_visit_url=https%3A%2F%2Fpayu.in%2Fbusiness%2Chttps%3A%2F%2Fpayu.in%2F%2Chttps%3A%2F%2Fpayu.in%2Fbusiness%2Chttps%3A%2F%2Fpayu.in%2F">PayU dashboard</Anchor> and go to **Payment Links&#x20;**&#x75;nder **Payment Tools.**


     <Image src="https://files.readme.io/f435da3d1c07338957b79786bc9f159f1d9a7c6f3aa38d8856be45865b01712d-image.png" align="center" caption="Access Payment Links" border={true} />


  2. Click the **Download** drop-down at the top of the table and select any of the following format:

  | Format                           | Contents                             |
  | -------------------------------- | ------------------------------------ |
  | **csv**                          | Summary of all payment links         |
  | **xlsx**                         | Summary of all payment links (Excel) |
  | **Txns - csv**                   | Transaction-level detail per link    |
  | **Txns - xlsx**                  | Transaction-level detail (Excel)     |
  | **Old Payment Link Data - csv**  | Legacy link data                     |
  | **Old Payment Link Data - xlsx** | Legacy link data (Excel)             |


  <Image src="https://files.readme.io/725bfcf87501665e6d3b5b15b9c5838fd12377c1b4966ee7a636c88ace4e1d89-Screenshot_2026-09-21_at_3.18.03_PM.png" align="center" caption="Select the Format" border={true} />


  3. Click **Download&#x20;**&#x6F;n the **Report Ready for Download&#x20;**&#x70;op-up menu to download the report.
</Accordion>

***

<Callout icon="fad fa-code" theme="success">
  ### **For Developers**

  - If you want to create payment links from your own system such as a CRM, billing tool, or backend, use the Create Payment Link API.
  - If you want to fetch, update, or deactivate links from your own system, see the Fetch Payment Links API and the Cancel / Update Status API.
</Callout>

***

## Next Steps

<Cards>
  <Card title="Send a Payment Link" href="doc:send-a-payment-link" icon="fa-paper-plane">
    Step-by-step guide to creating and sending a payment link.
  </Card>

  <Card title="Payment Links API" href="doc:api-fetch" icon="fa-code">
    Fetch, update, and cancel payment links programmatically.
  </Card>

  <Card title="Payment Links Troubleshooting" href="doc:payment-links-troubleshooting" icon="fa-wrench">
    Fix issues with links not working, payments not reflecting, and more.
  </Card>
</Cards>
