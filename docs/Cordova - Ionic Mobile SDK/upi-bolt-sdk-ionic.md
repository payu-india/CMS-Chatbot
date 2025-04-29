---
title: UPI Bolt UI SDK - Ionic
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
PayU UPI Bolt SDK will provide a simpler and more efficient payment experience to the merchants. It will eliminate any third-party redirection and higher success rate. Profile management including accounts and balances for users. Enhancing the overall customer experience and decreasing customer drop-offs. This section lists the benefits and various workflows for UPI Bolt UI SDK for Ionic. For the procedure to integrate UPI Bolt UI SDK for Ionic, refer to [UPI Bolt UI SDK Integration - Ionic](doc:upi-bolt-ui-sdk-integration-ionic).

## Benefits

* One-click payment journey and no hassle of redirection to a third-party UPI application.
* Quick completion of transactions because of direct integration with the bank.
* Seamless user experience to the customers with in-app payment.
* Easy to integrate and get the advantage of existing customer profiles created with banks.
* 5-6% higher success rate and better transaction conversion..
* Merchants can take advantage of a complete user funnel to understand user behavior. User Journeys in PayU UPI Bolt

## Workflow

### Registration and Pay

1. Merchant Application can do the User registration for customers who are coming first time for PayU UPI Bolt. The Registration can be done during the checkout process or it can be called in a separate user journey. In case of Merchant is using PayU Checkout Pro SDK, PayU will take care of customer registration.
2. Once the registration process is initiated, the user will be asked to accept the SMS sending permissions required to verify the SIM card. If the phone has dual SIM, the SIM card selection screen will be shown to customers to select the specific SIM card.
3. After the device verification, UPI ID creation and the Bank selection will be done. Add bank journey will be completed after adding a bank account connected to the same mobile number used for device verification.
4. Finally, customers can do a transaction using the added bank account. In case the customer is using the bank account for the first time they will need to set the MPIN as well.
5. Finally, customers can make a transaction using the added bank account. If the customer is using the bank account for the first time, he will also need to set the MPIN

<Image align="center" src="https://files.readme.io/2272c002c3f3d8270ef276a74f03cffae2ba4c2a98c696e8d4a9d727b87d69ef-upi-bolt-ionic-wf-registration-pay.jpeg" />

### Pay

1. Customers who are already registered with PayU UPI Bolt can make a One-click payment.
2. The customer needs to select the already added bank account and enter the MPIN and the transaction will be completed.
3. The customer can also check the balance before making a transaction to avoid low-balance transaction failure.

<Image align="center" src="https://files.readme.io/5b5d73b9166fcb358dccade47a547ff6a133e63a9d422a5872ed07a4ff9a2136-upi-bolt-ionic-wf-pay.jpeg" />

### Profile Management Journey

1. Customers can add new bank accounts, set MPIN, change MPIN, reset MPIN, delete accounts, and check the balance of already added bank accounts. 
2. Transaction history can be seen and queries can be raised and resolved within the PayU UI Bolt SDK. 
3. Customers can see all the raised disputes from the Dispute history screen.
4. Customers can also deregister their all accounts with PayU UI Bolt SDK.

<Image align="center" src="https://files.readme.io/6f0785d533c691c505b4f5a7d32306946fb9d11d1af17f4b44f2e3d5cbc752f2-upi-bolt-ionic-wf-profile-mgmt.jpeg" />
