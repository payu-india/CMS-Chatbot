---
title: Payment State Explanations
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
The following table provides description for each status of the transaction. You must map the order status using the payment state specified in the **Status** column of the following table. As Test environment (Sandbox) is a replica of the Production environment, you can push the code in production by just replacing account credentials and URL.

<block:parameters>
{
  "data": {
    "h-0": "Unmapped Status",
    "h-1": "Status",
    "h-2": "**Description**",
    "0-0": "auth",
    "0-1": "Success",
    "0-2": "Auth refers to the transaction which has been authorized from the bank and the amount has been debited from the customer’s bank account, but that amount is not captured at PayU’s end (reflects in your PayU Dashboard).",
    "1-0": "captured",
    "1-1": "Success",
    "1-2": "The transaction is successful.",
    "2-0": "userCancelled",
    "2-1": "Failure",
    "2-2": "This status is used when a transaction is canceled by the customer.",
    "3-0": "bounced",
    "3-1": "Failure",
    "3-2": "When a transaction is not completed by the customer. For example, the customer does not click **Pay Now** on the PayU Payment page (PayU Hosted Checkout) and forfeits the transaction. In such cases, the transaction as bounced.\nThis can happen due to various reasons: intent of the customer, Internet issues, etc.",
    "4-0": "dropped",
    "4-1": "Failure",
    "4-2": "When a transaction reaches PayU, the transaction is redirected to the respective payment gateway. The payment gateway sends the response back to PayU with the status of the transaction. In few instances, PayU not get any response from the payment gateway. In such cases, PayU marks the transaction as dropped.",
    "5-0": "failed",
    "5-1": "Failure",
    "5-2": "When a transaction gets failed, it can be due to several reasons, such as, failed payment gateway, failed from PayU, from issuing bank of the card, authentication failure, etc.",
    "6-0": "autoRefund",
    "6-1": "Failure",
    "6-2": "When PayU initiates refund for the transaction where PayU got success during reconciliation.",
    "7-0": "initiated",
    "7-1": "Pending",
    "7-2": "When the merchant lands on PayU’s page, the transaction status will be initiated.",
    "8-0": "in progress",
    "8-1": "Pending",
    "8-2": "When the customer clicks **Pay Now** on the PayU Payment page (PayU Hosted Checkout) and the transaction is routed to the 3DS page, and then the transaction status will be changed to \"In progress\".",
    "9-0": "pending",
    "9-1": "Pending",
    "9-2": "The pending state of a transaction occurs when a payment has been initiated but not yet completed. Further, it will be moved as per the payment gateway response, such as captured, failed, bounced, or dropped."
  },
  "cols": 3,
  "rows": 10,
  "align": [
    null,
    "left",
    null
  ]
}
</block:parameters>