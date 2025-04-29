---
title: Actions for a Transaction
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
The **Actions** option enables you to copy the customer email for your next action.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/58ab0ba-Screenshot_2023-09-22_at_7.28.40_PM.png",
        null,
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]


- **Authorize**: After end-user has entered Card/Account credentials bank checks for availability of Credit Limit or Account balance to authorize the transaction as valid.
- **Capture**: If an authorized (explained before) transaction is not captured automatically, the merchant can capture them manually to get payments credited to their account.
- **Cancel**: An authorized Transaction can be cancelled to get the money refunded in the customer account. The cancel function does not work for Captured transactions.
- **Refund/ Partial Refund**: Captured transactions can be refunded back to the customer using this function. Even Partial refunds are possible. A transaction is refunded owing to many reasons like product/service non-availability, customer request, etc.
- **Chargeback**: A Chargeback or dispute request is raised by the customer to issuing bank, owing to many reasons like a fraud transaction or unsatisfactory product/service delivery, etc.
- **Bounced**: The customers who did not click on Pay Now/Make Payment button on PayU Payment Page.
- **Dropped**: Customer who did not receive any status revert from Bank. Could be due to various reasons like 3D Secure Password not being available, Bank server downtime, the problem with an internet connection, etc.
- **Failed by Bank**: A transaction not authorized by the bank due to reasons like Invalid Credentials, Credit Limit exhausted, etc.
- **User Cancelled**: Transaction cancelled by the customer at PayU payment page via Cancel Button.