---
title: Integrate with Closed Looped Wallet
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
Closed-Loop wallets allow merchants to accept payments with their self-branded wallets. PayU’s SDK enables you to seamlessly integrate with a closed-loop wallet and start accepting payments.

<Callout icon="📘" theme="info">
  **Note**: You can enable Closed-Loop wallet payment mode from PayU’s Merchant Dashboard. Contact your PayU Key Account Manager if you do not see the payment mode on your PayU Dashboard.
</Callout>

## Prerequisites

1. Enable Closed-Loop Wallet from your Dashboard.
2. Build the payment parameters with the`walletURN` key in `additionalParam`.

## Workflow

The following screens show how Closed-Loop wallet payment works on the PayU payment page:

1. When you enable the Closed-Loop wallet for your account, your customer sees the Closed-Loop wallet payment on top of the payment page under the **Save Option** tab.
2. The closed-loop wallet balance is fetched and loaded by default.
3. If the balance is not loaded due to some error, an error message will be displayed (see the screenshot below). The customer can tap on the wallet option to reload the amount.
4. Once the balance is loaded the customer can make the payment by clicking Pay Now.
