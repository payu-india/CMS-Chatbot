---
title: Flutter UPI Bolt UI SDK
deprecated: false
hidden: true
metadata:
  robots: index
---
PayU UPI Bolt UI SDK will provide a simpler and more efficient payment experience to the merchants. It will eliminate any third-party redirection and higher success rate. Profile management including accounts and balances for users. Enhancing the overall customer experience and decreasing customer drop-offs.

## Advantages

1. One-click payment journey and no hassle of redirection to a third-party UPI application.
2. Quick completion of transactions because of direct integration with the bank.
3. Seamless user experience to the customers with in-app payment.
4. Easy to integrate and get the advantage of existing customer profiles created with banks.
5. 5-6% higher success rate and better transaction conversion.
6. Merchants can take advantage of a complete user funnel to understand user behavior.

## User Journeys in PayU UPI Bolt

<Accordion title="Registration and Pay" icon="fa-folder">
  1. Merchant Application can do the User registration for customers who are coming first time for PayU UPI Bolt. The Registration can be done during the checkout process or it can be called in a separate user journey. In case of Merchant is using PayU Checkout Pro SDK, PayU will take care of customer registration.
  2. Once the registration process is initiated, the user will be asked to accept the SMS sending permissions required to verify the SIM card. If the phone has dual SIM, the SIM card selection screen will be shown to customers to select the specific SIM card.
  3. After the device verification, UPI ID creation and the Bank selection will be done. Add bank journey will be completed after adding a bank account connected to the same mobile number used for device verification.
  4. Finally, customers can do a transaction using the added bank account. In case the customer is using the bank account for the first time they will need to set the MPIN as well.
  5. Finally, customers can make a transaction using the added bank account. If the customer is using the bank account for the first time, he will also need to set the MPIN.

  <Image align="center" src="https://files.readme.io/477aa57e491d8be306be606858728a809e562aed4a65bef8663d03703a82d98f-0.jpg" alt="Flutter UPI Bolt UI SDK Integration Registration and Pay Flow" />
</Accordion>

<Accordion title="Pay" icon="fa-folder">
  1. Customers who are already registered with PayU UPI Bolt can make a One-click payment.
  2. The customer needs to select the already added bank account and enter the MPIN and the transaction will be completed.
  3. The customer can also check the balance before making a transaction to avoid low-balance transaction failure.

  <Image align="center" src="https://files.readme.io/b3050b0d3581a62b29ddccb4d183cf14f0251e6cbd033cea8916eae364209586-1.jpg" alt="Flutter UPI Bolt UI SDK Integration Pay Flow" />
</Accordion>

<Accordion title="Profile Management Journey" icon="fa-folder">
  1. Customers can add new bank accounts, set MPIN, change MPIN, reset MPIN, delete accounts, and check the balance of already added bank accounts.
  2. Transaction history can be seen and queries can be raised and resolved within the PayU UI Bolt SDK.
  3. Customers can see all the raised disputes from the Dispute history screen.
  4. Customers can also deregister their all accounts with PayU UI Bolt SDK.

  <Image align="center" src="https://files.readme.io/f6649179d1e3193799da08174d44e0d4a021da5b3bcfbf62b6c7863d13fd26ed-2.jpg" alt="Flutter UPI Bolt UI SDK Integration Registration and Profile Management Flow" />

</Accordion>
