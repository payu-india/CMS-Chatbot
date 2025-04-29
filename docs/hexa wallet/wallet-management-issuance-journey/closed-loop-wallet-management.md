---
title: Closed-Loop Wallet Management
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
Closed-Loop Wallet can be used only at the issuing merchant’s website/app.

Closed loop wallet management involves the following APIs:

* [Create Wallet/Card API](ref:create-walletcard-api):  This API will be required by the merchants to register the customer for wallet.
* [Retrieve Customer Record API](ref:retrieve-customer-record-api): This API will be required by Merchants to fetch customer details and balance present in the customer wallet.
* [Update Profile API](ref:update-profile-api-wallet): This API will be used to update the customer profile details.
* [Load API](ref:l): To load the money in the wallet post receiving success of the transaction.
* [Unload API](ref:unload-api): To spend the money from the wallet.
* [Check Status API](ref:check-status-api): This will be required to check status of the load API used in the top-up journey.
* [Statement Inquiry API](ref:statement-inquiry-api): This API can be used to fetch wallet transaction data between specific range.
* [Change Card Status API](ref:change-card-status-api): This API used to change the card status of the card number of the customer.
