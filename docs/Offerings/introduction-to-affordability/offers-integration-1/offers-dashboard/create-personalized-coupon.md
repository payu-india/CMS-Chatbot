---
title: Create a Personalized Coupon
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Create a Personalized Coupon Offer
  description: >-
    The document outlines the process of creating personalized coupon offers,
    which can be used to attract customers and boost sales by providing
    discounts or cashback. It details steps such as selecting discount types,
    adding offer details, setting rules, configuring payment modes, setting up
    customer communications, and reviewing the offer before publishing.
  keywords:
    - Personalized Coupon Offer
    - ' Coupon Offer'
    - ' Personalized Coupon'
    - ' Coupon on Dashboard'
  robots: index
next:
  description: ''
---
Coupon codes are an important feature of offers as they add tangibility to offers, thereby helping attract customers and improve sales by providing discounts or cashback on behalf of merchants, banks and brands.  Personalised coupons helps you mass-generate unique coupons that are specifically mapped to a unique customer, thus no pilferage, wrongful usage or mis-use of coupons. Also, they can be easily shared with your customers directly on WhatsApp.

This procedure describes how to create a Personalized coupon.

### Steps to Create an Offer

1. [Select the discount type](#step-1-select-the-discount-type)
2. [Add basic details of the offer](#step-2-add-basic-details)
3. [Include the offer rules or limitations](#step-3-include-the-offer-rules-or-limitations)
4. [Configure the payment modes which can avail the offer](#step-4-configure-the-payment-modes-which-can-avail-the-offer)
5. [Setting up customers and communications](#step-5-setting-up-customers-and-communications)
6. [Subvention details](#step-6-subvention-details)
7. [Review the offer](#step-7-review-the-offer)

***

<br />

## Step 1: Add the basic details

1. Navigate to [.Offers Dashboard](doc:offers-dashboard).
2. Click **Create an Offer** at the top-right corner.

   The _Create New Offer_ page is displayed.

   <Image align="center" className="border" border={true} src="https://files.readme.io/94d041dbfbfc5faa76260a76e736cdbb4030553dddcde8c5ef3efeb9ca5d0f95-Screenshot_2025-06-03_at_10.16.03_AM.png" />
3. Select **Personalised Coupons** as the offer type.  

![](https://files.readme.io/30ed57e78d5f6d50dc129247e00df255cea989015879d9b9440e5e8a88494dc8-Screenshot_2025-06-05_at_11.31.13_AM.png) 

## Step 2: Add basic details

1. Include the basic details as described in the following table:

| **Field**               | **Description**                                                                                                                                                                       |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Offer Title             | Enter a unique title for the offer. This would be displayed as the offer title on your Checkout page.                                                                                 |
| Offer Description       | Enter the offer text that would be shown to your customer at checkout (for PayU Hosted Checkout Integration transactions).                                                            |
| Offer Period            | Enter the offer validity date and time range. Your offer will be valid and visible to the customer between this time period. You can specify the time range up to the seconds detail. |
| Terms & Conditions Text | Enter the text content that should appear under the “Terms and Conditions” on the Checkout page for customers.                                                                        |
| Apply Offer as          | You can apply the offer as **Instant Discount**or **Cashback Offer.**                                                                                                                 |

2. Include the details in the **Coupon Code Guidelines** section as described in the following table and then click **Save & Process**:

<Table>
  <thead>
    <tr>
      <th>
        **Field**
      </th>

      <th>
        **Description**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Coupon Code Prefix
      </td>

      <td>
        Enter a prefix for the coupon code to match with your campaign. For example, "Welcome".
      </td>
    </tr>

    <tr>
      <td>
        Authenticate coupon at checkout
      </td>

      <td>
        Select **Yes** to authenticate the coupon code entered by your customer whether it is valid one.
      </td>
    </tr>

    <tr>
      <td>
        Show coupon at checkout
      </td>

      <td>
        Select **Yes** to show the coupon code on the checkout page after authentication.

        * _Note_*: This option is enabled or visible only if**Yes**is selected in**Authenticate coupon at checkout**.
      </td>
    </tr>
  </tbody>
</Table>

2. After you complete the above details and click **Next**.

   The _Payment Options_ page is displayed.

   <Image align="center" className="border" border={true} src="https://files.readme.io/20face5ca921ac455c7dd74ba8fb532e274b2ac4dd69b581d64b52b3072af1a7-dashboard-prediscounted-payment-options.png" />

   > 📘 Note
   >
   > When you are creating an offer, you can choose to save the incomplete offer details in the Draft state using the **Save as Draft & Exit** button at the top-right corner and publish it later.

   ## Step 2: Configure payment modes

   1. Configure the payment modes. For more information, refer to [Create an Instant Discount or Cashback Offer](doc:create-an-offer#configure-payment-modes).
   2. Click **Next**.

   The _Offer Rules_ page is displayed.

   <Image align="center" className="border" border={true} src="https://files.readme.io/2e7610844659ed93bfa6380b4023a90f4ff3c2b5743acdbe9ed3a2eeb39c385c-dashboard-prediscounted-offer-rules.png" />

   ## Step 3: Include the Offer rules

   1. Enter the offer rules and limitations on the _Set Offer Rules_ page. For more information, refer to [Create an Instant Discount or Cashback Offer](doc:create-an-offer#step-3-include-the-offer-rules).
   2. After you complete the above details and click **Next**.

      The _Subvention Details_ page is displayed.

   ## Step 5: Setting up customers and communications

   ### Setting up new customer base

   1. Select the customer base from the **Customer Base** field.

   <Image align="center" className="border" border={true} width="350px" src="https://files.readme.io/32326ce0ac00bf43784bf5184705f1c555e80986a21413895836426c9c640453-offers-dashboard-coupon-step5-customer-base.png" />

   2. If you wish to configure a new customer base, click **New Customer Base** and follow these steps:

   <Image align="center" className="border" border={true} width="400px" src="https://files.readme.io/cf9dec12ce2b0b95420f20ade7d570ab6d6b68f71efcdd86fe5fafc8de3072d0-dashboard-offers-upload-new-customer-base-for-coupon.png" />

   * Click **Download Sample File** if you are not having the sample file or CSV file template. The CSV file contains some sample customer details, which you need to update according to your requirements.  
   * Update the CSV or text file to include the customer details with a unique user token. For updating the CSV file, you can use Microsoft Excel or any other Spreadsheet tool. 
   * Click **Choose file** and select the CSV or text file and click **Upload**.

   ### Setting up communications (via WhatsApp)

   This is an optional step. You can send the messages to the recipients directly and seamlessly from within the dashboard without the need to do it manually. The following communications are supported by PayU:

   * [Pre-launch communication for building Intrigue](#pre-launch-communication-for-building-intrigue)

   * [Post-launch communication](#post-launch-communication)

   > 📘 Note:
   >
   > For sending WhatsApp messages, you are required to have a Meta account, using AISensy as our service provider. AISensy is a BSP that helps manage and approve WhatsApp templates with META. If you have any difficulties in setting up the AISensy account, contact your PayU Key Account Manager (KAM or [PayU Support](https://help.payu.in).) You need to log on to AISensy account to set up your WhatsApp templates. Click **logging into** and connect to the AISensy account.
   >
   > <Image align="center" src="https://files.readme.io/8efe2dedae743d120eddcf4c639283ab545da4916126e615dfeed33f6195fd9f-dashboard-offers-coupon-setup-aisensy-acct.png" />

   #### Pre-launch communication for building Intrigue

   They help send notifications to the end users for any upcoming offers

   <Image align="center" className="border" border={true} src="https://files.readme.io/2fcac7582f25ec71ee6ac756fbd249db67da89983d8bd716dbe1b84c0bb83cc6-dashboard-offers-upload-coupon-whatsapp-comm.png" />

   #### Post-launch communication

   This section is used to launch after coupon delivery. You need select template and then allow user to set up the delivery dates.

   1. Click the **Enable Launch Communication** toggle button.

   <Image align="center" className="border" border={true} src="https://files.readme.io/ef85097c3e7b68a1927d177e3b378913dd90ddfa93c07b3085deb83f9546069f-dashboard-offers-upload-coupon-whatsapp-comm-post-launch.png" />

   2. Select the coupon from the **Select Communication Template (WhatsApp)** drop-down list.
   3. Click the **Enable Re-Targeting Communication** toggle button enter the following details to enable the re-targeting communication:

   | Field                                          | Description                                                                                                                                                                                   |
   | ---------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Set Retargeting Delay                          | Specify the number of days after the coupon is generated or the offer goes live to send retargeting communication.                                                                            |
   | No. of communication to be sent (per customer) | Enter the total number of messages to be sent per customer for re-targeting. Once this limit is reached, no further messages will be sent.                                                    |
   | Base interval between communication            | Set the number of days between messages. For example, if 2 messages are sent with a 4-day interval, the second message will go out 4 days after the first, only if the coupon remains unused. |
   | Message template and Value of variables        | Choose the template that you want to trigger a message for.                                                                                                                                   |

   4. After you complete the above details and click **Next**.

   ## Step 5: Configure Offer Subvention Details

   1. Enter the subvention details in the _Subvention Details_ page. For more information, refer to refer to [Create an Instant Discount or Cashback Offer](doc:create-an-offer#step-4-configure-offer-subvention-details).
   2. After you complete the above details and click **Next**.

   The _Preview Details_ page is displayed.

   <Image align="center" className="border" border={true} src="https://files.readme.io/a87a0559ec1e51c8daed008b50a26c33c186b877accfc72a3a4bc72b15eb3aa5-dashboard-prediscounted-preview_page.png" />

   ## Step 6: Review of the Offer

   The _Preview Details_ page summarizes the details you provided in Step 2 to Step 4.
3. Review all the configurations added before you make the offer available to your customers.
4. Click the **Edit** button to return back to the corresponding page and update the configuration.
5. Click **Publish** to make it available to customers.