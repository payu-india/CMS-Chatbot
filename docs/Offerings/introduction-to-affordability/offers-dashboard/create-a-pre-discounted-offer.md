---
title: Create a Pre-Discounted Offer
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  keywords:
    - PayU India Pre-Discounted Offer
    - Pre-Discounted Offer Setup
    - Pre-Discounted Offer Creation
    - Pre-Discounted Offer for PayU Checkout Integration
  robots: index
next:
  description: ''
---
Pre-discounted offers are applied at your (merchant) end and the transaction amount passed is the discounted transaction amount. PayU is primarily used for doing certain checks and validations rather than applying the discount itself. Pre-discounted offers help you with the following:

- Better user experience on the PayU Payment page (PayU Hosted Checkout) as the offer is already applied at your side, PayU will not be showing the list of offers on the PayU Payment page.
- Reconciliation and Settlements (offer engine back calculates original transaction amount, discount amount, and the net debit amount which can be used on reconciliation & settlements).
- The **Don’t allow transaction, if offer is not applicable** flag is enabled by default.

This procedure describes how to create a Prebuilt offer on PayU Dashboard and it is similar to creating a Discount offer.

> 📘
>
> **Note**: In Merchant Hosted Checkout integration, hide all other offers if Pre-Discounted offer is used.

***

### Steps to Create a No-Cost EMI Offer

1. [Add the basic details](#step-1-add-the-basic-details)
2. [Configure payment modes](#step-2-configure-payment-modes)
3. [Include the Offer rules](#step-3-include-the-offer-rules)
4. [Configure Offer Subvention Details](#step-4-configure-offer-subvention-details)
5. [Review of the Offer](#step-5-review-of-the-offer)

***

## Step 1: Add the basic details

1. Navigate to [.Offers Dashboard](doc:offers-dashboard).
2. Click **Create an Offer** at the top-right corner.

   The _Create New Offer_ page is displayed.


   <Image src="https://files.readme.io/94d041dbfbfc5faa76260a76e736cdbb4030553dddcde8c5ef3efeb9ca5d0f95-Screenshot_2025-06-03_at_10.16.03_AM.png" align="center" border={true} />

3. Select the discount type as **Pre-Discounted Offer**.

The Choose an Offer Type to get started.


<Image src="https://files.readme.io/02fa936e855901b9f6faf8bae897cf7ad501390a4e565567315abee82f0b5020-dashboard_prediscounted_offer_types.png" align="center" border={true} />


4. Select any of the following offer sub-types:
   - **Instant Discount**: The instant discount is applied and discounted amount is displayed on the PayU Payment page and other offers are not shown.
   - **Low-Cost EMI**: The low-cost EMI is applied and the EMI amount is displayed on the PayU Payment page and other offers are not shown.

 The _Basic Offer Details_ page is displayed.


<Image src="https://files.readme.io/09dec7da3915af1371413ad8eb9195dbaebacd7934c5ba93e97f54d311c001eb-Screenshot_2025-06-05_at_10.16.18_AM.png" align="center" border={true} />


5. Add the basic details. For more information, refer to [Create an Instant Discount or Cashback Offer](doc:create-an-offer).
6. After you complete the above details and click **Next**.

   The _Payment Options_ page is displayed.


<Image src="https://files.readme.io/20face5ca921ac455c7dd74ba8fb532e274b2ac4dd69b581d64b52b3072af1a7-dashboard-prediscounted-payment-options.png" align="center" border={true} />


> 📘 **Note**: When you are creating an offer, you can choose to save the incomplete offer details in the Draft state using the **Save as Draft & Exit** button at the top-right corner and publish it later.

## Step 2: Configure payment modes

1. Configure the payment modes.

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

2. Click **Next**.

The _Offer Rules_ page is displayed.


<Image src="https://files.readme.io/2e7610844659ed93bfa6380b4023a90f4ff3c2b5743acdbe9ed3a2eeb39c385c-dashboard-prediscounted-offer-rules.png" align="center" border={true} />


## Step 3: Include the Offer rules

1. Enter the offer rules and limitations on the _Set Offer Rules_ page. For more information, refer to [Create an Instant Discount or Cashback Offer](doc:create-an-offer#step-3-include-the-offer-rules).
2. After you complete the above details and click **Next**.

   The _Subvention Details_ page is displayed.

## Step 4: Configure Offer Subvention Details

1. Enter the subvention details in the _Subvention Details_ page. For more information, refer to [Create an Instant Discount or Cashback Offer](doc:create-an-offer#step-4-configure-offer-subvention-details).
2. After you complete the above details and click **Next**.

The _Preview Details_ page is displayed.


<Image src="https://files.readme.io/a87a0559ec1e51c8daed008b50a26c33c186b877accfc72a3a4bc72b15eb3aa5-dashboard-prediscounted-preview_page.png" align="center" border={true} />


## Step 5: Review of the Offer

The _Preview Details_ page summarizes the details you provided in Step 2 to Step 4.

1. Review all the configurations added before you make the offer available to your customers.
2. Click the **Edit** button to return back to the corresponding page and update the configuration.
3. Click **Publish** to make it available to customers.

<br />
