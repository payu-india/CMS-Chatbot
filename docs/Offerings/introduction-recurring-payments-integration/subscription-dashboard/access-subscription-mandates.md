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


<Image src="https://files.readme.io/68ddc2bd0da45682b940b391fcdd7778d29a825d90f486cd7e802b32858b95fb-dashboard-subscriptions-mandate.png" align="center" border={true} />


This part of the document includes the following sections:

- [Filter and View a Mandate Details](https://docs.payu.in/docs/access-subscription-mandates?isFramePreview=true#filter-and-view-a-mandate-details)
- [View a Mandate Activity](https://docs.payu.in/docs/access-subscription-mandates?isFramePreview=true#view-a-mandate-activity)
- [View Payments Received for a Mandate](https://docs.payu.in/docs/access-subscription-mandates?isFramePreview=true#view-payments-received-for-a-mandate)
- [Download a Memo for a Bounced Transacton](https://docs.payu.in/docs/access-subscription-mandates?isFramePreview=true#download-a-memo-for-a-bounced-transacton)

<Callout icon="📘" theme="info">
  ###

  **Reference**: You can perform the following for mandates on Subscriptions Dashboard similar to Transactions Dashboard:

  - Export the subscription mandates. For more information, refer to [Export the Transaction Records](doc:export-the-transaction-records).
  - You can filter the mandates by last week, month or by custom date range.  For more information, refer to [View Transactions for a Custom Period](doc:view-transactions-for-a-custom-period).
  - Search the mandates based on the following parameters. For more information, refer to [Search the Transactions](doc:search-the-transactions).
    - PayU ID
    - Merchant Transaction ID
    - UMRN
    - Recurring PayU ID
</Callout>

## Filter and View a Mandate Details

Each mandate includes a drop-down or expandable menu that displays the associated recurring transactions. This drop-down provides key information, including the initiation dates of the recurring transactions, their status (such as Success or Failed), transaction IDs, and the amounts.

The **Mandates** has a  **Details** sub-tab shows the amount, identifiers like the PayU ID/UMRN Number and Merchant Transaction ID corresponding to the mandate on the top. You can also see the payment mode used, whether it’s Cards, Net Banking, or UPI. Also, the following sections display the various information:

- **Plan Details**: Provides subscription plan details: purpose, billing amount, billing cycle, and billing duration.
- **Payment Details**: Shows payment mode and instrument used:
  - **Card**: Last four digits, bank name, bank reference number.
  - **Enach**: Bank account number, bank name, bank reference number.
  - **UPI**: UPI ID, flow type.
- **Customer Details**: Includes customer information: name, email, mobile number, address.

To filter and view a mandate details:

1. Navigate to Subscriptions Dashboard and ensure that your are on **Mandates** tab.
2. Filter using any of the following fields on the top of the grid:
   - Subscription Created Date
   - Filter
   - Transaction ID
3. Click the drop-down or expandable menu for a mandate to view the details.


   <Image src="https://files.readme.io/e72831e78642d5a775c768a8a8f3e1258624cb1a2701548bd9bff95c8daf9b0e-dashboard-subscriptions-mandate-details.png" align="center" border={true} />

4. Select **View Details** from the **Actions** menu for the mandate that your wish to see the activity similar to the following screenshot:


<Image src="https://files.readme.io/be2f41972c972d7ec2672d1e3dd6d4b6d0f8351b7425e6f38b4bfbbc46312ba0-dashboard-subcitptions-mandate-actions-menu.png" align="center" border={true} />


5. Click the **Date** column header to sort recurring transactions in ascending or descending order based on the creation date.

The _Subscription Details_ page is displayed with the **Details** sub-tab selected.


<Image src="https://files.readme.io/a646071eadc9c2384deb59f1a0d8b8fbe55d28e541ceb9144dfd4ad3cd066d1e-dashboard-subscription-mandate-details.png" align="center" border={true} />


<br />

## View a Mandate Activity

The **Activity** sub-tab allows you to review a chronological timeline of all actions and events for a specific mandate. It displays key details at the top, including the amount, PayU ID/UMRN Number, and Merchant Transaction ID. Shows the payment mode used (Cards, Net Banking, or UPI). Provides a comprehensive view of the mandate’s history and progress. Also, it provides the following information:

- **Chronological Activity Log**: View all actions in the order they occurred. Step-by-step record of events since the mandate’s creation.
- **GMV Tracking**: Track the Gross Merchandise Value (GMV) received through the mandate. Clear view of the mandate’s financial performance.
- **Recurring Payment Count**: See the count of recurring payments completed under the mandate.

<Callout icon="📘" theme="info">
  ### Note:

  The recurring transaction is reflected on the **Activity** sub-tab after 30 mins from when the actual debit is attempted.
</Callout>

To view a mandate activity:

1. Navigate to Subscriptions Dashboard and ensure that your are on **Mandate** tab.
2. Select **View Details** from the **Actions** menu for the mandate that your wish to see the activity similar to the following screenshot:


<Image src="https://files.readme.io/be2f41972c972d7ec2672d1e3dd6d4b6d0f8351b7425e6f38b4bfbbc46312ba0-dashboard-subcitptions-mandate-actions-menu.png" align="center" border={true} />


The _Subscription Details_ page is displayed with the **Details** tab selected.

2. Select the **Activity** sub-tab.

The **Activity** sub-tab is displayed with the mandate activity similar to the following screenshot.


<Image src="https://files.readme.io/56dd5b9e20bdc31cc86291a903807813a3d25e7816a97374bb7d3c685ba9c861-dashboard-subscription-mandate-activity.png" align="center" border={true} />


<br />

## View Payments Received for a Mandate

The **Payments** sub-tab allows you to manage and review all recurring transactions linked to a mandate. You can filter, search, and download transaction details, ensuring you have a clear view of recurring transactions. This sub-tab provides the following to filter, search or sort:

- **Status-Based Filtering**: Filter transactions by status (Recurring Success or Recurring Failed).
- **Search Functionality**: Use the search bar to find transactions by Recurring PayU ID or Merchant Transaction ID.
- **Sorting Options**: Sort transactions by initiated date or amount in ascending or descending order.

To view payments received for a mandate:

1. Navigate to Subscriptions Dashboard and ensure that your are on **Mandate** tab.
2. Select **View Details** from the **Actions** menu for the mandate that your wish to see the activity similar to the following screenshot:


<Image src="https://files.readme.io/be2f41972c972d7ec2672d1e3dd6d4b6d0f8351b7425e6f38b4bfbbc46312ba0-dashboard-subcitptions-mandate-actions-menu.png" align="center" border={true} />


The _Subscription Details_ page is displayed with the **Details** tab selected.

2. Select the **Payments** tab.

The **Payments** tab is displayed with the payments received the for selected mandate similar to the following screenshot.


<Image src="https://files.readme.io/340d1cf5bbcbf24ac74a125cafe5239933b0c8ffa93b617560e6228fd725b956-dashboard-subscriptions-mandate-activity-pymts.png" align="center" border={true} />


<br />

## Download a Memo for a Bounced Transacton

For eNACH transactions that have failed, you can download a Bounce Memo.

To download a memo for failed transaction:

1. Navigate to Subscriptions Dashboard and ensure that your are on **Mandate** tab.
2. Select **View Details** from the **Action** menu for the eNACH mandate that your wish to download memo.

The _Subscription Details_ page is displayed with the **Details** tab selected.

3. Select the **Payments** tab.

The **Payments** tab is displayed with the payments received the for selected mandate similar to the following screenshot.


<Image src="https://files.readme.io/340d1cf5bbcbf24ac74a125cafe5239933b0c8ffa93b617560e6228fd725b956-dashboard-subscriptions-mandate-activity-pymts.png" align="center" border={true} />


4. Select **Bounce Memo** from the **Action** menu for the failed transaction for which bounce memo is required similar to the following screenshot:


<Image src="https://files.readme.io/822dac3b76bdbc6910d92a24e40fe7aff413f1a9b429034381932f05e90b071e-dashboard-subscriptions-mandate-activity-pymts-bounce-memo-menu.png" align="center" border={true} />


The bounce memo is downloaded. The file contents is similar to the following screenshot:


<Image src="https://files.readme.io/3735dc54f30e28d437cd91c66d801b418eab9a6cb203b4f1044cbd819e2c6d64-bounce_memo_sample.png" align="center" width="550px" border={true} />


<br />
