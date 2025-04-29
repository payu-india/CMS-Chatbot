---
title: Create Downpayment+EMI Offer
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
Downpayment EMI is an **hybrid payment** **method** where a customer may choose to pay downpayment on a payment method and EMI via a different payment methods. For example, if a customer wants to purchase the newly launched laptop worth Rs 90,000.  The customer can use the **Downpayment+EMI** offer on your website to fund her purchase with UPI and avail No Cost EMI on their credit card. 

Downpayment+EMI offer allows you to :

* **Making affordable products for end customer-** The customer can now use the funds available along with availing benefits of their credit line.
* **Do more with your budget -** You can provide No Cost EMI with reduced subvention burden and acquire more customers.

The procedure to create an Instant Discount or Cashback Offer on PayU Dashboard is similar.

***

### Steps to Create an Offer

1. [Select the discount type](#step-1-select-the-discount-type)
2. [Add basic details of the offer](#step-2-add-basic-details)
3. [Include the offer rules or limitations](#step-3-include-the-offer-rules-or-limitations)
4. [Set up EMI options](#step-4-set-up-emi-options)
5. [Review the offer](#step-5-review-of-the-offer)

***

After you create an Instant Discount or Cashback Offer, you can collect payments from your customers using PayU Hosted (Non-seamless) or Merchant Hosted (Seamless) Checkout integration as described in the following sections:

* PayU Hosted
  * [Integrate with PayU Hosted Checkout - Offers](doc:payu-hosted-checkout-integration-with-offers)
* Merchant Hosted Checkout
  * [Instant Discount or Cashback using Merchant Hosted Checkout](doc:instant-discount-or-cashback-offers-integration-using-merchant-hosted-checkout)
  * [SKU-Based Offer using Merchant Hosted Checkout](doc:collect-payments-with-sku-based-offer-using-merchant-hosted-checkout-offers-integration)

***

## Step 1: Select the discount type

1. Navigate to [Offers Dashboard](doc:offers-dashboard).
2. Click **Create an Offer** at the top-right corner.

   The *Create New Offer* page is displayed.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Screenshot-2022-02-23-at-8.10.38-PM-1024x573.png)

3. Select the **No Cost EMI** offer.

  The *Basic Offer Details* page is displayed.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Screenshot-2022-02-23-at-8.11.36-PM-1024x573.png)

***

## Step 2: Add basic details

1. Include the basic details as described in the following table and then click **Save & Process**:

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
        Title
      </td>

      <td>
        Enter a unique title for the offer. This would be displayed as the offer title on your Checkout page.
      </td>
    </tr>

    <tr>
      <td>
        Description
      </td>

      <td>
        Enter the offer text that would be shown to your customer at checkout (for PayU Hosted Checkout Integration transactions).
      </td>
    </tr>

    <tr>
      <td>
        From Date, From Time, To Date, To Time
      </td>

      <td>
        Enter the offer validity date and time range. Your offer will be valid and visible to the customer between this time period. You can specify the time range up to the seconds detail.
      </td>
    </tr>

    <tr>
      <td>
        Terms & Conditions
      </td>

      <td>
        Enter the text content that should appear under the “Terms and Conditions” on the Checkout page for customers.
      </td>
    </tr>

    <tr>
      <td>
        Terms & Conditions Links
      </td>

      <td>
        Enter the hyperlinks for independent hosted pages.  

        * \*Note\*\*: It is recommended to be used only If it is absolutely necessary to avoid redirections outside your customer purchase journey).
      </td>
    </tr>
  </tbody>
</Table>

2. After you complete the above details and click **Save & Process**,

   The *Set Offer Rules* page is displayed.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/05/Screenshot-2022-05-26-at-11.39.03-AM-1-1024x665.png)

3. Scroll down *Set Offer Rules* page for the **Additional Options** section.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/06/Offers_Details_Additional_Options-875x1024.png)

> 📘 Note:
>
> When you are creating an offer, you can choose to save the incomplete offer details in the Draft state using the **Save as Draft & Exit** button at the top-right corner and publish it later.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Screenshot-2022-02-23-at-8.15.59-PM-1024x573.png)

***

## Step 3: Include the Offer rules or limitations

The procedure to include the rules and limitations is similar to creating an Instant Discount or Cashback Offer. For more information, refer to [Create an Instant Discount or Cashback Offer](https://docs.payu.in/docs/create-an-offer#step-3-include-the-offer-rules-or-limitations).

***

## Step 4: Set up EMI options

To complete the offer details for No Cost EMI:

1. Select **Cards** from the **Select EMI Type** drop-down list:

> **Note**: Currently, only Downpayment via Credit Card and No Cost EMI on Credit Cards.

The *Setup Payment options of your offer* page is updated to display the options for Cards EMI.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/03/Screenshot-2022-03-21-at-7.41.49-PM-1-1024x877.png)

2. Click **Add Payment Option**.

   The offer for the debit card payment option gets added to the Setup *Payment options of your offer* page.

3. Select **EMI** to add the cards supporting No-Cost EMI.

4. Enter the details as described in the *Setup EMI Options* page. For more information, refer to [Create an Instant Discount or Cashback Offer](doc:create-an-offer).

5. Select **Yes** in the **Subvent GST** field to subvent the GST for the customers.

> **Notes**: The following must be taken care if you select the **Subvent GST** check box:
>
> * Create these types of offers if there is an agreement with the bank/brand. Reach out to KAM for any queries
> * Bank share, brand share, and merchant share should all add up to 100%
> * You will receive your reconciliation reports in this email
> * Reconciliation will be possible only after the refund window

6. Scroll down and  select the **All downpayment options with No Cost EMI** that you want to configure

<Image align="center" src="https://files.readme.io/a485b5f-create_offer_downpayment_options.webp" />

7. Select any of the following options:

* **Absolute Downpayment**: Configure a flat amount against a tenure that you want to accept as Downpayment
* **Percentage Downpayment**: Configure the percentage of transaction/product amount against a tenure that you want to accept as Downpayment.

8. Select the bank and tenures where you want to provide No Cost EMI or No Cost EMI With downpayment.

   For example: in the following screenshot, Axis bank for No Cost EMI and No Cost EMI with Downpayment on different tenures.

<Image align="center" width="422px" src="https://files.readme.io/4563832-create-offer-card-emi-options.png" />

9. Select tenures where you want to provide only No Cost EMI and No Cost EMI with Downpayment.

   For example, in the following screenshot, No Cost EMI on 3 and 6 month tenure for Axis bank that was selected and No Cost EMI with Downpayment on.

<Image align="center" src="https://files.readme.io/a178007-create_offer_emi_card_downpayment_options.webp" />

10. Click **Save & Proceed**.

***

## **Step 5: Review of the Offer**

The *Preview of Cashback Offer* page summarizes the details you provided in Step 2 to Step 4.

1. Review all the configurations added before you make the offer available to your customers.
2. Click the **Edit** button to return back to the corresponding page and update the configuration.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Screenshot-2022-02-23-at-8.32.06-PM-1024x573.png)

3. Click **Publish Offer** to make it available to customers.
