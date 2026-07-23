---
title: APIs used in Integration
deprecated: false
hidden: false
icon: far fa-rectangle-api
metadata:
  title: APIs used in Closed-Loop Wallet integration
  robots: index
---
---
title: APIs used in Integration
deprecated: false
hidden: false
icon: far fa-rectangle-api
metadata:
  title: APIs used in Closed-Loop Wallet integration
  robots: index
---
<br />

Use these APIs to manage closed-loop wallet customers, load funds, debit wallets, and retrieve transaction status and history.

### Manage customers

| Use case → Reference | `command` / primary value | Description |
| --- | --- | --- |
| [Register Customer API](ref:register-customer-api) | `POST /v1/wallet/enroll` | Onboard a customer and create a closed-loop wallet account. |
| [Retrieve Customer Record API](ref:retrieve-customer-record-api-1) | `POST /v1/wallet/retrieveCustRecord` | Fetch customer details and wallet balance before debit or load operations. |
| [Update Profile API – Closed Loop](ref:update-profile-api-closed-loop) | `PATCH /v1/wallet/onboarding/v3/updateProfile` | Update customer profile details for a closed-loop wallet. |
| [Change Wallet Status API](ref:change-wallet-status-api) | `PATCH /v1/wallet/onboarding/walletStatus` | Change the wallet status for a customer account. |

### Load funds

| Use case → Reference | `command` / primary value | Description |
| --- | --- | --- |
| [PG Load API](ref:pg-load-api) | `POST /ppi/payment/pg-load/v1` | Initiate a wallet top-up through the payment gateway. |
| [PG Load Enquiry API](ref:pg-load-enquiry-api) | `POST /ppi/payment/pg-load/enquiry/v1` | Check the status of a PG Load transaction during the top-up journey. |
| [Load API – Closed Loop Wallet](ref:load-api-closed-loop-wallet) | `PATCH /v1/wallet/load-account` | Credit the wallet after a successful payment gateway transaction. |
| [Check Status API – CLW](ref:check-status-api-clw) | `POST /v1/wallet/check-status` | Check the status of a load transaction in the top-up journey. |

### Debit the wallet

| Use case → Reference | `command` / primary value | Description |
| --- | --- | --- |
| [Seamless Debit Transaction API](ref:collect-payment-api-card-seamless) | `_payment` | Debit the wallet through a server-to-server request without user redirection. |
| [Non-Seamless Debit Transaction API](ref:non-seamless-debit-transaction-api) | `_payment` | Debit the wallet through PayU Hosted Checkout with user authorization. |
| [Seamless Debit Enquiry API](ref:seamless-debit-enquiry-api) | `_payment` | Check the status of a seamless debit transaction. |
| [Load and Pay Transaction API](ref:load-and-pay-transaction-api) | `_payment` | Load funds and debit the wallet in one request when the balance is insufficient. |
| [Collect Payment API – PayU Hosted Checkout](ref:_payment_payu_hosted_checkout) | `_payment` | Redirect customers to PayU Hosted Checkout for wallet debit or load-and-pay flows. |

### Enquiries

| Use case → Reference | `command` / primary value | Description |
| --- | --- | --- |
| [Statement Inquiry API – CLW](ref:statement-inquiry-api-clw) | `POST /v1/wallet/statement-inquiry` | Fetch wallet transaction history for a date range. |
| [Verify Payment API](ref:verify_payment_api) | `verify_payment` | Reconcile wallet load or payment gateway transaction status from your server. |

<br />

<Callout icon="📘" theme="info">
  **Note**: To unload your wallet, refer to [Seamless Debit Integration - CLW](doc:seamless-wallet-debit-integration-clw) or [PayU Hosted Check-out Integration - CLW](https://docs.payu.in/docs/pay-hosted-checkout-merchant-integration-merchant-wallet) based on the integration.
</Callout>

<br />