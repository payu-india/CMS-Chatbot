---
title: Create a Low-Cost EMI Offer
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
Low-Cost EMI offers are for credit or debit cards to make purchases by paying a low-interest rate on the purchase amount. In this payment option, the customer has to pay interest charges on their purchase amount but at a lower rate than the regular interest rate.

For example, the purchase amount is ₹50,000. If the customer opts for the Low-Cost EMI offer, they can choose to pay for the product in installments over a period of 12 months at a lower interest rate. If the regular interest rate for a credit card is 18% per annum, but the bank is offering a special interest rate of 12% per annum. In this case, the customer will pay a total interest of ₹3,000 (i.e., ₹50,000 x 12% x 1 year) on the purchase, which adds up to a total payment of ₹53,000 over 12 months. So, instead of paying the entire amount upfront, the customer will pay ₹4,417 per month for 12 months.

While Low-Cost EMI may offer a lower interest rate than the regular interest rate, the total interest cost may still add up to a considerable amount over the payment period.

### **Steps to Create an Offer:**

1. [Select the discount type](https://devguide.payu.in/temp-offers-integration/create-an-offer-temp/create-a-low-cost-emi-offer/#step1)
2. [Add basic details of the offer](https://devguide.payu.in/temp-offers-integration/create-an-offer-temp/create-a-low-cost-emi-offer/#step2)
3. [Include the offer rules or limitations](https://devguide.payu.in/temp-offers-integration/create-an-offer-temp/create-a-low-cost-emi-offer/#step3)
4. [Configure the payment modes which can avail the offer](https://devguide.payu.in/temp-offers-integration/create-an-offer-temp/create-a-low-cost-emi-offer/#step4)
5. [Review the offer](https://devguide.payu.in/temp-offers-integration/create-an-offer-temp/create-a-low-cost-emi-offer/#step5)

***

After you create a Pre-Discounted Offer, you can collect payments from your customers using PayU Hosted (Non-seamless) as described in the PayU Hosted Checkout Integration with Offers.

***

## **Step 1: Select the Discount Type**

1. Navigate to [_Offers_ section of PayU Dashboard](https://devguide.payu.in/affordability/getting-started-with-affordability/navigate-to-offer-engine/).
2. Click **Create an Offer** at the top-right corner.

The _Create New Offer_ page is displayed.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/03/Screenshot-2023-03-23-at-11.15.54-AM-1024x662.png)

1. Select the discount type as **Low-Cost EMI**.

 The _Basic Offer Details_ page is displayed.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/03/Screenshot-2023-03-24-at-10.32.25-AM-1024x612.png)

***

## **Step 2: Add Basic Details**

1. Add the basic details. For more information, refer to [Create and Instant Discount or Cashback offer](https://devguide.payu.in/offers-integration/create-an-offer/create-an-instant-discount-or-cashback-offer#step2).
2. Select any of the following options in the **No cost EMI offer to be applied as** field:
   - **Instant Discount**: The specified amount is discounted from the total amount.
   - **Cashback**: The specified amount is credited back to the customer’s payment instrument later.
3. After you complete the above details and click **Save & Process**,

The _Set Offer Rules_ page is displayed.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/05/Screenshot-2022-05-26-at-11.39.03-AM-1-1024x665.png)

Scroll down the _Set Offer Rules_ page for the **Additional Options** section.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/06/Offers_Details_Additional_Options-875x1024.png)

> 📘 Note:
>
> When you are creating an offer, you can choose to save the incomplete offer details in the Draft state using the **Save as Draft & Exit** button at the top-right corner and publish it later.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/03/Pre-discounted_offer_step2-988x1024.png)

***

## **Step 3: Include the Offer Rules or Limitations**

1. Enter the offer rules and limitations on the _Set Offer Rules_ page. For more information, refer to [Create an Instant Discount or Cashback Offer](https://devguide.payu.in/offers-integration/create-an-offer/create-an-instant-discount-or-cashback-offer/) > [Include the Offer Rules or Limitations](https://devguide.payu.in/offers-integration/create-an-offer/create-an-instant-discount-or-cashback-offer#step3)
2. After you complete the above details and click **Save & Process**.

The _Set Offer Rules_ page is displayed.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Screenshot-2022-02-23-at-8.17.28-PM-1024x573.png)

***

## **Step 4: Configure Payment Modes**

1. Click **Download Sample File** under **Setup Options for Low Cost EMI** if you are not having the sample file or CSV file template. The Excel file contains the banks offering Low-Cost EMI for Debit Cards or Credit Cards, which you need to include the interest rates according to your requirements.
2. Update the Excel or text file to include the interest rates for applicable cards.
3. Click **Select file from your library** and select the Excel file.
4. Restrict the offer on a select list of BINs on the banks that were selected in Step 1 to Step 3 if required using the following steps:

- Click **Download Sample File** if you are not having the sample file or CSV file template. The CSV file contains some sample BIN numbers (first 6 digits of the Debit Card or Credit Cards), which you need to update according to your requirements.  

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/01/Screenshot-2022-01-12-at-10.07.22-PM.png)

- Update the CSV or text file to include the BIN details. For updating the CSV file, you can use Microsoft Excel or any other Spreadsheet tool. 
- Click **Select .csv or .txt from your library** and select the CSV or text file. 

After you complete adding any one or combination of the offers involving various payment options, click **Save & Proceed**.

The offer for the payment options you configured gets added to the Setup _Payment options of your offer_ page.

***

## **Step 5: Review of the Offer**

The _Preview of Cashback Offer_ page summarizes the details you provided in [Step 2](https://devguide.payu.in/temp-offers-integration/create-an-offer-temp/create-a-low-cost-emi-offer/#step2) to [Step 4](https://devguide.payu.in/temp-offers-integration/create-an-offer-temp/create-a-low-cost-emi-offer/#step4).

1. Review all the configuration added before you make the offer available to your customers.
2. Click the **Edit** button to return back to the corresponding page and update the configuration.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Screenshot-2022-02-23-at-8.32.06-PM-1024x573.png)

1. Click **Publish Offer** to make it available to customers.

<br />
