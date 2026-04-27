---
title: Refund Wallet Dashboard
deprecated: false
hidden: false
metadata:
  robots: index
---
The Refund Wallet allows you to manage, recharge, and configure your refund funds for faster and more transparent refund processing. This guide walks you through activating, configuring, recharging, and monitoring your Refund Wallet.

<Callout icon="📘" theme="info">
  **Funds cannot be withdrawn**: Pre‑funding withdrawals are not permitted under RBI PA‑PG guidelines (refer to RBI circular no. RBI/DPSS/2025-26/141CO.DPSS.POLC.No.S-633/02-14-008/2025-26).The transferred funds must be used only for their intended purpose or for future refunds.
</Callout>

<Callout icon="📘" theme="info">
  **Notes**:

  * Refund Wallet is currently available to all normal merchants (excluding split settlement merchants and MCC merchants).
  * You must only use your Settlement-linked account for adding funds.
  * PayU suggests you regularly monitor your wallet balance and set up notifications to avoid refund delays.
</Callout>

## Activate Refund Wallet

To activate your refund wallet if not already activated:

1. Navigate to **Settings** > **Preferences** > **Refund Wallet** tab.
2. Click **Activate Now**.

OR

Click **Know More** in the ad similar to following screenshot and then click **Activate Now**.

<Image align="center" alt="Activate Refund Wallet on Dashboard" src="https://files.readme.io/ffece402fa25ae70215a023ba438920f2b4970c7cb6aad1e647fa73cd60f2ea3-dashboard_refund_wallets_activate_ad.png" />

<Callout icon="📘" theme="info">
  **Note**: After the refund wallet is activated, you can set the refund wallet priority. For more information, refer to [Configure Refund Wallet](https://docs.payu.in/docs/refund-wallet-dashboard#configure-refund-wallet).
</Callout>

## Add Funds to Refund Wallet

To add funds to your refund wallet:

1. Navigate to **Explore Products** and navigate to **Settlement & Refund Upgrades**section.

<Image align="center" alt="Explore PayU > Post Payment tab" border={true} src="https://files.readme.io/bbd4ccd0737b82d2c81eaec9037c89c3344cc3e64bbad84df5eabd805a864dff-Screenshot_2026-04-24_at_3.28.32_PM.png" className="border" />

2. Select the **Refund Wallet** tile.
3. Click the **Add Funds** button.

   A popup page is displayed listing the VA, IFSC, and beneficiary details.

<Image align="center" alt="Refund Wallets > Add Fund Popup Page" src="https://files.readme.io/658c821c585d8fcff00edb08f03b10d2e57b53942837a0ef7c001d8db9dbc813-dashboard_refund_wallets_add_fund_popup.png" />

4. Transfer funds from your Settlement-linked account.

<Callout icon="📘" theme="info">
  **Notes**:

  * Funds added to the Refund Wallet **cannot be withdrawn** from PayU Escrow and are used only for processing refunds.
  * Transfer funds from your Settlement-linked account only. Amounts transferred from other accounts will be rejected.
</Callout>

## Configure Refund Wallet

After activation, to configure your wallet:

1. Navigate to **Settings** > **Preferences** > **Refund Wallet** tab.

<Image align="center" alt="Configure Refund Wallet Preferences" border={true} src="https://files.readme.io/ed8a7ba9dea85137ee14bf4b03ab276843514b8dc9f9eb35e5bfe14cc17b5e97-dashboard_refund_wallets_preferences.png" className="border" />

2. Perform any of the following:

* **Threshold Limit**: Set a threshold limit for minimum balance. For more information, refer to [Configure Thresholds and Notifications](https://docs.payu.in/?isFramePreview=true#configure-thresholds-and-notifications).
* **Email Notifications**: Enable email notifications for low balance alerts. For more information, refer to [Configure Thresholds and Notifications](https://docs.payu.in/?isFramePreview=true#configure-thresholds-and-notifications).
* **Payment Link Reminders**: Configure the payment link reminders before number of days when it will expire. For more information, refer to [Configure Payment Link Reminders](https://docs.payu.in/?isFramePreview=true#configure-payment-link-reminders)

### Configure Thresholds and Notifications

To configure wallet threshold amount and email notifications:

1. In the **Set default priority** field, select any of the following:
   * **Refund wallet when settlement is not enough**: Refund Wallet balance will be used to process refunds to your customers when you do not have enough settlement funds.
   * **Refund wallet always**: Refund Wallet balance will always be used to process refunds to your customers. Refund processed via this option will be present in the refund wallet statement but not in settlement MIS.
2. Enter the threshold limit amount in the **Set low balance limit** field to get notified when your wallet balance is low.
3. Click **Set Notification**.

The _Customer Notifications_ page is displayed.

4. Select the **Refund Wallet** tab.
5. Update the email for notifications.

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
