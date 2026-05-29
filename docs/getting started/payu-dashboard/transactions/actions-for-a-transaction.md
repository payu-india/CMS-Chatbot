---
title: Actions for a Transaction
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Actions for a Transaction
  description: >-
    Track, search, filter, and export PayU Dashboard transactions. View individual payment details, success rates, and transaction history for your merchant account in India. Covers Actions for a Transaction.
  robots: index
  keywords:
    - payu dashboard transactions guide
    - view payment transactions payu merchant dashboard
    - payu transaction search filter export
    - payment gateway transaction history payu dashboard
    - payu dashboard transaction details page
    - merchant transaction reports payu india
    - payu dashboard track transactions guide
    - payment gateway merchant dashboard payu vs razorpay cashfree
    - payu transaction export csv dashboard
    - payu dashboard transaction success rate
next:
  description: ''
---
The **Actions** option enables you to copy the customer email for your next action.

<Image align="center" alt="Actions for a Transaction illustration" className="border" border={true} src="https://files.readme.io/58ab0ba-Screenshot_2023-09-22_at_7.28.40_PM.png" />

* **Authorize**: After end-user has entered Card/Account credentials bank checks for availability of Credit Limit or Account balance to authorize the transaction as valid.
* **Capture**: If an authorized (explained before) transaction is not captured automatically, the merchant can capture them manually to get payments credited to their account.
* **Cancel**: An authorized Transaction can be cancelled to get the money refunded in the customer account. The cancel function does not work for Captured transactions.
* **Refund/ Partial Refund**: Captured transactions can be refunded back to the customer using this function. Even Partial refunds are possible. A transaction is refunded owing to many reasons like product/service non-availability, customer request, etc.
* **Chargeback**: A Chargeback or dispute request is raised by the customer to issuing bank, owing to many reasons like a fraud transaction or unsatisfactory product/service delivery, etc.
* **Bounced**: The customers who did not click on Pay Now/Make Payment button on PayU Payment Page.
* **Dropped**: Customer who did not receive any status revert from Bank. Could be due to various reasons like 3D Secure Password not being available, Bank server downtime, the problem with an internet connection, etc.
* **Failed by Bank**: A transaction not authorized by the bank due to reasons like Invalid Credentials, Credit Limit exhausted, etc.
* **User Cancelled**: Transaction cancelled by the customer at PayU payment page via Cancel Button.
