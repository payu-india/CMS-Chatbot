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
**Closed-Loop Wallet API** enables businesses to implement merchant-specific digital wallet solutions that can only be used within the issuing merchant's website or mobile application. This prepaid payment instrument provides a controlled, branded payment experience that drives customer loyalty and repeat engagement.

Unlike semi-closed-loop wallets, closed-loop wallets are **not regulated by RBI** and operate within the merchant's ecosystem, making them ideal for businesses looking to create a seamless, integrated payment experience for their customers.

Closed loop wallet management involves the following APIs:

* [Create Wallet/Card API](ref:create-walletcard-api): This API will be required by the merchants to register the customer for wallet.
* [Retrieve Customer Record API](ref:retrieve-customer-record-api): This API will be required by Merchants to fetch customer details and balance present in the customer wallet.
* [Update Profile API](ref:update-profile-api-wallet): This API will be used to update the customer profile details.
* [Load API](ref:l): To load the money in the wallet post receiving success of the transaction.
* [Unload API](ref:unload-api): To spend the money from the wallet.
* [Check Status API](ref:check-status-api): This will be required to check status of the load API used in the top-up journey.
* [Statement Inquiry API](ref:statement-inquiry-api): This API can be used to fetch wallet transaction data between specific range.
* [Change Card Status API](ref:change-card-status-api): This API used to change the card status of the card number of the customer.
