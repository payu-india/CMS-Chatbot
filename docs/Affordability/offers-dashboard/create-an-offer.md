---
title: Create an Instant Discount or Cashback Offer
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  keywords:
    - Create Instant Discount Offer
    - Create Cashback Offer
    - PayU India checkout cashback offer
    - PayU India checkout Instant Discount Offer
    - Cashback Offer Setup
    - Instant Discount Setup
    - Discount and Cashback Offers PayU
    - Instant Discount Offer Creation
    - Cashback Offer Creation
  robots: index
next:
  description: ''
---
The procedure to create an Instant Discount or Cashback Offer on PayU Dashboard is similar.

***

### Steps to Create an Offer

1. [Select the discount type](#step-1-select-the-discount-type)
2. [Add basic details of the offer](#step-2-add-basic-details)
3. [Include the offer rules or limitations](#step-3-include-the-offer-rules-or-limitations)
4. [Configure the payment modes which can avail the offer](#step-4-configure-the-payment-modes-which-can-avail-the-offer)
5. [Review the offer](#review-the-offer)

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

<Image align="center" className="border" border={true} src="https://files.readme.io/94d041dbfbfc5faa76260a76e736cdbb4030553dddcde8c5ef3efeb9ca5d0f95-Screenshot_2025-06-03_at_10.16.03_AM.png" />

3. Select the discount type.

  The *Basic Offer Details* page is displayed.

<Image align="center" src="https://files.readme.io/5002858696d93c6edf465cf830ca8b20c69c06231342acce95fbcf8add81e0d2-Screenshot_2025-06-03_at_10.16.41_AM.png" />

***

## Step 2: Add basic details

1. Include the basic details as described in the following table and then click **Save & Process**:

| **Field**          | **Description**                                                                                                                                                                       |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Offer Title        | Enter a unique title for the offer. This would be displayed as the offer title on your Checkout page.                                                                                 |
| Offer Description  | Enter the offer text that would be shown to your customer at checkout (for PayU Hosted Checkout Integration transactions).                                                            |
| Offer Period       | Enter the offer validity date and time range. Your offer will be valid and visible to the customer between this time period. You can specify the time range up to the seconds detail. |
| Terms & Conditions | Enter the text content that should appear under the “Terms and Conditions” on the Checkout page for customers.                                                                        |

2. Select the **Create Generic Coupon Code** check box to create a coupon code.

The fields to collect coupon code details are displayed.

<Image align="center" className="border" border={true} src="https://files.readme.io/c35975feb22ef487cd1e4491153280ee8decae1fb092c2d66af7774becbaf267-dashboard_instant_disc_coupon_code_details.png" />

* Enter the coupon code in the **Set Coupon Code** field.
* Click the **Display coupon to customer on checkout** toggle button to display the coupon code on the PayU Checkout page.

2. After you complete the above details and click **Next**.

The *Payment Options* page is displayed.

2. Select the applicable payment options and click **Next.**

The *Offer Rules* page is displayed.

<Image align="center" className="border" border={true} src="https://files.readme.io/a169ac96a97658d1884f8047cd73ace82b112223eb6b67aae45e495c83288e23-Screenshot_2025-06-03_at_10.27.01_AM.png" />

> 📘 Note:
>
> When you are creating an offer, you can choose to save the incomplete offer details in the Draft state using the **Save as Draft & Exit** button at the top-right corner and publish it later.

***

## Step 3: Include the Offer rules or limitations

1. Enter the following details on the *Set Offer Rules* page.

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
        Type of Cashback/Instant Discount
      </td>

      <td>
        Specify whether the discount is in in terms of a percentage of the transaction amount or in terms of a flat discount.
      </td>
    </tr>

    <tr>
      <td>
        Offer Percentage/Discount per transaction
      </td>

      <td>
        Specify the discount value that has to applied in in terms of percentage or rupees in flat.
      </td>
    </tr>

    <tr>
      <td>
        Maximum times an offer can be used
      </td>

      <td>
        Specify how many times a customer can avail the offer.
      </td>
    </tr>

    <tr>
      <td>
        Minimum transaction amount & Maximum transaction amount
      </td>

      <td>
        Specify the threshold or range for a transaction to be applicable for the offer.
      </td>
    </tr>

    <tr>
      <td>
        User Limits
      </td>

      <td>
         
      </td>
    </tr>

    <tr>
      <td>
        Max time an offer can be used by a user?
      </td>

      <td>
        Select any of the following options from the drop-down list to specify the maximum number of transactions the user can avail this offer:
         - **Unlimited**: Users can avail the offer for unlimited transactions.

        * **Custom**: Specify the custom limit up to which the users can avail the offer.
      </td>
    </tr>

    <tr>
      <td>
        Budget per user
      </td>

      <td>
         Enter the budget amount per user.
      </td>
    </tr>

    <tr>
      <td>
        Reset User Limits
      </td>

      <td>
        Select any of the following options from the drop-down list to reset the user limit for specified frequency:  

        * **Every Day**: Reset the user limit everyday
        * **Every Week**: Reset the user limit every week
        * **Every Month**: Reset the user limit every month
        * **Custom**: Specify the custom frequency after which the user limit is reset
      </td>
    </tr>
  </tbody>
</Table>

#### Additional Options

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Select for Offer – Counter or Budget Amount
      </th>

      <th>
        Specify a limit on the number of times an offer can be availed or a budget for the discount volume.

        For example, if you select Budget amount to provide the offer to customers until you reach the budget of Rs. 3 Lakhs, specify 3,00,000.
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Don’t allow transaction, if offer is not applicable
      </td>

      <td>
        Select this check box if you do not want to allow the transaction if the offer is not applicable for the user. 

        * *Note*\*: The option will work only if you post the offer key and the offer is live.
      </td>
    </tr>

    <tr>
      <td>
        Do you wish to apply offers on certain products?
      </td>

      <td>
        Select **Yes** if you wish to apply product-based or SKU-based offer. For more information, refer to [SKU-Based Offer using Merchant Hosted Checkout](doc:collect-payments-with-sku-based-offer-using-merchant-hosted-checkout-offers-integration).
      </td>
    </tr>

    <tr>
      <td>
        In case of multiple quantity of same product?
      </td>

      <td>
        Select **Yes** if you wish to apply the product-based or SKU-based offer to apply for multiple quantity. This field is enabled if **Yes** is selected in the Do you wish to apply offers on certain products? field.
      </td>
    </tr>
  </tbody>
</Table>

2. After you complete the above details and click **Save & Process**.

The *Setup Payment options of your offer* page is displayed.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Screenshot-2022-02-23-at-8.17.28-PM-1024x573.png)

***

## Step 4: Configure payment modes

Select any of the following payment modes to configure offer details that is explained in the corresponding tabs:

> 📘 Note:
>
> You can configure one or multiple payment options for an offer. For example, the “HDFC Diwali Offer” can contain 10% discount for HDFC debit or credit cards, HDFC UPI, and a 3-month interest-free EMI for HDFC cards.

* [Cards](#cards)
* [Net Banking](#net-banking)
* [UPI](#upi)
* [Wallets](#wallets)
* [EMI](#emi)
* [BNPL](#bnpl)

### Cards

1. Select any of the following options on the *Setup Payment options of your offer* page:

* Credit Card
* Debit Card

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Screenshot-2022-02-24-at-9.21.48-PM-1024x865.png)

2. Perform any of the following based on the method you want to select the bank and network:

<Table>
  <thead>
    <tr>
      <th>
        **Method**
      </th>

      <th>
        **Description**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Select Bank and Networks
      </td>

      <td>
         - Search and select the bank from the Select Banks and Select Networks drop-down list.

        * Search and select a network from the **Select Networks** drop-down list.
      </td>
    </tr>

    <tr>
      <td>
        Specify the BIN numbers in CSV File
      </td>

      <td>
        * Click **Download Sample File** if you are not having the sample file or CSV file template. The CSV file contains some sample BIN numbers (first 6 digits of Debit Card or Credit Cards), which you need to update according to your requirements.
        * Update the CSV or text file to include the BIN details. For updating the CSV file, you can use Microsoft Excel or any other Spreadsheet tool.
        * Click **Select .csv or .txt from your library** and select the CSV or text file.
      </td>
    </tr>
  </tbody>
</Table>

3. Select any of the following options in the **Set budget for credit card** field (optional):

**Note**: You can choose either specify count or amount based on the **Counter** or **Budget amount** option.

| Budget Type   | Description                                                                                                                                                                                    |
| :------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Counter       | Select this option and then specify the count in the **Counter Value** field. This offer will be enabled only for the transactions count as defined in the **Counter Value** field.            |
| Budget amount | Select this option and then specify the amount in the **Budget Amount** field. This offer will be enabled to customers until this budget amount is reached for your transactions cumulatively. |

4. Click **Add Payment Option**.

   The offer for the debit or credit card payment option gets added to the Setup *Payment options of your offer* page.

### UPI

1. Select the **UPIs** option on the *Setup Payment options of your offer* page.

   The *Select UPIs* page is displayed.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Screenshot-2022-02-23-at-8.28.25-PM-1024x556.png)

2. Select the check boxes for the UPIs you wish to enable the offer.
3. Select any of the following options in the **Set budget for credit card** field (optional):

**Note**: You can choose either enter count or amount based on the **Counter** or **Budget amount** option.

| **Budget Type** | **Description**                                                                                                                                                                                |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Counter         | Select this option and then specify the count in the **Counter Value** field. This offer will be enabled only for the transactions count as specified in the **Counter Value** field.          |
| Budget amount   | Select this option and then specify the amount in the **Budget Amount** field. This offer will be enabled to customers until this budget amount is reached for your transactions cumulatively. |

4. Click **Add Payment Option**.

### Wallets

1. Select the **Wallets** option on the *Setup Payment options of your offer* page.

   The *Select Wallets* page is displayed.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Screenshot-2022-02-23-at-8.30.25-PM-1024x746.png)

2. Select the check boxes for the wallets you wish to enable the offer.
3. Select any of the following options in the **Set budget for credit card** field (optional):

**Note**: You can choose either enter count or amount based on the **Counter** or **Budget amount** option.

| **Budget Type** | **Description**                                                                                                                                                                                |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Counter         | Select this option and then specify the count in the **Counter Value** field. This offer will be enabled only for the transactions count specified in the **Counter Value** field.             |
| Budget amount   | Select this option and then specify the amount in the **Budget Amount** field. This offer will be enabled to customers until this budget amount is reached for your transactions cumulatively. |

4. Click **Add Payment Option**.

### EMI

1. Select the **EMI** option on the *Setup Payment options of your offer* page.

   The *EMI* Offer page is displayed.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/03/Screenshot-2022-03-21-at-7.41.49-PM-1024x877.png)

2. Select Banks and Tenures on which you wish to enable the offer. You can select all tenures of a specific bank and choose specific tenures for each bank. 
3. Restrict the offer on a select list of BINs on the banks that were selected in Step 4 if required using the following steps:

* Click **Download Sample File** if you are not having the sample file or CSV file template. The CSV file contains some sample BIN numbers (first 6 digits of Debit Card or Credit Cards), which you need to update according to your requirements.  

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/01/Screenshot-2022-01-12-at-10.07.22-PM.png)

* Update the CSV or text file to include the BIN details. For updating the CSV file, you can use Microsoft Excel or any other Spreadsheet tool. 
* Click **Select .csv or .txt from your library** and select the CSV or text file. 

5. Select any of the following options in the **Set budget for EMI** field (optional):

**Note**: You can choose either enter count or amount based on the **Counter** or **Budget amount** option.

| **Budget Type** | **Description**                                                                                                                                                                                 |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Counter         | Select this option and then specify the count in the **Counter Value** field. This offer will only be enabled for the transactions count specified in the **Counter Value** field.              |
| Budget amount   | Select this option and then specify the amount in the **Budget Amount** field. This offer will be enabled for customers until this budget amount is reached for your transactions cumulatively. |

6. Click **Add Payment Option**.

### BNPL

Select the **BNPL** option on the *Setup Payment options of your offer* page.

The *Select BNPL Options* page is displayed.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/03/BNPL_Offer_Options-1024x651.png)

After you complete adding any one or combination of the offers involving various payment options, click **Save & Proceed**.

> 📘 **References:**
>
> * No-Cost EMI offers can be created on Credit and Debit Card EMIs. For more information, refer to [Create a No-Cost EMI Offer](doc:create-a-no-cost-emi-offer).
> * Low-Cost EMI offers can create on Credit and Debit Card EMIs. For more information, refer to Create a Low-Cost EMI Offer.

The offer for the payment options you configured gets added to the Setup *Payment options of your offer* page.

***

## **Step 5: Review of the Offer**

The *Preview of Cashback Offer* page summarizes the details you provided in Step 2 to Step 4.

1. Review all the configurations added before you make the offer available to your customers.
2. Click the **Edit** button to return back to the corresponding page and update the configuration.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Screenshot-2022-02-23-at-8.32.06-PM-1024x573.png)

3. Click **Publish Offer** to make it available to customers.