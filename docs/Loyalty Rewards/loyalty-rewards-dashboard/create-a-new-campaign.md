---
title: Create a New Campaign
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
Setting up a campaign involves the following steps:

1. [Basic details](#basic-details)
2. [Payment options](#payment-options)
3. [Campaign settings](#campaign-settings)
4. [Review and Publish](#review-and-publish)

## Basic details

1. Log In to PayU Dashboard
2. Select **Loyalty and Offers Suite> Loyalty** on the navigation pane.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/6b6fc209fd6a808256249f0d861beb23f921dd61013f4a230de9b26a0808bf89-dashboard-loyalty-campaign.png",
        "",
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]


1. Click **Setup Campaign** to begin creating a new campaign.

The _Create a New Campaign _ page is displayed.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/4551b582583d830459a12bea52ef802e151ab07686d2be8f84f6099b0a574cf8-dashboard-loyalty-create-new-campaign.png",
        "",
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]


1. Enter the basic campaign details as described in the following table:

| Field             | Description                                                                                                 |
| ----------------- | ----------------------------------------------------------------------------------------------------------- |
| Campaign Name     | Enter a name for your campaign and this name will appear during checkout.                                   |
| Campaign Details  | Enter any specific details or terms and conditions. This will also be visible during checkout.              |
| Campaign Validity | Select either **Valid Forever** or **Occasional Validity** to set how long the campaign will remain active. |

1. Click **Save & Next**.

The _Payment options_ page is displayed.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/48f751bbf782cde763866903276068d63790f3579851307492da807c92b30fd5-dashboard-loyaty-create-campaign-step2.png",
        "",
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]


## Payment options

Select any of the following payment modes to configure offer details that is explained in the corresponding tabs and then click **Save & Next** after you have selected payment options:

- All Payment Modes
- [Cards](#cards)
- [Net Banking](#net-banking)
- [UPI](#upi)
- [Wallets](#wallets)
- [EMI](#emi)
- [BNPL](#bnpl)

### Cards

1. Select any of the following options on the _Setup Payment options of your offer_ page:

- Credit Card
- Debit Card

2. Perform any of the following based on the method you want to select the bank and network:

[block:parameters]
{
  "data": {
    "h-0": "**Method**",
    "h-1": "**Description**",
    "0-0": "Select Bank and Networks",
    "0-1": " - Search and select the bank from the Select Banks and Select Networks drop-down list.  \n  \n- Search and select a network from the **Select Networks** drop-down list.",
    "1-0": "Specify the BIN numbers in CSV File",
    "1-1": "- Click **Download Sample File** if you are not having the sample file or CSV file template. The CSV file contains some sample BIN numbers (first 6 digits of Debit Card or Credit Cards), which you need to update according to your requirements.\n- Update the CSV or text file to include the BIN details. For updating the CSV file, you can use Microsoft Excel or any other Spreadsheet tool.\n- Click **Select .csv or .txt from your library** and select the CSV or text file."
  },
  "cols": 2,
  "rows": 2,
  "align": [
    null,
    null
  ]
}
[/block]


3. Select any of the following options in the **Set budget for credit card** field (optional):

**Note**: You can choose either specify count or amount based on the **Counter** or **Budget amount** option.

| Budget Type   | Description                                                                                                                                                                                    |
| :------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Counter       | Select this option and then specify the count in the **Counter Value** field. This offer will be enabled only for the transactions count as defined in the **Counter Value** field.            |
| Budget amount | Select this option and then specify the amount in the **Budget Amount** field. This offer will be enabled to customers until this budget amount is reached for your transactions cumulatively. |

4. Click **Add Payment Option**.

   The offer for the debit or credit card payment option gets added to the Setup _Payment options of your offer_ page.

### UPI

1. Select the **UPIs** option on the _Setup Payment options of your offer_ page.

   The _Select UPIs_ page is displayed.

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

1. Select the **Wallets** option on the _Setup Payment options of your offer_ page.

   The _Select Wallets_ page is displayed.
2. Select the check boxes for the wallets you wish to enable the offer.
3. Select any of the following options in the **Set budget for credit card** field (optional):

**Note**: You can choose either enter count or amount based on the **Counter** or **Budget amount** option.

| **Budget Type** | **Description**                                                                                                                                                                                |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Counter         | Select this option and then specify the count in the **Counter Value** field. This offer will be enabled only for the transactions count specified in the **Counter Value** field.             |
| Budget amount   | Select this option and then specify the amount in the **Budget Amount** field. This offer will be enabled to customers until this budget amount is reached for your transactions cumulatively. |

Click **Save & Next** after you have selected payment options.

The Earn Rules page is displayed.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/32dc30af2b03c890f39f4b3bfb5a1e36cf25a84630f62b8f4e6e6180ddd0cb63-dashboard-loyaty-create-campaign-step3.png",
        "",
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]


## Campaign settings

1. Configure the campaign settings as described in the following table:

[block:parameters]
{
  "data": {
    "h-0": "Field",
    "h-1": "Description",
    "0-0": "Earning Rule Type",
    "0-1": "Select **Flat** or **Percentage** to define how points are earned per transaction.",
    "1-0": "Fixed Points Per Transaction",
    "1-1": "Enter the number of points awarded for each transaction if the \"Flat\" earning type is selected.",
    "2-0": "Min. Transaction Amount  \n(Optional)",
    "2-1": "Enter the minimum transaction amount required to earn points.",
    "3-0": "Max. Transaction Amount  \n(Optional)",
    "3-1": "Enter the maximum transaction amount for earning eligible points.",
    "4-0": "Set Point Expiry  \n(Optional)",
    "4-1": "Enter the duration in days for point expiry, or leave blank to use the default expiry setting from loyalty configuration."
  },
  "cols": 2,
  "rows": 5,
  "align": [
    null,
    null
  ]
}
[/block]


1. Click **Show Advanced Options** at bottom and configure the following advance options (if required):

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/b3e011e5c462e0c97cf51d17d010f24e6c82791f9739765281ae9789576d54c5-dashboard-loyaty-create-campaign-step3-adv_options.png",
        "",
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]


[block:parameters]
{
  "data": {
    "h-0": "Field",
    "h-1": "Description",
    "0-0": "Budget Amount per User (optional)",
    "0-1": "Enter the points limit you want to set per user for the campaign.",
    "1-0": "Apply Campaign on Certain Products SKU",
    "1-1": "Select this check box if the campaign should apply only to specific product SKUs, enabling targeted promotions.",
    "2-0": "Allow Campaign on Specific Days",
    "2-1": "Select this check box to restrict the campaign to operate on particular days, enabling scheduling flexibility.",
    "3-0": "Set Overall Budget for the Campaign",
    "3-1": "Select this check box to set a total points budget for the campaign, capping the total point distribution.",
    "4-0": "Reset User Limits",
    "4-1": "Select how often to reset user limits from the drop-down list, with the following options:  \n  \n- Do Not Reset\n- Every Day\n- Every Week\n- Every Month (Campaign Start Date)\n- Every Month (Calendar Month)"
  },
  "cols": 2,
  "rows": 5,
  "align": [
    null,
    null
  ]
}
[/block]


1. Click **Save & Next**.

## Review and Publish

Click **Publish **to go live with the campaign.