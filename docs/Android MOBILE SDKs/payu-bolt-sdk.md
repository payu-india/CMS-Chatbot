---
title: Android UPI Bolt SDK
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
**Introduction**

The PayU UPI Bolt SDK delivers a seamless and efficient payment experience, boosting success rates and reducing transaction drop-offs for merchants. It eliminates the need for third-party redirections to complete payments. Features like one-time registration, profile management with account addition, balance checks, UPI PIN setup, and transaction history make this SDK a comprehensive solution for managing everything within the merchant's app.

The PayU UPI Bolt UI SDK, built on PayU UPI Bolt, provides a ready-made interface to go live in under a week with minimal development costs. Its modular design allows merchants to integrate features like registration, payment, profile management, or transaction history as needed.

**Advantages**

1. One-click payments with no redirection to third-party UPI apps.
2. Faster transactions via direct bank integration.
3. Seamless in-app payment experience for users.
4. Simple integration leveraging existing bank customer profiles.
5. 5-6% higher success rates and improved transaction conversions.
6. Complete user funnel insights for understanding customer behavior

**User Journeys in PayU UPI Bolt**

**a. Register and Pay**

1. First-time users need to register for the UPI Bolt SDK. Registration and payment can be completed during checkout or as separate user journeys.
2. During registration, users must grant SMS permissions to verify their device and SIM. For dual SIM phones, a selection screen will appear to choose the correct SIM.
3. Once the device is verified, the process moves to UPI ID creation and bank selection. Users complete the journey by linking a bank account tied to the verified mobile number.
4. Finally, transactions can be made using the linked account. For first-time users, setting up an MPIN will be required before completing a transaction.
5. For the first 24 hours, new users have a maximum transaction limit of ₹5000 on their registered bank account.

<Image align="center" src="https://files.readme.io/aaac0320d6f7078eb8528ca0afdfd64061bb2f8331cdf181b70c0661f36c0acf-R.jpg" />

**b. Repeat Payment**

1. Registered PayU UPI Bolt customers can make one-click payments seamlessly.
2. They simply select their added bank account, enter the MPIN, and complete the transaction.
3. Additionally, customers can set the MPIN for their bank account beforehand to prevent transaction cancellation.

<Image align="center" src="https://files.readme.io/ecb18268b712dfa6d06c9ca03bcb2b614d4b5b71b8aa99f29a9e80e00625b6de-P.jpg" />

**c. Profile Management and Transaction History**

1. Customers can manage their bank accounts within the PayU UPI Bolt SDK, including adding new accounts, setting, changing, or resetting MPINs, deleting accounts, and checking balances of linked accounts.
2. They can view transaction history, raise and resolve queries, and track all disputes through the Dispute History screen.
3. Customers also have the option to deregister all their accounts from the PayU UPI Bolt SDK.
4. Merchants can enforce direct access to Transaction History, UPI Account Management, and Queries/Dispute resolution from their app, bypassing the Profile Management bottom sheet if preferred.

<Image align="center" src="https://files.readme.io/5ca8ceb2d259d6e116529edca1e459c5255283ccc5e61148f621b290989879b0-M.jpg" />

To integrate PayU Bolt SDK, refer to [PayU Bolt SDK Integration](doc:payubolt-sdk-integration-native).

To integrate PayU Bolt UI SDK, refer to [PayU Bolt UI SDK Integration]()
