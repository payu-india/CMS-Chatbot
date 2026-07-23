---
title: APIs used in Integration
deprecated: false
hidden: false
icon: far fa-rectangle-api
metadata:
  title: APIs used in TPV integration
  robots: index
---
Use these APIs to restrict payments to registered beneficiary accounts across checkout, recurring, and Payment Link TPV flows.

### Collect payment

| Use case → Reference                                                            | `command` / primary value | Description                                                                                      |
| ------------------------------------------------------------------------------- | ------------------------- | ------------------------------------------------------------------------------------------------ |
| [Collect Payment API – PayU Hosted Checkout](ref:_payment_payu_hosted_checkout) | `_payment`                | Initiate a TPV payment with `beneficiarydetail` on PayU Hosted Checkout.                         |
| [Collect Payment API – Merchant Hosted Checkout](ref:_payment_merchant_hosted)  | `_payment`                | Submit a merchant-hosted TPV request with `beneficiarydetail` for NetBanking, UPI, or NEFT/RTGS. |

### Recurring payments with TPV

| Use case → Reference                                           | `command` / primary value | Description                                                                          |
| -------------------------------------------------------------- | ------------------------- | ------------------------------------------------------------------------------------ |
| [Recurring Payment Transaction API](ref:recurring_payment_api) | `si_transaction`          | Execute recurring debits after successful UPI Autopay mandate registration with TPV. |

### Payment Links

| Use case → Reference                                                          | `command` / primary value           | Description                                                                  |
| ----------------------------------------------------------------------------- | ----------------------------------- | ---------------------------------------------------------------------------- |
| [Create Payment Link API](ref:create-payment-links)                           | `create_payment_links` scope        | Create a payment link with beneficiary account details for TPV verification. |
| [Get Access Token API for Payment Links](ref:get-token-api-for-payment-links) | OAuth scope: `create_payment_links` | Generate the OAuth token used to authenticate Payment Link API requests.     |

### General

| Use case → Reference                         | `command` / primary value | Description                                                                  |
| -------------------------------------------- | ------------------------- | ---------------------------------------------------------------------------- |
| [Validate VPA API](ref:validate_vpa_api)     | `validateVpa`             | Validate the customer's UPI handle before initiating UPI TPV or UPI Autopay. |
| [Verify Payment API](ref:verify_payment_api) | `verify_payment`          | Reconcile the transaction status from your server after payment.             |

<br />
