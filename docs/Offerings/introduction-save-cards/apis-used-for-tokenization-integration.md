---
title: APIs used for Integration
deprecated: false
hidden: false
icon: far fa-square-half-stroke-horizontal
metadata:
  title: APIs used for Tokenization Integration
  robots: index
---
Use these APIs to tokenize cards with the selected vault model, pay with saved cards, manage tokens, and verify payments.

### Model 1

| Use case → Reference                                                            | `command` / primary value | Description                                                                                                    |
| ------------------------------------------------------------------------------- | ------------------------- | -------------------------------------------------------------------------------------------------------------- |
| [Collect Payment API – PayU Hosted Checkout](ref:_payment_payu_hosted_checkout) | `_payment`                | Initiate first-time or repeat card payments on PayU Hosted Checkout with vault consent and `user_credentials`. |

### Model 2

| Use case → Reference                                                                                   | `command` / primary value | Description                                                                                                   |
| ------------------------------------------------------------------------------------------------------ | ------------------------- | ------------------------------------------------------------------------------------------------------------- |
| [Model 2 – Zero Code Change for Vault Integration](ref:model-2-zero-code-change-for-vault-integration) | `_payment`                | Tokenize a card during the first payment with customer consent while PayU manages token creation and storage. |
| [Get User Cards API](ref:get_user_cards_api)                                                           | `get_user_cards`          | Retrieve a customer's tokenized cards for display at checkout.                                                |
| [Process Transaction with a Saved Card](ref:process-transaction-with-a-saved-card)                     | `_payment`                | Initiate a repeat payment using a stored PayU vault token.                                                    |
| [Collect Payment API – Merchant Hosted Checkout](ref:_payment_merchant_hosted)                         | `_payment`                | Submit merchant-hosted card payment requests with saved-card or token parameters.                             |

### Model 3

| Use case → Reference                                                       | `command` / primary value   | Description                                                                         |
| -------------------------------------------------------------------------- | --------------------------- | ----------------------------------------------------------------------------------- |
| [Save a Card API](ref:save_card_api)                                       | `save_payment_instrument`   | Create a card token after a successful payment.                                     |
| [Get User Cards API – Model 3](ref:get_user_cards_api_model3)              | `get_payment_instrument`    | Retrieve saved card tokens created through Model 3 APIs.                            |
| [Get Payment Details (Cryptogram) API](ref:get_payment_details_cryptogram) | `get_payment_details`       | Fetch the TAVV or cryptogram for a PayU or network token before initiating payment. |
| [Edit a Tokenized Card API](ref:edit_saved_card_api)                       | `edit_payment_instrument`   | Update a stored card token when the customer changes card details.                  |
| [Delete a Tokenized Card API](ref:delete_saved_card_api)                   | `delete_payment_instrument` | Delete a stored card token for customer consent management.                         |

### General

| Use case → Reference                         | `command` / primary value | Description                                                      |
| -------------------------------------------- | ------------------------- | ---------------------------------------------------------------- |
| [Verify Payment API](ref:verify_payment_api) | `verify_payment`          | Reconcile the transaction status from your server after payment. |

<br />
