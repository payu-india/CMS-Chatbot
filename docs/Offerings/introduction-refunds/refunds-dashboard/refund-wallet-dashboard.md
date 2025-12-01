---
title: Refund Wallet Dashboard
deprecated: false
hidden: true
metadata:
  robots: index
---
The Refund Wallet allows you to manage, recharge, and configure your refund funds for faster and more transparent refund processing. This guide walks you through activating, configuring, recharging, and monitoring your Refund Wallet.

<Callout icon="📘" theme="info">
  **Notes**:

  * Refund Wallet is currently available to available to all normal merchants (excluding split settlement merchants, MCC merchants, FK, Amazon, and Myntra).
  * You must only use your Settlement-linked account for adding funds.
  * Funds in the Refund Wallet are non-withdrawable and strictly for refunds.
  * PayU suggests you regularly monitor your wallet balance and set up notifications to avoid refund delays.
</Callout>

## Activate Refund Wallet

Activate your refund wallet if not already activated:

1. Navigate to **Settings** > **Preferences** > **Refund Wallet** tab.
2. Click **Activate Now**.

OR

   Click **Know More** in the ad similar to following screenshot and then click **Activate Now**.

<Image align="center" border={false} src="https://files.readme.io/ffece402fa25ae70215a023ba438920f2b4970c7cb6aad1e647fa73cd60f2ea3-dashboard_refund_wallets_activate_ad.png" />

<Callout icon="📘" theme="info">
  **Note**: After the refund wallet is activated, you can set the refund wallet priority. For more information, refer to [Configure Refund Wallet](https://docs.payu.in/docs/refund-wallet-dashboard#configure-refund-wallet).
</Callout>

## Add Funds to Refund Wallet

1. Navigate to **Explore Pay** > **Post Payments** tab.

<Image align="center" alt="Explore PayU > Post Payment tab" border={true} src="https://files.readme.io/4f0a2e60bcb9623a6e337bb1099c984a283a1d513f5122a60956a411aca1e61f-dashboard_explore_payu_post_payments_tab.png" className="border" />

2. Select the **Refund Wallet** tile.
3. Click the **Add Funds** button.

   A popup page is displayed listing the VA, IFSC, and beneficiary details.

<Image align="center" alt="Refund Wallets Add Fund Popup Page" border={false} src="https://files.readme.io/658c821c585d8fcff00edb08f03b10d2e57b53942837a0ef7c001d8db9dbc813-dashboard_refund_wallets_add_fund_popup.png" />

<Callout icon="📘" theme="info">
  **Note**: Transfer funds from your Settlement-linked account only. Amounts transferred from other accounts will be rejected.
</Callout>

4. Transfer funds from your Settlement-linked account.

<Callout icon="📘" theme="info">
  **Notes**:  Funds added to the Refund Wallet **cannot be withdrawn** from PayU Escrow and are used only for processing refunds.
</Callout>

## Configure Refund Wallet

After activation, configure your wallet:

1. Navigate to **Settings** > **Preferences** > **Refund Wallet** tab.

<Image align="center" border={true} src="https://files.readme.io/ed8a7ba9dea85137ee14bf4b03ab276843514b8dc9f9eb35e5bfe14cc17b5e97-dashboard_refund_wallets_preferences.png" className="border" />

2. Perform any of the following:

* **Wallet Priority**: Set refund wallet priority (choose which wallet is used first for refunds).
* **Threshold Limit**: Set a threshold limit for minimum balance. Fo
* **Notifications**: Enable notifications (email/SMS) for low balance alerts.

### Configure Thresholds and Notifications

1. In the **Set default priority** field, select any of the following:
   * **Refund wallet when settlement is not enough**: Refund Wallet balance will be used to process refunds to your customers when you do not have enough settlement funds.
   * **Refund wallet always**: Refund Wallet balance will always be used to process refunds to your customers. Refund processed via this option will be present in the refund wallet statement but not in settlement MIS.
2. Enter the threshold limit amount in the **Set low balance limit** field to get notified when your wallet balance is low.
3. Click **Set Notification**. 

  The Customer Notifications page is displayed.

4. Select the **Refunds** tab.

<Image align="center" border={true} src="https://files.readme.io/18703b0ca7316b87ccab5588e851e255d3c33222c8a7bf8ba2b597e8be855dba-dashboard_refunds_notifications.png" className="border" />

5. Update the email for notifications.

### Configure Payment Link Reminders

To configure the payment link reminders:

1. Navigate to **Payment Link Reminders** tab.

<Image align="center" border={true} width="450px" src="https://files.readme.io/f6a2cc98dd97b08179651b225618e34fab83046bac856016dc826f7ef9edd43d-dashboard_explore_refund_wallets_payment_link_reminders.png" className="border" />

2. In the **For links with an expiry date** field,  enter the days before expiry when the reminder must be sent.
3. In the **For links without any expiry date** field, remove number of days before expiry or retain all of them.

## View Refund Wallet Ledger

The Refund Wallet Ledger offers:

* View available balance.
* See count of refunds processed in a selected date range.
* Full ledger (debit/credit) with PayuID and UTR numbers.
* Download ledger as CSV/Excel.
* Filter ledger by Credit/Debit and Source.
* Refund tab includes a source column for refund debit source.
* Download reports:
  * Successful refunds via wallet
  * Failed refunds due to insufficient balance
  * Refunds stuck due to insufficient balance
* Dashboard alerts for refunds stuck due to insufficient balance.

<br />
