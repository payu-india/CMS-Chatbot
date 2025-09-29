---
title: Manage Loyalty Edge Campaigns
deprecated: false
hidden: true
metadata:
  robots: index
---
You can check or update the details of an existing campaign and customer transactions as a result of a campaign as described in the following sections:

* [View Campaign Transactions](##view-campaign-transactions)
* [Update Campaign Details](#update-campaign-details)

## View Campaign Transactions

To view the transactions due to campaign:

1. Navigate to the Loyalty Edge page.
2. Select the campaign for which you wish to view the transactions

The campaign details are displayed.

<Image align="center" className="border" border={true} src="https://files.readme.io/e4e1943690eab75eb01ade9c1897624a64e8a7705016be81c6d41a86232034cc-dashboard_campaign_details_view.png" />

3. Select the **Transactions** tab.

<Image align="center" className="border" border={true} src="https://files.readme.io/3a753fbed6ed886f02246fb26657c851bd1a54a15d0eb7b7eafd850bd4efb877-dashboard_campaign_transactions.png" />

4. Perform any of the following:
   * Use the **Filter** drop-down menu to filter the transactions.
   * Use the **Calendar** drop-down menu to view the transactions for a period.
   * Search using the transaction ID, order ID or phone number in the **Search** field.

## Update Campaign Details

To update the campaign details:

1. Navigate to the Loyalty Campaigns page.
2. Click the menu next to the campaign and select Edit similar to the following screenshot:

<Image align="center" className="border" border={true} src="https://files.readme.io/44cdca009b290ef1ec73a78c6a5307a25adc32223ee80bb83c5064c18edc494c-Screenshot_2025-06-04_at_12.42.45_PM.png" />

A confirmation message similar to the following screenshot is displayed.

<Image align="left" className="border" border={true} src="https://files.readme.io/21a4ba9613de94672c18888a09bd69d19a58ce3c1195e5265355e216031ed86d-dashboard_edit_campaign_confirmation.png" />

1. Click **Confirm**.
2. Enter the basic campaign details as described in the following table:

| Field             | Description                                                                                                 |
| ----------------- | ----------------------------------------------------------------------------------------------------------- |
| Campaign Name     | Enter a name for your campaign and this name will appear during checkout.                                   |
| Campaign Details  | Enter any specific details or terms and conditions. This will also be visible during checkout.              |
| Campaign Validity | Select either **Valid Forever** or **Occasional Validity** to set how long the campaign will remain active. |

5. Click **Save & Next**.

The *Payment options* page is displayed.

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

        * Do Not Reset
        * Every Day
        * Every Week
        * Every Month (Campaign Start Date)
        * Every Month (Calendar Month)
      </td>
    </tr>
  </tbody>
</Table>

9. Click **Save & Publish**.