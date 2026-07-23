---
title: APIs used in Integration
deprecated: false
hidden: false
icon: far fa-rectangle-api
metadata:
  title: APIs used in International Payments Integration
  robots: index
---
Use these APIs to identify international cards, collect international payments, and verify the transaction.

### Check the card

| Use case → Reference                               | `command` / primary value | Description                                                                                       |
| -------------------------------------------------- | ------------------------- | ------------------------------------------------------------------------------------------------- |
| [Check is Domestic API](ref:check_is_domestic_api) | `check_isDomestic`        | Determine whether the customer's card BIN is domestic or international before initiating payment. |

### Collect payment

| Use case → Reference                                                            | `command` / primary value | Description                                                                                                                    |
| ------------------------------------------------------------------------------- | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| [Collect Payment API – PayU Hosted Checkout](ref:_payment_payu_hosted_checkout) | `_payment`                | Initiate an international card payment on PayU Hosted Checkout, where PayU displays DCC conversion for an international card.  |
| [Collect Payment API – Merchant Hosted Checkout](ref:_payment_merchant_hosted)  | `_payment`                | Submit an international card payment with the relevant parameters, including optional `transactionCurrency` for MCC merchants. |

### Verify the payment

| Use case → Reference                         | `command` / primary value | Description                                                      |
| -------------------------------------------- | ------------------------- | ---------------------------------------------------------------- |
| [Verify Payment API](ref:verify_payment_api) | `verify_payment`          | Reconcile the transaction status from your server after payment. |

<br />
