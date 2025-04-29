---
title: Create a Payment Link with SI
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
You can create a payment link with Standing Instruction on PayUBiz Dashboard and send it to your customer. After the customer enters his card details, the Standing Instruction or recurring payment is enabled or registered.

To create a payment link with Standing Instruction on PayUBiz Dashboard:

1. Log on to PayUBiz Dashboard.
2. Select **New Email Invoice** from the menu of the left pane.

   The _New Invoice_ popup page is displayed.

[block:image]
{
  "images": [
    {
      "image": [
        "https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/PayUBizDasgh_Home-2-1024x615.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "552px"
    }
  ]
}
[/block]

[block:image]
{
  "images": [
    {
      "image": [
        "https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/PayUBizDash_New_Email_Invoice_First_Page-1024x733.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "552px"
    }
  ]
}
[/block]

3. Provide the the basic details as described in the following table:

| **Field**      | **Description**                                   |
| -------------- | ------------------------------------------------- |
| Name           | Enter the name of your customer.                  |
| Transaction ID | Enter the transaction ID for the transaction.     |
| Email ID       | Enter the customer email ID.                      |
| Description    | Enter the description of the transaction details. |
| Amount         | Enter the transaction amount.                     |
| Mobile No      | Enter the customer’s mobile number.               |

4. Scroll down the _New Invoice_ pop-up page to enable the Standing Instructions and provide the additional details.

[block:image]
{
  "images": [
    {
      "image": [
        "https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/PayuBiz_DB_New_Email_Invoice-1-1024x733.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "552px"
    }
  ]
}
[/block]

5. Provide the Standing Instructions details as described in the following table:

[block:parameters]
{
  "data": {
    "h-0": "**Field**",
    "h-1": "**Description**",
    "0-0": "SI credential",
    "0-1": "Enter the SI credential provided by PayU to you (merchant).",
    "1-0": "Send Reminder",
    "1-1": "Select this check box and perform the following:  \n_ Use the first drop-down list to configure the frequency.  \n_ Select the period in the second drop-down list.  \n\\* Select the period duration in the third drop-down list.",
    "2-0": "Set Expiry",
    "2-1": "Select this check box and perform the following:  \n_ Use the date selector to configure the expiry date of the Standing Instruction.  \n_ Enter the time of expiry in the second field on the specified date.",
    "3-0": "Enable SI",
    "3-1": "Select this check box to enable Standing Instruction for this transaction.",
    "4-0": "Billing Amount",
    "4-1": "Enter the billing amount that must be collected using Standing Instruction.",
    "5-0": "Billing Currency",
    "5-1": "Select the currency for the transaction.",
    "6-0": "Billing Interval",
    "6-1": "Select the billing interval from the drop-down list.",
    "7-0": "Billing Cycle",
    "7-1": "Select the billing cycle from the drop-down list.",
    "8-0": "Payment Expiry",
    "8-1": "Select the payment expiry date using the date selector."
  },
  "cols": 2,
  "rows": 9,
  "align": [
    null,
    null
  ]
}
[/block]

6. Click **Confirm**.