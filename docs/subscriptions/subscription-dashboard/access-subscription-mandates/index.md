---
title: Access Subscription Mandates
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: >-
    Access Subscription Mandates or Access Subscription Manual Mandates or
    Access Recurring Manual Mandates
  description: >-
    Learn how to access subscription mandates or mandates created manually using
    the PayU Dashboard. Follow our comprehensive guide to efficiently manage and
    streamline your recurring (SI) payment processes
  keywords:
    - access subscription mandates
    - ' access mandates created manually'
    - ' subscription mandates PayU'
    - ' recurring payments setup'
    - ' standing instruction setup'
    - ' subscription management'
    - ' PayU recurring billing'
    - ' SI mandates created manually'
    - ' subscription mandates created manually'
    - ' access recurring payments mandates'
    - standing instruction mandates created manually
  robots: index
next:
  description: ''
---
The **Mandates** tab on the Subscriptions Dashboard allows you to view all mandates done manually, check their statuses, and track the payment methods used, all in one place. It also provides a comprehensive view of all activities related to each mandate, detailing every recurring payment. It supports mandates created through various payment methods, such as Cards, eNACH, and UPI, making it accessible and convenient on a single platform.

<Image align="center" border={true} src="https://files.readme.io/68ddc2bd0da45682b940b391fcdd7778d29a825d90f486cd7e802b32858b95fb-dashboard-subscriptions-mandate.png" className="border" />

This part of the document includes the following sections:

* [Filter Subscription Mandates](doc:filter-subscription-mandates)
* [View a Mandate Details](doc:view-a-mandate-details)
* [View a Mandate Activity](doc:view-a-mandate-activity)
* [View Payments Received for a Mandate](doc:view-payments-received-for-a-mandate)
* [Download Memo for a Bounced Transaction](doc:download-memo-for-bounced-transaction)

<Callout icon="📘" theme="info">
  **Reference**: You can perform the following for mandates on Subscriptions Dashboard similar to Transactions Dashboard:

  * Export the subscription mandates. For more information, refer to [Export the Transaction Records](doc:export-the-transaction-records).
  * You can filter the mandates by last week, month or by custom date range.  For more information, refer to [View Transactions for a Custom Period](doc:view-transactions-for-a-custom-period).
  * Search the mandates based on the following parameters. For more information, refer to [Search the Transactions](doc:search-the-transactions).
    * PayU ID
    * Merchant Transaction ID
    * UMRN
    * Recurring PayU ID
</Callout>

## Filter and View a Mandate Details

Each mandate includes a drop-down or expandable menu that displays the associated recurring transactions. This drop-down provides key information, including the initiation dates of the recurring transactions, their status (such as Success or Failed), transaction IDs, and the amounts.

The **Mandates** has a  **Details** sub-tab shows the amount, identifiers like the PayU ID/UMRN Number and Merchant Transaction ID corresponding to the mandate on the top. You can also see the payment mode used, whether it’s Cards, Net Banking, or UPI. Also, the following sections display the various information:

* **Plan Details**: Provides subscription plan details: purpose, billing amount, billing cycle, and billing duration.
* **Payment Details**: Shows payment mode and instrument used:
  * **Card**: Last four digits, bank name, bank reference number.
  * **Enach**: Bank account number, bank name, bank reference number.
  * **UPI**: UPI ID, flow type.
* **Customer Details**: Includes customer information: name, email, mobile number, address.

To filter and view a mandate details:

1. Navigate to Subscriptions Dashboard and ensure that your are on **Mandates** tab.
2. Filter using any of the following fields on the top of the grid:
   * Subscription Created Date
   * Filter
   * Transaction ID
3. Click the drop-down or expandable menu for a mandate to view the details.

   <Image align="center" border={true} src="https://files.readme.io/e72831e78642d5a775c768a8a8f3e1258624cb1a2701548bd9bff95c8daf9b0e-dashboard-subscriptions-mandate-details.png" className="border" />
4. Select **View Details** from the **Actions** menu for the mandate that your wish to see the activity similar to the following screenshot:

<Image align="center" border={true} src="https://files.readme.io/be2f41972c972d7ec2672d1e3dd6d4b6d0f8351b7425e6f38b4bfbbc46312ba0-dashboard-subcitptions-mandate-actions-menu.png" className="border" />

5. Click the **Date** column header to sort recurring transactions in ascending or descending order based on the creation date.

The _Subscription Details_ page is displayed with the **Details** sub-tab selected.

<Image align="center" border={true} src="https://files.readme.io/a646071eadc9c2384deb59f1a0d8b8fbe55d28e541ceb9144dfd4ad3cd066d1e-dashboard-subscription-mandate-details.png" className="border" />

<br />
