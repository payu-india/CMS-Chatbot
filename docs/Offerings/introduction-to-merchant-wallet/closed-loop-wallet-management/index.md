---
title: Closed-Loop Wallet Management
deprecated: false
hidden: false
metadata:
  title: Closed-Loop Wallet Management
  keywords:
    - Closed-Loop Wallet Management
    - clw
    - closed loop wallet management
  robots: index
---
**Closed-Loop Wallet API** enables businesses to implement merchant-specific digital wallet solutions that can only be used within the issuing merchant's website or mobile application. This prepaid payment instrument provides a controlled, branded payment experience that drives customer loyalty and repeat engagement.

Unlike semi-closed-loop wallets, closed-loop wallets are **not regulated by RBI** and operate within the merchant's ecosystem, making them ideal for businesses looking to create a seamless, integrated payment experience for their customers.

## Key Highlights

* Merchant-specific wallet usage only
* No RBI regulatory requirements
* Enhanced customer retention through integrated experience
* Cashback and loyalty program integration

## Implementation Benefits

* **Easy to Integrate:** Simplified implementation process
* **Merchant Control:** Complete control over wallet features and experience
* **Customer Retention:** Enhanced loyalty through integrated payment experience
* **Flexible Features:** Support for cashback, promotions, and loyalty programs

## Key Features

### Merchant-Specific Usage

The wallet can only be used on the issuing merchant's website or mobile application, ensuring complete control over the customer payment experience.

### One-Click Payments

* Instant payment processing using stored wallet balance
* Pre-fetched wallet balance display during checkout
* Seamless transaction completion without redirections

### Load & Pay Functionality

* On-the-fly wallet loading during checkout
* Flexible payment options when wallet balance is insufficient
* Immediate transaction processing after successful loading

### No Cash Withdrawal

Cash withdrawal is not permitted, ensuring funds remain within the merchant ecosystem for future purchases.

## Advantages

* **Enhanced Customer Retention**: Closed-loop wallets keep customers within your ecosystem, encouraging repeat purchases and building long-term customer relationships through integrated loyalty programs
* **Simplified Compliance**: Since closed-loop wallets are not regulated by RBI, businesses can implement wallet solutions without complex regulatory compliance requirements.
* **Complete Control**: Merchants have full control over the wallet experience, including branding, features, and customer journey optimization.
* **Increased Transaction Success**: With funds pre-loaded in the wallet, transaction success rates improve significantly compared to traditional payment methods.
* **No Limit**: No restriction on limit of wallet balance or usage of wallet supporting high ticket size transactions

### Load & Pay Journey

For Transaction Amount > Wallet Balance:

1. **Insufficient Balance Detection**
   System identifies when wallet balance is insufficient for the transaction

2. **Add Amount Option**
   Customer can choose to add the required amount to complete the purchase

3. **Payment Instrument Selection**
   Customer selects preferred payment method for wallet loading

4. **Transaction Completion**
   Wallet is loaded and original transaction is processed immediately

Closed loop wallet management involves the following APIs:

* <br />
  Closed loop wallet management involves the following APIs:
  * [Register Customer API](https://docs.payu.in/reference/register-customer-api): This API will be required by the merchants to register the customer for wallet.
  * [Retrieve Customer Record API](https://docs.payu.in/reference/retrieve-customer-record-api-1): This API will be required by Merchants to fetch customer details and balance present in the customer wallet.
  * [Update Profile API](https://docs.payu.in/reference/update-profile-api-closed-loop): This API will be used to update the customer profile details.
  * [Load API](https://docs.payu.in/reference/load-api-closed-loop-wallet): To load the money in the wallet post receiving success of the transaction.
  * Unload API: To spend the money from the wallet.
  * [PG Load Enquiry API](https://docs.payu.in/reference/pg-load-enquiry-api): This will be required to check status of the load API used in the top-up journey.
  * [Statement Inquiry API](https://docs.payu.in/reference/statement-inquiry-api-clw): This API can be used to fetch wallet transaction data between specific range.
  * [Change Wallet Status API](https://docs.payu.in/reference/change-wallet-status-api): This API used to change the card status of the card number of the customer.
