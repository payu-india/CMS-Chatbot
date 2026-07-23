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

1. [Add the basic details](#step-1-add-the-basic-details)
2. [Configure payment modes](#step-2-configure-payment-modes)
3. [Include the Offer rules](#step-3-include-the-offer-rules)
4. [Configure Offer Subvention Details](#step-4-configure-offer-subvention-details)
5. [Review of the Offer](#step-5-review-of-the-offer)

***

After you create an Instant Discount or Cashback Offer, you can collect payments from your customers using PayU Hosted (Non-seamless) or Merchant Hosted (Seamless) Checkout integration as described in the following sections:

* PayU Hosted
  * [Integrate with PayU Hosted Checkout - Offers](doc:payu-hosted-checkout-integration-with-offers)
* Merchant Hosted Checkout
  * [Instant Discount or Cashback using Merchant Hosted Checkout](doc:instant-discount-or-cashback-offers-integration-using-merchant-hosted-checkout)
  * [SKU-Based Offer using Merchant Hosted Checkout](doc:collect-payments-with-sku-based-offer-using-merchant-hosted-checkout-offers-integration)

***

## Step 1: Add the basic details

1. Navigate to [Offers Dashboard](doc:offers-dashboard).
2. Click **Create an Offer** at the top-right corner.

   The _Create New Offer_ page is displayed.

<Image align="center" border={true} src="https://files.readme.io/94d041dbfbfc5faa76260a76e736cdbb4030553dddcde8c5ef3efeb9ca5d0f95-Screenshot_2025-06-03_at_10.16.03_AM.png" className="border" />

3. Select the **Instant Discount** or **Cashback Offer** as the discount type.

  The _Basic Offer Details_ page is displayed.

<Image align="center" border={true} src="https://files.readme.io/5002858696d93c6edf465cf830ca8b20c69c06231342acce95fbcf8add81e0d2-Screenshot_2025-06-03_at_10.16.41_AM.png" className="border" />

4. Include the basic details as described in the following table and then click **Save & Process**:

| **Field**          | **Description**                                                                                                                                                                       |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Offer Title        | Enter a unique title for the offer. This would be displayed as the offer title on your Checkout page.                                                                                 |
| Offer Description  | Enter the offer text that would be shown to your customer at checkout (for PayU Hosted Checkout Integration transactions).                                                            |
| Offer Period       | Enter the offer validity date and time range. Your offer will be valid and visible to the customer between this time period. You can specify the time range up to the seconds detail. |
| Terms & Conditions | Enter the text content that should appear under the “Terms and Conditions” on the Checkout page for customers.                                                                        |

5. Select the **Create Generic Coupon Code** check box to create a coupon code.

The fields to collect coupon code details are displayed.

<Image align="center" border={true} src="https://files.readme.io/c35975feb22ef487cd1e4491153280ee8decae1fb092c2d66af7774becbaf267-dashboard_instant_disc_coupon_code_details.png" className="border" />

* Enter the coupon code in the **Set Coupon Code** field.
* Click the **Display coupon to customer on checkout** toggle button to display the coupon code on the PayU Checkout page.

6. After you complete the above details and click **Next**.

The _Payment Options_ page is displayed.

<Image align="center" border={true} src="https://files.readme.io/db5bf09d5216d77a25b7e3b81af9dc0de8974d6b0640404b069ab69f5986e04e-Screenshot_2025-06-03_at_10.41.42_AM.png" className="border" />

***

## Step 2: Configure payment modes

Select any of the following payment modes to configure offer details that is explained in the corresponding tabs:

> 📘 Note:
>
> You can configure one or multiple payment options for an offer. For example, the “HDFC Diwali Offer” can contain 10% discount for HDFC debit or credit cards, HDFC UPI, and a 3-month interest-free EMI for HDFC cards.

<Accordion title="Debit Cards" icon="fa-bell">
  1. Click the **Edit** button on the **Debit Cards** tile.

  The *Debit Card Details* page is displayed.

  <Image align="center" border={true} src="https://files.readme.io/f4debd9c82f8c3454c0956ecb20e30df6d4166551c291d521ea1abc13b88dee9-dashboard_payment_options_debit_card.png" />

  2. Perform any of the following based on the method you want to select the bank and network:

  <Table>
    <thead>
      <tr>
        <th>
          Channel
        </th>

        <th>
          Description
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td>
          Upload Bins to be include
        </td>

        <td>
          * Click **Download Sample File** if you are not having the sample file or CSV file template. The CSV file contains some sample BIN numbers (first 6 digits of Debit Card or Credit Cards), which you need to update according to your requirements.
          * Update the CSV file to include the BINs to be included.
          * Click the **Upload Bins** button upload the bins to be included.

            ![](https://files.readme.io/eb89a85f7a1920608e9f00e451d11cb8c92ce606734891c80383ad1a015c93e5-dashboard_payment_options_debit_card_upload_card_bin.png)

            **Note**: For the sample file, click **Download** .
        </td>
      </tr>

      <tr>
        <td>
          Bank
        </td>

        <td>
          Select the banks for which the offer is applicable from  **Select Banks** drop-down list.
          ![](https://files.readme.io/f963378804c89d83e901c6876e88d1cccc166fe077f22b06e2f6a62764291acc-dashboard_payment_options_debit_card_bank_options.png)

          **Note**: You can include exclusion list for offers. For the sample exclusion list file, click **Download** .
        </td>
      </tr>

      <tr>
        <td>
          Bank + Network
        </td>

        <td>
          <br />- Select the banks for which the offer is applicable from  **Select Banks** drop-down list.

          * Search and select a network from the **Select Networks** drop-down list.

            ![](https://files.readme.io/dbca7324d592ee3371239fb619e4517792135100fede381c8576b23a47be6e76-dashboard_payment_options_debit_card_bank_and_bin_options.png)

            **Note**: You can include exclusion list for offers. For the sample exclusion list file, click **Download** .
        </td>
      </tr>

      <tr>
        <td>
          Network
        </td>

        <td>
          Search and select a network from the **Select Networks** drop-down list.

          ![](https://files.readme.io/2463947de43fb77bec7c51b88e6073b7ab01af6ad74c1aa2b03775d4eb27db22-dashboard_payment_options_debit_card_network_options.png)

          **Note**: You can include exclusion list for offers. For the sample exclusion list file, click **Download** .
        </td>
      </tr>
    </tbody>
  </Table>

  3. Click the **Back** button to go back to the payment options list.
</Accordion>

<Accordion title="Credit Cards" icon="fa-card">
  1. Click the **Edit** button on the **Credit Cards**.

  The *Credit Card Details* page is displayed.

  <Image align="center" border={true} src="https://files.readme.io/76e11ce918eea78d776d4e1e58d725ede254db76915876b06c3da6c666aae885-dashboard_payment_options_credit_card.png" />

  2. Perform any of the following based on the method you want to select the bank and network:

  <Table>
    <thead>
      <tr>
        <th>
          **Channel**
        </th>

        <th>
          **Description**
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td>
          Upload Bins to be include
        </td>

        <td>
          * Click **Download Sample File** if you are not having the sample file or CSV file template. The CSV file contains some sample BIN numbers (first 6 digits of Debit Card or Credit Cards), which you need to update according to your requirements.
          * Update the CSV file to include the BINs to be included.
          * Click the **Upload Bins** button upload the bins to be included.![](https://files.readme.io/c955da31efdc6b4d2503d9a2ad5da6a86aa2285f8a0e754397c30c20c37bc880-dashboard_payment_options_upload_card_bin.png)**Note**: For the sample file, click **Download** .
        </td>
      </tr>

      <tr>
        <td>
          Bank
        </td>

        <td>
          Select the banks for which the offer is applicable from  **Select Banks** drop-down list.
          ![](https://files.readme.io/fc566b263b8296ca383f15ff3db5b34ec4f27be6d9b10ccb6876b53b7fc92747-dashboard_payment_options_select_bank.png)

          **Note**: You can include exclusion list for offers. For the sample exclusion list file, click **Download** .
        </td>
      </tr>

      <tr>
        <td>
          Bank + Network
        </td>

        <td>
          <br />- Select the banks for which the offer is applicable from  **Select Banks** drop-down list.

          * Search and select a network from the **Select Networks** drop-down list.
            ![](https://files.readme.io/5f46cc00126b4bb750577aaa70755da76171c5dbc5494a50babc0c70a90afbb3-dashboard_payment_options_select_bank_and_upload_bin.png)
            **Note**: You can include exclusion list for offers. For the sample exclusion list file, click **Download** .
        </td>
      </tr>

      <tr>
        <td>
          Network
        </td>

        <td>
          Search and select a network from the **Select Networks** drop-down list.

          ![](https://files.readme.io/86ce097797b4a7e3292feaec58a9ddc661a0b32dd9e528d4e61f9ff8cd2335b3-dashboard_payment_options_select_network.png)

          **Note**: You can include exclusion list for offers. For the sample exclusion list file, click **Download** .
        </td>
      </tr>
    </tbody>
  </Table>

  3. Click the **Back** button to go back to the *Payment Options* page.
</Accordion>

<Accordion title="UPI" icon="fa-terminal">
  1. Click the **Edit** button on the **UPIs** tile.

     The *UPI Details* page is displayed.

  <Image align="center" border={true} src="https://files.readme.io/ed2bf68ddd113d64d0b18c364319deca799bc85451af4e74c4a99388c8a2e057-dashboard_payment_options_upi.png" />

  2. Select the check boxes for the UPIs you wish to enable the offer from the \*\*Select UPI Channel \*\*drop-down list.
  3. Click the **Back** button to go back to the payment options list.
</Accordion>

<Accordion title="Wallets" icon="fa-copy">
  1. Click the **Edit** button on the the **Wallets** option.

     The *Select Wallets* page is displayed.

  <Image align="center" border={true} src="https://files.readme.io/a33d1d65b26720c45c414770c1adb2f0f7284fce6f0b1278b64d240eb79aa5de-dashboard_payment_options_wallets.png" />

  2. Select the check boxes for the wallets you wish to enable the offer.
  3. Click the **Back** button to return to the *Payment Options* page.
</Accordion>

<Accordion title="EMI" icon="<fa-line-columns">
  1. Click the **Edit** button on the the **EMI** option.

     The *EMI* Offer page is displayed.

  <Image align="center" border={true} src="https://files.readme.io/bdfb661ae9732fc1c7293a8bd54935d378efb781a8903804fbc19ef14ab1506b-dashboard_payment_options_emi.png" />

  2. For each of the following sub tabs, select the desired item on first column and **Tenures** column on which you wish to enable the offer. You can select all tenures of a specific bank and choose specific tenures for each bank.
     *  Credit Card
     * Debit Card
     * Cardless
  3. Select the **Set an exclusion/inclusion bin for the offer** check box to include/exclude the offer on a select list of BINs on the banks that were selected in Step 2 using the following steps in each **Exclusion Bin** and **Inclusion Bin** sub tabs:

  <Image align="center" border={true} src="https://files.readme.io/ffcb358c53def42d01a66edd5348191f536fd70af20a216e8e8c262b094a706d-dashboard_payment_options_emi_exclusion_list.png" />

  * Click **Download Sample File** if you are not having the sample file or CSV file template. The CSV file contains some sample BIN numbers (first 6 digits of Debit Card or Credit Cards), which you need to update according to your requirements.
  * Update the CSV or text file to include the BIN details. For updating the CSV file, you can use Microsoft Excel or any other Spreadsheet tool. 
  * Click the browse button in the **Add a list of bins that you want to include or exclude on offer** to upload the updated CSV file.

  4. Click the **Back** button to go to *Payment Options* page.
</Accordion>

<Accordion title="BNPL" icon="<fa-file-book">
  Select the **BNPL** option on the *Setup Payment options of your offer* page.

  The *Select BNPL Options* page is displayed.

  <Image align="center" src="https://files.readme.io/d5a47d52dd4c1b7f1eeae0b3c8e37fd2dff576352ae578b5108b2528042f4795-dashboard_payment_options_bnpl.png" />
</Accordion>

After you complete adding any one or combination of the offers involving various payment options, click **Next**.

> 📘 **References:**
>
> * No-Cost EMI offers can be created on Credit and Debit Card EMIs. For more information, refer to [Create a No-Cost EMI Offer](doc:create-a-no-cost-emi-offer).
> * Low-Cost EMI offers can create on Credit and Debit Card EMIs. For more information, refer to Create a Low-Cost EMI Offer.

The offer for the payment options you configured gets added to the Setup _Payment options of your offer_ page.

2. Select the applicable payment options and click **Next.**

The _Offer Rules_ page is displayed.

<Image align="center" border={true} src="https://files.readme.io/a169ac96a97658d1884f8047cd73ace82b112223eb6b67aae45e495c83288e23-Screenshot_2025-06-03_at_10.27.01_AM.png" className="border" />

> 📘 Note:
>
> When you are creating an offer, you can choose to save the incomplete offer details in the Draft state using the **Save as Draft & Exit** button at the top-right corner and publish it later.

## Step 3: Include the Offer rules

1. Select the **Flat Discount** or **Percentage** tab to specify the discount is in terms of a flat discount or percentage of the transaction amount.
2. Enter the following details on the _Set Offer Rules_ page.

| **Field**                                               | **Description**                                                                    |
| ------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Discount per transaction/Offer Percentage               | Specify the value that has to applied in in terms of discount or discount in flat. |
| Minimum transaction amount & Maximum transaction amount | Specify the threshold or range for a transaction to be applicable for the offer.   |

#### Offer Usage Guidelines

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
        **User Limits**
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Set the frequency for your customers to use this offer
      </td>

      <td>
        Select any of the following options from the drop-down list to specify the maximum number of transactions the user can avail this offer:

        * **Set unlimited**: Users can avail the offer for unlimited transactions.
        * **Custom**: Specify the custom limit up to which the users can avail the offer.
      </td>
    </tr>

    <tr>
      <td>
        Set Budget per user
      </td>

      <td>
        Click this toggle button (if required) and then enter the budget amount per user.
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

3. After you complete the above details and click **Next**.

The _Set Offer Subvention Details_ page is displayed.

<Image align="center" border={true} src="https://files.readme.io/a74a7875c37e0a2924fedb73fe7b047068bfb8fe6c7d2ca2aa1a755eabad1c65-dashboard_offers_subvention_step.png" className="border" />

## Step 4: Configure Offer Subvention Details

1. Select any of the following options from the **Set Offer Subvention Details** drop-down list.
   * **All offer settlements will be borne by me**: Choose this option if you want to make the cashback settlements by yourself to the customer.
   * I will share offer settlements with bank and brand:  Choose this option if you want to make the cashback settlements to bank or brand.
2. After you complete the above details and click **Next**.

   The _Preview Details_ page is displayed.

## Step 5: Review of the Offer

The _Preview of Cashback Offer_ page summarizes the details you provided in Step 2 to Step 4.

1. Review all the configurations added before you make the offer available to your customers.
2. Click the **Edit** button in the relevant areas return back to the corresponding page and update the configuration.

<Image align="center" border={true} src="https://files.readme.io/cc600ba18551a10ed4f013bce1e8ff67038cbd4f545d88f69216ae58f25ede19-dashboard_offers_preview_offer_step.png" className="border" />

3. Click **Publish** to make it available to customers.
