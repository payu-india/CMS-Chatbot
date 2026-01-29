---
title: React-Native UPI Bolt UI SDK
deprecated: false
hidden: true
metadata:
  robots: index
---
PayU UPI Bolt SDK will provide a simpler and more efficient payment experience to the merchants. It will eliminate any third-party redirection and higher success rate. Profile management including accounts and balances for users. Enhancing the overall customer experience and decreasing customer drop-offs.

## Advantages

1. One-click payment journey and no hassle of redirection to a third-party UPI application.
2. Quick completion of transactions because of direct integration with the bank.
3. Seamless user experience to the customers with in-app payment.
4. Easy to integrate and get the advantage of existing customer profiles created with banks.
5. 5-6% higher success rate and better transaction conversion.
6. Merchants can take advantage of a complete user funnel to understand user behavior.

## User Journeys in PayU UPI Bolt

<Accordion title="Registration and Pay" icon="fa-folder">


<Image align="center" alt="UPI Bolt React Native Custome Journey for Registration and Pay" border={false} src="https://files.readme.io/a2d41854641a44082dcb2bc0e38a3bea213ef7c25ca0ce9429d8c8221581ab75-upi_bolt_reactnative_customer_journey_register_pay.jpeg" />

1. Merchant Application can do the User registration for customers who are coming first time for PayU UPI Bolt. The Registration can be done during the checkout process or it can be called in a separate user journey. In case of Merchant is using PayU Checkout Pro SDK, PayU will take care of customer registration.
2. Once the registration process is initiated, the user will be asked to accept the SMS sending permissions required to verify the SIM card. If the phone has dual SIM, the SIM card selection screen will be shown to customers to select the specific SIM card.
3. After the device verification, UPI ID creation and the Bank selection will be done. Add bank journey will be completed after adding a bank account connected to the same mobile number used for device verification.
4. Finally, customers can do a transaction using the added bank account. In case the customer is using the bank account for the first time they will need to set the MPIN as well.
5. Finally, customers can make a transaction using the added bank account. If the customer is using the bank account for the first time, he will also need to set the MPIN.

</Accordion>

<Accordion title="Pay" icon="fa-folder">

<br />

<Image align="center" alt="UPI Bolt React Native Custome Journey for Pay" border={false} src="https://files.readme.io/fad794f25f0f6b108bc694ee13f79f7a3b5de220f6f90990409f7267e86446bb-upi_bolt_reactnative_customer_journey_pay.jpeg" />

1. Customers who are already registered with PayU UPI Bolt can make a One-click payment.
2. The customer needs to select the already added bank account and enter the MPIN and the transaction will be completed.
3. The customer can also check the balance before making a transaction to avoid low-balance transaction failure.

<br />

</Accordion>

### Profile Management Journey

<Image align="center" alt="UPI Bolt React Native Custome Journey for Profile Management" border={false} src="https://files.readme.io/556315528c71a4e06f9cb9c4edb40fd651eef3c10b20a9418d569231877d98a7-upi_bolt_reactnative_customer_journey_profile_mgmt.jpeg" />

1. Customers can add new bank accounts, set MPIN, change MPIN, reset MPIN, delete accounts, and check the balance of already added bank accounts.
2. Transaction history can be seen and queries can be raised and resolved within the PayU UI Bolt SDK.
3. Customers can see all the raised disputes from the Dispute history screen.
4. Customers can also deregister their all accounts with PayU UI Bolt SDK.

## Steps to Integrate PayU Bolt SDK
