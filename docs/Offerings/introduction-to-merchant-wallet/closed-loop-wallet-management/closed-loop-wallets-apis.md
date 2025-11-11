---
title: Closed-Loop Wallets APIs
deprecated: false
hidden: false
metadata:
  robots: index
---
Closed-loop wallets management involves the following APIs:

* [Register Customer API](https://docs.payu.in/reference/register-customer-api): This API will be required by the merchants to register the customer for wallet.
* [Retrieve Customer Record API](https://docs.payu.in/reference/retrieve-customer-record-api-1): This API will be required by Merchants to fetch customer details and balance present in the customer wallet.
* [Update Profile API](https://docs.payu.in/reference/update-profile-api-closed-loop): This API will be used to update the customer profile details.
* [Load API](https://docs.payu.in/reference/load-api-closed-loop-wallet): To load the money in the wallet post receiving success of the transaction.
* [PG Load API](ref:pg-load-api): To create a credit transaction entry through a payment gateway.
* [PG Load Enquiry API](https://docs.payu.in/reference/pg-load-enquiry-api): This will be required to check status of the load API used in the top-up journey.
* [Statement Inquiry API](https://docs.payu.in/reference/statement-inquiry-api-clw): This API can be used to fetch wallet transaction data between specific range.
* [Change Wallet Status API](https://docs.payu.in/reference/change-wallet-status-api): This API used to change the card status of the card number of the customer.

<Callout icon="📘" theme="info">
  **Note**: To unload your wallet, refer to [Seamless Debit Integration - CLW](https://docs.payu.in/docs/seamless-debit-integration-clw) or [PayU Hosted Check-out Integration - CLW](https://docs.payu.in/docs/pay-hosted-checkout-merchant-integration-merchant-wallet) based on the integration.
</Callout>
