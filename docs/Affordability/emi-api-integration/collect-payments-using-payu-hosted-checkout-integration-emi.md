---
title: PayU Hosted Checkout Integration
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: PayU Hosted Checkout Integration - EMI
  description: ''
  keywords:
    - Non-Seamless EMI PayU
    - PayU Hosted Checkout EMI
    - Credit Card EMI PayU Integration
    - PayU EMI Transaction Request
  robots: index
next:
  description: ''
---
Using the PayU Hosted Checkout (non-seamless) integration, you can collect payments with EMI.

This section describes how to collect payments with EMI and the customer journey on the PayU Payment page.

1. Make the transaction request to PayU. For more information on request, refer to [Collect Payment API - Merchant Hosted Checkout](ref:_payment_payu_hosted_checkout)
2. Customer Submits Payment Details on the _PayU_ Payment page using the following steps:
   - Select EMI on the PayU Payment page.

[block:image]
{
  "images": [
    {
      "image": [
        "https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/10/Screenshot-2022-10-28-at-1.24.54-PM-858x1024.png",
        null,
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]


- Select the **Credit Card EMI** option. Based on your eligibility you can choose other emi options too. For this example,we have chosen the Credit Card EMI of HDFC bank.

[block:image]
{
  "images": [
    {
      "image": [
        "https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/10/Screenshot-2022-10-27-at-3.55.47-PM-983x1024.png",
        null,
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]


- Enter the credit card details, then select the EMI tenure under the **EMI plans** section.

[block:image]
{
  "images": [
    {
      "image": [
        "https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/10/Screenshot-2022-10-27-at-3.59.11-PM-983x1024.png",
        null,
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]


- Enter the OTP sent to the mobile for card validation.

3. Check the response From PayU and look for the following params and their values:
   - **PG_TYPE**
   - **bankcode**