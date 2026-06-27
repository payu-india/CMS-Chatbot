---
title: Launch a Loyalty Program using Dashboard
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The Loyalty Rewards on Dashboard provides you with comprehensive tools to manage and analyse your loyalty programs, featuring key components like summary views, graphical representations, and detailed reports. It facilitates configurable settings, and easy navigation to boost customer engagement and optimize loyalty strategies. These settings help you easily configure the PayU Checkout page with PayU Hosted Checkout integration.

<Callout icon="📘" theme="info">
  ###

  **Enable Loyalty Edge**:

  Refer to [Enable Loyalty Edge](doc:enable-loyalty-edge) to enable Loyalty Edge. If you are not able to see it on Dashboard, contact you PayU Key Account Manager (KAM) or raise a ticket with [PayU Support](https://help.payu.in).
</Callout>

The Loyalty Rewards on PayU Dashboard provides the following features:

- **General**:
  - Highlights the potential benefits for merchants, such as increasing Average Revenue Per User (ARPU) and Customer Lifetime Value (CLTV).
  - A call-to-action (CTA) button available to guide merchants through the initial setup of their loyalty program.
  - Displays Gross Merchandise Value (GMV) associated with loyalty points, total points issued, and details on redemption transactions.
  - Highlights the number of customers who used points, new customers earning points for the first time, and the overall redemption rate.
- **Graphical Representation:** Provides a visual breakdown of redeemed and earned points on a day-to-day basis, enabling easy analysis and tracking of trends.
- **Loyalty Activity**: Offers the ability to filter or search loyalty activities based on user phone numbers, arranged in a paginated list. Displays detailed information such as transaction dates, event types (earn or redemption), and available loyalty points.
- **Burn Rule Display**: Displays a card with the current active burn rule, including the conversion ratio. Also,. provides option for you to edit and update the burn rule as needed.
- **Loyalty Settings:**: You can configure settings related to point expiry, customer limits for earning and redemption, and notifications for various loyalty events.

Steps to launch a loyalty program using PayU Dashboard:

1. [Setup Loyalty](#step-1-setup-loyalty)
2. [Create a New Campaign](#step-2-create-a-new-campaign)

## Step 1. Setup Loyalty

The _Set-up Loyalty_ page is designed to help you configure the loyalty programs by setting up how points are branded, and redeemed. It includes options for defining point naming, branding visuals, redemption rules, and allowing for a tailored loyalty experience that aligns with the merchant's brand and objectives.

<Callout icon="📘" theme="info">
  ###

  **Reference**:

  After you complete the setting up a loyalty, you can start creating campaigns. For more information, refer to [Create a New Campaign](doc:create-a-new-campaign).
</Callout>

To set up loyalty:

1. Log In to PayU Dashboard

2. Select **Loyalty and Offers Suite> Loyalty** on the navigation pane.

   The **Loyalty** page with **Loyalty Campaigns** tab is displayed.

3. Click **Edit Loyalty** at the top-right corner of the **Loyalty Campaigns** tab.

   A confirmation message is displayed similar to the following screenshot:


<Image src="https://files.readme.io/c424d38a1e5e50fc482a82b10480d5174bd31ef3efcd84a1441269c2b08e1193-setup-loyalty-update-confirmation.png" align="center" width="320px" border={true} />


4. Click **Proceed**.

The _Set-up Loyalty_ wizard is displayed with _Step 1 - Points Branding_ page.


<Image src="https://files.readme.io/ba91303d91a845bd16552cebd1431a9eb19b82a46c83ed596ad3f3c97fcfa74e-setup-loyalty-step1-points-branding.png" align="center" border={true} />


5. Enter a short name for your loyalty points in the  **Name Your Loyalty Points**  field that will be visible to your customers. For example, Star.

6. Select or customize an icon in the **Default Currency Icon:** field to visually represent your loyalty points.

7. Click **Save & Next**.

The _Step 2:Burn Loyalty_ page of  _Set-up Loyalty_ wizard is displayed.


<Image src="https://files.readme.io/559196081c40dd47d28806bcdad7d7a5bfac232e99af551e284f71bb199b711a-setup-loyalty-step2-burn-rules.png" align="center" border={true} />


8. Enter the following details to configure the redemption logic:

   | Field                                            | Description                                                                                                                                       |
   | ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Set Burn Ratio                                   | Define the conversion rate for redeeming points. For example, "50 Stars = 1 INR". It specifies how many points are needed to redeem for currency. |
   | Min. Transaction Amount To Redeem (optional)     | Specify the minimum transaction amount required for redeeming points.                                                                             |
   | Max. Transaction Amount To Redeem (optional)     | Specify the maximum transaction amount for which points can be redeemed.                                                                          |
   | Set Maximum Points a Customer Can Burn at a Time | Check this option to limit the maximum number of points a customer can redeem in a single transaction.                                            |



9. Click **Save & Next**.

The _Step 3: Earn Configuration_ page of  _Set-up Loyalty_ wizard is displayed.


<Image src="https://files.readme.io/a1349b0e19d9755645af06c9cdc9634e722a2bc4f7b6c98594b44ddaf99723d4-setup-loyalty-step3-earn-config.png" align="center" border={true} />


10. Select any of the following to specify earn points based on

- Final Payable amount
- Order amount

11. Specify the duration in days or when points will expire in the **Set Point Expiry** field. You may choose to leave blank for no expiry.

12. Click **Save & Publish**.

## Step 2. Create a New Campaign

To set up a campaign:

1. Log In to PayU Dashboard
2. Select **Loyalty and Offers Suite> Loyalty** on the navigation pane.


<Image src="https://files.readme.io/6b6fc209fd6a808256249f0d861beb23f921dd61013f4a230de9b26a0808bf89-dashboard-loyalty-campaign.png" align="center" border={true} />


3. Click **Setup Campaign** to begin creating a new campaign.

The _Create a New Campaign_ page is displayed.


<Image src="https://files.readme.io/4551b582583d830459a12bea52ef802e151ab07686d2be8f84f6099b0a574cf8-dashboard-loyalty-create-new-campaign.png" align="center" border={true} />


4. Enter the basic campaign details as described in the following table:

| Field             | Description                                                                                                 |
| ----------------- | ----------------------------------------------------------------------------------------------------------- |
| Campaign Name     | Enter a name for your campaign and this name will appear during checkout.                                   |
| Campaign Details  | Enter any specific details or terms and conditions. This will also be visible during checkout.              |
| Campaign Validity | Select either **Valid Forever** or **Occasional Validity** to set how long the campaign will remain active. |

5. Click **Save & Next**.

The _Payment options_ page is displayed.


<Image src="https://files.readme.io/48f751bbf782cde763866903276068d63790f3579851307492da807c92b30fd5-dashboard-loyaty-create-campaign-step2.png" align="center" border={true} />


6. Select the relevant payment modes to configure offer details that is explained in the corresponding tabs and then click **Save & Next** after you have selected payment options.


<Image src="https://files.readme.io/32dc30af2b03c890f39f4b3bfb5a1e36cf25a84630f62b8f4e6e6180ddd0cb63-dashboard-loyaty-create-campaign-step3.png" align="center" border={true} />


7. Configure the campaign settings as described in the following table:

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
        Earning Rule Type
      </td>

      <td>
        Select **Flat** or **Percentage** to define how points are earned per transaction.
      </td>
    </tr>

    <tr>
      <td>
        Fixed Points Per Transaction
      </td>

      <td>
        Enter the number of points awarded for each transaction if the "Flat" earning type is selected.
      </td>
    </tr>

    <tr>
      <td>
        Min. Transaction Amount
        (Optional)
      </td>

      <td>
        Enter the minimum transaction amount required to earn points.
      </td>
    </tr>

    <tr>
      <td>
        Max. Transaction Amount
        (Optional)
      </td>

      <td>
        Enter the maximum transaction amount for earning eligible points.
      </td>
    </tr>

    <tr>
      <td>
        Set Point Expiry
        (Optional)
      </td>

      <td>
        Enter the duration in days for point expiry, or leave blank to use the default expiry setting from loyalty configuration.
      </td>
    </tr>
  </tbody>
</Table>

8. Click **Show Advanced Options** at bottom and configure the following advance options (if required):


<Image src="https://files.readme.io/b3e011e5c462e0c97cf51d17d010f24e6c82791f9739765281ae9789576d54c5-dashboard-loyaty-create-campaign-step3-adv_options.png" align="center" border={true} />


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
        Budget Amount per User (optional)
      </td>

      <td>
        Enter the points limit you want to set per user for the campaign.
      </td>
    </tr>

    <tr>
      <td>
        Apply Campaign on Certain Products SKU
      </td>

      <td>
        Select this check box if the campaign should apply only to specific product SKUs, enabling targeted promotions.
      </td>
    </tr>

    <tr>
      <td>
        Allow Campaign on Specific Days
      </td>

      <td>
        Select this check box to restrict the campaign to operate on particular days, enabling scheduling flexibility.
      </td>
    </tr>

    <tr>
      <td>
        Set Overall Budget for the Campaign
      </td>

      <td>
        Select this check box to set a total points budget for the campaign, capping the total point distribution.
      </td>
    </tr>

    <tr>
      <td>
        Reset User Limits
      </td>

      <td>
        Select how often to reset user limits from the drop-down list, with the following options:

        - Do Not Reset
        - Every Day
        - Every Week
        - Every Month (Campaign Start Date)
        - Every Month (Calendar Month)
      </td>
    </tr>
  </tbody>
</Table>

9. Click **Save & Next**.
10. Click **Publish** to go live with the campaign.

## Manage Loyalty Edge Campaigns

You can check or update the details of an existing campaign and customer transactions as a result of a campaign as described in the following sections:

### View Campaign Transactions

To view the transactions due to campaign:

1. Navigate to the Loyalty Edge page.
2. Select the campaign for which you wish to view the transactions

The campaign details are displayed.


<Image src="https://files.readme.io/e4e1943690eab75eb01ade9c1897624a64e8a7705016be81c6d41a86232034cc-dashboard_campaign_details_view.png" align="center" border={true} />


3. Select the **Transactions** tab.


<Image src="https://files.readme.io/3a753fbed6ed886f02246fb26657c851bd1a54a15d0eb7b7eafd850bd4efb877-dashboard_campaign_transactions.png" align="center" border={true} />


4. Perform any of the following:
   - Use the **Filter** drop-down menu to filter the transactions.
   - Use the **Calendar** drop-down menu to view the transactions for a period.
   - Search using the transaction ID, order ID or phone number in the **Search** field.

### Update Campaign Details

To update the campaign details:

1. Navigate to the Loyalty Campaigns page.
2. Click the menu next to the campaign and select Edit similar to the following screenshot:


<Image src="https://files.readme.io/44cdca009b290ef1ec73a78c6a5307a25adc32223ee80bb83c5064c18edc494c-Screenshot_2025-06-04_at_12.42.45_PM.png" align="center" border={true} />


A confirmation message similar to the following screenshot is displayed.


<Image src="https://files.readme.io/21a4ba9613de94672c18888a09bd69d19a58ce3c1195e5265355e216031ed86d-dashboard_edit_campaign_confirmation.png" align="left" border={true} wrap={true} />


1. Click **Confirm**.
2. Enter the basic campaign details as described in the following table:

| Field             | Description                                                                                                 |
| ----------------- | ----------------------------------------------------------------------------------------------------------- |
| Campaign Name     | Enter a name for your campaign and this name will appear during checkout.                                   |
| Campaign Details  | Enter any specific details or terms and conditions. This will also be visible during checkout.              |
| Campaign Validity | Select either **Valid Forever** or **Occasional Validity** to set how long the campaign will remain active. |

5. Click **Save & Next**.

The _Payment options_ page is displayed.

6. Select the relevant payment modes to configure offer details that is explained in the corresponding tabs and then click **Save & Next** after you have selected payment options.
7. Configure the campaign settings as described in the following table:

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
        Earning Rule Type
      </td>

      <td>
        Select **Flat** or **Percentage** to define how points are earned per transaction.
      </td>
    </tr>

    <tr>
      <td>
        Fixed Points Per Transaction
      </td>

      <td>
        Enter the number of points awarded for each transaction if the "Flat" earning type is selected.
      </td>
    </tr>

    <tr>
      <td>
        Min. Transaction Amount
        (Optional)
      </td>

      <td>
        Enter the minimum transaction amount required to earn points.
      </td>
    </tr>

    <tr>
      <td>
        Max. Transaction Amount
        (Optional)
      </td>

      <td>
        Enter the maximum transaction amount for earning eligible points.
      </td>
    </tr>

    <tr>
      <td>
        Set Point Expiry
        (Optional)
      </td>

      <td>
        Enter the duration in days for point expiry, or leave blank to use the default expiry setting from loyalty configuration.
      </td>
    </tr>
  </tbody>
</Table>

8. Click **Show Advanced Options** at bottom and configure the following advance options (if required):

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
        Budget Amount per User (optional)
      </td>

      <td>
        Enter the points limit you want to set per user for the campaign.
      </td>
    </tr>

    <tr>
      <td>
        Apply Campaign on Certain Products SKU
      </td>

      <td>
        Select this check box if the campaign should apply only to specific product SKUs, enabling targeted promotions.
      </td>
    </tr>

    <tr>
      <td>
        Allow Campaign on Specific Days
      </td>

      <td>
        Select this check box to restrict the campaign to operate on particular days, enabling scheduling flexibility.
      </td>
    </tr>

    <tr>
      <td>
        Set Overall Budget for the Campaign
      </td>

      <td>
        Select this check box to set a total points budget for the campaign, capping the total point distribution.
      </td>
    </tr>

    <tr>
      <td>
        Reset User Limits
      </td>

      <td>
        Select how often to reset user limits from the drop-down list, with the following options:

        - Do Not Reset
        - Every Day
        - Every Week
        - Every Month (Campaign Start Date)
        - Every Month (Calendar Month)
      </td>
    </tr>
  </tbody>
</Table>

9. Click **Save & Publish**.

<br />
