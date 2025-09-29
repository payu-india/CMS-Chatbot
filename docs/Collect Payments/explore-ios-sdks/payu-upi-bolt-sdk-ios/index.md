---
title: iOS UPI Bolt SDK
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
PayU UPI Bolt SDK will provide a simpler and more efficient payment experience to the merchants. It will eliminate any third-party redirection and higher success rate. Profile management including accounts and balances for users. Enhancing the overall customer experience and decreasing customer drop-offs. This section describes the advantages and user journeys. For steps to integrate UPI Bolt UI, refer to [UPI Bolt UI Integration](doc:upi-bolt-ui-integration-ios-bolt-sdk).

## UPI Bolt UI advantages

1. One-click payment journey and no hassle of redirection to a third-party UPI application.
2. Quick completion of transactions because of direct integration with the bank.
3. Seamless user experience to the customers with in-app payment.
4. Easy to integrate and get the advantage of existing customer profiles created with banks.
5. 5-6% higher success rate and better transaction conversion..
6. Merchants can take advantage of a complete user funnel to understand user behavior. 

## UPI Bolt UI user journeys

### Registration and Pay

1. Merchant Application can do the User registration for customers who are coming first time for PayU UPI Bolt. The Registration can be done during the checkout process or it can be called in a separate user journey. In case of Merchant is using PayU Checkout Pro SDK, PayU will take care of customer registration.
2. Once the registration process is initiated, the user will be asked to accept the SMS sending permissions required to verify the SIM card.  If the phone has dual SIM, the SIM card selection screen will be shown to customers to select the specific SIM card.
3. After the device verification, UPI ID creation and the Bank selection will be done. Add bank journey will be completed after adding a bank account connected to the same mobile number used for device verification.
4. Finally, customers can do a transaction using the added bank account. In case the customer is using the bank account for the first time they will need to set the MPIN as well. 

<Image align="center" src="https://files.readme.io/6c8ab77aaa068c2667ab98f46c81e24f881e3255566bdff3d6bb84130587dd4f-bolt_reg_and_pay_flow.jpeg" />

### Pay

1. Customers who are already registered with PayU UPI Bolt can make a One-click payment.
2. The customer needs to select the already added bank account and enter the MPIN and the transaction will be completed.
3. The customer can also check the balance before making a transaction to avoid low-balance transaction failure. 

<Image align="center" src="https://files.readme.io/253c320479271a77460a628915a381d0fcfbfc1cab71e93e46704127689b382a-bolt_pay_flow.jpeg" />

### Profile Management Journey

1. Customers can add new bank accounts, set MPIN, change MPIN, reset MPIN, delete accounts, and check the balance of already added bank accounts. 
2. Transaction history can be seen and queries can be raised and resolved within the PayU UI Bolt SDK. 
3. Customers can see all the raised disputes from the Dispute history screen.
4. Customers can also deregister their all accounts with PayU UI Bolt SDK.

<Image align="center" src="https://files.readme.io/85fc63476b9a08cd16d8d51d5e3f03c1744f82d0ce104186286268ae16ece310-bolt_profile_mgmt_flow.jpeg" />
