---
title: Semi-Closed or Open Loop Wallets
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
This part of the document includes the overview and advantages of Semi-Closed or Open Loop Wallet Management APIs:

### Wallet/Card management

- Co-Branded cards with PayU PPI as issuer with Rupay and Master
- Virtual/Physical card, personalized / non-personalized card availability
- Single and multi-wallet support
- API and SDK Availability for Integration
- Under RBI purview and compliance handled by PayU as PPI Issuer

### Wallet/Card Redemption

- Click Payment, Pre- Integrated with PayU PG
- Reloadable using other payment methods / Just In Time Funding
- Transaction Limit and Beneficiary Management

### Customer Incentive

- Pre-Integrated with PayU’s offer engine
- Cashback rule creation and redemption
- Redeem Cashback with other wallet balance

### Report & analytics

- Reports availability through Portal / Email
- Get customized reports as per the requirement

Semi-Closed or Open Loop Wallet/Card can be used at websites/app where the issuing merchant’s wallets are allowed.  This involves the following APIs:

- [Create Wallet/Card API](ref:create-walletcard-api):  This API will be required by the merchants to register the customer for wallet
- [Retrieve Customer Record API](ref:retrieve-customer-record-api): This API will be required by Merchants to fetch customer details and balance present in the customer wallet.
- [Update Profile API](ref:update-profile-api-wallet): This API will be used to update the customer profile details.
- [Load API](ref:load_api_hexawallet): To load the money in the wallet post receiving success of the transaction.
- [Unload API](ref:unload-api): To spend the money from the wallet.
- [Check Status API](ref:check-status-api): This will be required to check status of the load API used in the top-up journey.
- [Statement Inquiry API](ref:statement-inquiry-api): This API can be used to fetch wallet transaction data between specific range
- [Change Card Status API](ref:change-card-status-api): This API used to change the card status of the card number of the customer.
- [Block Card API](ref:block-card-api): This API is used to block the customer card. Card can be blocked temporarily or permanent basis merchant use-case.
- [Unblock Card API](ref:unblock-card-api): This API can be used to unblock card.
- [Link Card API](ref:link-card-api): This API is used to activate/link card in the system link it to a customer.
- [Verify Cardholder API](ref:verify-cardholder-api): This API is used to validate the cardholder’s details before allowing the cardholder to view or perform any critical/sensitive activities like initiating KYC or setting PIN etc.
- [Reset PIN API](ref:reset-pin-api): This API is used when a cardholder forgot his existing PIN and wants to reset the PIN.
- [Card Inquiry API](ref:card-inquiry-api): This API is used to retrieve the summary of the card. e.g. cardholder information, balance on the card etc.
- [Create Beneficiary API](ref:create-beneficiary-api): This API is used for creation of beneficiary.
- [Fetch Beneficiary API](ref:fetch-beneficiary-api):  This API is used for fetching beneficiary details.
- [Update Beneficiary API](ref:update-beneficiary-api): API is used to update the beneficiary details.
- [Delete Beneficiary API](ref:delete-beneficiary-api): This API is used for deletion of beneficiary.
- [Fund Transfer API](ref:fund-transfer-api): This API is used to transfer funds.

<Callout icon="📘" theme="info">
  ###

  **Note**: If card is permanently blocked, it can’t be unblocked using the **Unblock Card** API.
</Callout>

<br />
